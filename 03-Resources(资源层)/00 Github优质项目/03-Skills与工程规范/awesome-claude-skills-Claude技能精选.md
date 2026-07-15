---
title: "Awesome Claude Skills 精选技能列表"
tags: [GitHub, 开源, AI, Claude, Skills, awesome-list, Composio]
type: 资源索引
status: 待评估
created: 2026-07-06
updated: 2026-07-16
source: https://github.com/ComposioHQ/awesome-claude-skills
related: [[awesome-codex-skills-Codex技能精选], [anthropics-skills-官方Skills仓库]]
summary: "Composio 维护的 1000+ Claude Skills 精选列表——覆盖文档处理/开发/数据分析/商业/写作/创意/生产力/安全等全场景，含 78 个 SaaS 自动化技能，66.9k Stars"
---

# Awesome Claude Skills 精选技能列表

https://github.com/ComposioHQ/awesome-claude-skills

## 基本信息

**类型：** 资源索引（Awesome List）
**链接：** https://github.com/ComposioHQ/awesome-claude-skills
**适用领域：** Claude Skills 发现与索引、工作流自动化
**推荐程度：** ★★★★★
**Stars：** ~66.9k | Fork 7.5k
**维护方：** ComposioHQ

## 是什么

**Composio 维护的 Claude Skills 精选列表**（Awesome List 格式）。收录 1000+ 生产级 Claude Skills 和插件，覆盖 Claude.ai、Claude Code、Codex、Cursor、Gemini CLI、Antigravity 等平台。是目前最全面的 Claude Skills 索引。

## 技能分类

### 文档处理
- **docx** — Word 文档创建/编辑/分析（Anthropic 官方）
- **pdf** — PDF 文本/表格提取/合并/标注（Anthropic 官方）
- **pptx** — 幻灯片读写/生成（Anthropic 官方）
- **xlsx** — 电子表格操作（Anthropic 官方）
- Markdown to EPUB — 文档转电子书
- Master Claude for Legal — 法律团队技能包

### 开发与代码工具
- **artifacts-builder** — HTML 构件创建（React/Tailwind/shadcn）
- **aws-skills** — AWS CDK/无服务器开发
- **Chrome Relay** — 驱动已登录 Chrome 会话
- **D3.js Visualization** — D3 图表可视化
- **FFUF Web Fuzzing** — Web 模糊测试
- **MCP Builder** — MCP 服务器创建指南
- **OpenWeb** — 90+ 网站的 Agent 原生访问
- **Playwright** — 浏览器自动化测试
- **Septim Agents** — 10 个命名子代理
- **Skill Creator** — Skill 创建指南
- **Webapp Testing** — Playwright Web 测试
- 以及 overkill、lean-ctx、prompt-engineering 等

### 数据与分析
- CSV Data Summarizer、deep-research、postgres（只读 SQL）、recursive-research、root-cause-tracing

### 商业与营销
- Brand Build Skills（59 技能）、Brand Guidelines、Competitive Ads Extractor、Domain Name Brainstormer、Internal Comms、Lead Research Assistant

### 沟通与写作
- article-extractor、brainstorming、Content Research Writer、Meeting Insights Analyzer、NotebookLM Integration、Twitter Algorithm Optimizer

### 创意与媒体
- anydesign（Figma/URL → design.md）、Canvas Design、imagen（Gemini 图像生成）、Image Enhancer、Slack GIF Creator、Theme Factory、Video Downloader、youtube-transcript、swiftui-design-skill

### 生产力与组织
- File Organizer、Invoice Organizer、kaizen、n8n-skills、Raffle Winner Picker、solo-skills（7 个双语技能）、Tailored Resume Generator、tapestry

### 协作与项目管理
- git-pushing、google-workspace-skills、mercury-mcp、outline、review-implementing、test-fixing

### 安全与系统
- computer-forensics、file-deletion、metadata-extraction、threat-hunting-with-sigma-rules

### SaaS 自动化（78 个应用）

通过 Composio 的预构建工作流技能，覆盖：
- **CRM**：Close / HubSpot / Pipedrive / Salesforce / Zoho CRM
- **项目管理**：Asana / Basecamp / ClickUp / Jira / Linear / Monday / Notion / Todoist / Trello / Wrike
- **通讯**：Discord / Intercom / Microsoft Teams / Slack / Telegram / WhatsApp
- **邮件**：Gmail / Outlook / Postmark / SendGrid
- **DevOps**：Bitbucket / CircleCI / Datadog / GitHub / GitLab / PagerDuty / Render / Sentry / Supabase / Vercel
- **存储**：Box / Dropbox / Google Drive / OneDrive
- **表格与数据库**：Airtable / Coda / Google Sheets
- **日历**：Cal.com / Calendly / Google Calendar / Outlook Calendar
- **社交媒体**：Instagram / LinkedIn / Reddit / TikTok / Twitter / YouTube
- **营销**：ActiveCampaign / Brevo / ConvertKit / Klaviyo

## 安装

```bash
# 连接 500+ 应用
claude --plugin-dir ./connect-apps-plugin
/connect-apps:setup
```

## 评价

- **优点**：1000+ 技能最全索引、分类清晰、78 个 SaaS 自动化技能实用、66.9k Stars 社区活跃
- **局限**：只是索引非独立工具、部分技能依赖 Composio 生态、质量参差不齐
- **是否值得长期保留**：✅ 重点关注——Claude Skills 生态的入口和索引
