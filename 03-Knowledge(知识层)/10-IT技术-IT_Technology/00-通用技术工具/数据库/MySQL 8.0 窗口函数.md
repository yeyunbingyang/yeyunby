
---

## 一、基础环境准备（实践）

### 1.1 数据库生命周期管理

```sql
-- 删除已存在的数据库（避免重复创建报错）
DROP DATABASE IF EXISTS D04;

-- 创建新数据库
CREATE DATABASE D04;

-- 切换使用数据库
USE D04;

-- 查看当前数据库中的所有表
SHOW TABLES;
```

### 1.2 建表：员工表设计

```sql
CREATE TABLE employ (
    employID    INT PRIMARY KEY,           -- 员工ID
    ename       VARCHAR(50),               -- 员工姓名
    deptID      INT,                       -- 部门ID
    salary      DECIMAL(10, 2)             -- 工资：总长度10位，保留2位小数
);
```

### 1.3 数据类型深度解析：DECIMAL vs FLOAT vs DOUBLE

| 类型               | 精度        | 适用场景          | 示例                          |
| ---------------- | --------- | ------------- | --------------------------- |
| **DECIMAL(M,D)** | **精确无误差** | 金额、工资等需精确计算   | `DECIMAL(10,2)`：最多8位整数+2位小数 |
| **FLOAT**        | 小数点后约7位   | 非高精度科学计算      | 存在微小精度误差                    |
| **DOUBLE**       | 小数点后约15位  | 需要较高精度但允许微小误差 | 精度比FLOAT高但仍非精确              |

**DECIMAL(M,D) 详解：**
- **M**：数字总长度（整数位 + 小数位）
- **D**：小数点后的位数

```sql
DECIMAL(5,1):  1234.5  ✓ 合法（总长5位，1位小数）
               123456.7 ✗ 非法（总长超过5位）
```

> 💡 **为什么工资用 DECIMAL？** 工资、金额等不允许精度误差，必须用定点数。

---

## 二、窗口函数理论核心

### 2.1 什么是窗口函数？

> **窗口函数是 MySQL 8.0 的新特性**，MySQL 5.x 不支持。
> 
> **本质**：给表**新增一列**，新增内容取决于使用的具体函数。
> 
> **特点**：不减少原表行数，只是为每行附加计算结果。

### 2.2 基础语法结构

```sql
窗口函数 OVER (
    [PARTITION BY 分组字段]        -- 类似于 GROUP BY，但保留所有行
    [ORDER BY 排序字段 ASC/DESC]    -- 组内排序
)
```

### 2.3 窗口函数分类

| 类别      | 函数                                  | 说明                    |
| ------- | ----------------------------------- | --------------------- |
| **聚合类** | `SUM`, `COUNT`, `MAX`, `MIN`, `AVG` | 在窗口内做聚合计算             |
| **排序类** | `ROW_NUMBER`, `RANK`, `DENSE_RANK`  | 对数据进行排名               |
| **分桶类** | `NTILE(N)`                          | 将数据分为 N 等份            |
| **偏移类** | `LAG`, `LEAD`                       | 取前/后 N 行的值（连续签到、趋势分析） |
| **首尾类** | `FIRST_VALUE`, `LAST_VALUE`         | 取窗口内第一个/最后一个值         |

> 🎯 **初学者建议**：先重点掌握 `ROW_NUMBER`、`RANK`、`DENSE_RANK` 三个排序函数。

---

## 三、三大排序函数：理论详解 + 实践对比

### 3.1 理论对比

| 函数               | 相同值处理    | 后续排名         | 记忆口诀     |
| ---------------- | -------- | ------------ | -------- |
| **ROW_NUMBER()** | 不并列，强制编号 | 不跳跃          | "行号，不重复" |
| **RANK()**       | 并列同排名    | **跳跃**（跳名次）  | "有跳，同排名" |
| **DENSE_RANK()** | 并列同排名    | **连续**（不跳名次） | "无跳，同排名" |

### 3.2 实践对比：数据演示

