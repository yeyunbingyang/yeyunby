---
title: "AirLLM 极低显存运行超大模型"
tags: [GitHub, 开源, AI, LLM, 推理, 显存优化, MoE, Python]
type: 工具
status: 待评估
created: 2026-08-12
updated: 2026-08-12
source: https://github.com/lyogavin/airllm
related:
  - "[[01-ollama-本地LLM]]"
  - "[[08-vllm-+⭐高吞吐低延迟的LLM推理和服务引擎PagedA]]"
  - "[[02-transformers-+⭐最先进的ML模型库10万+预训练模型]]"
summary: "31k⭐——用很小的显存运行远大于显存容量的大模型：同一时刻只把一层模型放 GPU，权重放 CPU/SSD 按层/专家逐步加载，用显存换时间/IO。70B 约 4GB 显存、Llama 405B 约 8GB、DeepSeek-V3 671B 约 12GB；2026 版针对 MoE 做 expert streaming。"
---

# AirLLM 极低显存运行超大模型

## 基本信息

**类型：** ML 引擎
**链接：** https://github.com/lyogavin/airllm
**Star：** ~31k

## 支持的模型

Llama（2/3/3.1/3.3/4）、Qwen（1/2/2.5/3，含 MoE 和 FP8）、DeepSeek（V2/V3/R1）、Mistral & Mixtral、Phi、Gemma、ChatGLM、Baichuan、InternLM、Yi 等。使用方式：把 Hugging Face 模型 ID 传给 `AutoModel.from_pretrained(...)`。

## 核心思路

**用很小的显存，运行远大于显存容量的大模型。** 不把整个模型一次性塞进 GPU，而是把权重放在 CPU 内存 / SSD，推理时按层或按专家逐步加载到 GPU，用"显存换时间 / IO"把超大模型跑起来。

```text
普通推理：模型权重 → 全部/大部分驻留 GPU → 逐 token 推理
AirLLM：  SSD/RAM → 加载 Layer 1 → GPU计算 → 卸载 → Layer 2 → GPU计算 → ……
```

## 解决的问题

**AirLLM 降的是 VRAM 门槛，不是模型真实资源需求。** 70B FP16/BF16 模型本身仍非常大，磁盘空间、系统内存、PCIe/SSD 带宽不会消失；AirLLM 只是让 GPU 不必同时容纳整个模型。早期卖点：**无需量化、蒸馏或剪枝，也能让 70B 在 4GB GPU 上推理。**

## 代价

最大的代价是**速度**。Dense Transformer 每生成一个 token 都要跑完整个 Transformer，加上 CPU↔GPU / SSD↔RAM↔GPU 数据搬运，IO 容易成为瓶颈。

- ✅ 适合："我就是想在自己机器上把这个超大模型跑起来"
- ❌ 不适合："高 TPS、低延迟、本地实时聊天、Agent 高频调用"

## 2026 版亮点（3.x）

- 3.0：加入 Qwen3、DeepSeek-V3、FP8、MoE 支持，重做 layer streaming
- 3.1：针对 Kimi K3 2.8T MoE 做 per-expert streaming

**MoE 特别适合这种架构**：每个 token 只激活少量 experts，可只加载当前需要的 Expert 计算后释放，而非加载整个巨大 MoE Layer。官方"2.8T 参数只占几 GB VRAM"指的是**运行时 GPU 显存占用**，不是说模型只有几 GB。

## 与同类方案定位对比

| 方案 | 优先目标 |
|---|---|
| **AirLLM** | 极低 VRAM 跑超大模型 |
| **llama.cpp** | CPU/GPU 混合 + 量化 + 消费级设备高效推理 |
| **Ollama** | 本地模型管理和使用体验 |
| **vLLM** | GPU 高吞吐服务 |
| **Transformers + Accelerate** | 通用模型加载 / offload |
| **TensorRT-LLM** | NVIDIA GPU 高性能推理 |

**选型建议**：想"体验 70B/235B/671B"用 AirLLM；想"本地部署长期使用的 Coding Agent"应优先 Qwen3/DeepSeek 蒸馏模型 + GGUF/AWQ/GPTQ + llama.cpp/Ollama/SGLang/vLLM——因为 Agent 会疯狂连续调用模型，AirLLM 的 IO/加载延迟会被不断放大。

## 安装与快速开始

```bash
pip install airllm
```

```python
from airllm import AutoModel

model = AutoModel.from_pretrained(
    "Qwen/Qwen3-32B"
)
```

官方支持 Qwen3、DeepSeek-V3、Mixtral 等多个模型族。

## 选型决策参数

选择 AirLLM / llama.cpp / Ollama / vLLM 前需明确：显卡型号 + 显存 + 内存 + SSD 容量，据此评估各方案最大可跑参数规模与速度瓶颈。
