---
title: "9Router 免费AI路由与Token节省器"
tags: [GitHub, 开源, AI, API, 路由, Token优化, 免费]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-07-16
source: https://github.com/decolua/9router
zh-CN: https://github.com/decolua/9router/blob/main/i18n/README.zh-CN.md
related: [[ECC-Agent全套配置系统], [codegraph-预索引代码图谱MCP]]
summary: "免费AI编码路由网关，对接40+供应商100+模型，RTK压缩节省20-40% Token，三级自动回落（订阅→廉价→免费），14.4k Stars"
---

# 9Router 免费AI路由与Token节省器

https://github.com/decolua/9router

## 基本信息

**类型：** 工具（API 路由网关）
**链接：** https://github.com/decolua/9router
**主页：** https://9router.com
**NPM：** 9router | Docker: decolua/9router
**适用领域：** AI API 成本优化、多模型路由、Token 节省
**推荐程度：** ★★★★☆
**Stars：** ~14.4k | Fork 2.2k
**语言：** JavaScript
**许可证：** MIT

## 是什么

9Router 是一个智能 AI API 路由网关。核心理念：**免费无限编程**——把你的 Claude Code / Codex / Cursor 等工具接到 9Router，它会自动在不同供应商间路由，优先用免费的，不行再用廉价的，最后才用付费订阅。同时通过 RTK 压缩机制节省 20-40% Token。

一句话：**永远不会因为配额用完或太贵而停下手里的代码。**

## 快速开始

```bash
npm install -g 9router
9router
# Dashboard 自动打开 http://localhost:20128
```

然后在 Claude Code / Codex / Cursor 等工具中设置：
```
Endpoint: http://localhost:20128/v1
API Key: [从 Dashboard 复制]
Model: kr/claude-sonnet-4.5   # 免费！
```

## 核心功能

### 三级自动回落

```
你的 CLI 工具
    ↓
  9Router (:20128)
    ↓
[Tier 1: 订阅] Claude Code / Codex / Copilot / Cursor
    ↓ 配额用完
[Tier 2: 廉价] GLM ($0.6/1M) / MiniMax ($0.2/1M) / Kimi ($9/月)
    ↓ 预算用完
[Tier 3: 免费] Kiro (Claude免费无限) / OpenCode Free (无需注册) / Vertex ($300赠金)

零停机自动切换
```

### RTK Token 节省器

自动压缩 `tool_result` 内容，每次请求节省 **20-40% Token**。移植自 [rtk-ai/rtk](https://github.com/rtk-ai/rtk) 的压缩管道。

### 40+ 供应商 · 100+ 模型

| 层级  | 代表供应商                               | 代表模型                                      |
| --- | ----------------------------------- | ----------------------------------------- |
| 订阅  | Claude Code, Codex, Copilot, Cursor | Claude Opus 4.7, GPT-5.5, Gemini 3.1      |
| 廉价  | GLM, MiniMax, Kimi                  | GLM-5.1 ($0.6/M), MiniMax-M2.7 ($0.2/M)   |
| 免费  | Kiro, OpenCode Free, Vertex         | Claude Sonnet 4.5 (免费), DeepSeek 3.2 (免费) |

### 其他能力

- **格式转换**：OpenAI ↔ Claude API 格式自动互转
- **配额追踪**：Dashboard 可视化配额消耗
- **Token 自动刷新**：OAuth Token 过期自动续
- **多账户轮询**：同供应商多账户负载均衡
- **Combo 模式**：自定义回落链 `cc/claude-opus → glm/glm-5.1 → kr/claude-sonnet`
- **支持全部主流工具**：Claude Code / Codex / Cursor / Cline / Copilot / Gemini / OpenCode / OpenClaw

## 技术栈

- **Runtime**：Node.js 20+
- **框架**：Next.js 16 + React 19 + Tailwind CSS 4
- **数据库**：SQLite
- **认证**：OAuth 2.0 (PKCE) + JWT + API Keys

## 适用场景

- AI 编程重度用户——每月 API 费用 $50-200，用 9Router 降到接近零
- 多工具切换——Claude Code 写代码、Cursor 做 Review、Codex 做部署，统一走 9Router
- 配额焦虑——免费层兜底，永远不会「本月配额已用完」
- 与 ECC + CodeGraph 形成「省钱三件套」：ECC 优化 Agent 效率 → CodeGraph 减少工具调用 → 9Router 降低 API 成本

## 评价

- **优点**：三级回落设计精巧、免费层覆盖 Claude/GPT/Gemini、RTK 压缩 20-40% 实打实省钱、Dashboard 可视化友好、支持全部主流 AI 编程工具、MIT 开源
- **局限**：依赖第三方免费供应商稳定性、部分供应商可能需要科学上网、作为中间代理增加延迟
- **是否值得长期保留**：✅ 重点使用——省钱效果立竿见影，与 ECC + CodeGraph 组成完整降本方案