**假设数据（部门10）：**
```sql
INSERT INTO employ VALUES 
(1, '刘备', 10, 25000.00),
(2, '关羽', 10, 18000.00),
(3, '张飞', 10, 18000.00),  -- 与关羽同薪资
(4, '赵云', 10, 15000.00);
```

**查询三种排序结果：**
```sql
SELECT 
    employID,
    ename,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn,
    RANK() OVER (ORDER BY salary DESC) AS rk,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS drk
FROM employ
WHERE deptID = 10;
```

**输出结果：**

| employID | ename | salary | ROW_NUMBER | RANK | DENSE_RANK |
| -------- | ----- | ------ | ---------- | ---- | ---------- |
| 1        | 刘备    | 25000  | 1          | 1    | 1          |
| 2        | 关羽    | 18000  | 2          | 2    | 2          |
| 3        | 张飞    | 18000  | 3          | 2    | 2          |
| 4        | 赵云    | 15000  | 4          | 4    | 3          |

**关键观察：**
- `ROW_NUMBER`：关羽第2，张飞第3（不并列）
- `RANK`：关羽张飞并列第2，赵云跳到第4（**跳跃**）
- `DENSE_RANK`：关羽张飞并列第2，赵云是第3（**连续**）

---

## 四、PARTITION BY：分组窗口（理论+实践）

### 4.1 理论：PARTITION BY vs GROUP BY

|          | `GROUP BY`    | `PARTITION BY`     |
| -------- | ------------- | ------------------ |
| **作用**   | 将数据分组后聚合      | 将数据分组后计算           |
| **结果行数** | **压缩**，每组返回1行 | **保持原行数**，每行附加计算结果 |
| **类比**   | 汇总统计          | 给每行打标签             |

### 4.2 实践：按部门分组排名

```sql
-- 每个部门内部，按薪资降序排名
SELECT 
    employID,
    ename,
    deptID,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY deptID        -- 按部门切分窗口
        ORDER BY salary DESC       -- 每个窗口内独立排序
    ) AS dept_rn
FROM employ;
```

**理解要点：**
- `PARTITION BY deptID` → 把数据切成多个独立"窗口"（每个部门一个窗口）
- `ORDER BY salary DESC` → 每个窗口内部各自排序
- 结果中每个部门都有自己的 1, 2, 3... 排名

---

## 五、经典实战：分组取 Top N（理论+完整实践）

### 5.1 需求分析

> **需求**：查询每个部门薪资最高的 **前 2 名员工**。
> 
> 假设有 3 个部门，每组取 2 人，最终返回 **6 条记录**。

### 5.2 传统 SQL 的困境

用传统子查询实现：
- 需要复杂的关联查询或变量技巧
- 代码冗长，可读性差
- 性能不佳

### 5.3 窗口函数方案（核心代码）

```sql
SELECT * 
FROM (
    SELECT 
        employID,
        ename,
        deptID,
        salary,
        RANK() OVER (
            PARTITION BY deptID 
            ORDER BY salary DESC
        ) AS rk
    FROM employ
) t 
WHERE rk <= 2;
```

### 5.4 为什么必须嵌套子查询？（重要理论）

```sql
-- ❌ 错误写法：直接 WHERE 筛选窗口函数结果
SELECT 
    employID, ename, deptID, salary,
    RANK() OVER (PARTITION BY deptID ORDER BY salary DESC) AS rk
FROM employ
WHERE rk <= 2;  
-- 报错！因为 rk 是窗口函数生成的列，不属于原表字段
-- SQL 执行顺序：WHERE 在 SELECT 之前执行，此时 rk 还未生成

-- ✅ 正确写法：子查询包裹后外层筛选
SELECT * FROM (
    SELECT *, RANK() OVER (...) AS rk FROM employ
) t WHERE rk <= 2;
-- 子查询先执行，rk 列已生成，外层 WHERE 可以正常筛选
```

### 5.5 完整可运行脚本

