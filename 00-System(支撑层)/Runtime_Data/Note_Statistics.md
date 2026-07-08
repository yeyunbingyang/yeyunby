---
title: 笔记统计
tags: [仪表盘, 统计]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "知识库笔记数量与状态统计，用于评估知识资产健康度"
---

# 笔记统计

---

## 按状态分布

```dataview
TABLE length(rows) as "数量"
FROM "02-Knowledge(知识层)"
WHERE file.name != "IT_Technology-MOC" AND file.name != "Cognition-MOC" AND file.name != "Core_Ability-MOC"
GROUP BY status
```

---

## 按领域分布

```dataview
TABLE length(rows) as "笔记数"
FROM "02-Knowledge(知识层)"
GROUP BY domain
```

---

## 最近更新（近 10 条）

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)"
WHERE file.name != "IT_Technology-MOC" AND file.name != "Cognition-MOC" AND file.name != "Core_Ability-MOC"
SORT updated DESC
LIMIT 10
```

---

## 待改进笔记

```dataview
TABLE summary, domain, updated
FROM "02-Knowledge(知识层)"
WHERE status = "改进"
SORT updated ASC
```

---

## 计划中笔记（未开始写）

```dataview
TABLE summary, domain
FROM "02-Knowledge(知识层)"
WHERE status = "计划"
```
