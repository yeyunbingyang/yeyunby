---
title: "CodeGraph 预索引代码知识图谱"
tags: [GitHub, 开源, AI, 知识图谱, 代码分析, Agent, MCP]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/colbymchenry/codegraph
related: [[understand-anything]]
summary: "预索引代码知识图谱，通过 MCP 服务为 AI Agent 提供符号关系/调用图/代码结构即时查询，平均节省 35% 成本+71% 工具调用，100% 本地运行，26.9k Stars"
---

# CodeGraph 预索引代码知识图谱

https://github.com/colbymchenry/codegraph

## 基本信息

**类型：** 工具（MCP Server）
**链接：** https://github.com/colbymchenry/codegraph
**主页：** https://colbymchenry.github.io/codegraph/
**适用领域：** AI Agent 代码智能、Token 优化、代码库理解
**推荐程度：** ★★★★★
**Stars：** ~26.9k | Fork 1.5k
**NPM：** @colbymchenry/codegraph
**语言：** TypeScript
**许可证：** MIT
**支持平台：** Windows / macOS / Linux（x64 + arm64，自包含运行时无需装 Node.js）

## 是什么

当 Claude Code / Codex 探索代码库时，会频繁调用 grep、glob、Read——每次工具调用都消耗 Token。**CodeGraph 给 Agent 一个预索引的知识图谱**——符号关系、调用图、代码结构全部预先建好，Agent 通过 MCP 服务即时查询，不再逐文件扫描。

**与 Understand-Anything 的定位差异**：UA 偏重交互式 Dashboard + LLM 语义分析，CodeGraph 偏重本地预索引 + 极致省钱——两者互补。

## 快速开始

```bash
# 无需 Node.js，自包含运行时
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# 或 npm
npx @colbymchenry/codegraph

# 初始化项目
cd your-project
codegraph init -i
```

## 核心功能

### Benchmark（v0.9.4，7 个真实项目，Claude Opus 4.7）

**平均：35% 更便宜 · 57% 更少 Token · 46% 更快 · 71% 更少工具调用**

| 代码库 | 语言 | 节省成本 | 减少 Token | 更快 | 减少工具调用 |
|--------|------|----------|------------|------|-------------|
| VS Code | TS · ~10k 文件 | 26% | 78% | 52% | 85% |
| Excalidraw | TS · ~640 文件 | 52% | 90% | 73% | 96% |
| Django | Python · ~3k | 12% | 36% | 19% | 53% |
| Tokio | Rust · ~790 | 82% | 86% | 71% | 92% |
| OkHttp | Java · ~645 | 2% | 13% | 31% | 45% |
| Gin | Go · ~110 | 21% | 34% | 27% | 40% |
| Alamofire | Swift · ~110 | 47% | 64% | 48% | 83% |

**收益随代码库规模递增**：大项目上 Agent 从索引中几个调用即可回答，无需读文件。

### 支持 22 种语言

TypeScript/JavaScript/Python/Go/Rust/Java/C#/PHP/Ruby/C/C++/Objective-C/Swift/Kotlin/Scala/Dart/Svelte/Vue/Liquid/Pascal/Lua/Luau——全部「Full Support」。

### 命令集

| 命令 | 功能 |
|------|------|
| `/cg:find-definition` | 跳转到精确定义 |
| `/cg:find-references` | 查找所有引用 |
| `/cg:call-graph-inbound/outbound` | 导航调用图 |
| `/cg:search` | 模糊/语义搜索 |
| `/cg:diagram` | 生成 ASCII 架构图 |
| `/cg:explain` | 总结符号功能 |
| `/cg:dep-tree` | 依赖树 |
| `/cg:diff-impact` | 展示待提交变更影响范围 |

### 技术特点

- **100% 本地**：不调用外部 API，代码不出本机
- **MCP Server 模式**：Agent 通过 MCP 协议查询图谱
- **自动同步**：文件保存后自动增量更新索引（WAL 模式，并发读不阻塞写）
- **零依赖**：自包含 Node 运行时，不编译、不构建
- **多 Agent 兼容**：Claude Code / Cursor / Codex CLI / OpenCode / Hermes Agent

## 适用场景

- 大项目 Agent 编码：显著降低 Token 消耗和 API 成本
- 与 Understand-Anything 互补：CodeGraph 做实时查询+省钱，UA 做全局可视化
- 离线/安全敏感场景：100% 本地索引，代码不离开本机
- 多语言项目：22 种语言全部 Full Support

## 评价

- **优点**：省钱效果实锤（Benchmark 数据透明）、100% 本地安全、22 语言 Full Support、自包含安装零门槛、MCP 协议标准化、与现有 Agent 工具无缝集成
- **局限**：纯结构分析无 LLM 语义理解（和 UA 互补）、需预索引（首次有等待）、不支持交互式 Dashboard 可视化
- **是否值得长期保留**：✅ 重点关注——与 Understand-Anything 形成「结构查询（CodeGraph）+ 语义可视化（UA）」的完整方案
