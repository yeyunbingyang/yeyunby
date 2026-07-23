---
title: Obsidian 软件资源
tags: [资源, Obsidian, 软件, 插件, 主题, 教程]
type: 工具
status: 稳定
created: 2026-07-21
updated: 2026-07-21
source: https://obsidian.md
related: [Obsidian知识管理-MOC]
summary: "Obsidian 软件资源合集：官网下载、11 个插件完整清单、主题推荐、官方与社区学习资源"
---

# Obsidian 软件资源

## 一、软件资源

| 资源 | 链接 |
|------|------|
| 官网 | https://obsidian.md |
| 下载 | https://obsidian.md/download（Windows / Mac / Linux / iOS / Android） |
| 官方文档 | https://help.obsidian.md |
| 发行说明 | https://obsidian.md/changelog |
| 官方论坛 | https://forum.obsidian.md |
| Discord 社区 | https://discord.gg/obsidianmd |
| 中文论坛 | https://forum-zh.obsidian.md |

**优点**：本地优先、数据归用户所有、纯 Markdown、可扩展性强、社区活跃
**局限**：闭源（非开源）、移动端体验不如桌面端、不适合实时协作

## 二、插件清单

### 已启用（9 个）

| 插件 ID | 名称 | 用途 | 依赖程度 |
|---------|------|------|----------|
| `dataview` | Dataview | 将 Vault 变成可查询数据库，支持 DQL 查询语言 | 🔴 高 |
| `obsidian-git` | Obsidian Git | Git 版本控制与自动备份 | 🔴 高 |
| `calendar` | Calendar | 侧边栏日历视图，日记快捷入口 | 🔴 高 |
| `obsidian-tasks-plugin` | Tasks | 任务管理增强，支持截止日期、优先级、重复任务 | 🔴 高 |
| `obsidian-excalidraw-plugin` | Excalidraw | 手绘风格白板、流程图、草图 | 🟡 中 |
| `realclaudian` | Claudian | 在 Obsidian 内调用 Claude AI 辅助写作 | 🟡 中 |
| `surfing` | Surfing | 在 Obsidian 内浏览网页 | 🟡 中 |
| `xmind-linker` | XMind Linker | 链接外部 XMind 文件到 Obsidian | 🟢 低 |
| `mxmind` | MxMind | 在 Obsidian 内创建思维导图 | 🟢 低 |

### 已安装未启用（2 个）

| 插件 ID | 名称 | 未启用原因 |
|---------|------|-----------|
| `templater-obsidian` | Templater | 知识库模板已使用 Templater 语法，建议启用 |
| `supermind` | SuperMind | 与 Claudian 功能重叠，待评估 |

### 插件恢复说明

`.obsidian/plugins/` 目录被 `.gitignore` 排除（二进制文件 14MB+），不会随 Git 备份。插件列表通过 `community-plugins.json` 跟踪。新设备恢复时，Obsidian 会读取该文件自动提示安装所有插件。

> 详见 [[Obsidian设置与个性化#新系统快速恢复]]

## 三、主题资源

### 当前主题

**moonstone**（Obsidian 默认浅色主题）— 简洁清晰，无需更换。

### 推荐主题

| 主题 | 特点 |
|------|------|
| Minimal | 极简风格，高度可定制，支持颜色方案 |
| Blue Topaz | 中文社区流行，功能丰富 |
| AnuPpuccin | 柔和配色，多种风格变体 |
| Things | macOS 风格，精致优雅 |

### 安装方法

设置 → 外观 → 主题 → 浏览 → 搜索主题名 → 安装并使用

### CSS Snippets

自定义样式放在 `.obsidian/snippets/` 目录，在 设置 → 外观 → CSS 代码片段 中启用。

## 四、学习资源

### 官方

- [Obsidian Help](https://help.obsidian.md) — 官方文档，最权威
- [Obsidian Blog](https://obsidian.md/blog) — 官方博客
- [Obsidian YouTube](https://www.youtube.com/@obsidian) — 官方视频教程

### 社区教程

- B站搜索"Obsidian 教程" — 大量中文视频教程
- [少数派 Obsidian 专题](https://sspai.com/tag/Obsidian) — 高质量中文文章
- [Obsidian Roundup](https://obsidian-roundup.com) — 每周社区动态汇总

### 示例库

- [LYT Kit](https://github.com/nickmilo/LYT-Kit) — Linking Your Thinking 框架
- [PARA Vault](https://github.com/fortelabs/para-vault) — Tiago Forte 的 PARA 方法

### 本知识库已有资源

- [[Obsidian知识管理-MOC]] — 本知识库的 Obsidian 使用指南
- [[11-obsidian-skills-Obsidian官方开发者kepano出品的AI|kepano/obsidian-skills]] — GitHub 资源（42.3k stars），Obsidian 官方开发者出品
- [[Obsidian-Agent操作指南]] — Agent 操作 Obsidian 的完整手册
- [[Hermes-Agent-技能工具手册]] — 知识库自动整理 Agent 项目