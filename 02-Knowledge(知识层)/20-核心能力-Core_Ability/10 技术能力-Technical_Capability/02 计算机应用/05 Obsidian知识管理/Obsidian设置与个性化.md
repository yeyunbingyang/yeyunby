---
title: Obsidian 设置与个性化
domain: Core_Ability
tags: [Obsidian, 设置, 个性化, 备份, 恢复, 配置]
status: 稳定
created: 2026-07-21
updated: 2026-07-21
related: [Obsidian知识管理-MOC, Obsidian插件体系, Obsidian插件-版本控制]
summary: "当前 Obsidian 配置全记录：moonstone 主题、附件 ./附件 子文件夹、alwaysUpdateLinks 自动更新链接、Alt+B 自定义快捷键，以及完整的备份策略和新系统 8 步恢复流程"
---

# Obsidian 设置与个性化

## 一句话结论

> 当前 Obsidian 配置以简洁实用为原则——默认主题，少量自定义，重点投入在备份策略上。这篇笔记是换电脑时恢复配置的唯一参考。

---

## 外观设置

| 设置项 | 当前值 | 说明 |
|--------|--------|------|
| 主题 | moonstone | Obsidian 默认浅色主题，简洁清晰 |
| 界面语言 | 中文 | — |
| CSS 代码片段 | 无 | 未使用自定义 CSS |

## 编辑器设置

| 设置项 | 当前值 | 说明 |
|--------|--------|------|
| 默认编辑模式 | 实时预览 | 编辑时即时渲染 Markdown |
| 显示行号 | 关闭 | `showLineNumber: false` |
| 可读行宽 | 关闭 | `readableLineLength: false`，不限制行宽 |
| 严格换行 | 关闭 | `strictLineBreaks: false`，使用宽松换行 |
| 拼写检查 | 默认 | — |

## 文件与链接

| 设置项 | 当前值 | 说明 |
|--------|--------|------|
| 新建笔记位置 | 当前文件夹 | `newFileLocation: "current"` |
| 附件位置 | `./附件` 子文件夹 | `attachmentFolderPath: "./附件"`，每个文件夹的附件独立存放 |
| 自动更新内部链接 | **开启** | `alwaysUpdateLinks: true`，重命名笔记时自动更新所有引用 |
| 删除确认 | 关闭 | `promptDelete: false`，删除不弹确认框 |
| 新文件默认位置 | 06-Archive(归档层) | `newFileFolderPath: "06-Archive(归档层)"` |

## 核心插件配置

### 日记

- 日记路径：`01-日常流(日常流层)/日记/`
- 日期格式：`YYYY-MM-DD`
- 模板：使用 `日记-模板.md`

### 模板

- 模板文件夹：`00-System(支撑层)/Templates/`
- 模板引擎：Templater（已安装，建议启用）

### 文件恢复

- 快照功能：已启用
- 快照间隔：默认（Obsidian 自动管理）

### 其他

- **Sync**：已启用（Obsidian 核心同步功能）
- **Bases**：已启用（数据库视图功能）
- **图谱**：已配置，中心强度 0.519，排斥力 10

## 自定义快捷键

| 快捷键 | 命令 | 说明 |
|--------|------|------|
| `Alt+B` | `editor:insert-callout` | 插入 callout 标注块（当前唯一自定义） |

> 所有快捷键定义在 `.obsidian/hotkeys.json`（已纳入 Git 版本控制）。

---

## 备份策略

### 备份架构

```
┌─────────────────┐     自动 commit + push      ┌─────────────────┐
│  Obsidian Vault  │ ──────────────────────────→ │  GitHub 远程仓库  │
│  (本地文件夹)     │ ←────── 启动时 pull ─────── │  (远程备份)       │
└─────────────────┘                              └─────────────────┘
      执行者：obsidian-git 插件
```

### 跟踪什么、排除什么、为什么

| 类别 | 文件/目录 | 是否跟踪 | 原因 |
|------|----------|----------|------|
| **配置** | `app.json` | ✅ 跟踪 | 核心设置：附件路径、链接行为、编辑行为 |
| **配置** | `appearance.json` | ✅ 跟踪 | 外观设置：主题选择 |
| **配置** | `community-plugins.json` | ✅ 跟踪 | 插件列表：新设备恢复时自动安装的依据 |
| **配置** | `core-plugins.json` | ✅ 跟踪 | 核心插件开关状态 |
| **配置** | `hotkeys.json` | ✅ 跟踪 | 自定义快捷键 |
| **插件代码** | `plugins/` | ❌ 排除 | 二进制文件 14MB+，从社区市场重新下载 |
| **工作区** | `workspace.json` | ❌ 排除 | 机器相关：打开的标签页、面板布局 |
| **工作区** | `workspace-mobile.json` | ❌ 排除 | 移动端工作区状态 |
| **类型** | `types.json` | ❌ 排除 | 属性类型定义，可重建 |
| **图谱** | `graph.json` | ❌ 排除 | 图谱渲染状态，机器相关 |
| **CSS** | `snippets/` | ❌ 排除 | CSS 片段缓存 |
| **回收站** | `.trash/` | ❌ 排除 | 已删除文件，无需备份 |
| **数据库** | `*.base` | ❌ 排除 | Bases 缓存文件，可重建 |
| **会话** | `.claudian/sessions/` | ❌ 排除 | AI 对话缓存 |
| **Agent** | `.hermes/` | ❌ 排除 | Hermes Agent 本地文件 |

