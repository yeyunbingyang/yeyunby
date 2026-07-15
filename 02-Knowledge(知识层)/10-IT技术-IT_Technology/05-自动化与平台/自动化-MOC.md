---
title: 自动化工具链 MOC
domain: IT_Technology
tags: [MOC, 自动化, RPA, 桌面自动化, Web自动化, 文件处理]
status: 稳定
created: 2026-05-07
updated: 2026-06-12
summary: "面向桌面端的自动化工具链，覆盖桌面RPA、文件批处理、应用自动化与Web自动化，聚焦单机/终端侧的实际工作流替代手工操作"
---

# 自动化工具链

消除日常生活中重复的手工操作——让文件处理、桌面操作、网页操作和应用交互变得可重复、可审计、可扩展。核心原则：**凡是做了两次的事，第三次必须自动化**。

## 学习路径

`Bat / PowerShell 脚本基础` → `Python 本地自动化` → `桌面 RPA（影刀 / UiPath）` → `Web 自动化（Selenium / Playwright）` → `跨工具综合编排`

## 核心概念

| 概念       | 一句话定义                                                |
| -------- | ---------------------------------------------------- |
| 幂等性      | 脚本运行多次结果相同，不产生副作用                                    |
| 选择器定位    | 通过 XPath / CSS / 图像识别定位 UI 元素，是 RPA 和 Web 自动化的根基     |
| 异常兜底     | 自动化流程中预留 try-catch 和人工接管节点，避免无人值守时静默失败               |
| Headless | 浏览器不显示界面的运行模式，适合服务器端无人值守跑 Web 自动化                    |
| 录制回放     | RPA 工具通过录屏操作自动生成脚本，降低入门门槛                            |
| COM 对象   | Windows 组件对象模型，PowerShell 通过 COM 可操控 Office、IE 等桌面应用 |

## 关键知识点

### 脚本基础（Bat / PowerShell）
- [[01-Bat脚本详解]] — Windows 批处理，双击即执行，适合快速文件批量处理、系统配置
- PowerShell 脚本基础 — 对象管道、COM 互操作、比 Bat 更强的字符串与结构化数据处理
- 错误处理（try-catch / $LASTEXITCODE vs %ERRORLEVEL%）
- 定时触发（schtasks 注册计划任务 → 无人值守执行的入口）
- 脚本健壮性（参数校验 / 日志 / 幂等设计）

### 文件处理自动化
- 批量重命名 / 格式转换 / 编码转换
- 文件监听与自动分类（Python watchdog / PowerShell FileSystemWatcher）
- 日志轮转与归档清理
- 大文件分片与合并
- 结构化文件处理（CSV/JSON/XML 的读写与转换）

### 桌面 RPA【结合AI决策、操作使用RPA】
- 影刀 — 国产 RPA，低代码 + 中文生态友好，适合个人和小团队快速落地
- UiPath — 企业级 RPA 标杆，Studio + Orchestrator + Robot 三层架构
- Power Automate — 微软生态内免费/低成本桌面 RPA，与 Office 365 深度集成
- 元素定位策略（选择器 vs 图像识别 vs 坐标点击，优先级与回退链）
- 异常处理与人工接管节点设计
- 凭据管理与安全沙箱

### 应用自动化（Windows 桌面应用）
- PowerShell COM 对象操控 Office（Excel/Word/Outlook）
- 剪贴板操作与模拟按键（SendKeys / AutoHotkey 思路）
- 窗口句柄操作（FindWindow / SetForegroundWindow → 跨应用编排的底层能力）
- 注册表读写自动化配置

### Web 自动化
- Selenium — 老牌浏览器自动化框架，生态最全、语言支持广
- Playwright — 微软出品，自动等待、网络拦截、多浏览器原生支持，开发体验优于 Selenium
- Puppeteer — Google 维护，专注 Chrome/Chromium，轻量无头场景首选
- 反检测策略（stealth 插件 / 指纹伪装 / 人机行为模拟）
- 数据抓取与表单自动填写
- 截图对比与视觉回归测试（Playwright 内置能力）

### 跨工具综合编排
- Python 作为胶水语言串联 Bat → RPA → Web 自动化
- 通过 CLI 调用 RPA 工程（影刀 / UiPath 的命令行触发）
- 统一日志与告警（Python logging → 文件 / 钉钉 / 微信通知）
- 自动化巡检脚本：定时触发 → 多工具协作 → 结果汇总 → 异常告警

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/05-自动化与平台"
WHERE file.name != "自动化-MOC"
SORT updated DESC
```
