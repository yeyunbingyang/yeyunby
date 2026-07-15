---
title: "Agent Skills 生产级工程技能包"
tags: [GitHub, 开源, AI, Agent, Skills, 工程规范, Google]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-07-16
source: https://github.com/addyosmani/agent-skills
related: [[ECC-Agent全套配置系统], [knowledge-work-plugins-知识工作角色插件]]
summary: "Addy Osmani（Google）出品的 23 个生产级 Agent 工程技能，覆盖 spec→plan→build→test→review→ship 全生命周期，融入 Google 工程文化，45.9k Stars"
---

# Agent Skills 生产级工程技能包

https://github.com/addyosmani/agent-skills

## 基本信息

**类型：** 工具（Skill 集合 + Commands）
**链接：** https://github.com/addyosmani/agent-skills
**适用领域：** AI Agent 工程规范、软件开发生命周期、代码质量保障
**推荐程度：** ★★★★★
**Stars：** ~45.9k | Fork 5.1k
**许可证：** MIT
**作者：** Addy Osmani（Google 工程 leader，《Software Engineering at Google》作者）

## 是什么

Addy Osmani 出品的 **23 个生产级 Agent 工程技能**——把高级工程师在软件开发的每个阶段遵循的工作流、质量门禁和最佳实践，编码为 AI Agent 可执行的标准化流程。

核心理念：AI Agent 默认走最短路径——跳过规格、跳过测试、跳过安全审查。这些技能给 Agent 注入了与高级工程师同等的纪律约束。每个技能融入了 **Google 工程文化** 的具体实践：Hyrum 定律（API 设计）、Beyonce 规则（测试）、Chesterton's Fence（简化）、主干开发（Git）、Shift Left（CI/CD）等。

## 快速开始

```bash
# Claude Code（推荐）
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# Gemini CLI
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills

# 也支持 Cursor / Windsurf / OpenCode / Copilot / Codex / Kiro
```

## 核心功能

### 7 个开发生命周期命令

| 命令               | 阶段  | 核心原则        |
| ---------------- | --- | ----------- |
| `/spec`          | 定义  | 先写规格再写代码    |
| `/plan`          | 规划  | 小而原子的任务拆分   |
| `/build`         | 构建  | 一次一个切片，逐步交付 |
| `/test`          | 验证  | 测试是证明，不是装饰  |
| `/review`        | 审查  | 持续改善代码健康度   |
| `/code-simplify` | 简化  | 清晰优于聪明      |
| `/ship`          | 发布  | 更快就是更安全     |

### 23 个技能（按生命周期）

| 阶段 | 技能 | 作用 |
|------|------|------|
| **Define** | interview-me | 一对一访谈，挖出用户真正想要什么（到 95% 置信度） |
| | idea-refine | 发散/收敛思维，把模糊想法变成具体方案 |
| | spec-driven-development | 先写 PRD（目标/命令/结构/测试/边界）再写代码 |
| **Plan** | planning-and-task-breakdown | 将 spec 分解为小而原子的可执行任务 |
| **Build** | incremental-implementation | 一次一个切片，持续可运行 |
| | context-engineering | 优化 Agent 上下文利用效率 |
| | source-driven-development | 先读现有代码再写新代码 |
| | doubt-driven-development | 遇到不确定时主动停下来确认 |
| | frontend-ui-engineering | 前端 UI 工程最佳实践 |
| | test-driven-development | TDD 红→绿→重构循环 |
| | api-and-interface-design | API 设计规范（含 Hyrum 定律） |
| **Verify** | browser-testing-with-devtools | 浏览器 DevTools 验证 |
| | debugging-and-error-recovery | 系统化调试与错误恢复 |
| **Review** | code-review-and-quality | 代码审查与质量门禁 |
| | code-simplification | 简化代码（含 Chesterton's Fence 原则） |
| | security-and-hardening | 安全加固审查 |
| | performance-optimization | 性能优化 |
| **Ship** | git-workflow-and-versioning | 主干开发 + 版本管理 |
| | ci-cd-and-automation | CI/CD 自动化（Shift Left + Feature Flags） |
| | deprecation-and-migration | 废弃与迁移——代码即负债 |
| | documentation-and-adrs | 文档 + 架构决策记录 |
| | shipping-and-launch | 发布上线流程 |
| **Meta** | using-agent-skills | 自动匹配任务到对应技能，定义共享操作规则 |

### 技能设计原则

- **Process, not prose**：技能是可执行工作流，不是参考文档。每项含步骤、检查点、退出标准
- **Anti-rationalization**：每项技能含常见借口表（如「测试之后再加」）及反驳论据
- **Verification is non-negotiable**：每项技能结尾要求证据——测试通过、构建输出、运行时数据。「看起来对」永远不够
- **Progressive disclosure**：SKILL.md 是入口，引用按需加载，Token 消耗最小

## 与 ECC 的定位差异

| 维度 | ECC | agent-skills |
|------|-----|-------------|
| 侧重 | Agent 性能优化（Token/记忆/并行/安全） | 软件开发流程纪律（spec→ship 全生命周期） |
| 来源 | 社区实战（黑客松冠军） | Google 工程文化（Addy Osmani） |
| 技能数 | 覆盖运营/开发/安全等多角色 | 23 个专注软件工程生命周期 |
| 互补性 | 让 Agent 跑得更快更省 | 让 Agent 写得更稳更好 |

## 适用场景

- 想让 AI Agent 遵循真正的工程纪律（而非快速糊代码）
- 团队标准化 AI 编程工作流——spec→plan→build→test→review→ship
- 学习 Google 级工程实践在 AI Agent 中的具体落地
- 与 ECC 互补：ECC 管 Agent 运行效率，agent-skills 管代码质量流程

## 评价

- **优点**：Addy Osmani 背书质量权威、Google 工程文化深度融入（Hyrum/Beyonce/Chesterton's Fence）、Anti-rationalization 设计精妙、Progressive disclosure 控制 Token、23 技能全生命周期覆盖无死角、MIT 开源
- **局限**：偏软件工程流程，缺少 ECC 那样的 Token/内存/安全扫描等运维优化、对非软件工程场景（如知识管理）覆盖有限
- **是否值得长期保留**：✅ 必读参考——与 ECC 形成「效率+质量」双塔，Skill 设计模式（Process/Anti-rationalization/Verification）可直接复用到本知识库的 Agent 化
