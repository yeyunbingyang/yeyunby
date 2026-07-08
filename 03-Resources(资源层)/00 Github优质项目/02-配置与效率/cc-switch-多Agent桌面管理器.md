---
title: "CC Switch AI Agent 多合一桌面管理"
tags: [GitHub, 开源, AI, Agent, 桌面应用, Claude, Codex, MCP, Tauri]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-06-18
source: https://github.com/farion1231/cc-switch
zh-CN: https://github.com/farion1231/cc-switch/blob/main/README_ZH.md
related: [[9router-免费AI路由网关], [ECC-Agent全套配置系统]]
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

与 9Router 的关系：9Router 做**命令行代理路由**（省钱），CC Switch 做**图形化管理面板**（省心）。两者可串联使用——9Router 作为 CC Switch 的供应商端点。

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


## 深入功能

### 代理增强（Proxy Mode）

CC Switch 内置本地代理服务器（默认 `localhost:9100`），是核心杀手功能之一：

- **模型热切换**：修改供应商/模型后立即生效，无需重启 Agent
- **格式自动转换**：自动处理 OpenAI ↔ Claude API 格式差异，任何 Agent 都能调用任何供应商
- **Combo 链**：可串联多层代理——例如 CC Switch → 9Router → 各供应商，实现「CC Switch 管配置 + 9Router 省钱路由」组合
- **请求拦截与注入**：代理层可注入自定义 headers（如 Referer、Origin），解决某些 MCP/API 的跨域限制
- **流量监控**：Dashboard 实时可视化每个 Agent 的 API 调用量、Token 消耗、延迟分布

### Skills 商店

CC Switch 深度集成了 **Skills 生态系统**：

- **官方商店**：从 CC Switch 社区商店浏览/安装 Skills，含 Agent Skills、CLI Skills、Developer Tools Skills 等分类
- **跨 Agent 同步**：安装一个 Skill 后自动同步到所有支持的 Agent（Claude Code / Codex / Gemini CLI）
- **自定义导入**：支持本地 `SKILL.md` 文件导入，兼容 Codex 和 Claude Code 的 skill 格式
- **Skills 组合**：可创建「Skills 配置文件」，一键切换不同场景的 Skills 集合（如「前端开发套装」「后端开发套装」）
- **版本管理**：Skills 更新通知 + 一键升级，回滚到历史版本

### MCP 管理深度

MCP 管理不仅是简单的启停开关：

- **MCP 市场**：社区贡献的 MCP 服务器一键安装启动，覆盖文件系统、数据库、浏览器、云服务等类别
- **配置导入导出**：支持标准 `mcp.json` / `.cursor/mcp.json` / `.codex/mcp.json` 格式互转
- **实时文件同步**：修改 MCP 配置后自动写入各 Agent 的配置文件，无需手动复制粘贴
- **环境变量管理**：MCP 服务器需要的 API Key 等环境变量统一管理，避免泄露
- **状态监控**：MCP 服务器运行状态（CPU/内存/端口）实时展示

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


## 进阶用法

### 与 9Router 串联

```
Claude Code / Codex / Gemini CLI
    ↓ 配置 API Endpoint
CC Switch 代理 (localhost:9100)
    ↓ 供应商列表中添加
9Router (localhost:20128)
    ↓ 三级回落
免费/廉价/付费供应商
```

**配置步骤**：
1. 启动 9Router（`9router`）
2. CC Switch → 供应商管理 → 新建供应商 → 端点设为 `http://localhost:20128/v1`
3. 各 Agent 的 API Endpoint 指向 CC Switch 的代理端口

这样实现**配置 GUI（CC Switch）+ 智能省钱路由（9Router）**的完美组合，一个面板管理所有 Agent 配置，背后自动省钱。

## 评价

- **优点**：真正实用的多 Agent 统一管理、Tauri 2 桌面性能优秀、内置代理热切换无需重启、MCP/Skills/Prompts 管理全覆盖、中文界面友好、81.5k Stars 社区验证、MIT 开源
- **局限**：功能繁多学习曲线陡、需要一定配置才能发挥全部威力、与特定 Agent 版本兼容性需关注
- **是否值得长期保留**：✅ 重点关注——多 Agent 时代的统一控制面板，与 9Router+ECC+CodeGraph 组成完整的 Agent 工具链
