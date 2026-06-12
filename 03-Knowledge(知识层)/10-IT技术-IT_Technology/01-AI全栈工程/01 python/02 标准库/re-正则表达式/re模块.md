# Python 正则表达式（re模块）核心知识点详解

## 1. 正则表达式基础概念

### 1.1 什么是正则表达式？

正则表达式是一种用于**描述字符串模式**的语法规则。它不是一个具体的字符串，而是一个**模式模板**，用于匹配、查找、提取或替换文本中符合该模式的子串。

**核心思想**：模式匹配。正则表达式匹配的是符合某种规则的字符串集合，而非精确的字符串本身。

### 1.2 原始字符串（Raw String）

在Python中，正则表达式模式字符串通常使用**原始字符串**（前缀 `r`）表示，以避免反斜杠转义带来的混淆。

```
# 不使用原始字符串 - 反斜杠需要转义
pattern1 = "\\d+"

# 使用原始字符串 - 反斜杠直接表示
pattern2 = r"\d+"

# 两者等价，但原始字符串更清晰
```

---

## 2. re模块核心函数

### 2.1 主要匹配与搜索函数

|   |   |   |   |
|---|---|---|---|
|函数|描述|返回值|适用场景|
|`re.match()`|从字符串**开头**尝试匹配模式|`Match`对象或`None`|检查字符串是否以特定模式开头|
|`re.search()`|扫描整个字符串，返回**第一个**匹配|`Match`对象或`None`|在字符串中查找任意位置的匹配|
|`re.findall()`|查找字符串中**所有**非重叠匹配|匹配字符串的列表|提取所有符合模式的内容|
|`re.finditer()`|查找字符串中**所有**非重叠匹配|匹配对象的迭代器|需要获取匹配详细信息时使用|
|`re.fullmatch()`|检查整个字符串是否完全匹配模式|`Match`对象或`None`|验证字符串完全符合特定格式|

```
import re

text = "今天是2025年12月26日，温度是25℃"

# re.match() - 从开头匹配
result1 = re.match(r"今天", text)  # 匹配成功
result2 = re.match(r"2025", text)  # 匹配失败（不是开头）

# re.search() - 搜索任意位置
result3 = re.search(r"\d+", text)  # 找到"2025"
result4 = re.search(r"温度", text)  # 找到"温度"

# re.findall() - 查找所有数字
numbers = re.findall(r"\d+", text)  # ['2025', '12', '26', '25']

# re.finditer() - 迭代获取匹配详情
for match in re.finditer(r"\d+", text):
    print(f"找到数字: {match.group()}，位置: {match.span()}")

# re.fullmatch() - 完全匹配
text2 = "2025-12-26"
result5 = re.fullmatch(r"\d{4}-\d{2}-\d{2}", text2)  # 匹配成功
```

### 2.2 字符串处理函数

|   |   |   |   |
|---|---|---|---|
|函数|描述|返回值|适用场景|
|`re.sub()`|替换字符串中匹配模式的部分|替换后的新字符串|批量替换文本内容|
|`re.subn()`|替换并返回替换次数|(新字符串, 替换次数)|需要知道替换了多少处|
|`re.split()`|根据模式分割字符串|分割后的字符串列表|按复杂规则分割文本|

```
import re

# re.sub() - 替换
text = "我的电话是123-4567-8901"
new_text = re.sub(r"\d", "*", text)  # "我的电话是***-****-****"

# re.subn() - 替换并计数
new_text, count = re.subn(r"\d", "*", text)  # count = 11

# re.split() - 分割
csv_data = "苹果,香蕉,橙子,西瓜"
items = re.split(r",", csv_data)  # ['苹果', '香蕉', '橙子', '西瓜']

# 复杂分割：按多个分隔符
text2 = "苹果;香蕉,橙子 西瓜|葡萄"
items2 = re.split(r"[;, \|]", text2)  # ['苹果', '香蕉', '橙子', '西瓜', '葡萄']
```

### 2.3 编译与性能优化

对于需要重复使用的正则表达式，可以使用 `re.compile()` 预编译，提高执行效率[[1]]。

```
import re

# 编译正则表达式
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

# 重复使用编译后的模式
texts = [
    "电话: 123-456-7890",
    "备用: 987-654-3210",
    "无电话"
]

for text in texts:
    match = pattern.search(text)
    if match:
        print(f"找到电话: {match.group()}")
```

---

## 3. 正则表达式语法详解

### 3.1 字符类与预定义字符集

