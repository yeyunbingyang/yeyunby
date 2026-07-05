---
title: 9router 快速入门手册
domain: Core_Ability
tags: [AI, 路由器, 代理, 成本优化]
status: 稳定
created: 2026-06-16
updated: 2026-06-16
source: "https://github.com/decolua/9router"
related: ["模型路由策略", "CC Switch 模型管理器", "主流模型对比"]
summary: "9router 是免费 AI 路由器——RTK 技术节省 20-40% Token，自动 fallback 到免费/廉价模型，连接所有 AI 代码工具到 40+ 厂商 100+ 模型"
---

# 9router 快速入门手册

> Never stop coding. 连接所有 AI 代码工具到 40+ 厂商 100+ 模型，RTK 节省 20-40% Token。

## 一句话结论

9router 是一个**免费 AI 路由器/代理**，部署在你和 AI API 之间：它用 RTK（Response Token Kernel）技术压缩响应 Token，并在主模型不可用时自动 fallback 到免费/廉价模型。

## 与 CC Switch 的区别

| | CC Switch | 9router |
|------|-----------|---------|
| **核心功能** | 模型替换（A→B 映射） | 智能路由 + Token 压缩 |
| **Token 节省** | 无 | RTK 节省 20-40% |
| **自动 Fallback** | 无 | 多级自动降级 |
| **接入方式** | 环境变量劫持 | 本地代理服务 |
| **免费模型** | 需自行配置 | 内置免费 fallback |
| **适用场景** | Claude Code 专属 | 所有 AI 代码工具 |

## 核心能力

### 1. RTK — Response Token Kernel

```
AI 响应（1000 token）
      │
      ▼
  RTK 压缩引擎
      ├─ 移除冗余表达
      ├─ 压缩重复结构
      └─ 保留语义完整
      │
      ▼
  压缩后响应（600-800 token）
  节省 20-40% Token，语义不变
```

### 2. 自动 Fallback 链路

```
请求 → 主模型（如 DeepSeek V3）
          │
          ├─ 成功 → 返回
          └─ 失败/超时/限流
               └─ Fallback 1（如 Qwen-Plus）
                    ├─ 成功 → 返回
                    └─ 失败
                         └─ Fallback 2（如免费模型）
                              └─ 返回
```

### 3. 全工具兼容

9router 作为本地代理运行，任何支持自定义 API Base URL 的 AI 工具都能接入：

- **Claude Code**（通过 CC Switch 间接接入）
- **Cursor / Windsurf / Trae** — 直接在设置里改 API Base URL
- **Codex / OpenClaw / Cline / OpenCode** — 配置 baseUrl 指向 9router
- **Copilot / Gemini CLI** — 通过代理层接入

## 快速安装

### 方式一：npm 全局安装

```bash
npm install -g 9router
9router init
```

### 方式二：Docker

```bash
docker run -d -p 9000:9000 \
  -v ~/.9router:/app/config \
  decolua/9router:latest
```

### 方式三：npx 直接运行

```bash
npx 9router start
```

## 基础配置

创建 `~/.9router/config.yaml`：

```yaml
# 主模型配置
default_model: deepseek-chat

# API 密钥
api_keys:
  openai: sk-xxx
  deepseek: sk-xxx
  qwen: sk-xxx

# Fallback 策略
fallback:
  enabled: true
  candidates:
    - deepseek-chat          # 首选 fallback
    - qwen-plus              # 次选
    - gemini-2.5-flash       # 免费兜底
  max_retries: 2

# RTK Token 压缩
rtk:
  enabled: true
  compression_level: medium   # low / medium / high
  preserve_code_blocks: true  # 代码块不压缩

# 端口与日志
server:
  port: 9000
  log_level: info
```

## 在 Claude Code 中接入 9router

```bash
# 第一步：启动 9router
9router start

# 第二步：配置 CC Switch 指向 9router
# 编辑 ~/.claude-switch/config.json
{
  "profiles": {
    "default": {
      "medium": {
        "provider": "custom",
        "model": "deepseek-chat",      # 9router 会路由
        "baseURL": "http://localhost:9000/v1",
        "apiKey": "9router"
      }
    }
  }
}

# 第三步：启动 CC
claude-switch start
claude
```

现在 CC 的所有 API 请求都经过 9router，享受自动 fallback 和 RTK 压缩。

## 在其他工具中接入

### Cursor / Windsurf

在设置中修改 API Base URL：
```
https://api.openai.com/v1  →  http://localhost:9000/v1
```

### Codex / OpenClaw

```bash
# 设置环境变量
$env:OPENAI_BASE_URL="http://localhost:9000/v1"
```

### 所有支持自定义端点工具

将 API Base URL 指向 `http://localhost:9000/v1`，API Key 填 `9router` 或你的实际密钥。

## 成本优化实例

| 场景 | 无路由 | 使用 9router | 节省 |
|------|--------|-------------|------|
| 月均 5M token（Claude Sonnet） | ~$75 | ~$45 | 40% |
| 月均 10M token（混合模型） | ~$100 | ~$55 | 45% |
| 月均 20M token（重度 Agent） | ~$200 | ~$110 | 45% |

> 节省来自两个方向：RTK 压缩省 Token（20-40%）+ 自动 fallback 把偶尔的高档请求降级到廉价模型。

## 常见问题

**Q: RTK 压缩会不会影响代码质量？**
不会。`preserve_code_blocks: true` 确保所有代码块原样保留，RTK 只压缩自然语言描述部分。

**Q: 9router 本身免费吗？**
完全开源免费，Apache 2.0 协议。Token 消耗节省即省钱，无额外费用。

**Q: 和直接调用 API 比有什么延迟？**
本地代理延迟 < 50ms，几乎无感。Fallback 重试会增加延迟（首次失败后才触发）。

---

## 关联

- [[04-模型路由策略]] — 三档路由决策框架
- [[02-CC-Switch-模型管理器]] — Claude Code 多模型切换
- [[03-主流模型对比]] — 各模型能力与定价速查
