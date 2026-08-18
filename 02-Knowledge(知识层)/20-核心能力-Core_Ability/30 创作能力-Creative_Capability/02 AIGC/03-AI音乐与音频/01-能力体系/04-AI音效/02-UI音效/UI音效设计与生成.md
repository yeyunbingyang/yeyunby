---
title: UI音效设计与生成
tags: [AI音效, UI, UX, SoundDesign]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "UI 音效应建立一套声音设计系统，让点击、确认、警告、成功、删除等状态形成统一品牌语言。"
---

# UI 音效设计与生成

## 不是随机做几十个 beep

UI 声音应该像视觉 Design System 一样有家族关系。

## 声音 Token

| Token | 设计维度 |
|---|---|
| Click | 极短、轻、低干扰 |
| Confirm | 上扬/稳定、明确完成 |
| Success | 更明亮，可稍长 |
| Warning | 中频突出但避免刺耳 |
| Error | 下行/不稳定、明确但不惊吓 |
| Delete | 短促、收缩、消失感 |
| Notification | 可识别、与点击声区分 |

## Prompt 结构

```text
功能 + 材质 + 音高趋势 + 时长 + 空间 + 禁止项
```

示例：

```text
Minimal premium UI confirmation sound,
soft glassy pluck with a subtle upward two-note motion,
180 milliseconds, dry and clean, no reverb tail,
no harsh high-frequency click.
```

## 验收

- 是否在小音量仍可识别
- 连续触发是否烦躁
- 同系列是否像同一个产品
- 是否抢夺音乐/对白
- 是否能在手机小扬声器上听见

## 相关

- [[AI音效模型路线图-2026]]
- [[混音母带与AI音频验收]]