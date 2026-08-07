---
title: 图片与视频资产-MOC说明及导航
status: 归档
status_cn: 已归档
maturity: stable
maturity_cn: 稳定
domain: Core_Ability
tags:
- AI绘画
- 图片资产
- 视频资产
created: 2026-08-02
updated: 2026-08-02
summary: 图片与视频资产目录保存生产过程中的媒体母资产，按角色或研究对象聚合，不代表全部已经通过验收。
content_type: moc
scope: asset
---

# 图片与视频资产-MOC说明及导航

过程资产按角色或研究对象聚合。通过验收、可直接复用的文件另登记到 `07-最终交付物`；失败文件保留在 `06-版本与失败记录`。

## 目录导航与概括

- `版式参考/`：人物身份参考板等现行版式示例。
- `JULIA/`：JULIA 身份、三视图、比例和动漫化过程资产。
- `研究角色-S01/`：四格研究和不同风格路线的过程资产。
- `古风角色/`：古风题材提示词示例和角色媒体。
- `角色设定案例/`：角色规范板案例图。
- `作品四格研究卡/`：作品视觉研究卡媒体。

## 历史媒体入口

- `99-归档/05-历史媒体资产/身份实验/`：早期身份、多角度与三视图实验媒体。
- `99-归档/05-历史媒体资产/动漫风格实验/`：早期动漫风格探索和被替代路线。

历史媒体只用于追溯，不应作为现行提示词参考、身份锚点或最终交付物。

```dataview
TABLE file.folder AS "目录", file.ext AS "格式"
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/10-AI人物身份参考资产库/04-图片与视频资产"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```
