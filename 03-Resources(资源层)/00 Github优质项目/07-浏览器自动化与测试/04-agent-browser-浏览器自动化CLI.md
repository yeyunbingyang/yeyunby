---
title: "Agent Browser 浏览器自动化 CLI"
tags: [GitHub, 开源, AI, 浏览器, 自动化, CLI, Vercel]
type: 工具
status: 待评估
created: 2026-07-06
updated: 2026-07-06
source: https://github.com/vercel-labs/agent-browser
related: [[opencli-网站CLI桥接工具], [playwright]]
summary: "Vercel 出品的 AI Agent 浏览器自动化 CLI——原生 Rust 实现，支持无障碍树快照/点击/填表/截图/JS 执行，npm/Homebrew/Cargo 三路安装，37.9k Stars"
---

# Agent Browser 浏览器自动化 CLI

https://github.com/vercel-labs/agent-browser

## 基本信息

**类型：** 工具（CLI + 浏览器自动化）
**链接：** https://github.com/vercel-labs/agent-browser
**安装：** `npm install -g agent-browser` + `agent-browser install`
**适用领域：** AI Agent 浏览器操控、网页自动化测试
**推荐程度：** ★★★★☆
**Stars：** ~37.9k | Fork 2.4k
**语言：** Rust + TypeScript
**许可证：** 未明确标注

## 是什么

Vercel Labs 出品的**浏览器自动化 CLI**，专为 AI Agent 设计。原生 Rust 实现，速度快。核心交互模式是无障碍树快照（accessibility tree）→ 按 ref ID 操作元素，而非传统 CSS/XPath 选择器。

## 快速开始

```bash
npm install -g agent-browser
agent-browser install   # 首次下载 Chrome for Testing
agent-browser open example.com
agent-browser snapshot                    # 获取无障碍树（含 ref 编号）
agent-browser click @e2                   # 按 ref 点击
agent-browser fill @e3 "test@example.com" # 按 ref 填表
agent-browser screenshot page.png
agent-browser close
```

也支持传统选择器：`agent-browser click "#submit"`。

## 核心功能

### 浏览操控
- `open`/`goto`/`navigate` — 打开页面
- `click`/`dblclick`/`focus`/`hover` — 元素交互
- `type`/`fill`/`press`/`keyboard` — 键盘输入
- `scroll`/`scrollintoview` — 滚动
- `drag`/`upload`/`select`/`check` — 表单操作
- `screenshot`/`pdf` — 页面截图/PDF（支持标注编号）

### AI 友好
- `snapshot` — 无障碍树快照（AI 最佳输入）
- `read` — 获取页面可读文本（无需启动浏览器）
- `chat` — 自然语言浏览器操控（单次/REPL 模式）
- `eval` — 执行 JavaScript
- `find` — 语义定位器（按 role/text/label/placeholder/alt/title/testid）

### 信息获取
- `get text`/`get html`/`get value`/`get attr` — 元素属性
- `get title`/`get url` — 页面信息
- `get box`/`get styles` — 布局信息
- `is visible`/`is enabled`/`is checked` — 状态检查

### 高级
- `stream enable` — WebSocket 实时流
- `connect` — CDP 连接已有浏览器
- `close --all` — 关闭所有会话

## 安装方式

| 方式 | 命令 |
|------|------|
| npm 全局 | `npm install -g agent-browser` |
| Homebrew | `brew install agent-browser` |
| Cargo | `cargo install agent-browser` |
| 源码 | `pnpm install && pnpm build && pnpm build:native` |

## 适用场景

- AI Agent 需要操控浏览器（填表/爬取/测试）
- 替代 Playwright/Puppeteer 的轻量方案
- 无障碍树快照模式适合 AI 解析

## 评价

- **优点**：Rust 原生性能好、无障碍树快照模式 AI 友好、多安装方式、Vercel 背书
- **局限**：依赖 Chrome for Testing、无障碍树模式对复杂 SPA 可能不完整
- **是否值得长期保留**：✅ 关注——AI 浏览器自动化的轻量方案
