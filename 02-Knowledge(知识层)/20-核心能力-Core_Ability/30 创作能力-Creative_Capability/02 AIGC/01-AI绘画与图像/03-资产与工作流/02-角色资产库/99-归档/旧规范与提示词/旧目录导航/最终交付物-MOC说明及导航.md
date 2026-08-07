---
title: 最终交付物-MOC说明及导航
status: 归档
status_cn: 已归档
maturity: stable
maturity_cn: 稳定
domain: Core_Ability
tags:
- AI绘画
- 最终资产
- 交付物
created: 2026-08-02
updated: 2026-08-02
summary: 最终交付物目录只保存已通过验收、可直接用于下游生产的图片、视频和角色资产。
content_type: moc
scope: asset
---

# 最终交付物-MOC说明及导航

未通过验收的过程图、失败图和临时展示板不得进入本目录。每项交付物必须能追溯到实验记录和验收结论。

## 目录导航与概括

- `JULIA/`：JULIA 已通过验收的正式人物资产。
- `墨衣少年/`：墨衣少年已通过静态门禁的关键帧。

```dataview
TABLE file.folder AS "目录", file.ext AS "格式"
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/10-AI人物身份参考资产库/07-最终交付物"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```
