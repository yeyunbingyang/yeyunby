---
title: 通用 Skills 最佳实践
domain: Core_Ability
tags: [AI, Agent, Skills, 最佳实践, 工作流]
status: 稳定
created: 2026-05-12
updated: 2026-06-30
related:
  - "01-快速说明"
  - "02-我的skills蒸馏"
  - "01-Agent数据获取-可用Skills与开源项目"
  - "01-Codex-使用指南"
  - "02-opencli-browser"
summary: "Skills 的核心价值在于「渐进式披露」——元数据常驻、指令按需加载、资源按需调用，大幅降低 Token 消耗；日常使用按场景选 skill、组合多 skill 形成工作流、定期蒸馏固化为自己的 skill"
---

## 一、核心心法

### Skills 的本质：渐进式披露

不要把所有指令一次性塞进上下文。Skills 的三层结构决定了它的效率：

```
元数据（name + description）→ 常驻上下文，Token 消耗极低
指令层（SKILL.md 正文）     → AI 判断匹配后才加载
资源层（scripts/references） → 执行时才调用，不进入上下文
```

**判断一个 skill 写得好不好的唯一标准**：AI 能否在正确的时机自动触发它。这取决于 `description` 字段是否精准描述了调用时机。

### 三条铁律

1. **能用 skill 就不用自然语言反复描述** — 重复 3 次以上的工作流，固化为 skill
2. **skill 之间可以组合，不要试图用一个 skill 覆盖所有场景** — skill 应是小而专的，不是大而全的
3. **定期蒸馏** — 每 2 周回顾高频使用的 skill，看是否能合并、简化、或发现新的自动化机会

---

## 二、当前 Skills 全景 & 调用方式

### 2.1 Claude Code Skills（当前会话可用，共 30+ 个）

按使用频率分为四类：

#### 🔥 日常高频

| Skill                 | 触发场景             | 典型用法                              |
| --------------------- | ---------------- | --------------------------------- |
| **obsidian-vault**    | 搜索、创建、整理笔记       | "帮我找到所有讲 Docker 的笔记"              |
| **obsidian-markdown** | 编辑 Obsidian 格式内容 | 自动处理 wikilink、callout、frontmatter |
| **think**             | 出方案、做设计决策        | "帮我分析一下这个架构是否合理"                  |
| **write**             | 润色、改写、去 AI 味     | "帮我把这段改得更自然"                      |
| **learn**             | 深入研究一个主题         | "深入研究一下 Kubernetes 网络模型"          |
| **read**              | 读取网页/PDF         | "看看这篇文章讲了什么"                      |

#### 🔍 调研与搜索

| Skill             | 触发场景                   | 典型用法                |
| ----------------- | ---------------------- | ------------------- |
| **agent-reach**   | 全网调研、社交媒体搜索            | "调研一下小红书上的 xxx"     |
| **deep-research** | 需要多源交叉验证的深度报告          | "出一个关于 xxx 的深度调研报告" |
| **defuddle**      | 提取网页正文（比 WebFetch 更干净） | 自动用于网页内容提取          |
| **web-scraping**  | Python 爬虫抓取            | 需要批量抓取结构化数据时        |

#### 🛠 开发与审查

| Skill | 触发场景 | 典型用法 |
|-------|---------|---------|
| **code-review** | 审查代码改动 | "帮我 review 一下这次的改动" |
| **verify** | 验证改动是否生效 | "帮我验证一下这个修复是否有效" |
| **check** | 项目体检、发布前检查 | "检查一下项目状态" |
| **hunt** | 排查报错/Bug | "这个报错是怎么回事" |
| **simplify** | 代码简化重构 | "帮我把这段代码简化一下" |

#### 🎨 设计与创作

| Skill              | 触发场景                 | 典型用法           |
| ------------------ | -------------------- | -------------- |
| **design**         | UI 设计、页面美化           | "这个页面不好看，帮我优化" |
| **json-canvas**    | 编辑 Obsidian Canvas   | 创建思维导图、流程图     |
| **obsidian-bases** | 编辑 Obsidian Bases 视图 | 创建数据库视图        |

