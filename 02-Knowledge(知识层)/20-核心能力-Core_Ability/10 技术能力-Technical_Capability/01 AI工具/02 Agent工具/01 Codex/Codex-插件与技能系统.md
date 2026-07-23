---
title: Codex 插件与技能系统（含市场全目录）
domain: Core_Ability
tags: [Codex, 插件, Skills, Plugins, MCP, Marketplace, 对比, Claude]
status: 稳定
created: 2026-07-17
updated: 2026-07-17
source: "插件 marketplace 官方 plugin.json; config.toml 配置; skills_instructions 运行时"
summary: "Codex 扩展体系完全手册 + 插件市场全目录——三层架构、Skills 详解、16 个已启用 + 1 个未启用 + 180 个可安装插件的官方描述和中文说明，MCP 集成，Claude 对比，实践指南。"
---

# Codex 插件与技能系统（含市场全目录）

> Codex 扩展体系分为三层：Skills → Agent-Skills → Plugins。全部 197 个插件的中文说明与使用示例。

---

## 整体架构

```
Codex 扩展体系                        Claude 扩展体系
──────────────────────              ──────────────────────

Plugins（17 个可用/16 个启用）       .claude/skills/（单层）
  ├─ Skills + MCP + Apps             └─ SKILL.md + scripts
  └─ 通过 marketplace 分发

Agent-Skills（.agents/skills/）
  └─ 浏览器/调研/爬虫等智能体行为

User/System Skills
  ├─ .system/（系统内置）
  └─ .codex/skills/（用户安装）

MCP Servers（独立配置）              MCP Servers（独立配置）
```

| 层级 | 复杂度 | 示例 |
|------|--------|------|
| Skill | 低 | SKILL.md + scripts |
| Agent-Skill | 中 | .agents/skills/ |
| Plugin | 高 | Skills + MCP + Apps 打包 |
| MCP | 中 | config.toml 配置 |

---

## Skills 详解

### 目录结构
```
skill-name/
├── SKILL.md          # 核心指令（description 决定自动触发）
├── scripts/          # 辅助脚本
├── references/       # 按需加载文档
└── assets/           # 模板/输出
```

### 已安装 Skills（14+）

**系统内置**（`.system/`）：imagegen, openai-docs, plugin-creator, skill-creator, skill-installer

**用户安装**（`.codex/skills/`）：agent-browser, agent-reach, cli-creator, figma, pdf, playwright, find-skills, check, docx, pptx, mcp-builder

**Agent-Skills**（`.agents/skills/`）：agent-browser, agent-reach, find-skills, frontend-design, web-scraping, defuddle, hunt, read, antigravity, json-canvas, mcp-builder, obsidian-bases, obsidian-cli, obsidian-markdown, obsidian-vault, opencli-browser, write, yuanbao

### 创建 Skill
1. **从零构建**：告知需求，自动生成标准结构
2. **从工作流沉淀（推荐）**：跑通一次完整流程后，说"刚才这套流程，帮我做成一个 Skill"

### 自动记忆
设置 → 个性化 → 自动记忆。触发条件：对话足够长 + 额度充足 + 闲置状态。召回类似 RAG：关键词匹配 → 项目关联 → 时间衰减。

---

## Plugins 总览

### Marketplace 来源

| Marketplace | 类型 | 插件 | 版本 |
|-------------|------|------|------|
| `openai-bundled` | 官方内置 | browser, chrome, computer-use, visualize, latex | v26.715.21425+ |
| `openai-primary-runtime` | 官方运行时 | documents, spreadsheets, presentations, pdf, template-creator* | v26.715.12143 |
| `openai-api-curated` | 社区精选（官方审核） | github, superpowers, game-studio, zotero, hyperframes, remotion | v0.1.2~5.1.3 |
| `openai-bundled` 可安装市场 | 第三方 | 180 个插件（见下文分类目录） | — |

> \* template-creator 已安装但未启用。总安装数 17，已启用 16。

### 插件管理
- **桌面端**：左侧插件面板 → 拼图图标
- **config.toml**：`[plugins."name@marketplace"] enabled = true`
- **安装**：插件面板 `+` → 浏览 marketplace

