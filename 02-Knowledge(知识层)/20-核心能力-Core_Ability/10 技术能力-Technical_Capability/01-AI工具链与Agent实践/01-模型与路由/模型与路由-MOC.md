---
title: 模型与路由 MOC
domain: Core_Ability
tags: [MOC, AI, 模型, 工具]
status: 稳定
created: 2026-06-16
updated: 2026-07-25
verified: 2026-07-25
review_after: 2026-08-25
source: ""
related: ["AI工具链与Agent实践-MOC", "Agent平台-MOC"]
summary: "模型与路由决策应以任务质量、成本、上下文和官方兼容性为依据，而不是长期绑定某个版本排名"
---

# 模型与路由 MOC

> 本层数据变化快，模型名称、价格、上下文、版本和供应商数量以笔记中的官方来源及 `verified` 日期为准。

## 核心笔记

- [[00-主流模型对比]] — 模型能力、价格和场景对比
- [[04-模型路由策略]] — 按任务复杂度分配模型
- [[01-9router-快速入门手册]] — 轻量路由与自动回退
- [[02-CC-Switch-模型管理器]] — Claude Code、Codex 等客户端配置管理
- [[03-omniRoute-使用指南]] — 多供应商网关和路由策略

## 官方核验入口

- [OpenAI Models](https://developers.openai.com/api/docs/models)
- [Anthropic Models](https://platform.claude.com/docs/en/about-claude/models/overview)
- [9Router](https://github.com/decolua/9router)
- [CC Switch](https://github.com/farion1231/cc-switch)
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

## 本域笔记

```dataview
TABLE summary, verified, review_after, status
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/01-模型与路由"
WHERE file.name != "模型与路由-MOC"
SORT file.name ASC
```
