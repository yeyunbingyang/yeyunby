---
title: OmniRoute 完全指南
domain: Core_Ability
tags: [OmniRoute, AI网关, 模型路由, Token压缩, MCP, 免费]
status: 稳定
created: 2026-07-22
updated: 2026-07-22
summary: "OmniRoute v3.8.49 完全指南——278供应商/90+免费/~1.53B免费Token/月，18路由策略、RTK+Caveman压缩省15-95%Token、104 MCP工具、Auto-Combo智能路由"
source: GitHub README v3.8.49 + 官方文档
related: ["04-模型路由策略", "01-9router-快速入门手册", "02-CC-Switch-模型管理器", "模型及代理-MOC", "MCP深度解析与本地模型企业级应用指南"]
---

# OmniRoute 完全指南

> **版本：v3.8.49** | 24.1k⭐ | MIT 开源 | 500+ 贡献者
>
> 免费 AI 网关：一个端点，278 供应商，90+ 免费，~1.53B 免费 Token/月。

---

## 一、核心定位

OmniRoute 是一个**开源 AI 网关**，将所有 AI 模型统一到一个 OpenAI 兼容端点。它不是"又一个路由器"——它是 AI 工具的**总接线板**。

```
你的 IDE / CLI（Claude Code / Codex / Cursor / Cline…）
   │
   └── http://localhost:20128/v1  （一个端点）
         │
         └── OmniRoute 智能路由器
               ├── RTK + Caveman 压缩（省 15-95% Token）
               ├── 18 种路由策略（包括自动最优选择）
               ├── 3 层韧性（熔断 + 冷却 + 锁定）
               ├── TLS 指纹隐身（JA3/JA4）
               └── 278 供应商 → 90+ 免费 → 500+ 模型
```

---

## 二、关键数据（v3.8.49）

| 指标 | 数值 | 备注 |
|------|------|------|
| **供应商** | 278 | 从 OpenAI 到本地 Ollama |
| **免费供应商** | 90+（40+ 永久免费） | 无需信用卡 |
| **免费 Token/月** | ~1.53B | 聚合所有免费层级 |
| **模型数** | 500+ | Claude / GPT / Gemini / Kimi / DeepSeek … |
| **路由策略** | 18 种 | priority / weighted / cost-optimized / fusion… |
| **MCP 工具** | 104 | 3 传输方式，31 作用域 |
| **压缩率** | 15-95%（平均 ~89%） | RTK + Caveman 堆叠 |
| **多语言** | 43 种 | 含简体中文 |
| **GitHub Stars** | 24.1k | 2026年7月 |

---

## 三、快速开始

### 安装

```bash
# npm
npm install -g omniroute

# Docker
docker run -d -p 20128:20128 diegosouzapw/omniroute

# 一键启动
omniroute launch
```

### 零配置使用

启动后，将你的 AI 工具（Claude Code / Codex / Cursor）的 API endpoint 改为：

```
http://localhost:20128/v1
```

然后设置模型为 `auto`——OmniRoute 自动从已连接的供应商中选择最优模型。

---

## 四、Auto-Combo：智能模型组合

OmniRoute 最核心的特性——**Combo**（模型链），按优先级自动切换：

| Combo ID | 优化目标 |
|----------|---------|
| `auto` | 🎯 平衡默认（LKGP：粘住最后成功的目标） |
| `auto/coding` | 🧑‍💻 代码生成质量优先 |
| `auto/fast` | ⚡ 最低延迟 |
| `auto/cheap` | 💰 每 Token 最便宜 |
| `auto/offline` | 🔋 最多配额余量 |
| `auto/smart` | 🔭 质量优先 + 10% 探索新模型 |

**4 层自动 Fallback：**
```
Subscription（订阅配额）
  → API Key（按量付费）
    → Cheap（廉价模型 $0.2-0.5/M）
      → Free（完全免费）
```

---

## 五、18 种路由策略

| # | 策略 | 说明 |
|---|------|------|
| 1 | `priority` | 顺序消耗列表，用完一个再下一个 |
| 2 | `fill-first` | 填满配额再移动 |
| 3 | `weighted` | 按权重随机 |
| 4 | `round-robin` | 循环轮询 |
| 5 | `p2c` | 两次随机选负载低的 |
| 6 | `least-used` | 选当前负载最低的 |
| 7 | `random` | 均匀随机（去重） |
| 8 | `strict-random` | 随机（允许重复） |
| 9 | `cost-optimized` | 💸 最小化每次请求成本 |
| 10 | `headroom` | 剩余配额最多的 |
| 11 | `reset-window` | 配额窗口即将重置的 |
| 12 | `reset-aware` | 按重置时间排序 |
| 13 | `context-relay` | 🧠 长对话上下文接力 |
| 14 | `context-optimized` | 匹配上下文大小 |
| 15 | `lkgp` | 粘住最后成功路径 |
| 16 | `auto` | 🤖 12 因子实时评分 |
| 17 | `fusion` | 🧬 多模型并行 + 裁判合成 |
| 18 | `pipeline` | 🔗 链式：每步输出喂下一步 |

