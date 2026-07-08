---
title: "Awesome Codex Skills 精选技能列表"
tags: [GitHub, 开源, AI, Codex, Skills, awesome-list]
type: 资源索引
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/ComposioHQ/awesome-codex-skills
related: [[agent-skills-生产级工程技能包], [ECC-Agent全套配置系统]]
summary: "Composio 官方维护的 Codex Skills 精选列表，覆盖开发/协作/写作/数据分析/元工具 5 大类，含 Skill 安装器和创建模板，11.8k Stars"
---

# Awesome Codex Skills 精选技能列表

https://github.com/ComposioHQ/awesome-codex-skills

## 基本信息

**类型：** 资源索引（Awesome List）
**链接：** https://github.com/ComposioHQ/awesome-codex-skills
**适用领域：** Codex Skills 发现与安装、工作流自动化
**推荐程度：** ★★★★☆
**Stars：** ~11.8k | Fork 1.1k
**维护方：** ComposioHQ

## 是什么

Composio 官方维护的 Codex Skills 精选列表（Awesome List 格式）。收录了社区贡献的实用 Codex 技能，覆盖开发工具、协作、写作、数据分析、元工具五大类。附带 Skill 安装器和创建模板，降低 Skill 的发现和安装门槛。

## 快速开始

```bash
git clone https://github.com/ComposioHQ/awesome-codex-skills.git
cd awesome-codex-skills

# 安装单个技能到 ~/.codex/skills
python skill-installer/scripts/install-skill-from-github.py \
  --repo ComposioHQ/awesome-codex-skills \
  --path meeting-notes-and-actions
```

安装后重启 Codex，技能根据 `SKILL.md` 中的 `description` 自动触发。

## 核心功能

### 五大技能分类

| 分类 | 代表技能 | 说明 |
|------|----------|------|
| **开发与代码工具** | brooks-lint, codebase-migrate, codebase-recon, create-plan | 代码审查（六本经典工程书为基准）、大规模迁移重构、Git 历史热点分析 |
| **协作与效率** | meeting-notes-and-actions, slack-message-scheduler, github-issue-create | 会议纪要生成、Slack 消息调度、GitHub Issue 自动化 |
| **写作与沟通** | unslop | 去除 AI 写作痕迹（三段式、破折号滥用、讨好式开头） |
| **数据分析** | spreadsheet-formula-helper, datadog-logs, lead-research-assistant | Excel 公式助手、Datadog 日志查询、线索研究 |
| **元工具** | brand-guidelines, skill-installer, skill-creator, template-skill | 品牌规范应用、Skill 安装器、创建指南、模板 |

### Skill 结构规范

```
skill-name/
├── SKILL.md          # 必需：指令 + YAML frontmatter
├── scripts/          # 可选：确定性操作的辅助脚本
├── references/       # 可选：按需加载的长文档
└── assets/           # 可选：模板或输出文件
```

### Skill 安装器

项目自带的安装器支持从任意 GitHub 仓库安装 Skill：

```bash
python skill-installer/scripts/install-skill-from-github.py \
  --repo <owner/repo> --path <skill-path> --name <skill-name>
```

## 适用场景

- 发现和试用社区 Codex Skills
- 参考 Skill 结构规范创建自己的 Skill（`template-skill/` + `skill-creator/`）
- 快速安装常用自动化工作流（会议纪要、Issue 管理、日志查询等）
- 了解 Codex Skill 生态现状和最佳实践

## 评价

- **优点**：Awesome List 格式便于发现、自带安装器降低门槛、Skill 模板+创建指南完善、Composio 官方维护质量有保障、覆盖场景实用（非玩具技能）
- **局限**：技能数量还不多（社区早期阶段）、部分技能依赖 Composio 生态、非独立工具只是索引
- **是否值得长期保留**：✅ 关注——Codex Skill 生态的入口，模板和安装器模式可复用
