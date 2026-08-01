---
title: "koala73/worldmonitor 全球情报态势感知仪表盘"
domain: IT_Technology
tags: [GitHub, 开源, OSINT, AI应用]
status: 稳定
created: 2026-07-27
updated: 2026-07-27
verified: 2026-07-27
review_after: 2026-10-27
source: "https://github.com/koala73/worldmonitor"
related: ["[[Github优质项目-MOC]]"]
summary: "World Monitor 将新闻、地缘政治、金融、灾害与基础设施信号聚合到统一地图仪表盘，并通过 Web、桌面端、MCP、REST API、CLI 和多语言 SDK 提供访问能力。"
---

# koala73/worldmonitor 全球情报态势感知仪表盘

> [!abstract] 一句话定位
> 面向研究、OSINT 与态势感知的实时全球情报平台，以交互式地图统一呈现 AI 新闻简报、地缘政治风险、金融市场、灾害、航空和基础设施信号。

## 基本信息

| 项目 | 内容 |
|---|---|
| 仓库 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) |
| 在线体验 | [worldmonitor.app](https://www.worldmonitor.app) |
| 主要语言 | TypeScript |
| 许可证 | AGPL-3.0-only；闭源专有使用或官方品牌权利需另行授权 |
| 项目热度 | 约 75.1k Stars、11.2k Forks（2026-07-27） |
| 产品形态 | Web、PWA、Tauri 桌面端、MCP Server、REST API、CLI、SDK |

## 核心能力

- 聚合 500+ 精选新闻源，覆盖 15 个类别，并使用 AI 生成综合简报。
- 提供 3D 地球仪与 WebGL 平面地图两套引擎，共 56 种地图图层。
- 关联军事、经济、灾害、风险升级和基础设施等跨信息流信号。
- 提供 31 个重点国家的国家不稳定指数（CII v8）。
- 通过金融雷达追踪 29 家证券交易所、大宗商品、加密货币和综合市场信号。
- 支持通过 Ollama 在本地运行 AI 功能，降低对外部模型 API 的依赖。
- 同一代码库提供全球、科技、金融、大宗商品、正能量和能源 6 种站点变体。
- 支持 25 种语言及从右到左书写语言。

## 技术架构

| 层级 | 主要技术 |
|---|---|
| 前端 | Vanilla TypeScript、Vite |
| 地图与可视化 | globe.gl、Three.js、deck.gl、MapLibre GL |
| 桌面端 | Tauri 2（Rust）+ Node.js sidecar |
| AI/ML | Ollama、Groq、OpenRouter、Transformers.js |
| API 契约 | Protocol Buffers、sebuf HTTP 注解 |
| 部署 | Vercel Edge Functions、Railway、Tauri、PWA |
| 缓存 | Redis（Upstash）、三层缓存、CDN、Service Worker |

## 快速开始

```bash
git clone https://github.com/koala73/worldmonitor.git
cd worldmonitor
npm install
npm run dev
```

默认访问 `http://localhost:3000`。基础应用无需环境变量即可启动，但部分外部数据源需要在 `.env.local` 中配置凭据，完整字段见仓库的 `.env.example`。

常用开发命令：

```bash
npm run dev:tech
npm run dev:finance
npm run dev:commodity
npm run dev:happy
npm run dev:energy

npm run typecheck
npm run build:full
```

## 编程访问

- **MCP Server：** `https://worldmonitor.app/mcp`；工具列表公开，调用工具需要 API Key 或 OAuth。
- **REST API：** `https://api.worldmonitor.app`，提供 OpenAPI 规范。
- **CLI：** 可通过 `npx worldmonitor tools` 临时调用，也可全局安装 `worldmonitor`（别名 `wm`）。
- **SDK：** 提供 Python、Ruby 和 Go 官方客户端。
- **Agent 发现：** 提供 `llms.txt`、Agent Skills 清单和 API Catalog。

## 适用场景

- 搭建个人或团队的全球新闻与地缘政治态势看板。
- 研究多源情报聚合、地图可视化与事件关联的产品设计。
- 通过 MCP、API 或 SDK 为 Agent 增加实时风险与市场数据能力。
- 自托管面向金融、能源、科技或大宗商品的垂直监测平台。
- 学习 TypeScript、Tauri、边缘函数和多源数据缓存的完整工程实践。

## 评估

### 优势

- 数据源、地图图层和产品形态覆盖广，开箱即可在线体验。
- 同时兼顾人类可视化界面和 Agent/程序化访问。
- 支持本地 Ollama、桌面端和自托管，部署选择较丰富。
- 单仓库支持多个垂直变体，适合作为大型 TypeScript 应用架构案例。

### 注意事项

- 65+ 外部提供商与 API 会带来凭据、限流、可用性和数据许可管理成本。
- 情报聚合结果用于辅助研判，不应直接替代原始来源核验或专业决策。
- AGPL-3.0-only 对网络服务和修改版本的源代码开放有明确义务；闭源商业集成前应完成许可证评估。
- 仓库规模和功能面较大，二次开发前应先确定必要的数据源与站点变体，避免承担全部运维复杂度。

## 相关链接

- [中文 README](https://github.com/koala73/worldmonitor/blob/main/README.zh-CN.md)
- [中文文档](https://www.worldmonitor.app/docs/zh/documentation)
- [自托管指南](https://www.worldmonitor.app/docs/zh/getting-started)
- [架构文档](https://www.worldmonitor.app/docs/zh/architecture)
- [数据源目录](https://www.worldmonitor.app/docs/zh/data-sources)
- [发布版本](https://github.com/koala73/worldmonitor/releases/latest)
- [[Github优质项目-MOC]]
