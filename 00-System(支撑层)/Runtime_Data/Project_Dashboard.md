---
title: 项目仪表盘
tags: [仪表盘, 待办, 任务]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "待办事项集中管理入口，每条任务直接链接到对应笔记"
---

# 项目仪表盘

待办事项集中管理。格式：`- [ ] 任务描述 → [[对应笔记名]]`，点击 `[[]]` 直接跳转笔记。

---

## 进行中

- [ ] 示例：完善 IT_Technology-MOC 子主题内容 → [[IT技术-MOC]]

---

## 本周计划

- [ ] 示例：建立第一条知识笔记 → [[IT技术-MOC]]

---

## 已完成

- [x] 重构知识库三域结构（10/20/30） ✅ 2026-05-07
- [x] 新建 Project_Dashboard 待办系统 ✅ 2026-05-07
- [x] 新建 06-Archive 封存层 ✅ 2026-05-07

---

## 笔记内嵌任务（自动聚合）

> 以下由 Dataview 自动从 03-Knowledge 中的所有笔记内抓取未完成 checkbox，无需手动维护。

```dataview
TASK
FROM "KnowledgeBase/03-Knowledge"
WHERE !completed
GROUP BY file.link
```

---

## Inbox 待处理

> 显示 Inbox 中所有待整理的文件，目标：保持清空。

```dataview
TABLE file.mtime as "最后修改"
FROM "KnowledgeBase/01-Inbox"
WHERE file.name != "README"
SORT file.mtime ASC
```

---

## 使用说明

1. **新增任务**：在"进行中"或"本周计划"下添加 `- [ ] 任务 → [[笔记名]]`
2. **完成任务**：勾选 checkbox，移到"已完成"并加 `✅ 日期`
3. **笔记内任务**：在知识笔记中写 `- [ ] 下一步：xxx`，会自动出现在"笔记内嵌任务"区块
