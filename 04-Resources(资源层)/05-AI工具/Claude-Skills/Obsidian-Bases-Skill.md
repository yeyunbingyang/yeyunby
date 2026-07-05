---
title: obsidian-bases — Obsidian Bases 数据视图手册
description: 创建和管理 .base 文件，通过视图（表格/卡片/列表/地图）、过滤器和公式创建数据库般的笔记视图。
aliases:
  - obsidian-bases skill
tags:
  - obsidian
  - bases
  - claude-code
  - formula
  - database-view
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: IT_Technology
source: kepano/obsidian-skills
install: npx skills add kepano/obsidian-skills@obsidian-bases
links:
  - help/bases/syntax
  - help/bases/functions
  - help/bases/views
  - help/formulas
---

# obsidian-bases 使用手册

## 概述

Bases 将 Obsidian 笔记转化为类数据库视图（表格/卡片/列表），可定义过滤、公式计算、分组统计。文件扩展名为 `.base`。

## 工作流

1. 创建 `.base` 文件 → 2. 定义过滤范围 → 3. 添加公式（可选） → 4. 配置视图 → 5. 在 Obsidian 中打开验证

## Schema

```yaml
# 全局过滤条件
filters:
  and:
    - 'status == "active"'
    - not:
        - 'file.hasTag("archived")'

# 计算公式
formulas:
  总价: "price * quantity"
  状态图标: 'if(done, "✅", "⏳")'

# 属性显示名
properties:
  formula.总价:
    displayName: "总价 (¥)"

# 视图定义
views:
  - type: table
    name: "视图名"
    limit: 30
    groupBy:
      property: status
      direction: ASC
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.总价
    summaries:
      formula.总价: Sum
```

## 过滤语法

### 结构

```yaml
# 单条件
filters: 'status == "done"'

# AND
filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

# OR
filters:
  or:
    - 'file.hasTag("book")'
    - 'file.hasTag("article")'

# NOT
filters:
  not:
    - 'file.hasTag("archived")'

# 嵌套
filters:
  or:
    - file.hasTag("tag")
    - and:
        - file.hasTag("book")
        - file.hasLink("Textbook")
```

### 操作符

| 操作符 | 说明 |
|--------|------|
| `==` | 等于 |
| `!=` | 不等于 |
| `>`, `<`, `>=`, `<=` | 比较 |
| `&&`, `\|\|`, `!` | 逻辑与/或/非 |

## 属性类型

1. **笔记属性** — 从 frontmatter 读取：`author` 或 `note.author`
2. **文件属性** — 文件元数据：`file.name`, `file.mtime` 等
3. **公式属性** — 计算值：`formula.我的公式`

### 文件属性参考

| 属性 | 类型 | 说明 |
|------|------|------|
| `file.name` | String | 文件名 |
| `file.basename` | String | 无扩展名文件名 |
| `file.path` | String | 完整路径 |
| `file.folder` | String | 父文件夹路径 |
| `file.ext` | String | 扩展名 |
| `file.size` | Number | 大小(字节) |
| `file.ctime` | Date | 创建时间 |
| `file.mtime` | Date | 修改时间 |
| `file.tags` | List | 所有标签 |
| `file.links` | List | 内部链接 |
| `file.backlinks` | List | 反向链接 |
| `file.embeds` | List | 嵌入内容 |
| `file.properties` | Object | 所有 frontmatter |

## 公式语法

```yaml
formulas:
  # 算术
  total: "price * quantity"

  # 条件
  状态图标: 'if(done, "✅", "⏳")'

  # 日期格式化
  创建日期: 'file.ctime.format("YYYY-MM-DD")'

  # 天数计算
  已创建天数: '(now() - file.ctime).days'
  截止剩余: 'if(due, (date(due) - today()).days, "")'

  # 优先级标签
  优先级标签: 'if(priority == 1, "🔴 高", if(priority == 2, "🟡 中", "🟢 低"))'
```

## 关键函数

| 函数 | 说明 |
|------|------|
| `date(str)` | 解析日期 |
| `now()` | 当前日期时间 |
| `today()` | 当前日期(时间归零) |
| `if(条件, 真, 假?)` | 条件判断 |
| `duration(str)` | 解析持续时间 |
| `file(path)` | 获取文件对象 |
| `link(path, 显示?)` | 创建链接 |

### Duration 陷阱

两日期相减得到 **Duration** 类型（非数字），必须先访问 `.days` 等字段再调用数值函数：

```yaml
# ✅ 正确
"(date(due) - today()).days.round(0)"

# ❌ 错误 - Duration 不支持直接 round
"(now() - file.ctime).round(0)"
```

### 日期算术

```yaml
"now() + \"1 day\""        # 明天
"today() + \"7d\""         # 7天后
"(now() - file.ctime).days"  # 经过天数
```

单位：`y`/`M`/`d`/`w`/`h`/`m`/`s`

## 视图类型

### 表格 (Table)
```yaml
- type: table
  name: "我的表格"
  order:
    - file.name
    - status
  summaries:
    price: Sum
    count: Average
```

### 卡片 (Cards) — 显示属性排列
### 列表 (List) — 简洁列表
### 地图 (Map) — 需 Maps 插件和经纬度属性

## 嵌入 Bases

```markdown
![[MyBase.base]]
![[MyBase.base#视图名]]
```

## YAML 引号规则

- 含双引号的公式用单引号包裹：`'if(done, "是", "否")'`
- 含特殊字符（`: { } [ ] ,`等）的字符串必须引号包裹

## 常见错误

1. **Duration 的算术**：先取 `.days` 再 `.round(0)`
2. **空值检查**：属性可能不存在，用 `if()` 守卫
3. **未定义的公式引用**：`order` 中的 `formula.X` 必须有对应的 `formulas.X` 定义

## 完整示例

### 任务追踪器

```yaml
filters:
  and:
    - file.hasTag("task")
    - 'file.ext == "md"'

formulas:
  剩余天数: 'if(due, (date(due) - today()).days, "")'
  是否逾期: 'if(due, date(due) < today() && status != "done", false)'
  优先级标签: 'if(priority == 1, "🔴 高", if(priority == 2, "🟡 中", "🟢 低"))'

views:
  - type: table
    name: "活跃任务"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.优先级标签
      - due
      - formula.剩余天数
    groupBy:
      property: status
      direction: ASC
    summaries:
      formula.剩余天数: Average

  - type: table
    name: "已完成"
    filters:
      and:
        - 'status == "done"'
    order:
      - file.name
      - completed_date
```

### 阅读清单

```yaml
filters:
  or:
    - file.hasTag("book")
    - file.hasTag("article")

formulas:
  阅读时间: 'if(pages, (pages * 2).toString() + " min", "")'
  状态图标: 'if(status == "reading", "📖", if(status == "done", "✅", "📚"))'

views:
  - type: cards
    name: "图书馆"
    filters:
      not:
        - 'status == "dropped"'
    order:
      - cover
      - file.name
      - author
      - formula.状态图标
```

## 参考链接

- [Bases 语法](https://help.obsidian.md/bases/syntax)
- [函数参考](https://help.obsidian.md/bases/functions)
- [视图](https://help.obsidian.md/bases/views)
- [公式](https://help.obsidian.md/formulas)
