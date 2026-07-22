# Agent 学习与 Vibe Coding 完全指南（2026年7月版）

> **整理日期**: 2026-07-22
> **版本**: v2.0（综合版 — 完整合并三大源笔记）
> **核心场景**: Codex + Claude Code + Hermes + OmniRoute 网关 + MCP 协议 + 本地部署 + 企业安全 + 团队工作流 + 零基础入门
> **策略原则**: 复杂任务 → GPT/Claude（贵但强）；日常任务 → DeepSeek/Kimi（便宜）；隐私敏感 → 本地模型（零成本）

---

## 目录

1. [核心概念全景](#一核心概念全景)
2. [CLI Agent 四剑客](#二cli-agent-四剑客)
3. [LLM 模型全景矩阵](#三llm-模型全景矩阵)
4. [本地模型部署指南](#四本地模型部署指南)
5. [联网搜索能力差异](#五联网搜索能力差异)
6. [敏感内容与合规限制](#六敏感内容与合规限制)
7. [OmniRoute 网关完全配置](#七omniroute-网关完全配置)
8. [MCP 深度解析：从 USB-C 到企业级工具链](#八mcp-深度解析从-usb-c-到企业级工具链)
9. [团队级 Agent 工作流](#九团队级-agent-工作流)
10. [Vibe Coding 实战](#十vibe-coding-实战)
11. [AI 编程零基础入门指南](#十一ai-编程零基础入门指南)
12. [Codex Desktop 完全教程](#十二codex-desktop-完全教程)
13. [Skills 深度实践](#十三skills-深度实践)
14. [Github 优质项目生态图谱](#十四github-优质项目生态图谱)
15. [中国订阅 GPT / Claude 指南](#十五中国订阅-gpt--claude-指南)
16. [价格策略与成本优化](#十六价格策略与成本优化)
17. [快速决策速查卡](#十七快速决策速查卡)
18. [附录：配置模板合集](#十八附录配置模板合集)
19. [提示词工程完全指南](#十九提示词工程完全指南)

---

## 一、核心概念全景

### 1.1 概念关系链

`
用户需求
  |
  +-- CLI Agent 层（Codex / Claude Code / Hermes / Codex Desktop）
  |     |
  |     +-- CC Switch（7+ 工具配置统一管理）
  |     |
  |     +-- OmniRoute 网关（智能路由、负载均衡、Token 压缩）
  |           |
  |           +-- MCP 协议 -> Skills/插件/工具
  |           |
  |           +-- 本地模型（Ollama / vLLM）
  |           |
  |           +-- 国内低价 API（DeepSeek / Kimi / 通义）
  |           |
  |           +-- 国外高端 API（OpenAI / Anthropic / Google）
  |
  +-- 输出（代码 / 文档 / 分析 / 自动化任务）
`

### 1.2 关键术语速查

| 术语                      | 一句话解释                                        |
| ----------------------- | -------------------------------------------- |
| **Agent**               | 能自主感知环境、决策并执行动作的 AI 系统                       |
| **LLM**                 | 大语言模型，Agent 的大脑                              |
| **MCP**                 | Model Context Protocol，AI 调用工具的 USB-C 接口标准   |
| **A2A**                 | Agent-to-Agent，Agent 之间的协作协议                 |
| **Skills**              | Agent 的技能树，可插拔的功能模块                          |
| **Vibe Coding**         | 用自然语言 vibe 出代码的开发方式                          |
| **RAG**                 | Retrieval-Augmented Generation，让 AI 查本地资料再回答 |
| **Function Calling**    | AI 主动调用你定义的函数/工具                             |
| **Constitutional AI**   | Anthropic 的宪法式安全对齐方法                         |
| **Flat-rate**           | 固定费率（订阅制），不按 Token 计费                        |
| **MoE**                 | Mixture of Experts，混合专家架构，内存跟踪总参数量           |
| **SDD**                 | Specification-Driven Development，规范驱动开发      |
| **Agentic Engineering** | 系统化的 AI 驱动开发方法论                              |
| **CC Switch**           | 多 Agent 桌面管理器                                |
| **Hermes**              | 可本地运行的成长型 AI Agent                           |

### 1.3 AI 编程发展历程

| 阶段 | 时间 | 代表产品 | 核心特征 |
|------|------|---------|---------|
| **智能补全时代** | 2020-2022 | GitHub Copilot、TabNine | 像输入法联想，下一词/下一行预测 |
| **对话编程时代** | 2023-2024 | ChatGPT、Claude、Cursor | 多轮对话生成代码，人手动复制执行 |
| **Agent 编程时代** | 2025-2026 | Codex、Claude Code、Hermes | AI 自主规划执行，读写文件跑命令，自动纠错迭代 |

**关键转折**：从 AI 辅助写代码到 Agent 自主写代码的转变，核心在于 Agent 能够执行终端命令、读写文件、安装依赖、运行测试，形成完整的感知-决策-执行闭环。

---
---|------|-----------|-----------|----------|-----------|----------|
| **Ollama** | 开发友好、一键启动 | ~62 tok/s | ~155 tok/s | Good | 极低 | 个人开发、快速验证 |
| **LM Studio** | GUI 桌面应用 | ~58 tok/s | ~140 tok/s | Good | 低 | 非技术用户 |
| **llama.cpp** | 性能引擎、底层控制 | ~71 tok/s | ~180 tok/s | Excellent | 中等 | CPU/边缘设备 |
| **vLLM** | 生产级服务 | ~71 tok/s | **~920 tok/s** | Excellent | 中等 | 团队共享、高并发 |

> 关键数据: vLLM 在 50 用户并发下可达 920 tok/s，p99 延迟约 2.8s；Ollama 同条件下约 41 tok/s。

### 4.2 本地部署模型矩阵

#### Tier 1：轻量设备（4-8GB 内存）

| 模型 | 参数量 | 内存占用 | 速度 | 上下文 | 最佳用途 |
|------|--------|----------|------|--------|----------|
| **Gemma 3 2B** | 2B | ~1.7 GB | 40-60 tok/s (CPU) | 128K | 速度优先、极低内存 |
| **Llama 3.2 3B** | 3B | ~2.5 GB | 25-45 tok/s (CPU) | 128K | 综合最佳入门 |
| **Phi-4 Mini 3.8B** | 3.8B | ~2.5 GB | 30-50 tok/s (CPU) | 128K | 低内存最强推理 |

#### Tier 2：消费级主力（8-16GB VRAM）

| 模型 | 参数量 | 显存占用 | 速度 | 上下文 | 最佳用途 |
|------|--------|----------|------|--------|----------|
| **Qwen3 8B** | 8B | ~5.2 GB | 10-18 tok/s | 32K-131K | 多语言、编程、中文首选 |
| **Llama 3.3 8B** | 8B | ~5.5 GB | 10-18 tok/s | 128K | 通用全能 |
| **DeepSeek-R1-Distill-Qwen-14B** | 14B | ~10 GB | 中等 | 128K | 推理强化、数学证明 |

#### Tier 3：工作站级（16-24GB VRAM）

| 模型 | 参数量 | 显存占用 | 速度 | 上下文 | 最佳用途 |
|------|--------|----------|------|--------|----------|
| **Qwen3-Coder 30B-A3B** | 30B (MoE) | ~18-20 GB | 中等 | 128K | 严肃编码、复杂算法 |
| **Qwen3.6 27B** | 27B | ~16-18 GB | 中等 | 128K | 平衡多模态 + Agentic |
| **DeepSeek-R1-Distill-Qwen-32B** | 32B | ~18-20 GB | 中等 | 128K | 推理最强、数学/逻辑 |

#### Tier 4：服务器级（40GB+ VRAM / 多 GPU）

| 模型 | 参数量 | 显存需求 | 架构 | 最佳用途 |
|------|--------|----------|------|----------|
| **GLM-5.2** | ~753B (MoE) | 多 GPU | 稀疏 MoE | 企业级推理、开源 |
| **Kimi K2.7** | ~1T (MoE) | 多 GPU | 稀疏 MoE | 长文本、多模态 |
| **DeepSeek V4-Pro** | ~1.6T (MoE) | 多 GPU | 稀疏 MoE | 前沿推理、接近 API 质量 |

> 关键事实: MoE 模型内存跟踪总参数量，即使每 token 只激活部分专家，所有专家权重都需驻留显存。单卡 24GB 无法运行这些模型。

### 4.3 Ollama 快速部署

`
# 安装
curl -fsSL https://ollama.com/install.sh | sh
export OLLAMA_NO_ANALYTICS=1
ollama serve

# Tier 1 (4-8GB 内存)
ollama run gemma3:2b          # 最快，1.7GB
ollama run llama3.2:3b        # 综合最佳，2.5GB
ollama run phi4-mini           # 推理最强，2.5GB

# Tier 2 (8-16GB VRAM)
ollama run qwen3:8b           # 多语言+编程，5.2GB
ollama run llama3.3:8b        # 通用全能，5.5GB

# Tier 3 (16-24GB VRAM)
ollama run qwen2.5-coder:32b  # 严肃编码，~18GB
ollama run deepseek-r1:32b    # 推理最强，~18GB
`

### 4.4 量化策略

| 量化级别 | 精度损失 | 显存节省 | 适用场景 |
|---------|---------|---------|---------|
| **Q4_K_M** | ~5-10% | 75% | 日常使用首选 |
| **Q5_K_M** | ~3-5% | 70% | 质量要求较高 |
| **Q8_0** | ~1-2% | 50% | 专业编码 |
| **AWQ** | ~2-3% | 50% | vLLM 生产环境 |

### 4.5 vLLM 生产部署

`
# docker-compose.yml
version: "3.8"
services:
  vllm:
    image: vllm/vllm-openai:latest
    ports:
      - "8000:8000"
    environment:
      - CUDA_VISIBLE_DEVICES=0
    volumes:
      - ~/.cache/huggingface:/root/.cache/huggingface
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    command: >
      --model Qwen/Qwen3-8B-AWQ
      --quantization awq
      --max-model-len 32768
      --gpu-memory-utilization 0.85
      --enable-prefix-caching
`

### 4.6 按硬件配置快速推荐

| 硬件 | 可运行模型 | 适用场景 |
|------|-----------|----------|
| 4-8GB 内存 | Gemma 3 2B, Llama 3.2 3B | 基础问答、学习实验 |
| RTX 3060 12GB | Qwen3 8B, Llama 3.3 8B | 个人编码主力 |
| RTX 4090 24GB | Qwen-Coder 32B, DeepSeek-R1 32B | 专业开发者 |
| Mac M3 Max 64GB | Qwen3.6 27B | 移动 AI 工作站 |
| Mac M3 Ultra 128GB | DeepSeek V3, 70B+ | 企业私有化 |

---

## 二、CLI Agent 四剑客

### 2.1 核心对比（2026年7月）

| 维度 | **Codex** (OpenAI) | **Claude Code** (Anthropic) | **Hermes** (Claude harness) | **Codex Desktop** (OpenAI) |
|------|-------------------|---------------------------|----------------------------|---------------------------|
| **定位** | 全自动编程 Agent | 终端协作式助手 | 本地增强版/自定义工作流 | 桌面级 AI 工作代理 |
| **交互模式** | 命令式 | 对话式 | 自动化：定时/事件驱动 | 图形界面 + 对话式 |
| **记忆能力** | 单会话，无持久记忆 | 项目级记忆，跨会话保持 | 持久记忆 + 自定义知识库 | agents.md 全局+项目规则 |
| **执行环境** | 云端 sandbox | 本地终端 | 本地 + 可扩展环境 | 本地桌面环境 |
| **底层模型** | GPT-5.3 Codex（专用） | Claude Opus 4.8 / Fable 5 | 可接多模型（含本地） | GPT-5.x 系列 |
| **本地模型支持** | 不支持 | 间接（经 OmniRoute） | 原生支持 | 不支持 |
| **上手难度** | 低 | 中（需懂终端） | 中高 | **极低（图形界面）** |
| **适用人群** | 开发者 | 开发者 | 高级用户/DevOps | **零基础到高级** |

### 2.2 场景决策树

`
开始
  |
  +-- 零基础 / 图形界面偏好？
  |     +-- YES -> Codex Desktop
  |
  +-- 需要全自动完成？
  |     +-- YES -> Codex（云端 sandbox）
  |
  +-- 需要云端审查舰队？
  |     +-- YES -> Claude Code
  |
  +-- 需要持久记忆 + 定时自动化？
  |     +-- YES -> Hermes
  |
  +-- 隐私敏感 / 完全离线？
  |     +-- YES -> Hermes + 本地 Ollama
  |
  +-- 日常协作编码 -> Claude Code（最佳平衡）
`

### 2.3 组合使用模式

| 模式 | 工具组合 | 说明 |
|------|----------|------|
| 快速出原型 | Codex -> 人工 Review | Codex 生成，人把关核心逻辑 |
| 深度维护项目 | Claude Code 长期会话 | 持续数周的协作，保持上下文 |
| 团队规范巡检 | Hermes + Cron + 本地模型 | 每天自动检查，零成本运行 |
| 复杂 Bug 攻坚 | Claude Code 深度推理 | 逐步分析，验证每个假设 |
| 完全离线开发 | Hermes + Ollama | 无网络也能编码 |
| 国内外混合 | OmniRoute 智能路由 | 自动根据环境选择最佳模型 |
| 零基础入门 | Codex Desktop 图形界面 | 无需懂终端，对话式开发 |

### 2.4 各 Agent 快速安装

| Agent | 安装命令 | 前置条件 |
|-------|---------|---------|
| **Claude Code** | [官方安装](https://claude.ai/install) / curl -fsSL https://claude.ai/install.sh | macOS/Linux/WSL 原生安装，支持 Homebrew / WinGet |
| **Codex CLI** | npm install -g @openai/codex | Node.js >= 18、OpenAI API Key |
| **Hermes** | git clone https://github.com/NickLatkovich/hermes-agent | Node.js >= 18、Ollama（可选） |
| **Codex Desktop** | 官网下载安装包 | OpenAI 账号、桌面系统 |

### 2.5 Hermes Agent 详解

Hermes 是本知识库中**最深入实践的 Agent**，拥有完整的项目实战体系：

**Hermes 实战项目一览**（共9个项目，位于 02-Agent/04-Hermes-Agent/项目实战/）：

| 项目 | 核心流程 |
|------|---------|
| 博客自动发布系统 | 草稿 -> AI 润色 -> 发布到多个平台 |
| 智能客服 Agent 系统 | 用户提问 -> FAQ 匹配 -> 人工升级 |
| CI/CD 自动化运维 Agent | 代码提交 -> 自动构建 -> 部署验证 |
| 代码审查 Agent（CodeReview） | PR 提交 -> AI 审查 -> 生成报告 |
| 社交媒体舆情监控 Agent | 关键词监控 -> 情感分析 -> 告警 |
| 个人知识库自动整理 Agent | 新笔记 -> 分类 -> 链接 -> 索引 |
| AI 内容工厂 - 多平台自媒体矩阵 | 选题 -> 生成 -> 多平台分发 |
| AI 电商商品图批量生成 Agent | 产品图 -> AI 换背景 -> 批量导出 |
| AI 短视频自动生成与发布 Agent | 脚本 -> 配音 -> 视频合成 -> 发布 |

---

## 三、LLM 模型全景矩阵

### 3.1 国外模型梯队（2026年7月）

| 模型 | 发布日期 | 定位 | 上下文 | 价格(输入/输出/1M tokens) | 核心优势 |
|------|---------|------|--------|--------------------------|---------|
| **GPT-5.6 Sol** | 2026-06-26 | OpenAI 旗舰 | 1.1M | US / US | 通用最强、Agentic 评分 81.6 |
| **Claude Fable 5** | 2026-06-09 | Anthropic 最强 | 1M | US / US | 编码、写作、自主 Agent 最强 |
| **Claude Opus 4.8** | 2026-05-22 | Claude Code 默认 | 1M | US / US | 高 Effort 模式、代码库理解 |
| **GPT-5.3 Codex** | 2026-06 | Codex 专用 | 400K | US.75 / US | 编码优化、比 5.6 便宜 2.1x |
| **Gemini 3.5 Flash** | 2026-06 | Google I/O 发布 | 1M | **免费** / ~US.50 | 免费、速度最快、多模态 |

### 3.2 国内模型梯队（2026年7月）

| 模型 | 发布日期 | 定位 | 上下文 | 价格(输入/输出/1M tokens) | 核心优势 |
|------|---------|------|--------|--------------------------|---------|
| **Kimi K3** | 2026-07-16 | Moonshot 最新旗舰 | **1M** | US / US | 2.8T 参数、多模态、开源 |
| **DeepSeek V4 Pro** | 2026-04-24 | 性价比之王 | **1M** | **US.43** / US.87 | 编码强、开源可本地部署 |
| **DeepSeek V4 Flash** | 2026-04 | 极速版 | 1M | **US.14** / US.28 | 成本最低、适合高并发 |
| **Kimi K2.6** | 2026-06 | 长文本专家 | 256K | US.95 / US.00 | 长上下文检索、中文优化 |
| **GLM-5.2** | 2026-06-13 | 智谱旗舰 | 1M | US.40 / US.75 | 开源、高/Max 推理模式 |
| **Qwen 3.7-max** | 2026-06 | 阿里旗舰 | 256K | US.50 / US.50 | Thinking 模式、工具调用 |

### 3.3 代理/路由层对比

| 工具 | 定位 | 支持的 Provider | 免费层 | 版本 |
|------|------|---------------|-------|------|
| **OmniRoute** | 智能路由+负载均衡+故障转移 | 237+ AI 提供商 | ~16亿 Token/月 | v3.8.46 |
| **CC Switch** | 多 Agent 桌面管理器 | 7+ CLI 工具 | 内置 | 最新 |
| **9Router** | 免费 AI 路由网关 | 多模型 | 免费 | 开源 |

### 3.4 场景选择矩阵

| 场景            | 国外环境                 | 国内环境              | 本地部署           | 推荐工具              |
| ------------- | -------------------- | ----------------- | -------------- | ----------------- |
| 全自动出原型        | GPT-5.3 Codex        | DeepSeek V4 Pro   | -              | Codex             |
| 复杂系统架构        | GPT-5.6 Sol          | Kimi K3           | -              | Claude Code       |
| 深度 Bug 分析     | Claude Fable 5       | DeepSeek V4 Pro   | Qwen-Coder 32B | Claude Code       |
| 代码安全审查        | Claude Fable 5       | 文心一言              | Qwen-Coder 32B | Claude Code       |
| 分析 UI 截图      | Gemini 3.5 Flash（免费） | Kimi K3           | -              | Claude Code       |
| 处理 10万+ Token | Kimi K3              | Kimi K3           | -              | Claude Code       |
| 写中文技术文档       | Kimi K3              | Kimi K3           | Qwen3 8B       | Hermes            |
| 每天自动巡检        | -                    | DeepSeek V4 Flash | Qwen3 8B       | Hermes + Cron     |
| 预算极紧日常编码      | Gemini Flash（免费）     | DeepSeek V4 Flash | Qwen3 8B       | Codex/Claude Code |
| 完全离线开发        | -                    | -                 | Qwen-Coder 32B | Hermes            |
| 隐私敏感数据处理      | -                    | -                 | Qwen-Coder 32B | Hermes            |
| 初学者学习         | GPT-5.6 Sol          | DeepSeek V4 Pro   | -              | Codex Desktop     |

---

## 四、本地模型部署指南

### 4.1 推理工具选择

| 工具 | 定位 | 单用户速度 | 50用户并发 | 内存效率 | 设置复杂度 | 最佳场景 |
|---
## 五、联网搜索能力差异

### 5.1 搜索策略差异

| 模型 | 搜索风格 | 典型行为 | 索引来源 |
|------|---------|---------|---------|
| **ChatGPT** | 发散式 | 4-5 个并行查询，追求新鲜度 | Bing 索引 |
| **Claude** | 保守式 | 1-2 个精准查询，先分解子问题 | Brave Search |
| **Gemini** | 实体式 | 3 个简洁查询 + site 操作符 | Google Search |
| **Kimi** | 覆盖式 | 1000+ 网页检索 | 中文全网 |

### 5.2 国内外环境搜索差异

| 维度 | 国外环境 | 国内环境 |
|------|---------|---------|
| **索引覆盖** | 全球互联网（英文为主） | 中文互联网生态 |
| **时效性** | 实时或近实时 | 实时（热点分钟级） |
| **信息类型** | 技术文档、学术论文、GitHub | 国内新闻、政策、电商、短视频 |
| **国外模型搜索** | 稳定 | 可能超时或失败 |

### 5.3 本地模型联网替代方案

本地模型不联网是设计特性而非缺陷。企业场景下可通过以下方式替代：

`
用户提问：最新的 React 19 特性有哪些？

云端方案：AI -> 联网搜索 -> 获取最新博客/文档 -> 回答

本地方案（企业安全）：
  AI -> MCP: vector-search -> 查询本地知识库（定期同步官方文档）
      -> MCP: fetch -> 查询预批准的内部文档站点
      -> 基于本地缓存回答

差异：信息可能滞后 1-7 天，但绝对安全、可控、可审计
`

---

## 六、敏感内容与合规限制

### 6.1 治理逻辑根本不同

| 维度 | 国外模型 | 国内模型 |
|------|---------|---------|
| **治理主体** | 厂商自主设定 | 网信办等监管机构强制执行 |
| **合规依据** | 企业使用政策 | 《生成式人工智能服务管理暂行办法》 |
| **审查机制** | Constitutional AI 安全对齐 | AI技术过滤 + 人工复审 |
| **透明度** | 部分公开 | 备案审查，不对外公开 |
| **处罚方式** | 账号限制/API封禁 | 法律责任 + 平台下架 + 行政处罚 |

### 6.2 2026年关键法规

| 法规 | 生效时间 | 核心要求 |
|------|---------|---------|
| 《人工智能生成合成内容标识办法》 | 2025-09-01 | **显式+隐式双重标识** |
| GB 45438-2025 | 2025-09-01 | 显式标识尺寸>=最短边5%，视频>=2秒 |
| 大模型备案 | 持续 | 31类安全风险，拒答率>=95%，人工审核率>=10% |
| 深度合成规定（更新版） | 2025-11 | AI音视频必须携带机器可读水印 |
| EU AI Act | 2026-08-02 | 风险分级监管，透明度义务 |
| 美国AI芯片出口管制 | 2026-05-31 | 禁止向中企境外子公司出口先进AI芯片 |
| NO FAKES法案 | 2025年底 | 联邦数字复制权，平台48小时内标注/下架 |

### 6.3 合规红线清单

| 违规行为 | 后果 |
|---------|------|
| 使用未备案境外AI工具进行商业内容生产 | 封号/行政处罚 |
| AI生成内容未标识即发布 | 最低处罚：限流30天 |
| 生成伪专业内容（无证医疗/法律建议） | 法律责任 |
| 删除/篡改AI生成内容标识 | 依法处理 |
| 训练数据含侵权素材 | 版权诉讼（赔偿可达80万） |

---

## 七、OmniRoute 网关完全配置

### 7.1 工具链定位

`
CC Switch（配置管理）-> 管理 7+ CLI 工具配置、Provider 预设、MCP 统一管理

OmniRoute（智能网关）
  -> 运行时路由决策、负载均衡、故障转移、成本监控、Token 压缩
  -> 支持 237+ AI 提供商，90+ 免费层级，~16亿免费 Token/月
  -> 内置 95 个 MCP 工具
  -> 压缩算法：RTK + Caveman，可减少 15-95% Token 消耗
  -> 版本：v3.8.46（2026-07-07）

9Router（免费替代）-> 免费 AI 路由网关，开源，适合预算极紧或学习用途
`

### 7.2 完整路由配置（含本地模型 + 企业安全版）

`yaml
# omni-route.config.yaml（2026-07 完全版）
version: "3.0"

# ========== 本地模型 Provider ==========
providers:
  ollama:
    base_url: "http://localhost:11434/v1"
    api_key: "ollama"
    models:
      - id: "qwen2.5-coder:32b"
        context: 128000
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "core"
      - id: "qwen3:8b"
        context: 131072
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "general"
    region: "local"

  vllm-local:
    base_url: "http://localhost:8000/v1"
    api_key: "local"
    models:
      - id: "qwen3-8b-awq"
        context: 32768
        cost_in: 0
        cost_out: 0
        local: true
        security_level: "internal"
    region: "local"

  # --- 国外云端 ---
  openai:
    api_key: ""
    models:
      - id: "gpt-5.6-sol"
        context: 1100000
        cost_in: 5.00
        cost_out: 30.00
        security_level: "public"
    region: "international"

  claude:
    api_key: ""
    models:
      - id: "claude-fable-5"
        context: 1000000
        cost_in: 10.00
        cost_out: 50.00
        security_level: "public"
    region: "international"

  gemini:
    api_key: ""
    models:
      - id: "gemini-3.5-flash"
        context: 1000000
        cost_in: 0.30
        cost_out: 2.50
        free_tier: true
        security_level: "public"
    region: "international"

  # --- 国内云端 ---
  deepseek:
    api_key: ""
    base_url: "https://api.deepseek.com/v1"
    models:
      - id: "deepseek-v4-pro"
        context: 1000000
        cost_in: 0.43
        cost_out: 0.87
        security_level: "general"
      - id: "deepseek-v4-flash"
        context: 1000000
        cost_in: 0.14
        cost_out: 0.28
        security_level: "general"
    region: "domestic"

  kimi:
    api_key: ""
    base_url: "https://api.moonshot.cn/v1"
    models:
      - id: "kimi-k3"
        context: 1000000
        cost_in: 3.00
        cost_out: 15.00
        multimodal: true
        security_level: "general"
    region: "domestic"

# ========== 安全路由规则 ==========
routing:
  default_strategy: "security_first"

  rules:
    # 1. 核心数据 -> 强制本地
    - name: "core-data-local-only"
      priority: 100
      condition: "data_classification == 'core' || contains_pii == true"
      action:
        target: "ollama:qwen2.5-coder:32b"
        fallback: "ollama:qwen3:8b"
      reason: "核心数据绝对本地处理，禁止出域"
      block_cloud: true

    # 2. 敏感数据 -> 本地优先
    - name: "sensitive-data-local"
      priority: 90
      condition: "data_classification == 'sensitive'"
      action:
        target: "ollama:qwen2.5-coder:32b"
        fallback: "vllm-local:qwen3-8b-awq"

    # 3. 一般数据 -> 国内云端默认
    - name: "general-data-domestic"
      priority: 70
      condition: "data_classification == 'general' || task_type == 'code_completion'"
      action:
        target: "deepseek:deepseek-v4-pro"
        fallback: "ollama:qwen3:8b"

    # 4. 公开数据 -> 可用国外高端
    - name: "public-data-international"
      priority: 60
      condition: "data_classification == 'public' && network_type == 'international'"
      action:
        target: "claude:claude-fable-5"
        fallback: "openai:gpt-5.6-sol"

    # 5. 默认 fallback
    - name: "default-local"
      priority: 1
      condition: "true"
      action:
        target: "ollama:qwen3:8b"
`

### 7.3 Web Cookie Provider 与 API Key 对比

| 维度 | **Web Cookie Provider** | **API Key Provider** |
|------|------------------------|---------------------|
| **认证方式** | 浏览器会话 Cookie | 官方开发者 API Key |
| **成本模型** | **Flat-rate**（订阅制） | **按 Token 计费** |
| **OmniRoute 成本显示** | **US\** | 按实际 Token 消耗 |
| **本地文件操作** | 不支持 | 支持（MCP） |
| **持久记忆** | 每次跨会话 | 项目级 |
| **MCP 工具调用** | 不支持 | 完整支持 |
| **稳定性** | 较低（Cookie 过期） | 较高 |
| **适用场景** | 已有订阅，轻量使用 | 生产环境、深度开发 |

---

## 八、MCP 深度解析：从 USB-C 到企业级工具链

### 8.1 一句话定义

> **MCP（Model Context Protocol）是 AI 调用外部工具的 USB-C 接口。** 它标准化了 LLM 与文件系统、数据库、API、浏览器等外部资源的连接方式，让任何符合标准的工具都能即插即用。

| 类比 | USB-C | MCP |
|------|-------|-----|
| **标准化** | 一根线连手机、电脑、显示器 | 一个协议连文件、数据库、Git、浏览器 |
| **即插即用** | 插入自动识别设备 | 配置后 AI 自动识别工具能力 |
| **厂商无关** | 不分苹果/安卓/Windows | 不分 OpenAI/Anthropic/本地模型 |
| **扩展性** | 转接头扩展更多接口 | 任意开发者可开发新 MCP Server |

### 8.2 MCP 与 A2A 的关系

`
用户请求
  |
  +-- [A2A 层] Agent 之间协作（多个 Agent 分工）
  |      -> 招聘主 Agent 委托 简历筛选 Agent 干活
  |
  +-- [MCP 层] Agent 调用工具（单个 Agent 的能力延伸）
         -> 简历筛选 Agent 通过 MCP 连接数据库查简历
`

**核心区别**：
- **MCP** = Agent 怎么调用工具（内部能力延伸）
- **A2A** = Agent 之间怎么对话（外部协作分工）

### 8.3 技术架构五层

| 层级 | 组件 | 作用 |
|------|------|------|
| **传输层** | stdio / HTTP / SSE | 数据传输通道 |
| **协议层** | JSON-RPC 2.0 | 消息格式标准 |
| **能力层** | Tools / Resources / Prompts | 三种能力抽象 |
| **应用层** | MCP Client / Server | 客户端发起请求，服务端提供工具 |
| **生态层** | Registry / Marketplace | 工具注册与发现 |

### 8.4 三种核心能力

| 能力 | 说明 | 示例 |
|------|------|------|
| **Tools** | 函数调用，AI 主动执行动作 | read_file, execute_sql, send_slack_message |
| **Resources** | 只读数据，AI 查询信息 | file://project/README.md |
| **Prompts** | 预设模板，标准化交互 | /code_review, /generate_tests |

### 8.5 MCP 的使用全流程

#### 安装 MCP Server

`ash
# npx 直接运行（无需安装）
npx -y @modelcontextprotocol/server-filesystem /path/to/your/project

# 全局安装
npm install -g @modelcontextprotocol/server-filesystem

# Python 环境
pip install mcp-server-filesystem
`

#### 配置到 Claude Desktop / Cursor

`json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "" }
    }
  }
}
`

#### AI 调用 MCP 的完整流程

`
用户：帮我读取项目根目录的 README.md
  |
  +-- AI 识别意图：需要读取文件
  +-- AI 查询可用 MCP Tools：发现 filesystem Server 有 read_file 工具
  +-- AI 生成调用请求：{ "tool": "read_file", "arguments": { "path": ".../README.md" } }
  +-- MCP Client 发送请求 -> MCP Server (filesystem)
  +-- MCP Server 读取文件 -> 返回内容
  +-- AI 接收内容 -> 生成回答
  +-- 用户看到：README.md 内容
`

### 8.6 MCP 的价值：为什么需要它

| 维度 | 无 MCP | 有 MCP | 提升 |
|------|--------|--------|------|
| **集成效率** | 10 模型 x 20 工具 = 200 个适配 | 10 + 20 = 30 个配置 | **5 倍提升** |
| **开发周期** | 2 周/工具 | 2 天/工具 | **7 倍提升** |
| **安全审计** | 分散在各处 | 统一在 MCP Server | **覆盖率 100%** |
| **故障排查** | 难以定位 | 标准化日志 | **时间缩短 80%** |

### 8.7 常用 MCP Server 分类

#### 开发工具类

| Server | 功能 | 安装命令 |
|--------|------|---------|
| **Git MCP** | 读取仓库、搜索代码、管理 PR | npx -y @modelcontextprotocol/server-git |
| **Filesystem MCP** | 读写本地文件系统 | npx -y @modelcontextprotocol/server-filesystem |
| **GitHub MCP** | Issue、PR、Code Review | npx -y @modelcontextprotocol/server-github |
| **Fetch MCP** | HTTP 请求、网页抓取 | npx -y @modelcontextprotocol/server-fetch |

#### 数据与知识类

| Server | 功能 | 安全级别 |
|--------|------|---------|
| **PostgreSQL MCP** | 连接 SQL 数据库 | **高** |
| **SQLite MCP** | 本地数据库操作 | 高 |
| **Vector Search MCP** | 语义检索向量数据库 | 高 |
| **Puppeteer MCP** | 浏览器自动化 | 中 |
| **Memory MCP** | 持久化键值存储 | 中 |

#### SaaS 集成类

| Server | 功能 |
|--------|------|
| **Slack MCP** | 发消息、读频道 |
| **Notion MCP** | 读写页面、数据库 |
| **Jira MCP** | 创建/查询任务 |
| **Figma MCP** | 设计文件访问 |
| **Google Drive MCP** | 读写文档、搜索文件 |

### 8.8 按安全级别选择

| 安全级别 | 允许的操作 | 推荐 MCP Server | 审计要求 |
|---------|-----------|----------------|---------|
| **公开级** | 只读公开文档 | fetch, filesystem(只读) | 可选 |
| **内部级** | 读取内部代码/文档 | filesystem, git, github | 记录访问日志 |
| **敏感级** | 查询数据库、调用内部 API | postgres, 自定义 API | 全量审计 |
| **核心级** | 执行命令、修改生产环境 | command(严格受限) | 双人复核 + 实时告警 |

### 8.9 企业级 MCP 权限控制

`yaml
mcp_permissions:
  roles:
    - name: "developer"
      allowed_servers: ["filesystem", "git", "github", "fetch"]
      denied_servers: ["command", "postgres"]
    - name: "dba"
      allowed_servers: ["postgres", "sqlite"]
      denied_operations: ["DELETE", "DROP", "UPDATE"]
    - name: "devops"
      allowed_servers: ["command"]
      command_whitelist: ["docker ps", "kubectl get pods", "systemctl status"]
      command_blacklist: ["rm -rf", "DROP DATABASE"]
`

### 8.10 开发自定义 MCP Server

`python
from mcp.server import Server

app = Server("my-service")

@app.tool()
async def my_tool(param1: str, param2: int = 10) -> dict:
    """Tool description: AI uses this to decide whether to call"""
    result = await your_business_logic(param1, param2)
    return {"status": "success", "data": result}

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run(transport="stdio"))
`

### 8.11 MCP 实际落地案例

**案例一：金融风控系统**
智能风控引擎通过 MCP 对接 10+ 外部数据源。风险识别准确率提升 **22%**，欺诈案件减少 **40%**。

**案例二：工业物联网**
5000+ 传感器通过边缘 MCP 节点采集数据。设备故障率降低 **28%**，故障提前 72 小时预测。

**案例三：医疗 RAG**
本地 LLM + MCP 向量检索，患者数据 **100% 本地处理**。诊断报告生成时间 < 30 秒，诊断准确率 **92%**。

**案例四：微信支付 MCP**
AI 内容平台通过 MCP 集成微信支付。付费率提升 **28%**，复购率提升 **15%**。

### 8.12 企业级 MCP 开发 Checklist

`
[ ] 1. 定义清晰的 Tool description（AI 据此决定是否调用）
[ ] 2. 参数校验（类型、范围、必填字段）
[ ] 3. 权限控制（基于角色的访问控制）
[ ] 4. 审计日志（记录每次调用）
[ ] 5. 错误处理（友好错误信息，不暴露内部细节）
[ ] 6. 速率限制（防止滥用）
[ ] 7. 数据脱敏（敏感字段不返回给 AI）
[ ] 8. 超时控制（防止长期阻塞）
[ ] 9. 健康检查（MCP Server 状态监控）
[ ] 10. 文档更新（变更时同步 Tool 描述）
`

---

## 九、团队级 Agent 工作流

### 9.1 分层 Agent 架构

`
+-------------------------------------------+
|  第一层：边缘/本地 Agent                    |
|  本地小模型处理简单查询、过滤、预处理        |
+-------------------------------------------+
|  第二层：OmniRoute 网关                     |
|  智能路由、负载均衡、故障转移               |
+-------------------------------------------+
|  第三层：云端大模型 Agent                   |
|  复杂推理、生成、审查                       |
+-------------------------------------------+
`

### 9.2 企业安全分级部署策略

`
+-----------------------------------------------+
|  核心数据区（最高安全）                         |
|  -> 本地模型 + 本地 RAG + 本地 MCP             |
|  -> 金融交易数据、患者病历、核心代码            |
|  -> 物理隔离，无网络出口                        |
+-----------------------------------------------+
|  内部数据区（高安全）                           |
|  -> 本地模型 + 内部 MCP Server                  |
|  -> 内部文档、员工信息、项目资料                |
|  -> 内网访问，受控出口                          |
+-----------------------------------------------+
|  一般数据区（中等安全）                         |
|  -> 国内云端模型（备案）+ 审计                  |
|  -> 公开文档、一般性代码、测试数据              |
+-----------------------------------------------+
|  公开数据区（低安全）                           |
|  -> 国外云端模型（按需）                        |
|  -> 开源项目、公开论文、技术调研                |
+-----------------------------------------------+
`

### 9.3 代码审查流水线

`
code_review_pipeline:
  trigger: [pull_request_opened, pull_request_updated]
  steps:
    - name: local-lint
      model: ollama:qwen2.5-coder:32b
      task: 检查代码风格、基本语法错误
    - name: security-audit
      model: claude:claude-fable-5
      task: 深度安全审查
      condition: file_type in ['auth', 'payment']
    - name: architecture-review
      model: openai:gpt-5.6-sol
      task: 跨文件架构分析
      condition: file_count > 10
    - name: generate-report
      model: kimi:kimi-k3
      task: 汇总审查结果，生成中文报告
`

### 9.4 企业安全编码工作流

`
workflow:
  name: secure-code-development

  steps:
    # Step 1: 需求理解（本地）
    - name: understand-requirement
      model: local:qwen3-coder-32b
      mcp_tools: [company-kb:search_knowledge]

    # Step 2: 架构设计（云端 fallback）
    - name: architecture-design
      model: claude:claude-fable-5
      condition: complexity == 'high'

    # Step 3: 代码实现（本地）
    - name: code-implementation
      model: local:qwen3-coder-32b
      mcp_tools: [filesystem:read_file, filesystem:write_file, git:diff]

    # Step 4: 安全审查
    - name: security-review
      model: local:qwen3-coder-32b
      fallback: claude:claude-fable-5

    # Step 5: 提交代码
    - name: commit-code
      model: local:qwen3-coder-32b
      mcp_tools: [git:commit, git:push]
      condition: test_results == 'passed' && security_report == 'clean'
`

### 9.5 数据分级处理策略

| 数据级别 | 处理方式 | 模型选择 | MCP 工具 |
|---------|---------|---------|---------|
| **核心数据** | 本地处理 | 本地模型（32B+） | 本地 MCP |
| **敏感数据** | 本地 + 脱敏 | 本地模型 | 受限 MCP |
| **内部数据** | 本地或国内 | 本地 / DeepSeek | 内网 MCP |
| **公开数据** | 国内外均可 | 任何模型 | 任意 |

### 9.6 本地 RAG 构建：企业知识库实践

> 本地模型知识截止于训练日期。RAG（检索增强生成）让本地模型能够查询企业私有知识库，弥补这一缺陷。

#### 本地 RAG 架构

`
+-----------------------------------------------+
|  索引层                                        |
|  +-- 文档加载（PDF/Word/Markdown）              |
|  +-- 文档切分（Chunk Size ~1000, Overlap 200）  |
|  +-- 向量化（bge-large-zh 本地 Embedding）      |
+-----------------------------------------------+
|  存储层（ChromaDB）                             |
|  +-- 向量数据库（本地持久化）                    |
|  +-- 语义检索（向量相似度）                      |
|  +-- 关键词检索（BM25）                         |
+-----------------------------------------------+
|  生成层（本地 LLM）                             |
|  +-- Qwen3-Coder 32B / DeepSeek-R1 32B         |
+-----------------------------------------------+
`

#### 本地 RAG 实施步骤

`ash
# Step 1: 安装本地向量数据库
pip install chromadb

# Step 2: 准备 Embedding 模型（本地）
# 下载 bge-large-zh 到本地
# https://huggingface.co/BAAI/bge-large-zh

# Step 3: 文档处理与索引
python << 'EOF'
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

loader = DirectoryLoader("/company/docs", glob="**/*.md")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
)
chunks = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="/local/models/bge-large-zh"
)

vectorstore = Chroma.from_documents(
    documents=chunks, embedding=embeddings,
    persist_directory="/company/vector_db"
)
vectorstore.persist()
EOF

# Step 4: 开发 RAG MCP Server 封装检索
`

#### 自定义 RAG MCP Server

`python
# rag_mcp_server.py
from mcp.server import Server
import chromadb
from sentence_transformers import SentenceTransformer

app = Server("company-knowledge-base")

client = chromadb.PersistentClient(path="/company/vector_db")
collection = client.get_collection("company_docs")
model = SentenceTransformer("/local/models/bge-large-zh")

@app.tool()
async def search_knowledge(query: str, top_k: int = 5) -> list[dict]:
    """Search enterprise knowledge base"""
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return [
        {"content": doc, "source": meta["source"], "score": score}
        for doc, meta, score in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]

if __name__ == "__main__":
    app.run()
`

---

### 9.5 Agent Teams 多会话编排（实验性）

Claude Code v2.1.178+ 支持 Agent Teams 模式——协调多个 Claude Code 实例作为团队协作。
一个实例作为 Team Lead 分配任务，其他 Teammate 在自己独立的上下文窗口中并行工作，且可以互相直接通信。

适用场景：并行调研、新模块开发、复杂调试、跨层协调

启用方式：设置环境变量 CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

Advisor Tool：Claude Code 还支持调用更强模型（如 Opus 4）在关键时刻做决策审核，
通过 /advisor opus 命令启用。目前 Fable 5 暂不支持作为 advisor。


## 十、Vibe Coding 实战

### 10.1 核心原则

| 原则 | 说明 | 实践方法 |
|------|------|----------|
| **意图优先** | 先描述要什么，再考虑怎么做 | 用 PRD 代替技术方案 |
| **快速迭代** | 小步快跑，即时验证 | 15 分钟一个可运行原型 |
| **人机协作** | 人类决策，AI 执行 | 你写 Prompt，AI 写代码；你 Review，AI 修复 |
| **工具链整合** | 让 AI 使用你的工具 | 配置 MCP Server 连接数据库、API、文档 |
| **规范即代码** | 把团队规范写成 AI 可读的规则 | agents.md、.cursorrules、CLAUDE.md |

### 10.2 快速构建产品规范的流程

`
1. 需求描述（自然语言）-> 2. AI 生成 PRD -> 3. 人工确认核心逻辑
        |
4. AI 生成技术方案 -> 5. 人工选择技术栈 -> 6. AI 初始化项目
        |
7. 迭代开发（AI 编码 + 人工 Review）-> 8. AI 生成测试 -> 9. 部署
`

### 10.3 5 日行动清单

| 阶段 | 任务 | 预计时间 | 产出 |
|------|------|----------|------|
| **Day 1** | 安装 Codex Desktop / Claude Code + 配置 agents.md | 30min | 有规范的 AI 开发环境 |
| **Day 2** | 注册 DeepSeek / Kimi，接入 2-3 个国产模型 | 1h | 多模型对比体验 |
| **Day 3** | 学习 Prompt 工程 + 第一天用 AI 重构旧项目 | 2h | 理解协作式编程 |
| **Day 4** | 配置 MCP Server（文件系统 + Git） | 2h | AI 能操作本地文件和代码 |
| **Day 5** | 用 Vibe Coding 方式完成一个小产品 | 4h | 完整流程体验 |

### 10.4 Prompt 模板库

**项目初始化模板：**
`
我要创建一个 [项目类型] 项目。
项目名称：[名称]
简述：[一句话描述]
技术栈：[前端框架] + [后端框架] + [数据库]
核心功能（MVP）：
1. [功能1]
2. [功能2]
3. [功能3]
请先创建项目结构和基础配置文件，暂不实现具体功能。
`

**Bug 修复模板：**
`
发现一个Bug，需要修复：
现象：[实际看到的行为]
期望：[应该是什么行为]
复现步骤：
1. [步骤1]
2. [步骤2]
错误信息：[粘贴完整的错误堆栈]
我已经尝试过：[你尝试的解决方案]
请定位问题原因并修复。
`

**代码审查模板：**
`
请对 [文件路径或范围] 进行代码审查。
审查重点：
1. 安全性（输入验证、XSS防护、SQL注入）
2. 错误处理（异常是否被正确捕获和处理）
3. 性能（是否有明显的性能问题）
4. 代码质量（可读性、命名规范、重复代码）
请按严重程度分级：Critical / Warning / Info
`

### 10.5 Vibe Coding 常见陷阱与对策

| 陷阱 | 表现 | 对策 |
|------|------|------|
| **AI 陷入修复循环** | 改一个 bug 又引入新 bug | git checkout 回退 + 重新描述需求 |
| **AI 推荐不存在的包** | 编造不存在的 npm 包名 | 先到 npmjs.com 搜索确认 |
| **对话太长 AI 遗忘** | 忘记之前的约定或上下文 | 使用 /compact 压缩上下文 |
| **AI 修改了不该改的文件** | 改到了无关模块 | Prompt 中明确指定文件范围 |
| **数据库同步问题** | AI 不知道怎么存数据库 | 用 npx prisma db push 手动同步 |

---

## 十一、AI 编程零基础入门指南

> 融合尚硅谷 AI Coding 教程精华，面向完全没有编程经验的初学者。

### 11.1 什么是 AI 辅助编程

| 维度 | 传统编程 | AI 辅助编程 |
|------|---------|------------|
| **核心技能** | 编程语言语法、算法 | 需求描述、意图表达、结果验证 |
| **人的角色** | 代码编写者 | 需求定义者 + 结果审查者 |
| **关注点** | 怎么做（How） | 做什么和为什么（What & Why） |
| **学习周期** | 数月到数年 | 数天到数周 |
| **出错时** | 自己调试代码 | 用自然语言告诉 AI 去修复 |

### 11.2 环境准备

#### 终端基础命令（5 条必会）

| 命令 | 功能 | Windows 等效 |
|------|------|-------------|
| pwd | 查看当前目录 | pwd (PowerShell) |
| ls | 列出文件 | dir |
| cd <路径> | 切换目录 | cd |
| mkdir <名称> | 创建目录 | mkdir |
| clear | 清屏 | cls |

#### 安装 Node.js

1. 访问 https://nodejs.org/，下载 LTS 版本
2. 安装（勾选 "Add to PATH"）
3. 验证：
ode -v 和 
pm -v

#### 安装 Git

1. 访问 https://git-scm.com/download/win 下载
2. 安装（一路 Next）
3. 首次配置：git config --global user.name "Your Name"
4. 配置邮箱：git config --global user.email "your.email@example.com"

#### Git 最小生存技能（6 条命令）

`
git init      # 初始化仓库（只需一次）
git status    # 查看状态
git add .     # 暂存所有修改
git commit -m "描述"  # 提交版本
git push      # 推送到远程
git pull      # 拉取更新
`

> **避坑**：在让 AI 做大的修改之前，先 git add . && git commit -m "保存当前进度"。这样即使 AI 改坏了，你也能用 git checkout . 恢复到之前的状态。这是你的后悔药。

#### 开发环境检查清单

`
[ ] Node.js 已安装，版本 >= 18
[ ] npm 已安装
[ ] Git 已安装并完成基本配置（user.name 和 user.email）
[ ] 已创建工作目录并初始化 Git
[ ] 至少一个 AI 编程工具已安装（Codex Desktop / Claude Code / Codex CLI）
`

### 11.3 学习路径总览

`
1. 理解 AI 编程原理 -> 建立认知，理解 Vibe Coding / Agentic Engineering
   |
2. 安装工具 -> Codex Desktop 或 Claude Code
   |
3. 第一个项目 -> 用自然语言搭建一个简单的 Web 应用
   |
4. 多模型体验 -> 用不同模型做同一任务，感受差异
   |
5. 工具链整合 -> 配置 MCP、Skills，让 AI 更强大
   |
6. 独立项目 -> 从零到一完成一个完整产品
`

### 11.4 五个核心学习建议

1. **动手大于阅读** — 每学一个概念，立刻打开终端实践
2. **项目驱动学习** — 带着"我要做出一个产品"的目标去学
3. **拥抱错误** — AI 会犯错，你也会犯错，这都是学习过程
4. **持续迭代** — 没有一步到位的完美，先能跑再说
5. **记录与分享** — 把踩的坑记下来，分享出去，加深理解

---

## 十二、Codex Desktop 完全教程

### 12.1 什么是 Codex Desktop

Codex Desktop 是 OpenAI 推出的桌面端 AI 编程与工作代理工具。它不是更会聊天的搜索框，而是可以在你电脑上执行任务的工作代理。相比 CLI 版本的 Codex，Desktop 版本提供了**图形界面**，适合零基础入门，也适合高级用户管理复杂工作流。

### 12.2 核心能力一览

| 能力 | 说明 |
|------|------|
| **项目文件夹访问** | 项目文件夹就是 Codex 的工作范围和主要上下文 |
| **终端命令执行** | 可以直接在本地终端中运行命令 |
| **计划模式** | 复杂任务先讨论方案，再进入执行 |
| **持久记忆** | agents.md 全局规则 + 项目规则 + 自动记忆 |
| **插件系统** | 连接部署、浏览器、代码托管等外部服务 |
| **Skills** | 把高频流程变成可复用能力 |
| **MCP** | 连接外部知识库和工具系统 |
| **自动化任务** | 定时执行固定流程 |
| **手机端远程控制** | 从手机 App 下发任务到电脑 |

### 12.3 安装与配置

1. 从 OpenAI 官网下载 Codex Desktop 安装包
2. 按照安装向导完成安装
3. 使用 OpenAI 账号登录
4. 指定项目文件夹作为工作目录
5. 编写全局 agents.md 规则

**全局 agents.md 示例：**
`markdown
- 默认使用中文回答。
- 修改文件前先说明计划。
- 重要操作前先列出影响范围。
- 文档改写时保留原意，不制造未经确认的数据。
`

### 12.4 使用技巧

| 技巧 | 说明 |
|------|------|
| **让任务描述足够具体** | 给出目标、约束、技术栈，而非模糊指令 |
| **分步授权** | 从只读操作开始，确认能力边界后再开放写权限 |
| **安装前先问清来源** | 要求 Codex 说明工具来源、影响范围、配置位置 |
| **复杂任务先计划后执行** | 让 Codex 列出步骤和风险再执行 |
| **使用 Fork 保留上下文** | 前半段讨论有价值但后面走偏时，从某条回复 Fork 出新会话 |
| **预览与批注** | 前端项目使用内置预览，边看边提修改意见 |

### 12.5 Codex Desktop vs Claude Code

| 使用场景 | 推荐选择 |
|---------|---------|
| 零基础上手、图形界面学习 | Codex Desktop |
| 深度编码、代码审查、复杂重构 | Claude Code |
| 文件整理、部署、安装工具 | Codex Desktop |
| 编写 Skills、沉淀工作流 | 两者都可以 |
| 想获得更完整的 Agent 体验 | 两者搭配使用 |

---

## 十三、Skills 深度实践

### 13.1 什么是 Skills

Skills 是 Agent 的技能树，可插拔的功能模块。在 Codex、Claude Code、Hermes 等生态中，Skills 是封装了特定能力的可复用指令集。

### 13.2 Skills 体系全景（基于本知识库）

当前知识库中已整理的 Skills 体系：

| 类别 | Skills 内容 | 目录位置 |
|------|------------|---------|
| **Claude 官方 Skills** | Obsidian 系列（Bases/CLI/Markdown/Vault） | 02-Agent/skills/Claude-Skills |
| **数据获取 Skills** | Python 爬虫、浏览器自动化、Agent 数据获取 | 02-Agent/skills/数据获取 |
| **通用 Skills** | Karpathy 四大原则、Skills 生态全景、调用机制 | 02-Agent/skills |
| **Hermes 实战 Skills** | 博客发布、智能客服、CI/CD、代码审查等 | 02-Agent/04-Hermes-Agent |
| **Codex Skills** | 插件与技能系统 | 02-Agent/02-codex |

### 13.3 常用 Skill 分类

| 分类 | Skills 名称 | 功能说明 |
|------|------------|---------|
| **效率提升** | 代码审查 Skill | 自动化 PR 审查流程 |
| **内容生成** | 博客自动发布 Skill | 从草稿到发布全自动 |
| **数据处理** | 数据获取 Skill | 从网页/API 获取数据 |
| **自动化运维** | CI/CD 自动化 Skill | 自动构建部署 |
| **知识管理** | 知识库整理 Skill | 自动分类归档笔记 |
| **创意设计** | 电商商品图生成 Skill | 批量生成产品图片 |
| **媒体制作** | 短视频自动生成 Skill | 从脚本到成片自动化 |

### 13.4 创建 Skills 的方法

**方法一：描述目标，让 AI 帮你起草**

`
我想创建一个代码审查 Skill，用于自动审查 PR。
请先和我确认输入、输出、规则和示例。
`

**方法二：先跑通真实任务，再沉淀为 Skill（更推荐）**

这种方式更推荐。因为你已经知道流程中哪些步骤有效、哪些检查必须保留，生成出来的 Skill 会更实用。

### 13.5 Karpathy 四大原则（Skills 核心指南）

| 原则 | 含义 | 在 Skills 中的应用 |
|------|------|-------------------|
| **先思考再编码** | 分析问题，列出方案，权衡后再动手 | Skill 的 prompt 中先要求分析再执行 |
| **优先简单方案** | 不要引入新框架或库，除非绝对必要 | Skill 设计从最小可用功能开始 |
| **精准手术式修改** | 只改需要改的地方，不顺手重构 | Skill 明确指定修改范围 |
| **目标驱动执行** | 每步完成后验证，测试通过才算完成 | Skill 流程中嵌入验证步骤 |

---

## 十四、Github 优质项目生态图谱

> 本章从 282 个优质开源项目中提炼出 7 个最佳组合方案，覆盖从 AI 编码到全栈开发的完整场景。

### 组合概览

| 组合 | 适用场景 | 核心项目 |
|------|---------|---------|
| [AI编码套装](#141-ai编码套装) | 日常AI辅助编程 | Codex + Claude Code + Aider + OpenCode |
| [Agent自动化套装](#142-agent自动化套装) | 定时任务工作流编排 | Hermes + ECC + Superpowers + 9Router |
| [本地RAG套装](#143-本地rag套装) | 企业知识库私有数据 | Ollama + AnythingLLM + Chroma |
| [多模型网关套装](#144-多模型网关套装) | 成本优化合规审计 | OmniRoute + CC-Switch + 9Router |
| [浏览器自动化套装](#145-浏览器自动化套装) | 数据采集E2E测试 | Playwright + agent-browser + MediaCrawler |
| [全栈开发套装](#146-全栈开发套装) | 从0到1构建应用 | Next.js + FastAPI + Prisma + Vercel AI SDK |
| [AI内容创作套装](#147-ai内容创作套装) | 视频设计文案生成 | MoneyPrinter + ComfyUI + Remotion |

### 14.1 AI编码套装

开发者的每日AI编程工具箱。

| 项目 | 定位 | 安装命令 |
|------|------|---------|
| Codex (OpenAI) | 全自动编程Agent | npm install -g @openai/codex |
| Claude Code (Anthropic) | 终端协作式助手 | curl -fsSL https://claude.ai/install.sh |
| Aider | AI结对编程(Git原生) | pip install aider-chat |
| OpenCode | 开源编程Agent(多模型) | pip install opencode |

适用场景: 日常编码、Bug修复、代码重构。Codex适合一键生成，Claude Code适合逐步协作调试。

### 14.2 Agent自动化套装

定时任务和工作流编排。

| 项目 | 定位 | 安装方式 |
|------|------|---------|
| Hermes Agent | 本地自托管AI代理 | git clone + docker compose |
| ECC | Agent全套配置系统 | git clone + skills配置 |
| Superpowers | Agent开发方法论 | fork + 自定义指令集 |
| 9Router | 免费AI路由网关 | pip install 9router |

适用场景: 每日代码审查、定时舆情监控、自动博客发布、CI/CD流水线。

### 14.3 本地RAG套装

企业知识库+私有数据的本地化方案。

| 项目 | 定位 | 安装命令 |
|------|------|---------|
| Ollama | 一键运行本地模型 | ollama pull llama3 |
| AnythingLLM | 私有ChatGPT替代品 | docker run |
| Chroma | 轻量向量数据库 | pip install chromadb |
| Open WebUI | ChatGPT风格WebUI | docker run |

适用场景: 企业内部知识库、私有文档检索、离线问答系统。

### 14.4 多模型网关套装

企业级成本优化与合规审计。

| 项目 | 定位 | 安装方式 |
|------|------|---------|
| OmniRoute | 236供应商AI网关 | docker compose up |
| CC-Switch | Claude Code模型管理器 | pip install cc-switch |
| 9Router | 免费AI路由 | pip install 9router |

适用场景: 企业API成本控制、多供应商fallback、合规审计日志。

### 14.5 浏览器自动化套装

数据采集与E2E测试。

| 项目 | 定位 | 安装命令 |
|------|------|---------|
| Playwright | E2E自动化测试 | npm install playwright |
| agent-browser | AI浏览器自动化CLI | pip install agent-browser |
| MediaCrawler | 多平台爬虫 | pip install media-crawler |
| OpenCLI | 网站CLI桥接工具 | npm install -g opencli |

适用场景: Web应用测试、多平台数据采集、网站操作自动化。

### 14.6 全栈开发套装

从0到1构建AI应用。

| 项目 | 定位 | 安装命令 |
|------|------|---------|
| Next.js | React全栈框架 | npx create-next-app |
| FastAPI | Python高性能后端 | pip install fastapi |
| Prisma | 数据库ORM | npm install prisma |
| Vercel AI SDK | AI应用前端SDK | npm install ai |

适用场景: 快速原型到生产部署、AI应用前后端全链路。

### 14.7 AI内容创作套装

视频、设计、文案AI生成。

| 项目 | 定位 | 安装方式 |
|------|------|---------|
| MoneyPrinter Turbo | AI短视频生成 | pip install money-printer |
| ComfyUI | StableDiffusion工作流 | git clone + 下载模型 |
| Remotion | React视频编程框架 | npm init video |
| voicebox | 语音克隆合成 | pip install voicebox |

适用场景: 社交媒体内容生产、产品营销视频、品牌视觉设计。

---

### 14.8 Top 10 必装工具

| 项目 | 推荐理由 |
|------|---------|
| Ollama | 一键运行本地模型，入门必备 |
| vLLM | 生产级高性能推理引擎 |
| Dify | 可视化LLM应用开发平台 |
| Playwright | 最成熟的E2E自动化测试 |
| ripgrep (rg) | 史上最快的代码搜索 |
| lazygit | 终端Git可视化 |
| markitdown | 文档格式转换利器 |
| Open WebUI | ChatGPT风格的自托管WebUI |
| ComfyUI | 节点式Stable Diffusion工作流 |
| Chroma | 最轻量的本地向量数据库 |

---
## 十五、中国订阅 GPT / Claude 指南


### 15.1 前置条件

| 条件 | ChatGPT | Claude |
|------|---------|--------|
| **网络** | 稳定海外 IP | 稳定海外**住宅** IP（更严格） |
| **邮箱** | Gmail/Outlook 等海外邮箱 | Gmail/Outlook 等海外邮箱 |
| **支付方式** | 境外信用卡 / 虚拟卡 / 礼品卡 | 境外信用卡 / 美区 Apple ID / 虚拟卡 |
| **手机号** | 部分需验证 | 网页版不需要，API 需境外手机号 |

### 15.2 ChatGPT 订阅方法

| 方法 | 路径 | 优点 | 缺点 |
|------|------|------|------|
| **官网直付** | chat.openai.com -> Upgrade | 最稳定 | 需境外信用卡 |
| **iOS App 内购** | 美区 Apple ID -> App 内订阅 | 绕过网页风控 | 仅限 iOS |
| **礼品卡充值** | 购买 OpenAI 礼品卡 -> 兑换 | 无需信用卡 | 渠道有限 |

### 15.3 Claude 订阅方法

| 方法 | 路径 | 优点 | 缺点 |
|------|------|------|------|
| **官网直付** | claude.ai -> Settings -> Billing | 功能最全 | 需住宅 IP + 境外卡 |
| **美区 Apple ID** | App 内订阅 Pro/Max | 绕过部分风控 | 需美区账号 |
| **第三方代充** | 选择可信服务商 | 无信用卡可用 | 需谨慎选择 |

### 15.4 Claude Pro vs Max

| 功能 | Pro (US/月) | Max (US/月) |
|------|-------------|---------------|
| 模型访问 | Opus 4 / Sonnet 4 全线 | 所有模型 + 优先新模型 |
| Claude Code | 可用 | 可用，用量大幅提升 |
| Extended Thinking | 基础 | 更长推理链 |
| Projects 知识库 | 基础容量 | 更大容量 |

### 15.5 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| "Your card was declined" | 卡发行地区受限 | 换境外卡或 Apple 内购 |
| "Unable to verify" | IP 被识别为数据中心 | 换住宅 IP |
| "Service not available" | 账号注册地或 IP 不匹配 | 保持 IP 与注册时一致 |

---

## 十六、价格策略与成本优化

### 16.1 三层价格模型

`
+-----------------------------------------------------------+
|  第一层：本地模型（US）                                   |
|  -> Ollama + Qwen-Coder 32B / DeepSeek-R1 32B             |
|  -> 日常编码、简单问答、隐私敏感、完全离线                   |
+-----------------------------------------------------------+
|  第二层：国内低价（US-20/月）                             |
|  -> DeepSeek V4 Pro (US.43/1M) / Kimi K3 (US/1M)      |
|  -> 中文处理、长文本、常规开发、国内网络稳定                 |
+-----------------------------------------------------------+
|  第三层：国外高端（US-200/月，按需）                     |
|  -> Claude Fable 5 (US/1M) / GPT-5.6 Sol (US/1M)     |
|  -> 复杂架构、安全审计、跨文件重构、最终审查                 |
+-----------------------------------------------------------+
`

### 16.2 月度成本预估

| 用户类型 | 本地模型 | 国内低价 | 国外高端 | 月度总计 |
|----------|---------|---------|---------|---------|
| **个人学习者** | 80% | 15% | 5% | US-15 |
| **个人开发者** | 60% | 30% | 10% | US-50 |
| **专业开发者** | 40% | 40% | 20% | US-150 |
| **小团队 (5人)** | 50% | 35% | 15% | US-500 |

### 16.3 一句话策略

> **简单任务本地跑，中文任务 DeepSeek，复杂任务 Claude，紧急任务 GPT，省钱就用 Gemini Flash**

---

## 十七、快速决策速查卡

### 17.1 按任务类型

| 你要做什么 | 首选模型 | 环境 | 工具 |
|-----------|---------|------|------|
| 全自动出原型 | GPT-5.3 Codex | 云端 | Codex |
| 复杂系统架构 | Claude Fable 5 / GPT-5.6 | 云端 | Claude Code |
| 深度 Bug 分析 | Claude Fable 5 | 云端 | Claude Code |
| 代码安全审查 | Claude Fable 5 | 云端 | Claude Code |
| 分析 UI 截图 | Gemini 3.5 Flash（免费） | 云端 | Claude Code |
| 写中文技术文档 | Kimi K3 | 云端/国内 | Hermes |
| 每天自动巡检 | DeepSeek V4 Flash / 本地 | 国内/本地 | Hermes + Cron |
| 预算极紧日常编码 | Gemini Flash / DeepSeek Flash | 均可 | Codex/Claude Code |
| 完全离线开发 | Qwen-Coder 32B | 本地 | Hermes |
| 隐私敏感数据处理 | Qwen-Coder 32B | 本地 | Hermes |
| 快速轻量查询 | Gemini 3.5 Flash（免费） | 均可 | 任意 |
| 零基础入门 AI 编程 | GPT-5.6 / DeepSeek V4 Pro | 云端 | Codex Desktop |

### 17.2 按网络环境

| 网络情况 | 推荐策略 |
|---------|---------|
| 稳定国外代理 | Claude Fable 5 默认，复杂任务上 GPT-5.6 |
| 代理不稳定 | OmniRoute 混合：国内默认，国外 fallback |
| 纯国内网络 | DeepSeek V4 Pro 默认，长文本切 Kimi |
| 企业合规要求 | 文心/通义/智谱（备案完整） |
| 完全离线 | DeepSeek 本地部署 + Ollama |

### 17.3 按成本敏感度

| 预算 | 推荐组合 |
|------|---------|
| 不差钱 | OpenAI + Claude API Key |
| 中等 | OmniRoute 智能路由：DeepSeek 默认，复杂任务 fallback 国外 |
| 极紧 | Gemini Flash（免费）+ DeepSeek V4 Flash |
| 已有订阅 | Web Cookie Provider（ChatGPT Plus/Grok SuperGrok） |
| 零成本 | 纯本地 Ollama |

### 17.4 按硬件配置

| 硬件 | 可运行模型 | 适用场景 |
|------|-----------|----------|
| 4-8GB 内存 | Gemma 3 2B, Llama 3.2 3B | 基础问答、学习实验 |
| RTX 3060 12GB | Qwen3 8B, Llama 3.3 8B | 个人编码主力 |
| RTX 4090 24GB | Qwen-Coder 32B, DeepSeek-R1 32B | 专业开发者 |
| Mac M3 Max 64GB | Qwen3.6 27B | 移动 AI 工作站 |
| Mac M3 Ultra 128GB | DeepSeek V3, 70B+ | 企业私有化 |

---

## 十八、附录：配置模板合集

### A.1 环境变量模板

`
# .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=sk-...
KIMI_API_KEY=sk-...
GEMINI_API_KEY=...

# OmniRoute 代理配置（国内环境）
OMNIROUTE_PROXY=http://127.0.0.1:7890
OMNIROUTE_PROXY_BYPASS=localhost,127.0.0.1
`

### A.2 .cursorrules 示例

`
# .cursorrules (Cursor 项目规范)
## 角色
你是一位全栈开发专家，擅长 React + TypeScript + Node.js。

## 代码规范
- 使用函数式组件，避免 class
- 所有 API 调用使用统一的 error handling 模式
- 注释使用中文，代码使用英文

## 文件组织
- 组件放在 src/components/
- 工具函数放在 src/utils/
- 类型定义放在 src/types/

## 禁止事项
- 不要生成未使用的 import
- 不要使用 any 类型
`

### A.3 CC Switch 配置要点

`
providers:
  - name: openai
    api_key: ""
  - name: anthropic
    api_key: ""
  - name: deepseek
    api_key: ""
    base_url: https://api.deepseek.com
  - name: kimi
    api_key: ""
    base_url: https://api.moonshot.cn

mcp_servers:
  - name: filesystem
    command: npx
    args: [-y, @modelcontextprotocol/server-filesystem, /path/to/project]
  - name: git
    command: uvx
    args: [mcp-server-git, --repository, /path/to/repo]
`

### A.4 完整工具链架构图

`
用户
  |
  +-- CC Switch（配置管理）
  |     -> 统一管理 7+ CLI 工具配置
  |     -> Provider 预设
  |     -> MCP Server 安装
  |
  +-- CLI Agent 层
  |     +-- Codex（全自动/云端）
  |     +-- Claude Code（协作式/云端）
  |     +-- Hermes（自动化/本地+云端）
  |     +-- Codex Desktop（图形界面/零基础）
  |
  +-- OmniRoute 网关
        +-- 智能路由（本地/国内/国外）
        +-- 负载均衡（成本/速度/质量优先）
        +-- Token 压缩（RTK + Caveman）
        +-- 故障转移（多级 fallback）
        +-- 成本监控（日限额告警）
        |
        +-- 本地模型层
        |     +-- Ollama（个人开发）
        |     +-- vLLM（团队共享）
        |
        +-- 国内低价层
        |     +-- DeepSeek V4 Pro/Flash
        |     +-- Kimi K3
        |     +-- 通义/文心/智谱
        |
        +-- 国外高端层
              +-- Claude Fable 5 / Opus 4.8
              +-- GPT-5.6 Sol / GPT-5.3 Codex
              +-- Gemini 3.5 Flash/Pro
`

### A.5 命令速查表

**Claude Code 命令速查：**

| 命令 | 功能 |
|------|------|
| claude | 启动交互式会话 |
| claude -p "prompt" | 单次执行模式 |
| /model | 查看/切换模型 |
| /compact | 压缩上下文 |
| /clear | 清空对话 |
| /memory | 管理记忆 |
| /cost | 查看费用 |
| /review | 代码审查 |
| /init | 初始化 CLAUDE.md |

**Git 命令速查：**

| 命令 | 功能 |
|------|------|
| git init | 初始化仓库 |
| git status | 查看状态 |
| git add . | 暂存所有修改 |
| git commit -m "msg" | 提交 |
| git push | 推送到远程 |
| git pull | 拉取远程更新 |
| git checkout . | 撤销所有未提交的修改 |

**npm 命令速查：**

| 命令 | 功能 |
|------|------|
| npm init -y | 初始化项目 |
| npm install <包名> | 安装依赖 |
| npm install -g <包名> | 全局安装 |
| npm run dev | 启动开发服务器 |
| npm run build | 构建项目 |

### A.6 MCP Server 完整速查表

| 类别 | Server 名称 | 安装命令 | 安全级别 |
|------|------------|---------|---------|
| **文件系统** | filesystem | npx -y @modelcontextprotocol/server-filesystem | 低 |
| **Git** | git | npx -y @modelcontextprotocol/server-git | 中 |
| **GitHub** | github | npx -y @modelcontextprotocol/server-github | 中 |
| **数据库** | postgres | npx -y @modelcontextprotocol/server-postgres | **高** |
| **数据库** | sqlite | npx -y @modelcontextprotocol/server-sqlite | **高** |
| **网络** | fetch | npx -y @modelcontextprotocol/server-fetch | 中 |
| **浏览器** | puppeteer | npx -y @modelcontextprotocol/server-puppeteer | 中 |
| **搜索** | brave-search | npx -y @modelcontextprotocol/server-brave-search | 低 |
| **Slack** | slack | npx -y @modelcontextprotocol/server-slack | 中 |
| **命令** | command | 自定义 | **极高** |
| **向量检索** | vector-search | 自定义 | **高** |

### A.7 常见问题排查指南

| 类别 | 问题 | 解决方案 |
|------|------|---------|
| **安装** | npm install -g 报权限错误 | macOS: 前加 sudo；Windows: 管理员运行 |
| **安装** | 下载超时 | npm config set registry https://registry.npmmirror.com |
| **连接** | Invalid API Key (401) | 检查 Key 是否完整复制 |
| **连接** | 网络超时 | 国内用户使用中转服务或国产模型 |
| **连接** | Rate limit exceeded | 等待1分钟后重试，或升级 API 套餐 |
| **使用** | AI 修改了不该改的文件 | Prompt 中明确指定文件范围，或 git checkout 回退 |
| **使用** | AI 陷入修复循环 | git checkout 回退 + /clear 清空对话 + 重新描述需求 |
| **使用** | 对话太长 AI 遗忘 | 使用 /compact 压缩上下文 |
| **使用** | AI 推荐不存在的 npm 包 | 先到 npmjs.com 搜索确认包是否存在 |
| **费用** | 不确定花了多少钱 | 使用 /cost 查看当前会话费用 |
| **费用** | 想控制费用 | 简单任务用 Haiku/DeepSeek；设置月度预算 |
| **项目** | 数据库报错 | 运行 npx prisma db push 同步数据库 |
| **项目** | 端口被占用 | 杀掉占用端口的进程，或在命令中指定其他端口 |

### A.8 术语表

| 英文术语 | 中文释义 | 简要说明 |
|---------|---------|---------|
| AI-Assisted Programming | AI辅助编程 | 使用AI工具帮助编写代码 |
| Agent | 智能体 | 能自主执行任务的AI系统 |
| Agentic Engineering | 智能体工程化 | 系统化的AI驱动开发方法论 |
| API | 应用程序接口 | 程序之间通信的规则 |
| API Key | API密钥 | 访问AI服务的身份凭证 |
| CLI | 命令行界面 | 通过文字命令操作电脑 |
| Context Window | 上下文窗口 | AI一次能处理的最大内容量 |
| CRUD | 增删改查 | Create/Read/Update/Delete |
| Hallucination | 幻觉 | AI编造不存在的信息 |
| IDE | 集成开发环境 | 编写代码的专业软件 |
| LLM | 大语言模型 | 如Claude、GPT等AI模型 |
| MCP | 模型上下文协议 | AI工具的扩展能力标准 |
| MVP | 最小可行产品 | 只包含核心功能的第一个版本 |
| PRD | 产品需求文档 | 描述产品做什么的文档 |
| Prompt | 提示词 | 给AI的指令/问题 |
| RAG | 检索增强生成 | 结合搜索和AI生成的技术 |
| SDD | 规范驱动开发 | 先写规范再让AI执行的方法 |
| Skill | 技能 | 封装的可复用AI指令集 |
| Token | 令牌 | AI处理文本的基本单位 |
| Vibe Coding | 氛围编程 | 凭感觉和意图驱动的AI编程方式 |

## 十九、提示词工程完全指南

> Prompt Engineering 是与AI高效沟通的核心技能。本章覆盖从System Prompt到Skills的完整知识体系。

### 19.1 System Prompt 结构设计

一个好的 System Prompt 包含三个要素：

| 要素 | 说明 | 示例 |
|------|------|------|
| 角色定位 | 告诉AI它是什么角色 | "你是一位资深Python工程师" |
| 行为约束 | 规定AI怎么做 | "始终保持代码简洁，添加中文注释" |
| 输出规范 | 规定输出格式 | "输出JSON格式，包含以下字段" |

设计原则：
- 角色定位越具体,输出质量越高（"资深Python工程师" > "程序员" > "助手"）
- 约束用否定式：告诉AI不要做什么（"不要引入外部依赖"）
- 输出规范越明确越少幻觉

### 19.2 Task Prompt 精确度

一个有效的 Task Prompt 应包含四要素：

| 要素 | 说明 | 反例 | 正例 |
|------|------|------|------|
| 目标 | 你要什么 | "帮我写个函数" | "写一个读取CSV返回平均值的Python函数" |
| 上下文 | 相关背景信息 | 无 | "输入第一行是列名，数值可能含空值" |
| 约束 | 边界条件 | 无 | "Python 3.10+，仅标准库，无需异常处理" |
| 格式 | 期望输出 | 无 | "输出函数定义+一个使用示例" |

### 19.3 Chain-of-Thought 策略

引导AI逐步推理的三个技巧：

1. Step-by-Step：直接要求"请逐步分析"
2. Few-shot示例：给2-3个问题+答案样例
3. 结构化输出：先分析再回答（"列出关键点，然后给出结论"）

示例：
``
请逐步分析这段代码的时间复杂度：
1. 先列出每个循环的复杂度
2. 分析递归调用深度
3. 给出最终结论
``

### 19.4 常见陷阱与反模式

| 陷阱 | 说明 | 改进方式 |
|------|------|---------|
| 过于模糊 | "帮我写个网站" | "帮我写一个待办管理React组件" |
| 目标堆积 | 一个请求放5件事 | 拆分为多个子任务逐步完成 |
| 缺乏迭代 | 一次结果不满意就放弃 | 用AI结果做起点，逐步精化 |
| 忽略上下文 | 新任务不告诉前置条件 | 显式提供文件和项目上下文 |

### 19.5 从 Prompt 到 Skill

当重复使用同一组 Prompt 时,将其封装为 Skill（SKILL.md）。

Skill 设计规范：
- 明确的触发条件
- 结构化的步骤模板
- 可控的参数化变量
- 带示例的输出格式

参考：[[../../02 工具链/00 基础设施/skills/03-通用skills最佳实践.md|通用skills最佳实践]]

### 19.6 四层提示词策略

| 层级 | 用途 | 工具 | 示例 |
|------|------|------|------|
| 系统层 | 全局行为设定 | AGENTS.md / CLAUDE.md | 角色、约束、偏好 |
| 任务层 | 单次执行指令 | Prompt | 具体任务定义 |
| 技能层 | 可复用指令包 | SKILL.md | 代码审查Skill |
| 规则层 | 临时行为调整 | 自然语言 | "请用中文回答" |

---

> **维护建议**: 本笔记涉及技术快速迭代领域，建议每月回顾一次模型更新（关注 OpenAI/Anthropic/Google/DeepSeek/Moonshot 官方发布），每季度更新一次 OmniRoute 配置和合规法规变化。

> **核心总结**: MCP 是 AI 的手脚，让 Agent 能够操作文件、查询数据库、调用 API；本地 RAG 是 AI 的记忆，让本地模型能够访问企业私有知识；两者结合 = 企业级安全 Agent：数据不出域、操作可审计、权限可控制。云端模型作为外脑，仅在处理公开数据或复杂架构设计时 fallback 调用。

> **对初学者**: 从 Codex Desktop 图形界面开始，先用自然语言描述需求体验 AI 编程的威力；掌握后再切换到 Claude Code 终端模式，深入控制；最后配置 OmniRoute + 本地模型，完成全栈自动化。先能跑，再做好。

> **对本知识库读者**: 本指南融合了 01 AI工具/ 目录下的 200+ 篇笔记，以及 00 Github优质项目/ 目录下的 300+ 精选开源项目。如需深入了解特定 Agent 或工具，请参阅对应目录的详细笔记。

