---

# 🔍 一、基础过滤（1～10）

---

### 1️⃣ 查关键词

```
grep "error" app.log
```

---

### 2️⃣ 忽略大小写

```
grep -i "error" app.log
```

---

### 3️⃣ 显示行号⭐

```
grep -n "error" app.log
```

---

### 4️⃣ 统计出现次数⭐

```
grep -c "error" app.log
```

---

### 5️⃣ 反向匹配（排除）

```
grep -v "info" app.log
```

---

### 6️⃣ 多关键词（或）

```
grep -E "error|fail" app.log
```

---

### 7️⃣ 精确匹配单词

```
grep -w "root" /var/log/secure
```

---

### 8️⃣ 匹配开头

```
grep "^ERROR" app.log
```

---

### 9️⃣ 匹配结尾

```
grep "timeout$" app.log
```

---

### 🔟 匹配空行注释⭐

```
# 匹配空行
grep "^$" app.log 

grep -E "^\s*$|^\s*#" app.log
```

---

# 🔎 二、正则进阶（11～20）

---

### 1️⃣1️⃣ 匹配数字

```
grep -P "\d+" app.log
```

---

### 1️⃣2️⃣ 匹配IP地址

```
grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" app.log
```

---

### 1️⃣3️⃣ 匹配手机号

```
grep -E "^1[3-9][0-9]{9}$" file
```

---

### 1️⃣4️⃣ 匹配邮箱

```
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}" file
```

---

### 1️⃣5️⃣ 匹配URL

```
grep -E "https?://[a-zA-Z0-9./?=_-]+" file
```

---

### 1️⃣6️⃣ 匹配连续3位数字

```
grep -E "[0-9]{3}" file
```

---

### 1️⃣7️⃣ 匹配非数字

```
grep -P "\D+" file
```

---

### 1️⃣8️⃣ 提取时间（HH:MM:SS）

```
grep -E "[0-9]{2}:[0-9]{2}:[0-9]{2}" app.log
```

---

### 1️⃣9️⃣ 匹配重复字符

```
grep -E "(.)\1" file
```

---

### 2️⃣0️⃣ 匹配以字母开头的行

```
grep -E "^[a-zA-Z]" file
```

---

# 🚀 三、运维实战（重点🔥 21～30）

---

### 2️⃣1️⃣ 查登录失败

```
grep "Failed password" /var/log/secure
```

---

### 2️⃣2️⃣ 查成功登录

```
grep "Accepted" /var/log/secure
```

---

### 2️⃣3️⃣ 查某IP访问日志

```
grep "192.168.1.1" access.log
```

---

### 2️⃣4️⃣ 统计某IP访问次数

```
grep "192.168.1.1" access.log | wc -l
```

---

### 2️⃣5️⃣ 找访问最多的IP（Top10🔥）

```
grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log | sort | uniq -c | sort -nr | head
```

---

### 2️⃣6️⃣ 查404错误

```
grep " 404 " access.log
```

---

### 2️⃣7️⃣ 查5xx服务器错误

```
grep -E " 5[0-9]{2} " access.log
```

---

### 2️⃣8️⃣ 查响应时间超过1秒（假设日志有 time）

```
grep -E "time=[1-9]" access.log
```

---

### 2️⃣9️⃣ 查最近日志（结合 tail）

```
tail -f app.log | grep "error"
```

---

### 3️⃣0️⃣ 多条件过滤（同时匹配🔥）

```
grep "error" app.log | grep "timeout"
```

👉 或更高级👇

```
grep -E "error.*timeout" app.log
```

---

# 🧠 面试级总结

👉 **grep = 查日志核心工具**

👉 **-E 解决80%问题，-P处理复杂场景**

👉 **组合拳最强：grep + sort + uniq + wc**

---

# ⚠️ 高级技巧（加分）

### 🔹 只输出匹配内容

```
grep -o "error" file
```

---

### 🔹 显示上下文

```
grep -A 3 -B 3 "error" file
```

---

# ✅ 一句话记忆

👉 **grep不是单用，而是“日志分析流水线”的核心工具**

---