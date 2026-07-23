---
title: Skills 生态全景
domain: Core_Ability
tags: [AI, Agent, Skills, 生态, 开源项目, 索引]
status: 稳定
created: 2026-07-06
updated: 2026-07-06
related:
  - "01-快速说明"
  - "02-我的skills蒸馏"
  - "03-通用skills最佳实践"
  - "03-Resources(资源层)/00 Github优质项目/Github优质项目-MOC"
summary: "Skills 生态的完整全景——从 Anthropic 官方规范源头到社区最大集合，13 个核心仓库按定位分类，含安装方式、设计哲学和选型建议"
---

# Skills 生态全景

> 截至 2026-07-06，Skills 生态已从 Anthropic 官方规范发展到 1000+ 技能覆盖全技术栈，形成了「官方规范 → 工程习惯 → 内容创作 → 多智能体编排 → 技术栈全覆盖」的多层次格局。

## 一、生态总览

Skills 生态可按定位分为 6 层：

```
官方规范层 ── anthropics/skills（141k★）—— 定义标准
    │
    ├─ 索引层 ── ComposioHQ/awesome-claude-skills（66.9k★）
    │            ComposioHQ/awesome-codex-skills（11.8k★）
    │
    ├─ 工程习惯层 ── tw93/Waza / mattpocock/skills（106k★）
    │                 addyosmani/agent-skills（45.9k★）
    │                 multica-ai/andrej-karpathy-skills（156k★）
    │
    ├─ 内容创作层 ── JimLiu/baoyu-skills（20+ 中文技能）
    │
    ├─ 多智能体层 ── stellarlinkco/myclaude
    │                 msitarzewski/agency-agents（105k★）
    │                 anthropics/knowledge-work-plugins（16.3k★）
    │
    ├─ 技术栈层 ── Mindrally/skills（240+ 技能）
    │               remotion-dev/skills（视频编程）
    │               kepano/obsidian-skills（Obsidian 生态）
    │
    └─ 浏览器自动化层 ── vercel-labs/agent-browser（37.9k★）
                         jackwener/OpenCLI（22.7k★）
```

## 二、各仓库详解

### 2.1 官方规范层

#### anthropics/skills（141k★）— 生态源头

- **定位**：Skill 格式标准的定义者，所有 Skills 生态的根仓库
- **内容**：17 个官方示例技能（创意/设计/技术/企业）+ 文档技能（docx/pdf/pptx/xlsx）+ Skill 规范 + 模板
- **安装**：`/plugin marketplace add anthropics/skills`
- **许可证**：Apache-2.0（示例技能）/ 源码可用（文档技能）
- **关键技能**：`canvas-design`、`mcp-builder`、`webapp-testing`、`skill-creator`、`web-artifacts-builder`
- **链接**：[[anthropics-skills-官方Skills仓库]]

### 2.2 索引层

#### ComposioHQ/awesome-claude-skills（66.9k★）— 最全索引

- **定位**：1000+ 生产级 Claude Skills 精选列表，覆盖全场景
- **内容**：文档处理、开发工具、数据分析、商业营销、写作沟通、创意媒体、生产力、项目管理、安全、78 个 SaaS 自动化技能
- **亮点**：自带 connect-apps 插件，Claude 可直接操作 500+ 应用（Gmail/Slack/GitHub/Notion 等）
- **安装**：`claude --plugin-dir ./connect-apps-plugin`
- **链接**：[[awesome-claude-skills-Claude技能精选]]

#### ComposioHQ/awesome-codex-skills（11.8k★）— Codex 索引

- **定位**：Codex Skills 精选列表，5 大类 + 安装器 + 创建模板
- **内容**：开发工具、协作效率、写作沟通、数据分析、元工具
- **链接**：[[awesome-codex-skills-Codex技能精选]]

### 2.3 工程习惯层

#### tw93/Waza — 8 个工程习惯

