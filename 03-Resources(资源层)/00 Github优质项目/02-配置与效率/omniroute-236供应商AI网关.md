---
title: "OmniRoute 免费AI网关与智能路由器"
tags: [GitHub, 开源, AI, API, 路由, Token优化, MCP, 免费]
type: 工具
status: 待评估
created: 2026-07-07
updated: 2026-07-07
source: https://omniroute.online
related: [[9router-免费AI路由网关]], [[ECC-Agent全套配置系统]], [[codegraph-预索引代码图谱MCP]]
summary: "开源AI网关，236供应商统一一个端点，RTK+Caveman堆叠压缩省15-95% Token，三层韧性+95 MCP工具+17路由策略，9router的同源升级版"
---

# OmniRoute 免费AI网关与智能路由器

https://omniroute.online

## 基本信息

**类型：** 工具（AI 网关 / 智能路由器）
**主页：** https://omniroute.online
**NPM：** omniroute | Docker: omniroute
**适用领域：** AI API 成本优化、多模型路由、Token 压缩、MCP/A2A 网关
**推荐程度：** ★★★★☆
**语言：** TypeScript
**技术栈：** Next.js 16 + React 19
**许可证：** MIT
**测试覆盖：** 21,000+ tests

> [!info] 与 9router 的关系
> OmniRoute 是 [[9router-免费AI路由网关]] 的同源升级继任者（同样监听 `:20128` 端口，对比表中将 9router 的 RTK 压缩称为 "ours"）。供应商 40+ → 236，路由策略 3-tier → 17 种，压缩 RTK 20-40% → RTK+Caveman 堆叠 15-95%，并新增 MCP Server / A2A / 三层韧性。

## 是什么

OmniRoute 是一个免费、开源的 AI 路由网关。核心理念：**一个端点，所有工具可用，永不因配额或成本停下**。

把 Claude Code / Codex / Cursor 等 16+ 编程 Agent 指向 `localhost:20128/v1`，OmniRoute 在 236 个供应商间自动路由——优先用免费层，配额耗尽毫秒级切换到下一个，同时用 RTK + Caveman 堆叠压缩省 15-95% Token。

一句话：**统一端点 + 自动回落 + 极致压缩 = 接近零成本的 AI 编程。**

## 快速开始（Quickstart）

### 三步上手

```bash
# 1. 安装并启动 —— API 和 Dashboard 同时起来（端口 20128）
npm install -g omniroute
omniroute
# ▸ dashboard ✓ http://localhost:20128/dashboard
# ▸ api......✓ serving on:20128

# 2. 验证模型列表
curl localhost:20128/v1/models
# ✓ models listed 🎉
```

1. **Install & run** — 一个 `npm install` 即启动，API 与 Dashboard 同时运行在 20128 端口
2. **Connect a FREE provider** — 打开 Dashboard，从 90+ 免费层中选一个登录，无需信用卡、无需付费 API Key
3. **Point your IDE** — 把工具的 base URL 设为 `localhost:20128/v1`，填入 Dashboard Key

### 配置 IDE / CLI 工具

```
Base URL: http://localhost:20128/v1
API Key:  ‹from dashboard›
```

一个端点，所有工具都指向这里。OpenAI ↔ Claude ↔ Gemini ↔ Responses API 格式自动互转。

### 接入为 MCP Server

```bash
claude mcp add omniroute --type http --url http://localhost:20128/api/mcp/stream
# ✓ omniroute connected — 95 tools available
```

### 其他安装方式

| 方式 | 命令 / 说明 |
|------|------------|
| npm | `npm i -g omniroute` |
| Docker | `docker run omniroute` |
| Desktop | Electron app · Win/Mac/Linux |
| ARM | arm64 · Raspberry Pi ready |
| Termux | `pkg install nodejs` · Android 可跑 |
| PWA | 浏览器安装 · 离线可用 |
| OpenCode 插件 | `@omniroute/opencode-plugin` |
| 源码 | `git clone` · `npm run dev` |

## 核心功能

### 236 供应商 · 一个端点

最完整的开源路由目录。90+ 免费层，11 个永久免费。

| 类别 | 数量 | 代表 |
|------|------|------|
| OAuth | 20 | Claude Code, Codex, Cursor, Gemini CLI, Antigravity |
| API-key | 158 | OpenAI, Groq, NVIDIA, Cerebras, Mistral |
| Free forever | 11 | Kiro, Qoder, Pollinations, LongCat |
| Local | 11 | Ollama, LM Studio, vLLM |

