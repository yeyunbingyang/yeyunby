---
title: "MyClaude 多智能体工作流系统"
tags: [GitHub, 开源, AI, Claude, 多智能体, 工作流, 编排]
type: 工具
status: 待评估
created: 2026-07-06
updated: 2026-07-16
source: https://github.com/stellarlinkco/myclaude
related: [[agent-skills-生产级工程技能包], [superpowers-Agent开发方法论]]
summary: "Claude Code 多智能体工作流系统——5 阶段 do 工作流/OmO 智能路由/SPARV/BMAD 敏捷/11 开发命令，多后端执行（Codex/Claude/Gemini/OpenCode）"
---

# MyClaude 多智能体工作流系统

https://github.com/stellarlinkco/myclaude

## 基本信息

**类型：** 工具（多智能体工作流系统）
**链接：** https://github.com/stellarlinkco/myclaude
**安装：** `npx github:stellarlinkco/myclaude`
**适用领域：** AI 驱动开发自动化、多智能体编排
**推荐程度：** ★★★★☆
**Stars：** 未统计
**语言：** Shell + Markdown
**许可证：** AGPL-3.0

## 是什么

**Claude Code 多智能体工作流系统**——多后端执行架构（Codex/Claude/Gemini/OpenCode）。核心架构：Claude Code 作为编排者（规划/上下文收集/验证），codeagent-wrapper 作为执行者（代码编辑/测试执行）。

## 模块概览

| 模块 | 描述 |
|------|------|
| **do**（推荐） | 5 阶段功能开发 + codeagent 编排 |
| **OmO** | 多智能体编排 + 智能路由 |
| **BMAD** | 敏捷工作流 + 6 个专业智能体 |
| **requirements** | 轻量级需求到代码流水线 |
| **essentials** | 11 个核心开发命令 |
| **SPARV** | Specify→Plan→Act→Review→Vault 工作流 |

### do 工作流（推荐）

5 阶段功能开发：
1. **Understand** — 并行探索理解需求和代码库
2. **Clarify** — 解决阻塞性歧义（条件触发）
3. **Design** — 产出最小变更方案
4. **Implement + Review** — 构建并审查
5. **Complete** — 记录构建结果

### OmO 多智能体编排

基于风险信号智能路由任务：
- `oracle`（技术顾问）→ Claude
- `librarian`（外部研究）→ Claude
- `explore`（代码库搜索）→ OpenCode
- `develop`（代码实现）→ Codex
- `frontend-ui-ux-engineer` → Gemini
- `document-writer` → Gemini

### SPARV 工作流

极简 5 阶段：Specify → Plan → Act → Review → Vault
- **10 分规格门**：得分 >=9 才能进入 Plan
- **2 动作保存**：每 2 次工具调用写入 journal.md
- **3 失败协议**：连续 3 次失败后停止并上报

### 11 开发基础命令

`/code` `/debug` `/test` `/review` `/optimize` `/refactor` `/docs` `/ask` `/bugfix` `/enhance-prompt` `/think`

## 评价

- **优点**：多后端架构灵活、工作流设计完整（do/OmO/SPARV/BMAD 四种模式）、中文文档完善
- **局限**：AGPL-3.0 许可证限制商用、依赖 Claude Code 生态、配置复杂度较高
- **是否值得长期保留**：✅ 关注——多智能体编排的实用参考
