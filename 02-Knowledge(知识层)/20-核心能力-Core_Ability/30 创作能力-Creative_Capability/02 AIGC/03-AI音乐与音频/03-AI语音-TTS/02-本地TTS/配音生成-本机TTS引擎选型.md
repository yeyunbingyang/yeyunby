---
title: 配音生成-本机TTS引擎选型
domain: Core_Ability
tags: [AI音频, TTS, 配音, 本地部署]
status: 稳定
created: 2026-08-16
updated: 2026-08-17
verified: 2026-08-17
review_after: 2026-10-17
source: "IndexTTS、CosyVoice、GPT-SoVITS、Kokoro 官方仓库"
related:
  - "[[本地TTS路线图-2026]]"
  - "[[角色语音一致性设计]]"
  - "[[AI音乐音频任务选型矩阵-2026]]"
summary: "本地动漫/视频配音采用四层架构：Kokoro 快速预览、IndexTTS2 高质量主力、Fun-CosyVoice3 情绪/多语言平台、GPT-SoVITS 固定角色克隆。"
---

# 配音生成：本机 TTS 引擎选型（2026-08-17 校正版）

## 先校正旧版本名

此前笔记写过 “IndexTTS-2.5”，经官方仓库复核，当前应以 **IndexTTS2** 作为正式记录名称。官方在 2025-09-08 发布 IndexTTS-2，重点包括情绪表达、speaker/emotion 解耦以及精确时长控制研究方向。

> 官方 release note 曾明确提示：论文中的部分精确时长控制功能在初始公开版本中尚未启用。因此项目里必须按实际代码/模型实测，不能只按论文能力写“已支持”。

## 四层架构

```text
┌────────────────────────────────┐
│       本地 TTS Production       │
├────────────────────────────────┤
│  ⚡ 快速预览      Kokoro 82M      │
│  ★ 高质量默认    IndexTTS2        │
│  🎭 情绪/多语言   Fun-CosyVoice3   │
│  👤 固定角色克隆  GPT-SoVITS       │
└────────────────────────────────┘
```

## 1. Kokoro：快速预览

定位：快、轻、低成本。

适合：
- 写台词时即时试听
- HTML / 浏览器预览
- CPU 兜底

不承担最终角色身份锁定。

## 2. IndexTTS2：高质量角色主力

优先测试：
- 中文角色对白
- 强情绪
- speaker / emotion 分离
- 视频对白时长对齐能力

正式使用要固定模型版本与参考音频。

## 3. Fun-CosyVoice3：完整平台路线

CosyVoice 官方当前重点推荐 `Fun-CosyVoice3-0.5B`，并提供推理、训练、WebUI、服务化/vLLM 等路线。

更适合：
- 多语言 / 多口音
- 情绪和角色演绎
- 需要训练或后端服务化的项目

## 4. GPT-SoVITS：固定角色克隆

优势在成熟的角色声音克隆与数据工具链。

适合：
- 固定人物跨集保持声音身份
- 建立角色专属训练/参考素材
- 中文/日文/英文等角色实验

## 角色库建议

```text
voices/
  ZITANG_V01/
    neutral.wav
    gentle.wav
    cold.wav
    angry.wav
    profile.yaml
```

`profile.yaml` 同时记录：引擎、模型版本、参考素材、语言、语速、情绪策略和后处理。

## 本机测试不要预设统一显存数字

TTS 项目的占用受版本、后端、精度和长度影响明显。本知识库不再给每个引擎写一个永久“最低显存”，而是在 `08-实验室-Lab/TTS实验` 中记录本机实测。

## 推荐验证顺序

1. Kokoro：测单句启动与实时预览延迟。
2. IndexTTS2：同一角色 10 条不同文本，测身份/情绪稳定性。
3. Fun-CosyVoice3：测情绪、多语言和服务化。
4. GPT-SoVITS：建立一个固定角色 Voice Profile 做跨场景测试。

## 官方来源

- [IndexTTS](https://github.com/index-tts/index-tts)
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [Kokoro](https://github.com/hexgrad/kokoro)

## 相关

- [[本地TTS路线图-2026]]
- [[声音克隆基础与参考音频规范]]
- [[角色语音一致性设计]]