#### ⚙️ 基础设施

| Skill | 触发场景 | 典型用法 |
|-------|---------|---------|
| **skill-creator** | 创建/优化 skill | "帮我创建一个自动备份的 skill" |
| **cli-creator** | 从 API 文档生成 CLI 工具 | "把这个 API 包装成命令行工具" |
| **update-config** | 修改 Claude Code 配置 | "允许 npm 命令" |
| **find-skills** | 发现可安装的新 skill | "有没有能处理 Excel 的 skill" |
| **health** | Claude Code 配置健康检查 | "检查我的 Claude 配置" |

> **如何查看完整列表**：在对话中输入 `/` 可以看到所有可用 skill。或者直接描述需求，AI 会自动匹配最合适的 skill。

### 2.2 Codex Skills（你已安装的 9 个）

| Skill | 用途 | 调用方式 |
|-------|------|---------|
| **imagegen** | AI 图片生成 | 自然语言描述即可 |
| **openai-docs** | OpenAI 官方文档查询 | 提问涉及 OpenAI API 时自动触发 |
| **plugin-creator** | 创建 Codex 插件 | "帮我创建一个插件" |
| **skill-creator** | 创建 Codex skill | "帮我创建一个 skill" |
| **skill-installer** | 从社区安装 skill | "帮我安装 xxx skill" |
| **cli-creator** | 从 API 文档生成 CLI | 同 Claude Code 版 |
| **figma** | Figma 设计稿 → 代码 | "把这个 Figma 设计转成代码" |
| **pdf** | PDF 读写 | "帮我读一下这个 PDF" |
| **playwright** | 浏览器自动化 | "帮我打开网页做 xxx" |

### 2.3 Codex Plugins（你已安装的 5 个）

| Plugin | 能力 | 典型场景 |
|--------|------|---------|
| **documents** | Word / Google Docs | 自动生成文档 |
| **spreadsheets** | Excel / Google Sheets | 自动生成表格 |
| **presentations** | PowerPoint / Google Slides | 自动生成 PPT |
| **browser-use** | 浏览器操控 | 复杂网页交互 |
| **chrome** | Chrome 原生集成 | 复用已有登录态 |

### 2.4 Obsidian 插件（与 Skills 协同）

| 插件 | 作用 | 与 Skills 的协同 |
|------|------|------------------|
| **dataview** | 动态查询笔记 | obsidian-vault skill 会操作 dataview 查询 |
| **templater-obsidian** | 模板系统 | obsidian-markdown skill 不破坏模板语法 |
| **obsidian-git** | Git 版本控制 | check/code-review skill 的 Git 操作互补 |
| **surfing** | 内嵌浏览器 | agent-browser/agent-reach 调研结果的落地 |
| **calendar** | 日历视图 | 与 daily notes 工作流联动 |
| **obsidian-tasks** | 任务管理 | 任务跟踪与 Agent 执行记录 |
| **excalidraw** | 手绘图表 | design/json-canvas skill 的视觉补充 |

---

## 三、实战案例

### 案例 1：知识库维护工作流（最常用）

**场景**：你想整理某个技术领域的笔记，但不想手动操作。

**使用的 skills**：`obsidian-vault` → `obsidian-markdown` → `write`

```
你说："帮我整理一下 03-Knowledge 下所有讲 Docker 的笔记，
       检查 frontmatter 是否完整，缺失的补上"

AI 内部执行：
1. obsidian-vault  → Grep 搜索 Docker 相关笔记
2. obsidian-markdown → 逐篇读取，检查 frontmatter 字段
3. write（可选）  → 润色 summary 字段的描述
4. 输出整理报告
```

### 案例 2：深度调研 + 沉淀为笔记

**场景**：调研一个新技术，产出笔记。

**使用的 skills**：`deep-research` → `agent-reach` → `obsidian-vault` → `write`

