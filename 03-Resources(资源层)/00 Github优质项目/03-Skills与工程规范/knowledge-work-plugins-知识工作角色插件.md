---
title: "Knowledge Work Plugins 知识工作插件集"
tags: [GitHub, 开源, AI, Anthropic, Claude, Plugin, MCP]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/anthropics/knowledge-work-plugins
related: [[anthropics-skills-官方Skills仓库]]
summary: "Anthropic 官方知识工作插件集，11 个角色化插件将 Claude 变成岗位专家，纯 Markdown+JSON 无代码架构，16.3k Stars"
---

# Knowledge Work Plugins 知识工作插件集

https://github.com/anthropics/knowledge-work-plugins

## 基本信息

**类型：** 工具（Plugin 集合）
**链接：** https://github.com/anthropics/knowledge-work-plugins
**适用领域：** 知识工作自动化、团队协作、Claude Cowork / Claude Code 扩展
**推荐程度：** ★★★★★
**Stars：** ~16.3k | Fork 1.9k
**许可证：** Apache-2.0
**作者：** Anthropic 官方

## 是什么

Anthropic 官方开源的 11 个知识工作插件，面向 Claude Cowork 和 Claude Code。每个插件将 Claude 变成特定岗位专家——告诉它你的工具、术语、流程，Claude 就像为团队定制的一样工作。

每个插件 = Skills（领域知识，自动激活）+ Commands（斜杠命令，显式触发）+ Connectors（MCP 对接外部工具）。**纯 Markdown + JSON，零代码。**

## 快速开始

```bash
# Claude Code
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins

# Claude Cowork
# 从 claude.com/plugins 直接安装
```

安装后插件自动激活——Skills 在相关场景自动生效，命令如 `/sales:call-prep`、`/data:write-query` 可直接调用。

## 核心功能

### 11 个角色插件

| 插件                           | 场景           | 对接工具                                              |
| ---------------------------- | ------------ | ------------------------------------------------- |
| **productivity**             | 任务/日历/日常工作流  | Slack, Notion, Asana, Linear, Jira, Microsoft 365 |
| **sales**                    | 客户调研/通话准备/漏斗 | Slack, HubSpot, Close, Clay, ZoomInfo             |
| **customer-support**         | 工单分类/回复/知识库  | Slack, Intercom, HubSpot, Guru, Jira              |
| **product-management**       | 规格书/路线图/用户研究 | Slack, Linear, Figma, Amplitude, Pendo            |
| **marketing**                | 内容/活动/品牌语调   | Slack, Canva, Figma, HubSpot, Ahrefs              |
| **legal**                    | 合同审查/NDA/合规  | Slack, Box, Egnyte, Jira, Microsoft 365           |
| **finance**                  | 日记账/对账/财报/审计 | Snowflake, Databricks, BigQuery, Slack            |
| **data**                     | SQL/统计分析/仪表盘 | Snowflake, Databricks, BigQuery, Hex              |
| **enterprise-search**        | 跨工具统一搜索      | Slack, Notion, Guru, Jira, Asana, Microsoft 365   |
| **bio-research**             | 临床前研究/基因组学   | PubMed, bioRxiv, ChEMBL, Open Targets             |
| **cowork-plugin-management** | 创建/定制新插件     | —                                                 |

### 插件架构（三段式）

```
plugin-name/
├── .claude-plugin/plugin.json   # 清单
├── .mcp.json                    # MCP 工具连接
├── commands/                    # 用户显式触发的命令
└── skills/                      # 自动激活的领域知识
```

### 定制化

官方插件是起点，真正威力在于定制：换连接器（`.mcp.json`）→ 加公司术语和流程到 skill → 调工作流 → 建新插件（用 `cowork-plugin-management`）。

## 适用场景

- 团队用 Claude 标准化岗位工作流（销售/客服/PM/法务/财务等）
- 参考官方结构设计自有团队插件——纯 Markdown 定义 Agent 行为
- 企业跨工具语义搜索（Slack/Notion/Jira 等统一检索）
- 与本知识库的 Obsidian 架构理念一致——文件即配置，零代码

## 评价

- **优点**：Anthropic 官方出品、纯 Markdown+JSON 零门槛、11 角色覆盖广、MCP 连接器生态完善、Apache-2.0 商用友好
- **局限**：依赖 Claude Cowork/Code 生态、中文场景需自行定制
- **是否值得长期保留**：✅ 必读参考——「Markdown 定义 Agent」范式是知识库→Agent 自动化的关键路径
