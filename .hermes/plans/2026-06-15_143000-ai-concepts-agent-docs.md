# AI 相关概念文档（含 Agent 领域深度覆盖）实施计划

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** 在知识库中创建一套结构清晰、专业与通俗兼顾的 AI 概念文档，重点覆盖 Agent 领域，每篇包含专业定义、大白话举例和可靠来源。

**Architecture:** 以现有 `Core_Ability/00 AI/00 概念/` 为落点，采用"总-分"结构：一篇总览 MOC + 多篇深度概念笔记，每篇遵循知识笔记模板规范（一句话结论 → 核心内容 → 大白话举例 → 来源 → 关联）。

**Tech Stack:** Obsidian Markdown + YAML Frontmatter + Dataview 查询 + Wikilink 双向链接

---

## 背景分析

### 现状

| 现状 | 详情 |
|------|------|
| `AI相关概念.md` | **空文件**（0行），位于 `Core_Ability/00 AI/00 概念/` |
| `提示词.md` | **空文件**（0行），同目录 |
| `AI工程-MOC.md` | 已有 Agent 框架大纲但零篇知识笔记 |
| `00 AI` 目录 | 有大量工具使用类笔记（Claude/CLI/Skills），但缺少概念层 |
| AI工程子域 | 只有 MOC 骨架，零篇实际笔记 |

### 定位决策

AI 概念文档放在 `Core_Ability/00 AI/00 概念/` 下（当前已有目录），聚焦**概念层**（what & why），与工具使用层（how）形成互补。

---

## Task 1: 重写 AI相关概念.md 为 AI 概念总览 MOC

**Objective:** 将空的 `AI相关概念.md` 改造为一篇结构化的概念导航 MOC，提供 AI 核心概念的全局视图和快速索引。

**Files:**
- Modify: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/AI相关概念.md`

**Step 1: 写入完整 frontmatter + MOC 内容**

```markdown
---
title: AI相关概念
domain: IT_Technology
tags: [MOC, AI, 概念, Agent]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: ""
related: [[AI工程-MOC]]
summary: "AI 核心概念导航地图，覆盖基础概念、大模型原理、Prompt 工程、Agent 架构与多 Agent 系统，每篇含专业定义与大白话举例"
---

# AI 相关概念

从零开始理解 AI 领域的关键概念，每个概念都配有**专业定义**和**大白话解释**。

## 概念地图

### 第一层：AI 基础概念

| 概念 | 一句话 | 详解 |
|------|--------|------|
| 人工智能 vs 机器学习 vs 深度学习 | 三层包含关系 | [[AI-机器学习-深度学习的关系]] |
| 监督学习 / 无监督学习 / 强化学习 | 三种学习范式 | [[机器学习三大范式]] |
| 神经网络基础 | 模拟人脑的计算模型 | [[神经网络核心概念]] |

### 第二层：大语言模型（LLM）

| 概念 | 一句话 | 详解 |
|------|--------|------|
| Token | 模型"读"文本的最小单位 | [[Token与分词]] |
| 上下文窗口 | 模型一次能"记住"多少内容 | [[上下文窗口与注意力机制]] |
| Temperature | 控制模型回答的"创造力" | [[Temperature与采样策略]] |
| Embedding | 把文字变成数学向量 | [[Embedding与向量检索]] |
| Transformer | 现代 LLM 的基础架构 | [[Transformer架构详解]] |

### 第三层：Prompt 工程

| 概念 | 一句话 | 详解 |
|------|--------|------|
| System Prompt | 给模型的"角色设定" | [[System-Prompt设计方法]] |
| Few-shot Prompting | 给模型几个例子让它照做 | [[Few-shot与思维链]] |
| Function Calling | 让模型"使用工具" | [[Function-Calling原理]] |

### 第四层：Agent 核心 ⭐

| 概念 | 一句话 | 详解 |
|------|--------|------|
| Agent 定义与架构 | 能自主规划+使用工具+记忆的 AI | [[Agent架构全景]] |
| ReAct 模式 | 思考-行动-观察的循环 | [[ReAct推理与行动模式]] |
| 工具调用 | Agent 的"手"——调 API、查数据库 | [[Agent工具调用机制]] |
| 记忆系统 | Agent 的"海马体"——短期/长期/语义记忆 | [[Agent记忆系统设计]] |
| 规划能力 | Agent 的"前额叶"——拆解任务、制定计划 | [[Agent规划与任务分解]] |

### 第五层：多 Agent 系统

| 概念 | 一句话 | 详解 |
|------|--------|------|
| 多 Agent 协作 | 多个 Agent 分工合作 | [[多Agent协作模式]] |
| LangGraph | 有状态的多步 Agent 工作流 | [[LangGraph核心概念]] |
| CrewAI / AutoGen | 角色扮演式多 Agent 框架 | [[多Agent框架对比]] |

### 第六层：模型部署与优化

| 概念 | 一句话 | 详解 |
|------|--------|------|
| 模型量化 (GGUF/GPTQ) | 给模型"减肥"让它跑在普通电脑上 | [[模型量化技术]] |
| LoRA 微调 | 只改模型一小部分来适配特定任务 | [[LoRA参数高效微调]] |
| RAG 架构 | 让模型"查资料"再回答 | [[RAG检索增强生成]] |

