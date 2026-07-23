---
title: 官方与社区 Skill 资源集成指南
description: Skills 生态的官方工具、社区仓库与聚合平台的完整指南——npx skills CLI、Anthropic/Vercel 官方库、GitHub 精选仓库、skills.sh/SkillsMP/AgentSkills.io/LobeHub
aliases:
  - Skill 资源集成
  - Skills 资源地图
tags:
  - skills
  - resources
  - CLI
  - marketplace
  - ecosystem
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
related:
  - "04-Skills生态全景"
  - "03-通用skills最佳实践"
summary: "从安装工具到聚合平台，再到社区 GitHub 精选仓库的完整 Skills 资源索引。配合 04-Skills生态全景 使用（生态全景侧重仓库分析，本指南侧重资源获取入口）。"
---

# 官方与社区 Skill 资源集成指南

> Skills 生态已从 Anthropic 官方规范发展到 1000+ 技能覆盖全技术栈。本文提供从**安装工具 → 官方库 → 社区仓库 → 聚合平台**的完整资源索引。
>
> 配合 [[04-Skills生态全景]] 使用——生态全景侧重 13 个核心仓库的深入分析，本指南侧重资源获取入口的实用索引。

---

## 一、安装与配置工具

### 1.1 `npx skills` — 官方 CLI 安装器

Skills 生态的核心安装工具，基于 npm 生态，支持从任意 GitHub 仓库安装技能。

```bash
# 基本安装
npx skills add <owner>/<repo>@<skill-name>

# 全局安装（对所有项目生效）
npx skills add <owner>/<repo>@<skill-name> -g

# 项目级安装
npx skills add <owner>/<repo>@<skill-name> -y

# 安装全部技能
npx skills add mindrally/skills -g

# 安装特定技能
npx skills add mindrally/skills --skill react
```

**常见安装来源**：

| 来源 | 安装命令 | 说明 |
|------|---------|------|
| 官方示范 | `npx skills add anthropics/skills@skill-creator` | 官方示例 |
| 工程习惯 | `npx skills add tw93/Waza@think` | Waza 链式技能 |
| Obsidian | `npx skills add kepano/obsidian-skills@obsidian-cli` | Obsidian 操作 |
| 全技术栈 | `npx skills add mindrally/skills` | 240+ 技能全集 |

### 1.2 Anthropic 官方 Skill 库（141k★）

- **仓库**：https://github.com/anthropics/skills
- **定位**：Skill 格式标准的定义者，生态源头
- **内容**：17 个官方示例技能 + 文档技能（docx/pdf/pptx/xlsx）+ Skill 规范 + 模板
- **安装**：`npx skills add anthropics/skills@<skill-name>` 或 `/plugin marketplace add anthropics/skills`
- **关键技能**：`canvas-design`、`mcp-builder`、`webapp-testing`、`skill-creator`、`web-artifacts-builder`
- **许可证**：Apache-2.0（示例技能）/ 源码可用（文档技能）
- **本库关联笔记**：[[05-anthropics-skills-官方Skills仓库]]

### 1.3 Vercel 官方 Skill 库

Vercel 作为 Skills 生态的重要贡献者，提供了以下核心工具：

**agent-browser（37.9k★）**
- 仓库：https://github.com/vercel-labs/agent-browser
- 定位：浏览器自动化 CLI，通过 Snapshot + refs 系统实现 Token 最优的网页交互
- 安装：`npx skills add vercel-labs/agent-browser@agent-browser`
- 本库关联笔记：[[04-agent-browser-浏览器自动化CLI]]

**Skills CLI（npx 生态）**
- Vercel 维护了 `npx skills` 包的 npm 发布和持续集成
- 通过 Skills CLI 格式兼容，使 Claude Code、Codex 等 Agent 共享同一技能规范

### 1.4 Community CLI 工具

| 工具 | 来源 | 说明 |
|------|------|------|
| `agent-skills CL`I | addyosmani/agent-skills | 23 个技能覆盖 spec→ship 全流程 |
| `opencli` | jackwener/OpenCLI | 网站 CLI 桥接，不直接安装 skills 但可与 skills 配合 |

---

## 二、社区 GitHub 精选仓库

### 2.1 配置与技能体系（26 个项目）

本库 `03-Resources/00 Github优质项目/02-Agent配置与Skills/` 下收录了 26 个 Skills 相关的 GitHub 项目，以下是分类速查：

#### 官方与标准

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **anthropics/skills** | 141k★ | 官方 Skills 仓库 | [[05-anthropics-skills-官方Skills仓库]] |
| **huggingface/skills** | 10.8k★ | SKILL.md 标准化技能包 | [[19-skills-通过SKILLmd标准化的可复用技能包兼容多种编码]] |

#### 索引与精选

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **awesome-claude-skills** | 66.9k★ | 1000+ Claude 技能索引 | [[09-awesome-claude-skills-Claude技能精选]] |
| **awesome-codex-skills** | 11.8k★ | Codex 技能索引 | [[18-awesome-codex-skills-Codex技能精选]] |

#### 工程习惯与工作流

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **mattpocock/skills** | 106k★ | 工程师日常技能（grill/TDD/review） | [[01-mattpocock-skills-工程师日常技能]] |
| **agent-skills** | 45.9k★ | 生产级工程技能包（23 个技能） | [[14-agent-skills-生产级工程技能包]] |
| **waza（tw93/Waza）** | — | 8 个工程习惯技能 | [[26-waza-工程习惯技能包]] |
| **sim（workflow builder）** | — | 工作流构建器 | [[12-sim-工作流构建器]] |
| **ECC** | 193k★ | Agent 全套配置系统 | [[03-ECC-Agent全套配置系统]] |

