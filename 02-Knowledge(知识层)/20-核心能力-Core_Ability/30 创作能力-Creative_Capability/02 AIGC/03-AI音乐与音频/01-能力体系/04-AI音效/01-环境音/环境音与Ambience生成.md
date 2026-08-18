---
title: 环境音与Ambience生成
tags: [AI音效, Ambience, 环境音]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "环境音生成要描述空间、距离、声源层级、时间、天气和循环要求，而不是只写一个地点名称。"
---

# 环境音与 Ambience 生成

## Prompt 维度

```text
空间：forest / cave / bedroom / city alley
时间：dawn / night / late afternoon
天气：rain / wind / dry / snow
声源：birds / traffic / AC hum / distant crowd
距离：near / mid / far
密度：sparse / moderate / dense
空间感：dry / small room / open field / cavernous
循环：seamless loop / evolving ambience
```

## 示例

```text
Quiet mountain temple ambience at dawn,
soft wind through bamboo, distant bell every 15–20 seconds,
very sparse birds, large open outdoor space,
no music, no speech, seamless evolving ambience.
```

## 生产建议

- 环境音尽量生成 20–60 秒以上，再选稳定区段循环。
- 不要把所有声源塞进一个 Prompt；复杂环境可分层生成再混音。
- 保留底噪层、事件层、特色层三组 Stem。

```text
BED.wav      连续环境底
EVENTS.wav   鸟鸣、钟声、车辆等离散事件
ACCENT.wav   剧情强调声音
```

## 推荐路线

Stable Audio 3 Small-SFX 适合长一些的本地环境声；ElevenLabs 支持 loop；TangoFlux 适合 30 秒以内的高质量片段。

## 相关

- [[AI音效模型路线图-2026]]
- [[混音母带与AI音频验收]]