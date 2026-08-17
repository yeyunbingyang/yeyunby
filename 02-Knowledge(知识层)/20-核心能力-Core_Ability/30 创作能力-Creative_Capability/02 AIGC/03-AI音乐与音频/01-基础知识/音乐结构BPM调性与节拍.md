---
title: 音乐结构BPM调性与节拍
tags: [AI音乐, BPM, 调性, 节拍, 歌曲结构]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "把音乐生成提示拆成结构、速度、拍号、调性、和声、配器和动态曲线，提升 AI 音乐可控性。"
---

# 音乐结构、BPM、调性与节拍

## AI 音乐最实用的控制层

```text
用途
→ 时长
→ 结构
→ BPM/速度
→ 拍号/律动
→ 调性/和声色彩
→ 配器
→ 情绪曲线
→ 制作与空间风格
```

## BPM

BPM 描述速度，但相同 BPM 可以因为鼓点密度、切分和拍号产生完全不同的体感。

Prompt 不建议只写 `120 BPM`，而应补充：

```text
120 BPM, steady four-on-the-floor pulse,
restrained intro, denser percussion in the climax
```

## 拍号 Meter

常见 4/4、3/4、6/8。模型是否严格遵循拍号因模型而异，所以“拍号”应同时进入生成约束和验收项。

## 调性 Key / Mode

不要把“大调=开心、小调=悲伤”绝对化。可用：

- 具体 Key：D minor、A major
- Mode：Dorian、Mixolydian 等（模型遵循程度需实测）
- Harmony character：open fifths、modal harmony、chromatic tension

## 歌曲结构

常见标签：

- Intro
- Verse
- Pre-Chorus
- Chorus
- Bridge
- Breakdown
- Climax
- Outro

对 BGM/OST 更适合用剧情功能：

```text
0–10s Establish
10–25s Build
25–40s Tension
40–55s Climax
55–60s Resolve
```

## 与模型的关系

ACE-Step v1.5 强调长时音乐规划和可控生成；Stable Audio 3 支持变长生成、音频续写和局部编辑，因此结构信息不仅用于 Prompt，也可映射为多阶段生成与修补。

## 来源

- [ACE-Step v1.5](https://github.com/ace-step/ACE-Step-1.5)
- [Stable Audio 3](https://github.com/Stability-AI/stable-audio-3)

## 相关

- [[AI音乐Prompt设计方法]]
- [[完整歌曲生成方法]]
- [[BGM与OST生成方法]]