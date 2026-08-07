---
title: ego-lite — AI Agent 专用浏览器（与 Agent 共享登录态，零配置）
description: ego-lite 是一个为 AI Agent 设计的浏览器——Agent 在独立 Space 中运行浏览器自动化，继承 Chrome 登录态，与用户互不干扰
aliases:
  - ego-lite
  - ego-browser
  - ego lite
tags:
  - AI
  - Agent
  - browser-automation
  - ego-lite
  - skills
  - 浏览器自动化
created: 2026-08-02
updated: 2026-08-02
status: 草稿
domain: Core_Ability
source: "https://github.com/citrolabs/ego-lite"
related:
  - "01-OpenCLI"
  - "04-Skills生态全景"
summary: "ego-lite 是为 AI Agent 设计的专用浏览器——Agent 在独立 Space 中运行浏览器自动化，直接继承 Chrome 登录态，用户正常浏览互不干扰。通过 ego-browser skill 暴露 JavaScript 函数接口（非 CLI），复杂任务比 agent-browser 快 2.5× 且 token 消耗更少。"
verified: 2026-08-02
review_after: 2026-11-02
---

# ego-lite — AI Agent 专用浏览器

> [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) 是一个专为 AI Agent 设计的浏览器。Agent 在独立的 **Space** 中运行浏览器自动化任务，直接继承 Chrome 的登录态、Cookie、扩展和书签，而用户在前台正常浏览，两者互不干扰。

## 核心定位

ego-lite 与其他浏览器自动化方案的最大区别：**它不是一个框架，而是一个浏览器**。

| 对比维度 | ego-lite | Browser-Use / agent-browser | ChatGPT Atlas / Perplexity Comet |
|---------|----------|---------------------------|--------------------------------|
| 是否自带浏览器 | ✅ 是 | ❌ 需要额外浏览器驱动 | ✅ 是 |
| 用户可同时使用 | ✅ 独立 Space，互不干扰 | ❌ 争夺标签页 | ❌ 内置 Agent 独占 |
| 继承 Chrome 登录态 | ✅ 一键迁移 | ❌ 需手动配置 | ✅ |
| 多 Agent 并行 | ✅ 多个 Space 同时运行 | ❌ 单任务 | ❌ 单 Agent |
| 外部 Agent 可控 | ✅ 任意 Agent（Claude Code/Codex/Cursor） | ✅ 任意 Agent | ❌ 仅内置 Agent |
| 接口形式 | **JavaScript 函数**（代码基础） | CLI 命令 | 内置 |
| 数据本地存储 | ✅ | ✅ | ❌ |
| 免费 | ✅ | ✅ | ❌ |

## 核心特性

### 1. 代码基础（Code Base）而非 CLI 基础

ego-lite 向 Agent 暴露的能力是 **JavaScript 函数**，Agent 直接编写代码调用。相比传统 CLI 的"调用两条命令→看结果→再调两条命令"循环，复杂任务可 **快 2.5×**，token 消耗大幅降低，任务成功率更高。

### 2. 独立 Space 机制

每个 Agent 获得完全隔离的 Space。用户在前台浏览，Agent 在后台工作。用户可随时查看或接管某个 Space 的运行。

### 3. 多 Agent 并行

多个 Space 同时运行——Claude Code 在 10 个 Space 中并发挖掘线索，Codex 在另外 5 个 Space 中抓取竞品站点，互不冲突。

### 4. 最强页面 Snapshot

基于内核级定制，ego-lite 能生成高质量页面快照（文本模型用来"看到"网页的视图），可靠处理深层嵌套 iframe 等复杂场景。

### 5. ego-browser Skill

`ego-browser` 是连接 AI Agent CLI（Claude Code、Codex、Cursor 等）与 ego-lite 的桥梁。它把浏览器能力封装为一组页内 JavaScript 工具：`snapshot`、`fill`、`click`、`wait`、`navigate`、`capture`。Agent 编写 JavaScript 片段调用这些工具，`ego-browser` 在一次传递中在页面上执行。

### 6. 经验积累（即将推出）

每次成功操作被提炼为可复用的工具和工作流，类似任务后续可快 5×。

## 安装与使用

目前仅支持 **macOS**，Windows 和 Linux 在路线图中。

### 安装方式

1. **下载 DMG**：Apple Silicon 或 Intel 版，安装后自动将 `ego-browser` skill 添加到 Agent 的 skills 目录
2. **npx 安装 skill**：`npx skills add citrolabs/ego-lite`
3. **Agent 自动安装**：在 Agent CLI 中粘贴指令，让 Agent 自行完成安装

首次启动时，ego-lite 询问是否迁移 Chrome 数据——选择"是"，Agent 继承所有现有登录态。

### 使用方式

在 Agent CLI 中键入 `/ego-browser` 后跟任务描述：

```
/ego-browser 帮我登录 x.com 关注 @ego_agent
```

## 与现有方案的对比

### 与 OpenCLI 对比

| 维度 | ego-lite | OpenCLI |
|------|---------|---------|
| 本质 | 专用浏览器 | 网站 CLI 桥接工具 |
| 接口 | JavaScript 函数（代码基础） | CLI 命令 |
| 适用场景 | 复杂多步浏览器自动化 | 快速网站操作、已有适配器的站点 |
| 登录态 | 自动继承 Chrome | 需单独配置 |
| 平台支持 | macOS（Windows/Linux 待定） | 跨平台 |
| 并行能力 | 多 Space 并行 | 单任务 |

### 与 agent-browser 对比（官方基准测试）

ego-lite 在 4 个复杂浏览器自动化任务上，比 Vercel 的 agent-browser 快 2.5×，token 消耗显著更少，且任务越难差距越大。

## 项目状态

- **仓库**：[citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)（MIT 协议）
- **平台**：macOS（Windows/Linux 路线图中）
- **文档**：[lite.ego.app/document/](https://lite.ego.app/document/)
- **社区**：Discord | GitHub Discussions | X/Twitter @ego_agent
- **技术栈**：基于内核级定制的浏览器，JavaScript 工具接口

---

## 相关笔记

- [[01-OpenCLI]] — 另一大浏览器自动化方案，CLI 桥接方式
- [[04-Skills生态全景]] — Agent Skills 生态全貌
- [[数据获取-可用Skills与开源项目]] — 更多数据获取工具列表