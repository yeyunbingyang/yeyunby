# 知识库说明

基于 Obsidian 构建的多领域 MD 知识库，AI 智能体通过此文件了解整体结构。

## 目录结构

```
MOC知识地图.md               # 顶级知识库导航入口
00-System(支撑层)/           # 元规则、规范、工作流、仪表盘与系统说明
├── Rules/                   # 命名规范、标签系统、清空规则
├── Templates/               # 笔记模板 (6种)
└── Runtime_Data/            # 项目/技能仪表盘、笔记统计
01-Inbox(入库层)/            # 新内容落点，每日整理后移入对应目录（已合并入 01-日常流/流入/）
01-日常流(日常流层)/        # 日记与规划（含流入/、日记/、周复盘/、阶段规划/）
02-Knowledge(知识层)/        # 核心知识（两大域：IT技术/核心能力）
  ├── 10-IT技术-IT_Technology/  # 技术工程
  └── 20-核心能力-Core_Ability/ # 能力与认知
03-Resources(资源层)/        # 工具、素材、课程、网站和 AI 平台收集

```

## AI 智能体检索路径

1. 读取本文件 → 了解结构
2. 读取 `MOC知识地图.md` → 确定目录与领域入口
3. 进入 `02-Knowledge/<编号-领域>/<领域> MOC.md` → 查看该领域导航与重点主题
4. 进入 `02-Knowledge/<编号-领域>/` → 读取具体笔记
5. 读取笔记 frontmatter 中的 `summary` 字段 → 语义匹配

## 规范文档

| 文档             | 路径                                                     | 说明                      |
| -------------- | ------------------------------------------------------ | ----------------------- |
| Frontmatter 规范 | [SCHEMA.md](SCHEMA.md)                                 | 笔记 frontmatter 字段定义与合法值 |
| 命名规范           | [Rules/Naming_Standards.md](Rules/Naming_Standards.md) | 文件、文件夹、MOC、模板命名规则       |
| 标签系统           | [Rules/Tag_System.md](Rules/Tag_System.md)             | 标签分类与使用规则               |
| 清空规则           | [Rules/Clearance_Rules.md](Rules/Clearance_Rules.md)   | Inbox 清理频率与归档触发条件       |
| 操作工作流          | [知识库操作工作流.md](知识库操作工作流.md)                             | 从收集到复盘的完整工作流            |
| 优化方案           | [知识库优化方案.md](知识库优化方案.md)                               | 知识库设计目标与架构说明            |
