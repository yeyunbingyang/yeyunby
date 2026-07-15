---
title: 知识库总导航
domain: ""
tags: [MOC, 导航]
status: 稳定
created: 2026-05-07
updated: 2026-07-07
summary: "知识库顶级导航入口，覆盖4层目录结构、三大知识域(354篇)、AI工具链、系统仪表盘、资源库"
---

# 知识库总导航

打开知识库先看这里，再进入对应目录或领域 MOC。

## 目录结构

```
├── MOC知识地图.md              # ← 你在这里
├── 00-System(支撑层)/          # 元规则、模板、工作流、仪表盘
│   ├── Rules/                  # 命名规范、标签系统、清空规则
│   ├── Templates/              # 6 种笔记模板
│   ├── Runtime_Data/           # 项目/技能仪表盘、笔记统计
│   └── SCHEMA.md               # Frontmatter 规范
├── 01-日常流(日常流层)/       # 日记、周复盘、阶段规划、流入（新内容第一落点）
│   ├── README.md
│   ├── 流入/                   # 新内容入口，目标每日清空
│   ├── 日记/                   # 每日笔记 YYYY-MM-DD
│   ├── 周复盘/                 # 每周回顾 YYYY-Wxx
│   └── 阶段规划/               # 学习/项目阶段计划
├── 02-Knowledge(知识层)/       # 核心知识 —— 按两大域组织
│   ├── 10-IT技术-IT_Technology/  # 技术工程（开发/运维/网络）
│   └── 20-核心能力-Core_Ability/ # 能力与认知（AI应用/思维/人文）
└── 03-Resources(资源层)/       # 外部资源收集
    ├── [[Github优质项目-MOC|00 Github优质项目]]/  # 31个项目，8个子分类
    ├── 01-软件工具/            # 开发/效率/系统工具
    ├── 02-课程索引/            # 课程与学习路径
    ├── 03-网站导航/            # 常用网站与文档站
    ├── 04-素材库/              # 图片、图表、素材
    └── 05-AI工具/              # AI 工具与平台
        ├── Claude-Skills/      # Claude Code Skills 使用手册
        └── Hermes-Agent/       # Hermes Agent 使用手册
```

## 核心入口

| 入口 | 说明 |
|------|------|
| [[Project_Dashboard\|项目仪表盘]] | 待办管理，任务 ↔ 笔记联动 |
| [[01-日常流(日常流层)/流入/README\|流入/ 收集箱]] | 新内容第一落点，每日整理 |
| [[IT技术-MOC\|IT 技术]] | 8 大子域：通用工具·AI工程·后端·前端·运维·自动化·嵌入·逆向 |
| [[Cognition-MOC\|认知层]] | 思维模型 · 认知科学 · 学习方法 · 人文社科 |
| [[Core_Ability-MOC\|核心能力]] | 职业 · 表达 · 商业 · 创作 · 生活 · 计算机 |
| [[03-Resources(资源层)/README\|资源库]] | 工具、课程、网站、素材、AI 平台 |

> 归档通过笔记 frontmatter 的 `status: 归档` 标记，无需独立目录。

## 三大知识域

### 10 IT 技术 — [[IT技术-MOC]]（工程开发）

| 子域 | MOC | 笔数 | 关键内容 |
|------|-----|------|----------|
| 00 通用技术工具 | [[通用技术工具-MOC]] | 7 | Git/数据库/IDE技巧 |
| 01 AI工程 | [[AI工程-MOC]] | 17 | Coze/Dify/RAG/大模型部署 |
| 02 后端开发 | [[后端开发-MOC]] | 78 | Python全体系/Java/JS/中间件 |
| 03 前端开发 | [[前端开发-MOC]] | 93 | HTML/CSS/JS/Vue/工程化 |
| 04 运维与交付 | [[运维云原生-MOC]] | 84 | Linux/Docker/K8s/Jenkins |
| 05 自动化与平台 | [[自动化-MOC]] | 3 | 低代码/RPA/Python脚本 |
| 06 嵌入式与物联网 | — | — | 骨架（含网络与安全概览） |
| 07 逆向 | — | — | 骨架 |

### 20 核心能力 — [[Core_Ability-MOC]]（能力与认知）

