---
title: 视频Foley与转场音效
tags: [AI音效, Foley, 视频, 转场]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "视频声音应按 Foley、环境、动作强调和转场四层贴合镜头，AI 生成更适合作为素材工厂而非自动替代整条声音设计。"
---

# 视频 Foley 与转场音效

## 四层视频声音

```text
Ambience  环境底
Foley     脚步、衣物、物件
Action    打击、机械、爆炸、技能
Transition whoosh、riser、hit、reverse
```

## Foley Prompt

Foley 要把材质和动作说清楚：

```text
Close-mic footsteps of leather boots walking slowly on wet stone,
three distinct steps, realistic film foley,
no ambience, no music, dry studio recording.
```

## 转场音效

常见：

- whoosh
- riser
- downer
- impact
- braam
- glitch
- reverse swell

转场音效应该跟镜头运动方向、速度和剪辑点一致，而不是每个切镜都加同一种 whoosh。

## AI 的正确角色

- 快速生成“缺的那个声音”
- 生成同类多版本
- 生成难录制/幻想类素材
- 作为 Foley 初稿

正式成片仍需要时间轴对齐、EQ、动态、空间和响度处理。

## 相关

- [[动漫音效设计方法]]
- [[环境音与Ambience生成]]
- [[混音母带与AI音频验收]]