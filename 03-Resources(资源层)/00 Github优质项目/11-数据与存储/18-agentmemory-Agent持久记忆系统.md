---
title: "agentmemory AI Agent 持久记忆系统"
tags: [GitHub, 开源, AI, Agent, 记忆, MCP, Obsidian, 知识图谱]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/rohitg00/agentmemory
related: [[ai-engineering-from-scratch-AI工程系统课程], [openhuman-个人AI超级智能]]
summary: "#1 AI Agent 持久记忆系统，95.2% 检索率+92% Token 节省，53 MCP 工具+12 自动钩子，内置知识图谱+Obsidian 导出，18.1k Stars"
---

# agentmemory AI Agent 持久记忆系统

https://github.com/rohitg00/agentmemory

## 基本信息

**类型：** 工具（MCP Server + REST API）
**链接：** https://github.com/rohitg00/agentmemory
**主页：** https://agent-memory.dev
**NPM：** @agentmemory/agentmemory
**适用领域：** Agent 持久记忆、跨会话上下文保持、知识图谱、团队记忆共享
**推荐程度：** ★★★★★
**Stars：** ~18.1k | Fork 1.5k
**语言：** TypeScript
**许可证：** Apache-2.0
**底层引擎：** [iii](https://iii.dev)（同作者）
**作者：** Rohit Ghumare（也是 ai-engineering-from-scratch 作者）

## 是什么

agentmemory 是当前 **#1 的 AI Agent 持久记忆系统**。核心理念：你的编程 Agent 应该记住一切——项目架构、你的偏好、之前修过的 Bug、做过的决策——不用每次会话都重新解释。

它扩展了 **Karpathy 的 LLM Wiki 模式**，加入置信度评分、生命周期管理、知识图谱、混合搜索。基于真实世界 Benchmark 构建，支持 Claude Code / Codex / Cursor / Gemini CLI / Hermes / OpenClaw 等所有主流 Agent。

**关键数据**：95.2% 检索 R@5 · 92% 更少 Token · 53 个 MCP 工具 · 12 个自动钩子 · 零外部数据库 · 950+ 测试

## 快速开始

```bash
npm install -g @agentmemory/agentmemory
agentmemory                    # 启动记忆服务器 :3111
agentmemory demo               # 体验演示项目
```

## 核心功能

### 自动记忆管道

| 钩子 | 时机 | 作用 |
|------|------|------|
| SessionStart | 会话开始 | 注入项目上下文（~1-2K chars）和记忆摘要 |
| PreToolUse | 工具调用前 | 文件上下文+相关记忆+已知Bug查询 |
| PostToolUse | 工具调用后 | 捕获操作观察，自动压缩存储 |
| Stop | 会话结束 | 触发记忆巩固+反思+清理 |

### 记忆能力

- **混合搜索**：语义搜索 + 关键词搜索，95.2% R@5 检索率
- **知识图谱**：自动从记忆中提取实体关系，构建可查询图谱
- **记忆巩固**：定期将短期观察压缩为长期结构化记忆
- **课程衰减**：过时信息自动降权（Lesson Decay）
- **置信度评分**：每条记忆带置信度，Agent 可据此决策
- **Obsidian 自动导出**：记忆可导出为 Obsidian Vault 格式
- **团队共享**：支持 Team ID 模式的多用户记忆共享

### 53 个 MCP 工具

包括 `memory_search`、`memory_save`、`memory_forget`、`memory_slot_*`（可编辑固定记忆槽：persona、user_preferences、project_context 等）、`memory_graph_query` 等。

### 124 个 REST API

本地 `127.0.0.1:3111`，含会话管理、观察捕获、混合搜索、知识图谱查询、团队共享、审计追踪等全功能 API。

## 与 OpenHuman 的关系

OpenHuman 可选对接 agentmemory 作为记忆后端——设置 `memory.backend = "agentmemory"` 后，同一持久存储同时服务 Claude Code、Cursor、Codex、OpenCode 等多个 Agent，实现跨 Agent 统一记忆。

## 适用场景

- 让 AI Agent 记住项目架构、你的偏好、历史决策——不用每次重复解释
- 多 Agent 共享同一记忆后端（Claude Code + Codex + Cursor 共用）
- 构建 Karpathy 式 LLM Wiki 的自动化管道（内置知识图谱+Obsidian 导出）
- 团队协作——Team Mode 支持多人共享记忆

## 评价

- **优点**：95.2% 检索率实锤、92% Token 节省显著降本、53 MCP 工具覆盖全面、零外部数据库部署简单、Obsidian 导出与本知识库直接打通、Apache-2.0 商用友好、与 OpenHuman+ai-engineering-from-scratch 同作者生态完整
- **局限**：本地运行需常驻进程（:3111）、配置项多学习曲线陡、重度使用时有 LLM 调用成本（PostToolUse 压缩走模型）
- **是否值得长期保留**：✅ 重点关注——Agent 持久记忆是 AI 编程的下一个瓶颈突破点，Obsidian 导出功能可直接对接本知识库