| 大类 | 子域 | 笔数 | 关键内容 |
|------|------|------|----------|
| **10 AI应用** | [[模型及代理-MOC]] | 104 | AI概念/Agent/Hermes/AIGC |
| **20 职场技能** | [[职业能力-MOC]] / [[表达沟通-MOC]] | 4 | 职业/面试/沟通 |
| **30 商业创作** | [[商业财经-MOC]] / [[内容创作-MOC]] | 2 | 待建设 |
| **40 生活工具** | [[生活基础设施-MOC]] / [[计算机应用-MOC]] | 7 | 生活/Windows/硬件 |
| **50 认知思维** | [[思维模型-MOC]] / [[认知心理学-MOC]] / [[学习方法-MOC]] | 5 | 思维/心理/学习 |
| **60 人文社科** | [[人文社科-MOC]] | 1 | 待建设 |

## 运行数据

- [[Project_Dashboard\|项目仪表盘]]：待办 → 笔记联动，Dataview 自动聚合任务
- [[Skill_Dashboard\|技能仪表盘]]：三大域技能成长追踪
- [[Note_Statistics\|笔记统计]]：按域和状态统计知识资产

## 系统规则

- [[Naming_Standards\|命名规范]] — 文件/文件夹命名约定
- [[Tag_System\|标签系统]] — 内容类型、状态辅助、跨域主题标签
- [[Clearance_Rules\|清空规则]] — 流入清空频率与归档触发条件
- [[SCHEMA\|Frontmatter 规范]] — 笔记元数据标准

## 模板

- [[知识笔记-模板]]
- [[读书笔记-模板]]
- [[项目笔记-模板]]
- [[资源条目-模板]]
- [[01-日常流(日常流层)/02 日记/日记-模板]]
- [[周复盘-模板]]
- [[MOC模板]]

## GitHub 优质项目

已收录 **139 个**高质量 GitHub 开源项目，详见 [[Github优质项目-MOC]]，12 大分类：

| 分类 | 数量 | 亮点项目 |
|------|------|----------|
| [[Github优质项目-MOC#01 Agent引擎\|01 Agent引擎]] | 14 | OpenClaw(374k)/claw-code(192k)/ruflo(57k) |
| [[Github优质项目-MOC#02 Agent配置与效率\|02 配置效率]] | 8 | Superpowers(207k)/ECC(193k)/CC-Switch(81k) |
| [[Github优质项目-MOC#03 Skills与工程规范\|03 Skills规范]] | 16 | Matt Pocock(170k)/Karpathy指南(156k)/Anthropic Skills(141k) |
| [[Github优质项目-MOC#04 AI应用与知识管理\|04 AI应用与知识]] | 7 | awesome-llm-apps(120k)/learn-claude-code(45k) |
| [[Github优质项目-MOC#05 视频制作与媒体\|05 视频制作媒体]] | 23 | MoneyPrinter(94k)/manim(88k)/penpot(56k) |
| [[Github优质项目-MOC#06 浏览器自动化\|06 浏览器自动化]] | 6 | MediaCrawler(54k)/agent-browser(37k) |
| [[Github优质项目-MOC#07 量化与交易\|07 量化交易]] | 3 | AI Hedge Fund(61k)/每日股票分析(52k) |
| [[Github优质项目-MOC#08 安全隐私与系统工具\|08 安全工具]] | 11 | hackingtool(69k)/Win11Debloat(51k)/pentagi(20k) |
| [[Github优质项目-MOC#09 开发者工具\|09 开发者工具]] | 15 | Bun(94k)/imgui(74k)/exo(39k)/pi-mono(18k) |
| [[Github优质项目-MOC#10 参考与收集\|10 参考收集]] | 14 | free-programming-books(392k)/system-prompts(138k) |
| [[Github优质项目-MOC#11 数据工程与可视化\|11 数据工程可视化]] | 16 | spec-kit(120k)/graphify(86k)/claude-mem(70k) |
| [[Github优质项目-MOC#12 DevOps与云原生\|12 DevOps云原生]] | 6 | apple-container(45k)/posthog(35k)/prefect(23k) |

## 使用流程

1. 新内容先放入 [[01-日常流(日常流层)/流入/README\|流入/]]
2. 每天整理流入，判断去向（Knowledge / Resources）
3. 待办任务在 [[Project_Dashboard\|项目仪表盘]] 中管理，格式：`- [ ] 任务 → [[笔记名]]`
4. 知识笔记内用 `- [ ] 下一步：...` 标记行动项，自动聚合到仪表盘
5. 每周完成流入清空，更新 [[Skill_Dashboard\|技能仪表盘]]
6. 过时笔记修改 `status: 归档`，保留在原位置