---

## 阅读路径

- **零基础入门**：从第一层开始，逐层往下
- **只想了解 Agent**：直接跳到第四层 → [[Agent架构全景]]
- **开发者实战**：第三层 → 第四层 → 第六层

## 相关笔记

```dataview
TABLE summary, status
FROM "KnowledgeBase/03-Knowledge/20-核心能力-Core_Ability/00 AI/00 概念"
WHERE file.name != "AI相关概念"
SORT file.name ASC
```
```

**Step 2: 验证**

在 Obsidian 中打开 `AI相关概念.md`，确认：
- [ ] Frontmatter 完整且符合 SCHEMA 规范
- [ ] Dataview 查询能正常显示同目录笔记
- [ ] 内部链接（[[wikilink]]）指向的目标文件名与实际一致

---

## Task 2: 创建 Agent架构全景.md — Agent 领域核心概念

**Objective:** 创建 Agent 概念入口笔记，覆盖 Agent 的定义、四要素架构（规划/工具/记忆/感知）、与传统程序的区别。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/Agent架构全景.md`

**Step 1: 写入笔记**

```markdown
---
title: Agent架构全景
domain: IT_Technology
tags: [概念, AI, Agent, 架构]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "Lilian Weng (2023) 'LLM Powered Autonomous Agents'; Andrew Ng (2024) 'AI Agentic Design Patterns'"
related: [[AI相关概念]], [[ReAct推理与行动模式]], [[Agent工具调用机制]], [[Agent记忆系统设计]]
summary: "AI Agent 是以大模型为大脑、具备规划-工具调用-记忆-感知四大能力的自主系统，与传统程序的本质区别在于'自主决策'而非'按预设逻辑执行'"
---

# Agent 架构全景

## 一句话结论

> AI Agent 就是一个 **"有脑子、会动手、能记住事"** 的 AI 系统。它的脑子是大模型（LLM），手是工具调用（API/数据库/文件），记忆是上下文窗口+外部存储。

## 专业定义

**AI Agent（智能体）** 是一种能够**自主感知环境、制定计划、调用工具、执行行动**以实现目标的 AI 系统。其核心架构包含四个关键模块：

```
┌─────────────────────────────────────────┐
│                  Agent                    │
│  ┌─────────┐  ┌─────────┐               │
│  │  规划    │  │  记忆    │               │
│  │ Planner  │  │ Memory  │               │
│  └────┬─────┘  └────┬─────┘               │
│       │              │                     │
│  ┌────┴──────────────┴─────┐               │
│  │        LLM (大脑)        │               │
│  └───────────┬──────────────┘               │
│              │                              │
│  ┌───────────┴──────────────┐               │
│  │      工具调用 (Tool Use)   │               │
│  └──────────────────────────┘               │
└─────────────────────────────────────────┘
```

| 模块 | 作用 | 类比 |
|------|------|------|
| **LLM（大脑）** | 理解任务、推理、生成回复 | 前额叶皮层 |
| **规划（Planner）** | 拆解复杂任务为子步骤 | 制定作战计划 |
| **记忆（Memory）** | 存储短期/长期信息 | 海马体 + 笔记本 |
| **工具调用（Tool Use）** | 与外部世界交互 | 手和工具 |

## 大白话举例

### 类比：你让一个实习生去"调研竞品并写报告"

| 步骤 | 实习生做什么 | Agent 做什么 |
|------|-------------|-------------|
| 1. 理解任务 | "老板要我调研三个竞品，写一份对比报告" | LLM 解析指令 |
| 2. 制定计划 | "先查官网 → 再看评测 → 整理成表格 → 写结论" | Planner 拆解步骤 |
| 3. 执行调研 | 打开浏览器搜索、访问竞品网站、截图 | Tool Use：调用搜索引擎 API、网页抓取 |
| 4. 记录信息 | 在笔记本上记录关键数据 | Memory：存到向量数据库 |
| 5. 写报告 | 整理笔记，写成结构化文档 | LLM 汇总生成 |
| 6. 自我检查 | "再看看有没有遗漏" | Reflection：自我纠错 |

### 与传统程序的区别

| | 传统程序 | AI Agent |
|----|---------|----------|
| 执行方式 | 预设逻辑，if-else | 自主推理，动态决策 |
| 输入处理 | 结构化数据 | 自然语言 + 非结构化数据 |
| 错误处理 | 异常捕获 | 自我反思 + 重试 |
| 工具使用 | 写死的函数调用 | 动态选择工具 |
| 适应性 | 只处理预设场景 | 可处理未见过的任务 |

## 关键点

- Agent ≠ LLM。LLM 只是 Agent 的"大脑"，Agent 还需要手脚（工具）和记事本（记忆）
- Agent 的核心循环是：**观察 → 思考 → 行动 → 观察 → ...**
- 目前最成熟的 Agent 模式是 **ReAct**（推理+行动交替）
- 多 Agent 系统不是简单的"多个 Agent 聊天"，而是**有组织的分工协作**

## 反例与边界

### Agent 不是万能的

- ❌ **不是**：给一个 Agent 就能自动完成所有工作
- ✅ **是**：Agent 适合**有明确目标、可分解、需要多步推理**的任务

### 不适合用 Agent 的场景

- 单次问答（直接用 LLM 更高效）
- 需要 100% 确定性的任务（Agent 本质是概率性系统）
- 实时性要求极高的场景（Agent 多步推理有延迟）

### 常见误用

- **过度工程化**：用 Agent 框架处理一个简单的 CRUD
- **自主性过强**：让 Agent 直接操作数据库而没有任何权限限制
- **幻觉放大**：Agent 多步推理中，第一步错了后面全错

## 可行动建议

- 想理解 Agent → 先手动走一遍 ReAct 循环（用 ChatGPT 试试"请一步步思考，每步告诉我你的行动和观察"）
- 想搭建 Agent → 从 LangChain 的 AgentExecutor 开始，再进阶到 LangGraph
- 想评估 Agent → 关注三个指标：任务完成率、工具调用准确率、推理步数

## 延伸与关联

- [[ReAct推理与行动模式]] — Agent 的核心推理循环
- [[Agent工具调用机制]] — Function Calling 原理与最佳实践
- [[Agent记忆系统设计]] — 短期/长期/语义记忆实现
- [[多Agent协作模式]] — LangGraph / CrewAI / AutoGen 对比

## 来源

- Lilian Weng, "LLM Powered Autonomous Agents", 2023 — [blog](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Andrew Ng, "AI Agentic Design Patterns", 2024 — [deeplearning.ai](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Anthropic, "Building effective agents", 2024 — [docs](https://docs.anthropic.com/en/docs/build-with-claude/agent-patterns)
```