```sql
-- ==========================================
-- 完整环境准备
-- ==========================================
DROP DATABASE IF EXISTS D04;
CREATE DATABASE D04;
USE D04;

CREATE TABLE employ (
    employID INT PRIMARY KEY,
    ename VARCHAR(50),
    deptID INT,
    salary DECIMAL(10, 2)
);

-- ==========================================
-- 插入测试数据（3个部门，共10人）
-- ==========================================
INSERT INTO employ VALUES 
(1, '刘备', 10, 25000.00),   -- 部门10
(2, '关羽', 10, 18000.00),   -- 部门10
(3, '张飞', 10, 18000.00),   -- 部门10（与关羽同薪）
(4, '赵云', 10, 15000.00),   -- 部门10
(5, '曹操', 20, 30000.00),   -- 部门20
(6, '司马懿', 20, 22000.00), -- 部门20
(7, '张辽', 20, 20000.00),   -- 部门20
(8, '孙权', 30, 20000.00),   -- 部门30
(9, '周瑜', 30, 19000.00),   -- 部门30
(10, '陆逊', 30, 19000.00);  -- 部门30（与周瑜同薪）

-- ==========================================
-- 步骤1：查看原始数据
-- ==========================================
SELECT * FROM employ;

-- ==========================================
-- 步骤2：全局薪资排名（不分组）
-- ==========================================
SELECT 
    employID, ename, deptID, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM employ;

-- ==========================================
-- 步骤3：部门内薪资排名（PARTITION BY）
-- ==========================================
SELECT 
    employID, ename, deptID, salary,
    ROW_NUMBER() OVER (PARTITION BY deptID ORDER BY salary DESC) AS rn,
    RANK() OVER (PARTITION BY deptID ORDER BY salary DESC) AS rk,
    DENSE_RANK() OVER (PARTITION BY deptID ORDER BY salary DESC) AS drk
FROM employ;

-- ==========================================
-- 步骤4：分组取 Top 2（最经典用法）
-- ==========================================
-- 方案A：使用 RANK()（并列不占名额）
SELECT * FROM (
    SELECT 
        employID, ename, deptID, salary,
        RANK() OVER (PARTITION BY deptID ORDER BY salary DESC) AS rk
    FROM employ
) t WHERE rk <= 2;

-- 方案B：使用 ROW_NUMBER()（每组恰好2条，不并列）
SELECT * FROM (
    SELECT 
        employID, ename, deptID, salary,
        ROW_NUMBER() OVER (PARTITION BY deptID ORDER BY salary DESC) AS rn
    FROM employ
) t WHERE rn <= 2;

-- 方案C：使用 DENSE_RANK()（并列不占名额，排名连续）
SELECT * FROM (
    SELECT 
        employID, ename, deptID, salary,
        DENSE_RANK() OVER (PARTITION BY deptID ORDER BY salary DESC) AS drk
    FROM employ
) t WHERE drk <= 2;
```

### 5.6 三种 Top N 方案的选择建议

| 场景           | 推荐函数           | 结果特点            |
| ------------ | -------------- | --------------- |
| 每组**恰好 N 条** | `ROW_NUMBER()` | 即使有并列，也只取 N 条   |
| 并列**不占名额**   | `RANK()`       | 并列者都入选，可能超过 N 条 |
| 并列**排名连续**   | `DENSE_RANK()` | 并列者都入选，排名不跳跃    |


---

## 六、扩展：其他窗口函数速览

### 6.1 NTILE(N) —— 数据分桶

```sql
-- 将员工按薪资分为4档（每档人数大致相等）
SELECT 
    employID, ename, salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employ;
```

**效果展示：**

| employID | ename | salary   | quartile |
| -------- | ----- | -------- | -------- |
| 5        | 曹操    | 30000.00 | 1        |
| 1        | 刘备    | 25000.00 | 1        |
| 6        | 司马懿   | 22000.00 | 1        |
| 7        | 张辽    | 20000.00 | 2        |
| 8        | 孙权    | 20000.00 | 2        |
| 9        | 周瑜    | 19000.00 | 2        |
| 10       | 陆逊    | 19000.00 | 3        |
| 2        | 关羽    | 18000.00 | 3        |
| 3        | 张飞    | 18000.00 | 4        |
| 4        | 赵云    | 15000.00 | 4        |

