---
title: 版本与失败记录-MOC说明及导航
status: 归档
status_cn: 已归档
maturity: stable
maturity_cn: 稳定
domain: Core_Ability
tags:
- AI绘画
- 版本管理
- 失败分析
created: 2026-08-02
updated: 2026-08-02
summary: 版本与失败记录保存被淘汰资产及其原因、证据、修复方案、验证结果和回退点。
content_type: moc
scope: asset
---

# 版本与失败记录-MOC说明及导航

失败记录不是图片堆放区。每条记录必须关联实验 ID，并说明可观察现象、原因证据、单变量解决方案、修复结果和下游准入结论。

## 文件导航与概括

| 文件／目录 | 概括 |
|---|---|
| [[失败分析模板]] | 新失败记录必须填写的标准结构。 |
| [[失败资产索引]] | 已归位失败样张的根因与修复索引（迁移后失败资产索引）。 |
| `JULIA/` | JULIA 比例、身份和生成失败版本。 |
| `墨衣少年/` | 墨衣少年未通过和候选版本。 |
| `研究角色-S01/` | 服装偏移、拼图等研究失败。 |

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/10-AI人物身份参考资产库/06-版本与失败记录"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```
