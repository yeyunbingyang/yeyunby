---
title: "code-graph-rag 代码库知识图谱 RAG"
domain: IT_Technology
tags: [GitHub, 开源, RAG, 知识图谱, 代码理解, MCP, Python]
status: 草稿
created: 2026-08-12
updated: 2026-08-12
source: "https://github.com/vitali87/code-graph-rag"
related: ["[[31-TencentDB-Agent-Memory-面向长任务多步Agent的分层记忆系统支持符号记忆]]", "[[01-langchain-+⭐构建LLM应用的标准框架支持]]", "[[Github优质项目-MOC]]"]
summary: "面向 monorepo 的终极 RAG：用 AI + 知识图谱（tree-sitter + Memgraph）查询、理解和编辑多语言代码库，提供 MCP Server，是个人代码库『Code Graph』环节的核心方案。"
---

# code-graph-rag 代码库知识图谱 RAG

> [!abstract] 一句话定位
> 面向 monorepo 的 RAG 方案——借助 AI 与知识图谱，让 Agent 能查询、理解、编辑多语言代码库。

## 基本信息

| 项目 | 内容 |
|---|---|
| 仓库 | [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) |
| 网站 | https://code-graph-rag.com |
| 语言 | Python |
| 许可证 | MIT |
| 项目热度 | 约 4k Stars（2026-08-12 抓取） |
| 核心技术 | tree-sitter、Memgraph（图数据库）、MCP Server |
| 主题 | code-analysis, codebase-search, knowledge-graph, mcp-server, monorepo, semantic-search |

## 核心能力

- 把代码库解析成**知识图谱**（AST + 依赖关系），而非纯向量检索。
- 跨多语言理解 monorepo，支持查询、理解、编辑代码。
- 以 **MCP Server** 形式暴露给 Claude Code 等 Agent，可直接接入工作流。

## 为什么值得研究（⭐⭐⭐⭐⭐）

- **个人代码库知识图谱**：比向量 RAG 更准——图结构保留代码的符号依赖关系，适合"个人程序开发"场景。
- 展示 **MCP + 图数据库 + RAG** 的组合范式，是代码理解类 Agent 工具的先进形态。

## 在「资料 → Skill → Memory → Agent」体系中的位置

**Code Graph 环节**：为个人代码库建立可检索的知识图谱，是体系里"程序开发知识"的结构化记忆层。与 Agent-Memory 的 Code-Graph 记忆资产互为印证。

## 相关

- [[31-TencentDB-Agent-Memory-面向长任务多步Agent的分层记忆系统支持符号记忆]]（同样含 Code-Graph 记忆资产）
- [[01-langchain-+⭐构建LLM应用的标准框架支持]]（通用 RAG 框架对照）
- [[Github优质项目-MOC]]
