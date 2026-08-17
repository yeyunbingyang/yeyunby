---
title: 配音生成-本机TTS引擎选型
domain: Core_Ability
tags:
  - AI音频
  - TTS
  - 配音
  - 待验证
status: 草稿
created: 2026-08-16
updated: 2026-08-16
review_after: 2026-09-16
source: "2026-08 对话记录，各引擎 GitHub 官方仓库见文末来源"
related:
  - "[[AI音乐与音频-MOC]]"
  - "[[配乐生成-本机项目选型]]"
  - "[[本机AI音乐项目适配评估]]"
  - "[[15-OpenMontage-视频生产平台|OpenMontage]]"
summary: "动漫视频本地中文女声配音采用四引擎架构：Kokoro 负责秒级预览、IndexTTS-2.5 作为高质量默认主力、CosyVoice 3 负责情绪演绎、GPT-SoVITS 负责固定角色音色克隆"
---

# 配音生成：本机 TTS 引擎选型

## 需求定义

目标是为动漫视频做 **中文女声 + 本地离线配音**，不依赖浏览器自带 TTS 的电子音，也不需要在线 API。典型用途：

- 动漫/漫剧角色对白、旁白
- 同一角色跨集保持同一音色
- 按「台词 → 选角色 → 选情绪 → 试听 → 生成 WAV」的本地工作流
- 最终接入 OpenMontage 的 TTS 环节

本机环境沿用既有结论：RTX 4060 Laptop 8GB、Windows、模型与缓存放 X 或 F 盘。

> [!important] 本机结论
> 先落 **Kokoro（秒级预览）+ IndexTTS-2.5（高质量默认）**，再补 **CosyVoice 3（高情绪角色）** 与 **GPT-SoVITS（固定角色音色克隆）**，组成四引擎架构。不要继续依赖浏览器自带的女声。

## 引擎对比

| 推荐 | 引擎 | 中文自然度 | 音色克隆 | 情绪控制 | 本地负担 | 定位 |
| --- | --- | --- | --- | --- | --- | --- |
| 🥇 | IndexTTS-2.5 | ★★★★★ | ✅ | ★★★★★ | 中高 | 主力动漫配音 |
| 🥈 | CosyVoice 3 | ★★★★★ | ✅ | ★★★★★ | 中高 | 对话、角色演绎 |
| 🥉 | GPT-SoVITS | ★★★★☆ | ✅ 强 | ★★★★☆ | 中 | 固定女角色音色 |
| 4 | F5-TTS | ★★★★☆ | ✅ | ★★★★☆ | 中 | 自然叙述、克隆 |
| 5 | Kokoro 82M | ★★★★ | ❌/弱 | ★★★ | 很低 | 快速预览 |
| 6 | MeloTTS | ★★★☆ | 较弱 | ★★★ | 低 | 简单离线 |
| 7 | Piper | ★★～★★★ | ❌ | ★★ | 极低 | CPU、系统提示音 |

## 四引擎架构

```text
┌───────────────────────────────┐
│        OpenMontage TTS        │
├───────────────────────────────┤
│  ⚡ 快速预览      Kokoro         │
│  ★ 默认高质量    IndexTTS 2.5   │
│  🎭 高情绪角色   CosyVoice 3    │
│  👤 固定角色音色 GPT-SoVITS      │
└───────────────────────────────┘
```

作用分工：

- **Kokoro**：写脚本时 1～2 秒快速试听，避免每改一句台词都跑大型 TTS。
- **IndexTTS 2.5**：默认高质量女声主力，一段参考音频即可 zero-shot 克隆。
- **CosyVoice 3**：对白演技、情绪起伏与流式生成，作第二个后端。
- **GPT-SoVITS**：把固定角色音色固化，跨集保持一致。

## 各引擎要点

### IndexTTS-2.5（主力）

- 2026-08-10 发布，支持 zero-shot 音色克隆。
- 语言：中 / 英 / 日 / 西 / 阿拉伯。
- 增加细粒度情绪、语速、发音控制。
- 适合为每个动漫角色保存多情绪参考音频。

### CosyVoice 3（情绪演绎）

- 支持 9 种语言、18+ 中文方言/口音，跨语言 zero-shot。
- 强调自然度、说话人相似度、韵律与流式生成，流式延迟最低约 150ms。
- 适合旁白 / 冷淡克制 / 活泼开心 / 战斗急促等不同情绪。

