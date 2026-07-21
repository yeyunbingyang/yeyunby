---
title: defuddle — 网页内容转 Markdown 工具
description: 使用 Defuddle CLI 从网页中提取干净的 Markdown 内容，去除导航栏、广告等干扰，适用于在线文档和文章的抓取。
aliases:
  - defuddle skill
tags:
  - obsidian
  - markdown
  - web-scraping
  - claude-code
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: Core_Ability
source: kepano/obsidian-skills
install: npx skills add kepano/obsidian-skills@defuddle
---

# defuddle 使用手册

## 概述

Defuddle CLI 从网页中提取干净可读的内容（Markdown），自动去除导航、广告等干扰。适用于在线文档、文章、博客等标准网页。

## 安装

```bash
npm install -g defuddle
```

## 基本用法

```bash
# 转为 Markdown 输出到终端
defuddle parse <url> --md

# 保存到文件
defuddle parse <url> --md -o content.md

# 提取特定元数据
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## 输出格式

| 标志 | 格式 |
|------|------|
| `--md` | Markdown（推荐） |
| `--json` | JSON（含 HTML 和 Markdown） |
| (无) | HTML |
| `-p <名称>` | 特定元数据属性 |

## 适用场景

- 阅读在线文章后存入知识库
- 抓取文档作为参考
- 保存博客文章到 Obsidian