- **定位**：把优秀工程师的日常习惯固化为技能，小而精
- **8 个技能**：`/think`（方案设计）、`/ui`（前端界面）、`/check`（发布前审查）、`/hunt`（系统化调试）、`/write`（散文润色）、`/learn`（六阶段研究）、`/read`（URL/PDF 读取）、`/health`（Agent 健康审计）
- **设计哲学**：克制（每个技能只做一件事）、可链式组合（think→check→merge）、来自真实项目经验（300+ 会话）
- **安装**：`npx skills add tw93/Waza -a claude-code codex cursor -g -y`
- **链接**：[[waza-工程习惯技能包]]

#### mattpocock/skills（106k★）— 工程师日常

- **定位**：TypeScript 大牛 Matt Pocock 的日常技能包，小/可组合/可定制
- **核心理念**：拒绝 GSD/BMAD/Spec-Kit 那种「接管流程但失去控制」的方案
- **关键技能**：`/grill-me`（需求对齐）、`/grill-with-docs`（+ 领域建模）、`/tdd`（红绿重构）、`/diagnosing-bugs`（调试循环）、`/improve-codebase-architecture`（架构救赎）、`/triage`（Issue 分诊）、`/to-prd`（PRD 生成）
- **安装**：`npx skills@latest add mattpocock/skills`
- **链接**：[[mattpocock-skills-工程师日常技能]]

#### addyosmani/agent-skills（45.9k★）— Google 工程文化

- **定位**：23 个生产级工程技能，融入 Google 工程文化（Hyrum 定律/Beyonce 规则/Chesterton's Fence）
- **覆盖**：spec→plan→build→test→review→ship 全生命周期
- **关键命令**：`/spec`、`/plan`、`/build`、`/test`、`/review`、`/code-simplify`、`/ship`
- **设计亮点**：Anti-rationalization（每个技能含常见借口表及反驳论据）、Verification is non-negotiable
- **安装**：`/plugin marketplace add addyosmani/agent-skills`
- **链接**：[[agent-skills-生产级工程技能包]]

#### andrej-karpathy-skills（156k★）— 极简指南

- **定位**：一个 CLAUDE.md 文件，四大原则（Think/Simplify/Surgical/Goal-Driven）
- **特点**：极简（一个文件）、源自 Karpathy 实战观察、可直接叠加到任何 Skill 包
- **链接**：[[andrej-karpathy-skills-四大原则指南]]

### 2.4 内容创作层

#### JimLiu/baoyu-skills — 中文内容创作

- **定位**：20+ 中文内容创作 Agent Skills，配套图书《图解 Skill —— AI 提效实战指南》
- **内容技能**：小红书图片卡片（12 风格 × 6 布局）、信息图（21 布局 × 21 风格）、SVG 图表、封面图、幻灯片、知识漫画、文章插图
- **发布技能**：X/Twitter、微信公众号（API/浏览器/远程 API 三种方式）、微博
- **AI 生成**：多后端图像生成（OpenAI/Azure/Google/OpenRouter/DashScope/MiniMax/即梦/豆包/Replicate）
- **工具技能**：YouTube 字幕下载、URL→Markdown、翻译（三模式）、微信群精华提取、Electron 源码提取
- **安装**：`npx skills add jimliu/baoyu-skills`
- **链接**：[[baoyu-skills-中文内容创作技能]]

### 2.5 多智能体层

#### stellarlinkco/myclaude — 多智能体工作流

- **定位**：Claude Code 多智能体工作流系统，多后端执行（Codex/Claude/Gemini/OpenCode）
- **架构**：Claude Code 编排 + codeagent-wrapper 执行
- **工作流**：do（5 阶段推荐）、OmO（智能路由）、SPARV（Specify→Plan→Act→Review→Vault）、BMAD（敏捷 + 6 智能体）
- **11 开发命令**：`/code`、`/debug`、`/test`、`/review`、`/optimize`、`/refactor`、`/docs`、`/ask`、`/bugfix`、`/enhance-prompt`、`/think`
- **安装**：`npx github:stellarlinkco/myclaude`
- **许可证**：AGPL-3.0
- **链接**：[[myclaude-多智能体工作流系统]]

