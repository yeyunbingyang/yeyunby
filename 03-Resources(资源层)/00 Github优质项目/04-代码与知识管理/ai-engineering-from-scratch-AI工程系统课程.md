---
title: "AI Engineering from Scratch 从零AI工程"
tags: [GitHub, 开源, AI, 课程, 深度学习, Agent, MCP, 从零实现]
type: 课程
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/rohitg00/ai-engineering-from-scratch
related: []
summary: "从数学基础到自主Agent集群的435课完整AI工程课程，Python/TS/Rust/Julia四语言，每课产出可复用产物（prompt/skill/agent/MCP），19.9k Stars"
---

# AI Engineering from Scratch 从零AI工程

https://github.com/rohitg00/ai-engineering-from-scratch

## 基本信息

**类型：** 课程
**链接：** https://github.com/rohitg00/ai-engineering-from-scratch
**主页：** https://aiengineeringfromscratch.com
**适用领域：** AI 工程系统学习、从零实现、Agent 开发、MCP 协议、多 Agent 集群
**推荐程度：** ★★★★★
**Stars：** ~19.9k | Fork 3.3k
**规模：** 435 课 · 20 阶段 · ~320 小时
**语言：** Python / TypeScript / Rust / Julia
**许可证：** MIT
**作者：** Rohit Ghumare ([@ghumare64](https://x.com/ghumare64))

## 一句话

> 84% 的学生已在使用 AI 工具，但只有 18% 觉得自己能专业地使用它们——这门课就是要填补这个鸿沟。

## 是什么

AI Engineering from Scratch 是一套从数学基础到自主 Agent 集群的完整 AI 工程课程。核心理念：**每个算法都从原始数学推导开始**——反向传播、分词器、注意力机制、Agent 循环——当 PyTorch 出现时，你已经知道它在底层做了什么。

每课产出可复用产物：一个 prompt、一个 skill、一个 agent、或一个 MCP server。免费、开源、MIT、可在自己笔记本上运行。

## 课程结构（20 阶段）

```
Phase  0  环境搭建
Phase  1  数学基础（线性代数/概率/微积分）
Phase  2  机器学习基础
Phase  3  深度学习核心
Phase  4  计算机视觉       Phase 5  NLP
Phase  6  语音与音频       Phase 9  强化学习
Phase  7  Transformers
Phase  8  生成式 AI
Phase 10  LLM 从零实现
Phase 11  LLM 工程         Phase 12  多模态
Phase 13  工具与协议（MCP）
Phase 14  Agent 工程
Phase 15  自主系统
Phase 16  多 Agent 与集群   Phase 17  基础设施与生产
                            Phase 18  伦理与对齐
Phase 19  毕业项目
```

## 每课结构

```
phases/<NN>-<phase-name>/<NN>-<lesson-name>/
├── code/      可运行实现（Python / TypeScript / Rust / Julia）
├── docs/
│   └── en.md  课程讲义
└── outputs/   本课产出的 prompt / skill / agent / MCP server
```

学习循环：**阅读问题 → 推导数学 → 编写代码 → 运行测试 → 保留产物**

## 核心特点

- **从零构建**：反向传播、分词器、注意力、Agent 循环——全部从数学出发手写实现
- **四语言**：Python / TypeScript / Rust / Julia 同步覆盖
- **覆盖关键论文**：Attention Is All You Need、GPT-3、Diffusion、InstructGPT/RLHF、DPO、CoT、ReAct、MCP 协议
- **MCP + Agent 体系**：Phase 13-16 专门覆盖 MCP 协议、Agent 工程、自主系统、多 Agent 集群——与当前 AI 编程工具生态直接对应
- **产物导向**：每节课不是学完就完了，而是留下可复用的 artifact

## 适用场景

- AI 工程系统学习（从数学到生产全链路）
- Agent + MCP 开发实战（Phase 13-16）
- 团队 AI 能力建设——课程结构清晰，可 Fork 定制
- 补全「会用 AI 工具但不懂底层原理」的断层

## 评价

- **优点**：体系完整（数学→ML→DL→LLM→Agent→生产）、四语言覆盖广、每课有产出物而非纯理论、Phase 13-16 MCP+Agent 部分与当前工具链高度匹配、MIT 开源可商用
- **局限**：内容量巨大（435 课 320 小时）、全英文无中文版、需要较强的数学和编程基础
- **是否值得长期保留**：✅ 重点关注——Agent 工程和 MCP 协议部分是当前最稀缺的系统化学习资源
