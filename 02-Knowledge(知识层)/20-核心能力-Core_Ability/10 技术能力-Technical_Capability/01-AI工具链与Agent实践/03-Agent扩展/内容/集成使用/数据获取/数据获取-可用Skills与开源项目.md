---
title: Agent数据获取-可用Skills与开源项目
domain: Core_Ability
tags: [AI, Agent, 数据获取, Skills, 爬虫]
status: 稳定
created: 2026-06-19
updated: 2026-07-22
summary: "Agent 数据获取全景——可用 Skills / 开源项目清单，覆盖浏览器自动化、API 抓取、反爬对抗"
source: "内部实践整理；外部依据见正文链接"
related: []
verified: 2026-07-25
review_after: 2026-10-25
---

# Agent 数据获取 — 可用 Skills / 开源项目全景

> 调研时间：2026-06-19
> 基于已有机遇笔记的补充

---

## 0. 已有 + 新工具的心智模型

```
任务描述（自然语言）
   │
   ├─ 轻量直接抓取 ──→ opencli eval / agent-browser snapshot / cf-browser
   ├─ 复杂多步导航 ──→ browser-use / browser-harness / HyperCrawl  
   ├─ 批量大规模爬取 ──→ Crawl4AI / Firecrawl / Lupin CLI
   └─ Claude Code 内嵌 ──→ agent-browser / browser-harness / browser-pilot / cf-browser
```

---

## 1. Claude Code 可直接安装的 Skills

### 1.1 agent-browser（⭐ 推荐）

https://agent-browser.dev/

| 维度 | 说明 |
|------|------|
| 来源 | Vercel Labs 开源 |
| 语言 | Rust CLI + Node.js daemon + Playwright Core |
| 安装 | `npm install -g agent-browser` |
| 调用 | Bash 命令，非 MCP/HTTP |
| GitHub | 11.8k stars，650k+ npm 周下载量 |

**核心创新 — Snapshot + Refs 系统**：
- 生成 accessibility tree snapshot，元素带确定性 ref（`@e1`, `@e2`）
- AI 通过 stable ref 操作，而非脆弱 CSS/XPath
- **token 消耗比 Playwright MCP 低 93%**

**80+ 命令（8 类）**：
- 导航: `open`, `back`, `forward`, `reload`
- 交互: `click`, `fill`, `type`, `press`, `hover`, `scroll`, `select`, `check`, `drag`, `upload`
- 提取: `get text`, `get html`, `get value`, `get attr`, `get title`, `get url`, `get count`
- 状态: `is visible`, `is enabled`, `is checked`
- 快照: `snapshot -i`, `screenshot --full`, `pdf`
- 网络: `network requests`, `network route`, `network har start/stop`
- 会话: `session create/list/close`, `--session` 参数
- 等待: `wait --load networkidle`, `wait --text`, `wait --url`

**亮点**：
- 冷启动 ~500ms，热命令 ~10ms
- 语义定位器: `find role`, `find label`, `find placeholder`, `find testid`
- Auth Vault 持久 cookie/storage
- 多 tab 管理
- CDP 连接已有 Chrome

```bash
# 和 opencli 对比
# opencli: 通过 Chrome Extension 复用用户浏览器，state/eval/extract 
# agent-browser: 通过 CDP 直连 Chromium，snapshot/click/fill/get text
# 两者互补：opencli 适合 JS eval 提取、agent-browser 适合多步导航交互
```

## 为什么互补？

```plain
┌─────────────────────────────────────────┐
│  任务：从已登录的小红书抓取笔记数据        │
├─────────────────────────────────────────┤
│  Step 1: 导航到目标页面                  │
│     → Agent Browser（多步点击、搜索）      │
├─────────────────────────────────────────┤
│  Step 2: 提取结构化数据                  │
│     → OpenCLI（eval 执行 JS 提取 window   │
│        初始状态，或拦截网络 API 响应）     │
├─────────────────────────────────────────┤
│  Step 3: 批量下载图片/视频               │
│     → OpenCLI（内置 download 命令）       │
└─────────────────────────────────────────┘
```

### 1.2 browser-harness（Python，CDP 直连）

| 维度 | 说明 |
|------|------|
| 来源 | browser-use 团队 |
| 语言 | Python（~1200 行核心，含 helpers） |
| 安装 | `pip install browser-harness` |
| GitHub | 7.2k stars，MIT License |

**核心理念**：最薄的 LLM↔浏览器桥接层，CDP WebSocket 直连

