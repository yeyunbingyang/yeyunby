---
title: FFmpeg音频处理常用方法
tags: [FFmpeg, 音频处理, 自动化]
status: 稳定
created: 2026-08-17
updated: 2026-08-17
verified: 2026-08-17
summary: "FFmpeg 是 AI 音频流水线的通用胶水层，可承担抽轨、转码、重采样、裁切、混音、测响度与批处理。"
---

# FFmpeg 音频处理常用方法

## 检查文件

```bash
ffprobe -v error -show_streams -show_format input.wav
```

## 视频抽取无损音频

```bash
ffmpeg -i input.mp4 -vn -c:a pcm_s24le output.wav
```

## 重采样为 48 kHz Stereo

```bash
ffmpeg -i input.wav -ar 48000 -ac 2 output_48k.wav
```

## 转 Mono

```bash
ffmpeg -i input.wav -ac 1 output_mono.wav
```

## 裁切

```bash
ffmpeg -ss 00:00:10 -to 00:00:25 -i input.wav output.wav
```

## 淡入淡出

```bash
ffmpeg -i input.wav -af "afade=t=in:st=0:d=1,afade=t=out:st=9:d=1" output.wav
```

## 测量 EBU R128 / True Peak

```bash
ffmpeg -i input.wav -filter_complex ebur128=peak=true -f null -
```

## Loudnorm 示例

下面只是技术示例，不是所有平台统一目标：

```bash
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 output.wav
```

正式项目应按平台/工程规范选择目标，并优先使用两遍测量流程。

## 混合两轨

```bash
ffmpeg -i voice.wav -i bgm.wav \
-filter_complex "[0:a][1:a]amix=inputs=2:duration=longest:normalize=0" \
output.wav
```

## 无损保存 / 发布编码

```bash
# WAV → FLAC
ffmpeg -i master.wav master.flac

# WAV → AAC
ffmpeg -i master.wav -c:a aac -b:a 192k publish.m4a

# WAV → Opus
ffmpeg -i master.wav -c:a libopus -b:a 128k publish.opus
```

## 作为 AI 流水线的原则

- 原始 AI 输出永远保留。
- 中间处理优先 WAV/FLAC。
- FFmpeg 命令写入脚本，不靠手工重复点击。
- 每个批处理脚本记录输入/输出参数。

## 官方来源

- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [FFmpeg Filters](https://ffmpeg.org/ffmpeg-filters.html)

## 相关

- [[音频格式编码与容器]]
- [[响度LUFS与True-Peak]]