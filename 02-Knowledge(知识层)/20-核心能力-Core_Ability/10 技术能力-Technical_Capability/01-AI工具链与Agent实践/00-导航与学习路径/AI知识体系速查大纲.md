---
title: AI 知识体系速查大纲（2026-07 修订版）
domain: Core_Ability
tags: [AI, 知识体系, 速查, 大纲]
status: 稳定
created: 2026-07-23
updated: 2026-07-23
source: "联网核查 + vault 内部知识蒸馏"
summary: "AI 技术体系层级化速查大纲：基础概念→模型→工具链→最佳实践，所有数据经网络交叉验证。"
related: []
verified: 2026-07-25
review_after: 2026-10-25
---

# AI 知识体系速查大纲

> **版本说明**：2026-07-23 修订。所有模型规格、工具功能、定价数据均经搜索引擎交叉验证。修正了 GPT-5.6 Sol 发布日期、章节编号重复等错误。

---

## 一、基础概念

### 人工智能基础
- **AI (Artificial Intelligence)**：人工智能，模拟人类智能完成任务。
- **AIGC (AI Generated Content)**：AI 生成内容。
- **多模态 (Multimodal)**：模型不仅理解文字，还能处理/理解图片、音频、视频等多种媒体文件。

### 大语言模型 (LLM) 核心术语
- **Token【词元】**
  - 模型处理文本的最小单元，一个汉字约 1-2 个 Token
  - Token 类型：
    - **Input Token**：输入 Token，用户发送给模型的文本
    - **Output Token**：输出 Token，模型生成的回复文本
    - **Cached Token**：缓存 Token，已缓存的上下文复用
    - **Reasoning Token**：推理 Token，模型内部思考/链式推理过程消耗的 Token。
- **Prompt【提示词】**：用户输入给模型的指令或问题
- **Context Window【上下文窗口】**：模型单次会话能"看到"的最大 Token 数量（如 128K、256K、1M 等，K=千，M=百万）。
- **Temperature【温度】**：控制输出随机性的参数（0 = 确定性，1 = 高创造性）
- **Hallucination 幻觉**：模型基于概率预测下一个词，可能生成看似合理但实际错误的内容。
- **参数量 (Parameters)**：模型的"大脑"规模，常用 B (Billion, 十亿) 表示。参数量越大，理解与复杂推理能力通常越强。
- **Embedding（向量/文本嵌入）**：将文本映射为高维数值向量，用于语义检索、RAG 和相关性计算。
- **Inference（推理）**：模型接受输入并计算生成答案的过程。
- **Fine-tuning（微调）**：在特定数据集上对预训练模型进行二次训练，使其适应特定领域任务。
- **RAG (Retrieval-Augmented Generation)**：检索增强生成，通过引入外部知识库/文档检索，解决模型知识时效性与局限性问题。

### Agent（智能体）概念与架构
- **核心定义**：Agent = LLM + 工具 + 规划 + 记忆 + 执行（不只是聊天，而是具身化完成复杂任务）。
- **工作循环**：感知 (Perceive) → 推理 (Reason) → 行动 (Act) → 反馈 (Feedback)。
- **Agent 生态**：
  - **MCP (Model Context Protocol)**：AI 调用外部工具/数据源的标准化通用接口（类比 AI 的 USB-C 接口）。
  - **A2A（Agent-to-Agent）**：Agent 之间怎么对话（外部协作分工）
  - **Agent Skills**：可复用、可组合、按需加载的工作流规范。
  - **Sub-agent（子代理）**：主 Agent 将子任务委派给独立的子 Agent 异步/并行处理。
  - **Hooks（自动触发器）**：事件驱动的自动响应机制
  - **Plugins（插件）**：扩展 Agent 能力的插件系统

### Vibe Coding（氛围编程）
- **核心理念**：关注产品效果与业务逻辑，不纠结代码微观细节，让 AI 协作实现代码。
- **核心原则**：
  - 意图优先：先描述你想要什么效果，而不是告诉 AI 怎么写代码
  - 快速迭代：不追求一次完美，拥抱"生成 → 测试 → 修正"的循环
  - 信任但验证：相信 AI 的能力，但始终检查关键逻辑
  - 上下文经营：持续维护和优化提供给 AI 的背景信息
