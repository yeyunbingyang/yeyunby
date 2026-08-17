---
title: AI音乐Prompt设计方法
tags: [AI音乐, Prompt, 控制变量]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
summary: "AI 音乐 Prompt 应从标签堆叠升级为用途、结构、速度/律动、调性、配器、情绪曲线、制作与硬约束的分层描述。"
---

# AI 音乐 Prompt 设计方法

## 推荐七层结构

```text
1. 用途 / 场景
2. 曲风 / 年代 / 地域
3. BPM / 拍号 / Groove
4. Key / Harmony
5. Instrumentation
6. Structure / Dynamics
7. Production / Avoid
```

## 模板

```text
用途：60秒仙侠战斗短片 BGM。
曲风：cinematic xianxia, orchestral + Chinese traditional instruments。
速度：132 BPM, 4/4, driving pulse。
调性：D minor, modal color, restrained dissonance。
配器：taiko-like drums, low strings, dizi, guzheng accents, brass only at climax。
结构：0-8s sparse intro → 8-28s build → 28-48s climax → 48-60s resolve。
制作：wide cinematic stereo, clear transients, dialogue-friendly midrange。
避免：vocals, spoken words, constant maximum intensity, abrupt ending。
```

## 重要原则

### 描述“变化”而不只描述“风格”

`epic cinematic` 很弱；`restrained intro → rising ostinato → brass climax → short resolve` 更可执行。

### 把可验证内容写成硬约束

- 时长
- 是否人声
- BPM
- 歌曲段落
- 必须/禁止乐器
- 是否循环

### 原曲编辑加入“保留项”

```text
Preserve: melody, lyric timing, section order.
Change: instrumentation, groove, ambience, vocal delivery.
```

## 生成后记录

每次实验至少记录：模型、版本、Prompt、Seed/随机参数、时长、输入音频、输出文件、主观评分。

## 相关

- [[音乐结构BPM调性与节拍]]
- [[AI音乐风格描述维度]]
- [[原音乐风格化改编-需求与模型选型]]