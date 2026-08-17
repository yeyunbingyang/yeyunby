---
title: Fun-CosyVoice3-项目笔记
tags: [TTS, Voice-Clone, CosyVoice, 本地部署, 开源项目]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
source: https://github.com/QwenAudio/CosyVoice
summary: "Fun-CosyVoice3 是面向多语言零样本声音克隆、低延迟流式 TTS、指令控制与训练/服务部署的一体化 0.5B TTS 路线。"
---

# Fun-CosyVoice3 项目笔记

## 一句话定位

**Fun-CosyVoice3 = 多语言零样本声音克隆 + 指令式控制 + 双向流式 + 训练/推理/服务完整工具链。**

它位于 IndexTTS-2.5 与 GPT-SoVITS 之间：既强调零样本、情绪和生产控制，也保留训练与服务部署路线。

## 当前主线

官方当前重点是：

```text
Fun-CosyVoice3-0.5B-2512
```

仓库当前归属 `QwenAudio/CosyVoice`，模型仍以 `FunAudioLLM` 命名空间发布。

## 核心能力

官方 README 当前列出的 Fun-CosyVoice 3.0 重点包括：

- 9 种常用语言：中文、英文、日文、韩文、德文、西班牙文、法文、意大利文、俄文
- 18+ 中文方言/口音
- 多语言 / 跨语言 zero-shot voice cloning
- 中文拼音与英文 CMU phoneme 的 pronunciation inpainting
- 数字、特殊符号等文本正规化能力
- Text-in Streaming + Audio-out Streaming 双向流式
- 官方标注最低约 150ms 延迟路线
- Instruct 控制：语言、方言、情绪、速度、音量等

## 为什么值得进入主线

### 1. 多语言与方言覆盖强

如果角色需要：

- 普通话
- 粤语/闽南/四川/东北等方言或口音
- 中英日韩跨语言

CosyVoice3 是很值得优先验证的路线。

### 2. 流式能力适合交互应用

双向流式意味着它不只是离线配音模型，也适合：

- 数字人
- AI 助手
- 实时 NPC
- 实时对话
- WebSocket / API 服务

### 3. 指令控制适合角色演绎

语言、方言、情绪、速度、音量等可以作为统一控制接口，适合角色对白系统化生产。

## 安装主线

```bash
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
cd CosyVoice
git submodule update --init --recursive

conda create -n cosyvoice -y python=3.10
conda activate cosyvoice
pip install -r requirements.txt
```

仓库发生过组织迁移/重定向；知识库统一使用当前 GitHub 入口：

```text
https://github.com/QwenAudio/CosyVoice
```

## 模型下载

ModelScope：

```python
from modelscope import snapshot_download
snapshot_download(
    'FunAudioLLM/Fun-CosyVoice3-0.5B-2512',
    local_dir='pretrained_models/Fun-CosyVoice3-0.5B'
)
```

Hugging Face：

```python
from huggingface_hub import snapshot_download
snapshot_download(
    'FunAudioLLM/Fun-CosyVoice3-0.5B-2512',
    local_dir='pretrained_models/Fun-CosyVoice3-0.5B'
)
```

## 基础使用

官方当前推荐优先使用 `Fun-CosyVoice3-0.5B`：

```bash
python example.py
```

WebUI 示例：

```bash
python3 webui.py --port 50000 --model_dir pretrained_models/Fun-CosyVoice3-0.5B
```

## 服务化

CosyVoice2/3 当前提供 vLLM 路线，并有：

- FastAPI
- gRPC
- Docker
- Triton / TensorRT-LLM 路线

因此它很适合从实验环境继续升级到局域网 TTS 服务或生产后端。

## 适合的任务

| 任务 | 适合度 | 说明 |
|---|---:|---|
| 多语言 zero-shot | ★★★★★ | 核心强项 |
| 中文方言/口音 | ★★★★★ | 18+ 方言/口音路线 |
| 实时对话/数字人 | ★★★★★ | 双向流式、低延迟 |
| 情绪/速度/音量控制 | ★★★★★ | Instruct 控制 |
| 发音修正 | ★★★★☆ | 拼音 / CMU pronunciation inpainting |
| 服务部署 | ★★★★★ | vLLM / FastAPI / gRPC / Docker |
| 固定角色 few-shot 资产 | ★★★★☆ | 有训练路线，但 GPT-SoVITS 的角色资产工作流更直观 |
| 极简本地预览 | ★★☆☆☆ | 轻量试听更适合 Kokoro |

## 与另外两条主线的分工

```text
IndexTTS-2.5
→ 强零样本 + 情绪解耦 + 语速/发音控制

Fun-CosyVoice3
→ 多语言/方言 + 指令控制 + 流式 + 服务/训练平台

GPT-SoVITS
→ 固定角色 + few-shot 微调 + 数据集制作
```

## 许可证

仓库当前为 **Apache License 2.0**。

正式产品仍需要分别确认下载模型、附加资源和训练/输入素材的许可条件。

## 后续实验建议

1. 普通话 / 日文 / 英文同音色跨语言一致性
2. 方言与口音可辨识度
3. 情绪/速度/音量指令控制稳定性
4. 流式首包延迟与 RTF
5. 长文本连续输出稳定性
6. 与 IndexTTS-2.5 的相同参考音频 A/B
7. 与 GPT-SoVITS 固定角色模型的角色一致性对比

## 相关

- [[本地TTS路线图-2026]]
- [[IndexTTS-2.5-项目笔记]]
- [[GPT-SoVITS-项目笔记]]
- [[Kokoro-82M-项目笔记]]
- [[AI音乐与音频开源项目索引-2026]]
