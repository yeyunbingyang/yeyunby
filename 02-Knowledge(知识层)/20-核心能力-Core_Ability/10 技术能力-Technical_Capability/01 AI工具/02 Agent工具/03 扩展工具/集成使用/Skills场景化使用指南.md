---
title: Skills 场景化使用指南（完整版）
description: 涵盖 6 大仓库 100+ Skills 的具体使用——按场景分类（对齐/研究/开发/笔记/创作/运维），附安装命令、触发方式、组合流程全表
tags:
  - skills
  - usage
  - scenarios
  - workflow
  - reference
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
related:
  - "04-Skills生态全景"
  - "03-通用skills最佳实践"
  - "官方与社区Skill资源集成指南"
summary: "100+ Skills 场景化使用指南——按 8 大场景分类（需求对齐/研究调研/代码开发/笔记管理/内容创作/运维安全/元技能/特定领域），每 Skill 含来源、安装、触发方式、具体用法。想找 Skill 来源看资源集成指南，想深入理解看生态全景。"
---

# Skills 场景化使用指南（完整版）

> 本文档按**实际工作场景**介绍 100+ 常用 Skills 怎么用。
>
> - 找 Skill 来源 → [[官方与社区Skill资源集成指南]]
> - 想深入理解 → [[04-Skills生态全景]]
> - 个人经验记录 → [[02-我的skills蒸馏]]

---

## 一、需求对齐与方案设计

### 1.1 `think` — 方案设计与风险评估

| 项目 | 说明 |
|------|------|
| **来源** | tw93/Waza |
| **安装** | `npx skills add tw93/Waza@think -g` |
| **触发** | `/think` 或"帮我分析这个方案" |
| **场景** | 架构设计、技术选型、重构方案 |

**原理**：AI 先分析问题 → 列出方案 → 指出权衡 → 确认理解后再动手，避免直接开干。

```bash
/think 我想重构 UserCard 组件，它现在 300 行
→ AI：挑战方案 → 分析职责拆分(4 个职责违反单一职责) → 指出风险(状态管理) → 产出计划
```

### 1.2 `grill-me` — 需求追问对齐

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **安装** | `npx skills add mattpocock/skills@grill-me -g` |
| **触发** | `/grill-me` |
| **场景** | 模糊需求时让 AI 反过来"面试"你 |

**原理**：AI 持续追问直到决策树全部分支解决——目标、范围、验收标准、约束、优先级。

```bash
/grill-me 我想做一个 CLI 工具管理笔记
→ AI：目标用户？核心功能？输入输出？技术栈？时间线？MVP 还是完整版？
→ 多轮后产出清晰规格
```

**进阶**：`grill-with-docs`（`/grill-with-docs`）除了追问还会同步构建 `CONTEXT.md` 领域语言和 ADR。

### 1.3 `interview-me` — 结构化需求访谈

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | 自然语言"帮我确认一下需求" |
| **场景** | 需要 95% 置信度的需求规格 |

**原理**：一对一访谈，挖出用户真正想要什么，直到 95% 置信度。

### 1.4 `spec-driven-development`（`/spec`）— 先写 PRD 再写代码

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | `/spec` |
| **场景** | 正式功能开发前 |

**原理**：先写 PRD（目标/命令/结构/测试/边界）再写代码，避免做出来不是你要的。

### 1.5 `idea-refine` — 模糊想法→具体方案

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | 自然语言 |

**原理**：发散/收敛思维，把模糊想法变成具体方案。

### 1.6 `domain-modeling` — 领域模型构建

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：构建和精炼项目领域模型，用边界场景检验术语准确性。

### 1.7 `codebase-design` — 代码规范设计

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：设计深度模块的规范和词汇。

### 1.8 `planning-and-task-breakdown`（`/plan`）— 任务拆解

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | `/plan` |

**原理**：将 spec 分解为小而原子的独立任务。

