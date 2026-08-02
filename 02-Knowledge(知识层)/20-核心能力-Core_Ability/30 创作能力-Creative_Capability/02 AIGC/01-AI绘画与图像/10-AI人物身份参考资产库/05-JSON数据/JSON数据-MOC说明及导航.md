---
title: JSON数据-MOC说明及导航
domain: Core_Ability
tags: [AI绘画, JSON, 数据]
status: 稳定
created: 2026-08-02
updated: 2026-08-02
summary: "JSON 数据目录是作品、来源、风格和实验状态的机器可读事实源。"
---

# JSON数据-MOC说明及导航

四个 JSON 文件已经迁入本目录，作为作品、来源、风格和实验状态的机器可读事实源。媒体路径均以资产库根目录为基准。

- `styles.json`：风格定义与作品映射
- `works.json`：作品研究与四格状态
- `sources.json`：来源与验证状态
- `experiments.json`：实验、输出、失败与版本链

## 使用关系

`works.json` 与 `sources.json` 支撑 [[风格与作品研究]]；`experiments.json` 连接实验记录、媒体、失败证据和交付物。人工结论写入 Markdown，稳定字段和路径写入 JSON。