|   |   |   |   |
|---|---|---|---|
|字符类|描述|等价字符集|示例|
|`.`|匹配除换行符外的任意字符|-|`a.c` 匹配 "abc"、"a c"|
|`\d`|匹配数字字符|`[0-9]`|`\d+` 匹配 "123"|
|`\D`|匹配非数字字符|`[^0-9]`|`\D+` 匹配 "abc"|
|`\w`|匹配单词字符（字母、数字、下划线）|`[a-zA-Z0-9_]`|`\w+` 匹配 "hello_123"|
|`\W`|匹配非单词字符|`[^a-zA-Z0-9_]`|`\W+` 匹配 "!@#"|
|`\s`|匹配空白字符（空格、制表符、换行等）|`[ \t\n\r\f\v]`|`\s+` 匹配空格和换行|
|`\S`|匹配非空白字符|`[^ \t\n\r\f\v]`|`\S+` 匹配 "abc123"|

```
import re

# 字符类示例
text = "用户ID: user_123, 电话: 138-0013-8000"

# 匹配所有数字
numbers = re.findall(r"\d+", text)  # ['123', '138', '0013', '8000']

# 匹配所有单词字符序列
words = re.findall(r"\w+", text)  # ['用户ID', 'user_123', '电话', '138', '0013', '8000']

# 匹配空白字符
spaces = re.findall(r"\s", text)  # [' ', ' ', ' ', ' ', ' ']
```

### 3.2 自定义字符集 `[...]`

|   |   |   |   |
|---|---|---|---|
|语法|描述|示例|匹配|
|`[abc]`|匹配 a、b 或 c 中的任意一个|`[aeiou]`|匹配任意元音字母|
|`[a-z]`|匹配 a 到 z 范围内的任意字符|`[a-z]+`|匹配小写字母序列|
|`[A-Z]`|匹配 A 到 Z 范围内的任意字符|`[A-Z]+`|匹配大写字母序列|
|`[0-9]`|匹配 0 到 9 范围内的任意数字|`[0-9]{3}`|匹配三位数字|
|`[^...]`|匹配**不在**字符集中的任意字符|`[^0-9]`|匹配非数字字符|

```
import re

# 自定义字符集示例
text = "颜色: Red, Green, Blue, Yellow"

# 匹配大写字母开头的单词
colors = re.findall(r"[A-Z][a-z]+", text)  # ['Red', 'Green', 'Blue', 'Yellow']

# 匹配元音字母
vowels = re.findall(r"[aeiouAEIOU]", text)  # ['e', 'e', 'e', 'u', 'e', 'o', 'e']

# 匹配非字母字符
non_letters = re.findall(r"[^a-zA-Z]", text)  # [':', ' ', ',', ' ', ',', ' ', ',', ' ']
```

### 3.3 量词（指定匹配次数）与贪婪

|   |   |   |   |
|---|---|---|---|
|量词|描述|示例|匹配说明|
|`*`|匹配前一个字符0次或多次|`a*`|"", "a", "aa", "aaa"...|
|`+`|匹配前一个字符1次或多次|`a+`|"a", "aa", "aaa"...|
|`?`|匹配前一个字符0次或1次|`a?`|"", "a"|
|`{n}`|匹配前一个字符恰好n次|`a{3}`|"aaa"|
|`{n,}`|匹配前一个字符至少n次|`a{2,}`|"aa", "aaa"...|
|`{n,m}`|匹配前一个字符n到m次|`a{2,4}`|"aa", "aaa", "aaaa"|

**贪婪 vs 非贪婪匹配**：

- 默认量词是**贪婪的**：尽可能多地匹配字符
- 在量词后加 `?` 变为**非贪婪**：尽可能少地匹配字符

```
import re

# 量词示例
text = "<div>内容1</div><div>内容2</div>"

# 贪婪匹配
greedy = re.findall(r"<div>.*</div>", text)  
# 结果: ['<div>内容1</div><div>内容2</div>'] - 匹配整个字符串

# 非贪婪匹配
non_greedy = re.findall(r"<div>.*?</div>", text)  
# 结果: ['<div>内容1</div>', '<div>内容2</div>'] - 匹配两个独立标签
```

### 3.4 边界与位置匹配

|   |   |   |   |
|---|---|---|---|
|锚点|描述|示例|匹配位置|
|`^`|匹配字符串开头|`^Hello`|仅匹配开头的"Hello"|
|`$`|匹配字符串结尾|`world$`|仅匹配结尾的"world"|
|`\b`|匹配单词边界|`\bcat\b`|匹配独立的"cat"单词|
|`\B`|匹配非单词边界|`\Bcat\B`|匹配"scatter"中的"cat"|

```
import re

# 边界匹配示例
text = "cat category scatter cat"

# 匹配独立的"cat"单词
independent_cat = re.findall(r"\bcat\b", text)  # ['cat'] (只匹配开头和结尾的cat)

# 匹配所有"cat"（包括作为部分单词）
all_cat = re.findall(r"cat", text)  # ['cat', 'cat', 'cat']

# 检查字符串是否以数字开头
if re.match(r"^\d", "123abc"):
    print("以数字开头")
```