### 1.9 `to-prd` / `to-issues` — 产出归档

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/to-prd`、`/to-issues` |

**原理**：将当前对话综合为 PRD 并发布到 Issue Tracker，或将计划拆分为独立 Issue。

### 1.10 `prototype` — 快速原型验证

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：构建可丢弃的原型（终端 app 或 UI 变体）验证设计思路。

### 其他相关

| Skill | 来源 | 触发 | 作用 |
|-------|------|------|------|
| `context-engineering` | agent-skills | 自动 | 优化 Agent 上下文利用效率 |
| `source-driven-development` | agent-skills | 自动 | 先读现有代码再写新代码 |
| `doubt-driven-development` | agent-skills | 自动 | 不确定时主动停下来确认 |
| `ask-matt` | mattpocock | `/ask-matt` | 询问哪个 skill 适合当前场景（路由） |
| Karpathy 四大原则 | karpathy-skills | 常驻 CLAUDE.md | 改变 Agent 行为基调 |

---

## 二、研究与调研

### 2.1 `learn` — 六阶段深度研究

| 项目 | 说明 |
|------|------|
| **来源** | tw93/Waza |
| **安装** | `npx skills add tw93/Waza@learn -g` |
| **触发** | `/learn` 或"深入研究一下 XXX" |
| **场景** | 需要完整的学习笔记或知识文档 |

**六阶段**：收集 → 消化 → 大纲 → 填充 → 润色 → 发布。产出完整的 Markdown 学习笔记。

### 2.2 `deep-research` — 多源调研报告

| 项目 | 说明 |
|------|------|
| **来源** | Anthropic 官方 Skills |
| **安装** | `/plugin marketplace add anthropics/skills` |
| **触发** | 自然语言"出深度调研报告" |

**原理**：多搜索引擎搜索 → 同时抓取多个来源 → 交叉验证 → 产出带引用的报告。

### 2.3 `research` — 高可信源调查

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：针对高信任源（官方文档/论文）调查问题，产出带引用的 Markdown 文档。

### 2.4 `agent-reach` / `read` — 信息获取

| Skill | 来源 | 触发 | 场景 |
|-------|------|------|------|
| `agent-reach` | 生态 Skill | 斜杠命令 | 社交媒体调研（小红书/推特/B站/Reddit） |
| `read` | Waza/内置 | `/read` 或 URL | 读取网页/PDF，摘要或 Markdown 输出 |

### 2.5 `defuddle` — 干净网页提取

| 项目 | 说明 |
|------|------|
| **来源** | kepano/obsidian-skills |
| **安装** | `npx skills add kepano/obsidian-skills@defuddle -g` |
| **用法** | `defuddle parse <url> --md` |

比 WebFetch 更干净的网页内容提取，去导航/广告。

### 2.6 `baoyu-youtube-transcript` — YouTube 字幕

| 项目 | 说明 |
|------|------|
| **来源** | baoyu-skills |
| **安装** | `npx skills add JimLiu/baoyu-skills@baoyu-youtube-transcript -g` |
| **触发** | `/baoyu-youtube-transcript` |

**功能**：YouTube 字幕下载，支持多语言翻译和章节提取。

---

## 三、代码开发与调试

### 3.1 `code-review` — 代码审查

| 版本 | 来源 | 触发 | 特点 |
|------|------|------|------|
| `/simplify` | Claude Code 内置 | `/simplify` | 审查+简化一体 |
| `code-review` | mattpocock/skills | 自动 | 双轴审查（标准合规 + Spec 实现） |
| `code-review-and-quality` | agent-skills | `/review` | 含质量门禁 |

**典型用法**：检查 diff → 输出 Bug + 优化建议 → 可选自动修复。

### 3.2 `hunt` — 系统化调试

| 项目 | 说明 |
|------|------|
| **来源** | tw93/Waza |
| **安装** | `npx skills add tw93/Waza@hunt -g` |
| **触发** | `/hunt` 或"这个报错是怎么回事" |

**原理**：先确认根因再修复，避免修错地方。

### 3.3 `diagnosing-bugs` — 严格诊断循环

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：再现 → 最小化 → 假设 → 验证 → 修复 → 回归测试。

### 3.4 `debugging-and-error-recovery` — 系统化调试

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | 自动 |

**原理**：系统化调试与错误恢复。

### 3.5 `incremental-implementation`（`/build`）— 增量构建

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | `/build` |

**原理**：一次一个切片，持续可交付。

### 3.6 `test-driven-development`（`/test`）— TDD 循环

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | `/test` |

**原理**：红→绿→重构循环。

### 3.7 `tdd` — TDD 循环（mattpocock 版）

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 模型可自动调用 |

**原理**：红→绿→重构，逐层推进。

### 3.8 `code-simplification`（`/code-simplify`）— 代码简化

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | `/code-simplify` |

**原理**：简化代码（含 Chesterton's Fence 原则——先理解再删除）。

### 3.9 `improve-codebase-architecture` — 架构改进

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/improve-codebase-architecture` |

