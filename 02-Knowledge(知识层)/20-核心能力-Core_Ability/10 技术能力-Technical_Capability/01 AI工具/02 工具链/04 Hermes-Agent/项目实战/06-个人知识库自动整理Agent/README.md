---
title: 个人知识库自动整理 Agent
description: 基于 Hermes Agent 的 Obsidian 知识库自动整理方案，覆盖 frontmatter 检测、标签推荐、链接检查、笔记关联与归档建议
created: 2026-07-07
updated: 2026-07-07
author: Hermes Agent
tags:
  - obsidian
  - hermes-agent
  - knowledge-management
  - automation
  - dataview
  - templater
  - project
status: draft
---

# 个人知识库自动整理 Agent

> 让 AI Agent 成为你的知识库管家——自动检测缺失元数据、推荐标签、检查链接完整性、发现笔记关联，并定期给出归档建议。

## 项目概述

本项目基于 **Hermes Agent** 构建，针对 **Obsidian 知识库**（6 层架构 + MOC + frontmatter 规范）实现自动化整理流水线。通过 Hermes 的 Cron 定时任务、session_search 语义搜索、Memory 持久记忆、@file 文件引用、Terminal Git 操作和 Kanban 任务板等核心能力，将知识库维护从手动劳动转变为自动化的 Agent 工作流。

### 解决的问题

| 痛点 | 方案 |
|------|------|
| 笔记缺少 frontmatter，无法被 Dataview 查询 | 自动检测并补全缺失字段 |
| 标签体系混乱，新笔记无标签 | 基于内容语义推荐标签 |
| 笔记间链接断裂（死链/空链） | 定期扫描并报告链接完整性 |
| 相关笔记分散各处，未被发现 | 基于向量相似度推荐关联 |
| 旧笔记堆积，归档不及时 | 按活跃度/时间自动建议归档 |

### 技术栈

```
Hermes Agent  →  编排调度层（Cron / Memory / session_search / Kanban）
Obsidian      →  知识库载体（Markdown + 6 层目录 + MOC）
Dataview      →  元数据查询引擎
Templater     →  模板注入与 frontmatter 补全
Git           →  版本控制与变更追踪
```

## 目录结构

```
06-个人知识库自动整理Agent/
├── README.md              # 项目总览（本文档）
├── docs/
│   ├── 01-架构设计.md     # 整体架构与模块划分
│   ├── 02-环境搭建.md     # 环境配置与依赖安装
│   ├── 03-核心流程.md     # 各 Agent 流程详解
│   ├── 04-踩坑记录.md     # 实施中遇到的问题与解决
│   └── 05-扩展思路.md     # 未来扩展方向
├── configs/
│   ├── cron-jobs.yaml     # Hermes Cron 任务配置
│   └── dataview-queries.md # Dataview 查询集合
├── references/
│   └── vault-structure.md # Vault 6 层架构参考
└── scripts/
    └── setup.sh           # 环境初始化脚本
```

## 快速开始

```bash
# 1. 克隆项目到知识库内
cd /path/to/your/vault/项目实战/06-个人知识库自动整理Agent

# 2. 安装依赖
pip install -r requirements.txt   # Python 依赖（如需要）
# Hermes Agent 需已安装并配置

# 3. 配置 Cron 任务
hermes cron create "every 6h" \
  --prompt "运行知识库完整性检查：检测缺失 frontmatter、死链、未标签笔记" \
  --deliver chat

# 4. 启动第一个整理任务
hermes chat -q "扫描当前 vault，列出所有缺失 frontmatter 的笔记"
```

## 核心能力一览

| 能力 | 触发方式 | 关键工具 |
|------|----------|----------|
| Frontmatter 检测 | Cron 定时 / 手动 | `terminal` (grep/find), `@file` 引用 |
| 标签推荐 | 新笔记创建时 | `session_search`, `delegate_task` |
| 链接完整性检查 | Cron 每日 | `terminal` (obsidian-export), `web_extract` |
| 笔记关联推荐 | Cron 每周 | `session_search`, Memory |
| 归档建议 | Cron 每月 | `terminal` (git log), Dataview 查询 |
| 变更追踪 | Git 提交时 | `terminal` (git), Kanban |

## 前置条件

- [Hermes Agent](https://hermes-agent.nousresearch.com) 已安装并配置
- Obsidian vault 遵循 [6 层架构规范](references/vault-structure.md)
- 已安装 Obsidian 插件：Dataview、Templater
- Git 已初始化并关联远程仓库（可选）
- Python 3.10+（用于部分辅助脚本）

## 许可

本项目为知识库内部实践文档，遵循知识库自身许可协议。
