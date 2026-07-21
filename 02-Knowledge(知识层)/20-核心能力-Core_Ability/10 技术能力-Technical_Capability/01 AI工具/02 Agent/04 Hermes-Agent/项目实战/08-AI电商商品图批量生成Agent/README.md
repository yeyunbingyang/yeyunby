---
title: AI 电商商品图批量生成 Agent
description: 基于 Hermes Agent 的电商商品图批量生成系统 — 从商品信息导入、自动去背、多风格模板生成到批量出图、自动上传店铺的全链路自动化方案
created: 2026-07-07
tags: [hermes-agent, ecommerce, comfyui, ai-image-generation, batch-processing, automation]
author: yeyunby
status: draft
---

# AI 电商商品图批量生成 Agent

## 项目概述

本方案基于 **Hermes Agent** 构建一个端到端的电商商品图批量生成系统。面向电商卖家与商品运营团队，解决多平台、多 SKU、多风格商品图的重复劳动问题。

### 核心流程

```
商品信息导入 → 自动去背 → 多风格模板生成 → 批量生成 → 自动上传店铺 → 数据追踪
```

### 解决的问题

| 痛点 | 方案 |
|------|------|
| 每款商品需多张不同风格图片 | 一套模板批量生成，一键切换风格 |
| 去背/抠图耗时 | ComfyUI + RMBG 模型自动去背 |
| 多店铺重复上传 | 自动上传至淘宝/拼多多/Shopify |
| 图片管理混乱 | 本地 + 云端双备份，按 SKU 索引 |
| 团队协作低效 | Hermes Kanban 看板 + Delegation 分发 |

### 技术栈

| 组件 | 技术选型 |
|------|----------|
| Agent 框架 | Hermes Agent |
| 图像生成 | ComfyUI（Stable Diffusion XL / Flux） |
| 去背/抠图 | ComfyUI RMBG-1.4 / BRIA RMBG |
| 调度编排 | Hermes Cron + Kanban |
| 商品数据 | CSV / Excel → Python 脚本解析 |
| 上传接口 | 淘宝开放平台 / 拼多多 API / Shopify REST |
| 存储 | 本地文件系统 + 对象存储（可选） |

### Hermes 核心能力应用

| 能力 | 用途 |
|------|------|
| **Cron** | 定时触发批量生成任务（夜间低谷运行） |
| **Terminal** | 执行 ComfyUI API 调用、Python 脚本、文件操作 |
| **Plugins** | 扩展商品平台 API 对接、自定义图像处理 |
| **Kanban** | 任务看板管理：待处理 → 生成中 → 审核 → 已上传 |
| **Delegation** | 子任务分发：去背、生成、上传各环节独立 Agent |
| **Memory** | 记录商品模板偏好、历史参数、失败重试策略 |

### 目录结构

```
08-AI电商商品图批量生成Agent/
├── README.md              # 项目总览（本文）
├── docs/
│   ├── 01-架构设计.md      # 系统架构与模块设计
│   ├── 02-环境搭建.md      # 环境配置与依赖安装
│   ├── 03-核心流程.md      # 批量生成完整流程
│   ├── 04-踩坑记录.md      # 常见问题与解决方案
│   └── 05-扩展思路.md      # 功能扩展与优化方向
├── configs/               # 配置文件
│   ├── comfyui/           # ComfyUI 工作流 JSON
│   ├── templates/         # 风格模板配置
│   └── platforms/         # 平台 API 配置
├── scripts/               # Python 脚本
│   ├── import_products.py # 商品数据导入
│   ├── batch_generate.py  # 批量生成调度
│   └── upload_assets.py   # 自动上传
└── references/            # 参考资料
    ├── api_docs/          # 平台 API 文档
    └── workflows/         # ComfyUI 工作流截图
```

---

## 快速开始

```bash
# 1. 克隆项目
cd /path/to/project

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 ComfyUI 工作流
# 将 configs/comfyui/ 下的 JSON 导入 ComfyUI

# 4. 准备商品数据
# 按 templates/product_template.csv 格式准备商品列表

# 5. 启动批量生成
python scripts/batch_generate.py --input products.csv --template white_bg
```

---

## 适用场景

- **电商卖家**：新品上架时批量生成白底图、场景图、模特图
- **商品运营团队**：大促活动前集中产出素材
- **跨境电商**：多平台（淘宝/拼多多/Shopify）统一管理商品图
- **代运营服务商**：批量处理多个店铺的商品图片需求

---

> **状态说明**：本文档为项目实战记录，持续更新中。欢迎提交 Issue 或 PR 完善内容。
