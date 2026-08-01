---
title: Agent扩展 MOC
domain: Core_Ability
tags: [MOC, AI, Agent, 工具]
status: 稳定
created: 2026-07-25
updated: 2026-07-30
verified: 2026-07-30
review_after: 2026-10-25
source: "内部实践整理；外部依据见正文链接"
related: ["AI工具链与Agent实践-MOC", "Agent平台-MOC"]
summary: "Agent 扩展能力通过 Skills、MCP 和工具集成把通用 Agent 转化为适配具体场景的工作系统"
---

# Agent扩展 MOC

> 本层只收录 Agent 的扩展机制与集成方法；Claude Code、Codex、Hermes Agent 等平台本体见 [[Agent平台-MOC]]。

## Skills

- [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/03-Agent扩展/内容/skills/01-快速入门|Skills 快速入门]] — Skills 的基本结构与使用方式
- [[02-我的skills蒸馏]] — 个人实践沉淀
- [[03-通用skills最佳实践]] — 编写、调用与维护规范
- [[04-Skills生态全景]] — 官方与社区生态
- [[05-需求到执行-Skills工作流]] — 从需求澄清到验证交付
- [[06-Karpathy四大原则]] — 简单、精准和目标驱动

## MCP

- [[MCP-概念与架构]] — 协议角色、通信流程与适用边界
- [[MCP-企业级应用与本地部署]] — 企业集成和本地部署
- [[Chrome-DevTools-MCP安装与操作指南]] — 在 Codex 中安装、配置并使用 Chrome 浏览器调试与自动化能力

## 集成场景

- [[Skills场景化使用指南]]
- [[官方与社区Skill资源集成指南]]
- [[01-OpenCLI]]
- [[02-opencli-browser]]
- [[Obsidian-Agent操作指南]]
- [[Obsidian-Markdown语法参考]]
- [[数据获取-可用Skills与开源项目]]

## 本域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/03-Agent扩展"
WHERE file.name != "Agent扩展-MOC"
SORT file.name ASC
```