**Step 2: 验证**

- [ ] 在 Obsidian 中确认链接跳跃正常
- [ ] Frontmatter `summary` 是一句话结论而非描述
- [ ] 大白话举例部分不需要技术背景就能理解

---

## Task 3: 创建 ReAct推理与行动模式.md

**Objective:** 创建 Agent 最核心的推理模式笔记，解释 ReAct 循环原理，含代码级伪代码示例。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/ReAct推理与行动模式.md`

**Step 1: 写入笔记**

```markdown
---
title: ReAct推理与行动模式
domain: IT_Technology
tags: [概念, AI, Agent, ReAct]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "Yao et al. (2022) 'ReAct: Synergizing Reasoning and Acting in Language Models'; LangChain ReAct Agent 文档"
related: [[Agent架构全景]], [[Agent工具调用机制]], [[Agent规划与任务分解]]
summary: "ReAct 是 Agent 的核心推理循环——交替进行'思考(Thought)→行动(Action)→观察(Observation)'，直到任务完成，解决了纯推理（缺行动）和纯行动（缺推理）的各自短板"
---

# ReAct 推理与行动模式

## 一句话结论

> ReAct = **Reasoning（推理）+ Acting（行动）**。Agent 不是想完再做，也不是做完再想，而是**边想边做、做一步看一步**。

## 专业定义

ReAct 是 2022 年由 Yao 等人提出的框架，让 LLM 交替生成**推理轨迹（Thought）**和**行动（Action）**，并通过**观察（Observation）**获取反馈来指导下一步。

### 核心循环

```
Thought → Action → Observation → Thought → Action → Observation → ... → Final Answer
```

| 步骤 | 含义 | 示例 |
|------|------|------|
| **Thought** | Agent 分析当前状态，决定下一步 | "我需要先查到北京的天气" |
| **Action** | 执行具体操作（调工具/搜索/计算） | `search("北京今天天气")` |
| **Observation** | 收到行动的结果反馈 | "北京今天晴，25°C" |
| **Final Answer** | 任务完成，输出最终答案 | "北京今天晴，25°C，适合出行" |

## 大白话举例

### 场景：Agent 被要求"北京今天适合户外运动吗？"

```
第 1 轮
  Thought: 我需要先知道北京今天的天气
  Action:  调用天气 API("北京", "2026-06-15")
  Observation: {天气: "晴", 温度: 25°C, 风速: "3级", AQI: 42}

第 2 轮
  Thought: 晴、25°C、风力3级、空气质量优 → 非常适合户外运动
  Action: 无需更多查询，可以给出结论
  Final Answer: 北京今天非常适合户外运动！晴，25°C，微风，空气质量优。
```

### 对比：没有 ReAct 会怎样？

| 方式 | 过程 | 问题 |
|------|------|------|
| 纯推理（Chain of Thought） | 模型直接"推测"天气 | 可能猜错，没有真实数据 |
| 纯行动（只调 API） | 拿到天气数据但不分析 | 不会判断是否适合户外运动 |
| **ReAct** | 调 API + 分析结果 | ✅ 数据准确 + 推理正确 |

## 关键点

- ReAct 是当前绝大多数 Agent 框架的**默认推理模式**（LangChain、LlamaIndex、CrewAI 都基于此）
- 每一步的 Observation 会追加到上下文中，形成"记忆"累积
- 如果 Action 失败（超时/报错），Agent 可以在下一轮 Thought 中调整策略
- 通常设置最大步数限制（如 10 步），防止无限循环

