---
title: Obsidian 插件 Dataview 使用指南
domain: Core_Ability
tags: [Obsidian, 插件, Dataview, 数据查询]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系, Obsidian插件-任务与日历]
summary: "Dataview 将 Obsidian Vault 变成可查询的数据库，支持 DQL 查询语言和 JavaScript API。是本知识库 MOC 自动聚合笔记、仪表盘统计任务的核心依赖"
---

# Obsidian 插件 Dataview 使用指南

## 一句话结论

> Dataview 让 Obsidian 的笔记不再只是文件——它把 frontmatter 和文件元数据当作数据库字段，用类似 SQL 的 DQL 语言查询，实现 MOC 自动聚合、仪表盘统计、任务追踪等功能。

## 核心概念

### 数据来源

| 数据类别 | 说明 | 示例 |
|----------|------|------|
| Frontmatter 字段 | YAML 头部的自定义属性 | `status`, `domain`, `tags`, `summary` |
| 文件元数据 | 文件自带属性 | `file.name`, `file.ctime`, `file.mtime`, `file.folder`, `file.link` |
| 任务列表 | 笔记中的 `- [ ]` 任务 | 可查询完成状态、优先级、截止日期 |

### 三种查询方式

| 方式 | 语法 | 适用场景 |
|------|------|----------|
| DQL 代码块 | `` ```dataview `` 块，独立查询 | MOC 聚合、仪表盘 |
| Inline DQL | `` `= ...` `` 内联表达式 | 单值显示（如笔记数量） |
| JavaScript API | `` ```dataviewjs `` 块 | 复杂逻辑、自定义渲染 |

## 核心语法

### TABLE 查询（最常用）

````
```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology"
WHERE status = "稳定"
SORT updated DESC
```
````

### LIST 查询

````
```dataview
LIST
FROM "02-Knowledge(知识层)"
WHERE contains(tags, "Obsidian")
```
````

### TASK 查询

````
```dataview
TASK
FROM "01-日常流(日常流层)"
WHERE !completed
GROUP BY file.link
```
````

### 常用过滤条件

| 条件 | 写法 |
|------|------|
| 等于 | `WHERE status = "稳定"` |
| 包含标签 | `WHERE contains(tags, "Obsidian")` |
| 排除当前文件 | `WHERE file.name != "当前笔记名"` |
| 排除目录 | `WHERE !contains(file.folder, "00_Resource")` |
| 多个条件 | `WHERE status = "稳定" AND domain = "IT_Technology"` |

## 本知识库中的应用实例

### MOC 自动聚合笔记

MOC 底部的 Dataview 块自动列出本目录下的所有笔记：

````
```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/00-通用技术工具/Obsidian知识管理"
WHERE file.name != "Obsidian知识管理-MOC"
SORT updated DESC
```
````

### 仪表盘统计

`Runtime_Data/Note_Statistics.md` 和 `Project_Dashboard.md` 中使用 Dataview 统计笔记数量、状态分布。

## 关键点

- **FROM 路径**：使用 Vault 的实际目录路径，不含 `KnowledgeBase/` 前缀
- **刷新**：Dataview 查询不会实时更新，需要切换到阅读视图或手动刷新
- **性能**：大库（1000+ 笔记）建议缩小 FROM 范围，避免全局扫描

## 反例与边界

- ❌ 不支持更新 frontmatter（Dataview 是只读查询工具）
- ❌ 不支持实时更新，需要刷新
- ⚠️ 大库中 FROM `""`（全局扫描）可能影响性能

## 可行动建议

- 每创建一个新 MOC 时，在底部添加 Dataview 查询自动聚合子笔记
- 参考 [[Obsidian知识管理-MOC]] 底部的 Dataview 代码块作为模板
- 阅读 [[MOC知识地图]] 了解 Dataview 在全库的分布