---
title: obsidian-vault — Obsidian 知识库组织规范
description: 用于搜索、创建、管理 Obsidian 仓库中的笔记，使用 wikilinks 和索引笔记进行组织。
aliases:
  - obsidian-vault skill
tags:
  - obsidian
  - skill
  - claude-code
  - vault-organization
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: IT_Technology
source: mattpocock/skills
install: npx skills add mattpocock/skills@obsidian-vault
---

# obsidian-vault 使用手册

## 概述

定义了 Obsidian 知识库的组织规范。**注意**：该 skill 自带特定的 vault 路径约定（`/mnt/d/Obsidian Vault/AI Research/`），本知识库已有自己的 [[CLAUDE.md|CLAUDE.md]] 规范，因此仅参考其通用设计模式。

## 核心约定

- **索引笔记**：聚合相关主题（如 `XX-MOC.md`），作为导航入口
- **标题命名**：建议英文 Title Case 或中文命名
- **链接**：使用 `[[wikilinks]]` 语法连接笔记
- **依赖/关联**：在笔记底部列出相关链接

## 适配本知识库

本知识库已有自己的 4 层架构（支撑层/日常流层/知识层/资源层），以及 MOC（Map of Content）体系。该 skill 的通用方法已被吸收至知识库的 CLAUDE.md 中。

## 通用搜索命令

```bash
# 按文件名搜索
find "/vault/path/" -name "*.md" | grep -i "关键词"

# 按内容搜索
grep -rl "关键词" "/vault/path/" --include="*.md"

# 查找反向链接
grep -rl "\\[\\[Note Title\\]\\]" "/vault/path/"

# 查找索引笔记
find "/vault/path/" -name "*Index*"
```
