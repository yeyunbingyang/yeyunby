---
title: Chrome DevTools MCP安装与操作指南
domain: Core_Ability
tags: [MCP, Chrome, 浏览器自动化, Codex]
status: 稳定
created: 2026-07-30
updated: 2026-07-30
verified: 2026-07-30
review_after: 2026-10-30
source: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
related: ["Agent扩展-MOC", "MCP-概念与架构", "opencli-browser"]
summary: "在 Windows Codex 中通过 npx 配置 Chrome DevTools MCP，可让 Agent 执行页面自动化、控制台与网络调试、截图及性能分析"
---

# Chrome DevTools MCP 安装与操作指南

> [!success] 本机状态
> 已在 Windows 11 + Codex CLI 0.145.0 + Node.js 22.19.0 环境完成配置，并以 `chrome-devtools-mcp 1.6.0` 验证启动成功。修改 MCP 配置后需要重启 Codex，当前会话不会自动加载新工具。

## 一、它能解决什么问题

[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) 是 Chrome DevTools 团队维护的 MCP Server。它让 Codex 等 Agent 通过 Chrome DevTools Protocol 和 Puppeteer 控制、检查浏览器，主要能力包括：

- 页面导航、点击、输入、拖拽、上传文件；
- 获取页面结构快照与截图；
- 查看控制台消息、执行 JavaScript；
- 查看网络请求及单个请求详情；
- 录制性能 trace 并分析性能问题；
- 执行 Lighthouse 审计与内存调试。

它适合网页调试、端到端操作、性能排查和需要真实浏览器渲染的页面检查。仅需读取普通网页正文时，不必启用浏览器自动化。

## 二、前置条件

```powershell
node --version
npm --version
codex --version
```

官方要求：

- Node.js LTS；
- npm；
- 当前稳定版或更新版本的 Google Chrome；
- 支持 MCP 的客户端，本指南使用 Codex。

## 三、Windows Codex 安装配置

### 3.1 推荐安装命令

```powershell
codex mcp add chrome-devtools `
  --env SystemRoot=C:\Windows `
  --env "PROGRAMFILES=C:\Program Files" `
  -- cmd /c npx -y chrome-devtools-mcp@latest
```

这会把配置写入用户级 `%USERPROFILE%\.codex\config.toml`。`npx` 会在首次启动时下载并缓存包，无需执行全局 `npm install -g`。

### 3.2 Windows 完整配置

确认配置包含以下内容：

```toml
[mcp_servers.chrome-devtools]
command = "cmd"
args = ["/c", "npx", "-y", "chrome-devtools-mcp@latest"]
startup_timeout_ms = 20_000

[mcp_servers.chrome-devtools.env]
PROGRAMFILES = 'C:\Program Files'
SystemRoot = 'C:\Windows'
```

其中 `cmd /c`、Chrome 安装路径环境变量和更长的启动超时是官方针对 Windows 11 给出的兼容配置。

> [!note] 固定版本
> `@latest` 会自动使用最新版，维护成本低，但升级可能改变行为。要求可复现时，把它改为已验证版本，例如 `chrome-devtools-mcp@1.6.0`。

### 3.3 验证包能否启动

```powershell
cmd /c npx -y chrome-devtools-mcp@latest --version
```

预期输出版本号。完成配置后重启 Codex，再在新任务中检查 MCP 工具或直接执行下一节的测试提示词。

## 四、第一次使用

在 Codex 中输入：

```text
使用 chrome-devtools 检查 https://developers.chrome.com 的性能，
输出主要性能问题、证据和改进建议。
```

MCP Server 只有在首次调用需要浏览器的工具时才会启动 Chrome；仅连接 MCP Server 不会立即打开浏览器。

## 五、常用操作提示词

### 5.1 页面结构与交互

```text
打开 https://example.com，获取页面快照，列出主要可交互元素。
```

```text
打开目标页面，填写搜索框并提交；等待结果加载后，汇总前三条结果。
```

### 5.2 控制台错误

```text
打开本地页面 http://localhost:3000，刷新页面，列出控制台 error 和 warning，
定位最可能的根因，但先不要修改代码。
```

### 5.3 网络请求

```text
打开目标页面，筛选失败的网络请求，给出 URL、状态码、响应摘要与触发步骤。
```

### 5.4 截图与视觉检查

```text
把页面调整为 1440×900，截取整页截图，检查溢出、遮挡和对齐问题。
```

### 5.5 性能分析

```text
录制一次页面加载性能 trace，分析 LCP、CLS、关键请求链和主线程长任务，
按影响程度给出前三项优化建议。
```

## 六、运行模式

### 默认模式：独立浏览器配置

不加参数时，MCP 会启动专用 Chrome 实例，并在 Windows 的用户目录下保留专用浏览器配置。它不会直接复用日常 Chrome 的登录状态。

### 隔离模式：一次性配置

希望每次结束后清除临时浏览器数据，可在 `args` 中加入：

```toml
"--isolated"
```

### 无头模式

不需要看到浏览器窗口时加入：

```toml
"--headless"
```

### 连接已有 Chrome

Chrome 144 及以上可先在 `chrome://inspect/#remote-debugging` 开启远程调试，再向 MCP 参数加入：

