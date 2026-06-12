---
title: "Understand-Anything 代码知识图谱"
tags: [GitHub, 开源, AI, 知识图谱, 代码分析, Agent, 可视化]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/Lum1104/Understand-Anything
zh-CN: https://github.com/Lum1104/Understand-Anything/blob/main/READMEs/README.zh-CN.md
related: [[ECC]]
summary: "将任意代码库/知识库转化为可交互知识图谱的 Claude Code 插件，Tree-sitter+LLM 混合分析+7 Agent 管道，支持 --language zh 中文输出，33.8k Stars"
---

# Understand-Anything 代码知识图谱

https://github.com/Lum1104/Understand-Anything

## 基本信息

**类型：** 工具（Claude Code Plugin）
**链接：** https://github.com/Lum1104/Understand-Anything
**主页 / 在线演示：** https://understand-anything.com | [Live Demo](https://understand-anything.com/demo/)
**适用领域：** 代码库理解、知识图谱可视化、团队 Onboarding、PR 变更影响分析
**推荐程度：** ★★★★★
**Stars：** ~33.8k | Fork 2.7k
**语言：** TypeScript
**许可证：** MIT
**社区：** [Discord](https://discord.gg/pydat66RY) | [YouTube 教程 (Better Stack)](https://www.youtube.com/watch?v=VmIUXVlt7_I)

## 一句话

> 目标不是用复杂图谱震撼你——而是默默告诉你每一块是怎么拼在一起的。

## 是什么

接手 20 万行陌生代码库时，Understand-Anything 通过多 Agent 管道自动分析项目，为每个文件、函数、类、依赖构建知识图谱，并提供交互式 Web Dashboard 可视化探索。支持 **`--language zh`** 生成中文内容。

核心思路：**教你的图 > 震撼你的图**（Graphs that teach > graphs that impress）。

## 快速开始

```bash
# 安装
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything

# 分析代码库（生成中文内容）
/understand --language zh

# 打开交互式 Dashboard
/understand-dashboard
```

其他支持平台：Codex、Cursor、Copilot、Gemini CLI、OpenCode、Windsurf、Trae、Cline、KIMI CLI 等，均提供 `install.sh` 脚本。

## 核心功能

### 三大视图

| 视图 | 说明 |
|------|------|
| **结构图谱** | 每个文件/函数/类是节点，可点击查看摘要、依赖关系和导览路径 |
| **业务领域视图** | 代码→业务流程映射，以水平图展示领域/流程/步骤（`/understand-domain`） |
| **知识库图谱** | `/understand-knowledge` 对 Karpathy 式 LLM Wiki 生成力导向图+社区聚类 |

### Dashboard 功能

- **🧭 Guided Tours**：按依赖顺序自动生成架构学习路径，自上而下学习整个系统
- **🔍 模糊+语义搜索**：搜「哪些部分处理认证？」即可跨图定位相关节点
- **📊 变更影响分析**：提交前查看改动会波及系统的哪些部分
- **🎭 角色自适应 UI**：根据用户类型（初级开发/PM/高级用户）调整信息密度
- **🏗️ 层级可视化**：按架构层自动分组（API/服务/数据/UI/系统工具），颜色编码
- **📚 语言概念**：12 种编程模式（泛型、闭包、装饰器等）在上下文中逐一解释

### 团队共享

图谱即 JSON——**提交一次，队友跳过管道直接用**：

```bash
# 提交（排除临时文件）
.understand-anything/intermediate/
.understand-anything/diff-overlay.json

# 大图（10MB+）用 git-lfs
git lfs track ".understand-anything/*.json"

# 增量自动更新
/understand --auto-update   # post-commit hook 自动补丁图谱
```

参考示例：[GoogleCloudPlatform/microservices-demo fork](https://github.com/Lum1104/microservices-demo)（Go/Java/Python/Node 多语言+已提交图谱）

## 技术架构

### Tree-sitter + LLM 混合分析

| 层 | 技术 | 职责 |
|----|------|------|
| **结构层**（确定性） | Tree-sitter | 解析源码→CST，提取 import/export/函数/类/调用点/继承关系，预解析为 `importMap`。相同输入→相同输出，可复现 |
| **语义层**（LLM） | Claude 等 | 基于结构+源码，生成英文摘要、标签、架构层归属、业务域映射、Guided Tours、语言概念标注 |

### 7 Agent 管道

| Agent | 职责 |
|-------|------|
| `project-scanner` | 扫描文件、检测语言和框架 |
| `file-analyzer` | 提取函数/类/import，生成节点和边（并行，最多 3 并发） |
| `architecture-analyzer` | 识别架构层级（API/服务/数据/UI 等） |
| `tour-builder` | 按依赖排序生成导览学习路径 |
| `graph-reviewer` | 验证图谱完整性和引用完整性 |
| `domain-analyzer` | 提取业务领域/流程/步骤（`/understand-domain` 专用） |
| `article-analyzer` | 从 Wiki 提取实体/论断/隐式关系（`/understand-knowledge` 专用） |

支持增量更新——仅重新分析上次运行后变更的文件。

## 适用场景

- 接手陌生大型代码库→30 分钟建立全局认知
- 团队 Onboarding→新成员自导航学习项目结构
- PR Review→查看改动影响范围
- 将 Obsidian/LLM Wiki 转化为可探索知识图谱（与本知识库高度相关）
- 持续维护→`--auto-update` 让图谱随代码演进同步

## 评价

- **优点**：Tree-sitter+LLM 分工清晰（结构可复现+语义有深度）、7 Agent 管道设计精良、Dashboard 功能丰富（Guided Tours/语义搜索/角色自适应）、图谱 Git 可提交实现团队零成本共享、增量更新实用、`--language zh` 对中文开发者友好
- **局限**：重度依赖 LLM API（大项目分析成本高）、需 Claude Code Plugin 环境（非独立 CLI）、并发限制 3（大项目首次分析较慢）
- **是否值得长期保留**：✅ 重点关注——知识图谱+AI 编程是趋势，`/understand-knowledge` 与本知识库的 Obsidian→图谱化方向直接对应
