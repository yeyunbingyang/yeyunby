---
title: BGM与OST生成方法
tags: [AI音乐, BGM, OST, 视频配乐]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "BGM/OST 的核心不是单独好听，而是服务画面、对白、节奏与情绪转折，因此应按时间轴和功能段生成。"
---

# BGM 与 OST 生成方法

## 与歌曲生成最大的不同

BGM 首先服务内容，其次才是独立音乐作品。

### 四个优先级

1. 镜头/剧情节奏
2. 对白可懂度
3. 情绪推进
4. 音乐自身完整性

## 时间轴 Prompt

```text
用途：60秒人物觉醒场景。
0–12s：低密度、神秘、留对白空间。
12–28s：弦乐 ostinato 渐入，增加紧张。
28–46s：鼓组与低铜管进入，形成高潮。
46–56s：保持能量但减少旋律密度。
56–60s：短尾奏，给下一镜头留空间。
No vocals. Avoid busy lead melody under dialogue.
```

## 模型选择

- Stable Audio 3：适合纯音乐、Audio-to-Audio、Inpaint、Continuation；Small-Music 可 CPU 使用，Medium 面向高质量 GPU 生成。
- ACE-Step v1.5：适合更长时结构、明确歌曲/音乐规划和本地生成。
- MusicGen/JASCO：适合旋律、和弦、鼓等控制研究。

## Loop BGM

循环音乐应同时检查：

- 首尾和声能否衔接
- 环境/混响尾巴是否断裂
- 律动相位是否跳变
- 结尾不要做明显终止式

必要时生成更长片段，再在 DAW/FFmpeg 中选择循环点，而不是强求模型直接完美无缝。

## 对白友好处理

- 避免 1–4 kHz 长时间高密度主旋律占用。
- 旁白段减少打击乐与尖锐瞬态。
- 高潮可以提升宽度和低频，但要给人声留中央信息区。

## 来源

- [Stable Audio 3](https://github.com/Stability-AI/stable-audio-3)
- [ACE-Step v1.5](https://github.com/ace-step/ACE-Step-1.5)
- [AudioCraft](https://github.com/facebookresearch/audiocraft)

## 相关

- [[配乐生成-本机项目选型]]
- [[音乐结构BPM调性与节拍]]