#### anthropics/knowledge-work-plugins（16.3k★）— 角色插件

- **定位**：Anthropic 官方 11 个知识工作插件，每个将 Claude 变成特定岗位专家
- **角色**：销售/客服/PM/市场/法务/财务/数据/企业搜索/生物研究/生产力/插件管理
- **架构**：Skills（自动激活）+ Commands（斜杠命令）+ Connectors（MCP 对接外部工具），纯 Markdown+JSON 零代码
- **链接**：[[knowledge-work-plugins-知识工作角色插件]]

#### agency-agents（105k★）— 社区角色库

- **定位**：社区版角色库，从工程到市场/运营/Reddit 社区管理全覆盖
- **链接**：[[agency-agents-完整AI机构角色库]]

### 2.6 技术栈层

#### Mindrally/skills — 240+ 全栈技能

- **定位**：从 Cursor Rules 转换的最大技能集合之一
- **覆盖**：前端框架（React/Vue/Angular/Svelte 等）、移动开发、后端 API、语言（12 种）、数据库 ORM、DevOps、测试、AI/ML、样式 UI、构建工具、认证
- **安装**：复制到 `.claude/skills/` 或 `~/.claude/skills/`
- **链接**：[[mindrally-skills-全技术栈技能集合]]

#### remotion-dev/skills — 视频编程

- **定位**：Remotion（React 视频渲染库）最佳实践
- **内容**：动画设计（interpolate/spring）、字幕、音频、3D、图表、动态时长
- **安装**：`npx skills add remotion-dev/skills`
- **链接**：[[remotion-skills-视频编程技能]]

#### kepano/obsidian-skills — Obsidian 生态

- **定位**：Obsidian 官方 Skill 集，5 个技能覆盖 Obsidian 全操作
- **技能**：`obsidian-markdown`（Obsidian 风味 Markdown）、`obsidian-bases`（数据库视图）、`json-canvas`（Canvas 画布）、`obsidian-cli`（CLI 操作）、`defuddle`（网页→Markdown）
- **安装**：`npx skills add kepano/obsidian-skills`
- **链接**：详见 [[Obsidian-Skills-索引]]

### 2.7 浏览器自动化层

#### vercel-labs/agent-browser（37.9k★）— 浏览器自动化 CLI

- **定位**：Vercel 出品的 Rust 原生浏览器自动化 CLI，专为 AI Agent 设计
- **核心模式**：无障碍树快照（accessibility tree）→ 按 ref ID 操作元素
- **关键命令**：`snapshot`（无障碍树）、`click @e2`（按 ref 点击）、`fill @e3 "text"`（填表）、`read`（无需启动浏览器的页面读取）、`chat`（自然语言操控）
- **安装**：`npm install -g agent-browser`
- **链接**：[[agent-browser-浏览器自动化CLI]]

#### jackwener/OpenCLI（22.7k★）— 网站→CLI

- **定位**：将任意网站变成 CLI 命令，AI Agent 操控已登录浏览器
- **内置适配器**：B站/知乎/小红书/Reddit/HackerNews/Twitter/LinkedIn 等 90+ 站点
- **AI 技能**：`opencli-browser`（浏览器操控）、`opencli-adapter-author`（适配器生成）、`opencli-autofix`（适配器修复）
- **安装**：`npm install -g @jackwener/opencli`
- **链接**：[[03-Resources(资源层)/00 Github优质项目/09-浏览器与网站自动化/opencli-网站CLI桥接工具]]

## 三、安装方式对照

| 安装方式 | 适用场景 | 命令示例 |
|---------|---------|---------|
| **npx skills** | 跨平台通用，推荐 | `npx skills add tw93/Waza -g -y` |
| **Plugin Marketplace** | Claude Code 原生 | `/plugin marketplace add anthropics/skills` |
| **手动复制** | 项目级安装 | `cp -r skills/react .claude/skills/` |
| **npx github** | 非 npm 包仓库 | `npx github:stellarlinkco/myclaude` |
| **npm 全局** | CLI 工具 | `npm install -g agent-browser` |

