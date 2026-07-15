---
title: jsonpath 数据提取
domain: IT_Technology
tags:
  - Python
  - 爬虫
  - jsonpath
  - 数据提取
status: 草稿
created: 2026-06-14
updated: 2026-06-14
source: 尚硅谷大模型技术之Python V1.0
related:
  - "[[01-数据提取基础]]"
  - "[[03-lxml模块与XPath]]"
  - "[[Python-MOC]]"
summary: jsonpath 是 JSON 版的 XPath——用路径表达式从嵌套 JSON 中提取数据，比手写 data["a"]["b"][0]["c"] 清晰 100 倍；爬虫中主要用于「肌肉层」（Ajax/XHR 接口返回的 JSON），掌握语法 + 拉钩实战即可覆盖 90% 的 JSON 提取场景
---

# jsonpath 数据提取

## 一句话结论

> `jsonpath(obj, "$..city")` 一行代码从嵌套 JSON 中挖出所有城市名——jsonpath 之于 JSON 正如 XPath 之于 HTML，是爬虫处理 Ajax 接口返回数据的利器。

### 在数据提取体系中的位置

回顾 [[01-数据提取基础]] 中的「骨骼·肌肉·皮肤」三文件模型：

```
骨骼（HTML 页面）→ 数据在 HTML 中 → XPath + lxml 提取
肌肉（Ajax/XHR）→ 数据在 JSON 中 → jsonpath 提取  ← 你在这里
皮肤（JS/CSS）   → 通常不含目标数据
```

> jsonpath 主要用于「肌肉层」数据提取——当你在 Network → XHR 中找到返回 JSON 的 Ajax 接口时，jsonpath 就是最佳工具。

---

## 一、jsonpath 是什么

- **jsonpath**：JSON 路径表达式语言，用类似 XPath 的语法在 JSON 结构中定位和提取数据
- **场景**：绝大多数现代网站的 Ajax 接口返回 JSON——jsonpath 直接解放双手
- **类比**：

| 数据格式 | 路径语言 |
|---------|---------|
| 文件系统 | `C:\Users\docs\file.txt` |
| HTML/XML | XPath：`//div[@class="item"]/h2` |
| JSON | jsonpath：`$.store.book[0].title` |

---

## 二、安装

```bash
pip install jsonpath
```

```python
from jsonpath import jsonpath

# jsonpath(obj, expr) → 返回匹配的结果列表（未匹配时返回 False）
result = jsonpath(data, "$.store.book[*].title")
print(result)   # ['Python入门', 'Java编程']
```

---

## 三、jsonpath 语法速查

### 3.1 基本语法

| 表达式  | 含义         | 示例          |     |
| ---- | ---------- | ----------- | --- |
| `$`  | 根节点        | `$`         |     |
| `.`  | 子节点        | `$.store`   |     |
| `..` | 递归搜索（任意深度） | `$..title`  |     |
| `*`  | 通配符，匹配任意节点 | `$.store.*` |     |
| `[]` | 下标 / 条件    | `$.book[0]` |     |

### 3.2 数组操作

| 表达式 | 含义 |
|--------|------|
| `[0]` | 第一个元素 |
| `[0,2]` | 第 1 和第 3 个元素 |
| `[0:2]` | 切片（不含 index 2） |
| `[-1]` | 最后一个元素 |
| `[*]` | 所有元素 |

### 3.3 条件过滤

| 表达式 | 含义 |
|--------|------|
| `[?(@.price < 10)]` | 过滤 price < 10 的元素 |
| `[?(@.category == "技术")]` | 过滤 category 为"技术"的元素 |
| `[?(@.title =~ /Python/i)]` | 正则匹配（title 含 Python） |

---

## 四、语法练习（基于示例 JSON）

```python
data = {
    "store": {
        "book": [
            {"title": "Python入门", "price": 29.9, "category": "技术"},
            {"title": "Java编程", "price": 39.9, "category": "技术"},
            {"title": "百年孤独", "price": 19.9, "category": "文学"},
        ],
        "bicycle": {"color": "red", "price": 299}
    }
}

from jsonpath import jsonpath

# 练习 1：取所有书名
print(jsonpath(data, "$.store.book[*].title"))
# → ['Python入门', 'Java编程', '百年孤独']

# 练习 2：递归搜索所有 title（不管在哪一层）
print(jsonpath(data, "$..title"))
# → ['Python入门', 'Java编程', '百年孤独']

# 练习 3：第一本书
print(jsonpath(data, "$.store.book[0]"))
# → [{'title': 'Python入门', 'price': 29.9, 'category': '技术'}]

# 练习 4：最后一本书
print(jsonpath(data, "$.store.book[-1].title"))
# → ['百年孤独']

# 练习 5：前两本书
print(jsonpath(data, "$.store.book[0:2].title"))
# → ['Python入门', 'Java编程']

# 练习 6：条件过滤——价格 < 30 的书
print(jsonpath(data, "$.store.book[?(@.price < 30)].title"))
# → ['Python入门', '百年孤独']

# 练习 7：条件过滤——技术类书籍
print(jsonpath(data, "$.store.book[?(@.category == '技术')].title"))
# → ['Python入门', 'Java编程']

# 练习 8：取所有商品（book + bicycle）
print(jsonpath(data, "$.store.*"))

# 练习 9：递归搜索所有价格
print(jsonpath(data, "$..price"))
# → [29.9, 39.9, 19.9, 299]

# 练习 10：获取 store 下所有含 price 的对象
print(jsonpath(data, "$.store..[?(@.price)]"))
```

