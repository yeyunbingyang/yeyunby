---
title: Agent工具 MOC
domain: Core_Ability
tags: [MOC, AI, Agent, CLI, Skills]
status: 稳定
created: 2026-07-22
updated: 2026-07-23
summary: "Agent工具层导航——Agent引擎（Claude/Codex/Hermes）、扩展工具（Skills/MCP/OpenCLI）"
---

# Agent工具 MOC

> Agent 工具层的完整导航。从引擎选型到 Skills 配置，再到协议与扩展。
>
> 需要宏观概览？见 [[AI知识体系速查大纲]] — 概念→模型→Agent工具→最佳实践

---

## Agent 引擎

| 工具 | 说明 |
|------|------|
| [[00 Claude/Claude-安装选项\|Claude Code 安装选项]] | Claude Code 首次运行登录方式选择指南 |
| [[00 Claude/Claude-Code操作手册\|Claude Code 操作手册]] | Claude Code 完全操作手册，从入门到高阶 |
| [[01 Codex/Codex-使用指南\|Codex (OpenAI)]] | OpenAI 官方编程 Agent，命令式自动化 |
| [[01 Codex/Codex-插件与技能系统\|Codex 插件与技能系统]] | Codex 扩展体系 + 市场全目录 |
| [[02 Hermes-Agent/Hermes-Agent-技能工具手册\|Hermes Agent]] | 本地增强型自托管 AI 代理，支持持久记忆 |

## 扩展工具

### Skills 理论

| # | 笔记 | 说明 |
|---|------|------|
| 01 | [[03 扩展工具/skills/01-快速入门\|Skills 快速入门]] | Skills 概念简介 |
| 02 | [[03 扩展工具/skills/02-我的skills蒸馏\|Skills 蒸馏]] | 个人最佳实践总结 |
| 03 | [[03 扩展工具/skills/03-通用skills最佳实践\|通用最佳实践]] | 编写规范 + 调用机制 + 管理方法 |
| 04 | [[03 扩展工具/skills/04-Skills生态全景\|Skills 生态全景]] | 1000+ Skills 全景分析 |
| 05 | [[03 扩展工具/skills/05-需求到执行-Skills工作流\|需求到执行]] | 需求→AI 执行完整流程 |
| 06 | [[03 扩展工具/skills/06-Karpathy四大原则\|Karpathy 四大原则]] | 简单优先/精准修改/目标驱动 |

### 集成使用（按领域分类）

| 分类 | 笔记 | 说明 |
|------|------|------|
| **索引** | [[03 扩展工具/集成使用/Skills场景化使用指南\|场景化使用指南]] | 按场景介绍 Skill 用法 |
| **索引** | [[03 扩展工具/集成使用/官方与社区Skill资源集成指南\|资源集成指南]] | 工具库、社区仓库索引 |
| **浏览器自动化** | [[03 扩展工具/集成使用/浏览器自动化/01-OpenCLI\|OpenCLI]] | 网站 CLI 桥接，6 个配套 Skills |
| **浏览器自动化** | [[03 扩展工具/集成使用/浏览器自动化/02-opencli-browser\|OpenCLI 浏览器抓取]] | 浏览器自动化抓取操作参考 |
| **Obsidian** | [[03 扩展工具/集成使用/Obsidian/Obsidian-Agent操作指南\|Obsidian 操作指南]] | Agent 操作 Obsidian 完整手册 |
| **Obsidian** | [[03 扩展工具/集成使用/Obsidian/Obsidian-Markdown语法参考\|Obsidian Markdown 语法]] | Obsidian 风味 Markdown |
| **数据获取** | [[03 扩展工具/集成使用/数据获取/数据获取-可用Skills与开源项目\|数据获取全景]] | Agent 数据获取方式全景 |

### 协议与扩展

| 工具 | 说明 |
|------|------|
| [[03 扩展工具/MCP/MCP-概念与架构\|MCP 协议]] | 模型上下文协议——概念、架构与应用 |
| [[03 扩展工具/MCP/MCP-企业级应用与本地部署\|MCP 企业级部署]] | 企业级应用与本地模型部署 |

## 实践项目

[[02 Hermes-Agent/项目实战/项目实战-MOC\|项目实战-MOC]] — 9 个 Hermes 驱动的实战项目。

## 相关 Github 项目

- [[03-Resources(资源层)/00 Github优质项目/Github优质项目-MOC#01-Agent引擎\|Agent引擎项目]] — 15个开源Agent
- [[03-Resources(资源层)/00 Github优质项目/Github优质项目-MOC#02-Agent配置与Skills\|Agent配置与Skills]] — 26个Skills合集

---

## 工具快速对比

| 维度 | Claude Code | Codex | Hermes |
|------|-----------|-------|--------|
| 类型 | AI 编程 Agent | AI 编程 Agent | 自托管 Agent |
| 交互 | 对话式 | 命令式 | 自动化/定时 |
| 模型 | Claude 全系 | GPT-5.x | 多种（含本地）|
| 上手 | 中 | 低 | 中高 |

---

## 本域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01 AI工具/02 Agent工具"
WHERE file.name != "Agent工具-MOC"
SORT file.name ASC
```