```
你说："调研一下 2026 年 Serverless 的最新趋势，出个报告"

AI 内部执行：
1. deep-research → 多搜索引擎交叉验证，抓取高权威来源
2. agent-reach   → 补充社交媒体（Twitter/B站/小红书）的观点
3. obsidian-vault → 按你的知识库模板创建笔记
4. write         → 润色行文，去 AI 味
```

### 案例 3：浏览器数据抓取 + 结构化存储

**场景**：从网页抓取数据，存入知识库。

**使用的 skills**：`agent-browser` / `playwright` → `web-scraping` → `obsidian-vault`

```
你说："把 https://example.com 上的产品列表抓下来，
       按我的模板存到 04-Resources 下"

AI 内部执行：
1. agent-browser → 打开页面、等待渲染、提取数据
   或 playwright  → snapshot + 正则提取
2. web-scraping  → Python 脚本做数据清洗、结构化
3. obsidian-vault → 创建笔记，填入提取的数据
```

**选 skill 的心法**（来自你已有的调研笔记）：
- 轻量、一步提取 → `agent-browser snapshot` 或 `opencli eval`
- 复杂多步导航 → `agent-browser` 多步交互
- 需要 JS 执行提取 → `opencli`（Chrome Extension 驱动）
- 批量大规模 → `web-scraping`（Python 生态）

### 案例 4：代码审查 + 自动修复

**使用的 skills**：`code-review` → `simplify` → `verify`

```
你说："review 一下今天的改动，有问题直接修"

AI 内部执行：
1. code-review → 检查 diff，输出 Bug + 优化建议
2. simplify    → 自动应用简化重构
3. verify      → 运行验证，确认修复有效
```

### 案例 5：每周复盘自动化

**使用的 skills**：`obsidian-vault` → `learn` → `write`

```
你说："帮我做这周的复盘"

AI 内部执行：
1. obsidian-vault → 收集本周 daily notes
2. learn          → 综合分析本周内容，提炼关键主题
3. write          → 生成周报复盘模板（KPT 格式）
```

### 案例 6：跨 Agent 协作（Claude Code + Codex）

**场景**：利用两个 Agent 各自的优势。

```
Claude Code 端（知识库管理更强）：
  "帮我整理知识库中所有运维笔记，补全 frontmatter"

Codex 端（办公套件更强）：
  "把这份笔记导出为 Word 文档，格式要好看"
  → documents plugin 自动生成
```

---

## 四、组合使用模式（Patterns）

### 模式 1：调研 → 整理 → 发布

```
deep-research / agent-reach    ← 信息获取
        ↓
learn（六阶段研究）             ← 深度加工
        ↓
write                          ← 润色去 AI 味
        ↓
obsidian-vault                 ← 存入知识库
```

### 模式 2：开发 → 审查 → 验证

```
code-review                    ← 检查改动
        ↓
simplify                       ← 自动优化
        ↓
verify                         ← 验证效果
        ↓
check（项目体检）               ← 最终把关
```

### 模式 3：数据抓取 → 清洗 → 入库

```
agent-browser / playwright     ← 浏览器抓取
        ↓
web-scraping                   ← Python 清洗
        ↓
obsidian-vault                 ← 创建笔记
```

### 模式 4：设计 → 代码 → 审查

```
design                         ← UI 设计
        ↓
（手动或 AI 写代码）
        ↓
code-review → simplify         ← 审查优化
```

---

## 五、Skill 管理最佳实践

### 5.1 何时创建自己的 Skill

满足以下任一条件就应该创建：

1. **同一工作流执行了 3 次以上** — 如"每周复盘"、"每日笔记整理"
2. **有固定的输入输出格式** — 如特定模板的笔记生成
3. **需要参考外部文档/范文** — 利用 `references/` 目录存范文
4. **需要调用脚本** — 利用 `scripts/` 目录放 Python/Bash 脚本

### 5.2 Skill 目录结构建议

