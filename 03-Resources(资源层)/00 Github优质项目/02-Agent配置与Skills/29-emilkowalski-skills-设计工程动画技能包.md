---
title: "emilkowalski/skills 设计工程动画技能包"
domain: Core_Ability
tags: [GitHub, 开源, Agent-Skills, 设计工程, 动画]
status: 稳定
created: 2026-08-02
updated: 2026-08-02
verified: 2026-08-02
review_after: 2026-11-02
source: "https://github.com/emilkowalski/skills"
related: ["[[mattpocock-skills-工程师日常技能]]", "[[agent-skills-生产级工程技能包]]", "[[Skills场景化使用指南]]"]
summary: "emilkowalski/skills 由前 Vercel/Linear 设计师 Emil Kowalski 出品，提供 8 个设计工程技能，帮助 AI 编码助手在 UI 动画、交互设计、原型制作方面做出专业级决策，弥补 AI 缺乏设计品味的短板。"
---

# emilkowalski/skills 设计工程动画技能包

> [!abstract] 一句话定位
> 一套面向**设计工程师（Design Engineer）**的 Agent Skills，将专业动画决策、UI 设计原则和原型制作能力注入 AI 编码助手，解决"AI 没有设计品味"的问题。

## 基本信息

| 项目 | 内容 |
|---|---|
| 仓库 | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| 作者 | [Emil Kowalski](https://emilkowal.ski)（前 Vercel / Linear 设计师） |
| 许可证 | MIT |
| 适用平台 | 支持 Agent Skills 标准的工具：Claude Code、Codex、Gemini CLI、GitHub Copilot、OpenClaw 等 |
| 安装命令 | `npx skills@latest add emilkowalski/skills` |
| 核心理念 | AI 没有品味，但这些技能让 AI 做出专业级的设计决策 |

## 背景

Emil Kowalski 是知名的 UI 动效专家，在 Vercel 和 Linear 期间积累了丰富的设计工程经验。他在博客文章 [Agents with Taste](https://emilkowal.ski/ui/agents-with-taste) 中提出：AI 编码助手擅长生成代码，但缺乏对设计细节的判断力——例如用 `ease-in` 做入场动画（应该用 `ease-out`），或者用实线边框代替半透明阴影。这些技能正是用来弥补这一差距的。

## 技能清单

| 技能 | 说明 | 典型用途 |
|------|------|---------|
| **emil-design-eng** | 主技能，包含动画和设计建议 | 通用设计工程咨询 |
| **review-animations** | 基于规则严格审查你的动画 | 代码审查发现动画问题 |
| **improve-animations** | 审计整个代码库中的动画，给出优先级排序的自包含执行计划 | 批量优化动画质量 |
| **find-animation-opportunities** | 在 UI 中查找值得加动画的位置，同时告知哪些地方**不该**加 | 动画体验规划 |
| **animation-vocabulary** | 反查术语表：将模糊的动效描述映射到精确术语（如"弹窗打开时的弹跳效果"→ Pop in） | 更精准地描述需求 |
| **apple-design** | 苹果 WWDC 设计原则提炼，适配 Web 实现 | 构建 Apple 风格界面 |
| **pick-ui-library** | 基于 Emil 信任的 UI 库列表，让 AI 选正确的库而非手写或安装过时包 | 技术选型 |
| **prototype** | 根据描述构建多个 UI 版本，用切换器浏览对比 | 快速原型比对 |

## 工作原理

这些技能的核心是**领域专家知识的外部化**：

- 将 Emil 多年积累的动画决策规则（缓动选择、持续时间、层级关系、手势交互）编码为结构化的 AI 提示
- 当 AI 处理设计工程任务时，自动加载对应技能，约束其输出符合专业标准
- 安全扫描（GenAI / Socket / Snyk）均为低风险，可直接使用

## 安装方法

```bash
npx skills@latest add emilkowalski/skills
```

安装后，8 个技能会自动链接到 Claude Code、Codex 等工具。

## 使用示例

- **审查动画**：调用 `review-animations` 技能，自动检查当前项目的动画是否符合专业标准
- **选 UI 库**：用 `pick-ui-library` 技能让 AI 推荐合适的 UI 组件库
- **原型设计**：用 `prototype` 技能快速生成多个 UI 版本进行对比

## 关联资源

- [[mattpocock-skills-工程师日常技能]] — 另一套面向软件工程的技能包，互补使用
- [[agent-skills-生产级工程技能包]] — 全面的工程技能集合
- [Emil Kowalski 博客](https://emilkowal.ski/ui/) — 设计工程文章