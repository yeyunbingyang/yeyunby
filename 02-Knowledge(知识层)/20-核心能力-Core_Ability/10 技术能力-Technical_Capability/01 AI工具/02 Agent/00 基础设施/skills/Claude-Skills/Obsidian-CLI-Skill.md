---
title: obsidian-cli — Obsidian CLI 操作手册
description: 通过命令行与运行中的 Obsidian 实例交互：读/创建/搜索/管理笔记、任务、属性、标签，以及插件和主题开发调试。
aliases:
  - obsidian-cli skill
  - Obsidian 命令行
tags:
  - obsidian
  - cli
  - claude-code
  - plugin-development
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: Core_Ability
source: kepano/obsidian-skills
install: npx skills add kepano/obsidian-skills@obsidian-cli
links:
  - help/cli
---

# obsidian-cli 使用手册

## 概述

通过 `obsidian` 命令与**正在运行**的 Obsidian 实例交互。要求 Obsidian 保持打开。

## 语法

- **参数**：使用 `=` 赋值，空格用引号
- **布尔标志**：直接写，不需要值

```bash
obsidian create name="我的笔记" content="Hello world" silent overwrite
```

多行内容用 `\n` 换行，`\t` 制表符。

## 文件定位

- `file=<名称>`：按 wikilink 方式解析（只需名称，不含路径/扩展名）
- `path=<路径>`：从 vault 根目录的精确路径（如 `folder/note.md`）
- 不加两者 → 当前活动文件

## Vault 定位

默认操作最近聚焦的 vault，用 `vault=` 指定：

```bash
obsidian vault="我的知识库" search query="测试"
```

## 常用命令

```bash
# 读取笔记
obsidian read file="笔记名"

# 创建笔记
obsidian create name="新笔记" content="# Hello" template="模板" silent

# 追加内容
obsidian append file="笔记名" content="新行"

# 搜索
obsidian search query="搜索词" limit=10

# 读取/追加日记
obsidian daily:read
obsidian daily:append content="- [ ] 新任务"

# 设置属性
obsidian property:set name="status" value="done" file="笔记名"

# 查看任务
obsidian tasks daily todo

# 查看标签统计
obsidian tags sort=count counts

# 查看反向链接
obsidian backlinks file="笔记名"
```

所有命令支持 `--copy` 复制到剪贴板、`silent` 阻止文件打开、`total` 获取计数。

## 插件开发工作流

```bash
# 1. 刷新插件
obsidian plugin:reload id=my-plugin

# 2. 检查错误
obsidian dev:errors

# 3. 截图确认
obsidian dev:screenshot path=screenshot.png

# 4. 查看控制台输出
obsidian dev:console level=error

# 5. DOM 检查
obsidian dev:dom selector=".workspace-leaf" text
```

### 高级开发命令

```bash
# 执行 JS
obsidian eval code="app.vault.getFiles().length"

# 检查 CSS
obsidian dev:css selector=".workspace-leaf" prop=background-color

# 移动端模拟
obsidian dev:mobile on
```

## 参考

运行 `obsidian help` 获取最新命令列表。完整文档：https://help.obsidian.md/cli
