---
title: AI工程 MOC
domain: IT_Technology
tags: [MOC, AI, LLM, RAG, Agent]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "AI工���子域地图，覆盖模型调用、Prompt工程、RAG架构、Agent框架与模型部署"
---

# AI 工程

将 AI 能力（尤其是大语言模型）集成到生产系统的工程实践，核心是"让模型稳定可靠地解决实际问题"。

## 学习路径

`API 调用基础` → `Prompt 工程` → `RAG 架构` → `Agent 框架` → `微调与模型部署`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| Token | LLM 处理文本的最小单位，约 0.75 词/汉字 |
| 上下文窗口 | 模型单次可处理的最大 token 数量 |
| Temperature | 控制生成随机性，越低越确定，越高越发散 |
| Embedding | 将文本映射到向量空间以计算语义相似度 |
| RAG | 检索增强生成，在推理时注入外部知识库 |
| Agent | 具备规划、工具调用、记忆能力的自主 AI 系统 |

## 关键知识点

### Prompt 工程
- 角色设定与系统提示（System Prompt）设计
- 少样本提示（Few-shot）与思维链（CoT）
- 结构化输出（JSON mode / Function calling）
- Prompt 注入攻击与防护
- 提示词版本管理

### RAG 架构
- 文档切分策略（固定大小/语义/层级）
- 向量数据库选型（Chroma/Pinecone/Weaviate/Milvus）
- 检索策略（相似度/关键词混合/重排序 Rerank）
- 上下文压缩与摘要
- 评估指标（RAGAS / TruLens）

### Agent 框架
- 工具调用（Function Calling / Tool Use） → [[Agent工具调用机制]]
- 规划模式（ReAct / Plan-and-Execute / Reflection） → [[ReAct推理与行动模式]] | [[Agent规划与任务分解]]
- 记忆管理（短期/长期/语义记忆） → [[Agent记忆系统设计]]
- 多 Agent 协作（LangGraph / AutoGen / CrewAI） → [[多Agent协作模式]] | [[多Agent框架对比]]
- Agent 架构全景 → [[Agent架构全景]]
- 工具链：LangChain / LlamaIndex

### 模型调用与 API
- OpenAI / Anthropic / Gemini API 差异
- 流式输出（Streaming）与异步调用
- 费用控制与 Token 计数
- 提示词缓存（Prompt Caching）

### 微调与部署
- LoRA / QLoRA 参数高效微调
- GGUF / ONNX 量化格式
- 本地部署（Ollama / vLLM / llama.cpp）
- 推理优化（KV Cache / 连续批处理）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/05-AI工程"
WHERE file.name != "AI工程-MOC"
SORT updated DESC
```