- **SDD (Specification-Driven Development，规范驱动开发)**：
  - 需求规范：PRD 文档（产品需求文档），明确"要做什么"。
  - 技术规范：SPEC 文档（技术规范文档），明确"怎么做"。
  - 质量规范：明确"做到什么程度算合格"

---

## 二、模型

### 主流模型对比

#### 国内模型
| 模型 | 上下文 | 发布时间 | 参数量 | 特色 |
|------|--------|----------|--------|------|
| **Kimi K3** | 1M | 2026-07-16 | 2.8T MoE | 多模态，开源，Delta Attention |
| **DeepSeek V4 Pro** | 1M | 2026-04 (Preview) / 2026-07 (GA) | — | 性价比极佳，支持本地/私有化部署 |
| **DeepSeek V4 Flash** | 1M | 2026-04 (Preview) / 2026-07 (GA) | — | 成本极低，适合高并发任务 |
| **Kimi K2.6** | 256K | 2026-06 | — | 长文本检索与中文场景深度优化，多模态 |
| **GLM-5.2** | 1M | 2026-06-13 | 744B MoE | 开源，支持 High/Max 推理模式 |

#### 国外模型
| 模型 | 上下文 | 发布时间 | 参数量 | 特色 |
|------|--------|----------|--------|------|
| **GPT-5.6 Sol** | 1.05M | 2026-07-09 | 未公开 | 复杂系统架构与代码编写首选 |
| **Claude Fable 5** | 1M | 2026-06 | 未公开 | 逻辑严密，擅长结构化输出与 Agent 工具调用 |
| **Claude Opus 4.8** | 1M | 2026-05-28 | 未公开 | 极致分析能力，适合跨文件大型工程重构 |
| **Gemini 3.5 Flash** | 1M | 2026-06 | — | 速度极快，多模态能力强，提供慷慨免费 API |

#### 场景选型建议
- **复杂架构设计**：GPT-5.6 Sol / Claude Opus 4.8
- **日常编码主力**：DeepSeek V4 Pro / Kimi K3
- **批量处理 / 高并发**：DeepSeek V4 Flash
- **中文内容创作**：Kimi K2.6
- **免费额度 / 快速原型开发**：Gemini 3.5 Flash

#### 成本优化策略
- **策略一：分层使用**（根据任务复杂度选择不同档位的模型）。
- **策略二：Prompt Cache 缓存利用**（复用高频上下文与 Prompt 模版，大幅降低 Token 消耗）。
- **策略三：本地模型补充**（部署轻量本地模型处理简单任务，降低 API 费用）。

### 代理与网关
- **CC-Switch 模型管理器**（Claude Code 模型切换层，GitHub: jawerty/claude-switch）
  - **原理**：劫持 Claude Code 的 API 请求，将模型名映射到任意厂商的任意模型。
  - **三档配置**：
    - 高 (opus)：复杂架构设计、多文件重构、深度分析 → GPT-5 / Claude Opus 4
    - 中 (sonnet)：日常编码、代码审查、文档生成 → DeepSeek V4 Pro / Qwen-Max
    - 低 (haiku)：简单问答、格式修正、文件检索 → DeepSeek V4 Flash / Gemini 2.5 Flash
  - 适用场景：在 Claude Code 内通过 `/model` 命令一键切换底层模型。

- **9router**（智能路由网关）
  - **核心能力**：模型路由——根据 Token 消耗自动在不同模型间 fallback。
  - **Token 优化**：
    - RTK 技术：压缩工具输出（git diff、grep 等），节省 **20-40%** Input Token
    - Caveman 模式：压缩模型回复，节省至高 **65%** Output Token
  - 适用场景：最大化订阅利用，防止单个 API 限额被打满。

