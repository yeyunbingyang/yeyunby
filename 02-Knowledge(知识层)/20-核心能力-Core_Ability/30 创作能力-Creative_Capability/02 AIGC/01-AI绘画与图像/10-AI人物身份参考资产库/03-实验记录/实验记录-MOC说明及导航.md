---
title: 实验记录-MOC说明及导航
domain: Core_Ability
tags: [AI绘画, 实验记录]
status: 稳定
created: 2026-08-02
updated: 2026-08-02
summary: "实验记录以实验ID和角色为索引，记录输入、提示词、参数、输出、验收结论和下一步。"
---

# 实验记录-MOC说明及导航

每次实验必须可追溯到角色、阶段、提示词版本、工具、输出资产和验收结论。失败本身不删除，失败分析另见 `06-版本与失败记录`。

## 文件导航与概括

| 文件／目录 | 概括 |
|---|---|
| [[正式案例]] | 已形成完整证据链的案例入口。 |
| `JULIA/` | JULIA 的历史实验、比例和风格验证。 |
| `墨衣少年/` | 墨衣少年资产卡与关键帧测试。 |
| `角色设定案例/` | 角色设定板提示词与案例。 |
| `风格研究/` | 风格分类和作品观察证据。 |
| `待验证提示词/` | 尚未进入正式规范的实验假设。 |

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/20-核心能力-Core_Ability/30 创作能力-Creative_Capability/02 AIGC/01-AI绘画与图像/10-AI人物身份参考资产库/03-实验记录"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```
