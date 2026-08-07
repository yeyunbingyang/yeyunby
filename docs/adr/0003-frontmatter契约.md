---
title: frontmatter契约
domain: ""
tags: [ADR, 元数据, SCHEMA]
status: 稳定
created: 2026-08-02
updated: 2026-08-02
source: "grill-with-docs全库会话"
related:
  - "[[知识库需求决策记录]]"
  - "[[00-System(支撑层)/SCHEMA|SCHEMA]]"
summary: "知识笔记必须携带title、domain、tags、status、created、updated、summary七项frontmatter；domain限三值，status按计划到归档流转。"
---

# ADR 0003：frontmatter 契约

## 状态

已接受（2026-08-02 确认）。

## 决策

知识笔记必须带 frontmatter，必填字段为 title、domain、tags、status、created、updated、summary。`domain` 仅限 `IT_Technology`、`Cognition`、`Core_Ability`；`status` 正常流转 `计划 → 草稿 → 稳定`，修订走 `改进`，过时走 `归档`；`summary` 写一句话核心结论。`verified` 与 `review_after` 仅用于会随外部产品变化的笔记。字段定义以 `00-System(支撑层)/SCHEMA.md` 为唯一真相来源。

## 背景

存量 217 篇知识笔记缺少 frontmatter，Dataview 无法聚合，AI 无法按 summary、status、domain 检索。没有契约时元数据各自为政，检索与自动化能力随规模递减。

## 权衡

- 备选：无 frontmatter 的自由笔记。写作更快，但检索、聚合与 Agent 操作都依赖全文猜测。
- 备选：超多字段的复杂元数据。聚合能力强，但创建与维护负担重，用户会放弃填写。
- 代价：创建笔记时多填一次元数据；存量缺口需要逐步补齐。

## 后果

存量缺 frontmatter 的笔记列入待办逐步补齐，不批量改写；新建笔记必须合规。系统文档（如 README、SCHEMA、ADR）不属于知识笔记，`domain` 可为空。