> 10 行 ÷ 4 桶，前 2 桶各 3 行，后 2 桶各 2 行。

---

```sql
-- 按部门分桶：每个部门内部将员工按薪资分为3档（高/中/低）
SELECT 
    employID, ename, deptID, salary,
    NTILE(3) OVER (PARTITION BY deptID ORDER BY salary DESC) AS tier,
    CASE NTILE(3) OVER (PARTITION BY deptID ORDER BY salary DESC)
        WHEN 1 THEN '高'
        WHEN 2 THEN '中'
        WHEN 3 THEN '低'
    END AS tier_label
FROM employ
ORDER BY deptID, salary DESC;
```

**效果展示：**

| employID | ename  | deptID | salary   | tier | tier_label |
|----------|--------|--------|----------|------|------------|
| 1        | 刘备   | 10     | 25000.00 | 1    | 高         |
| 2        | 关羽   | 10     | 18000.00 | 1    | 高         |
| 3        | 张飞   | 10     | 18000.00 | 2    | 中         |
| 4        | 赵云   | 10     | 15000.00 | 3    | 低         |
| 5        | 曹操   | 20     | 30000.00 | 1    | 高         |
| 6        | 司马懿 | 20     | 22000.00 | 2    | 中         |
| 7        | 张辽   | 20     | 20000.00 | 3    | 低         |
| 8        | 孙权   | 30     | 20000.00 | 1    | 高         |
| 9        | 周瑜   | 30     | 19000.00 | 2    | 中         |
| 10       | 陆逊   | 30     | 19000.00 | 3    | 低         |

> **NTILE 分配规则**：当总行数不能整除 N 时，前面的桶多分 1 行。
> 例如部门 10 有 4 人分 3 桶 → 桶1有2行，桶2、桶3各1行。

---

```sql
-- 实际场景：将员工按薪资分为 3 档，统计每档人数和平均薪资
SELECT 
    tier,
    COUNT(*) AS cnt,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM (
    SELECT salary, NTILE(3) OVER (ORDER BY salary DESC) AS tier
    FROM employ
) t
GROUP BY tier
ORDER BY tier;
```

**效果展示：**

| tier | cnt | avg_salary | min_salary | max_salary |
|------|-----|------------|------------|------------|
| 1    | 4   | 24250.00   | 20000.00   | 30000.00   |
| 2    | 3   | 19333.33   | 19000.00   | 20000.00   |
| 3    | 3   | 17000.00   | 15000.00   | 18000.00   |

> 可以直观看出各档的薪资区间和差距——第 1 档平均薪资比第 3 档高出约 43%。

---

### 6.2 LAG / LEAD —— 偏移分析

```sql
-- 查看每个员工与上一名员工的薪资差距
SELECT 
    employID, ename, salary,
    LAG(salary, 1) OVER (ORDER BY salary DESC) AS prev_salary,
    salary - LAG(salary, 1) OVER (ORDER BY salary DESC) AS diff
FROM employ;
```

**效果展示：**

| employID | ename  | salary   | prev_salary | diff     |
|----------|--------|----------|-------------|----------|
| 5        | 曹操   | 30000.00 | NULL        | NULL     |
| 1        | 刘备   | 25000.00 | 30000.00    | -5000.00 |
| 6        | 司马懿 | 22000.00 | 25000.00    | -3000.00 |
| 7        | 张辽   | 20000.00 | 22000.00    | -2000.00 |
| 8        | 孙权   | 20000.00 | 20000.00    | 0.00     |
| 9        | 周瑜   | 19000.00 | 20000.00    | -1000.00 |
| 10       | 陆逊   | 19000.00 | 19000.00    | 0.00     |
| 2        | 关羽   | 18000.00 | 19000.00    | -1000.00 |
| 3        | 张飞   | 18000.00 | 18000.00    | 0.00     |
| 4        | 赵云   | 15000.00 | 18000.00    | -3000.00 |

