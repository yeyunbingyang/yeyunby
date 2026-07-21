---
title: Github优质项目 MOC
tags: [MOC, GitHub, 开源, 资源]
status: 稳定
created: 2026-05-26
updated: 2026-07-17
summary: "GitHub 优质开源项目汇总（284个），覆盖14个子域：Agent引擎(16)/Agent配置与Skills(26)/AI应用与学习(20)/AI开发框架(18)/ML引擎与模型(15)/视频创作与设计(15)/浏览器自动化与测试(7)/安全与隐私(19)/终端工具(27)/构建工具与质量(13)/数据与存储(33)/DevOps与云原生(32)/前端框架与UI(27)/后端与全栈(11)"
---

# Github优质项目 MOC

收集 GitHub 上高质量开源项目，总收录 **282 个**，覆盖 14 个子域。

> 📌 每个分类内部按 Star 数降序排列。2026-07-17 更新（格式标准化+文件名补充中文）：从 17 分类精简优化为 14 分类。

---

## 分类导航

| # | 分类 | 数量 | 最亮项目 |
|---|------|------|---------|
| 01 | [[Github优质项目-MOC#01-Agent引擎\|Agent引擎]] | 15 | OpenClaw(383k)/claw-code(195k)/hermes(216k) |
| 02 | [[Github优质项目-MOC#02-Agent配置与Skills\|Agent配置与Skills]] | 26 | Superpowers(207k)/ECC(193k)/MattPocock(170k) |
| 03 | [[Github优质项目-MOC#03-AI应用与学习\|AI应用与学习]] | 13 | awesome-llm-apps(120k)/ai-hedge-fund(61k)/streamlit(50k) |
| 04 | [[Github优质项目-MOC#04-AI开发框架\|AI开发框架]] | 18 | LangChain(170k)/Dify(100k)/AutoGen(60k) |
| 05 | [[Github优质项目-MOC#05-ML引擎与模型\|ML引擎与模型]] | 15 | Ollama(200k)/TensorFlow(190k)/PyTorch(100k) |
| 06 | [[Github优质项目-MOC#06-视频创作与设计\|视频创作与设计]] | 23 | MoneyPrinter(97k)/manim(88k)/penpot(56k) |
| 07 | [[Github优质项目-MOC#07-浏览器自动化与测试\|浏览器自动化与测试]] | 8 | Playwright(80k)/MediaCrawler(54k)/Cypress(50k) |
| 08 | [[Github优质项目-MOC#08-安全与隐私\|安全与隐私]] | 18 | hackingtool(69k)/Metasploit(40k)/SQLMap(40k) |
| 09 | [[Github优质项目-MOC#09-终端工具\|终端与效率工具]] | 37 | ohmyzsh(180k)/markitdown(165k)/Bun(94k) |
| 10 | [[Github优质项目-MOC#10-构建工具与质量\|代码质量与构建]] | 6 | Webpack(65k)/spec-kit(120k)/Prettier(50k) |
| 11 | [[Github优质项目-MOC#11-数据与存储\|数据与存储]] | 33 | Elasticsearch(75k)/Redis(70k)/Pandas(50k) |
| 12 | [[Github优质项目-MOC#12-DevOps与云原生\|DevOps与云原生]] | 32 | Kubernetes(120k)/Docker(100k)/Grafana(70k) |
| 13 | [[Github优质项目-MOC#13-前端框架与UI\|前端框架与UI]] | 27 | React(250k)/Vue(210k)/Bootstrap(175k) |
| 14 | [[Github优质项目-MOC#14-后端与全栈\|后端与全栈]] | 11 | Flutter(170k)/Django(90k)/FastAPI(90k) |

---

## 2026-07 优化说明

### 旧 17 分类 → 新 14 分类

| 变更 | 说明 |
|------|------|
| 02-配置与效率 + 03-Skills与工程规范 | **合并**为 02-Agent配置与Skills |
| 07-量化与交易 | **合并**入 03-AI应用与学习 |
| 11-数据工程与可视化 + 16-数据与中间件 | **合并**为 11-数据与存储 |
| 09-开发者工具 | **拆分**为 09-终端工具 + 10-构建工具与质量 |
| 13-AI工具与框架 + 17-AI模型与推理 | **拆分**为 04-AI开发框架 + 05-ML引擎与模型 |
| 14-前端与UI | **拆分**为 13-前端框架与UI + 10-构建工具与质量 |

---

## 本域笔记

```dataview
TABLE summary, status, created
FROM "03-Resources(资源层)/00 Github优质项目/01-Agent引擎" OR "03-Resources(资源层)/00 Github优质项目/02-Agent配置与Skills" OR "03-Resources(资源层)/00 Github优质项目/03-AI应用与学习" OR "03-Resources(资源层)/00 Github优质项目/04-AI开发框架" OR "03-Resources(资源层)/00 Github优质项目/05-ML引擎与模型" OR "03-Resources(资源层)/00 Github优质项目/06-视频创作与设计" OR "03-Resources(资源层)/00 Github优质项目/07-浏览器自动化与测试" OR "03-Resources(资源层)/00 Github优质项目/08-安全与隐私" OR "03-Resources(资源层)/00 Github优质项目/09-终端工具" OR "03-Resources(资源层)/00 Github优质项目/10-构建工具与质量" OR "03-Resources(资源层)/00 Github优质项目/11-数据与存储" OR "03-Resources(资源层)/00 Github优质项目/12-DevOps与云原生" OR "03-Resources(资源层)/00 Github优质项目/13-前端框架与UI" OR "03-Resources(资源层)/00 Github优质项目/14-后端与全栈"
WHERE file.name != "Github优质项目-MOC"
SORT created DESC
```