能力分布：23 Web · 11 Search · 7 Audio · 24 Image · 14 Video · 14 Embeddings · 8 Rerank · 6 Music

**11 个永久免费层：**

| 供应商 | 配额 |
|--------|------|
| Kiro | 50 cr |
| Qoder | ∞ |
| LongCat | 50M/天 |
| Cerebras | 1M/天 |
| NVIDIA | 40 rpm |
| Pollinations | 无需 Key |

> 每月约 **~1.6B 免费_tokens**，pool-deduped 诚实计数（共享账户只算一次，不虚标）。

### 17 种路由策略

内置 `auto` 及 `/coding` `/fast` `/cheap` `/offline` `/smart` 快捷模式，亦可自定义。按目标分组：

| 目标 | 策略 |
|------|------|
| 🪫 榨干订阅 | `priority` `fill-first` |
| ⚖️ 均摊负载 | `round-robin` `p2c` `least-used` |
| 💸 最便宜优先 | `cost-optimized` |
| 🧵 上下文感知 | `context-relay` `context-optimized` |
| 🎲 随机化 | `random` `strict-random` |
| 🧠 智能自适应 | `auto` `lkgp` `reset-aware` `reset-window` |

`auto` 采用 **9 因子评分** + last-known-good + reset-aware 窗口，Tier 1/2/3 毫秒级回落。

### RTK + Caveman 堆叠压缩

7 层压缩管道，按顺序堆叠、可按 combo 混搭：

1. **Session-Dedup** — 跨轮次重复内容去重
2. **CCR** — 大块归档，按需检索
3. **RTK** — 智能工具结果过滤与去重
4. **Headroom** — JSON 数组无损表格压缩
5. **Relevance** — 相对最近查询的抽取式句子评分
6. **Caveman** — 规则散文压缩，最高 ~75%
7. **LLMLingua-2** — ML 语义剪枝（ONNX），代码安全

**压缩档位：** Lite 15% · Standard 30% · Aggressive 50% · Ultra 75% · RTK 60–90% · Stacked 78–95%

**输出样式（可组合）：** Terse prose · Less code (YAGNI) · Terse CJK 文言

**控制层级：** header › combo › profile › adaptive › default（支持命名 profile、可视化 Compression Studio、Anthropic Context Editing、自适应预算拨盘、按请求 header `x-omniroute-compression`、离线 eval、按 token 阈值自动触发）

### 三层韧性（3-Layer Resilience）

`model ⊂ connection ⊂ provider` —— 在正确的层级失败，绝不波及整体。懒恢复，无后台定时器。

| 故障 | 隔离层级 | 效果 |
|------|---------|------|
| 供应商宕机 | Circuit breaker（per provider） | combo 路由跳过该供应商直到恢复 |
| Key 失效 | Cooldown（per connection） | 同供应商其他 Key 继续服务 |
| 模型配额受限 | Lockout（per model） | 其他模型继续服务 |

超越其他工具的扁平 3-tier 回落。

### 3 级代理 + TLS 隐身

- **代理作用域：** Global · per-provider · per-connection；支持 SOCKS5 & HTTP(S)；1proxy marketplace 一键接入
- **TLS 隐身：** JA3/JA4 指纹（via wreq-js），按供应商匹配真实 CLI 指纹，IP 跨请求保持，IPv4/IPv6 出口控制 —— 让上游识别不出你是代理

### 隐私与本地优先

- SQLite 落盘 · AES-256 加密凭证
- 无遥测、无需账户
- 自托管，数据不离本机

### 网关即平台

- **MCP Server** — 把整个网关暴露为 **95 个工具 / 30 个 scope**，走 stdio / HTTP / SSE
- **A2A Server** — Agent-to-Agent 服务端，**6 个 skills**（智能路由、配额、发现、成本分析、健康上报），JSON-RPC 2.0 + Agent Card
- **Cloud Agents** — 一个接口驱动 Codex / Cursor / Devin / Jules：建任务、批计划、流式结果
- **嵌入式 sidecar** — Dashboard 内直接跑 Bifrost (Go relay)、[[9router-免费AI路由网关]]、CLIProxy，或完整集群 profile
- **知识接入** — Notion & Obsidian 作为 MCP 工具，笔记/Vault 成为任意模型的一等上下文
- **Guardrails** — 每条路由 prompt-injection 防护，可选 PII 脱敏与内容过滤归一化
- **游戏化** — 连续记录、成就、实时节省展示