**突出特性**：
- **Self-Healing**：Agent 运行时发现缺能力，直接编辑 `helpers.py` 注入
- **Domain Skills**：50+ markdown 站点知识库（GitHub、Amazon、LinkedIn、YouTube 等）
- **Interaction Skills**：16+ 指南（iframes、shadow DOM、dialogs、uploads、cross-origin）
- **Profile Sync**：本地 Chrome cookies → 远程 Browser Use Cloud
- **Multi-Agent**：`BU_NAME` 命名空间隔离多个并行 agent

**与 Claude Code 集成**：
```bash
# 一键让 Claude 自己配好
"Set up https://github.com/browser-use/browser-harness for me."
# 全局注册：在 CLAUDE.md 加 @~/path/to/SKILL.md
claude "go to github.com/trending and screenshot top 5 repos" --browser
```

### 1.3 browser-pilot
| 维度 | 说明 |
|------|------|
| 安装 | `npx @yqi96/browser-pilot` |
| 调用 | `/browser` 命令 |
| 特性 | 自动检测 Claude Code/Codex/Gemini CLI，CDP 直连 |

**功能**：深度网页调研、表单自动化、CAPTCHA 人机协作、截图+视觉分析

### 1.4 cf-browser（Cloudflare Browser Rendering，免费层）
| 维度 | 说明 |
|------|------|
| 安装 | `pip install cf-browser cf-browser-mcp` |
| GitHub | claude-world/cf-browser |
| 工具 | 15 MCP tools + 6 skills |

**能力**：markdown/screenshot/PDF/scrape/JSON AI 提取/links/a11y/crawl
**交互类（Worker 模式）**：click/type/evaluate/form submit/action chains
**费用**：读取类工具零成本免费

### 1.5 Firecrawl Plugin for Claude Code
| 维度 | 说明 |
|------|------|
| 安装 | Claude Code 内置 `/plugin marketplace` 搜索安装 |
| 前提 | `npm install -g firecrawl-cli` + 免费 API Key |
| 功能 | search / scrape / map / crawl / cloud browser |
| 输出 | 自动存 `.firecrawl/` 目录，不污染上下文 |

---

## 2. Python 生态核心开源项目

### 2.1 browser-use（⭐ 94k）
- **定位**：LLM 驱动的自主浏览器 Agent 框架
- **原理**：Playwright + 结构化 DOM 观察 / 截图视觉 → LLM 规划执行
- **适用**：复杂多步任务（"找到最便宜航班并预订"）
- **最佳驱动模型**：Claude Opus 4.6（62% 准确率）、Claude Sonnet 4.6（59%）
- **成本**：~$0.30-$1.00/任务（2026 年价格）

### 2.2 Crawl4AI（⭐ 62k）
- **定位**："Scrapy for LLMs"，自托管 Python 异步爬虫
- **许可证**：Apache 2.0（商业友好）
- **核心优势**：
  - 全自托管，数据不出域
  - 自适应选择器学习（DOM 变化时自动恢复）
  - 支持本地 LLM（Ollama/Llama），零 API 成本
  - 大规模成本 ~$0.0003/页（自建 infra）
- **劣势**：自己管 Docker/K8s/代理/监控，Python only

### 2.3 Firecrawl（⭐ 70k）
- **定位**："Scraping as an API"，托管服务
- **许可证**：AGPL-3.0（自托管）/ 商业（SaaS）
- **核心优势**：
  - 一条 API 调用拿到干净 Markdown
  - 自然语言提取（"提取标题和价格"）
  - 多语言 SDK（Python/Node/Go/Rust）
  - 内置代理轮换、反爬、CAPTCHA
- **劣势**：按页计费，大规模成本高，强防护站成功率 ~34%

### 2.4 Lupin CLI
- **定位**：自适应升级链（HTTP → Camoufox → Patchright）
- **亮点**：记录每个域名的成功引擎，下次自动选对
- **基准**：25 个最难站点 25/25 全过（Apr 2026）
- **内置 MCP server、社交爬虫、LLM 提取**

### 2.5 Scrapurrr
- **定位**：Schema 驱动（Pydantic 模型定义输出结构）
- **特性**：HTTP 优先/浏览器 fallback、智能获取、100+ LLM 提供商（LiteLLM）

### 2.6 BrowseGenie
- **定位**：一句话生成 BeautifulSoup4 提取器
- **特性**：提取器按页面布局缓存复用，~$0.007/次
- **Web UI + CLI + Python SDK**

---

## 3. MCP 服务器一览