## 四、设计哲学对比

| 仓库 | 设计哲学 | 技能数量 | 适合谁 |
|------|---------|---------|--------|
| anthropics/skills | 官方规范 + 示例 | 17 | 所有人（参考学习） |
| Waza | 克制、可组合、实战 | 8 | 追求少而精的工程师 |
| mattpocock/skills | 小、可组合、可改 | ~15 | TypeScript 开发者 |
| agent-skills | Google 工程纪律 | 23 | 重视流程质量的团队 |
| baoyu-skills | 中文内容创作 | 20+ | 中文创作者 |
| myclaude | 多智能体编排 | 多模块 | 需要多 Agent 协作的场景 |
| Mindrally/skills | 全技术栈覆盖 | 240+ | 需要按需安装的开发者 |

## 五、选型建议

### 必装（核心基础）
- **anthropics/skills** — 官方文档技能（pdf/docx/pptx/xlsx）
- **andrej-karpathy-skills** — 一个文件，四大原则，零成本
- **agent-skills** 或 **mattpocock/skills** — 二选一，看偏好 Google 流程还是 TypeScript 实战

### 按需安装（场景驱动）
- **中文内容创作** → baoyu-skills（小红书/公众号/微博发布）
- **多智能体编排** → myclaude（do/OmO/SPARV 工作流）
- **视频编程** → remotion-skills
- **Obsidian 操作** → kepano/obsidian-skills
- **浏览器自动化** → agent-browser 或 OpenCLI（看偏好）

### 不建议全装
- 每个 skill 的元数据（name+description）常驻上下文，虽然 Token 消耗低但太多也会影响 AI 的判断效率
- 推荐策略：安装核心基础 + 当前项目需要的 3-5 个场景技能，定期更换

## 六、各仓库 Skill 子包清单

> 以下按仓库列出所有可用 Skill 子包，方便查阅和按需安装。调用方式：已安装后，在对话中描述需求即可自动触发，或使用 `/skill-name` 斜杠命令显式调用。

### 6.1 anthropics/skills — 17 个官方示例技能

| Skill 子包                | 描述            | 调用场景                             |
| ----------------------- | ------------- | -------------------------------- |
| `algorithmic-art`       | 算法艺术生成        | 生成数学/算法驱动的视觉艺术作品                 |
| `brand-guidelines`      | 品牌规范应用        | 应用 Anthropic 官方品牌色和字体            |
| `canvas-design`         | 画布设计          | 创建 PNG/PDF 视觉艺术作品                |
| `claude-api`            | Claude API 开发 | 使用 Claude API 构建应用               |
| `doc-coauthoring`       | 文档协作          | 多人协作编辑文档                         |
| `docx`                  | Word 文档       | 创建/编辑/分析 .docx 文件                |
| `frontend-design`       | 前端设计          | 前端 UI 设计最佳实践                     |
| `internal-comms`        | 内部沟通          | 撰写公司内部通讯/简报/FAQ                  |
| `mcp-builder`           | MCP 服务器构建     | 创建 MCP 服务器连接外部 API               |
| `pdf`                   | PDF 处理        | 提取文本/表格/合并/标注 PDF                |
| `pptx`                  | 幻灯片           | 读写/生成/调整幻灯片                      |
| `skill-creator`         | Skill 创建      | 创建自定义 Skill 的指南                  |
| `slack-gif-creator`     | Slack GIF 创建  | 创建适合 Slack 的动画 GIF               |
| `theme-factory`         | 主题工厂          | 应用字体和颜色主题到构件                     |
| `web-artifacts-builder` | Web 构件构建      | 创建 React/Tailwind/shadcn HTML 构件 |
| `webapp-testing`        | Web 应用测试      | 使用 Playwright 测试本地 Web 应用        |
| `xlsx`                  | 电子表格          | 公式/图表/数据转换                       |

