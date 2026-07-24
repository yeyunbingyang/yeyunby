---
title: Obsidian Agent 操作指南
description: AI 代理操作 Obsidian 知识库的完整手册——CLI 命令、Vault 组织规范、Bases 数据库视图、Canvas 画布、Defuddle 网页转 Markdown
aliases:
  - obsidian-cli
  - obsidian-vault
  - obsidian-bases
  - json-canvas
  - defuddle
tags:
  - obsidian
  - cli
  - claude-code
  - vault-organization
  - bases
  - canvas
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
sources:
  - kepano/obsidian-skills (obsidian-cli, obsidian-bases, json-canvas, defuddle)
  - mattpocock/skills (obsidian-vault)
summary: "AI 代理操作 Obsidian 的知识库完整手册——通过 CLI 管理笔记、按规范组织 Vault、用 Bases 创建数据库视图、用 Canvas 制作思维导图、用 Defuddle 提取网页内容。6 个独立 Skills 的整合版。"
source: "https://obsidian.md/help/"
related: []
verified: 2026-07-25
review_after: 2026-10-25
---

# Obsidian Agent 操作指南

> 本文汇总了 AI 代理操作 Obsidian 知识库的 5 类核心技能，从命令行到高级视图全覆盖。

## 安装命令

```bash
# 安装全部 6 个原始 Skill（如使用 Claude Code）
npx skills add mattpocock/skills@obsidian-vault -g -y
npx skills add kepano/obsidian-skills@obsidian-markdown -g -y
npx skills add kepano/obsidian-skills@obsidian-cli -g -y
npx skills add kepano/obsidian-skills@obsidian-bases -g -y
npx skills add kepano/obsidian-skills@json-canvas -g -y
npx skills add kepano/obsidian-skills@defuddle -g -y
```

---

## 第一章：CLI 命令操作（obsidian-cli）

通过 `obsidian` 命令与**正在运行**的 Obsidian 实例交互。要求 Obsidian 保持打开。

### 语法

- **参数**：使用 `=` 赋值，空格用引号
- **布尔标志**：直接写，不需要值

```bash
obsidian create name="我的笔记" content="Hello world" silent overwrite
```

### 文件定位

- `file=<名称>`：按 wikilink 方式解析
- `path=<路径>`：从 vault 根目录精确路径
- 不加两者 → 当前活动文件

### 常用命令

```bash
obsidian read file="笔记名"
obsidian create name="新笔记" content="# Hello" template="模板" silent
obsidian append file="笔记名" content="新行"
obsidian search query="搜索词" limit=10
obsidian daily:read
obsidian property:set name="status" value="done" file="笔记名"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="笔记名"
```

### 插件开发

```bash
obsidian plugin:reload id=my-plugin
obsidian dev:errors
obsidian dev:screenshot path=screenshot.png
obsidian dev:console level=error
obsidian dev:dom selector=".workspace-leaf" text
```

**参考**：`obsidian help` / https://help.obsidian.md/cli

---

## 第二章：Vault 组织规范（obsidian-vault）

- **索引笔记**：聚合相关主题（`XX-MOC.md`），作为导航入口
- **链接**：使用 `[[wikilinks]]` 语法
- **注意**：本知识库已有自己的 4 层架构（支撑层/日常流层/知识层/资源层），该 skill 的通用方法已被吸收至 CLAUDE.md

---

## 第三章：Bases 数据库视图（obsidian-bases）

Bases 将笔记转化为类数据库视图（表格/卡片/列表），文件扩展名为 `.base`。

### 工作流

1. 创建 `.base` 文件 → 2. 定义过滤范围 → 3. 添加公式 → 4. 配置视图 → 5. 在 Obsidian 中打开验证

### 过滤语法

```yaml
filters:
  and:
    - 'status == "active"'
    - not:
        - 'file.hasTag("archived")'
```

### 公式语法

```yaml
formulas:
  总价: "price * quantity"
  状态图标: 'if(done, "✅", "⏳")'
  已创建天数: '(now() - file.ctime).days'
  截止剩余: 'if(due, (date(due) - today()).days, "")'
```

> ⚠️ Duration 陷阱：两日期相减得到 Duration 类型，必须先 `.days` 再 `.round(0)`

### 视图类型

- **表格 (Table)** — 可排序、分组、汇总
- **卡片 (Cards)** — 属性排列显示
- **列表 (List)** — 简洁列表
- **地图 (Map)** — 需 Maps 插件

### 嵌入 Bases

```markdown
![[MyBase.base]]
![[MyBase.base#视图名]]
```

**参考**：https://help.obsidian.md/bases/syntax

---

## 第四章：Canvas 画布（json-canvas）

操作 `.canvas` 文件，遵循 JSON Canvas Spec 1.0。

### 基本结构

```json
{
  "nodes": [{ "id": "16位hex", "type": "text|file|link|group", "x": 0, "y": 0, "width": 400, "height": 200 }],
  "edges": [{ "id": "16位hex", "fromNode": "...", "toNode": "..." }]
}
```

### 节点类型

| 类型 | 说明 |
|------|------|
| `text` | Markdown 文本节点 |
| `file` | 引用仓库文件（支持 `subpath`） |
| `link` | URL 链接 |
| `group` | 容器，带 `label` 和 `background` |

### 边 (Edges)

| 属性 | 说明 |
|------|------|
| `fromNode` / `toNode` | 源/目标节点 ID |
| `fromSide` / `toSide` | `top\|right\|bottom\|left` |
| `fromEnd` / `toEnd` | `none\|arrow` |
| `label` | 文字标签 |

**颜色预设**：`"1"`-`"6"`（红橙黄绿青紫）

> ⚠️ 换行陷阱：使用 `\n` 不是 `\\n`

**参考**：https://jsoncanvas.org/spec/1.0/

---

## 第五章：Defuddle 网页转 Markdown

```bash
npm install -g defuddle
defuddle parse <url> --md -o content.md
defuddle parse <url> -p title
```

| 标志 | 格式 |
|------|------|
| `--md` | Markdown（推荐） |
| `--json` | JSON（含 HTML 和 Markdown） |
| `-p <名称>` | 特定元数据 |

**适用**：阅读在线文章后存入知识库、抓取文档作为参考。

---

## 关联笔记

- [[Obsidian-Markdown语法参考]] — Obsidian 风味 Markdown 语法指南
- [[Agent平台-MOC]] — Agent 工具层总导航