---

## 六、Token 压缩：RTK + Caveman

OmniRoute 的杀手级特性——**堆叠压缩引擎**，省 15-95% Token：

| 引擎 | 原理 | 节省 |
|------|------|:---:|
| **RTK** | 工具输出保留关键字段，裁掉冗余 | 40-80% |
| **Caveman** | 上下文压缩为精简表示 | 30-70% |
| **堆叠** | RTK → Caveman 串联 | **15-95%（平均 ~89%）** |

> 11 个可组合压缩引擎，含 LLMLingua-2、Ultra 双层、omniglyph、GCF v3.2。

---

## 七、3 层韧性架构

| 层 | 机制 | 触发条件 |
|----|------|---------|
| **L1 Provider 熔断** | 整个供应商熔断 | 408/5xx：OAuth 3次 / API 5次 |
| **L2 连接冷却** | 单 key 退避 | 429 限流 → 指数退避（base 3-5s） |
| **L3 模型锁定** | 单模型禁用 | 单模型 429 / 404 → 只锁该模型 |

**Quota-Share**：将一个订阅配额公平分配给团队多个 key，支持权重、硬/软限制、突发借用。

---

## 八、集成能力

### 兼容的 CLI / IDE（26+）

Claude Code · Codex CLI · Cursor · Cline · Kilo Code · Roo Code · Continue · Aider · Copilot · DeepSeek TUI · Windsurf · OpenCode … 

全部通过一个端点 `http://localhost:20128/v1` 连接。

### MCP Server（内置 104 工具）

```yaml
# 3 种传输：stdio / HTTP / SSE
# 31 作用域：文件系统 / Git / 数据库 / 浏览器 / API …
```

### A2A 协议

6 个 Skills，JSON-RPC 2.0 → Agent 之间协作。

### 其他

- **Memory**：FTS5 + 向量，可选 int8 量化
- **Guardrails**：PII 检测 / Prompt 注入防护 / 视觉内容过滤
- **TLS 隐身**：JA3/JA4 指纹伪装（wreq-js）
- **Web Search**：DuckDuckGo 免费后备搜索
- **新端点**：`/v1/ocr`（Mistral OCR）、`/v1/audio/translations`
- **远程模式**：作用域 Token 驱动远程 OmniRoute
- **多平台**：Web · Desktop（Electron） · Termux · PWA

---

## 九、与竞品对比

| 特性 | OmniRoute | LiteLLM | OpenRouter |
|------|:---:|:---:|:---:|
| 供应商数 | **278** | ~100 | ~200 |
| 免费供应商 | **90+** | 1-5 | ~5 |
| 路由策略 | **18** | 1-3 | 1 |
| Token 压缩 | **RTK+Caveman 15-95%** | 无 | 无 |
| 内置 MCP | **104 工具** | 无 | 无 |
| TLS 隐身 | ✅ | ❌ | ❌ |
| 本地优先 | ✅ | ✅ | ❌ |
| 开源 | MIT | MIT | 部分 |

---

## 十、配置片段

### Docker 快速部署

```bash
docker run -d \
  --name omniroute \
  -p 20128:20128 \
  -v ~/.omniroute:/app/data \
  diegosouzapw/omniroute
```

### 添加 API Key

```bash
# 通过 CLI
omniroute keys add deepseek sk-xxx
omniroute keys add openai sk-xxx

# 或在 Dashboard http://localhost:20128/dashboard 手动添加
```

### Claude Code 配置

```json
// ~/.claude/settings.json
{
  "api": {
    "baseUrl": "http://localhost:20128/v1",
    "apiKey": "omniroute"
  }
}
```

---

## 十一、相关笔记

- [[04-模型路由策略]] — 高/中/低三档路由决策框架
- [[01-9router-快速入门手册]] — 免费 AI 路由网关（OmniRoute 的前身/轻量替代）
- [[02-CC-Switch-模型管理器]] — Claude Code 多模型切换
- [[MCP深度解析与本地模型企业级应用指南]] — MCP 协议完整指南
- [[Agent学习与VibeCoding完全指南_2026年7月版|完全指南]] — 第7章 OmniRoute 完整配置
- [[00-主流模型对比]] — 各模型能力与定价速查

---

> **维护提醒：** OmniRoute 更新极快（~5500 commits），建议每月检查新版本。关注 CHANGELOG 和 Discord 获取最新动态。