> 第一行 `prev_salary` 为 `NULL`（没有上一行），diff 随之也为 NULL。

---

```sql
-- LEAD：查看每个员工与下一名员工的差距（向前看）
SELECT 
    employID, ename, salary,
    LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_salary,
    salary - LEAD(salary, 1) OVER (ORDER BY salary DESC) AS lead_diff
FROM employ;
```

**效果展示：**

| employID | ename  | salary   | next_salary | lead_diff |
|----------|--------|----------|-------------|-----------|
| 5        | 曹操   | 30000.00 | 25000.00    | 5000.00   |
| 1        | 刘备   | 25000.00 | 22000.00    | 3000.00   |
| 6        | 司马懿 | 22000.00 | 20000.00    | 2000.00   |
| 7        | 张辽   | 20000.00 | 20000.00    | 0.00      |
| 8        | 孙权   | 20000.00 | 19000.00    | 1000.00   |
| ...      | ...    | ...      | ...         | ...       |
| 4        | 赵云   | 15000.00 | NULL        | NULL      |

> 最后一行 `next_salary` 为 `NULL`（没有下一行）。LAG 看"过去"，LEAD 看"未来"。

---

```sql
-- 按部门偏移：查看每个员工在部门内的薪资排名变化
SELECT 
    employID, ename, deptID, salary,
    LAG(salary, 1) OVER (PARTITION BY deptID ORDER BY salary DESC) AS dept_prev_salary,
    salary - LAG(salary, 1) OVER (PARTITION BY deptID ORDER BY salary DESC) AS dept_diff
FROM employ
ORDER BY deptID, salary DESC;
```

**效果展示（部门10）：**

| employID | ename | deptID | salary   | dept_prev_salary | dept_diff |
|----------|-------|--------|----------|------------------|-----------|
| 1        | 刘备  | 10     | 25000.00 | NULL             | NULL      |
| 2        | 关羽  | 10     | 18000.00 | 25000.00         | -7000.00  |
| 3        | 张飞  | 10     | 18000.00 | 18000.00         | 0.00      |
| 4        | 赵云  | 10     | 15000.00 | 18000.00         | -3000.00  |

> PARTITION BY 将每个部门切分为独立窗口，`LAG` 只在部门内部偏移，不会跨部门取值。

---

**实际场景A：连续签到天数计算**

```sql
-- 先建一张签到记录表
CREATE TABLE checkin (
    userID  INT,
    c_date  DATE,
    PRIMARY KEY (userID, c_date)
);

INSERT INTO checkin VALUES
(1, '2024-01-01'), (1, '2024-01-02'), (1, '2024-01-03'),
(1, '2024-01-05'), (1, '2024-01-06'),
(2, '2024-01-01'), (2, '2024-01-02'), (2, '2024-01-04');

-- 计算每位用户相邻签到的日期差
SELECT 
    userID, c_date,
    LAG(c_date, 1) OVER (PARTITION BY userID ORDER BY c_date) AS prev_date,
    DATEDIFF(c_date, LAG(c_date, 1) OVER (PARTITION BY userID ORDER BY c_date)) AS gap
FROM checkin;
```

**效果展示：**

| userID | c_date     | prev_date  | gap  |
|--------|------------|------------|------|
| 1      | 2024-01-01 | NULL       | NULL |
| 1      | 2024-01-02 | 2024-01-01 | 1    |
| 1      | 2024-01-03 | 2024-01-02 | 1    |
| 1      | 2024-01-05 | 2024-01-03 | 2    |
| 1      | 2024-01-06 | 2024-01-05 | 1    |
| 2      | 2024-01-01 | NULL       | NULL |
| 2      | 2024-01-02 | 2024-01-01 | 1    |
| 2      | 2024-01-04 | 2024-01-02 | 2    |