---

## 五、实战：拉钩网职位数据提取

### 5.1 背景

拉钩网的职位列表通过 Ajax 返回 JSON 数据（「肌肉层」），结构嵌套深、数据量大——jsonpath 是最佳提取工具。

### 5.2 抓包分析

1. 打开 `https://www.lagou.com/` → 搜索"Python"
2. F12 → Network → XHR → 找到返回 JSON 的接口
3. 查看 Response，典型结构：

```json
{
    "code": 0,
    "data": {
        "positionResult": {
            "result": [
                {
                    "positionName": "Python开发工程师",
                    "salary": "15k-25k",
                    "city": "北京",
                    "companyFullName": "某某科技有限公司",
                    "companySize": "500-2000人",
                    "education": "本科",
                    "workYear": "3-5年",
                    "skillLables": ["Python", "Django", "MySQL"],
                    "positionAdvantage": "六险一金,年终奖金"
                },
                { "positionName": "Python爬虫工程师", ... },
                ...
            ],
            "totalCount": 300
        }
    }
}
```

### 5.3 jsonpath 提取代码

```python
import requests
from jsonpath import jsonpath

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
    "Referer": "https://www.lagou.com/",
}

session = requests.Session()
session.headers.update(headers)

# 请求拉钩搜索接口（URL 需根据实际抓包替换）
api_url = "https://www.lagou.com/jobs/positionAjax.json"
params = {"city": "北京", "needAddtionalResult": "false"}
data = {"first": "true", "pn": 1, "kd": "Python"}

resp = session.post(api_url, params=params, data=data)
resp_data = resp.json()

# ============ jsonpath 提取 ============

# 1. 提取所有职位名称
positions = jsonpath(resp_data, "$..positionName")
print("职位列表:", positions)

# 2. 提取所有公司名
companies = jsonpath(resp_data, "$..companyFullName")
print("公司列表:", companies)

# 3. 提取所有薪资
salaries = jsonpath(resp_data, "$..salary")
print("薪资列表:", salaries)

# 4. 提取所有城市
cities = jsonpath(resp_data, "$..city")
print("城市列表:", cities)

# 5. 提取所有技能标签
skills = jsonpath(resp_data, "$..skillLables")
print("技能标签:", skills)

# 6. 提取第一条职位的完整信息
first = jsonpath(resp_data, "$.data.positionResult.result[0]")
print("第一条:", first)

# 7. 提取职位总数
total = jsonpath(resp_data, "$..totalCount")
print(f"共 {total[0]} 个职位")

# 8. 联合输出：职位 + 薪资 + 公司
result = []
for i in range(len(positions)):
    result.append({
        "职位": positions[i],
        "薪资": salaries[i] if i < len(salaries) else "",
        "公司": companies[i] if i < len(companies) else "",
        "城市": cities[i] if i < len(cities) else "",
    })

for r in result[:5]:
    print(f"{r['职位']} | {r['薪资']} | {r['公司']} | {r['城市']}")
```

### 5.4 jsonpath 的核心优势

```python
# 不用 jsonpath —— 层层字典取值，又臭又长
city = resp_data["data"]["positionResult"]["result"][0]["city"]

# 用 jsonpath —— 一行搞定，语义清晰
city = jsonpath(resp_data, "$..city")[0]
```

---

## jsonpath vs 手写取值 对照

| 需求 | 手写 | jsonpath |
|------|------|---------|
| 取嵌套值 | `d["a"]["b"][0]["c"]` | `$..c` |
| 取所有同名字段 | ❌ 需递归遍历 | `$..field` |
| 条件过滤 | ❌ for + if | `[?(@.price < 30)]` |
| 代码量 | 随嵌套深度暴增 | 一行路径表达式 |
| 可读性 | 差 | 一目了然 |

## 关键概念

- **`$`**：JSON 根节点——所有 jsonpath 表达式都以 `$` 开头
- **`..`**：递归下降——不管字段在哪一层，直接搜到所有匹配
- **条件过滤 `[?()]`**：相当于 SQL 的 WHERE 子句，支持比较、正则
- **返回类型**：jsonpath 始终返回列表——未匹配返回 `False`
- **肌肉层数据**：jsonpath 是 Ajax/XHR JSON 数据的标配工具，配合 [[01-数据提取基础]] 的三文件模型使用

## 可行动建议

- 面对嵌套 JSON：优先用 `$..fieldname` 递归搜索，找到数据后再精确路径
- 条件过滤 `[?(@.key == 'value')]` 是 jsonpath 最强大的功能，务必掌握
- API 返回的大 JSON：先用 jsonpath 提取，不要手写嵌套取值
- 调试时打印 `len(result)` 确认提取数量是否合理
- 在 Network → XHR 中找到 JSON 接口后，直接复制 Response 到本地测试 jsonpath 表达式

## 延伸与关联

- [[01-数据提取基础]] — 响应内容分类 + 三文件模型：jsonpath 对应「肌肉层」Ajax JSON 数据
- [[03-lxml模块与XPath]] — HTML/XML 提取用 XPath（骨骼层），JSON 用 jsonpath（肌肉层）——语法高度相似
- [[requests POST 请求与数据来源]] — 如何从 Network 抓包找到返回 JSON 的接口
- [[Python-MOC]] — Python 知识体系总导航