```toml
"--autoConnect"
```

浏览器会询问是否允许调试连接。该模式可复用现有页面与登录状态，因此也会暴露该 Chrome 配置下所有已打开页面。

### 精简工具模式

只需导航、脚本执行和截图时加入：

```toml
"--slim"
```

## 七、隐私与安全

> [!warning] 浏览器内容会暴露给 MCP 客户端
> Chrome DevTools MCP 能读取、调试并修改所连接浏览器中的页面数据。不要在受控浏览器中打开不希望交给 Agent 的账号、密钥、支付或个人隐私页面。

- 默认使用独立浏览器配置；处理敏感任务时优先加 `--isolated`。
- 连接已有 Chrome 前关闭无关敏感页面。
- 手工开放 `9222` 调试端口时必须配合非默认 `--user-data-dir`，并仅绑定本机；任务结束后关闭调试浏览器。
- 性能工具默认可能把 trace 中的 URL 发送到 Google CrUX API 获取真实用户体验数据；不需要时加入 `--no-performance-crux`。
- 使用统计默认开启；不希望发送时加入 `--no-usage-statistics`。
- 截图可能包含账号信息，分享前应检查并脱敏。

隐私优先的参数组合示例：

```toml
args = [
    "/c",
    "npx",
    "-y",
    "chrome-devtools-mcp@latest",
    "--isolated",
    "--no-performance-crux",
    "--no-usage-statistics",
]
```

## 八、故障排查

### Codex 中看不到工具

1. 修改配置后完全重启 Codex；
2. 检查 `%USERPROFILE%\.codex\config.toml` 中表名是否为 `[mcp_servers.chrome-devtools]`；
3. 执行版本验证命令，确认 npm 包能被解析；
4. 检查 Node.js 是否为 LTS、Chrome 是否已安装。

### 启动超时

首次下载可能较慢，保留：

```toml
startup_timeout_ms = 20_000
```

如果网络环境更慢，可适当提高该值。

### 找不到 Chrome

确认 Chrome 安装于标准位置，并保留：

```toml
env = { SystemRoot="C:\\Windows", PROGRAMFILES="C:\\Program Files" }
```

若使用自定义安装路径，可在 MCP 参数中指定 `--executable-path`，具体参数以当前版本的 `--help` 为准。

### npm 警告

若出现与 `sass_binary_site` 等无关 npm 用户配置有关的 warning，但命令仍返回版本号，通常不影响 MCP 启动。可另行检查用户 `.npmrc`，不要为了消除警告修改本 MCP 配置。

### 查看当前参数

```powershell
cmd /c npx -y chrome-devtools-mcp@latest --help
```

## 九、升级与卸载

使用 `@latest` 时无需手工升级，下一次 `npx` 解析会使用最新版。固定版本时，修改配置中的版本号并重新执行版本验证。

卸载：

```powershell
codex mcp remove chrome-devtools
```

然后重启 Codex。

## 十、参考资料

- [Chrome DevTools MCP 官方仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [工具参考](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md)
- [故障排查](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md)
- [Codex MCP 官方文档](https://developers.openai.com/codex/mcp/)

## 关联笔记

- [[Agent扩展-MOC]]
- [[MCP-概念与架构]]
- [[02-opencli-browser]]

