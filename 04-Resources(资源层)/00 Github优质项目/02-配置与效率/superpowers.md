---
title: "Superpowers Agent 技能框架"
tags: [GitHub, 开源, AI, Agent, Skills, 开发方法论]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/obra/superpowers
related: [[agent-skills], [mattpocock-skills]]
summary: "207k Stars 的 Agent 软件开发方法论——可组合 Skills + 子代理驱动开发，自动从Spec→Plan→Build→Review全流程"
---

# Superpowers Agent 技能框架

https://github.com/obra/superpowers

## 基本信息

**类型：** 工具（Skill 集合 + 方法论）
**链接：** https://github.com/obra/superpowers
**适用领域：** AI Agent 软件开发全流程、子代理编排
**推荐程度：** ★★★★★
**Stars：** ~207.5k | Fork 12k+
**语言：** Shell
**许可证：** MIT

## 是什么

Superpowers 是一套完整的 **Agent 软件开发方法论**。从 Agent 启动那一刻开始，它不会直接跳进写代码——而是先退一步问清楚你想做什么，提取 Spec，展示给你确认，制定实施计划，然后通过**子代理驱动开发**（subagent-driven-development）逐任务执行，自动审查和推进。Agent 可自主工作数小时不偏离计划。

支持 Claude Code / Codex CLI/App / Gemini CLI / OpenCode / Cursor / Copilot CLI / Factory Droid。

## 核心流程

Spec 对话确认 → 分块展示 → 用户签收 → 实施计划（TDD+YAGNI+DRY） → 子代理逐任务执行 → 自动审查 → 持续前进

## 适用场景

- 多步骤复杂功能开发——Agent 自主执行 2+ 小时不偏离
- 需要严格 TDD 流程的团队
- 与 agent-skills 互补：agent-skills 管单步骤质量，Superpowers 管全流程编排

## 评价

- **优点**：子代理驱动开发是 Agent 自主编程的成熟范式、安装即用无需配置、支持 7 个主流 Agent 平台
- **是否值得长期保留**：✅ 重点关注
