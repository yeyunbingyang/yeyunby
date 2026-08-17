---
title: 语音降噪与DeepFilterNet
tags: [音频处理, 降噪, SpeechEnhancement, DeepFilterNet]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
summary: "DeepFilterNet 是 48kHz 全频带语音增强/降噪开源路线，适合对白清理与实时降噪，但任何降噪都必须控制伪影和语音细节损失。"
---

# 语音降噪与 DeepFilterNet

## 降噪的目标

不是把频谱“变干净”，而是让有效语音更清晰，同时尽量不破坏：

- 辅音瞬态
- 齿音细节
- 呼吸与自然停顿
- 声音身份
- 房间空间感

过强降噪常产生比底噪更难听的水声、金属声和门限泵动。

## DeepFilterNet

官方项目定位为深度滤波驱动的实时语音增强，工作在 **48 kHz 全频带**，提供命令行、Python、实时和插件相关使用路线。

适合：

- 旁白/对白底噪
- 风扇与电脑噪声
- 轻度环境噪声
- 视频通话/实时输入
- TTS 参考音频预清理

## 推荐工作流

```text
原始语音
→ 检查削波 / DC / 严重爆音
→ 轻度降噪
→ 人工试听身份与辅音
→ EQ / 去齿音（按需）
→ 动态处理
→ 响度归一
```

> Voice Clone 参考音频不要盲目强降噪。严重处理产生的伪影也会被克隆模型学习进去。

## 验收 A/B

每次处理保留：

- `raw.wav`
- `denoise.wav`
- 同响度 A/B 试听

如果处理后只是“更安静”但语音变薄、变塑料，应降低强度或保留原始版本。

## 官方来源

- [DeepFilterNet](https://github.com/Rikorose/DeepFilterNet)

## 相关

- [[声音克隆基础与参考音频规范]]
- [[音频增强与响度标准化]]