- **omniRoute**（超级聚合路由，GitHub: diegosouzapw/OmniRoute / agenticocho/omniroute）
  - **250 个供应商**（含 90+ 免费层）
  - **~1.6B 有文档依据的免费 Token/月**（首月含注册赠额最高约 ~2.1B）
  - **18 种路由策略**（任务感知智能路由、Thinking Budget 控制、通配符路由等）
  - **94 个 MCP 工具**（路由、缓存、压缩、记忆、Skills、代理、上下文源等）
  - **RTK+Caveman 压缩省 15-95% Token**
  - **Auto-Combo 智能路由**：自动组合可用供应商，零配置启动
  - 适用场景：多供应商统一网关，大流量场景下的成本最优路由。

---

## 三、工具链

### 基础设施

#### Skills
- **核心定义**：可复用的提示词机制——将重复工作流固化为标准化技能规格说明书，避免自然语言反复描述。
- **核心原则**：
  - 能用 Skill 就不用自然语言
  - 重复 3 次以上的工作流，固化为 Skill
- **三层结构**：
  - 元数据（Metadata）：目录、必须加载
  - 指令层（Instructions）：正文、按需加载
  - 资源层（Resources）：附录、按需加载
- **文件结构**：
  ```
  项目根目录/
  └── .claude/
      └── skills/
          └── 技能名称/
              ├── skill.md      ← 定义文件（必须）
              ├── scripts/      ← 可执行脚本（可选）
              ├── references/   ← 参考文档（可选）
              └── assets/       ← 图片等资源（可选）
  ```
- **配置路径**：
  - 全局配置：`~/.claude/skills/` 或 `~/.codex/skills/`
  - 项目配置：项目根目录/`.claude/skills/` 或 项目根目录/`.codex/skills/`
- **自定义 Skill 最佳实践**：
  - **3 次法则**：重复 3 次以上的工作流，固化为 Skill
  - **小而专**：一个 Skill 只做一件事情
  - **定期蒸馏**：每 2 周回顾高频 Skill，合并、简化、发现自动化机会
- **调用方式**：
  - 方式一：斜杠命令（如输入 `/spec` 或 `/` 查看可用 Skill）
  - 方式二：自然语言触发，AI 自动匹配语义相符的 Skill
  - 注意：过多 Skills 会导致上下文膨胀、匹配精度下降。需分级管理（基础/项目/临时），按需动态加载，定期清理过时 Skill。
- **官方与社区 Skill 资源**：
  - 工具与库：npx skills、Anthropic 官方 Skill 库、Vercel 官方 Skill 库、社区 GitHub 精选仓库
  - 聚合平台：skills.sh, SkillsMP, AgentSkills.io, LobeHub
- **高频 Skill 分类速查**：

  **日常高频**
  | Skill | 用途 |
  |-------|------|
  | think | 思考、方案设计、架构决策 |
  | write | 润色、改写、降 AI 味 |
  | learn | 深度学习某一主题 |
  | obsidian-markdown | Obsidian Markdown 编辑 |
  | skill-creator | 创建或优化 Skill |
  | find-skills | 搜索可安装 Skill |
  | grill-me | 需求澄清、反向提问 |
  | spec | PRD、需求访谈、规格定 |

  **调研与搜索**
  | Skill | 用途 |
  |-------|------|
  | agent-reach | 全网调研、社交媒体搜索 |
  | deep-research | 多源交叉验证的深度报告 |
  | web-scraping | Python 爬虫抓取 |
  | agent-browser / OpenCLI | 浏览器自动化（按偏好选择） |

  **开发与审查**
  | Skill | 用途 |
  |-------|------|
  | code-review | 代码审查 |
  | verify | 验证/检查 |

  **中文内容创作**
  | Skill | 用途 |
  |-------|------|
  | baoyu-skills | 小红书/公众号/微博发布 |

- **Superpowers 插件**：把成熟工作流封装成可复用能力。

#### MCP
- **定义**：外部资源的连接方式
- **使用场景**：
  - 企业知识库 RAG
  - 访问 API
  - AI 编程工作流