### .gitignore 完整内容

```gitignore
# 系统文件
.DS_Store
Thumbs.db
desktop.ini

# 临时文件
*.tmp
*.log
*.bak

# Obsidian 工作区（机器相关）
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/types.json
.obsidian/graph.json

# Obsidian 插件二进制（从社区市场重新安装）
.obsidian/plugins/

# 其他缓存
.obsidian/snippets/
.trash/
*.base

# Agent 会话
.hermes/
.claudian/sessions/

# Node.js
node_modules/
```

### 备份检查清单

- [ ] 最近一次 commit 是否成功？（检查 Git 面板）
- [ ] 远程仓库是否同步？（检查 GitHub）
- [ ] 5 个配置文件是否在跟踪中？（`git status .obsidian/*.json`）
- [ ] 是否有大文件被误跟踪？（`git ls-files -z | xargs -0 ls -l | sort -nr | head -10`）

---

## 新系统快速恢复

> 换电脑或重装系统后，按以下 8 步恢复完整工作环境。

### 第 1 步：安装基础软件

- 安装 [Obsidian](https://obsidian.md/download)（Windows/Mac/Linux）
- 安装 [Git](https://git-scm.com/downloads)（用于 clone 仓库 + obsidian-git 插件）

### 第 2 步：克隆知识库

```bash
git clone <你的远程仓库地址> <本地路径>
# 例如：git clone git@github.com:yeyunby/knowledge-base.git D:/KMS/yeyunby
```

> 克隆后 `.obsidian/` 下只有 5 个配置文件，没有插件文件夹。

### 第 3 步：打开 Vault

1. 打开 Obsidian
2. 点击"打开文件夹作为 Vault"
3. 选择克隆到本地的知识库文件夹
4. 如果提示"安全模式"，点击"信任作者并启用插件"

### 第 4 步：关闭安全模式

1. 设置 → 社区插件 → 关闭"安全模式"
2. Obsidian 会读取 `community-plugins.json`
3. 自动弹出提示："检测到 X 个未安装的插件，是否安装？"
4. 点击 **"全部安装"**
5. 等待下载完成（约 1-2 分钟，取决于网络）

### 第 5 步：手动配置插件

> ⚠️ **注意**：插件代码已重新安装，但插件配置（`data.json`）没有被 Git 跟踪，需要手动重新配置。

需要重新配置的插件：

| 插件 | 需要配置的内容 | 参考 |
|------|---------------|------|
| Dataview | 无需配置，开箱即用 | [[Obsidian插件-Dataview]] |
| Obsidian Git | 自动备份间隔、commit 信息模板、push 设置 | [[Obsidian插件-版本控制]] |
| Calendar | 日记路径 | [[Obsidian插件-任务与日历]] |
| Tasks | 全局任务过滤器 | [[Obsidian插件-任务与日历]] |
| Claudian | API 配置 | [[Obsidian插件-AI与模板]] |

### 第 6 步：恢复核心插件状态

1. 设置 → 核心插件
2. 确认 `core-plugins.json` 中的开关状态已生效
3. 重点检查：日记、模板、文件恢复、Sync、Bases 是否已启用

### 第 7 步：恢复快捷键

- `hotkeys.json` 已随 Git 跟踪，快捷键自动生效
- 在设置 → 快捷键中确认 `Alt+B` 已绑定

### 第 8 步：验证恢复完成

- [ ] 所有社区插件已安装并启用（9 个）
- [ ] 核心插件开关状态正确
- [ ] 打开一篇笔记，wikilink 链接可点击
- [ ] Git 面板显示正常，可以手动 commit
- [ ] 日历面板显示正确
- [ ] 快捷键 `Alt+B` 可插入 callout

### 恢复时间估算

| 步骤 | 预计时间 |
|------|----------|
| 安装软件 | 5 分钟 |
| 克隆仓库 | 1-5 分钟（取决于仓库大小） |
| 自动安装插件 | 1-2 分钟 |
| 手动配置插件 | 5-10 分钟 |
| 验证 | 2 分钟 |
| **合计** | **15-25 分钟** |

---

## 配置文件清单

| 文件                       | 说明               | Git 跟踪 |
| ------------------------ | ---------------- | ------ |
| `app.json`               | 应用设置（附件、链接、编辑行为） | ✅      |
| `appearance.json`        | 外观设置（主题）         | ✅      |
| `community-plugins.json` | 社区插件列表           | ✅      |
| `core-plugins.json`      | 核心插件开关状态         | ✅      |
| `hotkeys.json`           | 自定义快捷键           | ✅      |
| `workspace.json`         | 工作区布局（标签页、面板）    | ❌      |
| `types.json`             | 属性类型定义           | ❌      |
| `graph.json`             | 图谱渲染状态           | ❌      |

## 可行动建议

- 将这篇笔记加入书签，换电脑时直接参考
- 定期执行"备份检查清单"
- 修改 Obsidian 设置后，回来更新这篇笔记
- 考虑创建一个"设置快照"笔记，记录每次重要配置变更的日期和原因
- 在另一台设备上实际执行一次恢复流程，验证文档的准确性