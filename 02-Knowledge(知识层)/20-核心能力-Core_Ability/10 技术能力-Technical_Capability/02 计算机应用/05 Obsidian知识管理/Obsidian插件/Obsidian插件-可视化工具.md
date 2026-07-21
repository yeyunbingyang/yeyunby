---
title: Obsidian 可视化工具插件
domain: Core_Ability
tags: [Obsidian, 插件, 可视化, 思维导图, 白板]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系]
summary: "Excalidraw 手绘白板、XMind-Linker 链接外部 XMind 文件、MxMind 内置思维导图——三个插件覆盖了可视化思考的主要场景"
---

# Obsidian 可视化工具插件

## 一句话结论

> 三个可视化插件各司其职：Excalidraw 画流程图和架构图，XMind-Linker 链接外部 XMind 文件，MxMind 在 Obsidian 内直接创建思维导图。

## Excalidraw（白板手绘）

### 用途

手绘风格的无限画布，适合画流程图、架构图、草图、头脑风暴。

### 核心功能

- 手绘风格：所有图形自动渲染为手绘效果
- 导出 PNG/SVG：可导出图片嵌入笔记
- 嵌入笔记：`.excalidraw` 文件可直接在笔记中预览
- 无限画布：支持缩放、平移
- 元素库：矩形、圆形、箭头、文字、图片

### 使用场景

- 画系统架构图
- 头脑风暴画布
- 教学演示配图
- 项目流程图

### 配置要点

- 文件保存位置：Vault 根目录或指定文件夹
- 自动导出 PNG：可设置保存时自动导出
- 模板：可创建 Excalidraw 模板

## XMind-Linker（XMind 链接器）

### 用途

在 Obsidian 笔记中链接外部 XMind 文件（`.xmind`），点击后在 XMind 软件中打开编辑。

### 使用场景

- 已有大量 XMind 文件，不想迁移
- 在 Obsidian 中统一管理各类文件

### 注意

需要安装 XMind 软件才能编辑。在 Obsidian 中只能预览，不能直接编辑 XMind 文件。

## MxMind（内置思维导图）

### 用途

在 Obsidian 内直接创建和编辑思维导图，无需外部软件。

### 核心功能

- 文本转导图：从 Markdown 大纲自动生成思维导图
- 内置编辑器：直接在 Obsidian 中拖拽编辑
- 导出：导出为图片或 PDF
- 双向链接：导图节点可链接到 Obsidian 笔记

### 使用场景

- 知识梳理（将笔记大纲可视化为导图）
- 会议纪要结构化
- 学习笔记整理

## 三者对比

| 维度 | Excalidraw | XMind-Linker | MxMind |
|------|------------|-------------|--------|
| 定位 | 白板绘图 | XMind 文件管理 | 思维导图 |
| 编辑方式 | 手绘拖拽 | 跳转 XMind 编辑 | 内置编辑 |
| 输出格式 | .excalidraw | .xmind | 内置格式 |
| 学习成本 | 低 | 低 | 中 |
| 依赖 | 无 | XMind 软件 | 无 |

## 可行动建议

- 用 Excalidraw 画一张本知识库的 4 层架构图
- 用 MxMind 将一篇长笔记的大纲转成思维导图，加速理解