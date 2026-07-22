---
title: 工具链 MOC
domain: Core_Ability
tags: [MOC, AI, Agent, CLI, Skills]
status: 稳定
created: 2026-07-22
updated: 2026-07-22
summary: "工具链层导航——Agent引擎、CLI工具、Skills体系、数据获取工具的统一入口"
---

# 工具链 MOC

> 工具层：Agent引擎、CLI 工具、Skills 体系、数据获取。

---

## Agent 引擎

| 工具 | 说明 |
|------|------|
| [[02 工具链/01 Claude/01-安装选项.md|Claude Code]] | Anthropic 官方终端 Agent，对话式协作 |
| [[02 工具链/02 codex/01-Codex-使用指南.md|Codex (OpenAI)]] | OpenAI 官方编程 Agent，命令式自动化 |
| [[02 工具链/04 Hermes-Agent/README.md|Hermes Agent]] | 本地增强型自托管 AI 代理，支持持久记忆 |

## 基础设施

| 模块 | 内容 |
|------|------|
| [[02 工具链/00 基础设施/CLI/OpenCLI/01-OpenCLI.md|OpenCLI]] | 网站 CLI 桥接工具，将任意网站转为 CLI 交互 |
| [[02 工具链/00 基础设施/MCP/MCP深度解析与本地模型企业级应用指南.md|MCP 协议]] | 模型上下文协议深度解析，企业级工具链 |

## Skills 体系

Skills 是面向 AI 代理的可复用指令集，当前收录 13+ 个 Skills。

| # | 笔记 | 说明 |
|---|------|------|
| 01 | [[02 工具链/00 基础设施/skills/01-快速说明.md|快速说明]] | Skills 概念简介 |
| 02 | [[02 工具链/00 基础设施/skills/02-我的skills蒸馏.md|我的 Skills 蒸馏]] | 个人最佳实践总结 |
| 03 | [[02 工具链/00 基础设施/skills/03-通用skills最佳实践.md|通用最佳实践]] | 跨工具 Skills 编写规范 |
| 04 | [[02 工具链/00 基础设施/skills/04-Skills生态全景.md|Skills 生态全景]] | 30KB 全景分析 |
| 05 | [[02 工具链/00 基础设施/skills/05-需求到执行-Skills工作流.md|需求到执行]] | 从需求到 AI 执行的完整流程 |
| 06 | [[02 工具链/00 基础设施/skills/06-Karpathy四大原则.md|Karpathy 四大原则]] | 简单优先/精准修改/目标驱动 |
| 07 | [[02 工具链/00 基础设施/skills/07-Skills调用机制与问题解法.md|调用机制]] | Skills 调用流程与问题排查 |

## 实践项目 (9个)

[[02 工具链/04 Hermes-Agent/项目实战/项目实战-MOC.md|项目实战-MOC]] — 9 个 Hermes 驱动的实战项目：博客发布、智能客服、CI/CD 自动化、代码审查、舆情监控、知识库整理、内容工厂、电商图生成、短视频发布。

---

## 工具快速对比

| 维度 | Claude Code | Codex | Hermes |
|------|-----------|-------|--------|
| 交互 | 对话式 | 命令式 | 自动化/定时 |
| 记忆 | 项目级 | 会话级 | 持久记忆 |
| 环境 | 本地终端 | 云端 sandbox | 本地扩展 |
| 模型 | Claude 全系 | GPT-5.x | 多种（含本地）|
| 上手 | 中 | 低 | 中高 |

---

## 本域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 工具链"
WHERE file.name != "工具链-MOC"
SORT file.name ASC
```
