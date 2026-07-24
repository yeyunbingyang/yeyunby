---
title: CC Switch 模型管理器
domain: Core_Ability
tags: [AI, 模型管理, Agent, 工具]
status: 稳定
created: 2026-06-16
updated: 2026-07-25
verified: 2026-07-25
review_after: 2026-08-25
source: "https://github.com/farion1231/cc-switch"
related: ["Claude-Code操作手册", "模型路由策略", "主流模型对比"]
summary: "CC Switch 通过图形界面统一管理多个 Agent CLI 的供应商、MCP、Prompts、Skills 与会话配置，而不是拦截或代理模型请求"
---

# CC Switch 模型管理器

> CC Switch 是 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw、Hermes Agent 等工具的桌面配置管理器。

## 一句话结论

CC Switch 的核心价值是**集中维护并切换各个 Agent 工具的配置文件**。它会把选定的供应商、MCP、Prompt 或 Skill 同步到对应工具的实际配置位置，但不充当 API 代理，也不会劫持或转发模型流量。

## 工作方式

```text
CC Switch 图形界面
   ├─ 供应商配置与启用状态
   ├─ MCP 服务器
   ├─ Prompts
   ├─ Skills
   └─ Sessions
          │
          ▼
同步到各工具的真实配置文件
   ├─ Claude Code
   ├─ Codex
   ├─ Gemini CLI
   ├─ OpenCode / OpenClaw
   └─ Hermes Agent
```

切换供应商后，大多数 CLI 需要重新启动才能读取新配置；官方说明指出 Claude Code 通常可以直接生效。

## 安装

### Windows

从官方 [Releases](https://github.com/farion1231/cc-switch/releases) 下载：

- `CC-Switch-v{version}-Windows.msi`
- `CC-Switch-v{version}-Windows-Portable.zip`

系统要求为 Windows 10 及以上。

### macOS

```bash
brew install --cask cc-switch
```

升级：

```bash
brew upgrade --cask cc-switch
```

也可以从 Releases 下载签名并公证过的 DMG。

### Linux

官方发布提供 `.deb`、`.rpm` 和 `.AppImage`；Arch Linux 可使用：

```bash
paru -S cc-switch-bin
```

## 基本使用

1. 打开 **Add Provider**，选择预设供应商或创建自定义配置。
2. 在主界面选择供应商并点击 **Enable**，或从系统托盘直接切换。
3. 重启对应 CLI 以重新载入配置；Claude Code 通常无需重启。
4. 如需恢复官方 OAuth 登录，启用 **Official Login** 预设，再按工具原生流程登录。

首次启动时，可以导入本机已经存在的 CLI 配置作为默认供应商，避免重复录入。

## MCP、Prompts、Skills 与 Sessions

### MCP

通过模板或自定义配置添加 MCP Server，并按应用选择是否同步。修改后应在目标 CLI 内确认服务器是否成功加载。

### Prompts

CC Switch 提供 Markdown 编辑器和预设切换，启用后同步到目标工具的实际 Prompt 文件。

### Skills

可以浏览 GitHub 仓库并向受支持的 Agent 工具安装 Skill。安装后仍需检查 Skill 的权限、依赖和适用范围。

### Sessions

会话页用于浏览、搜索和恢复受支持工具的历史会话。它是本地会话入口，不等同于跨厂商云同步。

## 与路由器的区别

| 维度 | CC Switch | 9Router / OmniRoute |
|------|-----------|---------------------|
| 定位 | 配置管理器 | API 网关或路由器 |
| 是否代理请求 | 否 | 是 |
| 切换方式 | 写入并启用配置 | 请求时动态选路 |
| Token 压缩 | 不负责 | 视具体网关能力而定 |
| 自动回退 | 不负责 | 支持多级回退 |
| MCP / Skills 管理 | 支持 | 视项目能力而定 |

CC Switch 可以负责把 CLI 指向 9Router 或 OmniRoute；真正的请求路由、限流、熔断和压缩仍由网关完成。

## 使用边界

- 第三方 API 中转服务的真实性、隐私和稳定性需要单独评估，CC Switch 只管理配置。
- 启用新供应商前，应备份目标 CLI 的配置并确认 API Base URL、模型 ID 与认证方式。
- 不要把 API Key 写入知识笔记或提交到 Git。
- 功能和支持工具会随版本变化，以官方 README 和 Releases 为准。

## 关联

- [[04-模型路由策略]] — 配置管理与动态路由如何组合
- [[00-主流模型对比]] — 模型能力与价格速查
- [[01-9router-快速入门手册]] — 轻量路由方案
- [[03-omniRoute-使用指南]] — 完整网关方案
