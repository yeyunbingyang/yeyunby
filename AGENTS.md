# AGENTS.md

本文档指导 Codex (Codex.ai/code) 在此仓库中的操作行为。

## 项目概述

这是一个基于 Obsidian 的个人知识管理库（知识库）。所有内容为中文 Markdown，带 YAML frontmatter。无构建步骤、无测试套件、无 lint——"代码"就是笔记本身。

## 仓库结构（4 层架构）

```
MOC知识地图.md              # 顶级导航入口 — 先读这个
00-System(支撑层)/          # 元规则、模板、工作流、仪表盘
   ├── Rules/               # 命名规范、标签系统、清空规则
   ├── Templates/           # 6 种笔记模板（02-Daily 另有 3 种）
   ├── Runtime_Data/        # 项目/技能仪表盘、笔记统计
   └── SCHEMA.md            # Frontmatter 规范
01-Inbox(入库层)/           # 临时收集区，目标每日清空（已合并入 01-日常流/流入/）
01-日常流(日常流层)/       # 日记、周复盘、阶段规划。子目录：流入/、日记/、周复盘/、阶段规划/
02-Knowledge(知识层)/       # 核心知识，按两大域组织：
   ├── 10-IT技术-IT_Technology/  # 技术工程
   └── 20-核心能力-Core_Ability/ # 能力与认知（含AI应用/思维/人文）
03-Resources(资源层)/       # 外部资源（GitHub项目、软件工具、课程、网站、素材、AI）
```

## 核心架构模式

- **MOC（内容地图）**：每个领域有一个 `领域名-MOC.md` 作为导航索引。MOC 只做链接和摘要，不写长文。当一个主题积累超过 10 条链接时，拆出子 MOC。
- **Frontmatter**：每条知识笔记都必须按 `00-System(支撑层)/SCHEMA.md` 要求包含 YAML frontmatter。关键字段：`summary`（一句话结论，不是"这篇笔记关于什么"）。`status` 流转：`计划 → 草稿 → 稳定`，修订时走 `改进`，过时走 `归档`。
- **Domain 合法值**：`IT_Technology`、`Cognition`、`Core_Ability` — 这三个是 `domain` frontmatter 仅有的合法值。
- **命名规则**：中文命名，英文专有名词保持英文。不用空格，用 `-` 连接多词。文件名不含日期。MOC 文件以 `-MOC.md` 结尾，模板文件以 `-模板.md` 结尾。
- **Templater**：模板使用 Templater 语法（`<% tp.date.now("...") %>`），不要替换为硬编码日期。
- **Dataview**：MOC 使用 Dataview 查询按 status/domain/tags 自动聚合笔记。查询 FROM 子句使用 vault 的实际目录路径（如 `"02-Knowledge(知识层)"`），不含 `KnowledgeBase/` 前缀。

## 编辑规范

- 内部链接使用 `[[wikilink]]` 语法，不用 Markdown 链接。
- 新建知识笔记时，必须： (1) 添加 frontmatter，(2) 链接回相关 MOC。
- 向 MOC 添加笔记时，同时更新 MOC 的链接列表和（如适用）Dataview 查询。
- `01-日常流(日常流层)/日记-模板.md` 和 `00-System(支撑层)/Templates/日记-模板.md` 必须保持同步——对其中一个的任何修改都要应用到另一个。
- 归档先于删除：将 status 改为 `归档`，保留在原位置（或移入 03-Resources/归档），可选在原位置保留重定向注释。
- `MOC知识地图.md` 是整个目录树的唯一真相来源——添加或重组织目录时保持更新。

## 当前状态

- **运维云原生** 是最完善的领域（7 个模块，~60 条笔记，大多缺少 frontmatter——它们是任务驱动的实践指南）。
- **认知层** 和 **核心能力** 是骨架：MOC 已存在，但几乎无实际知识笔记。
- 复盘体系已整合：每日/周用 KPT，阶段用 GRAI，系统级元复盘用 PDCA。参见 `02-Knowledge/20-核心能力-Core_Ability/50 认知思维-Cognitive_Thinking/03-学习方法论/复盘指南.md`。