### 6.2 tw93/Waza — 8 个工程习惯技能

| Skill 子包 | 斜杠命令 | 描述 | 调用时机 |
|-----------|---------|------|---------|
| `think` | `/think` | 挑战问题、压力测试设计、产出决策完备计划 | **构建任何新东西之前** |
| `ui` | `/ui` | 产出有方向感的前端 UI，截图驱动审美迭代 | **构建前端界面** |
| `check` | `/check` | 审查 diff、提取项目约束、处理发布/推送/验证 | **任务完成后、合并/发布前** |
| `hunt` | `/hunt` | 系统化调试，确认根因后再修复 | **任何 Bug/回归/异常行为** |
| `write` | `/write` | 重写散文使其自然（中英文），去公式化表达 | **写作或编辑散文** |
| `learn` | `/learn` | 六阶段研究：收集→消化→大纲→填充→润色→发布 | **进入陌生领域** |
| `read` | `/read` | 按平台路由读取 URL/PDF，摘要或 Markdown 输出 | **任何 URL 或 PDF** |
| `health` | `/health` | 检查 Codex/Claude Code/项目指令/Verifier/AI 可维护性 | **审计 Agent 健康度** |

### 6.3 mattpocock/skills — 工程 & 生产力技能

| Skill 子包                        | 斜杠命令                             | 类型   | 描述                                |
| ------------------------------- | -------------------------------- | ---- | --------------------------------- |
| `ask-matt`                      | `/ask-matt`                      | 用户调用 | 询问哪个 skill 适合当前场景（路由）             |
| `grill-with-docs`               | `/grill-with-docs`               | 用户调用 | 需求对齐 + 领域建模，更新 CONTEXT.md 和 ADR   |
| `triage`                        | `/triage`                        | 用户调用 | Issue 分诊状态机                       |
| `improve-codebase-architecture` | `/improve-codebase-architecture` | 用户调用 | 扫描代码库架构问题，生成 HTML 报告              |
| `setup-matt-pocock-skills`      | `/setup-matt-pocock-skills`      | 用户调用 | 配置 Issue Tracker/标签/文档路径          |
| `to-issues`                     | `/to-issues`                     | 用户调用 | 将计划/spec/PRD 拆分为独立 Issue          |
| `to-prd`                        | `/to-prd`                        | 用户调用 | 将当前对话综合为 PRD 并发布                  |
| `prototype`                     | —                                | 模型调用 | 构建可丢弃的原型验证设计                      |
| `diagnosing-bugs`               | —                                | 模型调用 | 系统化调试循环：复现→最小化→假设→验证              |
| `research`                      | —                                | 模型调用 | 针对高信任源调查问题，产出引用 Markdown          |
| `tdd`                           | —                                | 模型调用 | 红-绿-重构 TDD 循环                     |
| `domain-modeling`               | —                                | 模型调用 | 构建和精炼项目领域模型                       |
| `codebase-design`               | —                                | 模型调用 | 设计深度模块的规范和词汇                      |
| `code-review`                   | —                                | 模型调用 | 双轴审查（标准合规 + Spec 实现）              |
| `grill-me`                      | `/grill-me`                      | 用户调用 | 非代码场景的需求对齐追问                      |
| `handoff`                       | `/handoff`                       | 用户调用 | 压缩当前对话为交接文档                       |
| `teach`                         | `/teach`                         | 用户调用 | 多会话教授用户新技能                        |
| `writing-great-skills`          | —                                | 参考   | 编写高质量 Skill 的词汇和原则                |
| `grilling`                      | —                                | 模型调用 | grill-me/grill-with-docs 背后的可复用循环 |

### 6.4 addyosmani/agent-skills — 23 个生产级工程技能

