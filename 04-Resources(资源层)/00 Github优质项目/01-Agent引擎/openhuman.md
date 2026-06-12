---
title: "OpenHuman 个人AI超级智能"
tags: [GitHub, 开源, AI, Agent, 记忆, Obsidian, 个人助手]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/tinyhumansai/openhuman
zh-CN: https://github.com/tinyhumansai/openhuman/blob/main/README.zh-CN.md
related: [[ai-engineering-from-scratch]]
summary: "个人AI超级智能，Memory Tree+Obsidian式Markdown知识库实现持久记忆，118+集成自动拉取数据，28.1k Stars，Rust构建"
---

# OpenHuman 个人AI超级智能

https://github.com/tinyhumansai/openhuman

## 基本信息

**类型：** 工具（桌面应用）
**链接：** https://github.com/tinyhumansai/openhuman
**主页：** https://tinyhumans.ai/openhuman
**适用领域：** 个人AI助手、知识管理、Agent 持久记忆、工作流自动化
**推荐程度：** ★★★★★
**Stars：** ~28.1k | Fork 2.6k
**语言：** Rust
**许可证：** GPL-3.0
**状态：** Early Beta
**作者：** tinyhumansai（[@senamakel](https://x.com/senamakel)）

## 是什么

OpenHuman 是一个**个人 AI 超级智能**——不只是编程 Agent，而是全面了解你生活的 AI 助手。核心理念：大多数 Agent 需要数周「训练期」才能了解你的工作上下文，OpenHuman **几分钟就够**。

连接你的账户后，Auto-fetch 每 20 分钟自动拉取数据（邮件、日历、文档、聊天、代码仓库），Memory Tree 将所有内容压缩为 **Karpathy 式 Obsidian Markdown 知识库**——一次同步，Agent 就拥有了你的完整上下文。

## 快速开始

从 [tinyhumans.ai/openhuman](https://tinyhumans.ai/openhuman) 下载桌面安装包，连接账户即可使用。

## 核心功能

### 记忆系统（与本知识库直接相关）

- **Memory Tree**：将所有数据压缩为结构化 Markdown 文件，存储在 Obsidian 式 Vault 中
- **Auto-fetch**：20 分钟循环自动拉取所有连接账户的数据到本地
- **agentmemory 后端**：可选对接 [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)，让同一持久存储同时服务 Claude Code、Cursor、Codex 等多个 Agent
- **Karpathy 模式**：灵感来自 [Karpathy 的 LLM Knowledgebase](https://x.com/karpathy/status/2039805659525644595)

### 集成与工具

- **118+ 集成**：通过 OAuth 对接 Gmail、日历、Slack、GitHub、Notion 等
- **内置工具**：代码 + 搜索 + 爬虫 + 语音（超越纯代码 Agent）
- **模型路由**：内置，无需手动切换
- **TokenJuice**：统一账户管理 API 成本

### 竞品对比

| 维度 | Claude Cowork | OpenClaw | Hermes Agent | OpenHuman |
|------|:---:|:---:|:---:|:---:|
| 开源 | ❌ 闭源 | ✅ MIT | ✅ MIT | ✅ GPL |
| 上手难度 | ✅ 简单 | ⚠️ 终端 | ⚠️ 终端 | ✅ 分钟级 |
| 记忆 | ✅ 会话级 | ⚠️ 依赖插件 | ✅ 自学习 | 🚀 Memory Tree+Obsidian |
| 集成数 | ⚠️ 少量 | ⚠️ 自配 | ⚠️ 自配 | 🚀 118+ OAuth |
| 自动抓取 | ❌ | ❌ | ❌ | ✅ 20分钟循环 |

### 技术架构

- **本地+托管混合**：Memory Tree、Obsidian Vault、工作区配置存本地；模型路由、搜索代理、OAuth 流程走托管服务
- **可自托管**：支持自定义模型、搜索、Composio 凭证
- **技术栈**：Rust（核心）+ TypeScript（桌面壳）

## 适用场景

- 需要一个真正了解你全部上下文的个人 AI 助手
- 多 Agent 共享同一持久记忆（通过 agentmemory 后端）
- 与 Obsidian 知识库深度集成——OpenHuman 的 Memory Tree 本身就是 Obsidian Vault
- 减少 API 厂商分散（一个账户 vs 多平台 Key）

## 评价

- **优点**：Obsidian 式持久记忆是杀手特性、118+ 集成覆盖面广、几分钟即可用无需训练期、Rust 性能可靠、竞品对比中记忆/集成/自动抓取全面领先
- **局限**：Early Beta 不稳定、GPL-3.0 许可证限制商用、部分功能依赖托管服务
- **是否值得长期保留**：✅ 重点关注——Memory Tree→Obsidian Vault 的路径与本知识库理念完全一致，是「知识库→AI 记忆」的最佳实践参考