## 与同类对比

| 特性 | OmniRoute | 9router | LiteLLM | CLIProxyAPI |
|------|-----------|---------|---------|-------------|
| 供应商 | **236** | 40+ | 100+ | 8+ upstreams |
| 路由策略 | **17** | 3-tier | retry / priority | round-robin · fill-first |
| Tier 1/2/3 回落 + UI | ✅ | ✅ | manual | ⚠ multi-account |
| Token 压缩 | **RTK+Caveman 15–95%** | RTK 20–40% | ❌ | ❌ HTTP brotli only |
| 内置 MCP Server | **✅ 95 工具（暴露网关）** | ❌ | ⚠ client | ❌ |
| A2A 协议 | **✅ server, 6 skills** | ❌ | ⚠ client | ❌ |
| 云 Agent（Codex/Cursor/Devin/Jules） | ✅ | ❌ | ❌ | ⚠ sidecar |
| 韧性层数 | **3（breaker+cooldown+lockout）** | ⚠ cooldown | ⚠ cooldown | ⚠ cooldown |
| 记忆（FTS5 + 向量） | ✅ | ❌ | ⚠ semantic cache | ❌ |
| Guardrails（PII/注入/视觉） | ✅ | ❌ | ✅ | ⚠ cloak |
| Eval 框架 | ✅ | ❌ | ❌ | ❌ |
| TLS 指纹隐身 | **✅ wreq-js** | ❌ | ❌ | ✅ utls |
| Dashboard | Next.js 16 | Next.js 16 | Next.js | Next.js / React |
| i18n | **42** | 4 | ❌ | 3 |
| OAuth 供应商 | **16+** | 5 | SSO | 6 (CLI auth) |
| 自托管 | ✅ | ✅ | ✅ | ✅ |
| 许可证 | **MIT** | MIT | MIT + Comm | MIT |
| 技术栈 | **TS / Next 16** | Node / Next 16 | Python | Go |

> **诚实说明：** LiteLLM 是 MCP/A2A *客户端*（连接/调用）；OmniRoute 是 *服务端*（把自身网关暴露为 95 工具 / 6 skills）。CLIProxyAPI 也有 TLS 隐身（utls）。9router 有 RTK 压缩（20-40%），堆叠的 RTK+Caveman（15-95%）是 OmniRoute 的。

## 适用场景

- **AI 编程重度用户** —— 把每月 $20-50 的 API 费用降到接近零
- **配额焦虑** —— 免费层兜底 + 毫秒级回落，永远不再"本月配额已用完"
- **多工具统一** —— Claude Code / Codex / Cursor / Cline / Copilot 等共用一个端点
- **地区受限** —— 3 级代理 + TLS 隐身绕过 AI 区域封锁
- **Token 焦虑** —— 工具密集会话平均省 ~89% Token
- **MCP 生态** —— 把网关本身作为 95 工具 MCP Server 接入 Claude Code 等
- 与 [[ECC-Agent全套配置系统]] + [[codegraph-预索引代码图谱MCP]] 组成"降本增效三件套"：ECC 优化 Agent 效率 → codegraph 减少工具调用 → OmniRoute 降低 API 成本

## 评价

- **优点**：236 供应商目录最全；17 种路由策略 + 9 因子智能评分远超同类的扁平 3-tier；RTK+Caveman 7 层堆叠压缩 15-95% 实打实省钱；三层韧性（breaker+cooldown+lockout）故障隔离精细；唯一同时内置 MCP Server（95 工具）+ A2A Server 的开源路由；本地优先 + AES-256 + 无遥测；MIT 开源；21,000+ 测试背书
- **局限**：依赖第三方免费供应商稳定性；作为中间代理增加延迟；功能庞杂上手成本高于 9router；Stars/生态成熟度待观察（新项目）
- **是否值得长期保留**：✅ 重点评估——若已用 [[9router-免费AI路由网关]]，OmniRoute 是其功能超集升级版，可考虑迁移；功能全面性在开源 AI 路由器中目前无出其右

## 关联

- [[9router-免费AI路由网关]] — 同源前作，更轻量，三级回落 + RTK 20-40% 压缩
- [[ECC-Agent全套配置系统]] — Agent 配置体系，效率侧互补
- [[codegraph-预索引代码图谱MCP]] — 代码图谱 MCP，减少工具调用次数
- [[agentmemory-Agent持久记忆系统]] — Agent 持久记忆（OmniRoute 内置 FTS5+Qdrant 混合召回可对比）
