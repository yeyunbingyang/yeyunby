---
title: AI音乐与音频-MOC
domain: Core_Ability
tags: [AIGC, AI音乐, AI音频]
status: 稳定
created: 2026-08-10
updated: 2026-08-17
verified: 2026-08-17
related:
  - "[[Core_Ability-MOC]]"
summary: "AI音乐与音频知识域已完成 01–06 第一版：基础知识、音乐、TTS、SFX、音频处理与工具模型选型，并以实验/工作流/资产继续向 07–10 沉淀。"
---

# AI 音乐与音频

> [!abstract] 领域定位
> `yeyunby` AIGC 创作能力中的声音能力中心。这里不是独立软件项目，而是长期维护的知识/实验/工作流/资产体系。

## 01–06 核心知识地图

### 01 基础知识

- [[数字音频基础]]
- [[采样率位深与声道]]
- [[音频格式编码与容器]]
- [[响度LUFS与True-Peak]]
- [[音乐结构BPM调性与节拍]]
- [[混音母带与AI音频验收]]

### 02 AI 音乐

- [[AI音乐模型路线图-2026]]
- [[AI音乐Prompt设计方法]]
- [[AI音乐风格描述维度]]
- [[完整歌曲生成方法]]
- [[BGM与OST生成方法]]
- [[原音乐风格化改编-需求与模型选型]]

### 03 AI 语音 / TTS

- [[Web-Speech-API与浏览器TTS]]
- [[本地TTS路线图-2026]]
- [[IndexTTS-2.5-项目笔记]]
- [[GPT-SoVITS-项目笔记]]
- [[在线TTS能力与选型]]
- [[声音克隆基础与参考音频规范]]
- [[角色语音一致性设计]]
- [[配音生成-本机TTS引擎选型]]

### 04 AI 音效

- [[AI音效模型路线图-2026]]
- [[环境音与Ambience生成]]
- [[UI音效设计与生成]]
- [[动漫音效设计方法]]
- [[游戏音效设计方法]]
- [[视频Foley与转场音效]]

### 05 音频处理

- [[音乐源分离与Demucs]]
- [[语音降噪与DeepFilterNet]]
- [[音频增强与响度标准化]]
- [[Voice-Conversion概览-2026]]
- [[ASR路线图-Whisper-FunASR]]
- [[FFmpeg音频处理常用方法]]

### 06 工具与模型

- [[AI音乐与音频开源项目索引-2026]]
- [[AI音乐与音频在线平台索引-2026]]
- [[本地模型部署分层-2026]]
- [[AI音乐音频任务选型矩阵-2026]]

## 一条生产链看懂 01–06

```text
01 原理与标准
      ↓
02 音乐      03 语音      04 音效
      \        |        /
       \       |       /
          05 后处理
              ↓
       06 工具/模型选型
              ↓
07 工作流 → 08 实验 → 09 Prompt → 10 资产
```

## 2026-08 当前主线

- 音乐：ACE-Step v1.5 / Stable Audio 3；AudioCraft 用作控制研究；Magenta RealTime 用作实时路线参考。
- TTS：**IndexTTS-2.5** / Fun-CosyVoice3 / GPT-SoVITS；Kokoro 负责轻量预览。
- SFX：Stable Audio 3 Small-SFX / TangoFlux / AudioGen；在线可对照 ElevenLabs Sound Effects。
- 音频处理：Demucs 固定版本、DeepFilterNet、Whisper/FunASR、RVC/VC、FFmpeg。

## 动态索引

```dataview
TABLE summary, status, updated, verified
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/03-AI音乐与音频"
WHERE file.name != "AI音乐与音频-MOC" AND file.name != "README" AND file.name != "项目说明"
SORT updated DESC
```

## 信息维护规则

1. 技术原理放 01–05。
2. 项目/模型版本与平台事实放 06。
3. 未实测内容标记为“调研结论”，不能写成“本机已验证”。
4. 动态信息写 `verified` / `review_after`。
5. 正式实验进入 08，成熟流程再升格到 07。

## 上级导航

- [[Core_Ability-MOC]]