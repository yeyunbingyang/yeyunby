---
title: HTML 知识地图
domain: IT_Technology
tags:
  - HTML
  - 前端基础
  - MOC
status: 草稿
created: 2026-06-26
updated: 2026-06-26
source: ""
related:
  - "[[00 基础总结]]"
  - "[[CSS-MOC]]"
  - "[[01 HTML]]"
summary: HTML知识地图，完整笔记在01 HTML.md中，以下子笔记按知识点从原文拆分而成，每篇仅添加frontmatter不改原文内容。
---

# HTML 知识地图

## 学习路径

```mermaid
flowchart LR
  基础概念 --> 入门语法
  入门语法 --> 排版文本
  排版文本 --> 图片链接
  图片链接 --> 列表表格
  列表表格 --> 表单
  表单 --> 实体元信息
  实体元信息 --> H5新特性
```

## 笔记列表

| # | 笔记 | 描述 | 状态 |
|---|------|------|------|
| - | [[01 HTML]] | HTML完整笔记（原始全文） | 稳定 |
| 1 | [[02 HTML-基础概念]] | 计算机基础、C/S与B/S架构、浏览器、网页概念、HTML简介 | 草稿 |
| 2 | [[03 HTML-入门与语法]] | 准备工作、标签、属性、基本结构、注释、文档声明、字符编码、标准结构 | 草稿 |
| 3 | [[04 HTML-排版与文本标签]] | 排版标签、语义化、块级vs行内元素、常用/不常用文本标签 | 草稿 |
| 4 | [[05 HTML-图片与超链接]] | img标签、路径分类、图片格式、a标签、锚点、唤起应用 | 草稿 |
| 5 | [[06 HTML-列表与表格]] | 有序/无序/自定义列表、表格结构、常用属性、跨行跨列 | 草稿 |
| 6 | [[07 HTML-表单]] | form、input/text/radio/checkbox、textarea、select、button、label | 草稿 |
| 7 | [[08 HTML-实体与元信息]] | iframe、HTML实体、全局属性、meta元信息 | 草稿 |
| 8 | [[09 HTML-H5新特性]] | H5语义化标签、表单增强、video/audio多媒体、兼容性 | 草稿 |
| 9 | [[10 HTML-标签总结]] | HTML标签全景分类总结 | 草稿 |

## 核心原则

- **语义化**：使用合适的标签表达内容含义，而非关注默认样式
- **结构与表现分离**：HTML管结构，CSS管样式
- **标准化**：遵循W3C标准，保证跨浏览器一致性

## 相关资源

- [W3School HTML 教程](https://www.w3school.com.cn/html/)
- [MDN HTML 文档](https://developer.mozilla.org/zh-CN/docs/Web/HTML)
- [WHATWG HTML 标准](https://html.spec.whatwg.org/)

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/03-前端开发/web/01 前端基础/01 HTML与CSS"
WHERE contains(tags, "HTML") AND file.name != "01-HTML-MOC"
SORT file.name ASC
```
