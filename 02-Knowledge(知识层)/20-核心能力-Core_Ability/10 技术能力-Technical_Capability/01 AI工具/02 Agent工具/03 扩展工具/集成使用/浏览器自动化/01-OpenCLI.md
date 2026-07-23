---
title: OpenCLI — 网站 CLI 桥接与浏览器自动化工具
description: 将任意网站/桌面应用转为 CLI 命令的 AI Agent 工具——100+ 站点适配器、浏览器自动化（Browser Use）、配套 Skills 体系
aliases:
  - OpenCLI
  - opencli
tags:
  - AI
  - Agent
  - OpenCLI
  - CLI
  - browser-automation
  - skills
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
source: https://github.com/jackwener/OpenCLI（22.7k★）
related:
  - "04-Skills生态全景"
  - "03-通用skills最佳实践"
summary: "OpenCLI 是一个把网站、浏览器会话、Electron 应用和本地工具统一变成 CLI 接口的 AI Agent 工具，通过 6 个配套 Skills 让 AI Agent 直接操控网站。与 agent-browser 并列为两大浏览器自动化方案。"
---

# OpenCLI — 网站 CLI 桥接与浏览器自动化工具

> OpenCLI 是 [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)（22.7k★）的中文使用笔记。它把网站、浏览器会话、Electron 应用和本地工具，统一变成适合**人类与 AI Agent** 使用的 CLI 接口。
>
> 在 Skills 生态中属于`浏览器自动化层`，与 `agent-browser`（Vercel）并列为两大浏览器自动化方案。

---

## 一句话

OpenCLI 可以用同一套 CLI 做三类事情：

1. **直接使用现成适配器** — B站、知乎、小红书、Twitter/X、Reddit 等 [100+ 站点](#常用站点及命令) 开箱即用
2. **让 AI Agent 操作任意网站** — 通过安装 `opencli-browser` skill，Agent 用你的已登录浏览器导航、点击、填表、提取
3. **把新网站写成 CLI** — 站点侦察 → API 发现 → 字段解码 → 适配器验证一条龙

它还是一个 **CLI 枢纽**：可以把 `gh`、`docker`、`obsidian`、`notion` 等本地工具统一注册到 `opencli` 下，也可以通过桌面适配器控制 Cursor、Codex、ChatGPT 等 Electron 应用。

---

## 安装

```bash
node --version  # 要求 >= 20
npm install -g @jackwener/opencli
```

安装后需要安装 Chrome Browser Bridge 扩展（[Chrome Web Store](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk)）：

```bash
opencli doctor  # 验证环境连通性
```

---

## AI Agent 配置（Skills）

OpenCLI 配套 **6 个 Skills**，安装后 AI Agent 可以自动调用（详见 [[04-Skills生态全景#6.7 OpenCLI]]）：

```bash
npx skills add jackwener/opencli --skill opencli-browser
npx skills add jackwener/opencli --skill opencli-adapter-author
npx skills add jackwener/opencli --skill opencli-autofix
npx skills add jackwener/opencli --skill opencli-usage
```

| Skill | 场景 | 典型指令 |
|-------|------|---------|
| **opencli-browser** | 实时驱动 Chrome 页面——导航、填表单、点击、抓取 | "帮我看看小红书的通知" |
| **opencli-adapter-author** | 为新站点写可复用适配器 | "帮我做一个抖音热门的适配器" |
| **opencli-autofix** | 内置命令失败时修复已有适配器 | "`opencli zhihu hot` 返回空了" |
| **opencli-usage** | 所有命令和站点的快速参考 | "OpenCLI 有哪些 Twitter 命令？" |

安装后，AI Agent 内部自动处理所有 `opencli browser` 命令——你只需要用自然语言描述想做的事。

---

## 工作原理

```
Agent 收到请求 → 调用 opencli-browser skill
    → OpenCLI daemon → Chrome Browser Bridge 扩展
    → 操控已登录浏览器 → 返回结构化数据给 Agent
```

### 标准抓取流程

核心原则：**先观察（`state`/`find`），再定位（`ref`/`selector`），后提取（`get`/`extract`/`network`），每步验证**。

```bash
opencli browser demo open <url>          # 打开页面
opencli browser demo state               # 获取 DOM 快照（带 ref 编号）
opencli browser demo find --css ".item"  # 定位元素
opencli browser demo get text <ref>      # 提取数据
```

**拦截 API 优先于 DOM 抓取**：如果页面通过 XHR/Fetch 获取数据，优先用：

```bash
opencli browser demo network --filter "title"
opencli browser demo network --detail <key>  # 获取完整 JSON
```

API 返回结构化 JSON，无 DOM 漂移问题，比 scraping DOM 稳定省 Token。

> 完整操作流程含动态翻页、表单填写、复杂控件处理、诊断指令等见 [[02-opencli-browser|OpenCLI 浏览器抓取操作参考]]。

---

## 常用站点及命令

| 站点 | 示例命令 |
|------|---------|
| 小红书 | `opencli xiaohongshu search "AI"`、`opencli xiaohongshu hot` |
| B站 | `opencli bilibili hot`、`opencli bilibili search "教程"` |
| 知乎 | `opencli zhihu hot`、`opencli zhihu search "Agent"` |
| Twitter/X | `opencli twitter trending`、`opencli twitter timeline` |
| Reddit | `opencli reddit hot`、`opencli reddit search "Claude"` |
| HackerNews | `opencli hackernews top --limit 10` |
| LinkedIn | `opencli linkedin search`、`opencli linkedin profile-read` |

运行 `opencli list` 查看完整注册表（100+ 站点）。

### 下载支持

| 平台 | 内容 | 命令 |
|------|------|------|
| 小红书 | 图片/视频 | `opencli xiaohongshu download <url>` |
| B站 | 视频 | `opencli bilibili download BV1xxx` |
| Twitter/X | 图片/视频 | `opencli twitter download <username>` |
| 知乎 | 文章 MD | `opencli zhihu download <url>` |
| 微信公众号 | 文章 MD | `opencli weixin download <url>` |

---

## 输出格式

所有命令支持 `--format` / `-f`：`table`（默认）、`json`、`yaml`、`md`、`csv`。

---

## 外部 CLI 枢纽

将本地命令行工具统一接入 `opencli <tool> ...`：`gh` · `docker` · `vercel` · `obsidian` · `notion` · `tg(Telegram)` · `discord`

注册：`opencli external register <name>`

---

## 对比：OpenCLI vs agent-browser

| 维度 | OpenCLI | agent-browser（Vercel） |
|------|---------|----------------------|
| 安装方式 | `npm install` + Chrome 扩展 | `npm install -g` |
| 浏览器通信 | Browser Bridge 扩展 | CDP 直连 |
| 站点适配器 | 100+ 内置适配器 | 无内置适配器 |
| AI Agent Skill | 6 个配套 Skill | CLI 直接调用 |
| Hub 能力 | 注册本地 CLI + Electron 适配 | 专注浏览器自动化 |
| Stars | 22.7k★ | 37.9k★ |

**选型建议**：需要开箱即用站点适配器 → OpenCLI；需要纯轻量浏览器自动化 → agent-browser。

---

## 关联笔记

- [[浏览器自动化/02-opencli-browser|OpenCLI 浏览器抓取操作参考]] — 浏览器自动化标准抓取流程
- [[04-Skills生态全景#6.7 OpenCLI]] — 在 Skills 生态中的定位
- [[03-通用skills最佳实践]] — Skills 使用心法
- [[Claude-Code操作手册]] — Claude Code 中调用 OpenCLI 的上下文
