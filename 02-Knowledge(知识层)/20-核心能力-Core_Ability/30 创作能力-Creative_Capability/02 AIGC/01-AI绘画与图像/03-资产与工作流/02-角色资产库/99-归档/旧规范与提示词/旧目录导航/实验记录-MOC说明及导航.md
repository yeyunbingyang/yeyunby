---
title: 实验记录-MOC说明及导航
status: 归档
status_cn: 已归档
maturity: stable
maturity_cn: 稳定
domain: Core_Ability
tags:
- AI绘画
- 实验记录
created: 2026-08-02
updated: 2026-08-03
summary: 实验记录以实验ID和角色为索引，记录输入、提示词、参数、输出、验收结论和下一步。
content_type: moc
scope: asset
---

# 实验记录-MOC说明及导航

每次实验必须可追溯到角色、阶段、提示词版本、工具、输出资产和验收结论。失败本身不删除，失败分析另见 `06-版本与失败记录`。

## 文件导航与概括

| 文件／目录     | 概括                   |
| --------- | -------------------- |
| [[JULIA完整生产案例]] | 真人身份到动漫资产与视频验证的完整证据链。 |
| [[四格效果板案例]] | 研究角色 S01 的原创四格效果板实验。 |
| [[真人仙侠角色设定板提示词调教实验]] | 真人仙侠设定板的三轮提示词调教与母资产构建。 |
| `JULIA/`  | JULIA 的历史实验、比例和风格验证。 |
| `墨衣少年/`   | 墨衣少年资产卡与关键帧测试。       |
| `角色设定案例/` | 角色设定板提示词与案例。         |
| [[真人仙侠角色设定板提示词调教实验]] | 三轮对照验证身份、版式与真人感，并沉淀自然姿态修正模块。 |
| `风格研究/`   | 风格分类和作品观察证据。         |
| `待验证提示词/` | 尚未进入正式规范的实验假设。       |

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/10-AI人物身份参考资产库/03-实验记录"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```