| Skill 子包 | 斜杠命令 | 生命周期阶段 | 描述 |
|-----------|---------|------------|------|
| `interview-me` | — | Define | 一对一访谈，挖出用户真正需求 |
| `idea-refine` | — | Define | 发散/收敛思维，模糊想法→具体方案 |
| `spec-driven-development` | `/spec` | Define | 先写 PRD 再写代码 |
| `planning-and-task-breakdown` | `/plan` | Plan | 将 spec 分解为小而原子的任务 |
| `incremental-implementation` | `/build` | Build | 一次一个切片，持续可运行 |
| `context-engineering` | — | Build | 优化 Agent 上下文利用效率 |
| `source-driven-development` | — | Build | 先读现有代码再写新代码 |
| `doubt-driven-development` | — | Build | 不确定时主动停下来确认 |
| `frontend-ui-engineering` | — | Build | 前端 UI 工程最佳实践 |
| `test-driven-development` | `/test` | Verify | TDD 红→绿→重构循环 |
| `api-and-interface-design` | — | Build | API 设计规范（含 Hyrum 定律） |
| `browser-testing-with-devtools` | — | Verify | 浏览器 DevTools 验证 |
| `debugging-and-error-recovery` | — | Verify | 系统化调试与错误恢复 |
| `code-review-and-quality` | `/review` | Review | 代码审查与质量门禁 |
| `code-simplification` | `/code-simplify` | Review | 简化代码（Chesterton's Fence） |
| `security-and-hardening` | — | Review | 安全加固审查 |
| `performance-optimization` | — | Review | 性能优化 |
| `git-workflow-and-versioning` | — | Ship | 主干开发 + 版本管理 |
| `ci-cd-and-automation` | — | Ship | CI/CD 自动化（Shift Left + Feature Flags） |
| `deprecation-and-migration` | — | Ship | 废弃与迁移——代码即负债 |
| `documentation-and-adrs` | — | Ship | 文档 + 架构决策记录 |
| `shipping-and-launch` | `/ship` | Ship | 发布上线流程 |
| `using-agent-skills` | — | Meta | 自动匹配任务到对应技能 |

### 6.5 JimLiu/baoyu-skills — 20+ 中文内容创作技能

| Skill 子包 | 斜杠命令 | 分类 | 描述 |
|-----------|---------|------|------|
| `baoyu-xhs-images` | `/baoyu-xhs-images` | 内容 | 小红书图片卡片（12 风格 × 6 布局 × 3 配色） |
| `baoyu-infographic` | `/baoyu-infographic` | 内容 | 信息图（21 布局 × 21 风格） |
| `baoyu-diagram` | `/baoyu-diagram` | 内容 | SVG 图表（流程图/时序图/架构图/示意图/类图） |
| `baoyu-cover-image` | `/baoyu-cover-image` | 内容 | 文章封面图（5 维定制） |
| `baoyu-slide-deck` | `/baoyu-slide-deck` | 内容 | 幻灯片（16 风格预设，输出 PPTX+PDF） |
| `baoyu-comic` | `/baoyu-comic` | 内容 | 知识漫画（5 画风 × 7 基调） |
| `baoyu-article-illustrator` | `/baoyu-article-illustrator` | 内容 | 文章插图（类型 × 风格 × 色板） |
| `baoyu-post-to-x` | `/baoyu-post-to-x` | 发布 | 发布到 X/Twitter |
| `baoyu-post-to-wechat` | `/baoyu-post-to-wechat` | 发布 | 发布到微信公众号（API/浏览器/远程 API） |
| `baoyu-post-to-weibo` | `/baoyu-post-to-weibo` | 发布 | 发布到微博 |
| `baoyu-image-gen` | `/baoyu-image-gen` | AI 生成 | 多后端图像生成（10 个服务商） |
| `baoyu-danger-gemini-web` | `/baoyu-danger-gemini-web` | AI 生成 | Gemini Web 交互（文本+图片） |
| `baoyu-youtube-transcript` | `/baoyu-youtube-transcript` | 工具 | YouTube 字幕下载（多语言/翻译/章节） |
| `baoyu-url-to-markdown` | `/baoyu-url-to-markdown` | 工具 | URL → Markdown 抓取 |
| `baoyu-danger-x-to-markdown` | `/baoyu-danger-x-to-markdown` | 工具 | X/Twitter 内容 → Markdown |
| `baoyu-compress-image` | `/baoyu-compress-image` | 工具 | 图片压缩 |
| `baoyu-format-markdown` | `/baoyu-format-markdown` | 工具 | Markdown 格式化 |
| `baoyu-markdown-to-html` | `/baoyu-markdown-to-html` | 工具 | Markdown → HTML（公众号兼容） |
| `baoyu-translate` | `/translate` | 工具 | 三模式翻译（快速/标准/精翻） |
| `baoyu-wechat-summary` | `/baoyu-wechat-summary` | 工具 | 微信群聊精华提取 |
| `baoyu-electron-extract` | `/baoyu-electron-extract` | 工具 | Electron 应用源码提取 |