#### 多智能体与协作

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **myclaude** | — | 多智能体工作流系统 | [[22-myclaude-多智能体工作流系统]] |
| **agency-agents** | 105k★ | 完整 AI 机构角色库 | [[07-agency-agents-完整AI机构角色库]] |
| **knowledge-work-plugins** | 16.3k★ | 知识工作角色插件 | [[15-knowledge-work-plugins-知识工作角色插件]] |

#### 特定领域

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **kepano/obsidian-skills** | 42.3k★ | Obsidian 官方开发者出品 | [[11-obsidian-skills-Obsidian官方开发者kepano出品的AI]] |
| **baoyu-skills** | 23.8k★ | 20+ 中文内容创作技能 | [[23-baoyu-skills-中文内容创作技能]] |
| **remotion-skills** | 4k★ | 视频编程技能 | [[24-remotion-skills-视频编程技能]] |
| **mindrally/skills** | — | 240+ 全技术栈技能集合 | [[25-mindrally-skills-全技术栈技能集合]] |
| **claude-skills (jeffallan)** | 10.6k★ | 66 项专业技能 + 9 个工作流 | [[20-claude-skills-提供66项专业技能和9个工作流用于基于Claude]] |
| **Anthropic-Cybersecurity-Skills** | 25.7k★ | 754 个生产级安全技能，映射五大安全框架 | — |
| **spec-kit** | 122k★ | GitHub 官方规格驱动开发工具包 (理念相通) | — |

#### 工具与配置

| 仓库 | Stars | 说明 | 本库笔记 |
|------|-------|------|---------|
| **superpowers** | 207k★ | Agent 开发方法论 | [[02-superpowers-Agent开发方法论]] |
| **cc-switch** | — | 多 Agent 桌面管理器 | [[08-cc-switch-多Agent桌面管理器]] |
| **gstack** | — | Claude Code 配置 | [[06-gstack-ClaudeCode配置]] |
| **headroom** | — | 上下文压缩 | [[10-headroom-上下文压缩]] |
| **9router** | — | 免费 AI 路由网关 | [[13-9router-免费AI路由网关]] |
| **omniroute** | — | 236 供应商 AI 网关 | [[16-omniroute-236供应商AI网关]] |
| **agents.md** | — | 仓库上下文 | [[17-agents-md-仓库上下文]] |
| **hermes-desktop** | — | Hermes Agent 桌面管理 | [[21-hermes-desktop-HermesAgent的桌面可视化安装配置和对话管]] |

> 以上所有项目详情见 `03-Resources/00 Github优质项目/02-Agent配置与Skills/` 目录。

---

## 三、聚合平台

以下聚合平台可以搜索、发现和安装 Skills：

### 3.1 skills.sh

- **地址**：https://skills.sh
- **定位**：Skills 搜索引擎，检索已发布的 Agent Skills
- **特点**：按名称、描述、标签搜索，快速找到需要的技能
- **用法**：搜索到 skill 后，使用 `npx skills add` 安装

### 3.2 SkillsMP

- **地址**：https://skillsmp.com
- **定位**：Skills Marketplace——技能市场
- **特点**：社区提交、评分系统、分类浏览
- **覆盖**：Claude Code、Codex 等多平台的技能

### 3.3 AgentSkills.io

- **地址**：https://agentskills.io
- **定位**：Agent Skills 发现平台
- **特点**：可视化浏览、一键安装命令复制
- **用法**：找到技能后直接复制 `npx skills add` 命令

### 3.4 LobeHub

- **地址**：https://lobechat.com 或对应的 Skills 页面
- **定位**：开源 LLM 聊天框架的技能插件市场
- **特点**：LobeChat 生态中的 Agent 技能/插件集成
- **适用**：LobeChat 用户，通过技能扩展 AI 助手能力

---

## 四、技能资源快速导航

### 4.1 按需求选资源

| 需求 | 推荐资源 |
|------|---------|
| **想找官方标准** | Anthropic 官方库 + `npx skills` CLI |
| **想找最全索引** | awesome-claude-skills（1000+ 技能） |
| **想找工程习惯** | Waza（轻量）、mattpocock/skills（工程化） |
| **想找特定领域** | obsidian-skills、baoyu-skills、remotion-skills |
| **想搜技能** | skills.sh、SkillsMP、AgentSkills.io |
| **想安装试用** | `npx skills add <仓库>` 命令即可 |

### 4.2 快速安装示例

```bash
# 安装 skill-creator（官方，创建自定义技能）
npx skills add anthropics/skills@skill-creator -g

# 安装 think（Waza，方案设计）
npx skills add tw93/Waza@think -g

# 安装 grill-me（mattpocock，需求对齐）
npx skills add mattpocock/skills@grill-me -g

# 安装 code-review（agent-skills，代码审查）
npx skills add addyosmani/agent-skills@code-review -g
```

---

## 五、关联笔记

- [[04-Skills生态全景]] — Skills 生态 13 个核心仓库的深入对比分析（本指南的互补——那里讲"为什么好"，这里讲"去哪找"）
- [[03-通用skills最佳实践]] — Skills 使用心法与实战案例
- [[Obsidian-Agent操作指南]] — Obsidian 操作的具体技能
- [Github优质项目-MOC](../../../../../../../03-Resources(资源层)/00%20Github优质项目/Github优质项目-MOC.md) — 282 个开源项目总索引
