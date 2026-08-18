---
title: ASR路线图-Whisper-FunASR
tags: [ASR, Whisper, FunASR, 字幕, 语音识别]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
summary: "ASR 生产路线可用 Whisper 做通用多语言基线，用 FunASR 组合 VAD、标点、时间戳和中文/流式能力，再按任务选择。"
---

# ASR 路线图：Whisper + FunASR

## Whisper

OpenAI Whisper 是通用多语言语音识别模型系列，可用于：

- 多语言转写
- 语言识别
- 英语翻译（部分模型路线）
- 字幕与内容索引

官方当前提供 `turbo`，它基于 large-v3 的优化版本，目标是更快推理并尽量保持识别准确度；`turbo` 不适合拿来做翻译任务。

适合：
- 多语言通用基线
- 离线批量字幕
- 跨语言资料处理

## FunASR

FunASR 更像一套语音识别工具链，而不是单个模型，覆盖：

- ASR
- VAD
- Punctuation
- Speaker 相关能力
- Streaming
- 服务部署/API

当前官方文档的模型选择中包含 SenseVoice-Small 等快速多语种路线，也提供面向实时/服务化的组合方式。

## 任务选择

| 任务 | 优先 |
|---|---|
| 多语言通用字幕 | Whisper |
| 中文快速转写 | FunASR / SenseVoice 路线 |
| VAD + 标点 + 说话人流水线 | FunASR |
| 跨语言通用离线基线 | Whisper |
| 实时服务 | 优先验证 FunASR streaming 路线 |

## 字幕生产链

```text
音频
→ VAD
→ ASR
→ 标点恢复
→ 说话人/角色识别（按需）
→ 时间轴校正
→ 文本纠错
→ SRT/VTT/JSON
```

自动 ASR 不应直接作为最终字幕；角色名、术语、人名、数字和专有名词必须建立词表做人工校正。

## 官方来源

- [openai/whisper](https://github.com/openai/whisper)
- [modelscope/FunASR](https://github.com/modelscope/FunASR)

## 相关

- [[FFmpeg音频处理常用方法]]