## 反例与边界

### ReAct 的局限

- **处理简单任务时多余**：如果只是"1+1=?"，不需要 ReAct 循环
- **步数爆炸**：复杂任务可能走很多步，token 消耗大、延迟高
- **中间步骤错误传播**：一步的 Observation 如果被误解，后续全偏

### 常见误用

- 期望 Agent 在 3 步内完成所有事 → 实际可能需要 10-15 步
- 不给 Agent 设置终止条件 → 可能进入死循环

## 延伸与关联

- [[Agent规划与任务分解]] — Plan-and-Execute 模式是 ReAct 的升级版
- [[Agent工具调用机制]] — ReAct 的 Action 步骤依赖 Function Calling 实现
- [[多Agent协作模式]] — 多 Agent 系统中每个 Agent 内部也是 ReAct 循环

## 来源

- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022 — [arXiv](https://arxiv.org/abs/2210.03629)
- LangChain ReAct Agent 文档 — [docs](https://python.langchain.com/docs/modules/agents/agent_types/react)
```

**Step 2: 验证**

- [ ] Wikilink 链接目标存在
- [ ] 大白话场景不需要技术背景即可理解

---

## Task 4: 创建 Agent工具调用机制.md

**Objective:** 解释 Agent 如何调用外部工具（Function Calling），包括 JSON Schema 定义、工具选择策略。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/Agent工具调用机制.md`

**Step 1: 写入笔记**

```markdown
---
title: Agent工具调用机制
domain: IT_Technology
tags: [概念, AI, Agent, Function-Calling]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "OpenAI Function Calling 文档; Anthropic Tool Use 文档; LangChain Tools 文档"
related: [[Agent架构全景]], [[ReAct推理与行动模式]], [[Function-Calling原理]]
summary: "工具调用是 Agent 与外部世界交互的唯一通道——Agent 通过 JSON Schema 描述工具，LLM 决定何时调用哪个工具、传什么参数，执行结果返回后继续推理"
---

# Agent 工具调用机制

## 一句话结论

> 工具调用 = Agent 的"手"。LLM 本身只能生成文字，有了工具调用，它才能**查天气、搜网页、写文件、调 API、操作数据库**。

## 专业定义

**工具调用（Function Calling / Tool Use）** 是 LLM 的一项能力：模型不直接执行函数，而是输出一个**结构化的函数调用请求**（函数名 + 参数），由外部程序执行后把结果传回模型。

### 工作流程

```
1. 用户: "北京今天天气怎么样？"
2. LLM:  我无法回答，需要调用 get_weather 工具
   → 输出: { "function": "get_weather", "arguments": {"city": "北京"} }
3. 应用程序: 执行 get_weather("北京")
   → 返回: {"weather": "晴", "temp": 25}
4. LLM:  收到结果，生成最终回复
   → "北京今天晴，25°C"
```

### 工具定义示例

```json
{
  "name": "get_weather",
  "description": "获取指定城市的实时天气",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "城市名称"
      },
      "date": {
        "type": "string",
        "description": "日期，格式 YYYY-MM-DD，默认今天"
      }
    },
    "required": ["city"]
  }
}
```

## 大白话举例

### 类比：餐厅服务员

| 角色 | 餐厅场景 | Agent 场景 |
|------|---------|-----------|
| 你 | 顾客："来份宫保鸡丁" | 用户："帮我查下北京天气" |
| 服务员 | 在点餐系统上输入"宫保鸡丁" | LLM 输出 `get_weather("北京")` |
| 厨房 | 做好菜端出来 | 应用程序执行 API 调用 |
| 服务员端给你 | "您的宫保鸡丁" | LLM："北京今天晴，25°C" |

**服务员（Agent）不会做菜（不直接调用天气 API），但他知道怎么点菜（输出函数调用），厨房（外部程序）做好后端回来。**

## 关键点

- LLM **不执行**函数——它只输出"我想调用这个函数"的 JSON
- 工具描述（description）质量直接决定 Agent 能否正确选工具——描述要精确，不能模糊
- 一个 Agent 通常挂载多个工具，模型会根据任务**自动选择**调用哪个
- 工具可以串联：先搜索 → 再提取网页 → 再总结

## 反例与边界

### 不适合用工具调用的场景

- 纯文本推理（不需要外部数据）
- 工具太多（超过 20 个模型容易选错）

### 常见误用

- 工具描述写得太泛："一个查询工具" → 模型不知道什么时候用
- 参数描述不清晰：`date` 不说明格式 → 模型可能传 `"明天"` 而非 `"2026-06-16"`

## 延伸与关联

- [[ReAct推理与行动模式]] — ReAct 的 Action 步骤就是工具调用
- [[Function-Calling原理]] — OpenAI/Anthropic 的底层实现差异
- [[Agent记忆系统设计]] — 工具调用的结果如何存入记忆

## 来源

- OpenAI Function Calling Guide — [docs](https://platform.openai.com/docs/guides/function-calling)
- Anthropic Tool Use — [docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- LangChain Tools — [docs](https://python.langchain.com/docs/modules/agents/tools/)
```