### 已作为 Claude Code Skill 可用的
| 名称 | 安装 | 特点 |
|------|------|------|
| **agent-browser-mcp** | `npx -y agent-browser-mcp` | agent-browser 的 MCP 包装 |
| **HyperCrawl MCP** | `npx -y hypercrawl-mcp` | 自主 browse-and-act loop |
| **FourA MCP** | `npx -y @fouradata/mcp` | WAF/CF 反爬绕过+代理轮换 |
| **Stealth Scraper MCP** | `npx @stealth-scraper/mcp` | 反爬+结构化提取模板 |
| **WebLens MCP** | `npx -y weblens-mcp` | Playwright + Readability 提取 |
| **Vibe MCP** | GitHub vibetechnologies/vibe-mcp | 复用已有 Chrome Profile |
| **Spider MCP** | `cargo install spider_mcp` | Rust 爬虫+CDP 渲染 |
| **DrissionPage MCP** | `pip install drissionpage-mcp` | 14 tools，操控 Chrome |
| **webcrawl-mcp** | `pip install webcrawl-mcp` | trafilatura 本地提取+Firecrawl fallback |

### 托管型 MCP（Remote URL）
| 名称 | 特点 |
|------|------|
| **Firecrawl MCP** (Apify) | 13 tools，search/scrape/crawl/browser/agent |
| **Anakin MCP** | search/scrape/map/crawl/agentic_search |
| **Exa MCP** | 神经搜索+页面抓取，免费层无需 API Key |
| **Browserbase MCP** | CAPTCHA 解题+住宅代理+远程浏览器 |

---

## 4. 与已有技术栈的关系

### 已有工具
```
opencli ───────── Chrome Extension 驱动 ── 擅长 JS eval 一步提取
playwright-cli ── 独立 Chromium ───────── 擅长 snapshot+正则
```

### 新工具的互补定位
```
agent-browser ─── CDP 直连 ──────────── 擅长多步导航+快照
browser-harness ── CDP 直连 ─────────── 擅长 Domain Skills + Self-Healing
browser-use ────── Playwright ─────────── 擅长自主复杂任务
Crawl4AI ───────── 自托管异步 ─────────── 擅长合规大规模爬取
Lupin CLI ──────── 自适应升级链 ──────── 擅长高难度反爬站
cf-browser ─────── CF 边缘浏览器 ─────── 免费 + JS 渲染
```

---

## 5. 场景选择速查（含新工具）

| 场景 | 推荐工具 | 理由 |
|------|---------|------|
| 有规律 CSS 列表页，一步提取 | **opencli eval** | JS 一步返回 JSON |
| 有规律 CSS 列表页，轻量 CLI | **agent-browser snapshot** | refs 稳定，token 省 |
| 复杂多步导航+表单+登录 | **browser-use** / **browser-harness** | 自主规划+执行 |
| 大规模合规爬取（自建） | **Crawl4AI** | Apache 2.0，~$0.0003/页 |
| 快速 API 级抓取 | **Firecrawl API** | 一条 API → Markdown |
| 高难度反爬站（CF/DataDome） | **Lupin CLI** / **FourA MCP** | 自适应升级 / 专用反爬 |
| Claude Code 内一键使用 | **agent-browser** / **browser-harness** / **cf-browser** | 安装简单，原生集成 |
| 纯文本内容提取 | **opencli extract** / **cf-browser** | 直接输出 Markdown |
| Schema 结构化提取 | **Scrapurrr** (Pydantic) / **Firecrawl /extract** | 定义即所得 |
| 需要登录态复用 | **opencli** (Chrome Extension) / **Vibe MCP** (已有 Profile) | 共享日常浏览器 Cookie |
| CI/CD 环境 | **agent-browser** (headless) / **Crawl4AI** (Docker) | 无 GUI 依赖 |

---

## 6. 核心心法升级

1. **先用 HTTP，不行再上浏览器** — Lupin CLI 的思路，省 90% 成本
2. **能用 JS eval 不用 snapshot，能用 snapshot 不用视觉** — token 消耗梯度
3. **稳定选择器 > CSS > XPath** — agent-browser 的确定性 ref 是解法
4. **复用浏览器登录态 > 重新登录** — opencli/Vibe MCP/Profile Sync
5. **Self-healing > 手动修选择器** — browser-harness / Crawl4AI 的适应性
6. **先本地 LLM 后云端** — Crawl4AI + Ollama 零外部 API 成本
7. **CC 内嵌工具优先于外部框架** — agent-browser/browser-harness 一条 Bash 命令 vs Python 项目
