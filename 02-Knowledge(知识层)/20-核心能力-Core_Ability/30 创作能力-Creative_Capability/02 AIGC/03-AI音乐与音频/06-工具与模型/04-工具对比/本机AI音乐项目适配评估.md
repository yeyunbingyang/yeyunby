---
title: 本机AI音乐项目适配评估
domain: Core_Ability
tags: [AI音乐, 本地部署, 硬件选型]
status: 稳定
created: 2026-08-11
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
source: "ACE-Step v1.5、Stable Audio 3、AudioCraft、Magenta RealTime 官方仓库"
related:
  - "[[本地模型部署分层-2026]]"
  - "[[配乐生成-本机项目选型]]"
  - "[[AI音乐音频任务选型矩阵-2026]]"
summary: "针对当前 Windows + RTX 4060 Laptop 8GB，优先验证 ACE-Step v1.5 2B 与 Stable Audio 3 Medium/Small，避免强行部署 XL、MusicGen Medium 或 Magenta RealTime 本地大显存路线。"
---

# 本机 AI 音乐项目适配评估（2026-08-17 校正版）

## 当前硬件结论

目标硬件：Windows + RTX 4060 Laptop 8GB 级显存。

### 第一主线：ACE-Step v1.5

ACE-Step 官方当前给出了明确 GPU tier。对于 **6–8GB VRAM**，推荐路线是：

```text
DiT: 2B turbo
LM: 0.6B
LM backend: PyTorch
批次: 1
显存紧张时：INT8 + CPU offload
```

因此当前机器继续把 ACE-Step v1.5 2B 作为“完整歌曲 / Cover / 长结构”首选是合理的。

### 第二主线：Stable Audio 3

2026 的 Stable Audio 3 已把模型分成：

| 模型 | 参数 | 硬件 | 最大时长 |
|---|---:|---|---:|
| small-music | 433M | CPU | 120s |
| small-sfx | 433M | CPU | 120s |
| medium | 1.4B | CUDA | 380s |

官方 Medium benchmark 的峰值显存约 5–6.5GB，因此 8GB VRAM 在理论上适配；但 Medium 依赖 Flash Attention 2，Windows 原生部署仍可能比 ACE-Step 复杂。

这意味着：

- **CPU 轻量音乐/SFX**：Stable Audio Small 很值得作为随手工具。
- **GPU 高质量编辑**：Medium 值得实测。
- **Audio-to-Audio / Inpaint / Continuation**：Stable Audio 3 是重点补位。

## 不建议当前机器硬塞

### ACE-Step XL 4B

官方 XL 至少建议 12GB + offload/quantization；无 offload 更偏 20GB 级显存。8GB 不应作为主力路线。

### AudioCraft / MusicGen Medium

官方文档给出的 medium 推理级别约需要 16GB GPU，适合以后使用更大 GPU 或云端做研究对照。

### Magenta RealTime 本地

官方本地 GPU Docker 路线写明约 40GB 显存级需求，不属于当前笔记本主力。

## 推荐部署顺序

```text
1. ACE-Step v1.5 2B：完整歌曲 / Cover
2. Stable Audio 3 Small：CPU 音乐 + SFX
3. Stable Audio 3 Medium：GPU A2A / Inpaint / 长音频
4. Demucs 固定版本：Stem 分离
5. AudioCraft：只作为研究基线，不优先本机部署
```

## 测试记录必须包含

- 模型精确版本 / commit
- Torch / CUDA / Python
- 精度与量化
- CPU offload
- 生成时长
- 峰值 VRAM
- 生成耗时
- Prompt / 输入音频
- 主观质量评分

## 官方来源

- [ACE-Step v1.5](https://github.com/ace-step/ACE-Step-1.5)
- [Stable Audio 3](https://github.com/Stability-AI/stable-audio-3)
- [AudioCraft](https://github.com/facebookresearch/audiocraft)
- [Magenta RealTime](https://github.com/magenta/magenta-realtime)

## 相关

- [[本地模型部署分层-2026]]
- [[AI音乐音频任务选型矩阵-2026]]