### 3.5 分组与捕获

|   |   |   |   |
|---|---|---|---|
|语法|描述|示例|用途|
|`(...)`|捕获分组|`(\d{3})-(\d{4})`|提取区号和号码|
|`(?:...)`|非捕获分组|`(?:https?://)`|只匹配不捕获|
|`(?P<name>...)`|命名分组|`(?P<year>\d{4})`|通过名称引用分组|
|`\n`|引用第n个分组|`(\w+) \1`|匹配重复单词|

```
import re

# 分组示例
text = "日期: 2025-12-26, 电话: 010-1234-5678"

# 捕获分组 - 提取日期各部分
date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if date_match:
    year, month, day = date_match.groups()  # ('2025', '12', '26')
    print(f"年: {year}, 月: {month}, 日: {day}")

# 命名分组 - 更清晰的引用
phone_match = re.search(r"(?P<area>\d{3})-(?P<number>\d{4}-\d{4})", text)
if phone_match:
    print(f"区号: {phone_match.group('area')}")  # '010'
    print(f"号码: {phone_match.group('number')}")  # '1234-5678'

# 非捕获分组 - 只匹配不保存
urls = ["http://example.com", "https://example.org"]
for url in urls:
    match = re.match(r"(?:https?://)(\w+\.\w+)", url)
    if match:
        print(f"域名: {match.group(1)}")  # 'example.com', 'example.org'
```

### 3.6 选择与逻辑

|   |   |   |   |
|---|---|---|---|
|语法|描述|示例|匹配|
|`|`|逻辑"或"|`cat|
|`[...]`|字符集"或"|`[aeiou]`|任意元音字母|

```
import re

# 选择逻辑示例
text = "我喜欢猫和狗，但更喜欢猫"

# 匹配"猫"或"狗"
animals = re.findall(r"猫|狗", text)  # ['猫', '狗', '猫']

# 复杂选择
pattern = r"(小猫|小狗|成年猫|成年狗)"
text2 = "我家有只小猫和一只成年狗"
matches = re.findall(pattern, text2)  # ['小猫', '成年狗']
```

---

## 4. 匹配对象（Match Object）详解

当 `re.match()`、`re.search()` 等函数匹配成功时，返回一个匹配对象，包含丰富的匹配信息。

### 4.1 匹配对象常用方法

|   |   |   |
|---|---|---|
|方法|描述|示例|
|`group()`|返回匹配的完整字符串|`match.group()`|
|`group(n)`|返回第n个分组的内容|`match.group(1)`|
|`groups()`|返回所有分组的元组|`match.groups()`|
|`groupdict()`|返回命名分组的字典|`match.groupdict()`|
|`start()`|返回匹配开始位置|`match.start()`|
|`end()`|返回匹配结束位置|`match.end()`|
|`span()`|返回匹配范围 (start, end)|`match.span()`|

```
import re

text = "我的邮箱是: user@example.com，电话是: 138-0013-8000"

# 复杂匹配
pattern = r"(?P<type>邮箱|电话)[:：]\s*(?P<value>.+?)(?:，|$)"

# 使用finditer获取所有匹配的详细信息
for match in re.finditer(pattern, text):
    print(f"匹配类型: {match.group('type')}")
    print(f"匹配值: {match.group('value')}")
    print(f"匹配位置: {match.span()}")
    print(f"完整匹配: {match.group()}")
    print("-" * 30)
```

---

## 5. 正则表达式标志（Flags）

re模块提供多种标志来修改匹配行为，可以在 `re.compile()` 或直接函数调用中使用。

|   |   |   |   |
|---|---|---|---|
|标志|简写|描述|用途|
|`re.IGNORECASE`|`re.I`|忽略大小写|匹配"hello"、"Hello"、"HELLO"|
|`re.MULTILINE`|`re.M`|多行模式|使`^`和`$`匹配每行的开头结尾|
|`re.DOTALL`|`re.S`|点号匹配所有字符|使`.`匹配包括换行符的所有字符|
|`re.VERBOSE`|`re.X`|详细模式|允许在正则中添加空白和注释|

```
import re

# 使用标志的示例
text = """第一行: Hello World
第二行: hello python
第三行: HELLO REGEX"""

# 忽略大小写匹配所有"hello"
matches = re.findall(r"hello", text, re.IGNORECASE)  # ['Hello', 'hello', 'HELLO']

# 多行模式：匹配每行开头的单词
line_starts = re.findall(r"^第.行", text, re.MULTILINE)  # ['第一行', '第二行', '第三行']

# 详细模式：编写复杂的可读正则
pattern = re.compile(r"""
    \d{4}      # 年份：4位数字
    -          # 分隔符
    \d{2}      # 月份：2位数字
    -          # 分隔符
    \d{2}      # 日期：2位数字
""", re.VERBOSE)

