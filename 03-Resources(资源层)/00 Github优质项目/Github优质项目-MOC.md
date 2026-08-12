---
title: Github优质项目 MOC
tags: [MOC, GitHub, 开源, 资源]
status: 稳定
created: 2026-05-26
updated: 2026-08-12
summary: "GitHub 优质开源项目汇总（298个），覆盖14个子域：Agent引擎(18)/Agent配置与Skills(31)/AI应用与学习(21)/AI开发框架(20)/ML引擎与模型(17)/视频创作与设计(15)/浏览器自动化与测试(7)/安全与隐私(22)/终端工具(29)/构建工具与质量(14)/数据与存储(34)/DevOps与云原生(32)/前端框架与UI(27)/后端与全栈(11)；2026-08 精选 10 个重点研究项目（覆盖 资料→知识蒸馏→Skill→Memory→CodeGraph→Agent执行 链路）"
---

# Github优质项目 MOC

收集 GitHub 上高质量开源项目，总收录 **298 个**，覆盖 14 个子域。

> 📌 每个分类内部按 Star 数降序排列。2026-07-17 更新（格式标准化+文件名补充中文）：从 17 分类精简优化为 14 分类。
> 📌 2026-08-12 更新：新增 6 个重点研究项目（book-to-skill / cangjie-skill / reverse-skill / code-graph-rag / loopx / cloudflare-computer），总收录 298 个；见下方「2026-08 重点研究」。

---

## 分类导航

