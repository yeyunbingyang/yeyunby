# 笔记 Frontmatter 规范

## 标准模板

```yaml
---
title: 笔记标题
domain: IT_Technology      # 三大域之一，见下方说明
tags: []                   # 关键词，辅助检索（1-4个）
status: 草稿               # 计划 | 草稿 | 稳定 | 改进 | 归档
created: 2026-05-07
updated: 2026-05-07
source: ""                 # 来源（链接/书名/课程）
related: []                # 关联笔记 [[笔记名]]
summary: ""                # 一句话核心内容（AI 检索用，必填）
---
```

## domain 合法值

| 值 | 覆盖范围 |
|----|----------|
| `IT_Technology` | 运维、云原生、后端、前端、网络、AI工程、自动化 |
| `Cognition` | 思维模型、认知科学、决策框架、心理学、人文社科、学习方法 |
| `Core_Ability` | 职业能力、表达沟通、商业财经、创作方法、生活基础设施 |

## status 说明

| 值 | 含义 | 下一步行动 |
|----|------|-----------|
| `计划` | 主题已定，内容尚未写 | 开始写作 |
| `草稿` | 正在写，内容片段不完整 | 补充完善 |
| `稳定` | 内容完整，当前无需更新 | 定期回顾 |
| `改进` | 已有内容，但需修订或补充 | 更新笔记 |
| `归档` | 已过时或被替代，封存用 | 移入 06-Archive |

**工作流：** `计划 → 草稿 → 稳定`，知识更新时回退到 `改进 → 稳定`，过时时 `→ 归档`

## summary 写法

用一句话描述笔记的**核心结论**，而非描述"这篇笔记写了什么"。

- 好：`"Transformer 注意力机制通过 Q/K/V 点积计算实现序列全局依赖"`
- 差：`"关于 Transformer 的笔记"`

## Dataview 查询示例

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge"
WHERE status = "改进"
SORT updated ASC
```

```dataview
TABLE summary, domain
FROM "KnowledgeBase/03-Knowledge"
WHERE status = "计划"
```

```dataview
TASK
FROM "KnowledgeBase/03-Knowledge"
WHERE !completed
GROUP BY file.link
```