> **解读**：`gap=1` 表示连续签到，`gap>1` 表示断签。用户 1 在 01-03 → 01-05 之间断了一天（gap=2）。

---

**实际场景B：月度销售额环比分析**

```sql
-- 假设有一张月度销售表
CREATE TABLE monthly_sales (
    ym      VARCHAR(7),          -- 格式：2024-01
    amount  DECIMAL(12, 2)
);

INSERT INTO monthly_sales VALUES
('2024-01', 100000), ('2024-02', 120000), ('2024-03', 95000),
('2024-04', 130000), ('2024-05', 145000), ('2024-06', 160000);

-- 计算环比增长率
SELECT 
    ym, amount,
    LAG(amount, 1) OVER (ORDER BY ym) AS prev_amount,
    ROUND((amount - LAG(amount, 1) OVER (ORDER BY ym)) 
          / LAG(amount, 1) OVER (ORDER BY ym) * 100, 2) AS mom_pct
FROM monthly_sales;
```

**效果展示：**

| ym       | amount    | prev_amount | mom_pct |
|----------|-----------|-------------|---------|
| 2024-01  | 100000.00 | NULL        | NULL    |
| 2024-02  | 120000.00 | 100000.00   | 20.00   |
| 2024-03  | 95000.00  | 120000.00   | -20.83  |
| 2024-04  | 130000.00 | 95000.00    | 36.84   |
| 2024-05  | 145000.00 | 130000.00   | 11.54   |
| 2024-06  | 160000.00 | 145000.00   | 10.34   |

> 一眼看出 3 月销售额下滑 20.83%，4 月强劲反弹 36.84%，后续保持稳定增长。

---

### 6.3 FIRST_VALUE / LAST_VALUE

```sql
-- 查看每个部门最高薪资和最低薪资
SELECT 
    employID, ename, deptID, salary,
    FIRST_VALUE(salary) OVER (PARTITION BY deptID ORDER BY salary DESC) AS dept_max,
    LAST_VALUE(salary) OVER (
        PARTITION BY deptID ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS dept_min
FROM employ;
```

**效果展示（部门10）：**

| employID | ename | deptID | salary   | dept_max  | dept_min  |
|----------|-------|--------|----------|-----------|-----------|
| 1        | 刘备  | 10     | 25000.00 | 25000.00  | 15000.00  |
| 2        | 关羽  | 10     | 18000.00 | 25000.00  | 15000.00  |
| 3        | 张飞  | 10     | 18000.00 | 25000.00  | 15000.00  |
| 4        | 赵云  | 10     | 15000.00 | 25000.00  | 15000.00  |

> ⚠️ **LAST_VALUE 常见坑**：默认窗口框架是 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，
> 即窗口只到当前行为止，因此 `LAST_VALUE` 返回的永远是当前行自身，而不是分组的最后一行。
> **正确写法**：显式指定 `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`。

**错误写法对比（不加 ROWS 限定）：**

| employID | ename | deptID | salary   | LAST_VALUE(错误) | LAST_VALUE(正确) |
|----------|-------|--------|----------|------------------|------------------|
| 1        | 刘备  | 10     | 25000.00 | 25000.00         | 15000.00         |
| 2        | 关羽  | 10     | 18000.00 | 18000.00         | 15000.00         |
| 3        | 张飞  | 10     | 18000.00 | 18000.00         | 15000.00         |
| 4        | 赵云  | 10     | 15000.00 | 15000.00         | 15000.00         |

> 不加 `ROWS` 时 `LAST_VALUE` 始终等于当前行 salary——这是一个初学者极易踩的坑。

---

```sql
-- FIRST_VALUE 实际场景：计算每个员工与部门最高薪的差距
SELECT 
    employID, ename, deptID, salary,
    FIRST_VALUE(salary) OVER (PARTITION BY deptID ORDER BY salary DESC) AS dept_max,
    FIRST_VALUE(salary) OVER (PARTITION BY deptID ORDER BY salary DESC) - salary AS gap_from_max
FROM employ
ORDER BY deptID, salary DESC;
```

