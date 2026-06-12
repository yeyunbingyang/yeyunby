---
domain: IT_Technology
status: 稳定
summary: Python 知识体系导航，按语法核心/标准库/生态/代码库四域组织，通过 Dataview 自动聚合子目录笔记。
tags: [MOC, Python]
created: 2026-06-12
updated: 2026-06-12
---

# Python-MOC

> Python 知识地图，位于 `01-AI全栈工程` 子域下，按「极简扁平 + MOC 导航」模式组织。

## 目录结构

| 目录 | 定位 | 内容示例 |
|------|------|----------|
| [[01-语法核心]] | 语言基础 | 变量、运算符、流程控制、组合数据类型 |
| [[02 标准库]] | 官方标准库 | re、json、socket、threading、io、打包 exe |
| [[03 生态]] | 第三方包与框架 | 数据库驱动、FastAPI、爬虫、数据分析、Web 开发 |
| [[代码库]] | 实用代码片段 | 可复用代码收集 |

## 语法核心笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/01-语法核心"
WHERE file.name != "01-语法核心"
SORT file.name ASC
```

## 标准库笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/02 标准库"
SORT file.name ASC
```

## 生态笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/03 生态"
SORT file.name ASC
```

## 代码库

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/代码库"
SORT file.name ASC
```

---

## 跨域关联

- [[运维云原生-MOC]] — 运维场景下 Python 实战笔记（位于 `01 运维云原生`）
- [[AI工程-MOC]] — 上级 MOC，AI 全栈工程总导航