**原理**：扫描代码库生成可视化 Hotspot 报告，选改进点深入。

### 3.10 `wayfinder` — 超大任务规划

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/wayfinder` |

**原理**：超大任务拆成 investigation ticket，逐一度攻破。

### 3.11 `implement` — Spec 驱动实现

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/implement` |

**原理**：按 Spec/Ticket 驱动 TDD 实现，完成后跑 `/code-review`。

### 3.12 `resolving-merge-conflicts` — 冲突解决

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 自动 |

**原理**：逐块按意图解决合并冲突，永不 `--abort`。

### 3.13 `triage` — Issue 分诊

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/triage` |

**原理**：Issue 状态机流转，自动分类和路由。

### 3.14 前端开发 Skills

| Skill | 来源 | 说明 |
|-------|------|------|
| `frontend-ui-engineering` | agent-skills | 前端 UI 工程最佳实践 |
| `api-and-interface-design` | agent-skills | API 设计规范（含 Hyrum 定律） |
| `browser-testing-with-devtools` | agent-skills | 浏览器 DevTools 验证 |
| `security-and-hardening` | agent-skills | 安全加固审查 |
| `performance-optimization` | agent-skills | 性能优化 |

### 3.15 `handoff` — 会话交接

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/handoff` |

**原理**：压缩对话历史为交接文档，另一代理无缝接力。

### 3.16 `teach` — 多会话教学

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/teach` |

**原理**：用当前目录作为工作空间，多 session 教授新技能。

---

## 四、笔记与知识库管理

### 4.1 Obsidian 技能全集

详情见 [[Obsidian-Agent操作指南]]。

| 操作 | Skill | 命令/用法 |
|------|-------|----------|
| 创建笔记 | obsidian-cli | `obsidian create name="标题" content="内容"` |
| 搜索笔记 | obsidian-cli | `obsidian search query="关键词"` |
| 读取笔记 | obsidian-cli | `obsidian read file="笔记名"` |
| 追加内容 | obsidian-cli | `obsidian append file="笔记名" content="新行"` |
| 操作日记 | obsidian-cli | `obsidian daily:read / daily:append` |
| 设置属性 | obsidian-cli | `obsidian property:set name="status" value="done"` |
| 查看任务 | obsidian-cli | `obsidian tasks daily todo` |
| 标签统计 | obsidian-cli | `obsidian tags sort=count counts` |
| 反向链接 | obsidian-cli | `obsidian backlinks file="笔记名"` |
| 插件开发 | obsidian-cli | `plugin:reload / dev:errors / dev:screenshot / dev:console` |
| DOM 检查 | obsidian-cli | `obsidian dev:dom selector=".workspace-leaf" text` |
| 执行 JS | obsidian-cli | `obsidian eval code="app.vault.getFiles().length"` |
| Bases 视图 | obsidian-bases | 编写 `.base` 文件定义表格/卡片/列表/公式 |
| Canvas 画布 | json-canvas | 编写 `.canvas` 文件创建思维导图/流程图 |
| 网页提取 | defuddle | `defuddle parse <url> --md -o content.md` |
| 格式检查 | obsidian-markdown | wikilink/callout/embeds/frontmatter 自动处理 |

### 4.2 知识库维护工作流

```bash
# 搜索待整理笔记
obsidian search query="Docker" limit=20

# 检查格式（自动）
obsidian-markdown 自动处理

# 补全 frontmatter
write → 补全 summary

