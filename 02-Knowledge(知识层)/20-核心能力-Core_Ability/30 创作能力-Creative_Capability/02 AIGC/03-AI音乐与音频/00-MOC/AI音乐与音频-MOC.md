---
title: AI音乐与音频-MOC
domain: Core_Ability
tags: [AIGC, AI音乐, AI音频]
status: 稳定
created: 2026-08-10
updated: 2026-08-18
verified: 2026-08-18
related:
  - "[[Core_Ability-MOC]]"
summary: "AI音乐与音频按 01–05 能力组织；模型、工具与 Prompt 均融入对应能力，08 用于实验验证，07 仅保留跨能力端到端工作流，10 保存可复用资产。"
---

# AI 音乐与音频

> [!abstract] 领域定位
> `yeyunby` AIGC 创作能力中的声音能力中心。这里不是独立软件项目，而是长期维护的知识 / 实验 / 工作流 / 资产体系。

## 01–05 核心知识地图

### 01 基础知识

- [[数字音频基础]]
- [[采样率位深与声道]]
- [[音频格式编码与容器]]
- [[响度LUFS与True-Peak]]
- [[音乐结构BPM调性与节拍]]
- [[混音母带与AI音频验收]]
- [[AI音乐与音频开源项目索引-2026]]
- [[AI音乐与音频在线平台索引-2026]]
- [[本地模型部署分层-2026]]
- [[AI音乐音频任务选型矩阵-2026]]

### 02 AI 音乐

- [[AI音乐模型路线图-2026]]
- [[音乐生成模型与开源项目]]
- [[本机AI音乐项目适配评估]]
- [[配乐生成-本机项目选型]]
- [[AI音乐Prompt设计方法]]
- [[AI音乐风格描述维度]]
- [[完整歌曲生成方法]]
- [[BGM与OST生成方法]]
- [[原音乐风格化改编-需求与模型选型]]

### 03 AI 语音 / TTS

- [[Web-Speech-API与浏览器TTS]]
- [[本地TTS路线图-2026]]
- [[本地TTS横向对比-功能与环境要求-2026]]
- [[IndexTTS-2.5-项目笔记]]
- [[Fun-CosyVoice3-项目笔记]]
- [[GPT-SoVITS-项目笔记]]
- [[Kokoro-82M-项目笔记]]
- [[开源配音引擎全景]]
- [[配音生成-本机TTS引擎选型]]
- [[在线TTS能力与选型]]
- [[声音克隆基础与参考音频规范]]
- [[角色语音一致性设计]]

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

## 知识生命周期

```text
01 基础 / 标准 / 跨域索引
          ↓
02 音乐      03 语音      04 音效
(模型 + 工具 + 方法 + Prompt 都在能力内部)
          \      |      /
             05 后处理
                  ↓
             08 实验验证
             /          \
单能力成熟内容留在 02–05   跨能力端到端流程升格到 07
             \          /
                10 资产
```

> 原 `06-工具与模型`、`09-提示词库` 已取消。不要重新建立第二套工具树或总 Prompt 仓库。

## 2026-08 当前主线

- 音乐：ACE-Step v1.5 / Stable Audio 3；AudioCraft 用作控制研究；Magenta RealTime 用作实时路线参考。
- TTS：**IndexTTS-2.5 / Fun-CosyVoice3 / GPT-SoVITS / Kokoro-82M**，分别承担强可控零样本、实时多语言平台、固定角色训练、轻量预览。横向选型统一查看 [[本地TTS横向对比-功能与环境要求-2026]]。
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

1. 跨能力基础、标准、全局索引与通用部署知识放 01。
2. 项目 / 模型 / 平台技术卡直接放到 02–05 对应能力目录。
3. Prompt、参数模板和控制写法跟随能力放入 02–05，不建立总 Prompt 库。
4. 一个项目横跨多个能力时，只保留一个主技术卡，其他目录通过双链引用。
5. 未实测内容标记为“调研结论”，不能写成“本机已验证”。
6. 动态信息写 `verified` / `review_after`。
7. 正式实验进入 08；只有跨两个以上能力、已验证且可重复的完整生产链才进入 07。

## 上级导航

- [[Core_Ability-MOC]]
