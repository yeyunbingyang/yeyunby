---
title: "ECC (Everything Claude Code) Agent 性能优化系统"
tags: [GitHub, 开源, AI, Agent, Claude, MCP, 安全]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-07-16
source: https://github.com/affaan-m/ECC
zh-CN: https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md
related: [[anthropics-skills-官方Skills仓库]]
summary: "Anthropic 黑客松冠军作品，193k Stars 的 Agent 全套配置系统：技能、本能、记忆、安全、研究优先开发模式，支持 Claude Code/Codex/Cursor 等主流 AI 编程工具"
---

# ECC (Everything Claude Code) Agent 性能优化系统

https://github.com/affaan-m/ECC

## 基本信息

**类型：** 工具
**链接：** https://github.com/affaan-m/ECC
**主页：** https://ecc.tools
**适用领域：** AI Agent 配置优化、Claude Code 增强、MCP 管理、Agent 安全、研发工作流
**推荐程度：** ★★★★★
**Stars：** ~193k（Fork 29.9k）
**贡献者：** 170+
**语言：** TypeScript / JavaScript / Python / Go / Java / Perl
**许可证：** MIT
**NPM：** ecc-universal、ecc-agentshield
**背景：** Anthropic x Forum Ventures 黑客马拉松冠军

## 是什么

ECC（Everything Claude Code）是 Anthropic 黑客马拉松冠军作品，不止是 Claude Code 配置文件集合，而是一整套 Agent 性能优化系统。包含：技能体系、本能行为、记忆优化、持续学习、安全扫描、研究优先开发模式。作者用它在多个生产应用中高强度使用 10+ 个月打磨而成。

支持 **Claude Code**、**Codex**、**Cursor**、**OpenCode**、**Gemini** 等主流 AI Agent 框架。

## 快速开始

```bash
# 一键安装（推荐）
npx ecc-init

# 或手动
git clone https://github.com/affaan-m/ECC
cd ECC

# Claude Code
claude plugins install @affaan-m/ECC

# Codex
codex plugin install @affaan-m/ECC

# NPM 包
npm install ecc-universal ecc-agentshield
```

## 核心功能

### 四大子系统

- **Agents（代理）**：子代理以有限范围处理委托任务，含 code-reviewer、test-runner 等预置
- **Skills（技能）**：由命令或代理调用的工作流定义，如 TDD 工作流、brand-voice、customer-billing-ops 等
- **Hooks（钩子）**：工具事件触发自动化，如自动检测 console.log、安全扫描、上下文保存/加载
- **Rules（规则）**：始终遵循的编码指南，分 common/（通用）+ 语言特定（TypeScript/Python/Go/Perl/Java）

### 关键技术能力

- **Token 优化**：模型选择、系统提示精简、后台进程管理
- **记忆持久化**：自动跨会话保存/加载上下文的钩子系统
- **持续学习**：从会话中自动提取模式到可重用技能
- **验证循环**：检查点 vs 持续评估、多种评分器、pass@k 指标
- **并行化**：Git worktrees、级联方法、实例扩展策略
- **子代理编排**：上下文问题处理、迭代检索模式
- **安全扫描**：攻击向量检测、沙箱技术、数据净化、CVE 漏洞、Agent 防护

### v2.0.0-rc.1 新特性（2026年4月）

- 运营工作流扩展：brand-voice、social-graph-ranker、customer-billing-ops、google-workspace-ops
- 媒体工具：manim-video、remotion-video-creation
- GitHub App：150+ 安装量，可直接粘贴 MCP 配置

## 关键教训（来自作者实战经验）

- **不要一次启用所有 MCP**：配置 20-30 个 MCP，但每个项目启用 <10 个，活动工具 <80 个，否则 200k 上下文窗口可能缩减到 70k
- **定制优先**：从适合自己的开始，为技术栈修改，删除不用，添加自有模式
- **10 个月实战打磨**：在 zenith.chat 等生产项目中验证

## 适用场景

- Claude Code / Codex 用户想系统性提升 Agent 工作效率
- 需要 Agent 安全的团队（AgentShield 安全扫描）
- 多语言项目团队（12+ 语言系统内置）
- 想建立 Agent 持续学习/记忆持久化机制
- 从零搭建 AI 编程 Agent 配置体系

## 评价

- **优点**：覆盖面极广（Agents+Skills+Hooks+Rules+MCP）、黑客松冠军品质保证、193k Stars 社区验证、多 Agent 框架兼容、安全体系完善、NPM 包生态、10 个月实战打磨
- **局限**：学习曲线陡峭（配置量巨大）、重度依赖 Claude Code 生态、需大量定制才能匹配个人工作流
- **是否值得长期保留**：✅ 必读参考——目前最强的 Agent 性能优化开源方案，MCP 管理和安全体系可直接复用