# 更新 MOC
obsidian create name="主题-MOC" content="..."
```

---

## 五、内容创作与设计

### 5.1 Anthropic 官方创作技能

| Skill | 来源 | 说明 |
|-------|------|------|
| `algorithmic-art` | anthropics/skills | 算法/数学驱动的视觉艺术生成 |
| `canvas-design` | anthropics/skills | 创建 PNG/PDF 视觉艺术作品 |
| `frontend-design` | anthropics/skills | 前端 UI 设计最佳实践 |
| `brand-guidelines` | anthropics/skills | 应用 Anthropic 官方品牌色和字体 |
| `theme-factory` | anthropics/skills | 应用字体和颜色主题到构件 |
| `web-artifacts-builder` | anthropics/skills | React/Tailwind/shadcn HTML 构件 |

### 5.2 `write` — 润色改写

| 项目 | 说明 |
|------|------|
| **来源** | tw93/Waza / 内置 |
| **触发** | `/write` 或自然语言 |
| **场景** | 去 AI 味、润色、改写、中英文 |

### 5.3 `design` — UI 设计

| 项目 | 说明 |
|------|------|
| **来源** | 内置 |
| **触发** | "这个页面不好看" |
| **场景** | 页面布局、视觉优化 |

### 5.4 baoyu-skills — 中文内容创作（20+ 技能）

**内容创作类**（安装：`npx skills add JimLiu/baoyu-skills -g`）：

| Skill | 斜杠命令 | 功能 |
|-------|---------|------|
| `baoyu-xhs-images` | `/baoyu-xhs-images` | 小红书图片卡片（12 风格 × 6 布局 × 3 配色） |
| `baoyu-infographic` | `/baoyu-infographic` | 信息图（21 布局 × 21 风格） |
| `baoyu-diagram` | `/baoyu-diagram` | SVG 图表（流程图/时序图/架构图等） |
| `baoyu-cover-image` | `/baoyu-cover-image` | 文章封面图（5 维定制） |
| `baoyu-slide-deck` | `/baoyu-slide-deck` | 幻灯片（16 风格预设，输出 PPTX+PDF） |
| `baoyu-comic` | `/baoyu-comic` | 知识漫画（5 画风 × 7 基调） |
| `baoyu-article-illustrator` | `/baoyu-article-illustrator` | 文章插图（类型 × 风格 × 色板） |

**发布类**：

| Skill | 斜杠命令 | 功能 |
|-------|---------|------|
| `baoyu-post-to-x` | `/baoyu-post-to-x` | 发布到 X/Twitter |
| `baoyu-post-to-wechat` | `/baoyu-post-to-wechat` | 发布到微信公众号 |
| `baoyu-post-to-weibo` | `/baoyu-post-to-weibo` | 发布到微博 |

**工具类**：

| Skill | 斜杠命令 | 功能 |
|-------|---------|------|
| `baoyu-image-gen` | `/baoyu-image-gen` | 多后端图像生成（10 个服务商） |
| `baoyu-translate` | `/translate` | 三模式翻译（快速/标准/精翻） |
| `baoyu-format-markdown` | `/baoyu-format-markdown` | Markdown 格式化 |
| `baoyu-markdown-to-html` | `/baoyu-markdown-to-html` | Markdown → HTML（公众号兼容） |
| `baoyu-wechat-summary` | `/baoyu-wechat-summary` | 微信群聊精华提取 |
| `baoyu-compress-image` | `/baoyu-compress-image` | 图片压缩 |

### 5.5 社区设计 Skills

| Skill | 来源 | Stars | 说明 |
|-------|------|-------|------|
| `ui-ux-pro-max-skill` | nextlevelbuilder/ui-ux-pro-max-skill | 107k★ | 161 条推理规则 + 67 种 UI 风格 + 95 配色方案 |
| `taste-skill` | Leonxlnx/taste-skill | 64.5k★ | 可组合前端技能与图像转代码管道 |
| `impeccable` | pbakaus/impeccable | 47.5k★ | LLM 驱动的前端设计技能集 |

### 5.6 文档技能

| Skill | 来源 | 功能 |
|-------|------|------|
| `docx` | anthropics/skills | 创建/编辑/分析 .docx 文件 |
| `pptx` | anthropics/skills | 读写/生成/调整幻灯片 |
| `pdf` | anthropics/skills | 提取文本/表格/合并/标注 PDF |
| `xlsx` | anthropics/skills | 公式/图表/数据转换 |

### 5.7 `slack-gif-creator` — Slack GIF

| 项目 | 说明 |
|------|------|
| **来源** | anthropics/skills |
| **场景** | 创建适合 Slack 的动画 GIF |

---

## 六、运维与安全

### 6.1 CI/CD 与版本控制

| Skill | 来源 | 触发 | 说明 |
|-------|------|------|------|
| `git-workflow-and-versioning` | agent-skills | 自动 | 主干开发 + 版本管理 |
| `ci-cd-and-automation` | agent-skills | 自动 | CI/CD 自动化（Shift Left + Feature Flags） |
| `deprecation-and-migration` | agent-skills | 自动 | 废弃与迁移——代码即负债 |
| `shipping-and-launch` | agent-skills | `/ship` | 发布上线流程 |

### 6.2 健康检查

| Skill | 来源 | 触发 | 说明 |
|-------|------|------|------|
| `health` | Waza | `/health` | 检查 Codex/Claude Code/项目指令/Verifier |
| `check` | Waza | `/check` | 审查 diff、提取项目约束、处理发布/推送/验证 |

### 6.3 安全技能

| Skill | 来源 | 说明 |
|-------|------|------|
| `security-and-hardening` | agent-skills | 安全加固审查 |
| Anthropic-Cybersecurity-Skills | mukul975/Anthropic-Cybersecurity-Skills | 754 个生产级安全技能，映射五大安全框架 |

### 6.4 性能优化

| Skill | 来源 | 说明 |
|-------|------|------|
| `performance-optimization` | agent-skills | 性能优化 |

---

## 七、元技能与工具类

### 7.1 `skill-creator` — 创建自定义 Skill

| 项目 | 说明 |
|------|------|
| **来源** | anthropics/skills |
| **安装** | `npx skills add anthropics/skills@skill-creator -g` |
| **触发** | 自然语言"帮我创建一个 Skill" |

**自动化创建**：描述需求 → AI 生成标准 skill.md → 放入 `.claude/skills/` 即可使用。

```
.claude/skills/我的技能/
├── skill.md      ← 元数据 + 指令
├── scripts/      ← 可执行脚本（不进入 AI 上下文）
├── references/   ← 按需加载的参考文档
└── assets/       ← 模板、图片等资源
```

**何时创建**：同一工作流 3 次以上 / 固定输入输出格式 / 需要参考文档或脚本。

### 7.2 `writing-great-skills` — 优质 Skill 编写参考

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | 参考手册 |

**内容**：编写高质量 Skill 的词汇和原则。

### 7.3 `using-agent-skills` — 技能自动路由

| 项目 | 说明 |
|------|------|
| **来源** | addyosmani/agent-skills |
| **触发** | 自动 |

**原理**：自动匹配任务到对应技能。

### 7.4 `setup-matt-pocock-skills` — 初始配置

| 项目 | 说明 |
|------|------|
| **来源** | mattpocock/skills |
| **触发** | `/setup-matt-pocock-skills` |

**功能**：配置 Issue Tracker（GitHub/Linear/local）、标签和文档路径。

### 7.5 Anthropic 官方文档技能

| Skill | 功能 |
|-------|------|
| `claude-api` | Claude API 开发指南 |
| `doc-coauthoring` | 多人协作编辑文档 |
| `internal-comms` | 撰写公司内部通讯/简报/FAQ |
| `mcp-builder` | 创建 MCP 服务器连接外部 API |
| `webapp-testing` | 使用 Playwright 测试本地 Web 应用 |

### 7.6 OpenCLI 技能（6 个）

| Skill | 功能 |
|-------|------|
| `opencli-browser` | 驱动 Chrome 浏览器——导航、点击、填表、提取 |
| `opencli-adapter-author` | 为任意网站编写 CLI 适配器 |
| `opencli-autofix` | 修复损坏的适配器 |
| `opencli-browser-sitemap` | 使用站点地图导航浏览器 |
| `opencli-sitemap-author` | 创建/更新站点地图知识 |
| `opencli-usage` | OpenCLI 命令和站点快速参考 |

**安装**：`npx skills add jackwener/OpenCLI@opencli-browser -g`

### 7.7 agent-browser — 浏览器自动化 CLI

| 项目 | 说明 |
|------|------|
| **来源** | vercel-labs/agent-browser（37.9k★） |
| **安装** | `npm install -g agent-browser` |
| **触发** | 命令行直接调用 |

**命令**：

| 命令 | 功能 |
|------|------|
| `agent-browser open <url>` | 启动浏览器 + 导航 |
| `agent-browser snapshot` | 获取无障碍树快照 |
| `agent-browser click @e2` | 按 ref ID 点击 |
| `agent-browser fill @e3 "text"` | 按 ref ID 填表 |
| `agent-browser screenshot [path]` | 截图 |
| `agent-browser eval <js>` | 执行 JavaScript |
| `agent-browser chat "<指令>"` | 自然语言浏览器操控 |

### 7.8 `remotion-best-practices` — 视频编程

| 项目 | 说明 |
|------|------|
| **来源** | remotion-dev/skills |
| **安装** | `npx skills add remotion-dev/skills -g` |
| **核心** | 用 `interpolate()` 非 `spring()`、禁止 CSS transitions、资源放 `public/` |

---

## 八、多智能体协作与工作流编排

### 8.1 myclaude — 多智能体工作流（11 模块）

| 模块 | 斜杠命令 | 功能 |
|------|---------|------|
| `do`（5 阶段） | `/do` | Understand→Clarify→Design→Implement+Review→Complete |
| `omo`（多智能体编排） | `/omo` | 路由到 oracle/librarian/explore/develop 等专业 Agent |
| `sparv`（5 阶段） | `/sparv` | Specify→Plan→Act→Review→Vault |
| `bmad`（敏捷工作流） | `/bmad-pilot` | PO/Architect/Scrum Master/Dev/Reviewer/QA 六 Agent |
| `requirements`（需求流水线） | `/requirements-pilot` | 轻量级需求→代码 |
| `essentials`（核心命令） | `/code /debug /test /review` | 11 个核心开发命令 |
| `browser`（浏览器） | — | 浏览器自动化测试和数据提取 |
| `codeagent`（多后端） | — | Codex/Claude/Gemini/OpenCode 多后端调用 |
| `product-requirements`（PRD） | — | 交互式 PRD 生成（含质量评分） |
| `test-cases`（测试） | — | 从需求生成全面测试用例 |
| `skill-install`（安装） | — | 从 GitHub 安装技能（含安全扫描） |

### 8.2 knowledge-work-plugins — 11 个角色插件

| 插件 | 场景 | 对接工具 |
|------|------|---------|
| `productivity` | 任务/日历/日常工作流 | Slack, Notion, Asana, Linear, Jira, Microsoft 365 |
| `sales` | 客户调研/通话准备/漏斗 | Slack, HubSpot, Close, Clay, ZoomInfo |
| `customer-support` | 工单分类/回复/知识库 | Slack, Intercom, HubSpot, Guru, Jira |
| `product-management` | 规格书/路线图/用户研究 | Slack, Linear, Figma, Amplitude, Pendo |
| `marketing` | 内容/活动/品牌语调 | Slack, Canva, Figma, HubSpot, Ahrefs |
| `legal` | 合同审查/NDA/合规 | Slack, Box, Egnyte, Jira, Microsoft 365 |
| `finance` | 日记账/对账/财报/审计 | Snowflake, Databricks, BigQuery, Slack |
| `data` | SQL/统计分析/仪表盘 | Snowflake, Databricks, BigQuery, Hex |
| `enterprise-search` | 跨工具统一搜索 | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| `bio-research` | 临床前研究/基因组学 | PubMed, bioRxiv, ChEMBL, Open Targets |
| `cowork-plugin-management` | 创建/定制新插件 | — |

### 8.3 agency-agents — 完整 AI 机构角色库

| 项目 | 说明 |
|------|------|
| **来源** | msitarzewski/agency-agents（105k★） |
| **定位** | 社区版 AI 角色库，全岗位覆盖 |

---

## 九、特定技术栈技能（Mindrally 240+）

安装 `npx skills add mindrally/skills --skill <子包>` 按需安装，不必全装。

| 分类 | 包含 Skill |
|------|-----------|
| **前端** | react、nextjs、vue、angular、svelte、sveltekit、remix、astro、nuxtjs |
| **移动** | react-native、expo、flutter、swift、swiftui、android、kotlin、ionic |
| **后端** | nodejs、express、fastapi、django、flask、rails、laravel、spring-boot、go、nestjs、graphql、grpc、trpc |
| **语言** | typescript、python、go、rust、java、c-sharp、ruby、php、elixir、julia、lua、cpp |
| **数据库** | prisma、drizzle、sequelize、typeorm、mongodb、postgresql、mysql、redis、elasticsearch、supabase |
| **DevOps** | docker、kubernetes、terraform、aws、gcp、azure、ci-cd、github-workflow、gitlab-workflow、serverless |
| **测试** | jest、cypress、playwright、python-testing、rspec |
| **AI/ML** | pytorch、langchain、llamaindex、openai-api、anthropic-claude、transformers、ml、cv、nlp |
| **样式** | tailwindcss、css、sass、styled-components、framer-motion、three-js、design-systems |
| **构建** | vite、webpack、esbuild、parcel、rollup、turbopack |
| **认证** | auth0 |

---

## 十、快速选择矩阵

| 场景 | 首选 Skill | 来源 | 备用 |
|------|-----------|------|------|
| **需求模糊** | `/grill-me` | mattpocock | `/think` |
| **方案设计** | `/think` | Waza | agent-skills `/plan` |
| **PRD 编写** | `/spec` | agent-skills | `/to-prd`(mattpocock) |
| **深度研究** | `/learn` | Waza | `deep-research` |
| **网页调研** | `read` | Waza | `defuddle` |
| **社交媒体** | `agent-reach` | 生态 | `web-scraping` |
| **代码审查** | `code-review` | 多版本 | `/simplify` |
| **调试排查** | `/hunt` | Waza | `diagnosing-bugs` |
| **TDD 开发** | `/test` / `tdd` | agent-skills/mattpocock | `incremental-implementation` |
| **架构改进** | `/improve-codebase-architecture` | mattpocock | agent-skills 全套 |
| **笔记操作** | `obsidian-cli` | kepano | `obsidian-vault`(mattpocock) |
| **格式处理** | `obsidian-markdown` | kepano | — |
| **中文创作** | `baoyu-*` | baoyu-skills | `write` |
| **文档生成** | `docx`/`pptx`/`pdf`/`xlsx` | anthropics/skills | — |
| **UI 设计** | `design`(内置) | Claude Code | `ui-ux-pro-max-skill` |
| **浏览器自动化** | `agent-browser` | Vercel | OpenCLI |
| **多智能体编排** | `/do`(myclaude) | myclaude | `omo`/`sparv` |
| **角色化插件** | knowledge-work-plugins | Anthropic | agency-agents |
| **全栈技术** | mindrally/skills | Mindrally | 按需 `--skill` |
| **视频编程** | `remotion-best-practices` | remotion-dev | — |
| **创建 Skill** | `skill-creator` | anthropics/skills | `writing-great-skills` |
| **Agent 行为基调** | Karpathy 四大原则 | karpathy-skills | — |

---

## 关联笔记

- [[04-Skills生态全景]] — 13 核心仓库的深入对比分析
- [[03-通用skills最佳实践]] — Skills 使用心法与 description 优化
- [[05-需求到执行-Skills工作流]] — 需求→执行四阶段通用流程
- [[官方与社区Skill资源集成指南]] — 去哪找 Skill、哪些来源可信
- [[Obsidian-Agent操作指南]] — Obsidian 相关技能详细操作
- [[02-我的skills蒸馏]] — 个人高频技能记录
