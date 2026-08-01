---
title: 四格研究卡内聚于works数据
domain: Core_Ability
tags:
  - AI绘画
  - ADR
  - 数据模型
status: 稳定
created: 2026-07-30
updated: 2026-07-30
verified: 2026-07-30
review_after: 2027-01-30
source: "grill-with-docs领域建模会话"
related:
  - "[[AI人物身份参考资产库-MOC]]"
  - "[[CONTEXT]]"
summary: "60部作品的四格状态、素材和观察内聚在works.json，不新建重复数据库。"
---

# 四格研究卡内聚于works数据

资产库决定在 `works.json` 的每部作品记录中增加选片标签、四格状态及近景、全身、环境、动作四个视觉位，而不新建独立卡片数据库。来源仍由 `sources.json` 拥有，风格映射由 `styles.json` 拥有，原创效果板的提示词、修复和评分由 `experiments.json` 拥有。

