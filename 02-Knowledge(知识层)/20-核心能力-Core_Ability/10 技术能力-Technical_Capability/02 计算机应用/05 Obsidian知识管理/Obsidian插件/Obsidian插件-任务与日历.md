---
title: Obsidian 任务与日历插件
domain: Core_Ability
tags: [Obsidian, 插件, 任务管理, 日历, Calendar, Tasks]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系, Obsidian插件-Dataview]
summary: "Calendar 插件提供侧边栏日历视图和日记快捷入口，Tasks 插件增强任务管理（截止日期、优先级、重复任务），两者配合实现日记+任务驱动的工作流"
---

# Obsidian 任务与日历插件

## 一句话结论

> Calendar 负责"今天要做什么"的入口，Tasks 负责"所有要做的事"的追踪——日历点击日期写日记，Tasks 语法让任务跨笔记可查询、可聚合。

## Calendar（日历插件）

### 用途

在右侧边栏显示日历视图，点击日期直接创建或打开当天的日记。

### 核心功能

- 日历导航：侧边栏显示月历
- 日记入口：点击日期打开/创建日记
- 视觉标记：有日记的日期显示圆点
- 周数显示：可配置显示周数

### 配置

设置 → Calendar → 配置日记路径和日期格式。当前使用默认配置，与核心日记插件配合。

### 与日记的配合

1. 右侧栏打开 Calendar
2. 点击今天的日期 → 打开/创建日记
3. 在日记中记录任务：
   ```
   - [ ] 完成 Obsidian 使用笔记 📅 2026-07-21
   - [ ] 复习 Git 常用命令 ⏫
   ```
4. Tasks 插件自动追踪这些任务

## Tasks（任务管理插件）

### 用途

增强 Obsidian 原生的任务功能，支持截止日期、优先级、重复任务、全局任务查询。

### 核心语法

```
- [ ] 任务描述 📅 2026-07-21 ⏫ 🔁 every week
```

### 日期类型

| 符号 | 含义 | 示例 |
|------|------|------|
| 📅 | 截止日期 (due) | `📅 2026-07-21` |
| ⏳ | 计划日期 (scheduled) | `⏳ 2026-07-20` |
| ✅ | 完成日期 (done) | `✅ 2026-07-21` |
| ➕ | 创建日期 (created) | `➕ 2026-07-19` |

### 优先级

| 符号 | 含义 |
|------|------|
| ⏫ | 高优先级 |
| 🔼 | 中优先级 |
| 🔽 | 低优先级 |

### 重复任务

```
- [ ] 每周复盘 🔁 every week
- [ ] 每日站会 🔁 every weekday
- [ ] 每月总结 🔁 every month on the 1st
```

### 全局任务查询

在任意笔记中聚合所有未完成任务：

````
```tasks
not done
sort by due
```
````

按优先级过滤：

````
```tasks
not done
priority is high
sort by due
```
````

按截止日期过滤：

````
```tasks
not done
due before tomorrow
```
````

## 本库中的应用

- **日记**：每天在日记中记录 3 个关键任务
- **Project_Dashboard**：`Runtime_Data/Project_Dashboard.md` 使用 Tasks 查询聚合所有项目任务
- **自定义属性**：`types.json` 中定义了 `TQ_` 前缀的属性类型，用于控制 Tasks 查询的显示字段

## 可行动建议

- 建立每日在日记中记录 3 个关键任务的习惯
- 每周五用 Tasks 查询回顾本周完成情况
- 给重要任务加 ⏫ 优先级，防止淹没在任务海中