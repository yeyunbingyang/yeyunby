---
title: 社交媒体舆情监控 Agent
description: 基于 Hermes Agent 构建的多平台社交媒体舆情监控系统，支持微博、知乎、小红书、Hacker News、Reddit 的实时监控、情感分析、预警推送、自动回复建议与日报生成
created: 2026-07-07
tags: [hermes-agent, social-media, sentiment-analysis, cron, gateway, monitoring]
author: Hermes Agent
domain: Core_Ability
status: 改进
updated: 2026-07-25
source: ""
related: []
summary: "社交媒体舆情监控Agent 通过 Hermes Agent 串联配置、工具和自动化流程，形成可复用的端到端实践案例"
review_after: 2027-07-25
---

# 社交媒体舆情监控 Agent

## 项目概述

本项目基于 **Hermes Agent** 构建一套全自动的社交媒体舆情监控系统，覆盖国内外主流社交平台，实现从数据采集、情感分析、异常预警到日报生成的全链路自动化。

### 核心能力

| 能力 | 说明 |
|------|------|
| **多平台监控** | 微博、知乎、小红书、Hacker News、Reddit |
| **情感分析** | 基于 LLM 的细粒度情感分类（正面/负面/中性/强烈负面） |
| **实时预警** | 负面舆情出现时通过微信/Telegram 即时推送 |
| **自动回复建议** | 根据舆情内容生成品牌回复话术 |
| **日报生成** | 每日自动汇总舆情趋势，生成结构化报告 |

### 技术栈

- **Agent 框架**: [Hermes Agent](https://hermes-agent.nousresearch.com)
- **数据采集**: `web_search` 工具 + 平台搜索 API
- **定时调度**: Hermes Cron 任务系统
- **消息推送**: Hermes Gateway（微信 / Telegram）
- **记忆系统**: Hermes Memory（跨会话舆情上下文）
- **工作流编排**: Hermes Kanban（多 Agent 协作）
- **会话检索**: `session_search`（历史舆情回溯）

---

## 快速开始

```bash
# 1. 克隆项目
git clone <repo-url> social-media-monitor
cd social-media-monitor

# 2. 配置 Hermes
hermes config set model.default "anthropic/claude-sonnet-4"
hermes config set terminal.timeout 120

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置关键词
cp configs/keywords.yaml.example configs/keywords.yaml
# 编辑 keywords.yaml 填入监控关键词

# 5. 创建 Cron 任务
hermes cron create "30m" --prompt "执行社交媒体舆情监控轮询" --delivery wechat

# 6. 启动 Gateway
hermes gateway start
```

---

## 项目结构

```
social-media-monitor/
├── README.md                    # 项目总览（本文档）
├── configs/
│   ├── keywords.yaml            # 监控关键词配置
│   ├── platforms.yaml           # 平台搜索参数
│   └── sentiment.yaml           # 情感分析阈值
├── docs/
│   ├── 01-架构设计.md           # 系统架构与设计
│   ├── 02-环境搭建.md           # 环境配置与安装
│   ├── 03-核心流程.md           # 监控流程详解
│   ├── 04-踩坑记录.md           # 常见问题与解决方案
│   └── 05-扩展思路.md           # 功能扩展方向
├── scripts/
│   ├── monitor.sh               # 单次监控执行脚本
│   ├── sentiment.py             # 情感分析辅助脚本
│   └── report.py                # 日报生成脚本
└── references/
    └── api-examples.md          # 各平台 API 参考
```

---

## 核心功能矩阵

| 功能 | 实现方式 | 调度频率 | 输出 |
|------|---------|---------|------|
| 微博监控 | `web_search` + 关键词 | 每 30 分钟 | 舆情条目 JSON |
| 知乎监控 | `web_search` + 关键词 | 每 30 分钟 | 舆情条目 JSON |
| 小红书监控 | `web_search` + 关键词 | 每 30 分钟 | 舆情条目 JSON |
| Hacker News | `web_search` + site 限定 | 每 1 小时 | 舆情条目 JSON |
| Reddit 监控 | `web_search` + site 限定 | 每 1 小时 | 舆情条目 JSON |
| 情感分析 | LLM 分析（Cron prompt 内） | 每次采集后 | 情感标签 + 分数 |
| 负面预警 | 情感阈值触发 | 实时 | 微信/Telegram 推送 |
| 日报生成 | 定时 Cron | 每日 09:00 | Markdown 报告 |
| 回复建议 | LLM 生成 | 负面预警时 | 回复话术 |

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                    Hermes Agent                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  Cron    │  │ web_     │  │ Memory   │  │ session_ │  │
│  │ 调度器   │  │ search   │  │ 记忆系统  │  │ search   │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │             │              │         │
│  ┌────▼──────────────▼─────────────▼──────────────▼─────┐  │
│  │               舆情分析引擎 (LLM)                       │  │
│  │   采集 → 清洗 → 情感分析 → 分类 → 预警判断              │  │
│  └────────────────────────┬──────────────────────────────┘  │
│                           │                                  │
│  ┌────────────────────────▼──────────────────────────────┐  │
│  │              Gateway 推送层                             │  │
│  │   微信 (WeChat)  │  Telegram  │  Email  │  Slack       │  │
│  └────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 依赖清单

- **Hermes Agent** ≥ v2.0（核心框架）
- **Python** ≥ 3.10（辅助脚本）
- **Hermes Gateway**（消息推送）
- **网络环境**（访问各社交媒体平台）

---

## 相关文档

| 文档 | 内容 |
|------|------|
| [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/04-工作流与实践/Hermes-Agent案例/05-社交媒体舆情监控Agent/docs/01-架构设计\|架构设计]] | 系统架构、数据流、模块划分 |
| [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/04-工作流与实践/Hermes-Agent案例/05-社交媒体舆情监控Agent/docs/02-环境搭建\|环境搭建]] | 安装配置、Hermes 设置、Gateway 配置 |
| [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/04-工作流与实践/Hermes-Agent案例/05-社交媒体舆情监控Agent/docs/03-核心流程\|核心流程]] | 监控流程、情感分析、预警、日报 |
| [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/04-工作流与实践/Hermes-Agent案例/05-社交媒体舆情监控Agent/docs/04-踩坑记录\|踩坑记录]] | 常见问题、解决方案、优化建议 |
| [[02-Knowledge(知识层)/20-核心能力-Core_Ability/10 技术能力-Technical_Capability/01-AI工具链与Agent实践/04-工作流与实践/Hermes-Agent案例/05-社交媒体舆情监控Agent/docs/05-扩展思路\|扩展思路]] | 更多平台、高级分析、多 Agent 协作 |
