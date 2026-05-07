# 知识库说明

基于 Obsidian 构建的多领域 MD 知识库，AI 智能体通过此文件了解整体结构。

## 目录结构

```
KnowledgeBase/
├── 01-MOC.md       # 顶级知识库导航入口
├── 00-System/      # 元规则、规范、工作流、复盘与系统说明
│   └── Templates/  # 笔记模板
├── 01-Inbox/       # 新内容落点，每日整理后移入对应目录
├── 03-Knowledge/   # 核心知识（按领域存放，领域/笔记.md）
├── 05-Resources/   # 工具、素材、课程、网站和 AI 平台收集
└── 08-Daily/       # 日记
```

## AI 智能体检索路径

1. 读取本文件 → 了解结构
2. 读取 `01-MOC.md` → 确定目录与领域入口
3. 进入 `03-Knowledge/<编号-领域>/<领域> MOC.md` → 查看该领域导航与重点主题
4. 进入 `03-Knowledge/<编号-领域>/` → 读取具体笔记
5. 读取笔记 frontmatter 中的 `summary` 字段 → 语义匹配

## 规范文档

- 笔记 frontmatter 规范：`00-System/SCHEMA.md`
- 知识库优化方案：`00-System/知识库优化方案.md`
- 知识库操作工作流：`00-System/知识库操作工作流.md`
- 顶级知识地图：`01-MOC.md`
