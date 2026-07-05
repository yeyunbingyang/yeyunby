---
title: 后端开发 MOC
domain: IT_Technology
tags: [MOC, 后端, Python, FastAPI]
status: 稳定
created: 2026-05-07
updated: 2026-07-05
summary: "后端开发子域地图，以 Python 为核心(86篇)，覆盖语法核心/标准库/生态(爬虫+Web+数据库)/实战，含尚硅谷课程与 FastAPI 全栈实战"
---

# 后端开发

服务端软件工程的核心知识域。当前以 **Python** 为主要语言，源自尚硅谷大模型技术之 Python 课程，已建 86 篇笔记。

## 子域导航

| 子域 | 笔数 | 关键内容 |
|------|------|----------|
| [[Python-MOC\|01 Python]] | 86 | 语法核心(25篇)、标准库(18篇)、生态-爬虫(20篇)、生态-Web/FastAPI(7篇)、生态-数据库(3篇)、实战踩坑 |
| 02 JS | — | 待建设 |
| 03 Java | — | 待建设 |
| 04 通用技术 | — | 待建设 |

## 学习路径

`语言基础` → `标准库` → `生态框架` → `实战与踩坑` → `系统设计与高并发`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| RESTful API | 基于 HTTP 动词的无状态接口设计规范 |
| ORM | 对象-关系映射，将代码对象映射到数据库表 |
| 异步编程 | asyncio/aiohttp，Python 并发处理核心 |
| 爬虫 | requests + BeautifulSoup / DrissionPage / Selenium 数据抓取 |

## Python 知识体系概要

### 语法核心（25篇）
初识Python → 基础 → 变量与数据类型 → 运算符 → 流程控制 → 组合数据类型(序列/列表/元组/字典/集合) → 异常处理 → 函数与模块 → 面向对象 → 高级语法(闭包/装饰器/迭代器/生成器)

### 标准库（18篇）
pip包管理、os/sys、文件IO、正则re、网络socket、并发threading、图形界面PyQt6/wxPython、邮件smtplib、绘图turtle

### 生态 — 爬虫（20篇）
基础知识 → 静态抓取(requests) → 数据解析(BeautifulSoup/lxml/XPath) → 自动化(DrissionPage/Selenium) → 反爬与反反爬 → 框架scrapy(待建)

### 生态 — Web开发 FastAPI（7篇）
[[01-FastAPI入门]] → [[02-FastAPI进阶]] → [[03-ORM模板代码]] → AI掘金头条实战(新闻/用户/收藏/缓存)

### 生态 — 数据库（3篇）
mysqlclient / PyMySQL / FastAPI异步驱动选型

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/02-后端开发"
WHERE file.name != "后端开发-MOC" AND !contains(file.folder, "00_Resource")
SORT updated DESC
```
