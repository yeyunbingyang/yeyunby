---
title: Obsidian Claude Skills 索引
description: 已安装的 6 个 Obsidian 相关 AI 代理技能的索引与快速参考
aliases:
  - Obsidian Skills
tags:
  - obsidian
  - skills
  - claude-code
  - reference
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: IT_Technology
---

# Obsidian Claude Skills 使用手册索引

本索引汇集了从 [[agent-skills-生产级工程技能包|Skills]] 生态安装的 6 个 Obsidian 相关 AI 代理技能的使用手册。这些技能通过 `npx skills add` 安装到 Claude Code，扩展了 AI 代理对 Obsidian 的操作能力。

## 安装命令

```bash
# 安装全部 6 个技能
npx skills add mattpocock/skills@obsidian-vault -g -y
npx skills add kepano/obsidian-skills@obsidian-markdown -g -y
npx skills add kepano/obsidian-skills@obsidian-cli -g -y
npx skills add kepano/obsidian-skills@obsidian-bases -g -y
npx skills add kepano/obsidian-skills@json-canvas -g -y
npx skills add kepano/obsidian-skills@defuddle -g -y
```

## 技能列表

| #   | 技能名                                            | 用途                         | 安装量   | 来源                     |
| --- | ---------------------------------------------- | -------------------------- | ----- | ---------------------- |
| 1   | [[Obsidian-Vault-Skill\|obsidian-vault]]       | Obsidian 知识库组织规范           | 59.9K | mattpocock/skills      |
| 2   | [[Obsidian-Markdown-Skill\|obsidian-markdown]] | Obsidian 风味 Markdown 语法    | 47.1K | kepano/obsidian-skills |
| 3   | [[Obsidian-CLI-Skill\|obsidian-cli]]           | Obsidian CLI 命令操作          | 39.7K | kepano/obsidian-skills |
| 4   | [[Obsidian-Bases-Skill\|obsidian-bases]]       | Obsidian Bases 数据库视图       | 39.0K | kepano/obsidian-skills |
| 5   | [[JSON-Canvas-Skill\|json-canvas]]             | JSON Canvas 画布文件 (.canvas) | 35.0K | kepano/obsidian-skills |
| 6   | [[Defuddle-Skill\|defuddle]]                   | 网页内容 → Markdown 提取         | 34.0K | kepano/obsidian-skills |

## 效果

这些技能使得 Claude Code 等 AI 代理可以：

- 理解并生成标准的 Obsidian 风味 Markdown
- 通过 CLI 直接操作运行中的 Obsidian 实例
- 创建和管理复合视图、公式（Bases）
- 读写 Canvas 文件（思维导图/流程图）
- 将网页内容转为 Markdown 存入知识库