date = pattern.search("日期: 2025-12-26")
if date:
    print(f"找到日期: {date.group()}")
```

---

## 6. 实用技巧与常见模式

### 6.1 常用正则表达式模式

|   |   |   |
|---|---|---|
|用途|正则模式|说明|
|邮箱地址|`r'[\w\.-]+@[\w\.-]+\.\w+'`|简单邮箱匹配|
|手机号码|`r'1[3-9]\d{9}'`|中国大陆手机号|
|身份证号|`r'\d{17}[\dXx]'`|18位身份证号|
|中文汉字|`r'[\u4e00-\u9fff]+'`|匹配中文字符|
|URL地址|`r'https?://[^\s]+'`|匹配HTTP/HTTPS链接|
|IP地址|`r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'`|IPv4地址|

### 6.2 性能优化建议

1. **预编译常用模式**：使用 `re.compile()` 编译频繁使用的正则表达式
2. **避免过度回溯**：谨慎使用 `.*`、`.+` 等贪婪量词
3. **使用非贪婪量词**：在适当场景使用 `*?`、`+?` 避免不必要的回溯
4. **尽量具体**：使用更具体的字符集代替 `.`
5. **使用原子分组**：`(?>...)` 可以防止回溯（Python 3.11+）

```
import re
import time

# 性能对比示例
text = "a" * 1000 + "b"

# 低效模式：过度回溯
start = time.time()
pattern1 = re.compile(r"a.*b")
match1 = pattern1.search(text)
time1 = time.time() - start

# 高效模式：使用非贪婪
start = time.time()
pattern2 = re.compile(r"a.*?b")
match2 = pattern2.search(text)
time2 = time.time() - start

print(f"贪婪模式耗时: {time1:.6f}秒")
print(f"非贪婪模式耗时: {time2:.6f}秒")
```

---

## 7. 综合应用示例

### 7.1 日志文件解析

```
import re

log_data = """
2025-12-26 10:30:15 INFO 用户登录成功 user_id=12345
2025-12-26 10:31:22 ERROR 数据库连接失败 error_code=500
2025-12-26 10:32:45 WARN 内存使用率超过80%
2025-12-26 10:33:10 INFO 用户注销 user_id=12345
"""

# 解析日志条目
log_pattern = r"""
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+
    (?P<level>INFO|ERROR|WARN)\s+
    (?P<message>.*?)\s*
    (?:user_id=(?P<user_id>\d+)|error_code=(?P<error_code>\d+))?
"""

parsed_logs = []
for match in re.finditer(log_pattern, log_data, re.VERBOSE):
    log_entry = match.groupdict()
    parsed_logs.append(log_entry)

for log in parsed_logs:
    print(f"时间: {log['timestamp']}, 级别: {log['level']}, 消息: {log['message']}")
```

### 7.2 数据清洗与提取

```
import re

# 混合文本数据清洗
raw_text = """
姓名: 张三, 年龄: 25, 邮箱: zhangsan@example.com
姓名: 李四, 电话: 138-0013-8000, 地址: 北京市朝阳区
无效数据: xxx-yyy-zzz
姓名: 王五, 年龄: 30, 邮箱: wangwu@test.org
"""

# 提取结构化信息
person_pattern = r"""
    姓名[:：]\s*(?P<name>[\u4e00-\u9fff]{2,3})\s*,
    (?:年龄[:：]\s*(?P<age>\d+)\s*,)?
    (?:邮箱[:：]\s*(?P<email>[\w\.-]+@[\w\.-]+\.\w+)\s*)?
    (?:电话[:：]\s*(?P<phone>1[3-9]\d{9})\s*)?
"""

people = []
for match in re.finditer(person_pattern, raw_text, re.VERBOSE):
    person = match.groupdict()
    # 过滤掉所有值都为None的匹配
    if any(person.values()):
        people.append(person)

for p in people:
    print(f"姓名: {p.get('name', '未知')}, "
          f"年龄: {p.get('age', '未知')}, "
          f"邮箱: {p.get('email', '无')}, "
          f"电话: {p.get('phone', '无')}")
```

---

## 总结

正则表达式是文本处理的强大工具，Python的re模块提供了完整的功能支持。掌握正则表达式的核心在于：

1. **理解模式匹配的本质**：正则匹配的是规则，不是具体字符串
2. **熟悉常用语法**：字符类、量词、分组、边界等基本元素
3. **合理选择函数**：根据需求使用match、search、findall等不同函数
4. **注意性能优化**：预编译、避免过度回溯、使用非贪婪量词
5. **实践应用**：通过实际项目练习，掌握数据提取、文本清洗等常见场景