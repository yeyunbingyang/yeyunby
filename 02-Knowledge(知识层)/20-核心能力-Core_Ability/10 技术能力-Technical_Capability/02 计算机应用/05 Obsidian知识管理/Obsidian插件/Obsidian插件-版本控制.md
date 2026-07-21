---
title: Obsidian Git 版本控制插件
domain: Core_Ability
tags: [Obsidian, 插件, Git, 版本控制, 备份]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系, Obsidian设置与个性化, Git版本控制-MOC]
summary: "obsidian-git 插件将 Git 版本控制集成到 Obsidian，支持自动定时备份、手动 commit/push/pull、差异视图，是知识库备份策略的核心执行组件"
---

# Obsidian Git 版本控制插件

## 一句话结论

> obsidian-git 让 Obsidian 的备份从"手动操作"变成"自动运行"——定时 commit + push 到远程仓库，笔记的每一次修改都有版本记录，随时可以回退。

## 核心功能

### 自动备份

- 定时自动 commit：按设定间隔自动提交变更
- 自动 push：commit 后自动推送到远程仓库
- 启动时 pull：打开 Obsidian 时自动拉取最新内容

### 手动操作

通过命令面板（`Ctrl+P`）可执行：

| 命令 | 作用 |
|------|------|
| `Git: Commit all changes` | 手动提交所有变更 |
| `Git: Push` | 推送到远程仓库 |
| `Git: Pull` | 拉取远程更新 |
| `Git: Open diff view` | 查看文件变更历史 |
| `Git: Stage file` | 暂存特定文件 |

### 差异视图

- 查看笔记的变更历史：谁在什么时候改了什么
- 对比当前版本与历史版本
- 合并冲突时可手动解决

### 侧边栏面板

在 Obsidian 右侧栏中显示 Git 源代码控制面板，可视化查看变更状态。

## 配置指南

设置 → Obsidian Git → 主要配置项：

| 配置项 | 建议值 | 说明 |
|--------|--------|------|
| 自动备份间隔 | 30 分钟 | 太频繁消耗资源，太稀疏丢失风险大 |
| 自动 Push | 开启 | commit 后自动推送 |
| 启动时 Pull | 开启 | 打开 Obsidian 时同步最新内容 |
| 提交信息模板 | `vault backup: {{date}}` | 使用日期占位符 |
| 推送前 Pull | 开启 | 先拉取再推送，减少冲突 |

## 当前知识库的备份配置

### `.gitignore` 排除规则

```
# 机器相关，频繁变化
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/types.json
.obsidian/graph.json

# 插件二进制（14MB+，通过社区插件市场重新安装）
.obsidian/plugins/

# 其他缓存
.obsidian/snippets/
.trash/
*.base

# 临时文件
.hermes/
.claudian/sessions/
node_modules/
```

### 已跟踪的配置文件（5 个）

| 文件 | 内容 | 重要性 |
|------|------|--------|
| `.obsidian/app.json` | 应用设置（附件路径、链接行为等） | 🔴 核心 |
| `.obsidian/appearance.json` | 外观设置（主题等） | 🟡 重要 |
| `.obsidian/community-plugins.json` | 插件列表（不含插件代码） | 🔴 核心 |
| `.obsidian/core-plugins.json` | 核心插件开关状态 | 🟡 重要 |
| `.obsidian/hotkeys.json` | 自定义快捷键 | 🟡 重要 |

### 设计原则

- **跟踪**：配置文件（JSON，几 KB）——这是你在新设备上恢复配置的唯二依据
- **排除**：二进制文件（插件代码 14MB+）、机器相关状态（workspace）、缓存（snippets、trash）
- **为什么**：插件代码可从社区市场重新下载，工作区状态因设备而异，无需版本控制

## 关键点

- 插件目录被 gitignore 排除，新设备需重新安装插件
- 5 个配置文件的跟踪是新设备恢复配置的关键
- 附件（图片等）默认随 Git 跟踪，大文件建议用 Git LFS 或外部存储

## 反例与边界

- ❌ 不要将密钥/Token 写入笔记（API Key 等）——它们会被 Git 推送
- ⚠️ 大附件（>10MB 的视频、PDF）会拖慢 Git 操作
- ⚠️ 合并冲突时不要直接编辑 `.obsidian/` 下的 JSON 文件——容易破坏格式

## 关联思考

- 与 `[[Git版本控制-MOC]]` 的关联——obsidian-git 是 Git 在 Obsidian 场景的封装
- 备份策略的完整说明见 [[Obsidian设置与个性化#备份策略]]

## 可行动建议

- 定期检查远程仓库确认备份正常（如每周一次）
- 查看一次 Git 差异视图，了解笔记的变更历史
- 如果附件较多，考虑在 `.gitignore` 中添加 `附件/` 或用 Git LFS