**Step 2: 验证**

- [ ] 工具定义的 JSON 示例语法正确
- [ ] 餐厅类比不需要技术背景即可理解

---

## Task 5: 创建 Agent记忆系统设计.md

**Objective:** 解释 Agent 的记忆架构——短期记忆（上下文窗口）、长期记忆（向量数据库）、工作记忆（scratchpad）。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/Agent记忆系统设计.md`

**Step 1: 写入笔记**

```markdown
---
title: Agent记忆系统设计
domain: IT_Technology
tags: [概念, AI, Agent, Memory]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "MemGPT (2023); LangChain Memory 模块文档; Letta (MemGPT 商业化版本)"
related: [[Agent架构全景]], [[ReAct推理与行动模式]], [[Embedding与向量检索]]
summary: "Agent 的记忆分三层——短期记忆（对话上下文窗口，容量受限）、长期记忆（向量数据库，可持久化）、工作记忆（当前任务的中间状态），三层协同实现'记住你说过的话、记得之前的任务、不被新输入冲垮'"
---

# Agent 记忆系统设计

## 一句话结论

> Agent 的记忆就像人的记忆：有**短时记忆**（刚才说的话）、**长时记忆**（学过的知识）和**工作记忆**（正在处理的事）。没有记忆的 Agent 每次都是"金鱼"，7 秒就忘。

## 专业定义

### 三层记忆架构

```
┌─────────────────────────────────────────┐
│              Agent 记忆系统               │
│                                          │
│  ┌──────────────────┐                    │
│  │   工作记忆        │ ← 当前任务状态     │
│  │   (Scratchpad)   │   中间推理步骤     │
│  └────────┬─────────┘                    │
│           │                              │
│  ┌────────┴─────────┐                    │
│  │   短期记忆        │ ← 对话上下文窗口   │
│  │   (Short-term)   │   最近 N 条消息     │
│  └────────┬─────────┘                    │
│           │ 检索                          │
│  ┌────────┴─────────┐                    │
│  │   长期记忆        │ ← 向量数据库       │
│  │   (Long-term)    │   历史会话/知识库   │
│  └──────────────────┘                    │
└─────────────────────────────────────────┘
```

| 记忆层 | 存储位置 | 容量 | 持久性 | 用途 |
|--------|---------|------|--------|------|
| **工作记忆** | Prompt 中的 scratchpad | 极有限 | 仅当前任务 | 记录"现在做到哪一步了" |
| **短期记忆** | 上下文窗口 | 4K-200K tokens | 当前会话 | 记住本轮对话历史 |
| **长期记忆** | 向量数据库/SQLite | 近乎无限 | 持久化 | 跨会话回忆用户偏好和知识 |

## 大白话举例

### 场景：一个个人助手 Agent 和老用户的多轮对话

```
第 1 天
用户: "我叫小明，喜欢喝美式咖啡"
Agent: "记住了，小明喜欢美式"

第 2 天
用户: "帮我点杯咖啡"
Agent: "好的小明，给你点了一杯美式"  ← 用到了长期记忆！

（当前对话中）
用户: "上次你说的那个方案，再详细讲讲"
Agent: [查短期记忆找到"上次的方案"内容]  ← 用了短期记忆

（复杂任务中）
用户: "帮我做三件事：查天气、订机票、写周报"
Agent: [工作记忆中保持三个任务的进度]
       ✓ 天气已查
       → 正在订机票...
       □ 周报待写
```

### 类比：你的大脑

| 大脑 | Agent |
|------|-------|
| 刚才别人说的最后一句话 = 短期记忆 | 上下文窗口中的对话 |
| 你记得小学同学的名字 = 长期记忆 | 向量数据库中的历史记录 |
| 解一道数学题的中间步骤 = 工作记忆 | scratchpad 中的推理步骤 |

## 关键点

- **短期记忆的致命问题**：上下文窗口满了，旧信息会被截断（"忘了开头说过什么"）
- **长期记忆的核心技术**：Embedding → 向量检索 → 把相关历史"注入"到当前上下文
- **MemGPT/Letta** 是最早系统化解决 Agent 记忆问题的项目
- 记忆 ≠ 存所有东西。需要记忆管理策略：什么该记、什么该忘、怎么检索

## 反例与边界

### 常见陷阱

- ❌ 把所有对话都塞入长期记忆 → 检索噪音、token 浪费
- ❌ 只依赖短期记忆 → 跨会话完全失忆
- ❌ 记忆没有过期策略 → 存储膨胀

## 延伸与关联

- [[Embedding与向量检索]] — 长期记忆的检索技术基础
- [[RAG检索增强生成]] — RAG 本质是为 LLM 注入外部"记忆"
- [[Agent架构全景]] — 记忆是 Agent 四要素之一

## 来源

