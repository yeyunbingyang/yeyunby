---
title: 响度LUFS与True-Peak
tags: [音频, LUFS, TruePeak, EBU-R128, ITU-BS1770]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
summary: "以 ITU-R BS.1770 和 EBU R128 为基础理解 LUFS、True Peak、Momentary、Short-term 与 Integrated 响度。"
---

# 响度 LUFS 与 True Peak

## 为什么不能只看峰值

两个音频都峰值到 -1 dBFS，主观上仍可能一个很响、一个很轻。现代响度工作流因此使用感知加权的节目响度和 True Peak，而不是仅做峰值归一化。

## 核心术语

| 指标 | 含义 |
|---|---|
| LUFS | 感知响度单位，常用于整体节目响度 |
| Integrated | 从开始到结束的整体响度 |
| Short-term | 约 3 秒窗口 |
| Momentary | 约 400 ms 窗口 |
| LRA | Loudness Range，描述节目响度范围 |
| dBTP | True Peak，估计重建后的真实峰值 |

ITU-R BS.1770-5（2023）是当前在行版本，给出节目响度与 True Peak 的测量算法。EBU R128 在此基础上形成广播响度工作流。

## EBU R128 参考值

EBU 的广播推荐目标是 **-23 LUFS**（节目响度）；它更适合作为理解标准和广播链参考，并不意味着所有短视频/流媒体都必须使用 -23 LUFS。

> 发布平台最终目标应以平台规范为准，不要把单一 LUFS 数字硬套所有场景。

## AI 音频常见问题

- 生成结果过度限制器，动态被压扁。
- 峰值不高但 Integrated LUFS 非常高，听感疲劳。
- AI 补全/拼接前后响度突变。
- 压缩编码后出现 inter-sample peak。

## FFmpeg Loudness 分析

```bash
ffmpeg -i input.wav -filter_complex ebur128=peak=true -f null -
```

生产中建议先测量，再决定是否进行 loudnorm，而不是每个文件盲目套同一参数。

## 官方来源

- [ITU-R BS.1770-5](https://www.itu.int/rec/R-REC-BS.1770)
- [EBU Loudness / R128](https://tech.ebu.ch/loudness/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

## 相关

- [[混音母带与AI音频验收]]
- [[音频增强与响度标准化]]