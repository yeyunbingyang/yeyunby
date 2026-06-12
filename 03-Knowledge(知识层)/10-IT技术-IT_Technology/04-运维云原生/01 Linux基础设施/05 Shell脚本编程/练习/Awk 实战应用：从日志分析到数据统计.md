## **场景一：Web服务器日志分析（Nginx/Apache）**

这是 awk 最经典的应用。假设你有一行 Nginx 访问日志：

```
192.168.1.100 - - [15/Apr/2026:10:00:01 +0800] "GET /api/user?id=123 HTTP/1.1" 200 1234 "https://example.com" "Mozilla/5.0"
```

|   |   |   |
|---|---|---|
|任务|命令|说明|
|**1. 统计状态码分布**|`awk '{status_count[$9]++} END {for (s in status_count) print s, status_count[s]}' access.log`|`$9`是状态码。统计每个状态码（200、404、500等）的出现次数|
|**2. 找出访问最频繁的IP**|`awk '{ip_count[$1]++} END {for (ip in ip_count) print ip_count[ip], ip}' access.log \| sort -nr \| head -10`|`$1`是客户端IP。按访问量倒序取Top 10|
|**3. 统计每个URL的访问量**|`awk '{url_count[$7]++} END {for (url in url_count) print url_count[url], url}' access.log \| sort -nr`|`$7`是请求的URL路径|
|**4. 计算总流量**|`awk '{sum+=$10} END {print "总传输字节:", sum/1024/1024, "MB"}' access.log`|`$10`是响应体大小（字节），统计网站总出流量|
|**5. 分析特定时间段的请求**|`awk '/15\/Apr\/2026:14:/{print $0}' access.log \| wc -l`|筛选包含“15/Apr/2026:14:”的行，统计14时段的请求数|

---

## **场景二：系统监控与故障排查**

**案例：检查磁盘空间告警**

```
# 提取磁盘使用率超过80%的分区
df -h | awk 'NR>1 && $5+0 > 80 {print "警告: "$1" 使用率 "$5}'
```

- `NR>1`：跳过第一行标题
- `$5+0`：将“75%”这样的字符串转换为数字75
- 直接嵌入到监控脚本中，定时运行

**案例：分析进程内存占用**

```
# 找出内存占用最高的前5个进程
ps aux | awk 'NR>1 {print $4, $11}' | sort -nr | head -5
```

- `$4`是内存百分比，`$11`是命令名

---

## **场景三：CSV/TSV 数据处理**

假设有一个员工薪资表 `salary.csv`（逗号分隔）：

```
name,department,salary,bonus
张三,技术部,15000,3000
李四,市场部,12000,2000
王五,技术部,18000,4000
```

|   |   |   |
|---|---|---|
|任务|命令|说明|
|**1. 计算技术部平均薪资**|`awk -F',' '$2=="技术部" {sum+=$3; count++} END {print "平均薪资:", sum/count}' salary.csv`|先筛选部门，再累加计算|
|**2. 给每人加薪10%并输出新表**|`awk -F',' 'BEGIN {OFS=","; print "name,department,new_salary"} NR>1 {print $1,$2,$3*1.1}' salary.csv`|使用 `OFS` 设置输出分隔符，`NR>1` 跳过标题行|
|**3. 统计各部门薪资总额**|`awk -F',' 'NR>1 {dept_sum[$2]+=$3} END {for(d in dept_sum) print d, dept_sum[d]}' salary.csv`|使用数组进行分组统计|

---

## **场景四：配置文件提取与转换**

**案例：从** `/etc/passwd` **提取用户列表**

```
# 提取所有用户名和对应的shell
awk -F':' '{print $1, "->", $7}' /etc/passwd
```

- `/etc/passwd` 以冒号分隔，第1列是用户名，第7列是登录shell

**案例：生成 K8s ConfigMap 的 YAML 片段**

```
# 将 .env 文件转换为 K8s ConfigMap 的 data 部分
awk 'BEGIN {print "data:"} /^[^#]/ && NF>0 {print "  "$1": \""$2"\""}' .env
```

输入 `.env`：

```
DB_HOST=localhost
DB_PORT=3306
```

输出：

```
data:
  DB_HOST: "localhost"
  DB_PORT: "3306"
```

---

## **场景五：实时日志监控与报警**

将 awk 嵌入到 `tail -f` 管道中，实现实时分析：

```
# 实时监控日志，发现错误立即报警
tail -f /var/log/app/error.log | awk '/ERROR/ {print "[CRITICAL]", $0; system("echo \"发现错误\" | mail -s \"报警\" admin@example.com")}'
```

```
# 实时统计接口QPS（每60秒输出一次）
tail -f access.log | awk -v interval=60 '
BEGIN {start=systime(); req_count=0}
{
  req_count++
  now=systime()
  if(now - start >= interval) {
    print strftime("%Y-%m-%d %H:%M:%S"), "QPS:", req_count/interval
    req_count=0
    start=now
  }
}'
```

这里使用了 `systime()` 获取时间戳，`strftime()` 格式化时间输出[[2]]。

---

## **场景六：复杂文本报告生成**

**案例：从散乱的日志中生成整洁的日报**

```
awk '
# 初始化：设置月份映射和标题
BEGIN {
  month_map["Jan"]="01"; month_map["Apr"]="04";
  print "日期,访问量,异常数,平均响应时间"
}
# 解析每行日志
{
  # 提取日期（假设日志格式中有[15/Apr/2026:...]）
  split($4, date_part, "[/:]")
  date = date_part[3]"-"month_map[date_part[2]]"-"date_part[1]
  
  # 统计
  visits[date]++
  if ($9 >= 500) errors[date]++
  if ($NF ~ /ms/) {
    # 假设最后一列有响应时间如 "rt=123ms"
    split($NF, rt, "=")
    response_time[date] += substr(rt[2], 1, length(rt[2])-2)
    rt_count[date]++
  }
}
# 结束：输出CSV格式的报告
END {
  for (d in visits) {
    avg_rt = (rt_count[d] > 0) ? response_time[d]/rt_count[d] : 0
    print d","visits[d]","errors[d]","avg_rt
  }
}' /var/log/nginx/access.log
```

---

## **实用技巧与注意事项**

1. **先预览再操作**：用 `head` 命令先看几行数据，确认字段位置。

```
head -5 file.log | awk '{print NF, "列:", $0}'
```

2. **分隔符不确定时**：使用 `-F"[ :]+"` 这样的正则，表示“一个或多个空格或冒号”。
3. **处理大文件**：awk 本身很高效，但避免在循环中调用外部命令（如 `system()`）。
4. **与其它命令配合**：

```
# 经典组合：grep过滤 → awk提取 → sort排序 → uniq统计
grep "ERROR" app.log | awk '{print $4}' | sort | uniq -c | sort -nr
```

5. **保存常用命令**：将复杂的 awk 脚本保存为 `.awk` 文件，通过 `awk -f script.awk data.txt` 调用。

**核心思想**：在实际工作中，awk 很少单独使用，它通常是**文本处理流水线**的核心环节，负责**结构化提取**和**计算**，再结合 `sort`、`uniq`、`grep`、`xargs` 等命令完成完整任务。掌握这些真实案例，你就能用几行命令解决原本需要写脚本的问题。