### 插件结构
```
plugin-name/
├── .codex-plugin/plugin.json   # 清单：name/version/description/skills/MCP
├── skills/                     # 捆绑的 SKILL.md + scripts
├── apps/                       # 可选的应用
└── 自动注册 MCP 到 config.toml
---

## MCP 集成

```toml
[mcp_servers.node_repl]
command = '...node_repl.exe'
env.NODE_REPL_NODE_MODULE_DIRS = '...'
env.BROWSER_USE_AVAILABLE_BACKENDS = "chrome,iab"
```

**node_repl** 是核心 MCP：持久化 Node 运行时 + Playwright 浏览器自动化。

> Plugin 可内置 MCP（安装时自动写入 config.toml）；独立 MCP 需手动编辑。

---

## 触发机制

| 方式 | Codex | Claude |
|------|-------|--------|
| 名称触发 | 提及 skill/plugin 名 | 提及 skill 名 |
| 描述自动匹配 | `description` 字段 | `description` 字段 |
| 斜杠命令 | `/skill-name` | `/skill-name` |
| @插件名 | @browser, @browser-use 等 | ❌ 无 |
| 渐进式加载 | 主 agent 亲自读 SKILL.md | 可委托子 agent |

---

## 安装方式

| 方式 | 说明 |
|------|------|
| 对话安装 Skill | "帮我安装 xx Skill" |
| 对话安装 Plugin | 插件面板 `+` → marketplace |
| GitHub 安装 | 发链接给 Codex |
| find-skills 发现 | 搜索社区 skill 库 |
| 手动创建 | skill-creator 自动生成 |

---

## Codex vs Claude 关键差异

| 维度 | Codex | Claude |
|------|-------|--------|
| 扩展体系 | 3 层（skill → agent-skill → plugin） | 1 层（.claude/skills/） |
| Plugin | ✅ 打包 Skill + MCP + Apps | ❌ 无 |
| Agent-Skill 独立 | ✅ `.agents/skills/` | ❌ 混入常规 skills |
| MCP 管理 | config.toml 统一管理 | claude_desktop_config.json |
| Node REPL | ✅ 内置 node_repl | ❌ 无 |
| 系统级管理 | skill-creator 自我管理 | ❌ 需手动编辑 |

**设计哲学**：Codex 渐进式发现 + 三层组合（skill → agent-skill → plugin）；Claude 单层静态注入。

---

## 实践决策指南

| 需要 | 方案 |
|------|------|
| 固定操作流程 | 创建 Skill |
| 浏览器自动化 | agent-browser skill 或 browser Plugin |
| 全网调研 | agent-reach skill |
| 操控 Chrome | chrome Plugin |
| 操控桌面 | computer-use Plugin |
| 办公文档 | documents/spreadsheets/presentations Plugin |
| 连接外部知识库 | 配置 MCP Server |
| 代码审查 | check skill + github Plugin |
| 定时自动化 | Automations + Skill |

**优先级**：已有 Skill 自然调用 → 已有 Plugin @触发 → 新能力搜 find-skills → 创建 Skill

---

---

# 插件市场全目录

> 共 **已启用 16 + 未启用 1 + 可安装 180 = 197** 个插件。按功能分类，含中文说明与使用示例。

---

## 已启用插件（16 个）

### 浏览器与桌面操控

**browser**（`@browser`, `@browser-use`）
- **中文说明**：操控 ChatGPT 内置浏览器的插件。可打开网页、点击链接、填写表单、截图、测试 localhost 站点。
- **使用示例**："帮我打开 localhost:3000 看看效果"、"截图当前页面"
- **来源**：openai-bundled · v26.715.21425 · Engineering

**chrome**
- **中文说明**：操控已登录的 Chrome 浏览器。可访问有登录状态的网站，后台多标签页执行。
- **使用示例**："用 Chrome 打开 GitHub 创建仓库"、"查收最新邮件"
- **来源**：openai-bundled · v26.715.21425 · Productivity

**computer-use**
- **中文说明**：操控整个 Windows 电脑桌面。可操作任何应用程序，通过底层 cua 引擎驱动。
- **使用示例**："打开 Obsidian"、"在微信上发消息"
- **来源**：openai-bundled · v26.715.21425 · Productivity

### 办公生产力

**documents**
- **中文说明**：创建和编辑 Word/Google Docs 文档。支持从 Markdown、大纲生成格式化文档。
- **使用示例**："把 Markdown 转成 Word 报告"、"写一份项目方案书"
- **来源**：openai-primary-runtime · v26.715.12143

**spreadsheets**
- **中文说明**：创建/编辑/分析/导出 Excel/Google Sheets。支持公式、图表、数据清洗。
- **使用示例**："把销售数据做成表格加柱状图"、"分析 CSV 生成报表"
- **来源**：openai-primary-runtime · v26.715.12143

**presentations**
- **中文说明**：创建/编辑/导出 PowerPoint/Google Slides。支持大纲转幻灯片。
- **使用示例**："把提案做成 10 页 PPT"、"生成演讲幻灯片"
- **来源**：openai-primary-runtime · v26.715.12143

**pdf**
- **中文说明**：读取、创建、渲染和验证 PDF 文件。
- **使用示例**："把报告导出为 PDF"、"检查 PDF 排版"
- **来源**：openai-primary-runtime · v26.715.12143

### 开发与版本管理

**github**
- **中文说明**：GitHub 集成——PR/Issue/CI/发布。内置 Skills：gh-address-comments, gh-fix-ci, yeet。
- **使用示例**："查看 PR review 状态"、"调试 CI 失败"
- **来源**：openai-api-curated · v0.1.6

**superpowers**
- **中文说明**：Agentic 开发方法论框架。内置 13 个 Skills：脑暴/TDD/调试/审查/验证。
- **使用示例**："按 TDD 实现功能"、"审阅这段代码"
- **来源**：openai-api-curated · v5.1.3

**visualize**
- **中文说明**：在对话中创建交互式图表、地图、流程图、3D 模型。
- **使用示例**："做成折线图"、"画系统架构流程图"
- **来源**：openai-bundled · v1.0.12

### 创意与多媒体

**game-studio**
- **中文说明**：浏览器游戏全流程开发（2D/3D）。内置 9 个 Skills。
- **使用示例**："开发一个平台跳跃小游戏"
- **来源**：openai-api-curated · v0.1.2

**hyperframes**
- **中文说明**：写 HTML 渲染视频——GSAP 动效/字幕/配音/音画联动/网页转视频。内置 5 个 Skills。
- **版本**：v0.1.2 · **来源**：openai-api-curated
- **内置 Skills**：hyperframes, hyperframes-cli, hyperframes-registry, gsap, website-to-hyperframes

**使用方法**：在对话中自然描述需求，Codex 自动调用 hyperframes 相关 Skill 来生成 HTML 并渲染为视频。

**实际场景与操作指南**

**场景 1：产品介绍视频**
- **需求**：为新产品制作 30 秒宣传视频
- **操作示例**："帮我用 hyperframes 做 30 秒产品介绍，包含开场标题→3 个功能介绍（卡片切换）→CTA+LOGO，风格现代，品牌色 #2563EB"
- **工作流**：Codex 用 GSAP 写 HTML 动效 → 生成每帧画面 → 合成视频 → 输出 MP4
- **输出**：`.mp4` 文件（可选带字幕+配音）

**场景 2：教程讲解视频**
- **操作示例**："帮我把这篇博客做成讲解视频：提取要点作分页，加 GSAP 渐入动画，TTS 配音，自动添加中文字幕"
- **技巧**：先让 agent-reach 调研内容，再用 hyperframes 制作

**场景 3：社交媒体短视频（竖屏 9:16）**
- **操作示例**："做 15 秒竖屏视频：前 3 秒标题动画→中间 8 秒 4 个卖点→最后 4 秒品牌露出+引导关注"
- **输出**：直接生成可发布的竖屏视频文件

**场景 4：网页转视频**
- **操作示例**："帮我把这个网页（贴 URL）转成一段介绍视频，含截图和文字讲解"
- **原理**：browser-use 截取网页 → 整理脚本 → hyperframes 渲染


**Vibe Coding 场景**

**场景 5：创意粒子动画**
- **操作示例**："用 hyperframes 做一个 10 秒的粒子系统动画，彩色粒子从中心向外扩散，逐渐组成 'Hello World' 文字，GSAP 缓动，深色背景"
- **应用**：视频开场/intro/转场素材

**场景 6：产品 3D 旋转展示**
- **操作示例**："用 Three.js + hyperframes 做一个产品 360 度旋转展示视频，产品在白色背景上缓慢旋转，加环境光反射效果，底部有产品名称淡入"
- **技巧**：hyperframes 支持 Three.js 嵌入，适合产品官网/电商主图视频

**场景 7：动态数据可视化短视频**
- **操作示例**："帮我生成长宽比 1:1 的短视频，背景是深色渐变，中间是一个动态的环形图，数据从 0 增长到 75%，旁边显示 '75% 用户满意度'，用 GSAP 缓动动画，时长 8 秒"
- **原理**：先用 visualize 插件设计图表布局，hyperframes 渲染成动画视频

**场景 8：A/B 测试视频素材**
- **操作示例**："帮我生成 3 个版本的 5 秒片头动画，分别是：蓝色科技风、金色商务风、彩色创意风，每个版本输出单独的 MP4，方便我做 A/B 测试"
- **效率**：一次 prompt 批量生成多个版本，比手动制作快 10 倍

**场景 9：动态 Logo 动画**
- **操作示例**："帮我做一个 5 秒的公司 LOGO 动画：LOGO 从透明淡入，然后有一个微缩放大的呼吸效果循环，最后定格。背景渐变色 #0A1628 到 #1A365D"
- **输出**：可直接用于视频片头 / 网站 Hero 区域 / PPT 开场

**场景 10：文字排版动画**
- **操作示例**："做一个 quote 引用视频：'Vibe Coding is the future'，字体用粗体，文字逐字弹出，每字带轻微旋转，背景用毛玻璃效果，时长 6 秒"
- **格式**：竖屏 9:16，适合社交媒体传播
**最佳实践**
1. 先写脚本再制作，让 Codex 生成大纲确认后再渲染，省额度
2. 复用好效果后让 Codex 固化为 Skill
3. 单段 clip 建议 3-8 秒，先画面后配音分步迭代

**remotion**
- **中文说明**：用 React 写代码生成视频——动画/音频/字幕/3D。内置 remotion-best-practices Skill。
- **版本**：v1.0.3 · **来源**：openai-api-curated
- **与 hyperframes 的差异**：hyperframes 写 HTML 渲染视频（轻量、快速），remotion 用 React 代码生成视频（专业、可编程、适合复杂场景）

**使用方法**：在对话中描述视频需求，Codex 自动调用 remotion-best-practices Skill 编写 React 组件源码并渲染为视频。

**实际场景与操作指南**

**场景 1：产品发布会视频**
- **需求**：制作一段 60 秒的产品发布会开场视频，包含数据动效
- **操作示例**：
  ```
  "用 remotion 做一个 60 秒的产品发布会开场视频：
    - 0-5s：黑底白字 LOGO 淡入（带发光粒子效果）
    - 5-20s：3 个核心数据动效（用户数增长曲线 / 营收柱状图 / 覆盖区域地图）
    - 20-45s：产品功能演示动画（3 个功能依次出现，每个带 3D 翻转过渡）
    - 45-55s：客户评价轮播
    - 55-60s：Slogan + CTA
   色彩方案：深蓝 #0A1628 主色，青色 #00D4FF 强调色"
  ```
- **工作流**：Codex 生成 React 组件源码 → 本地渲染 → 逐帧合成 MP4 → 输出到项目目录
- **特点**：数据驱动的动画（传入 JSON 数据自动生成图表动画）

**场景 2：数据报告视频**
- **需求**：把季度销售数据做成可视化视频报告
- **操作示例**：
  ```
  "帮我把这份季度销售数据做成 2 分钟的可视化报告视频：
   1. 开头的数据概览动画（总收入、增长率、TOP3 产品）
   2. 月度趋势折线图（逐月展开动画）
   3. 各区域占比环形图（逐个扇区弹出）
   4. 同比对比柱状图（并排比较）
   5. 结尾关键结论文字页
   数据在这里：[贴 CSV/表格数据]"
  ```
- **技巧**：提前准备结构化数据（CSV/JSON），Codex 会直接嵌入 React 组件

**场景 3：教学/演示视频**
- **需求**：制作代码/操作步骤演示视频
- **操作示例**：
  ```
  "用 remotion 做一个代码教学视频：
   1. 逐行显示代码，高亮当前讲解行
   2. 右侧同步显示运行结果示意图
   3. 底部进度条显示当前位置
   4. 视频时长控制在 45 秒
   代码内容：[贴代码]"
  ```

**场景 4：社交媒体广告视频**
- **需求**：制作多渠道适配的广告视频（同内容不同尺寸）
- **操作示例**：
  ```
  "帮我做一个产品广告视频，输出 3 个版本：
   1. 横屏 16:9（YouTube）
   2. 竖屏 9:16（Reels/TikTok）
   3. 方形 1:1（朋友圈/小红书）
   内容：前 3 秒钩子 → 中间产品展示 → 最后 CTA"
  ```

**场景 5：动画图表/数据叙事**
- **操作示例**："用 remotion 做一个数据叙事动画：公司从创立到现在的里程碑时间线，每个节点有图标+年份+描述，用平滑缩放过渡"
- **特点**：remotion 的 React 生态可以复用现有图表库（如 d3.js, recharts）


**Vibe Coding 场景**

**场景 6：AI 产品宣传片**
- **操作示例**："用 remotion 做 30 秒 AI 产品宣传片：开场粒子效果拼出产品名，3 个核心功能截图嵌入，每截图旁动态标注箭头，背景渐变粒子，结尾倒计时后出现 CTA。全程用 spring 物理缓动"
- **特点**：remotion 的 React 生态可直接用 framer-motion / react-spring，实现超流畅动画

**场景 7：交互式作品集 Demo**
- **操作示例**："用 remotion 做个人作品集展示视频：5 个项目卡片依次出现，含截图、技术栈标签、描述。卡片用 3D 翻转进场的 rotateY 动画，底部进度条显示当前位置"
- **技巧**：remotion 除了输出视频，也支持输出交互式 HTML 版本

**场景 8：音乐可视化**
- **操作示例**："帮我做音乐可视化视频：输入音频，基于频谱实时生成动态波形图，波形颜色从 #FF6B6B 渐变到 #4ECDC4，背景深色粒子系统随节拍跳动，时长与音频同步"
- **工作流**：Codex 用 Web Audio API 分析音频，remotion 逐帧渲染

**场景 9：GIF 动效生成器**
- **操作示例**："用 remotion 生成 3 个 loading 动画 GIF：1. 旋转环形进度条 2. 弹跳的三个点 3. 渐变色流动背景，每个 2 秒循环播放，透明背景"
- **用途**：直接用于 Web 项目/App 启动页/微交互演示

**场景 10：代码到视频——从 GitHub 仓库生成项目演示**
- **操作示例**："接入这个 GitHub 仓库（贴 URL），自动生成 1 分钟项目演示视频：展示架构图、文件结构树、运行截图、核心代码高亮、Star 数量动效"
- **原理**：Codex 先 clone 仓库并分析，再用 remotion 渲染为视频——自动化的 repo→demo video 管线

**场景 11：动态时间线视频**
- **操作示例**："做一个项目里程碑时间线：2024 Q1 立项→Q2 原型→Q3 内测→Q4 上线，每个节点圆点标记，连线流动虚线动画，背景根据时间进度颜色渐变"
- **应用**：融资 Pitch Deck / 年终总结 / 产品发布

**场景 12：短视频批量工厂**
- **操作示例**："帮我准备一个 5 条短视频的批量脚本模板。主题：AI 科普，每条 20 秒，含标题卡、2-3 个要点图标动画、底部字幕，输出全部 5 条。第一条主题：什么是大语言模型"
- **效率**：用 remotion React 组件的 Props 机制，一套模板+不同数据=批量出片**最佳实践**
1. **分步迭代**：先让 Codex 生成基础骨架视频，预览后逐步加细节（"给标题加个渐入效果"、"过渡改成淡出"）
2. **⚠️ 额度提示**：remotion 渲染逐帧合成，较长视频消耗额度较大。先做短版本（15-30 秒）测试效果
3. **复用组件**：做好的 React 组件可以让 Codex 保存为可复用模板
4. **与 hyperframes 配合**：简单动效用 hyperframes（快），复杂合成用 remotion（强）
5. **数据可视化**：remotion + visualize 插件 = 数据动画的黄金组合
6. **导出格式**：默认输出 MP4，可以让 Codex 调整编码参数（码率、帧率、分辨率）

### 学术与设计

**zotero**
- **中文说明**：连接本地 Zotero 文献管理——搜索/导出 BibTeX/插入引用。
- **使用示例**："找到关于 Agent 的最新论文"
- **来源**：openai-api-curated · v0.1.2

**latex**
- **中文说明**：LaTeX 编译（Tectonic / TeX Live）。
- **使用示例**："编译这篇 LaTeX 论文"
- **来源**：openai-bundled · v0.2.4

**figma**
- **中文说明**：Figma 设计稿转代码，Code Connect 模板，设计系统规则。
- **使用示例**："把 Figma 设计稿转成 React 代码"
- **来源**：openai-api-curated

### 已安装未启用

**template-creator**
- **中文说明**：从现有文件创建可复用模板，保留布局样式。
- **使用示例**："把这个报告存成模板"
- **来源**：openai-primary-runtime · v26.715.12143

---

## 可安装插件（180 个）

### 开发工具与 DevOps

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **build-ios-apps** | iOS 应用开发——App Intents/SwiftUI/Simulator | "创建一个新的 iOS 应用" |
| **build-macos-apps** | macOS 应用开发——Xcode/SwiftUI/AppKit | "开发一个 macOS 菜单栏工具" |
| **build-web-apps** | Web 应用开发——React/Tailwind/支付/数据库 | "创建一个 React + Tailwind 项目" |
| **build-web-data-visualization** | 交互式数据可视化——图表/地图/仪表盘 | "把数据做成交互式图表" |
| **test-android-apps** | Android 测试——模拟器/截图/UI/日志 | "在模拟器中测试 App" |
| **circleci** | CI/CD 构建/测试/部署 | "看看最新构建状态" |
| **coderabbit** | AI 驱动的代码审查 | "审查 PR 的代码质量" |
| **codex-security** | 安全扫描/分析/调查工作流 | "扫描项目的安全漏洞" |
| **convex** | 响应式后端——数据库/函数/类型安全 | "创建一个 Convex 数据表" |
| **digitalocean** | 创建远程工作空间（DO 服务器） | "创建一个新的 DO 服务器" |
| **expo** | Expo/React Native 应用构建部署 | "创建一个新的 Expo 项目" |
| **hostinger** | Hostinger Horizons——描述需求自动建站 | "创建一个个人网站" |
| **lovable** | 描述需求自动创建全栈 Web 应用 | "创建一个 SaaS 登录页面" |
| **neon-postgres** | Neon Serverless Postgres 项目管理 | "创建一个新的 Postgres 数据库" |
| **netlify** | Netlify 部署——预览和生产管理 | "把网站部署到 Netlify" |
| **openai-developers** | OpenAI API/Agents SDK/ChatGPT Apps 开发 | "创建一个 OpenAI 调用脚本" |
| **quicknode** | QuickNode 区块链基础设施 | "查一下节点运行状态" |
| **render** | Render 部署/调试/监控/迁移 | "把应用部署到 Render" |
| **replit** | Replit Web 应用创建和迭代 | "在 Replit 中创建 Web 应用" |
| **supabase** | Supabase——表管理/配置/数据查询 | "查一下用户表的最新数据" |
| **temporal** | Temporal 全生命周期——开发/CLI/管理 | "排查 Workflow 执行失败原因" |
| **twilio-developer-kit** | Twilio API——短信/语音/验证开发 | "写一个 Twilio 短信发送函数" |
| **vercel** | Vercel 部署——Web 应用和 Agent | "把项目部署到 Vercel" |
| **cloudflare** | Cloudflare——Workers/Wrangler/API | "部署一个 Cloudflare Worker" |
| **fal** | Fal 模型——媒体生成和管理 | "用 fal 生成一张产品图" |
| **binance** | 币安公开市场数据查询（只读） | "查一下 BTC 当前价格" |
| **cloudinary** | 媒体库管理——搜索/转换/上传 | "优化图片并上传到 Cloudinary" |
| **brand24** | 品牌舆情监控——提及/情感/媒体类型 | "查一下品牌最近的社交媒体提及" |
| **plugin-eval** | 插件和 Skill 评估——本地报告/预算 | "评估一下这个 Skill 的质量" |
| **replayio** | Replay 浏览器录制——调试用 | "录制 Bug 的复现过程" |
| **yepcode** | 用 JSON Schema 构建自定义 AI 工具 | "创建一个自动发日报的 AI 工具" |
| **jam** | 屏幕录制——附带上下文 | "录一个 Bug 复现过程" |
| **nvidia** | NVIDIA 生态——GPU/CUDA/AI/机器人 | "优化 CUDA 程序性能" |
| **hugging-face** | Hugging Face 模型/数据集/Spaces | "查一下最新的开源 LLM" |
| **base44** | Base44 全栈应用开发 CLI | "创建一个 Base44 新项目" |

### CRM 与销售

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **apollo** | 客户勘探与外呼自动化 | "找一下 SaaS 行业的潜在客户" |
| **attio** | 直接连接你的 CRM 工作空间 | "更新这个客户的联系方式" |
| **close** | Close CRM 查询和更新 | "查一下客户的销售进度" |
| **hubspot** | HubSpot CRM 数据分析/记录管理 | "查一下客户在 HubSpot 的信息" |
| **zoho** | Zoho CRM 销售工作流管理 | "查一下 Zoho 中的客户信息" |
| **pipedrive** | Pipedrive 交易和联系人同步 | "查销售管道中当前的交易" |
| **streak** | Streak CRM（内嵌 Gmail） | "查一下客户的 Streak 管道进度" |
| **zoominfo** | 客户勘探和账户研究 | "查一下这家公司的最新联系人" |
| **outreach** | Outreach 营收工作流自动化 | "查一下客户的 outreach 沟通记录" |
| **clay** | 客户发现和 Engagement | "找符合画像的潜在客户" |
| **carta-crm** | 投资 CRM——交易流/公司/关系管理 | "查一下投资项目的进展" |
| **common-room** | 买家智能数据嵌入 | "查一下潜在客户的详细资料" |
| **hg-insights** | 潜在客户数据和营收智能 | "查一下潜在客户的背景信息" |
| **meticulate** | 公司研究和同类对标 | "分析这家公司和竞品" |
| **dnb-finance-analytics** | 商业信用授信和风控 | "查一下公司的信用评级" |
| **actively** | GTM 智能记账客户管理 | "查一下客户 actively 的最近活动" |

### 项目管理

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **asana** | 任务/子任务/评论/截止日期管理 | "查一下今天的 Asana 待办" |
| **atlassian-rovo** | Jira + Confluence 快速管理 | "查一下 Sprint 的进度" |
| **clickup** | ClickUp 项目管理中心 | "查一下我的 ClickUp 任务列表" |
| **linear** | 问题和项目管理 | "查一下这个 Sprint 的进度" |
| **monday-com** | monday.com 项目管理连接器 | "查一下项目任务进度" |
| **notion** | 规划/研究/会议/知识沉淀 | "把笔记整理到 Notion 中" |
| **teamwork-com** | Teamwork 项目和任务同步 | "查一下我的 Teamwork 任务" |

### 数据分析与 BI

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **airtable** | 数据库式电子表格平台 | "查 Airtable 项目表的数据" |
| **amplitude** | 产品分析和用户行为漏斗 | "分析用户注册流程的转化" |
| **cube** | 数据查询——预算/预测/差异/趋势 | "查 Q3 的预算执行情况" |
| **daloopa** | 金融分析——机构级数据 | "分析这家公司的财务指标" |
| **deepnote** | 协作数据工作空间 | "运行这个数据分析" |
| **hex** | Hex 项目搜索和 Thread 问答 | "查 Hex 中的数据分析项目" |
| **mixpanel** | Mixpanel 数据查询和分析 | "分析用户留存率变化" |
| **mixpanel-headless** | Python SDK 分析（headless 模式） | "批量分析用户行为数据" |
| **motherduck** | MotherDuck 数据仓库连接 | "在 MotherDuck 中查询销售数据" |
| **omni-analytics** | Omni 数据查询——保留权限 | "查上季度的销售额趋势" |
| **posthog** | 产品数据分析和 A/B 实验 | "分析 A/B 测试的结果" |
| **statsig** | Statsig 实验分析工作空间 | "查 Feature Flag 的状态" |
| **thoughtspot** | ThoughtSpot 业务数据问答 | "查上季度的销售数据" |
| **conductor** | SEO 性能指标——可见度/流量 | "分析网站 SEO 表现" |
| **semrush** | SEO/流量/关键词/反向链接 | "分析网站关键词排名" |
| **similarweb** | 网站和 App 流量情报 | "分析竞品流量来源" |
| **channel99** | 实时 GTM 营销智能 | "分析上周营销渠道 ROI" |
| **vantage** | 云成本观测和优化 | "分析上月云服务支出" |
| **datadog** | Datadog 遥测调查和工作流 | "查错误率趋势" |
| **sentry** | Sentry issue 和事件检查 | "查生产环境最新错误" |
| **rox** | Rox 销售工作空间数据分析 | "分析销售团队本月业绩" |
| **coupler-io** | 多维度业务数据分析 | "分析上月营销 ROI" |

### 金融与支付

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **aiera** | 机构金融数据与事件跟踪 | "查公司最新财报事件" |
| **alpaca** | 自动化股票/加密货币交易 | "查 AAPL 实时股价" |
| **brex** | 企业财务管理 | "查公司本月支出" |
| **fiscal-ai** | 审计级财务数据和股权研究 | "分析公司财务报表" |
| **lseg** | 金融市场数据和分析 | "查 FTSE 100 当前行情" |
| **moody-s** | 穆迪信用评级/实体情报 | "查公司的穆迪信用评级" |
| **morningstar** | 晨星基金筛选/总结/比较 | "比较两只基金的表现" |
| **quartr** | 上市公司 IR 数据和财报 | "查特斯拉最新财报数据" |
| **s-p** | 标普全球金融数据集 | "查这个行业的标普评级" |
| **stripe** | Stripe 支付和业务工具 | "查上周的 Stripe 收入" |
| **quickbooks** | QuickBooks 财务分析 | "查本月现金流" |
| **razorpay** | Razorpay 支付数据查询 | "查上周交易流水" |
| **cb-insights** | 一级市场研究——融资/趋势 | "查 AI Agent 赛道融资事件" |
| **pitchbook** | 一级市场数据——公司/投资者/基金 | "查 startup 的最新融资" |
| **factset** | 金融数据/分析/工作流 | "查股票历史 PE 数据" |
| **dow-jones-factiva** | Factiva 全球新闻档案 | "搜 AI Agent 行业报道" |
| **mt-newswires** | 实时全球金融新闻 | "查今天科技板块的重大新闻" |
| **third-bridge** | 行业专家洞察融入金融研究 | "查赛道的最新专家观点" |
| **chronograph-gp** | 私募 GP——投资组合监控/估值 | "查投资组合最新估值" |
| **chronograph-lp** | 私募 LP——投资组合监控分析 | "分析基金回报率" |
| **hebbia** | 机构研究和金融工作流 | "分析研究报告关键发现" |
| **tinman-ai** | 住房贷款审批——自动化承保 | "评估贷款申请风险" |
| **setu-bharat-connect-billpay** | 印度公共事业缴费 | "交这个月的电费" |
| **taxdown** | 西班牙税务咨询 | "算今年要交多少税" |

### 沟通与协作

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **gmail** | Gmail 邮件操作 | "查上周未回复的邮件" |
| **google-calendar** | Google 日历——日程/可用性 | "看看今天有哪些会议" |
| **outlook-email** | Outlook 邮件操作 | "查收件箱里标记重要的邮件" |
| **outlook-calendar** | Outlook 日历——日程/日报 | "看看明天会议安排" |
| **slack** | Slack 消息和工作流 | "给 xx 频道发一条消息" |
| **teams** | Microsoft Teams 频道和消息 | "在 Teams 上给团队发消息" |
| **zoom** | Zoom 会议 + Zoom App 开发 | "创建一个 Zoom 会议" |
| **fyxer** | AI 代写邮件——像你的语气 | "用我的风格回复邮件" |
| **sendgrid** | SendGrid 邮件 API | "发送一封通知邮件" |
| **superhuman** | Superhuman 邮件和日历 | "帮我发一封邮件" |
| **intercom** | 客户对话/工单/知识库 | "查客户对最近更新的反馈" |
| **help-scout** | 客服邮箱和对话同步 | "查未回复的客服工单" |
| **pylon** | 客户支持平台操作 | "查未解决的客户工单" |
| **dovetail** | 客户反馈分析 | "分析用户对功能的反馈" |
| **circleback** | AI 会议纪要/行动项/录音 | "总结昨天会议要点" |
| **fireflies** | 会议智能——转录/搜索/摘要 | "总结产品评审会议" |
| **otter-ai** | 会议转录和搜索 | "查上周产品会议转录" |
| **read-ai** | Read AI 会议智能 | "总结昨天所有会议" |
| **granola** | 会议历史连接 | "回顾上周客户会议决策" |
| **happenstance** | 职业人脉搜索 | "找一个 AI Agent 产品经理" |
| **marcopolo** | 安全容器处理实际数据 | "在安全环境分析敏感数据" |

### 文件存储与知识管理

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **box** | Box 云端文档搜索查阅 | "查 Box 里上周的合同" |
| **egnyte** | Egnyte 文档和文件操作 | "查 Egnyte 共享的项目文件" |
| **glean** | 企业知识库远程 MCP | "查公司知识库里的项目文档" |
| **google-drive** | Drive/文档/表格/幻灯片 | "查 Drive 里昨天共享的文档" |
| **mem** | Mem 知识库上下文获取 | "查我关于这个项目的笔记" |
| **sharepoint** | SharePoint 文件操作 | "查 SharePoint 中的项目文档" |
| **readwise** | Readwise/Reader 标注 | "查我在 Readwise 中的标注" |
| **coveo** | 企业内容搜索 | "搜公司知识库的资料" |
| **alation** | 企业数据目录和治理 | "查数据集的数据字典" |
| **docket** | 销售知识即时获取 | "查客户过往沟通记录" |

### 设计、内容与创意

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **canva** | Canva 设计搜索/创建/编辑 | "创建一个社交媒体海报" |
| **shutterstock** | Shutterstock 图库搜索 | "找一张商务风格配图" |
| **picsart** | 生成视频/图片/音频 | "生成一张社交媒体配图" |
| **heygen** | HeyGen 数字人视频创建 | "创建数字人产品介绍视频" |
| **magicpath** | UI 组件查找/安装/创建/编辑 | "找一个现成登录表单组件" |
| **wix** | Wix 网站/Headless 开发 | "在 Wix 上创建网站页面" |
| **shopify** | Shopify 开发——GraphQL/Liquid | "查一下商店的订单" |
| **myregistry-com** | 礼物清单管理 | "看看我的礼物清单" |
| **weatherpromise** | 天气保障——下雨可获赔付 | "查出行日期的天气保障" |
| **finn** | 汽车订阅服务 | "查可用的车型" |
| **waldo** | AI 策略平台 | "分析品牌社交媒体策略" |
| **responsive** | 组织数据接入 Codex | "查客户反馈数据" |
| **highlevel** | CRM/自动化/客户沟通统一平台 | "查客户沟通记录" |
| **windsor-ai** | 营销/业务数据源自然语言问答 | "分析上周广告渠道 ROI" |

### 研究与学术

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **biorender** | 科研绘图——科学示意图 | "画一个细胞结构示意图" |
| **life-science-research** | 生命科学研究——证据综合 | "查基因与疾病相关性文献" |
| **ngs-analysis** | 基因测序分析完整管线 | "分析这个 FASTQ 样本" |
| **scite** | 基于同行评审研究的答案 | "查关于这个课题的最新研究" |
| **boltz-api-cli** | 结构预测/分子筛选/蛋白质设计 | "预测这个蛋白质的结构" |

### 法律与合规

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **docusign** | 合同创建和签署自动化 | "创建一份电子签名合同" |
| **signnow** | 电子签名快速签合同 | "创建一份需要签名的合同" |
| **midpage** | 法律研究——判例法引用 | "查法律问题的相关判例" |
| **policynote** | 全球政策和监管情报 | "查 AI 监管最新政策动向" |
| **govtribe** | 政府合同/奖项/供应商搜索 | "查政府招标信息" |

### 电商与建站

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **network-solutions** | 域名搜索——找可用域名 | "找一个可用的 .com 域名" |
| **united-rentals** | 设备租赁——找工业设备 | "找合适的建筑设备" |
| **cogedim** | 法国头部房地产开发商 | — |
| **keybid-puls** | 短租投资 ROI 计算器 | "算短租投资回报率" |
| **domotz-preview** | 网络基础设施监控 | "检查网络设备状态" |
| **skywatch** | 卫星图像搜索 | "查区域最新卫星图" |

### 日历与日程

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **calendly** | 预约链接/可用性/排程管理 | "查下周可用的预约时间" |

### 招聘与人才

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **brighthire** | 面试智能数据连接 | "回顾候选人的面试记录" |

### OpenAI 官方

| 插件 | 中文说明 | 使用示例 |
|------|---------|---------|
| **openai-ads-conversions** | OpenAI 广告转化测量配置 | "设置广告转化跟踪" |

---

## 参考

- [[Codex-使用指南]] — Codex 整体指南