```
.claude/skills/我的技能/
├── SKILL.md          # 元数据（name + description）+ 指令
├── scripts/          # 可执行脚本（不进入 AI 上下文）
│   └── backup.py
├── references/       # 长文档、范文（按需加载）
│   └── 风格范例.md
└── assets/           # 模板、图片等资源
    └── 模板.md
```

### 5.3 description 的写法（最重要）

`description` 决定了 AI 能否在正确的时机触发这个 skill：

```yaml
# ❌ 不好的 description
description: 处理文件

# ✅ 好的 description
description: 当用户需要批量重命名 Markdown 笔记、统一文件名格式时使用此 skill
```

**写法公式**：`当用户[做什么操作/提出什么需求]时，[在什么场景下]，使用此 skill`

### 5.4 定期蒸馏（每 2 周）

在 [[02-我的skills蒸馏]] 中记录：

1. 这周用了哪些 skill？哪些没用过？
2. 有没有重复描述相同需求 3 次以上？→ 考虑固化为 skill
3. 有没有 skill 的 description 不够精准导致没触发？→ 优化 description
4. 有没有可以合并的 skill？→ 减少冗余

### 5.5 跨平台共享

Claude Code 和 Codex 的 Skills 格式兼容：

```bash
# 从 Claude Code 共享到 Codex
cp -r ~/.claude/skills/我的技能 ~/.codex/skills/

# 或反过来
cp -r ~/.codex/skills/我的技能 ~/.claude/skills/
```

两者的 `SKILL.md` 格式一致，`scripts/` 和 `references/` 目录结构也相同。

---

## 六、Skill vs MCP vs Plugin — 何时用什么

| 需求 | 用什么 | 原因 |
|------|--------|------|
| 定义工作流程、提示词模板 | **Skill** | Markdown 即可，最简单 |
| 调用外部 API / 数据库 | **MCP** | 标准化工具协议 |
| 打包 Skills + MCP + 应用 | **Plugin**（Codex） | 完整功能套件 |
| 一次性的自然语言指令 | 直接对话 | 不需要固化 |

**判断流程图**：

```
这个操作会重复吗？
  ├─ 否 → 直接自然语言对话
  └─ 是 → 需要调用外部工具吗？
           ├─ 否 → 创建 Skill
           └─ 是 → 已有 MCP 能用吗？
                    ├─ 是 → Skill 里引用 MCP
                    ├─ 否 → 能写一个 MCP 吗？
                    │        ├─ 是 → Skill + MCP
                    │        └─ 否 → 能否做成 Plugin（Codex）？
                    │                 └─ 是 → Skill + MCP + App = Plugin
                    └─ （Claude Code 生态暂不支持 Plugin）
```

---

## 七、当前已固化的本地 Skills

> 参见 [[02-我的skills蒸馏]] 持续更新

### 知识库相关
- `obsidian-vault` / `obsidian-markdown` — 内置，覆盖笔记 CRUD
- `obsidian-bases` / `json-canvas` — 高级视图

### 调研相关
- `deep-research` — 多源深度报告
- `agent-reach` — 社交媒体调研
- `learn` — 六阶段研究 → 文章

### 浏览器相关
- `agent-browser` — Snapshot + refs 系统，Token 最优
- `playwright` — 独立 Chromium，通用性强
- `web-scraping` — Python 生态，大规模抓取

### 开发相关
- `code-review` / `simplify` / `verify` / `check` / `hunt` — 完整开发闭环

### 内容创作
- `write` — 润色改写
- `design` — UI 设计
- `think` — 方案设计

---

## 关联

- [[01-快速说明]] — Agent Skills 概念入门
- [[02-我的skills蒸馏]] — 个人 skills 的持续记录与优化
- [[01-Agent数据获取-可用Skills与开源项目]] — 数据获取 skill 全景
- [[01-Codex-使用指南]] — Codex 端的 skills 与 plugins
- [[02-opencli-browser]] — opencli 浏览器自动化标准流程