---
title: 我的 Skills 清单
domain: Core_Ability
tags: [Skills, Agent, 工具清单]
status: 稳定
created: 2026-08-02
updated: 2026-08-02
source: ""
related: ["AI工具链与Agent实践-MOC", "02-我的skills蒸馏"]
summary: "个人 Agent Skills 全量清单：知识库 15 个 + 全局 43 个（codex/agents 合并去重），标注跨目录重复与待清理项"
---

# 我的 Skills 清单

> 扫描日期：2026-08-02。共发现 **知识库技能 15 个**（`X:\KMS\yeyunby\.agents\skills`）+ **全局技能 43 个**（`C:\Users\h2967\.codex\skills` 与 `C:\Users\h2967\.agents\skills` 合并去重）。

## 统计概览

| 位置 | 数量 | 说明 |
|------|------|------|
| 知识库 `X:\KMS\yeyunby\.agents\skills` | 15 | 随知识库管理，其中 obsidian 4 个与全局重复 |
| 全局 `.codex\skills` | 20 | 不含 `.system` 系统技能 |
| 全局 `.agents\skills` | 39 | 另有 1 个空目录 `learned`（待清理） |
| 全局合并去重 | 43 | codex 与 agents 有 16 个内容完全相同的重复 |

## 知识库技能（15 个）

存放于 `X:\KMS\yeyunby\.agents\skills\`，随知识库一起管理。

### Obsidian 与知识库管理

| 技能 | 用途 | 备注 |
|------|------|------|
| [[obsidian-vault]] | 搜索、创建、管理知识库笔记 | 另存于全局 `.agents/skills` |
| [[obsidian-bases]] | 创建编辑 Obsidian Bases（.base 数据库视图） | 另存于全局 `.agents/skills` |
| [[obsidian-markdown]] | 创建编辑 Obsidian 风格 Markdown | 另存于全局 `.agents/skills` |
| [[obsidian-cli]] | 用 Obsidian CLI 读写检索笔记 | 另存于全局 `.agents/skills` |
| [[vault-structure-refactor]] | 知识库目录重构与安全迁移 | |
| [[watch-notes]] | 视频转带关键帧的 Obsidian 笔记 | |

### 设计、动画与前端

| 技能 | 用途 |
|------|------|
| [[apple-design]] | Apple 风格界面设计与动效 |
| [[emil-design-eng]] | 设计工程打磨（Emil 方法论） |
| [[animation-vocabulary]] | 动效词汇反查 |
| [[find-animation-opportunities]] | 寻找应加动画的位置 |
| [[improve-animations]] | 动效审计与改进计划 |
| [[review-animations]] | 动效代码评审 |
| [[pick-ui-library]] | 前端组件库选型 |
| [[prototype]] | 多版本 UI 原型对比 |

### 信息获取

| 技能 | 用途 |
|------|------|
| [[github-trending]] | 抓取 GitHub 热门项目日/周/月榜（含上周） |

## 全局技能（43 个）

合并 `C:\Users\h2967\.codex\skills` 与 `C:\Users\h2967\.agents\skills` 去重。带 `*` 的技能在 codex 与 agents 各有一份完全相同的副本，建议只保留一份。

### 浏览器与网页自动化

| 技能 | 用途 |
|------|------|
| agent-browser* | 浏览器自动化 CLI |
| playwright* | 真实浏览器自动化（导航/表单/截图） |
| opencli-browser | 驱动真实 Chrome 窗口（opencli） |
| computer-use | 后台桌面操作（点击/输入/滚动） |
| web-scraping | Python 网页抓取与数据提取 |
| defuddle | 网页正文提取为干净 Markdown |
| dogfood | Web 应用探索式 QA（找 bug） |

### 网页与前端设计

| 技能 | 用途 |
|------|------|
| web-artifacts-builder | 复杂 HTML 工件构建 |
| web-design-guidelines | 网页设计规范评审 |
| design | 生产级 UI 设计（通用） |
| ui | 生产级 UI 设计（与 design 同类但内容独立） |
| frontend-design* | 前端视觉设计指导 |
| composition-patterns | React 组合模式 |
| react-best-practices | React/Next 性能优化 |

### 文档与办公

| 技能 | 用途 |
|------|------|
| docx* | Word 文档创建编辑 |
| pptx* | PowerPoint 演示文稿 |
| pdf* | PDF 读取创建审查 |
| read | URL/PDF 读取与总结 |
| write | 中英文润色、去 AI 味 |
| json-canvas | JSON Canvas（.canvas）可视化笔记 |

### 开发与工程

| 技能 | 用途 |
|------|------|
| cli-creator* | 从 API 文档构建 CLI |
| mcp-builder* | 构建 MCP 服务器 |
| skill-creator* | 创建改进技能 |
| find-skills* | 发现安装新技能 |
| check* | 代码审查与发布检查 |
| hunt | 定位 bug 根因 |
| health | 工程健康审计 |
| domain-modeling | 领域模型与术语梳理 |
| remotion-best-practices | Remotion 视频创作最佳实践 |

### 调研与学习

| 技能 | 用途 |
|------|------|
| agent-reach* | 全网多平台调研（搜索/社交/代码） |
| learn* | 六阶段研究学习工作流 |
| watch | 视频下载、抽帧与字幕提取 |
| think | 粗糙想法转为决策完整的计划 |
| grilling | 计划/方案压力测试（主技能） |
| grill-me* | grilling 的快捷入口（stub） |
| grill-with-docs | grilling + domain-modeling 组合入口（stub） |
| yuanbao | 元宝群组：@提及、查询信息/成员 |

### 其他工具

| 技能 | 用途 |
|------|------|
| antigravity* | Antigravity 平台自动化（OpenCLI） |
| figma* | Figma 设计稿转代码 |

## 维护说明

- **重复副本**：16 个带 `*` 的技能在 `.codex/skills` 与 `.agents/skills` 完全重复（MD5 相同）；obsidian 4 个在全局与知识库各有一份。建议统一保留一处、删除另一处，避免改后不同步。
- **待清理**：`.agents/skills/learned` 为空目录。
- **同类技能**：`design` / `ui` / `frontend-design` 三者都是 UI 设计，内容独立但职责重叠，可考虑合并；`watch`（通用）与 `watch-notes`（知识库笔记版）功能部分重叠。
- **新增技能**：放入 `X:\KMS\yeyunby\.agents\skills\<技能名>\SKILL.md`，并在此清单登记。
- **关联入口**：[[AI工具链与Agent实践-MOC]]、[[Github优质项目-MOC]]、[[02-我的skills蒸馏]]