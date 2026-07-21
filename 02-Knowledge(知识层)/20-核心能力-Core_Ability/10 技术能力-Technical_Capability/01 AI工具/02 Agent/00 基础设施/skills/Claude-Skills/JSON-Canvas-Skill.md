---
title: json-canvas — JSON Canvas 画布文件手册
description: 创建和编辑 .canvas 文件，包含节点（文本/文件/链接/分组）、边（连线）和颜色。
aliases:
  - json-canvas skill
tags:
  - obsidian
  - canvas
  - json
  - claude-code
  - mindmap
created: 2026-06-22
updated: 2026-06-22
status: 稳定
domain: Core_Ability
source: kepano/obsidian-skills
install: npx skills add kepano/obsidian-skills@json-canvas
links:
  - jsoncanvas.org
  - github/obsidianmd/jsoncanvas
---

# json-canvas 使用手册

## 概述

操作 `.canvas` 文件，遵循 [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/) 规范。用于创建思维导图、项目看板、流程图等可视化结构。

## 基本结构

```json
{
  "nodes": [],
  "edges": []
}
```

- `nodes` — 节点数组
- `edges` — 边数组，连接节点

## 工作流

### 1. 创建新 Canvas

1. 创建一个 `.canvas` 文件
2. 为每个节点生成 16 位十六进制 ID（如 `"6f0ad84f44ce9c17"`）
3. 添加节点（必填：`id`, `type`, `x`, `y`, `width`, `height`）
4. 添加边（`fromNode` → `toNode`）
5. 验证：所有 ID 唯一，边引用节点存在

### 2. 添加节点到已有 Canvas

1. 读取并解析 `.canvas` JSON
2. 生成不冲突的唯一 ID
3. 选择位置（间距 50-100px）
4. 追加到 `nodes` 数组
5. 可选添加边

### 3. 连接两个节点

1. 确定源和目标节点 ID
2. 生成边 ID
3. 设置 `fromNode` 和 `toNode`
4. 可选设 `fromSide`/`toSide` 锚点

## 节点类型

### 通用属性

| 属性 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `id` | 是 | string | 唯一 16 位十六进制 ID |
| `type` | 是 | string | `text`, `file`, `link`, `group` |
| `x`, `y` | 是 | integer | 位置（左上角） |
| `width`, `height` | 是 | integer | 尺寸（像素） |
| `color` | 否 | canvasColor | 预设 `"1"`-`"6"` 或 hex |

### Text 节点

```json
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0, "y": 0,
  "width": 400, "height": 200,
  "text": "# 标题\n\n**Markdown** 内容。"
}
```

> ⚠️ **换行陷阱**：使用 `\n`（不是 `\\n`），否则 Obsidian 渲染成字面量 `\` 和 `n`。

### File 节点

```json
{
  "id": "a1b2c3d4e5f67890",
  "type": "file",
  "x": 500, "y": 0,
  "width": 400, "height": 300,
  "file": "附件/图片.png",
  "subpath": "#标题"
}
```

### Link 节点

```json
{
  "id": "c3d4e5f678901234",
  "type": "link",
  "x": 1000, "y": 0,
  "width": 400, "height": 200,
  "url": "https://obsidian.md"
}
```

### Group 节点（容器）

```json
{
  "id": "d4e5f6789012345a",
  "type": "group",
  "x": -50, "y": -50,
  "width": 1000, "height": 600,
  "label": "项目概览",
  "color": "4",
  "background": "路径/背景.png",
  "backgroundStyle": "cover"
}
```

## 边 (Edges)

| 属性 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| `id` | 是 | string | — | 唯一 ID |
| `fromNode` | 是 | string | — | 源节点 ID |
| `fromSide` | 否 | string | — | `top`, `right`, `bottom`, `left` |
| `fromEnd` | 否 | string | `none` | `none`, `arrow` |
| `toNode` | 是 | string | — | 目标节点 ID |
| `toSide` | 否 | string | — | `top`, `right`, `bottom`, `left` |
| `toEnd` | 否 | string | `arrow` | `none`, `arrow` |
| `color` | 否 | canvasColor | — | 颜色 |
| `label` | 否 | string | — | 文字标签 |

```json
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "toNode": "a1b2c3d4e5f67890",
  "toSide": "left",
  "toEnd": "arrow",
  "label": "指向"
}
```

## 颜色预设

| 预设 | 颜色 |
|------|------|
| `"1"` | 红 |
| `"2"` | 橙 |
| `"3"` | 黄 |
| `"4"` | 绿 |
| `"5"` | 青 |
| `"6"` | 紫 |

## 布局指南

- 坐标可以为负（画布无限扩展）
- `x` 向右增加，`y` 向下增加
- 节点间距 50-100px，组内填充 20-50px
- 建议对齐网格（10 或 20 的倍数）

| 类型 | 建议宽 | 建议高 |
|------|--------|--------|
| 小文本 | 200-300 | 80-150 |
| 中文本 | 300-450 | 150-300 |
| 大文本 | 400-600 | 300-500 |
| 文件预览 | 300-500 | 200-400 |
| 链接预览 | 250-400 | 100-200 |

## 验证清单

1. 所有 `id` 在 nodes 和 edges 中唯一
2. 每个 `fromNode` 和 `toNode` 必须有对应的节点
3. 每个节点类型的必填字段齐全
4. `type` 为 `text`/`file`/`link`/`group`
5. `fromSide`/`toSide` 为 `top`/`right`/`bottom`/`left`
6. `fromEnd`/`toEnd` 为 `none`/`arrow`
7. 颜色为 `"1"`-`"6"` 或 hex
8. JSON 合法可解析

## 参考

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)
- [JSON Canvas GitHub](https://github.com/obsidianmd/jsoncanvas)
