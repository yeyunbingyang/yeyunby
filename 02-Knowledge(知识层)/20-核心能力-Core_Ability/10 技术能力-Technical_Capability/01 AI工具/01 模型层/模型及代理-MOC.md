---
title: 模型及代理 MOC
domain: Core_Ability
tags: [MOC, AI, 模型, 代理]
status: 稳定
created: 2026-06-16
updated: 2026-06-16
source: ""
related: ["AI概念全览", "Claude Code 快速入门", "AI工程-MOC"]
summary: "AI 模型选型与代理路由导航——覆盖主流模型对比、CC Switch 管理器、9router 路由工具及模型切换策略"
---

# 模型及代理 MOC

> 选模型、配代理、省 Token 的一站式入口。

## 子主题

### 模型认知
- [[03-主流模型对比]] — GPT-5 / Claude 4 / Gemini / DeepSeek / Qwen 等主流模型能力与定价速查
- [[04-模型路由策略]] — 什么任务用什么模型，如何配置高/中/低三档

### 工具与配置

| 工具 | 功能 |
|------|------|
| [[01 模型层/02-CC-Switch-模型管理器.md|CC Switch]] | Claude Code 多模型切换中枢 |
| [[01 模型层/01-9router-快速入门手册.md|9Router]] | 免费AI路由器 |
| [[01 模型层/03-omniRoute-使用指南.md|OmniRoute]] | 236供应商企业级AI网关 |

## 速查：模型与代理工具关系

```
用户需求
   │
   ├─→ CC Switch（模型管理器）
   │      ├─ 高档：Claude Opus 4 / GPT-5
   │      ├─ 中档：Claude Sonnet 4 / DeepSeek-V3
   │      └─ 低档：Claude Haiku / Qwen-Plus
   │
   └─→ 9router（代理路由器）
          ├─ RTK 节省 Token
          ├─ 自动 fallback 到免费模型
          └─ 对接 40+ 厂商 / 100+ 模型
```

## 本域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/01 模型层"
WHERE file.name != "模型及代理-MOC"
SORT updated DESC
```

