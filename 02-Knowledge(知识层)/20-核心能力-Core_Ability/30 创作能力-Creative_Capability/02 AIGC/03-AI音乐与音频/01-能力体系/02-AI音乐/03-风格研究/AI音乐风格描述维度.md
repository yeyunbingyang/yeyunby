---
title: AI音乐风格描述维度
tags: [AI音乐, 风格, 配器, Prompt]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "用多维属性描述音乐风格，避免仅靠 genre 名称导致生成结果模糊。"
---

# AI 音乐风格描述维度

“国风、史诗、Lo-fi、电子”都太宽。稳定描述至少拆成以下维度。

## 风格向量

| 维度 | 示例 |
|---|---|
| Genre | orchestral, ambient, synthwave |
| Region/Culture | Chinese traditional, Nordic folk |
| Era | 1980s, contemporary cinematic |
| Tempo/Groove | 90 BPM, swung, half-time |
| Harmony | modal, open fifths, jazz extensions |
| Instrument | guzheng, dizi, cello, analog synth |
| Texture | sparse, layered, granular, intimate |
| Emotion | serene, ominous, triumphant |
| Dynamics | slow build, sudden drop, restrained climax |
| Production | dry studio, large hall, vintage tape |
| Function | dialogue bed, boss battle, title theme |

## 风格迁移写法

不要只写：

```text
convert to xianxia
```

建议写：

```text
Preserve the original melody and section timing.
Replace pop drums with cinematic percussion.
Add dizi lead ornaments and guzheng arpeggios.
Use modal Chinese-inspired harmony, spacious hall reverb,
and reduce dense midrange under dialogue.
```

## 建立个人风格词典

后续可按以下格式沉淀：

```text
STYLE-XIANXIA-01
核心：清冷、空灵、克制仙侠
速度：70–95 BPM
配器：dizi / xiao / guzheng / strings
空间：large but transparent hall
禁用：EDM kick, bright pop clap, dense brass
```

## 相关

- [[AI音乐Prompt设计方法]]
- [[原音乐风格化改编-需求与模型选型]]