### 6.6 stellarlinkco/myclaude — 多智能体工作流模块

| 模块/技能 | 斜杠命令 | 描述 |
|----------|---------|------|
| `do`（5 阶段） | `/do` | 推荐工作流：Understand→Clarify→Design→Implement+Review→Complete |
| `omo`（多智能体编排） | `/omo` | 智能路由到 oracle/librarian/explore/develop 等专业 Agent |
| `sparv` | `/sparv` | Specify→Plan→Act→Review→Vault 极简 5 阶段 |
| `bmad` | `/bmad-pilot` | 敏捷工作流 + 6 个专业智能体（PO/Architect/Scrum Master/Dev/Reviewer/QA） |
| `requirements` | `/requirements-pilot` | 轻量级需求到代码流水线 |
| `essentials` | `/code /debug /test /review` 等 | 11 个核心开发命令 |
| `browser` | — | 浏览器自动化测试和数据提取 |
| `codeagent` | — | 多后端 AI 代码任务调用（Codex/Claude/Gemini/OpenCode） |
| `product-requirements` | — | 交互式 PRD 生成（含质量评分） |
| `test-cases` | — | 从需求生成全面测试用例 |
| `skill-install` | — | 从 GitHub 安装技能（含安全扫描） |

### 6.7 jackwener/OpenCLI — 6 个 AI Agent 技能

| Skill 子包 | 描述 | 调用场景 |
|-----------|------|---------|
| `opencli-browser` | 驱动 Chrome 浏览器——导航、点击、填表、提取 | 需要 AI 操控已登录浏览器 |
| `opencli-adapter-author` | 为任意网站编写 CLI 适配器 | 需要为新网站生成 CLI 命令 |
| `opencli-autofix` | 修复损坏的适配器 | 内置命令返回空/报错时 |
| `opencli-browser-sitemap` | 使用站点地图导航浏览器 | 需要结构化浏览网站 |
| `opencli-sitemap-author` | 创建/更新站点地图知识 | 记录稳定的浏览器工作流 |
| `opencli-usage` | OpenCLI 命令和站点快速参考 | 需要查询 OpenCLI 有哪些命令 |

### 6.8 kepano/obsidian-skills — 5 个 Obsidian 技能

| Skill 子包 | 描述 | 调用场景 |
|-----------|------|---------|
| `obsidian-markdown` | Obsidian 风味 Markdown（wikilink/embeds/callout/properties） | 编辑 Obsidian 笔记格式 |
| `obsidian-bases` | Obsidian Bases 数据库视图（views/filters/formulas/summaries） | 创建/编辑 .base 文件 |
| `json-canvas` | JSON Canvas 画布文件（nodes/edges/groups/connections） | 创建/编辑 .canvas 文件 |
| `obsidian-cli` | Obsidian CLI 操作 + 插件/主题开发 | 通过 CLI 操作 Obsidian |
| `defuddle` | 网页→干净 Markdown 提取 | 提取网页正文节省 Token |

### 6.9 Mindrally/skills — 240+ 全栈技能（按分类）