### CLI Agent（命令行智能体）

#### Claude Code
- **权限模式与交互方式**：
  - **Plan Mode**：仅生成执行计划，不修改文件，等待用户确认
  - **默认模式**：智能判断风险，平衡安全与效率
  - **Auto-edit**：自动修改文件，但执行终端命令前仍需确认
  - **YOLO Mode**（启动加参数）：完全自动零确认
  - **交互方式**：文本对话、@ 文件引用、图片多模态输入

- **高频斜杠命令**：
  | 命令 | 用途 |
  |------|------|
  | `/help` | 查看所有命令 |
  | `/model` | 切换模型或推理档位（配合 CC-Switch 使用） |
  | `/btw` | 临时提问（隔离当前项目上下文） |
  | `/simplify` | 代码优化、重构与简化 |
  | `/compact` | 压缩上下文，保留关键信息 |
  | `/clear` | 清空当前对话上下文 |
  | `/context` | 查看上下文占用情况 |
  | `/rewind` | 双击 Esc 或运行此命令，撤销 AI 代码修改 |
  | `/memory` | 管理 CLAUDE.md 与 Auto Memory |
  | `/init` | 初始化项目级 CLAUDE.md 配置 |
  | `/agent` | 创建或管理子 Agent |
  | `/plugin` | 插件管理 |

- **记忆与上下文管理体系**：
  - **CLAUDE.md（主动规则）**：项目级（`/init` 自动生成）、全局级（`CC "记住..."`）、文件夹级
  - **Auto Memory（自动记忆）**：通过 `/memory` 开启，自动积累上下文经验
  - **自定义文档记忆**：在 CLAUDE.md 中指引引用外部规范文档

- **版本控制与回滚（后悔药机制）**：
  - 双击 `Esc` 或输入 `/rewind`（局限：无法撤销终端命令）
  - Git 版本管理：每完成一个功能节点提交一次

- **上下文管理（解决"变笨"问题）**：
  - 主动压缩：`/compact`
  - 彻底重置：`/clear`
  - 查看占用：`/context`

#### Codex
- **记忆体系**：
  - 全局：`Agents.md`
  - 项目：`Agents.md`
  - 自动记忆（需在设置中开启）

#### Hermes Agent
- **配置文件与配置管理**（`~/.hermes/`）：
  ```
  ~/.hermes/
  ├── config.yaml        # 主配置文件（模型、终端、TTS、压缩等）
  ├── .env               # API 密钥和机密信息
  ├── auth.json          # OAuth 提供商凭证（Nous Portal 等）
  ├── SOUL.md            # 主 Agent 身份 / 人格文件
  ├── memories/          # 持久化记忆（MEMORY.md、USER.md）
  ├── skills/            # 技能（普通/总括/类别级三层体系）
  ├── cron/              # 定时任务
  ├── sessions/          # 会话
  └── logs/              # 日志（errors.log、gateway.log）
  ```

- **核心能力**：
  - **会话管理**：SQLite (`~/.hermes/state.db`) 存储，支持自动上下文压缩与 `/compress` 手动触发
  - **Session Search**：免 LLM 依赖的超高速会话搜索（速度提升 4500 倍）
  - **Web Dashboard**：可视化管理界面
  - **Toolsets & MCP**：标准工具集与 MCP 协议集成
  - **上下文文件**：自动发现并加载上下文文件；`SOUL.md` 用于描述人格和沟通风格
  - **持久记忆**：memory 保存稳定事实；session_search 用于回溯历史

