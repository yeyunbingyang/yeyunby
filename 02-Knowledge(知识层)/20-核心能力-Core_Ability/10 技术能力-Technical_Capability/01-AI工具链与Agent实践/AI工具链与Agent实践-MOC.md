---
title: AI工具链与Agent实践 MOC
domain: Core_Ability
tags: [MOC, AI, Agent, 工具]
status: 稳定
created: 2026-07-22
updated: 2026-07-25
verified: 2026-07-25
review_after: 2026-10-25
source: ""
related: ["Core_Ability-MOC", "模型与路由-MOC", "Agent平台-MOC", "Agent扩展-MOC", "工作流与实践-MOC"]
summary: "AI 工具链应按模型与路由、Agent 平台、扩展能力和工作流实践分层维护，以降低工具变化对长期知识的干扰"
---

# AI工具链与Agent实践 MOC

> 从模型选择进入 Agent 平台，再通过 Skills、MCP 和具体工作流完成实践落地。

## 学习路径

| 需求 | 入口 |
|------|------|
| 建立完整认知 | [[Agent学习与Vibe-Coding完全指南]] |
| 快速查概念 | [[AI知识体系速查大纲]] |
| 选择模型与路由方式 | [[模型与路由-MOC]] |
| 使用 Claude Code、Codex 或 Hermes Agent | [[Agent平台-MOC]] |
| 配置 Skills、MCP 与外部工具 | [[Agent扩展-MOC]] |
| 学习 AI Coding 与完整案例 | [[工作流与实践-MOC]] |

## 四层结构

- [[模型与路由-MOC]]：模型能力、价格、上下文和路由工具。
- [[Agent平台-MOC]]：Claude Code、Codex、Hermes Agent。
- [[Agent扩展-MOC]]：Skills、MCP、浏览器、数据与 Obsidian 集成。
- [[工作流与实践-MOC]]：AI Coding、Vibe Coding、视频创作与 Hermes Agent 案例。

## 资源区

- [[03-Resources(资源层)/05-AI工具/README|AI工具资源]]：示例工程、课程图片、附件与原始文稿。
- [[Github优质项目-MOC]]：外部开源项目索引。

## 待复核笔记

```dataview
TABLE verified, review_after, source, status
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践"
WHERE review_after AND date(review_after) <= date(today) AND status != "归档"
SORT review_after ASC
```

## 本域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践"
WHERE !endswith(file.name, "-MOC")
SORT file.name ASC
```
