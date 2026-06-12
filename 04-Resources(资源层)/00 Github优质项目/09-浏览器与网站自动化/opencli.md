---
title: "OpenCLI 网站→CLI桥接工具"
tags: [GitHub, 开源, AI, CLI, 浏览器, Agent, 自动化]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/jackwener/OpenCLI
zh-CN: https://github.com/jackwener/OpenCLI/blob/main/README.zh-CN.md
related: []
summary: "将任意网站变成 CLI 命令，让 AI Agent 操控已登录浏览器——内置B站/知乎/小红书/Reddit等适配器，22.7k Stars"
---

# OpenCLI 网站→CLI桥接工具

https://github.com/jackwener/OpenCLI

## 基本信息

**类型：** 工具（CLI + 浏览器桥接）
**链接：** https://github.com/jackwener/OpenCLI
**主页：** https://opencli.info/
**NPM：** @jackwener/opencli
**适用领域：** 网站自动化、浏览器操控、AI Agent 浏览器交互
**推荐程度：** ★★★★☆
**Stars：** ~22.7k | Fork 2.3k
**语言：** JavaScript
**许可证：** Apache-2.0

## 是什么

OpenCLI 把**任意网站变成 CLI 命令**——通过 Chrome 扩展桥接已登录浏览器，让人类和 AI Agent 都能用命令行操控网站。

三种使用模式：
- **内置适配器**：B站、知乎、小红书、Reddit、HackerNews、Twitter/X 等开箱即用
- **AI Agent 操控**：安装 `opencli-browser` skill，Claude Code/Cursor 等 Agent 直接操控浏览器——导航、填表、点击、提取
- **自定义适配器**：用 `opencli-adapter-author` skill 为任意网站生成 CLI 适配器

## 快速开始

```bash
npm install -g @jackwener/opencli
# 安装 Chrome 扩展 → opencli doctor
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

## 核心功能

- **网站→CLI**：`opencli bilibili hot` / `opencli zhihu daily` / `opencli reddit top`
- **AI Agent 浏览器操控**：skill 模式，Agent 可导航/点击/填表/提取任意网页
- **Adapter 生成器**：端到端为任意网站生成 CLI 适配器
- **CLI Hub**：统一管理 `gh`/`docker`/`discord` 等本地工具
- **桌面应用适配**：Cursor、Codex、Antigravity、ChatGPT 等 Electron 应用

## 适用场景

- 快速获取多平台热点（B站/知乎/Reddit 一条命令）
- AI Agent 需要操控已登录网站（真正的 browser-use）
- 批量自动化社交媒体操作
- 将团队常用网站操作标准化为 CLI

## 评价

- **优点**：Chrome 登录态桥接是独特优势（AI Agent 无需重新登录）、内置中文平台适配器实用、Apache-2.0、有中文文档
- **局限**：依赖 Chrome 扩展、22.7k Stars 社区尚在早期
- **是否值得长期保留**：✅ 关注——AI Agent 浏览器操控赛道的独特方案