- **自进化与高级生态**：
  - **Skills 技能系统**（Hermes 核心差异化能力）：
    - Agent 解决复杂问题后，自己把流程保存为 Skill，下次自动加载
    - 技能目录：`~/.hermes/skills/`
    - **三种层级**：
      1. **普通具体 Skill**：单一任务（如 `code-review`, `web-scraping`）
      2. **总括型 Skill（umbrella）**：聚合多个具体 Skill
      3. **类别级总括型 Skill**：按领域/功能分类的顶级入口（如 `software-development/`）
    - **Skill Bundles**：用一个斜杠命令同时加载多个技能
    - **Agent-Managed Skills**：创建、修改和删除自己的技能
  - **Curator 技能维护系统**：跟踪技能使用频率，将长期不用的从 active → stale → 归档
  - **三级 Hook 系统**：Shell Hooks（阻止危险命令/格式化）、Plugin Hooks（工具拦截/记忆召回）、Gateway Hooks（日志/告警/Webhook）
  - **Plugins 插件系统**：无需修改核心代码即可添加自定义工具、钩子和集成（`~/.hermes/plugins/`）
  - **Cron 定时任务**：`/cron` 命令管理

- **协作能力**：
  - **Gateway 消息网关**：消息平台接入层
  - **Profile 多实例**：通过 Profile 运行多个独立 Agent，各有独立的配置、会话、技能和记忆
  - **Delegation 任务委派**：创建子 Agent 处理独立任务
  - **Kanban 多 Agent 协作**：持久任务板，多个具名 profile 异步协作

---

## 四、最佳实践

### Vibe Coding（以 Claude Code 为例）

- **Vibe Coding 实战工作流**：Explore → Plan → Implement → Commit
  - 阶段一：需求对齐（需求完整度检查）
  - 阶段二：方案设计（选择 Skills + 规划步骤）
  - 阶段三：执行（按计划调用 Skills）
  - 阶段四：验证与收尾

- **标准项目启动**：
  1. 项目初始化（描述目标，生成项目骨架）
  2. 建立 CLAUDE.md（运行 `/init` 生成项目上下文文件）
  3. 配置权限与模式（复杂项目默认 Plan 模式）
  4. 功能开发（一个功能一个循环：Explore → Plan → Implement）
  5. 代码审查与测试（使用 `/review` 或测试 Skill）
  6. 代码提交（Git commit 保存阶段性成果）

- **Prompt 编写技巧**：
  - 具体明确：任务描述要清晰具体，避免模糊表达
  - 参考引用：明确引用已有代码或规范文档作为参考
  - 先计划后执行：先让 AI 制定 Plan，确认无误后再授权执行
  - 单步聚焦：一次只做一件事，避免"万能 Prompt"

- **大型代码库最佳实践**：
  1. 用 `/init` 自动生成 CLAUDE.md
  2. 任务粒度要小且聚焦
  3. 频繁重置上下文（`/clear` 是好朋友）
  4. 复杂任务从 Plan Mode 起手
  5. 用 Skills 与 Sub-agents 卸载长任务
  6. 接入 MCP / LSP

  **进阶建议**：
  - 在子目录初始化 Claude，别从仓库根目录开始（每个子目录放一份小的 `CLAUDE.md`）
  - 配置要定期审查（每 3-6 个月）
  - 团队内应有个"人"负责 Claude Code（DRI / Agent Manager）

- **新项目启动套件**：
  - 第一个文件：`CLAUDE.md`
  - 第二个文件：`settings.json`
  - 第三个文件：`.gitignore`
  - 第四个：9 个 Slash Command（Skills）
- **自定义斜杠命令**：`.claude/commands/` 目录

### Karpathy 四大原则（推荐写入项目 CLAUDE.md）

1. **Think Before Coding**：写代码前先分析问题、列出方案、指出权衡，确认理解正确后再动手
2. **Simplicity First**：优先选择最简单的方案，不引入新框架除非绝对必要
3. **Surgical Changes**：修改时只改需要改的地方，一次只做一件事
4. **Goal-Driven Execution**：每步完成后验证是否达到目标，测试通过才算完成

---

> **数据核查说明**：本文档于 2026-07-23 经搜索引擎交叉验证。OmniRoute 数据来自 GitHub 主仓库 (diegosouzapw/OmniRoute)，CC-Switch 数据来自 GitHub (jawerty/claude-switch) 与 vault 内部笔记。模型规格来自各厂商官方公告及 Artificial Analysis、OpenRouter 等第三方评测平台。
