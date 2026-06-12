---
title: "CC Switch AI Agent 多合一桌面管理"
tags: [GitHub, 开源, AI, Agent, 桌面应用, Claude, Codex, MCP, Tauri]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/farion1231/cc-switch
zh-CN: https://github.com/farion1231/cc-switch/blob/main/README_ZH.md
related: [[9router], [ECC]]
summary: "AI Agent 多合一桌面管理器，统一管理 Claude Code/Codex/Gemini 等 6 个 Agent 的供应商/MCP/Skills/Prompts，内置代理热切换，Tauri+Rust 构建，81.5k Stars"
---

# CC Switch AI Agent 多合一桌面管理

https://github.com/farion1231/cc-switch

## 基本信息

**类型：** 工具（桌面应用）
**链接：** https://github.com/farion1231/cc-switch
**主页：** https://ccswitch.io
**适用领域：** AI Agent 统一管理、多供应商切换、MCP/Skills 管理
**推荐程度：** ★★★★★
**Stars：** ~81.5k | Fork 5.3k
**语言：** Rust（Tauri 2 桌面框架 + React 前端）
**许可证：** MIT
**平台：** Windows / macOS / Linux

## 是什么

CC Switch 是一个**跨平台桌面应用**，把所有 AI 编程 Agent 的管理整合到一个 GUI 里——统一管理供应商（API Key/模型/端点）、MCP 服务器、Skills、Prompts，内置本地代理实现模型热切换。支持 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw、Hermes Agent 六大 Agent。

与 9Router 的关系：9Router 做**命令行代理路由**（省钱），CC Switch 做**图形化管理面板**（省心）。

## 快速开始

从 [ccswitch.io](https://ccswitch.io) 或 [GitHub Releases](https://github.com/farion1231/cc-switch/releases) 下载安装包即可。

## 核心功能

### 六大管理模块

| 模块 | 功能 |
|------|------|
| **供应商管理** | 统一管理 API Key/模型/端点，一键切换、排序、回填配置 |
| **MCP 管理** | MCP 服务器导入/导出，实时文件同步，一键开关 |
| **Skills 管理** | 技能市场浏览/安装，跨 Agent 技能同步 |
| **Prompts 管理** | 提示词模板管理与快速注入 |
| **本地代理** | 内置代理模式，模型热切换+格式转换（OpenAI↔Claude），无需重启 |
| **会话管理** | 跨 App 浏览对话历史 |

### 技术特点

- **Tauri 2 + Rust**：桌面级性能，内存友好
- **SQLite 持久化**：Mutex 保护并发安全，原子写入防配置损坏
- **双向同步**：GUI ↔ 配置文件实时同步
- **分层架构**：Commands → Services → DAO → Database 清晰分离
- **i18n**：中文/English/日本語

### 支持全部主流 Agent

Claude Code · Codex · Gemini CLI · OpenCode · OpenClaw · Hermes Agent

## 适用场景

- 同时使用多个 AI Agent，需要在它们之间统一管理配置
- 频繁切换模型/供应商，不想每次手动改配置文件
- 管理大量 MCP 服务器，需要一个可视化面板
- 团队统一 Agent 配置——导出/导入配置，备份轮转
- 与 9Router 互补：9Router 做智能路由省钱，CC Switch 做可视化管理省心

## 评价

- **优点**：真正实用的多 Agent 统一管理、Tauri 2 桌面性能优秀、内置代理热切换无需重启、MCP/Skills/Prompts 管理全覆盖、中文界面友好、81.5k Stars 社区验证、MIT 开源
- **局限**：功能繁多学习曲线陡、需要一定配置才能发挥全部威力、与特定 Agent 版本兼容性需关注
- **是否值得长期保留**：✅ 重点关注——多 Agent 时代的统一控制面板，与 9Router+ECC+CodeGraph 组成完整的 Agent 工具链
