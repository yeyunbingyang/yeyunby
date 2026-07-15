---
title: "autoresearch 自主AI研究"
tags: [GitHub, 开源, AI, Agent, 研究, Karpathy, LLM, 自主实验]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/karpathy/autoresearch
related: [[ai-engineering-from-scratch-AI工程系统课程]]
summary: "Karpathy 出品——让 AI Agent 自主运行 LLM 训练实验，修改代码→训练5分钟→评估结果→迭代，一夜跑100次实验，83.5k Stars"
---

# autoresearch 自主AI研究

https://github.com/karpathy/autoresearch

## 基本信息

**类型：** 工具（自主研究框架）
**链接：** https://github.com/karpathy/autoresearch
**适用领域：** AI 自主研究、LLM 训练优化、Agent 科研
**推荐程度：** ★★★★★
**Stars：** ~83.5k | Fork 12.1k
**语言：** Python
**许可证：** MIT
**作者：** Andrej Karpathy（前 Tesla AI 总监、OpenAI 联合创始人）

## 一句话

> 前沿 AI 研究曾经由血肉计算机在吃饭、睡觉和「组会」之间完成——那个时代已经结束了。这个仓库讲述了这一切是如何开始的。—— @karpathy, 2026年3月

## 是什么

autoresearch 是 Karpathy 的**自主 AI 研究系统**——给 AI Agent 一个小但真实的 LLM 训练环境，让它自主实验一整夜：修改代码 → 训练 5 分钟 → 检查结果是否改善 → 保留或丢弃 → 重复。你早上醒来看到一份实验日志，以及（希望）一个更好的模型。

核心理念：你不再像传统研究员那样手动改 Python 文件——你编写 `program.md` 来设定「研究组织的代码」，Agent 自主执行。一夜约 100 次实验。

## 快速开始

```bash
# 单 GPU（H100 测试通过）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run prepare.py          # 一次性：下载数据+训练分词器
uv run train.py            # 手动跑一次（5分钟），验证环境

# 启动 Agent 自主研究
# 在仓库目录下启动 Claude/Codex，提示：
"Hi have a look at program.md and let's kick off a new experiment!"
```

## 核心设计

### 三文件架构

| 文件 | 谁修改 | 内容 |
|------|--------|------|
| `prepare.py` | ❌ 不动 | 常量、数据准备、运行时工具 |
| `train.py` | 🤖 Agent 改 | GPT 模型 + Muon/AdamW 优化器 + 训练循环——全部可改 |
| `program.md` | 🧑 人改 | Agent 指令——类似轻量级 Skill |

### 关键设计决策

- **单文件修改**：Agent 只碰 `train.py`，范围可控、diff 可审阅
- **固定时间预算**：每次训练正好 5 分钟（实际 GPU 时间，不含启动编译）——约 12 次/小时，100 次/晚
- **统一指标**：`val_bpb`（validation bits per byte），越低越好，与词表大小无关，架构变更公平对比
- **自包含**：单 GPU、单文件、单指标——PyTorch + 极少量依赖

### 小算力平台调参建议

Karpathy 专门为 MacBook 等小算力写了调参指南：换 TinyStories 数据集、降 vocab_size、降 DEPTH（从 8 到 4）、用纯 "L" 窗口模式、降 TOTAL_BATCH_SIZE 到 2^14 等。

## 适用场景

- ML 研究员——用 Agent 自动探索模型架构/超参数空间
- 学习 LLM 训练——`train.py` 是 nanochat 的精简版，清晰可读
- Agent 自主科研的概念验证——Karpathy 认为这是「AI 科研取代人类」的起点
- 单 GPU 实验自动化——睡前启动，醒来收结果

## 评价

- **优点**：Karpathy 出品概念前瞻性极强、三文件极简设计优雅、5 分钟固定预算可比性强、program.md 的「人写指令→Agent 执行」范式清晰、MIT 开源
- **局限**：当前仅支持 NVIDIA GPU（社区已有 Mac/AMD fork）、5 分钟对小模型足够但对大模型实验不够、概念验证阶段尚不能替代复杂研究
- **是否值得长期保留**：✅ 重点关注——自主 AI 研究是 Agent 进化的终极形态，program.md 的「Skill 驱动 Agent 科研」范式可直接复用到本知识库
