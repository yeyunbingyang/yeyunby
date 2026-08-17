---
title: GPT-SoVITS-项目笔记
tags: [TTS, Voice-Clone, GPT-SoVITS, 本地部署, 开源项目]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
source: https://github.com/RVC-Boss/GPT-SoVITS
summary: "GPT-SoVITS 是偏角色声音克隆、few-shot 微调与数据工具链的一体化本地语音方案。"
---

# GPT-SoVITS 项目笔记

## 一句话定位

**GPT-SoVITS = 少样本声音克隆 + TTS + 数据预处理 + 训练 + 推理的一体化角色语音工具链。**

如果 IndexTTS-2.5 更像“高可控零样本推理引擎”，GPT-SoVITS 更适合长期维护固定角色声音、准备训练数据并做 few-shot 微调。

## 核心能力

官方当前 README 明确给出的能力包括：

- **Zero-shot TTS**：约 5 秒参考语音即可进行零样本合成
- **Few-shot TTS**：约 1 分钟训练数据可进行微调，提高音色相似度和真实感
- **跨语言推理**：支持中文、英文、日文、韩文、粤语等
- **WebUI**：完整图形界面
- **数据集工具链**：切片、ASR、标注、训练数据准备
- **伴奏/人声分离与去混响工具**
- **训练 GPT / SoVITS 模型**
- **推理与 API 使用**

## 为什么适合角色语音

### 1. 不只是“输入文本 → 生成声音”

它把角色声音生产中最麻烦的前后步骤也纳入了工具链：

```text
原始录音
  ↓
人声/伴奏处理
  ↓
音频切片
  ↓
ASR 转写
  ↓
文本校对/标注
  ↓
训练数据集
  ↓
GPT / SoVITS 训练或微调
  ↓
角色 TTS 推理
```

因此它更像一个本地“角色声音工作台”。

### 2. few-shot 微调适合长期固定角色

当零样本音色相似度还不够时，可以继续收集角色数据并微调，而不是频繁更换模型。

适合：

- 动漫角色
- 漫剧角色
- 游戏 NPC
- 视频固定旁白
- 虚拟主播/数字人
- 长期连续内容中的固定音色

## 当前性能信息

官方 README 当前以 **GPT-SoVITS v2 ProPlus** 展示推理性能，并给出了 4060 Ti、4090 和 Apple M4 CPU 的 RTF 示例。

这些数字适合用作“项目官方基准参考”，但不能直接当作本机结果。正式记录本机性能时，应单独进入实验室并记录：

- GPU
- CUDA / PyTorch
- 模型版本
- FP16/FP32
- 文本长度
- 输出时长
- 首包时间
- 总推理时间
- RTF

## Windows 安装路线

官方支持 Windows 10+，有两种主要方式。

### 方式 A：整合包

下载官方提供的 Windows package，使用：

```text
go-webui.bat
```

或：

```text
go-webui.ps1
```

这条路线适合先体验和验证模型。

### 方式 B：源码安装

官方当前推荐 Python 3.10 作为稳妥基线：

```powershell
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits
pwsh -F install.ps1 --Device CU128 --Source HF
```

也可选择：

```text
CU126
CU128
CPU
```

模型源支持 Hugging Face、HF Mirror、ModelScope 等路线。

## 依赖与附加工具

GPT-SoVITS 不是一个单模型仓库，使用时会涉及：

- FFmpeg
- ASR 模型
- VAD
- 标点模型
- UVR5 / Roformer 等音频分离模型
- GPT-SoVITS 预训练模型

这也是它功能强但目录和环境相对复杂的原因。

## 数据集格式

官方 TTS 标注格式：

```text
vocal_path|speaker_name|language|text
```

例如：

```text
D:\GPT-SoVITS\audio\001.wav|character_a|zh|你好，这是测试对白。
```

主要语言标识包括：

```text
zh  中文
ja  日文
en  英文
ko  韩文
yue 粤语
```

## 适合的任务

| 任务 | 适合度 | 说明 |
|---|---:|---|
| 固定角色声音克隆 | ★★★★★ | 核心强项 |
| few-shot 微调 | ★★★★★ | 少量数据即可继续优化角色 |
| 数据集制作 | ★★★★★ | 集成切片、ASR、标注等流程 |
| 中日韩角色语音 | ★★★★★ | 生态成熟 |
| 零样本快速克隆 | ★★★★☆ | 可直接用 5 秒参考尝试 |
| 强情绪程序化控制 | ★★★☆☆ | 相比 IndexTTS-2.5 不是主要优势 |
| 精确语速/时长控制 | ★★★☆☆ | 视频时长对齐优先评估 IndexTTS-2.5 |
| 极简快速部署 | ★★☆☆☆ | 功能丰富也意味着依赖较多 |

## 与 IndexTTS-2.5 的分工

### 优先 GPT-SoVITS

当需求是：

- 固定角色长期使用
- 有 1 分钟以上可用训练语音
- 想做角色微调
- 需要完整的数据准备工具链
- 需要自己维护角色模型资产

### 优先 IndexTTS-2.5

当需求是：

- 单参考音频直接克隆
- 快速生成多个角色
- 强情绪控制
- 独立情绪参考
- 程序化情绪向量
- 语速/时长倍率控制
- 更明确的生产服务化路线

## 推荐的角色声音工作流

```text
第一阶段：IndexTTS-2.5 / GPT-SoVITS Zero-shot
→ 快速筛选参考音频与角色方向

第二阶段：固定角色
→ 建立高质量参考音频资产
→ GPT-SoVITS few-shot 微调

第三阶段：正式生产
→ 对比 GPT-SoVITS 微调模型 与 IndexTTS-2.5 零样本
→ 按对白类型选择引擎
```

并不需要强制“一个项目包打天下”。

## 许可证

GPT-SoVITS 仓库当前标注为 **MIT License**。

但正式内容生产仍需分别确认：

- 训练语音是否有授权
- 克隆对象是否允许被克隆
- 使用的额外预训练模型/ASR/分离模型许可证
- 输出内容所在平台规则

## 后续实验建议

进入 `08-实验室-Lab` 后优先做：

1. 5 秒 / 10 秒 / 30 秒参考音频相似度实验
2. 1 分钟 few-shot 微调前后 A/B
3. 中文、日文、英文跨语言一致性
4. 同一角色长文本稳定性
5. 不同切片质量对训练结果的影响
6. 同参考音频与 IndexTTS-2.5 横向比较
7. Windows 一键启动脚本封装与端口管理

## 相关

- [[IndexTTS-2.5-项目笔记]]
- [[本地TTS路线图-2026]]
- [[声音克隆基础与参考音频规范]]
- [[角色语音一致性设计]]
- [[AI音乐与音频开源项目索引-2026]]
