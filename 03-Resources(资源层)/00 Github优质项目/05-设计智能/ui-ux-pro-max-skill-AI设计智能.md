---
title: "UI UX Pro Max AI设计智能技能"
tags: [GitHub, 开源, AI, Design, UI, UX, Skill, Tailwind, 前端]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
related: [[agent-skills-生产级工程技能包]]
summary: "AI 设计智能 Skill——161 条推理规则+67 种UI风格+95 个配色方案，内置设计系统生成器，让 Agent 产出专业级 UI/UX，82.9k Stars"
---

# UI UX Pro Max AI设计智能技能

https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## 基本信息

**类型：** 工具（AI Skill）
**链接：** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
**主页：** https://www.uupm.cc/
**NPM：** uipro-cli
**适用领域：** AI 辅助 UI/UX 设计、前端开发、设计系统生成
**推荐程度：** ★★★★☆
**Stars：** ~82.9k | Fork 8.5k
**设计资产：** 161 推理规则 · 67 UI 风格 · 95 配色 · 52 字体搭配 · 67 图表 · 27 UX 指南
**许可证：** MIT

## 是什么

UI UX Pro Max 是一个**为 AI Agent 注入设计智能的 Skill**。核心理念：AI 编程 Agent 代码能力很强，但 UI 审美通常很差——这个 Skill 给 Agent 提供专业的设计知识库（配色/排版/布局/UX 最佳实践），让 Agent 产出的界面从「能用」变成「好看」。

内置 **设计系统生成器**：输入项目需求（如「高端 SPA」），AI 自动推理出完整的配色方案、字体搭配、布局模式、CTA 策略。

## 快速开始

```bash
# CLI 安装（自动配置 Claude Code / Cursor / Codex 等）
npm install -g uipro-cli
uipro init --ai claude      # 或 --ai codex / --ai cursor

# 设计系统生成
python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
  "beauty spa wellness" --design-system -p "Serenity Spa"
```

## 核心功能

### 设计知识库

| 类别 | 数量 | 说明 |
|------|------|------|
| 推理规则 | 161 | 设计决策推理链（何时用卡片、何时用列表等） |
| UI 风格 | 67 | Soft UI Evolution、Glassmorphism、Brutalism 等 |
| 配色方案 | 95 | 含主色/辅色/CTA/背景/文字全套 |
| 字体搭配 | 52 | 标题+正文字体配对 |
| 图表建议 | 67 | 数据可视化图表选型 |
| UX 指南 | 27 | 可访问性、响应式、交互模式等 |

### 设计系统生成器（v2.0 旗舰功能）

输入 `"beauty spa wellness"` → AI 自动输出：
```
PATTERN:  Hero-Centric + Social Proof（转化驱动+信任元素）
STYLE:   Soft UI Evolution（柔阴影、微妙深度、高级感）
COLORS:  Primary #E8B4B8 / Secondary #A8D5BA / CTA #D4AF37
TYPO:    Playfair Display + Lato（优雅衬线+清晰无衬线）
SECTIONS: Hero → Services → Testimonials → Booking → Contact
```

### Master + Overrides 设计系统持久化

```bash
# 生成并持久化设计系统
python3 scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"
```

生成文件结构：
```
design-system/
├── MASTER.md           # 全局设计系统（颜色/字体/间距/组件）
└── pages/
    └── dashboard.md    # 页面级覆盖（仅记录与 Master 的差异）
```

### 支持 12+ 技术栈

HTML+Tailwind · React · Next.js · shadcn/ui · Vue · Nuxt · Angular · Laravel · Svelte · Astro · SwiftUI · Jetpack Compose · React Native · Flutter

## 适用场景

- 让 AI Agent 产出的 UI 从「能用」升级到「专业好看」
- 快速生成项目设计系统——配色/字体/布局一站式
- 前端开发时让 Agent 自动遵循 UX 最佳实践（可访问性 WCAG、响应式、反模式检查）
- 与 agent-skills 互补：agent-skills 管代码质量流程，UI UX Pro Max 管视觉设计质量

## 评价

- **优点**：161 推理规则库庞大专业、设计系统生成器实用、Master+Overrides 模式适合多页面项目、12+ 技术栈覆盖广、82.9k Stars 证明前端开发者对 AI 设计质量的强烈需求、MIT 开源
- **局限**：专注 UI/UX 设计领域（非通用 Agent 工具）、AI 产出的设计仍需人工审美判断、「设计好≠代码好」需要配合 agent-skills 等工程质量工具
- **是否值得长期保留**：✅ 关注——AI Agent 设计智能的标杆项目，UI/UX 知识库的结构化方式可参考用于其他领域知识注入