| 分类 | 包含 Skill 子包 |
|------|----------------|
| **前端框架** | react、nextjs-react-typescript、vue-typescript、angular、svelte、sveltekit、remix、astro、nuxtjs-vue-typescript |
| **移动开发** | react-native-cursor-rules、expo-react-native-typescript、flutter、swift、swiftui-development、android-development、kotlin-development、ionic |
| **后端 & API** | nodejs-development、express-typescript、fastapi-python、django-python、flask-python、ruby-rails、laravel、spring-boot、go-backend-microservices、nestjs-clean-typescript、graphql、grpc-development、trpc |
| **语言** | typescript、python、go、rust、java、c-sharp、ruby、php-development、elixir、julia、lua、cpp |
| **数据库 & ORM** | prisma、drizzle-orm、sequelize、typeorm、mongodb-development、postgresql-best-practices、mysql-best-practices、redis-best-practices、elasticsearch-best-practices、supabase |
| **DevOps** | docker、kubernetes、terraform、aws-development、gcp-development、azure、ci-cd-best-practices、github-workflow、gitlab-workflow、serverless |
| **测试** | testing、jest、cypress、playwright、python-testing、rspec |
| **AI & ML** | deep-learning、pytorch、langchain-development、llamaindex-development、openai-api-development、anthropic-claude-development、transformers-huggingface、machine-learning、computer-vision-opencv、nlp-natural-language-processing |
| **样式 & UI** | tailwindcss、css、sass-best-practices、styled-components-best-practices、framer-motion、three-js、design-systems、ui-design、ux-design |
| **构建工具** | vite、webpack-bundler、esbuild-bundler、parcel-bundler、rollup-bundler、turbopack-bundler |
| **认证** | auth0-authentication |

### 6.10 andrej-karpathy-skills — 1 个文件 4 原则

| 原则 | 解决的问题 | 说明 |
|------|-----------|------|
| Think Before Coding | 错误假设、隐藏困惑 | 先思考再编码 |
| Simplicity First | 过度复杂、臃肿抽象 | 优先简单方案 |
| Surgical Changes | 正交修改、误伤无关代码 | 精准手术式修改 |
| Goal-Driven Execution | 测试先行、可验证成功标准 | 目标驱动执行 |

### 6.11 anthropics/knowledge-work-plugins — 11 个角色插件

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

### 6.12 remotion-dev/skills — 1 个视频编程技能

| Skill 子包 | 描述 | 核心规则 |
|-----------|------|---------|
| `remotion-best-practices` | Remotion 视频编程最佳实践 | 用 `interpolate()` 非 `spring()`、禁止 CSS transitions/animations、资源放 `public/`、用 `<Sequence>` 控制时间 |

### 6.13 vercel-labs/agent-browser — 浏览器自动化 CLI 命令

> 注意：agent-browser 不是 SKILL.md 格式，而是独立的 CLI 工具，通过命令行直接调用。

| 命令 | 描述 |
|------|------|
| `agent-browser open <url>` | 启动浏览器 + 导航 |
| `agent-browser snapshot` | 获取无障碍树快照（AI 最佳输入） |
| `agent-browser click @e2` | 按 ref ID 点击元素 |
| `agent-browser fill @e3 "text"` | 按 ref ID 填表 |
| `agent-browser type @e3 "text"` | 按 ref ID 输入 |
| `agent-browser screenshot [path]` | 截图（支持标注编号） |
| `agent-browser read [url]` | 获取页面可读文本（无需启动浏览器） |
| `agent-browser eval <js>` | 执行 JavaScript |
| `agent-browser chat "<指令>"` | 自然语言浏览器操控 |
| `agent-browser close` | 关闭浏览器 |

---

## 七、关联笔记

- [[01-快速说明]] — Agent Skills 概念入门
- [[02-我的skills蒸馏]] — 个人 skills 的持续记录与优化
- [[03-通用skills最佳实践]] — Skills 使用心法与实战案例
- [[03-Resources(资源层)/00 Github优质项目/Github优质项目-MOC]] — 项目索引总表
