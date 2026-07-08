---
title: 运行时数据说明
tags: [仪表盘, 说明]
status: 稳定
created: 2026-05-07
updated: 2026-07-07
summary: "知识库运行时数据仪表盘说明，自动追踪笔记状态、项目和技能进度"
---

# 运行时数据说明

本目录存放知识库的运行时数据和自动聚合仪表盘。这些文件使用 Dataview 查询自动生成统计信息，帮助评估知识库健康度。

## 文件说明

| 文件 | 用途 | 更新方式 |
|------|------|---------|
| [Note_Statistics.md](Note_Statistics.md) | 笔记数量与状态统计 | Dataview 自动聚合，Obsidian 打开时自动刷新 |
| [Project_Dashboard.md](Project_Dashboard.md) | 待办事项集中管理 | 手动维护任务列表 + Dataview 自动聚合笔记内任务 |
| [Skill_Dashboard.md](Skill_Dashboard.md) | 技能成长追踪 | 手动维护技能表格 + Dataview 自动聚合待改进笔记 |

## 使用方式

1. `Note_Statistics.md` — 只读，无需手动编辑。用于快速了解知识库整体状态
2. `Project_Dashboard.md` — 新建任务时在"进行中"区域添加 `- [ ] 描述 → [[笔记名]]`
3. `Skill_Dashboard.md` — 每个领域技能表格需手动更新当前水平和目标

## Dataview 查询路径说明

本目录中的所有 Dataview 查询使用 vault 根目录下的实际文件夹路径，如 `"02-Knowledge(知识层)"`。如果目录结构调整，需要同步更新这些查询路径。