### GPT-SoVITS（固定角色）

- 约 5 秒样本可 zero-shot，约 1 分钟素材可 few-shot 精调。
- 语言：中 / 日 / 英 / 韩 / 粤语，自带 WebUI 与数据工具。
- 适合把「紫棠」等角色音色固定下来，贯穿 EP01/02/03。

### F5-TTS（自然叙述）

- 提供 Python 包、Docker、Gradio WebUI，可完全本地推理。
- ⚠️ 代码为 MIT，但官方预训练模型因训练数据采用 CC-BY-NC，偏非商业用途；商业流水线优先研究 IndexTTS / CosyVoice 许可。

### Kokoro 82M（预览）

- 仅 82M 参数，支持普通话 `zh` 管线，`pip install kokoro`。
- 定位是「写脚本 → 秒级试听 → 确定台词 → 再上高质量引擎」。

### MeloTTS（简单离线）

- 中 / 日 / 韩 / 英，MIT 许可，商业更宽松。
- 优点简单、轻、快；但真人感与演技不如第一梯队。

### Piper（系统级）

- 极轻量本地系统级 TTS，CLI / Python / C/C++ / Web Server。
- 适合应用提示、系统播报、无 GPU / CPU / NAS / 智能家居。
- 不是「好听的动漫女主角」的首选。

### 暂不推荐：Fish Audio S2 Pro

- 声音能力强，但官方当前明确建议 S2 推理至少 24GB VRAM，不适合本机硬塞。

## 音色库组织

一个角色按情绪保存多段参考音频，比「女声01、女声02」更可控：

```text
voices/
  紫棠/
    neutral.wav   冷静
    gentle.wav    温柔
    cold.wav      冷感
    angry.wav     愤怒
```

调用时以「角色 / 情绪」组合生成，例如：紫棠 / 温柔、紫棠 / 紧张、紫棠 / 悲伤。

## 落地顺序

1. V0.3/V0.4 先落 Kokoro + IndexTTS-2.5。
2. 预览接口固定为 Kokoro，最终合成走 IndexTTS。
3. 再增加 CosyVoice 3（情绪演绎）与 GPT-SoVITS（固定角色克隆）。

## HTML 配置界面参考

```text
配音引擎   [ IndexTTS 2.5 ▼ ]
角色音色   [ 紫棠 / 冷感女声 ▼ ]
情绪       [ 温柔 ▼ ]
语速       [────●────] 0.92x
情绪强度   [──────●──] 70%
台词       ┌─────────────────────────┐
           │ 我只是……不想再失去你了。 │
           └─────────────────────────┘
[ ▶ 试听 ]   [ 生成 WAV ]
```

## 首轮测试计划

- [ ] Kokoro 跑通普通话预览，记录单句延迟
- [ ] IndexTTS-2.5 用同一段台词生成，对比自然度与情绪
- [ ] 为「紫棠」保存 3～4 种情绪参考音频并做克隆测试
- [ ] 记录各引擎显存峰值、生成速度、是否 OOM
- [ ] 确认 F5-TTS / IndexTTS / CosyVoice 的商用许可边界
- [ ] 验证 Fish Audio S2 Pro 的 24GB VRAM 要求后再决定是否排除

## 待验证与风险

> [!warning] 待验证
> 各引擎的发布时间、语言列表、流式延迟、许可与显存要求来自 2026-08 对话记录，落地前以官方仓库复核。IndexTTS-2.5 的发布日期与 Fish Audio S2 Pro 的 24GB 要求尤其需再确认。

## 来源

- [index-tts/index-tts](https://github.com/index-tts/index-tts)
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice)
- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [SWivid/F5-TTS](https://github.com/swivid/f5-tts)
- [hexgrad/kokoro](https://github.com/hexgrad/kokoro)
- [myshell-ai/MeloTTS](https://github.com/myshell-ai/MeloTTS)
- [OHF-Voice/piper1-gpl](https://github.com/OHF-voice/piper1-gpl)
- [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)

## 相关笔记

- [[开源配音引擎全景]]
- [[配乐生成-本机项目选型]]
- [[本机AI音乐项目适配评估]]
- [[15-OpenMontage-视频生产平台|OpenMontage]]
- [[AI音乐与音频-MOC]]