| # | 分类 | 数量 | 最亮项目 |
|---|------|------|---------|
| 01 | [[Github优质项目-MOC#01-Agent引擎\|Agent引擎]] | 18 | OpenClaw(383k)/claw-code(195k)/hermes(216k) |
| 02 | [[Github优质项目-MOC#02-Agent配置与Skills\|Agent配置与Skills]] | 31 | Superpowers(207k)/ECC(193k)/MattPocock(170k) |
| 03 | [[Github优质项目-MOC#03-AI应用与学习\|AI应用与学习]] | 21 | awesome-llm-apps(120k)/ai-hedge-fund(61k)/streamlit(50k) |
| 04 | [[Github优质项目-MOC#04-AI开发框架\|AI开发框架]] | 20 | LangChain(170k)/Dify(100k)/AutoGen(60k) |
| 05 | [[Github优质项目-MOC#05-ML引擎与模型\|ML引擎与模型]] | 17 | Ollama(200k)/TensorFlow(190k)/PyTorch(100k) |
| 06 | [[Github优质项目-MOC#06-视频创作与设计\|视频创作与设计]] | 15 | MoneyPrinter(97k)/manim(88k)/penpot(56k) |
| 07 | [[Github优质项目-MOC#07-浏览器自动化与测试\|浏览器自动化与测试]] | 7 | Playwright(80k)/MediaCrawler(54k)/Cypress(50k) |
| 08 | [[Github优质项目-MOC#08-安全与隐私\|安全与隐私]] | 22 | hackingtool(69k)/Metasploit(40k)/SQLMap(40k) |
| 09 | [[Github优质项目-MOC#09-终端工具\|终端与效率工具]] | 29 | ohmyzsh(180k)/markitdown(165k)/Bun(94k) |
| 10 | [[Github优质项目-MOC#10-构建工具与质量\|代码质量与构建]] | 14 | Webpack(65k)/spec-kit(120k)/Prettier(50k) |
| 11 | [[Github优质项目-MOC#11-数据与存储\|数据与存储]] | 34 | Elasticsearch(75k)/Redis(70k)/Pandas(50k) |
| 12 | [[Github优质项目-MOC#12-DevOps与云原生\|DevOps与云原生]] | 32 | Kubernetes(120k)/Docker(100k)/Grafana(70k) |
| 13 | [[Github优质项目-MOC#13-前端框架与UI\|前端框架与UI]] | 27 | React(250k)/Vue(210k)/Bootstrap(175k) |
| 14 | [[Github优质项目-MOC#14-后端与全栈\|后端与全栈]] | 11 | Flutter(170k)/Django(90k)/FastAPI(90k) |

---

## 2026-08 重点研究（10 项目精选）

> 从 2026-08 GitHub Trending（周/月榜）精选 10 个与「知识库构建、Agent Skills、自动化/逆向、个人程序开发」高度重合的项目，作为下一步重点研究对象。

### 体系链路：原始资料 → Agent 能力

这 10 个项目不是零散工具，而是覆盖了一条完整链路：

```text
原始资料 ─→ 知识蒸馏 ─→ Skill ─→ Memory ─→ Code Graph ─→ Agent 执行
 (书/PDF)   (book-to-skill   (mattpocock/   (Agent-    (code-graph-   (loopx/orca/
 /视频)     cangjie-skill)    reverse-skill) Memory)    rag)          computer)
```

> [!note] 关键印证
> TencentDB-Agent-Memory 官方即把记忆资产定义为四种：**Chat Memory、Skill、LLM-Wiki、Code-Graph**——与上述链路高度同构，说明「内容 → 技能 → 记忆 → 图谱 → 执行」是当前 Agent 知识工程的主流共识。

### 优先级清单

| 优先级 | 项目 | 体系环节 | 为什么值得研究 |
|---|---|---|---|
| ⭐⭐⭐⭐⭐ | [[01-mattpocock-skills-工程师日常技能\|mattpocock/skills]] | Skill 编排 | 学习 Agent Skill 最直接 |
| ⭐⭐⭐⭐⭐ | [[30-book-to-skill-技术书籍转Claude技能\|book-to-skill]] | 知识蒸馏 | 非常适合「知识库 → Skill」 |
| ⭐⭐⭐⭐⭐ | [[31-cangjie-skill-内容蒸馏成可执行技能\|cangjie-skill]] | 知识蒸馏 | 视频/书籍/播客 → 可执行知识 |
| ⭐⭐⭐⭐⭐ | [[22-reverse-skill-逆向工程安全技能路由包\|reverse-skill]] | Skill 路由 | 逆向 + Agent + Skills |
| ⭐⭐⭐⭐⭐ | [[31-TencentDB-Agent-Memory-面向长任务多步Agent的分层记忆系统支持符号记忆\|TencentDB-Agent-Memory]] | Memory | Agent 长期知识库 |
| ⭐⭐⭐⭐⭐ | [[20-code-graph-rag-代码库知识图谱RAG\|code-graph-rag]] | Code Graph | 个人代码库知识图谱 |
| ⭐⭐⭐⭐ | [[17-loopx-长时Agent循环工程内核\|LoopX]] | Agent 执行 | 长时间 Agent 工作流 |
| ⭐⭐⭐⭐ | [[19-orca-多代理编排\|Orca]] | Agent 执行 | 多 Agent 并发调度 |
| ⭐⭐⭐⭐ | [[18-cloudflare-computer-给Agent一台电脑\|Cloudflare Computer]] | Agent 执行 | Computer-use Agent |
| ⭐⭐⭐⭐ | [[17-airllm-极低显存运行超大模型\|AirLLM]] | 推理基建 | 小显存运行大模型研究 |

**收藏状态：** 新增 6 个（book-to-skill / cangjie-skill / reverse-skill / code-graph-rag / loopx / cloudflare-computer），已有 4 个（mattpocock / Agent-Memory / orca / AirLLM）。

---

## 今日趋势整理（2026-07-28）

来源：[GitHub Trending · Daily](https://github.com/trending?since=daily)，数据于 2026-07-28 抓取。Star 数为抓取时快照。

| 排名 | 项目 | 分类 | 总 Star | 今日新增 | 收藏状态 |
|---|---|---|---:|---:|---|
| 1 | [[20-bitchat-蓝牙Mesh去中心化聊天\|bitchat]] | 安全与隐私 | 31,963 | 2,344 | 新增 |
| 2 | [[21-amnezia-client-自托管VPN客户端\|amnezia-client]] | 安全与隐私 | 13,697 | 515 | 新增 |
| 3 | [[13-airi-虚拟角色\|airi]] | AI应用与学习 | 43,903 | 554 | 已有 |
| 4 | [[29-superfile-现代终端文件管理器\|superfile]] | 终端工具 | 20,753 | 600 | 新增 |
| 5 | [[02-media-crawler-多平台爬虫\|MediaCrawler]] | 浏览器自动化与测试 | 58,092 | 349 | 已有 |
| 6 | [[08-impeccable-前端设计\|impeccable]] | 视频创作与设计 | 51,366 | 849 | 已有 |
| 7 | [[16-Kronos-金融K线基础模型\|Kronos]] | ML引擎与模型 | 34,478 | 442 | 新增 |
| 8 | [[14-open-code-review-阿里开源AI代码审查工具\|OpenCodeReview]] | 构建工具与质量 | 14,613 | 980 | 新增 |
| 9 | [[22-jenkins\|Jenkins]] | DevOps与云原生 | 25,851 | 179 | 已有 |
| 10 | [[14-claude-video-分析\|claude-video]] | 视频创作与设计 | 10,894 | 412 | 已有 |
| 11 | [[27-ag-kit-Antigravity-Agent工程套件\|AG Kit]] | Agent配置与Skills | 7,910 | 5 | 新增 |
| 12 | [[34-cassandra-高可扩展分布式数据库\|Apache Cassandra]] | 数据与存储 | 9,930 | 34 | 新增 |
| 13 | [[28-last30days-skill-多平台近期趋势调研技能\|last30days-skill]] | Agent配置与Skills | 54,058 | 221 | 新增 |
| 14 | [[05-imgui-即时GUI库\|Dear ImGui]] | 终端工具 | 75,164 | 64 | 已有 |

**整理结果：** 今日榜单 14 个项目，去重后新增收藏 8 个，已有 6 个。

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
