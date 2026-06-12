---
title: "UI-TARS Desktop 多模态GUI Agent"
tags: [GitHub, 开源, AI, Agent, 多模态, GUI, 字节跳动, VLM]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/bytedance/UI-TARS-desktop
zh-CN: https://github.com/bytedance/UI-TARS-desktop/blob/main/README.zh-CN.md
related: [[openhuman]]
summary: "字节跳动开源多模态AI Agent栈，Agent TARS（CLI+Web）做通用任务自动化，UI-TARS Desktop 做本地GUI操控，支持MCP工具集成，Apache-2.0，35.3k Stars"
---

# UI-TARS Desktop 多模态GUI Agent

https://github.com/bytedance/UI-TARS-desktop

## 基本信息

**类型：** 工具（桌面应用 + CLI）
**链接：** https://github.com/bytedance/UI-TARS-desktop
**主页：** https://agent-tars.com
**论文：** [arXiv 2501.12326](https://arxiv.org/abs/2501.12326)
**模型：** [UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B)（HuggingFace）
**适用领域：** GUI 自动化、计算机操控 Agent、浏览器自动化、多模态 Agent
**推荐程度：** ★★★★★
**Stars：** ~35.3k | Fork 3.5k
**语言：** TypeScript
**许可证：** Apache-2.0
**出品方：** 字节跳动（ByteDance）

## 是什么

TARS 是字节跳动开源的多模态 AI Agent 栈，包含两个项目：

| 项目                  | 形态           | 定位                                                         |
| ------------------- | ------------ | ---------------------------------------------------------- |
| **Agent TARS**      | CLI + Web UI | 通用多模态 Agent，将 GUI Agent + Vision 能力带入终端/浏览器/产品，支持 MCP 工具集成 |
| **UI-TARS Desktop** | 桌面应用         | 基于 UI-TARS 视觉语言模型的本地 GUI Agent，自然语言操控电脑和浏览器                |

核心能力：**让 AI 像人一样看屏幕、操作鼠标键盘、完成任务**——从「打开 VS Code 的自动保存设置」到「检查 GitHub 最新 Issue」都能通过自然语言指令完成。

## 快速开始

```bash
# Agent TARS CLI
npm install -g @agent-tars/cli
agent-tars

# UI-TARS Desktop
# 从 https://github.com/bytedance/UI-TARS-desktop/releases 下载安装包
```

## 核心功能

### Agent TARS（通用多模态 Agent）

- **CLI + Web UI** 双形态
- **GUI Agent**：截图识别 + 鼠标键盘精确操控
- **Vision**：视觉理解能力
- **MCP 工具集成**：对接真实世界工具
- **流式工具执行**：Shell 命令、多文件结构化展示
- **AIO Agent Sandbox**：隔离的一体化工具执行环境
- **Event Stream Viewer**：数据流追踪和调试

### UI-TARS Desktop（桌面 GUI Agent）

- 🤖 视觉语言模型驱动的自然语言操控
- 🖥️ 截图识别 + 精确鼠标键盘控制
- 💻 跨平台（Windows / macOS / Browser）
- 🌐 **本地操控**（Local Operator）+ **远程操控**（Remote Operator）
- 🔐 完全本地处理——隐私安全
- 🔄 实时反馈和状态显示

### 支持模式

| 模式 | 说明 |
|------|------|
| Local Computer Operator | 本机桌面操控 |
| Remote Computer Operator | 远程桌面操控 |
| Local Browser Operator | 本机浏览器操控 |
| Remote Browser Operator | 远程浏览器操控 |

## 技术亮点

- **纯视觉方案**：不依赖 DOM/无障碍 API，直接看屏幕截图理解界面——跨平台、跨应用通用
- **UI-TARS 模型**：字节跳动自研视觉语言模型，专为 GUI 操控优化
- **开源全套**：论文 + 模型（HuggingFace）+ 代码 + 桌面应用

## 适用场景

- 桌面自动化——用自然语言操控任意桌面应用
- 浏览器自动化——操控网页完成复杂任务（比传统 Selenium/Playwright 灵活）
- 远程运维——远程操控计算机完成 GUI 操作
- 研究 GUI Agent 的前沿实现方案
- 与 OpenHuman 互补：OpenHuman 做个人知识记忆，TARS 做 GUI 操作执行

## 评价

- **优点**：字节跳动出品、Apache-2.0 开源可商用、纯视觉方案跨平台跨应用通用、本地+远程双模式、论文+模型+代码全套开源、35.3k Stars 社区认可
- **局限**：需要 GPU 运行本地模型（UI-TARS-1.5-7B）、GUI Agent 准确性仍受 VLM 能力限制、安装配置有一定门槛
- **是否值得长期保留**：✅ 重点关注——开源 GUI Agent 赛道头部项目，视觉操控方案是 Agent 自主操作计算机的关键突破
