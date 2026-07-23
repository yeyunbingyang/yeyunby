---
title: 项目实战-MOC
summary: 企业级 AI Agent 落地项目索引，覆盖智能客服、CI/CD、代码审查、舆情监控、知识库整理、AIGC 内容工厂、电商商品图、短视频自动化等方向。
status: 稳定
domain: Core_Ability
tags:
  - MOC
  - 项目实战
  - Agent
  - 企业落地
created: 2026-07-07
updated: 2026-07-07
---

# 项目实战 — AI Agent 企业落地案例集

> 本目录收录基于 Hermes Agent 构建的企业级 AI Agent 实战项目，每个项目包含：项目概述、技术架构、核心流程、关键配置、踩坑记录、扩展思路。

## 项目清单

### 已完成

| # | 项目名称 | 方向 | 状态 | 难度 |
|---|---------|------|:----:|:----:|
| 01 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/01-博客自动发布系统-Hermes实战/README\|博客自动发布系统]] | 内容创作 | ✅ 完成 | ⭐⭐⭐ |
| 02 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/02-智能客服Agent系统/README\|智能客服 Agent 系统]] | 企业服务 | ✅ 完成 | ⭐⭐⭐ |
| 03 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/03-CICD自动化运维Agent/README\|CI/CD 自动化运维 Agent]] | DevOps | ✅ 完成 | ⭐⭐⭐⭐ |
| 04 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/04-代码审查Agent-CodeReview/README\|代码审查 Agent]] | 开发效能 | ✅ 完成 | ⭐⭐⭐ |
| 05 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/05-社交媒体舆情监控Agent/README\|社交媒体舆情监控 Agent]] | 品牌公关 | ✅ 完成 | ⭐⭐ |
| 06 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/06-个人知识库自动整理Agent/README\|个人知识库自动整理 Agent]] | 知识管理 | ✅ 完成 | ⭐⭐ |
| 07 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/07-AI内容工厂-多平台自媒体矩阵/README\|AI 内容工厂 — 多平台自媒体矩阵]] | AIGC | ✅ 完成 | ⭐⭐⭐⭐ |
| 08 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/08-AI电商商品图批量生成Agent/README\|AI 电商商品图批量生成 Agent]] | AIGC/电商 | ✅ 完成 | ⭐⭐⭐ |
| 09 | [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战/09-AI短视频自动生成与发布Agent/README\|AI 短视频自动生成与发布 Agent]] | AIGC/短视频 | ✅ 完成 | ⭐⭐⭐⭐ |

### 项目速查

```dataview
TABLE summary AS "简介", status AS "状态"
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具/02 Hermes-Agent/项目实战"
WHERE file.name != "项目实战-MOC"
SORT file.name ASC
```

## 项目结构规范

每个项目统一使用以下目录结构：

```
项目名称/
├── README.md          # 项目总览（必读入口）
└── docs/              # 详细文档
    ├── 01-架构设计.md
    ├── 02-环境搭建.md
    ├── 03-核心流程.md
    ├── 04-踩坑记录.md
    └── 05-扩展思路.md
```

> 按需添加 `scripts/`、`configs/` 等目录，不预占空位置。

## 技术栈对照

| 项目 | 核心 Hermes 功能 | 外部依赖 |
|------|----------------|---------|
| 博客自动发布 | Profile、Cron、Kanban、MCP | GitHub、Telegram/微信 |
| 智能客服 | RAG、Memory、Gateway、Delegation | 知识库、工单系统 |
| CI/CD 运维 | Cron、No-Agent、Webhook、Terminal | GitLab/GitHub、Docker、K8s |
| 代码审查 | MCP、Kanban、Orchestrator | GitHub API、ESLint |
| 舆情监控 | Cron、web_search、Gateway | RSS、社交媒体 API |
| 知识库整理 | session_search、Memory、Cron | Obsidian、Dataview |
| 内容工厂 | Cron、Delegation、Gateway、Plugins | 多模型 API、多平台 API |
| 电商商品图 | Cron、Terminal、Plugins | ComfyUI、商品平台 API |
| 短视频自动化 | Cron、web_search、Terminal、Gateway | 视频生成 API、抖音/小红书 API |