**效果展示：**

| employID | ename  | deptID | salary   | dept_max  | gap_from_max |
|----------|--------|--------|----------|-----------|--------------|
| 1        | 刘备   | 10     | 25000.00 | 25000.00  | 0.00         |
| 2        | 关羽   | 10     | 18000.00 | 25000.00  | 7000.00      |
| 3        | 张飞   | 10     | 18000.00 | 25000.00  | 7000.00      |
| 4        | 赵云   | 10     | 15000.00 | 25000.00  | 10000.00     |
| 5        | 曹操   | 20     | 30000.00 | 30000.00  | 0.00         |
| 6        | 司马懿 | 20     | 22000.00 | 30000.00  | 8000.00      |
| 7        | 张辽   | 20     | 20000.00 | 30000.00  | 10000.00     |
| 8        | 孙权   | 30     | 20000.00 | 20000.00  | 0.00         |
| 9        | 周瑜   | 30     | 19000.00 | 20000.00  | 1000.00      |
| 10       | 陆逊   | 30     | 19000.00 | 20000.00  | 1000.00      |

> 部门 10 中赵云距离部门最高薪差 10000，部门 20 中张辽同样差 10000——可以快速识别各部门的薪资公平性。

---

```sql
-- FIRST_VALUE + LAST_VALUE 实际场景：部门薪资极差
SELECT DISTINCT
    deptID,
    FIRST_VALUE(salary) OVER w AS max_salary,
    LAST_VALUE(salary) OVER w AS min_salary,
    FIRST_VALUE(salary) OVER w - LAST_VALUE(salary) OVER w AS salary_range
FROM employ
WINDOW w AS (
    PARTITION BY deptID ORDER BY salary DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
)
ORDER BY deptID;
```

**效果展示：**

| deptID | max_salary | min_salary | salary_range |
|--------|------------|------------|--------------|
| 10     | 25000.00   | 15000.00   | 10000.00     |
| 20     | 30000.00   | 20000.00   | 10000.00     |
| 30     | 20000.00   | 19000.00   | 1000.00      |

> 部门 30 薪资极差仅 1000，说明薪资非常平均；部门 10、20 极差均为 10000，内部差距较大。

> 💡 **WINDOW 子句**：当多个窗口函数共用同一窗口定义时，可以用 `WINDOW w AS (...)` 命名窗口，
> 之后通过 `OVER w` 复用，避免重复书写。

---

## 七、核心要点总结

| 要点 | 说明 |
|------|------|
| **版本要求** | MySQL 8.0+（5.x 不支持） |
| **本质** | 给表新增一列，不减少行数 |
| **语法核心** | `函数 OVER (PARTITION BY ... ORDER BY ...)` |
| **PARTITION BY** | 分组切窗口，类似 GROUP BY 但保留所有行 |
| **ORDER BY** | 组内排序，非全局排序 |
| **嵌套查询** | 窗口函数结果列不能直接在 WHERE 中使用，必须子查询包裹 |
| **初学者重点** | 掌握 **分组排名求 Top N** 这一经典用法 |

---

## 八、实际应用场景速查

| 场景 | 实现思路 |
|------|---------|
| **排行榜/Top N** | `ROW_NUMBER() OVER (ORDER BY score DESC)` |
| **分组排行榜** | `ROW_NUMBER() OVER (PARTITION BY group ORDER BY score DESC)` |
| **连续登录天数** | `LAG(date, 1)` 配合日期差计算 |
| **环比/趋势分析** | `LAG(value, 1)` 对比前后值 |
| **数据分档** | `NTILE(4)` 分为四等份 |
| **首尾值提取** | `FIRST_VALUE()`, `LAST_VALUE()` |

---

这份笔记涵盖了从**数据库创建 → 数据类型 → 窗口函数理论 → 三大排序函数对比 → 分组排名 → 经典 Top N 实战**的完整学习路径。如果需要进一步深入某个部分（如连续签到、环比分析等），可以继续补充！