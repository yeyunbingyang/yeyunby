---
title: "croc 安全跨平台文件传输工具"
tags: [GitHub, 开源, 工具, 终端, 文件传输, Go, 跨平台]
type: 工具
status: 待评估
created: 2026-07-28
updated: 2026-07-28
verified: 2026-07-28
review_after: 2026-10-28
source: https://github.com/schollz/croc
related: [Github优质项目-MOC]
summary: "croc 通过中继建立连接并使用 PAKE 端到端加密，让不同网络中的设备用短语安全传输文件、目录和文本，支持断点续传、浏览器互通与自建中继"
---

# croc 安全跨平台文件传输工具

## 基本信息

**类型：** 跨平台命令行文件传输工具  
**项目地址：** https://github.com/schollz/croc  
**官方网站：** https://getcroc.com  
**开发语言：** Go  
**许可证：** MIT  
**适用平台：** Windows、Linux、macOS、FreeBSD、Termux；浏览器客户端可与 CLI 互传

> [!abstract] 一句话说明
> croc 适合在两台不便配置局域网共享、SSH 或端口转发的设备之间，临时、安全地传输文件、目录或文本。

## 核心特点

- **连接简单**：发送端生成短语，接收端输入短语即可开始传输。
- **端到端加密**：使用密码认证密钥交换（PAKE）建立共享密钥，中继服务器不负责解密内容。
- **跨网络传输**：默认通过公共中继连接，无需搭建本地服务器或配置端口转发。
- **跨平台**：支持主流桌面系统，并可通过浏览器、Android 客户端等方式互通。
- **可靠传输**：支持多个文件、目录和中断后的断点续传。
- **部署灵活**：支持 SOCKS5 代理、IPv6 优先和自建中继。

## 安装

### Windows

任选一种包管理器：

```powershell
winget install schollz.croc
```

```powershell
scoop install croc
```

```powershell
choco install croc
```

### macOS

```bash
brew install croc
```

### 从源码安装

需要 Go 1.22 或更高版本：

```bash
go install github.com/schollz/croc/v10@latest
```

也可以直接从项目的 Releases 页面下载对应平台的可执行文件。

## 快速使用

### 发送文件或目录

```bash
croc send 文件或目录
```

发送端会显示一组代码短语，例如：

```text
Code is: example-code-phrase
```

### 接收

在另一台设备运行：

```bash
croc example-code-phrase
```

在 Linux 和 macOS 上，官方建议通过环境变量传入短语，避免它出现在进程名中：

```bash
CROC_SECRET="example-code-phrase" croc
```

### 常用操作

```bash
# 一次发送多个文件和目录
croc send 文件1 文件2 目录1

# 发送短文本或链接
croc send --text "hello world"

# 排除目录
croc send --exclude "node_modules,.venv" 项目目录

# 显示供移动设备扫描的二维码
croc send --qr 文件

# 自定义至少 6 个字符的代码短语
croc send --code "my-secret-code" 文件
```

## 自建中继

直接启动中继：

```bash
croc relay
```

默认使用 TCP 9009—9013 端口。发送时指定自建中继：

```bash
croc --relay "relay.example.com:9009" send 文件
```

Docker 部署示例：

```bash
docker run -d \
  -p 9009-9013:9009-9013 \
  -e CROC_PASS='替换为中继密码' \
  docker.io/schollz/croc
```

## 工作原理

1. 发送端与接收端使用同一代码短语连接中继。
2. 双方通过 PAKE 协议协商共享密钥。
3. 文件内容在发送端加密，在接收端解密。
4. 中继负责帮助双方建立连接和转发流量，不需要持有明文。

这意味着 croc 的便利性来自中继，而传输内容的保密性由端到端加密提供。若组织对网络边界、可用性或审计有更高要求，可部署自己的中继服务。

## 适用场景

- 临时向另一台电脑发送文件，无需配置共享目录。
- 跨公网、跨系统传输文件或目录。
- 通过短语或二维码向移动设备发送内容。
- 在脚本中通过标准输入、标准输出传递数据。
- 需要控制中继位置的团队内网或自托管环境。

## 使用注意

- 代码短语相当于本次传输的访问凭据，应通过可信渠道发送给接收方。
- Linux 和 macOS 上避免直接把敏感短语写入命令参数，优先使用 `CROC_SECRET` 环境变量。
- 公共中继可简化连接，但可用性依赖外部服务；敏感或稳定的组织内传输可考虑自建中继。
- 自动覆盖文件时需谨慎使用 `--yes --overwrite`，避免覆盖接收端已有文件。

## 评价

**优点：**

- 上手成本低，发送方和接收方通常各执行一条命令即可。
- 同时兼顾跨网络连接、端到端加密、跨平台和断点续传。
- 支持 CLI、浏览器、管道和自建中继，适用范围广。

**局限：**

- 双方都需安装兼容客户端或使用浏览器版本。
- 默认传输依赖公共中继；网络环境可能影响速度和可用性。
- 它更适合临时点对点传输，不替代带版本管理、权限体系和长期存储的网盘或对象存储。

**推荐程度：** ★★★★☆  
**是否值得长期保留：** 值得，适合作为临时跨设备文件传输的轻量工具。

## 相关导航

- [[Github优质项目-MOC]]