- Packer et al., "MemGPT: Towards LLMs as Operating Systems", 2023 — [arXiv](https://arxiv.org/abs/2310.08560)
- Letta (MemGPT 商业化) — [docs](https://docs.letta.com/)
- LangChain Memory 模块 — [docs](https://python.langchain.com/docs/modules/memory/)
```

**Step 2: 验证**

- [ ] 三层记忆的层次关系表达清晰
- [ ] 大白话场景连贯自然

---

## Task 6: 创建 Agent规划与任务分解.md

**Objective:** 解释 Agent 如何将复杂任务拆解为可执行的子步骤，覆盖 Plan-and-Execute、Reflection 等高级规划模式。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/Agent规划与任务分解.md`

**Step 1: 写入笔记**

```markdown
---
title: Agent规划与任务分解
domain: IT_Technology
tags: [概念, AI, Agent, Planning]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "Wang et al. (2023) 'Plan-and-Solve Prompting'; Shinn et al. (2023) 'Reflexion'; LangGraph 文档"
related: [[Agent架构全景]], [[ReAct推理与行动模式]]
summary: "Agent 的规划能力就像'先把大象装冰箱分三步'——将复杂目标拆解为可执行的子任务序列。从简单的一次性规划（Plan-and-Execute）到带自我反思的高级规划（Reflection），规划质量直接决定 Agent 能否完成长链任务"
---

# Agent 规划与任务分解

## 一句话结论

> 规划就是让 Agent **先想清楚再动手**。复杂任务不能想到哪做到哪，需要先拆成小步骤，然后一步步执行。

## 专业定义

### 三种规划模式对比

| 模式 | 流程 | 适用场景 | 代表框架 |
|------|------|---------|---------|
| **ReAct** | 思考→行动→观察，循环 | 需要实时反馈的任务 | LangChain Agent |
| **Plan-and-Execute** | 先制定完整计划 → 再逐步执行 | 目标明确、步骤可预见的任务 | LangGraph, BabyAGI |
| **Plan-Execute-Reflect** | 计划→执行→反思→修正计划→再执行 | 复杂、需要迭代修正的任务 | Reflexion, AutoGen |

### Plan-and-Execute 详解

```
Phase 1: Plan（规划）
  用户: "帮我分析竞品 A、B、C 并写对比报告"
  Planner: 
    1. 搜索竞品 A 的最新动态
    2. 搜索竞品 B 的最新动态
    3. 搜索竞品 C 的最新动态
    4. 提取每个竞品的关键信息
    5. 生成对比表格
    6. 撰写分析结论

Phase 2: Execute（执行）
  按计划顺序执行 1→2→3→4→5→6
```

### Reflection（自我反思）

```
Plan → Execute Step 1 → [检查] "这一步对吗？" 
  → ✅ 对 → Execute Step 2
  → ❌ 错 → 修正 → Execute Step 1 重新
```

## 大白话举例

### 类比例 1：搬家

| 没规划 | 有规划（Plan-and-Execute） |
|--------|--------------------------|
| 想起什么搬什么 | 1. 先列清单<br>2. 打包卧室<br>3. 打包客厅<br>4. 打包厨房<br>5. 叫搬家公司<br>6. 逐屋搬运 |

### 类比例 2：做菜

| 没反思 | 有反思（Reflection） |
|--------|---------------------|
| 按菜谱做，咸了也硬吃 | 尝一口 → "有点咸" → 加水 → 再尝 → "好了" |

## 关键点

- ReAct 适合**探索性任务**（不知道需要几步），Plan-and-Execute 适合**确定性任务**（步骤可预见）
- 规划质量和 LLM 的推理能力直接相关——模型越强，规划越靠谱
- Reflection 是让 Agent **自我纠错**的关键能力，大幅提升复杂任务成功率
- 实际生产中常混合使用：顶层用 Plan-and-Execute，每个子步骤内部用 ReAct

## 反例与边界

- **过度规划**：3 步能做完的事不要拆成 15 步
- **死板执行**：Plan-and-Execute 的缺点是中间步骤错了不会自动调整（需要 Reflection 机制）
- **规划本身就消耗 token**：小任务不划算

## 延伸与关联

- [[ReAct推理与行动模式]] — 最基础的 Agent 推理模式
- [[多Agent协作模式]] — 多 Agent 系统中"分配任务"本质也是规划
- [[AI工程-MOC]] — Agent 框架选型指南

## 来源

- Wang et al., "Plan-and-Solve Prompting", 2023 — [arXiv](https://arxiv.org/abs/2305.04091)
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", 2023 — [arXiv](https://arxiv.org/abs/2303.11366)
- LangGraph 规划模式 — [docs](https://langchain-ai.github.io/langgraph/)
```

**Step 2: 验证**

- [ ] 三种规划模式的对比表清晰直观
- [ ] 搬家/做菜类比简单易懂

---

## Task 7: 创建 多Agent协作模式.md 和 多Agent框架对比.md

**Objective:** 创建多 Agent 系统的概念笔记和框架对比笔记。

**Files:**
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/多Agent协作模式.md`
- Create: `03-Knowledge(知识层)/20-核心能力-Core_Ability/00 AI/00 概念/多Agent框架对比.md`

**Step 1: 写入 多Agent协作模式.md**

```markdown
---
title: 多Agent协作模式
domain: IT_Technology
tags: [概念, AI, Agent, Multi-Agent]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "Microsoft AutoGen (2023); LangGraph Multi-Agent 文档; CrewAI 文档"
related: [[Agent架构全景]], [[Agent规划与任务分解]], [[多Agent框架对比]]
summary: "多 Agent 系统不是让多个 AI 聊天，而是像公司一样有组织地分工——每个 Agent 有明确角色，通过消息传递协作完成单 Agent 无法独立完成的大型任务"
---

# 多 Agent 协作模式

## 一句话结论

> 单 Agent 像**一个人干活**，多 Agent 像**一个团队协作**。每个人有不同专长，通过分工配合完成更复杂的任务。

## 专业定义

多 Agent 系统（Multi-Agent System, MAS）由多个独立的 AI Agent 组成，每个 Agent 有特定角色、工具集和目标，通过**消息传递**进行协作。

### 三种协作拓扑

```
1. 顺序流水线（Sequential）
   Agent A → Agent B → Agent C
   研究员      写手      审校

2. 星型调度（Router/Orchestrator）
         ┌→ Agent B (搜索)
   调度器 ┼→ Agent C (分析)
         └→ Agent D (写作)

3. 网状讨论（Group Chat / Debate）
   Agent A ⇄ Agent B
     ⇅        ⇅
   Agent C ⇄ Agent D
```

| 拓扑 | 流程 | 适用场景 | 代表框架 |
|------|------|---------|---------|
| **顺序流水线** | 前一个的输出 = 后一个的输入 | 内容生成（调研→写作→审校） | CrewAI |
| **星型调度** | 调度器分发任务，汇总结果 | 复杂查询需多工具配合 | LangGraph Supervisor |
| **网状讨论** | Agent 自由交流、辩论、投票 | 创意发散、方案评审 | AutoGen GroupChat |

## 大白话举例

### 类比：写一本杂志

| 角色 | Agent 角色 | 做什么 |
|------|-----------|--------|
| 主编 | Orchestrator（调度器） | "这期封面是 AI 趋势，小张你负责调研，小王你写稿，小李你排版" |
| 记者 | Researcher Agent | 搜索最新 AI 新闻，整理素材 |
| 作者 | Writer Agent | 基于素材写文章 |
| 美编 | Designer Agent | 排版美化 |
| 校对 | Reviewer Agent | 检查错误、提出修改建议 |

## 关键点

- 多 Agent ≠ 更好的单 Agent。简单任务用多 Agent 反而增加延迟和成本
- 角色定义（role description）是多 Agent 系统最关键的设计——描述模糊则协作混乱
- 消息格式需要结构化（谁说的、说什么、发给谁），否则 Agent 之间会"聊跑偏"
- 多 Agent 系统中**终止条件**很重要，否则 Agent 们会没完没了地讨论

## 反例与边界

- ❌ 两个 Agent 互吹："你说得对""你也是"→ 无限循环
- ❌ 角色定义不清 → Agent A 抢了 Agent B 的活
- ❌ 过度拆分 → 3 步能完成的任务用了 5 个 Agent

## 延伸与关联

- [[多Agent框架对比]] — LangGraph / CrewAI / AutoGen 详细对比
- [[Agent架构全景]] — 单 Agent 的基础概念
- [[AI工程-MOC]] — Agent 框架选型与工程化

## 来源

- Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", 2023 — [arXiv](https://arxiv.org/abs/2308.08155)
- CrewAI 官方文档 — [docs](https://docs.crewai.com/)
- LangGraph Multi-Agent — [docs](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/)
```

**Step 2: 写入 多Agent框架对比.md**

```markdown
---
title: 多Agent框架对比
domain: IT_Technology
tags: [概念, AI, Agent, 框架对比]
status: 稳定
created: 2026-06-15
updated: 2026-06-15
source: "LangGraph/CrewAI/AutoGen 官方文档; 社区实践总结"
related: [[多Agent协作模式]], [[Agent架构全景]], [[AI工程-MOC]]
summary: "三大主流 Agent 框架各有侧重——LangGraph 重灵活可控（有状态图）、CrewAI 重角色分工（开箱即用）、AutoGen 重对话驱动（微软生态），选型取决于'控制力 vs 开发效率'的权衡"
---

# 多 Agent 框架对比

## 一句话结论

> LangGraph 是"乐高"（灵活但要多拼），CrewAI 是"预制菜"（上手快但定制度低），AutoGen 是"会议室"（适合多轮讨论）。

## 对比总表

| 维度 | LangGraph | CrewAI | AutoGen |
|------|-----------|--------|---------|
| **核心理念** | 有状态图（Graph） | 角色分工（Crew） | 对话驱动（Conversation） |
| **协作模式** | 自定义图结构 | 顺序/层级 | 群聊/辩论 |
| **灵活性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **上手难度** | 中等偏难 | 简单 | 中等 |
| **状态管理** | 内置（Checkpoint） | 需手动 | 需手动 |
| **人机协作** | 支持中断 | 有限 | 强（Human-in-loop） |
| **生态** | LangChain 生态 | 独立 | 微软 Azure 集成 |
| **适合场景** | 复杂工作流、生产环境 | 快速原型、内容生成 | 研究实验、群组讨论 |

## 选型指南

```
你的需求是什么？
  ├─ "我需要精细控制每一步" → LangGraph
  ├─ "我要快速搭一个多角色 Agent 试试" → CrewAI
  └─ "我需要 Agent 之间自由讨论+人类参与" → AutoGen
```

## 注意事项

- 三者不是互斥的，可以组合使用
- 框架更新极快（周级），选型后锁定版本
- 生产环境建议先用 LangGraph，因为其状态持久化能力是生产级的基础需求

## 来源

- LangGraph — [docs](https://langchain-ai.github.io/langgraph/)
- CrewAI — [docs](https://docs.crewai.com/)
- AutoGen — [docs](https://microsoft.github.io/autogen/)
```

**Step 3: 验证**

- [ ] 两篇笔记的 wikilink 互相关联
- [ ] 框架对比表的维度覆盖全面

---

## Task 8: 更新 AI工程-MOC.md 添加新笔记链接

**Objective:** 将新建的概念笔记链接添加到 AI 工程 MOC 中，形成知识与工程的桥梁。

**Files:**
- Modify: `03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/AI工程-MOC.md`

**Step 1: 在现有的 Agent 框架部分添加概念笔记链接**

对 `AI工程-MOC.md` 中 "### Agent 框架" 部分做 patch，在关键知识点下方添加概念笔记链接：

```markdown
### Agent 框架
- 工具调用（Function Calling / Tool Use）→ [[Agent工具调用机制]]
- 规划模式（ReAct / Plan-and-Execute / Reflection）→ [[ReAct推理与行动模式]] | [[Agent规划与任务分解]]
- 记忆管理（短期/长期/语义记忆）→ [[Agent记忆系统设计]]
- 多 Agent 协作（LangGraph / AutoGen / CrewAI）→ [[多Agent协作模式]] | [[多Agent框架对比]]
- Agent 架构全景 → [[Agent架构全景]]
```

**Step 2: 验证**

- [ ] 所有 wikilink 能正确跳转
- [ ] MOC 的 Dataview 查询无需修改（概念笔记在 Core_Ability 下而非 AI 工程子域）

---

## Task 9: 最终验证 — 全量检查

**Objective:** 逐篇检查所有新建/修改的笔记，确保规范合规。

**验证清单：**

- [ ] 每篇 frontmatter 包含：title, domain, tags, status, created, updated, source, related, summary
- [ ] `summary` 是一句话**核心结论**，而非"这篇笔记写了什么"
- [ ] `tags` 控制在 1-4 个，不使用领域标签
- [ ] 所有 `[[wikilink]]` 指向的文件名与实际一致
- [ ] 文件名不含日期、不含空格、中文用 `-` 分隔
- [ ] `AI相关概念.md` 中的 Dataview 查询路径正确
- [ ] `AI工程-MOC.md` 新增链接能正常跳转
- [ ] 每篇都有"专业定义 + 大白话举例"两层表达
- [ ] 每篇都有"来源"section，附原始文档链接
- [ ] 每篇都有"反例与边界"或"常见误用"

---

## 新增文件清单

| # | 文件 | 路径 | 类型 |
|---|------|------|------|
| 1 | `AI相关概念.md` | `Core_Ability/00 AI/00 概念/` | 修改（重写） |
| 2 | `Agent架构全景.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 3 | `ReAct推理与行动模式.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 4 | `Agent工具调用机制.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 5 | `Agent记忆系统设计.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 6 | `Agent规划与任务分解.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 7 | `多Agent协作模式.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 8 | `多Agent框架对比.md` | `Core_Ability/00 AI/00 概念/` | 新建 |
| 9 | `AI工程-MOC.md` | `01-AI全栈工程/` | 修改（追加链接） |

## 覆盖范围

- ✅ Agent 定义与架构
- ✅ ReAct 推理模式
- ✅ 工具调用机制（Function Calling）
- ✅ 记忆系统设计（三层记忆）
- ✅ 任务规划与分解（Plan/Execute/Reflection）
- ✅ 多 Agent 协作模式
- ✅ 主流框架对比（LangGraph/CrewAI/AutoGen）
- ✅ 每篇均含专业定义 + 大白话举例 + 来源

## 未覆盖（后续可扩展）

以下概念在 MOC 中已列出但本次不深度覆盖，后续按需补充：

- Token与分词、上下文窗口、Temperature、Embedding
- Transformer 架构
- System Prompt 设计、Few-shot、Function Calling 原理
- RAG 架构、模型量化、LoRA 微调

## 风险与注意事项

| 风险 | 缓解 |
|------|------|
| `00 AI` 目录放在 Core_Ability 下不完全符合 AGENTS.md 规范（AI 概念属于 IT_Technology） | 本次不调整目录结构，仅填充内容；未来可考虑将概念层笔记迁移或建立交叉链接 |
| wikilink 路径可能因中文文件夹名而失效 | Task 9 中逐个验证 |
| AI 领域快速迭代，概念可能过时 | `status` 设为 `稳定` 而非 `归档`，在 source 中标注年份，便于后续 `改进` |

---

## 执行方式

建议使用 subagent-driven-development 模式，按 Task 1→9 顺序执行。每篇笔记完成后立即验证 frontmatter 和 wikilink 正确性。
