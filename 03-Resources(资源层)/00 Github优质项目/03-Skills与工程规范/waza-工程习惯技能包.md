---
title: "Waza 工程习惯技能包"
tags: [GitHub, 开源, AI, Skills, 工程, 习惯, tw93]
type: 工具
status: 待评估
created: 2026-07-06
updated: 2026-07-16
source: https://github.com/tw93/Waza
related: [[mattpocock-skills-工程师日常技能], [agent-skills-生产级工程技能包], [anthropics-skills-官方Skills仓库]]
summary: "tw93 出品的 8 个工程习惯技能——Think/UI/Check/Hunt/Write/Learn/Read/Health，每个技能对应一个工程好习惯，小而精，可链式组合"
---

# Waza 工程习惯技能包

https://github.com/tw93/Waza

## 基本信息

**类型：** 工具（Skill 集合）
**链接：** https://github.com/tw93/Waza
**安装：** `npx skills add tw93/Waza -a claude-code codex cursor -g -y`
**适用领域：** AI Agent 工程习惯训练、软件开发全流程
**推荐程度：** ★★★★★
**Stars：** 未统计
**语言：** Markdown
**许可证：** MIT

## 是什么

**Waza（技/わざ）**——日本武术术语，意为「练成本能的技巧」。tw93 出品的 8 个工程习惯技能包，每个技能对应一个优秀工程师的日常习惯。设计哲学：**小、精、可链式组合**——每个技能只做一件事，但做到极致。

## 8 个技能

| 技能 | 触发 | 何时用 | 做什么 |
|------|------|--------|--------|
| `/think` | 构建任何新东西之前 | 挑战问题、压力测试设计、产出决策完备的计划 |
| `/ui` | 构建前端界面 | 产出有方向感的 UI，截图驱动审美迭代 |
| `/check` | 任务完成后、合并前 | 审查 diff、提取项目约束、处理发布/推送/验证 |
| `/hunt` | 任何 Bug/回归/异常行为 | 系统化调试，确认根因后再修复 |
| `/write` | 写作或编辑散文 | 重写散文使其自然（中英文），去掉生硬公式化表达 |
| `/learn` | 进入陌生领域 | 六阶段研究：收集→消化→大纲→填充→润色→发布 |
| `/read` | 任何 URL 或 PDF | 按平台路由读取，摘要或 Markdown 输出 |
| `/health` | 审计 Agent 健康度 | 检查 Codex/Claude Code/项目指令/Verifier/AI 可维护性 |

## 链式工作流

技能可以手动链式组合：

- **规划功能**：`/think` → 批准 → "实现 X" → `/check` → 合并
- **修复 Bug**：`/hunt` → 修复 → `/check` → 发布
- **研究与写作**：`/read`（获取源）→ `/learn`（综合）→ `/write`（润色）
- **调试与验证**：`/hunt`（找根因）→ 修复 → `/check`（审查变更）

## 安装

```bash
# 一键安装全部 8 个技能
npx skills add tw93/Waza -a claude-code codex cursor -g -y

# 原生插件
/plugin marketplace add tw93/Waza
/plugin install waza@waza

# Claude Desktop：下载 waza.zip 上传
```

## 设计理念

- **Process, not prose** — 可执行工作流，不是参考文档
- **Restraint** — 每个技能只设目标和约束，让模型自由发挥。模型越强，这种克制越有价值
- **Real gotchas** — 每个坑都来自真实项目的失败经验（300+ 会话，7 个项目）
- **Composable** — 技能可链式组合，但每个过渡是手动步骤

## 三件套

Waza 是三部曲之一：
- [[Kaku]]（書く）— 写代码
- **Waza**（技）— 练习惯
- Kami（紙）— 出文档

## 评价

- **优点**：8 个技能少而精、设计哲学成熟（克制/可组合）、来自真实项目经验、中英文支持、MIT 开源
- **局限**：技能数量少（覆盖核心习惯但不够全）、依赖 npx skills 生态
- **是否值得长期保留**：✅ 重点关注——工程习惯技能的最佳实践
