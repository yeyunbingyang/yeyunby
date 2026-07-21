---
title: Obsidian AI 与模板插件
domain: Core_Ability
tags: [Obsidian, 插件, AI, 模板, Claudian, Templater]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系, Obsidian设置与个性化]
summary: "Claudian 将 Claude AI 集成到 Obsidian 编辑流程，Templater 提供高级模板语法（当前未启用但建议启用），SuperMind 定位 AI 增强知识管理（与 Claudian 重叠，待评估）"
---

# Obsidian AI 与模板插件

## 一句话结论

> Claudian 让 AI 直接进入笔记编辑流程，Templater 让模板支持动态变量——两者搭配可实现"AI 生成 + 模板结构化"的高效工作流。

## Claudian（AI 对话插件）

### 用途

在 Obsidian 侧边栏内直接调用 Claude AI，辅助写作、内容生成、总结、翻译。

### 核心功能

- 对话式 AI：侧边栏聊天界面，与 Claude 对话
- 内容生成：选中文本 → 让 AI 扩展/总结/改写
- 上下文感知：可引用当前笔记内容作为对话上下文
- 会话缓存：`.claudian/sessions/`（已通过 gitignore 排除）

### 使用场景

- 笔记润色：选中草稿 → 让 AI 优化表达
- 知识提炼：选中长笔记 → 让 AI 提取关键结论
- 想法拓展：写下一个想法 → 让 AI 从多角度展开
- 翻译：选中中文 → 翻译为英文（或反过来）

### 配置

- 需要在设置中配置 API Key 或使用 Claude Code 集成
- 会话缓存路径：`.claudian/sessions/`

## Templater（模板引擎）

### 状态

⚠️ **已安装但未启用**——建议启用

### 为什么需要它

Obsidian 核心模板插件只能插入**静态内容**。Templater 支持动态变量：

```
核心模板：         标题：{{title}}              → 输出：标题：（空）
Templater：        标题：<% tp.file.title %>    → 输出：标题：Obsidian AI 与模板插件
```

### 核心语法

| 语法 | 作用 | 示例 |
|------|------|------|
| `<% tp.date.now("YYYY-MM-DD") %>` | 插入当前日期 | `2026-07-21` |
| `<% tp.file.title %>` | 插入当前笔记标题 | `Obsidian AI 与模板插件` |
| `<% tp.file.folder() %>` | 插入当前文件夹路径 | `Obsidian知识管理/Obsidian插件/` |
| `<% tp.file.cursor() %>` | 设置光标位置 | 新建笔记后光标定位 |
| `<% tp.system.prompt() %>` | 弹出输入框 | 用户输入后插入内容 |

### 启用后的影响

本知识库的模板（`00-System(支撑层)/Templates/` 下的 6 个模板）使用了 Templater 语法：

```yaml
created: <% tp.date.now("YYYY-MM-DD") %>
```

当前这些动态日期**不会生效**（因为 Templater 未启用），启用后模板中的 `tp.date.now()` 才会自动替换为当前日期。

### 建议

**立即启用 Templater**。启用后不会影响现有笔记，只会让新创建的笔记模板正常工作。

## SuperMind（AI 知识管理）

### 状态

⚠️ **已安装但未启用**——待评估

### 定位

AI 增强的知识管理，包括：
- 思维导图 AI 生成
- Markdown ↔ XMind 格式转换
- AI 驱动的知识关联

### 与 Claudian 的差异

| 维度 | Claudian | SuperMind |
|------|----------|-----------|
| 定位 | 通用 AI 对话 | AI 知识管理 |
| 核心功能 | 写作、总结、翻译 | 思维导图 AI、格式转换 |
| 与 Claude 的集成 | 深度集成 | 通过 API 调用 |
| 是否必要 | 已启用，有用 | 与 Claudian 功能重叠 |

### 建议

如果常用思维导图且希望 AI 自动生成，可启用 SuperMind。否则，保持禁用，避免功能冗余。

## 可行动建议

- **立即启用 Templater**（设置 → 社区插件 → Templater → 启用）
- 启用 Templater 后，用模板创建一篇测试笔记，验证 `tp.date.now()` 生效
- Claudian 的会话缓存无需备份，换设备后会重新生成