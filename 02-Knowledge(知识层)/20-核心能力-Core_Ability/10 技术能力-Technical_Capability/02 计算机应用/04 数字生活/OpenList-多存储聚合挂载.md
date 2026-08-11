---
title: "OpenList 学习笔记"
domain: Core_Ability
tags: [OpenList, rclone, WebDAV, 网盘挂载, 多存储聚合]
status: 草稿
created: 2026-07-08
updated: 2026-08-10
verified: 2026-08-10
review_after: 2026-11-10
source: "https://doc.oplist.org/"
summary: "OpenList 多网盘聚合平台部署与 rclone/WebDAV 深度配置"
---

# OpenList 学习笔记

> 更新时间：2026-08-10 | 适用版本：OpenList 4.x

- [一、基础认知与服务配置](#一基础认知与服务配置)
  - [1.1 OpenList 概述](#11-openlist-概述)
  - [1.2 快速入门](#12-快速入门)
- [二、Windows 挂载方案](#二windows-挂载方案)
  - [2.1 rclone 配置](#21-rclone-配置)
  - [2.2 OpenList Desktop](#22-openlist-desktop)
  - [2.3 RaiDrive](#23-raidrive)
- [三、方案选择与故障排除](#三方案选择与故障排除)
- [四、本机配置与 NAS 接入](#四本机配置与-nas-接入)
  - [4.1 本机实际配置](#41-本机实际配置)
  - [4.2 绿联 NAS SMB 接入](#42-绿联-nas-smb-接入)
- [附录：关键信息速查](#附录关键信息速查)

---

## 一、基础认知与服务配置

### 1.1 OpenList 概述

#### 1.1.1 什么是 OpenList
![[Pasted image 20260708134246.png]]

官网：https://doc.oplist.org/ | GitHub：https://github.com/OpenListTeam/OpenList

OpenList 是 AList 的开源社区分支项目，定位为**多网盘聚合管理平台**。在 AList 被商业公司收购并引发隐私争议后，开源社区迅速推出了 OpenList，延续 AGPL-3.0 协议，承诺不收集用户数据，界面与操作逻辑与 AList 完全兼容，老用户可无缝迁移。

**核心能力**：将多个云盘统一挂载到单一入口，提供统一的访问接口：

| 接口类型 | 说明 |
|---------|------|
| Web UI | 浏览器直接访问，支持文件管理、在线预览、视频播放 |
| WebDAV | 供播放器、资源管理器、rclone 等客户端挂载 |
| FTP（插件） | 传统 FTP 客户端访问 |
| S3（插件） | 兼容 S3 协议的客户端/工具 |
| API | 程序化调用，支持二次开发 |

**支持部署平台**：Windows / Linux / macOS / Docker / NAS / 路由器 / 云服务器

#### 1.1.2 统一目录映射

所有存储挂载后会映射到统一目录结构下，例如：

```
/
├── pikpak      ← PikPak 网盘
├── kk          ← 夸克网盘
├── onedrive    ← OneDrive
├── alidrive    ← 阿里云盘
├── local       ← 本地磁盘
└── ...         ← 其他存储
```

所有客户端（浏览器、播放器、rclone 等）只需连接 OpenList 即可访问全部网盘，无需分别登录。

#### 1.1.3 架构图解

```
┌─────────────────────────────────────────────────────┐
│                    客户端层                           │
├─────────────┬─────────────┬─────────────────────────┤
│  浏览器      │  播放器/资源  │  rclone / RaiDrive     │
│  (Web UI)   │  管理器      │  / OpenList Mount      │
└──────┬──────┴──────┬──────┴────────────┬────────────┘
       │             │                   │
       ▼             ▼                   ▼
┌─────────────────────────────────────────────────────┐
│              OpenList 服务端                         │
│  ┌────────┬────────┬────────┬────────┬───────────┐ │
│  │ PikPak │ 夸克   │ OneDrive│ 百度   │ 本地磁盘  │ │
│  └────────┴────────┴────────┴────────┴───────────┘ │
└─────────────────────────────────────────────────────┘
```

开启 WebDAV 后，播放器（如 Infuse、Kodi、PotPlayer）、资源管理器、Jellyfin、Emby 等均可通过 WebDAV 协议访问 OpenList 背后的所有网盘资源。

---

### 1.2 快速入门

#### 1.2.1 环境准备

| 工具                   | 用途                           | 必装            | 下载地址 |
| -------------------- | ---------------------------- | ------------- | ---- |
| **OpenList Desktop** | 管理 OpenList、管理存储、自动启动、内置挂载管理 | ✅ 推荐          | [GitHub Releases](https://github.com/OpenListTeam/OpenList/releases) |
| **rclone**           | 挂载、同步、备份、加密、定时同步、脚本自动化       | 可选            | [rclone 官网](https://rclone.org/downloads/) |
| **WinFsp**           | Windows 下 rclone 挂载的底层依赖     | ⚠️ Windows 必装 | [WinFsp 官网](https://winfsp.dev/rel/) |

> ⚠️ **WinFsp 未安装时的报错**：`cgofuse: cannot find winfsp`

#### 1.2.2 添加存储

默认地址：`http://127.0.0.1:5244/`
用户名/密码：桌面应用获取

路径：`存储 → 添加`
![[Pasted image 20260708134530.png]]

1. 选择存储类型（如夸克网盘、阿里云盘等）
2. 填写挂载路径（如 `/kk`、`/alidrive`）
3. 按向导完成网盘授权/配置
4. 确认状态显示为 **"工作中"**

#### 1.2.3 默认开启 WebDAV

- 开启 WebDAV 服务【默认开启】
- 默认地址：`http://127.0.0.1:5244/dav`
- 各存储的 WebDAV 子路径：
  - `http://127.0.0.1:5244/dav/pikpak`
  - `http://127.0.0.1:5244/dav/kk`
  - `http://127.0.0.1:5244/dav/alidrive`

#### 1.2.4 用户权限配置

![[Pasted image 20260708134640.png]]

路径：`用户 → 编辑`

建议为 WebDAV 用户开启以下权限，否则客户端可能无法正常操作：

- [x] WebDAV 访问
- [x] 读取
- [x] 写入
- [x] 删除
- [x] 重命名
- [x] 上传
- [x] 下载

#### 1.2.5 验证测试

| 测试项    | 地址                          | 预期结果          |
| ------ | --------------------------- | ------------- |
| Web UI | `http://127.0.0.1:5244`     | 正常打开管理界面      |
| WebDAV | `http://127.0.0.1:5244/dav` | 返回目录列表（见下方说明） |

> **关于 WebDAV 验证**：浏览器直接访问 `http://127.0.0.1:5244/dav` 出现 `405 Method Not Allowed` **属于正常现象**。WebDAV 协议需要专用客户端（如 rclone、RaiDrive、Windows 网络驱动器、Infuse 等）进行访问，浏览器本身不支持 WebDAV 协议。用 rclone、RaiDrive 等客户端配置后能正常列出目录即可。

---

## 二、Windows 挂载方案

### 2.1 rclone 配置

#### 2.1.1 创建 Remote

编辑 `rclone.conf` 或在命令行中配置：

```ini
[pikpak]
type = webdav
url = http://127.0.0.1:5244/dav/pikpak
vendor = other
user = admin
pass = <加密后的密码>

[kk]
type = webdav
url = http://127.0.0.1:5244/dav/kk
vendor = other
user = admin
pass = <加密后的密码>
```

> 密码需通过 `rclone config` 生成加密版本，不可直接写明文。

#### 2.1.2 常用命令速查

| 命令 | 作用 | 示例 |
|------|------|------|
| `rclone lsd <remote>:` | 查看目录 | `rclone lsd pikpak:` |
| `rclone ls <remote>:` | 查看文件 | `rclone ls pikpak:` |
| `rclone copy <src> <dst> -P` | 复制（增量） | `rclone copy D:\Movie pikpak:/Movie -P` |
| `rclone sync <src> <dst> -P` | 同步（镜像，谨慎！） | `rclone sync D:\Movie pikpak:/Movie -P` |
| `rclone mount <remote>: <盘符> --vfs-cache-mode full` | 挂载为本地盘符 | `rclone mount pikpak: P: --vfs-cache-mode full` |

> 💡 **强烈建议始终开启 `--vfs-cache-mode full`**：WebDAV 无法流式写入，不开启缓存容易出现写入异常或文件损坏。

#### 2.1.3 挂载参数详解

##### 缓存参数

| 参数 | 说明 | 默认值 | 推荐值 |
|------|------|--------|--------|
| `--vfs-cache-mode` | 缓存模式 | `off` | `full`（WebDAV 必开） |
| `--vfs-cache-max-size` | 缓存文件最大总大小 | `10G` | `10G` ~ `50G`（视磁盘空间） |
| `--vfs-cache-max-age` | 缓存文件最大生命周期 | `24h` | `24h` ~ `168h` |
| `--dir-cache-time` | 目录列表缓存时间 | `5m` | `5m` ~ `30m` |

**三种缓存模式详解**：

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| `off` | 不缓存，直接透传 | ⚠️ **WebDAV 不可用**，仅本地存储 |
| `minimal` | 只缓存文件元信息（大小、修改时间等） | 读多写少、磁盘空间紧张 |
| `writes` | 缓存本地写入，文件写完后再上传 | 频繁写入、需要写入确认 |
| `full` | 缓存文件的完整内容 | ✅ **WebDAV 推荐**，读写混合、大文件传输 |

> 💡 **WebDAV 必开 `full` 模式**：WebDAV 协议不支持流式写入，不开启缓存会导致写入异常或文件损坏。

##### 性能参数

| 参数 | 说明 | 默认值 | 推荐值 |
|------|------|--------|--------|
| `--buffer-size` | 读取文件的缓冲区大小 | `16M` | `32M` ~ `64M`（大文件场景） |
| `--transfers` | 并行传输数量 | `4` | `4` ~ `8`（带宽充足时） |
| `--checkers` | 并行检查器数量 | `8` | `8` ~ `16` |
| `--vfs-read-chunk-size` | 读取块大小 | `128M` | `128M` ~ `256M`（大文件） |

##### 带宽参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `--bwlimit` | 全局带宽限制 | `--bwlimit=10M` |
| `--bwlimit` | 分别限制上传/下载 | `--bwlimit=10M:100M`（上传10M，下载100M） |
| `--bwlimit` | 基于时间的带宽限制 | `--bwlimit="08:00,512k 18:00,10M 23:00,off"` |

> 时间格式：`HH:MM,带宽值`，带宽值支持 `k`/`M`/`G` 后缀，`off` 表示不限速。

##### 网络参数

| 参数 | 说明 | 默认值 | 推荐值 |
|------|------|--------|--------|
| `--timeout` | 空闲超时时间 | `5m` | `5m` ~ `10m`（网络不稳定时增大） |
| `--contimeout` | 连接超时时间 | `1m` | `60s` |
| `--retries` | 重试操作次数 | `3` | `3` ~ `5` |
| `--low-level-retries` | 低级重试次数 | `10` | `10` ~ `20` |

##### 安全与权限参数

| 参数 | 说明 | 默认值 | 适用场景 |
|------|------|--------|----------|
| `--read-only` | 以只读模式挂载 | — | 共享访问、防止误删 |
| `--allow-other` | 允许其他用户访问挂载点 | — | 多用户系统 |
| `--allow-root` | 允许 root 用户访问挂载点 | — | 需要 root 访问时 |
| `--umask` | 覆盖文件权限 | `022` | 自定义文件权限 |

##### WebDAV 专用参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `--webdav-headers` | 设置自定义 HTTP 标头 | `--webdav-headers="User-Agent, rclone/1.0"` |
| `--webdav-bearer-token` | 自定义 Bearer Token | `--webdav-bearer-token="your-token"` |

##### 调试参数

| 参数 | 说明 | 适用场景 |
|------|------|----------|
| `--log-level=INFO` | 日志级别：`ERROR` / `NOTICE` / `INFO` / `DEBUG` | 日常运行用 `INFO`，排错用 `DEBUG` |
| `--verbose` | 打印更多详细信息 | 排错调试 |
| `--use-json-log` | 使用 JSON 格式记录日志 | 日志收集/分析系统 |
| `--progress` | 传输期间显示进度条 | 手动操作 |

#### 2.1.4 推荐配置组合

##### 场景 A：日常挂载（推荐）

适用于 Windows 下通过 OpenList WebDAV 挂载网盘，兼顾稳定性与性能：

```bash
rclone mount pikpak: P: \
  --vfs-cache-mode full \
  --vfs-cache-max-size 10G \
  --vfs-cache-max-age 24h \
  --buffer-size 32M \
  --transfers 4 \
  --timeout 5m \
  --progress
```

##### 场景 B：大文件传输 / 视频播放

适用于挂载后播放高清视频、传输大文件：

```bash
rclone mount pikpak: P: \
  --vfs-cache-mode full \
  --vfs-cache-max-size 50G \
  --vfs-cache-max-age 168h \
  --buffer-size 64M \
  --vfs-read-chunk-size 256M \
  --transfers 8 \
  --checkers 16 \
  --timeout 10m \
  --progress
```

##### 场景 C：带宽受限环境

适用于共享网络、需要限速避免影响其他设备：

```bash
rclone mount pikpak: P: \
  --vfs-cache-mode full \
  --buffer-size 16M \
  --transfers 2 \
  --bwlimit 10M \
  --timeout 5m \
  --progress
```

##### 场景 D：夜间自动同步（脚本化）

适用于定时备份脚本，配合 cron/任务计划：

```bash
rclone sync D:\Backup pikpak:/Backup \
  --vfs-cache-mode writes \
  --transfers 4 \
  --bwlimit "02:00,off 08:00,5M" \
  --log-level INFO \
  --use-json-log \
  --log-file="C:\logs\rclone-sync.log"
```

> 夜间（02:00-08:00）不限速，白天限速 5M，避免影响办公网络。

##### 场景 E：只读安全挂载

适用于共享给他人访问，防止误删误改：

```bash
rclone mount pikpak: P: \
  --vfs-cache-mode full \
  --read-only \
  --allow-other \
  --umask 022 \
  --buffer-size 32M \
  --timeout 5m
```

#### 2.1.5 完整 mount 命令模板

```bash
# Windows 命令行
rclone mount <remote>: <盘符>: \
  --vfs-cache-mode full \
  --vfs-cache-max-size 10G \
  --vfs-cache-max-age 24h \
  --buffer-size 32M \
  --vfs-read-chunk-size 128M \
  --transfers 4 \
  --checkers 8 \
  --timeout 5m \
  --contimeout 60s \
  --retries 3 \
  --low-level-retries 10 \
  --progress

# Linux/macOS（去掉盘符，改为挂载点路径）
rclone mount <remote>: /mnt/<remote> \
  --vfs-cache-mode full \
  --vfs-cache-max-size 10G \
  --buffer-size 32M \
  --allow-other \
  --daemon
```

---

### 2.2 OpenList Desktop

![[Pasted image 20260708134916.png]]
![[Pasted image 20260708134933.png]]
![[Pasted image 20260708134948.png]]

图形化一键挂载，适合不想维护 rclone 命令的用户。

| 配置项 | 填写内容 |
|--------|----------|
| Remote | `http://127.0.0.1:5244/dav/pikpak` |
| 挂载点 | `P:`（推荐盘符） |
| 远程路径 | 留空 |

---

### 2.3 RaiDrive

RaiDrive 将 WebDAV 挂载为 Windows 资源管理器中的虚拟磁盘，适合日常文件管理。

#### 2.3.1 安装 RaiDrive

下载地址：[RaiDrive 官网](https://www.raidrive.com/download)

#### 2.3.2 添加 WebDAV 连接

打开 RaiDrive → **Add** → **NAS** → **WebDAV**，填写：

| 配置项 | 值 |
|--------|-----|
| **URL** | `http://127.0.0.1:5244/dav` |
| **Port** | `5244`（默认填充） |
| **Account** | OpenList WebDAV 用户名（默认 `admin`） |
| **Password** | OpenList WebDAV 密码 |
| **Mount Point** | 选择一个空闲盘符（如 `P:`） |
| **Protocol** | `HTTP` |

> 若勾选 **Connect at login**，RaiDrive 会在系统启动时自动挂载。

#### 2.3.3 验证

连接成功后，打开「此电脑」会看到新的虚拟磁盘（如 `P:`），展开即可看到 OpenList 中已添加的所有网盘目录：

```
P:\
├── pikpak
├── kk
├── onedrive
└── alidrive
```

可直接在资源管理器中拖拽文件进行上传/下载/删除等操作。

#### 2.3.4 推荐配置

| 设置项 | 建议 | 原因 |
|--------|------|------|
| 缓存策略 | **开启**（默认） | 避免频繁请求导致服务端压力 |
| 自动重连 | **开启** | OpenList 重启后自动恢复挂载 |
| 开机启动 | 按需开启 | 日常使用推荐，服务器场景建议关闭 |

---

## 三、方案选择与故障排除

### 3.1 常见问题

#### 问题 1：URL 与远程路径重复配置

**错误做法**（路径重复拼接导致 404）：

```
URL:        http://127.0.0.1:5244/dav/pikpak
远程路径:   /pikpak
实际访问:   /dav/pikpak/pikpak  → 404 object not found
```

**正确做法（二选一）**：

| 方案 | URL | 远程路径 |
|------|-----|----------|
| A | `http://127.0.0.1:5244/dav/pikpak` | 留空 |
| B | `http://127.0.0.1:5244/dav` | `/pikpak` |

#### 问题 2：挂载点冲突

| ✅ 推荐 | ⚠️ 不推荐 |
|--------|-----------|
| `P:` / `Q:` / `R:` 等空闲盘符 | `F:\pikpak` 等目录挂载 |

> 目录挂载要求：目录**必须不存在**、未被资源管理器占用、无其他程序占用，否则报错 `mountpoint path already exists`。

#### 问题 3：WinFsp 未安装

Windows 下 rclone 挂载依赖 WinFsp，未安装时报错：

```
cgofuse: cannot find winfsp
```

#### 问题 4：WebDAV 统一根目录策略

**推荐**：统一使用 `http://127.0.0.1:5244/dav` 作为根，所有存储挂载为子目录：

```
/dav
├── pikpak
├── kk
├── onedrive
├── alidrive
└── 115
```

**好处**：新增存储时无需重新配置客户端，只需在 OpenList 中添加即可自动暴露。

---

### 3.2 WebDAV 客户端对比

| 工具 | 类型 | 核心优势 | 适合场景 |
|------|------|----------|----------|
| **rclone** | CLI | 功能最全、开源免费、支持同步/加密/脚本自动化/多平台 | 自动备份、数据同步、大文件传输、服务器环境 |
| **RaiDrive** | GUI | 图形界面、配置简单、直接映射盘符、支持多协议 | 日常办公、资源管理器直接访问 |
| **OpenList Desktop Mount** | GUI | 集成 rclone、一键挂载、自动管理配置、自动启动 | OpenList 用户、不想手动维护命令 |

---

### 3.3 推荐方案与完整流程

```
┌──────────────────────────────────────────────────────────┐
│                     OpenList 服务端                        │
│              ┌────────┬────────┬────────┐                │
│              │  Web   │ WebDAV │  API   │                │
│              └───┬────┴────┬───┴───┬────┘                │
└──────────────────┬──────────┼───────┼──────────────────────┘
                   │          │       │
         ┌─────────┴──────────┼───────┴──────────────┐
         │                    │                      │
      浏览器                rclone               RaiDrive
                              │                      │
                              ▼                      ▼
                        P:/Q:/R: 等              虚拟磁盘
                        虚拟磁盘
```

#### 完整部署流程

1. **安装 OpenList Desktop**（或 Docker/服务端部署） → [下载](https://github.com/OpenListTeam/OpenList/releases)
2. **添加各类网盘存储** → 确认状态为"工作中"
3. **开启 WebDAV 服务**
4. **配置用户权限**（读、写、上传、下载等）
5. **Windows 用户安装 WinFsp** → [下载](https://winfsp.dev/rel/)
6. **安装 rclone** → [下载](https://rclone.org/downloads/)
7. **使用 rclone 或 OpenList Desktop 挂载**
   - 优先选择未占用的盘符（P:/Q:/R:）
   - 若用目录挂载，确保目录不存在且未被占用
8. **使用 WebDAV 客户端统一访问所有网盘资源**

---

## 四、本机配置与 NAS 接入

### 4.1 本机实际配置

> [!info] 采集说明
> 本节于 2026-08-10 根据本机正在运行的 OpenList Desktop、OpenList 配置数据库、rclone 配置及进程状态整理。密码、令牌、Cookie、密钥等敏感信息未写入知识库。

#### 4.1.1 软件与运行目录

| 项目 | 当前配置 |
|------|----------|
| OpenList Desktop | `0.9.0` |
| OpenList Core | `v4.1.10`，前端 `v4.1.10` |
| OpenList 可执行文件 | `D:\softs\openlist.exe` |
| OpenList 数据目录 | `C:\Users\h2967\AppData\Roaming\OpenList Desktop\data` |
| SQLite 数据库 | `C:\Users\h2967\AppData\Roaming\OpenList Desktop\data\data.db` |
| rclone | `v1.74.3` |
| rclone 可执行文件 | `D:\softs\rclone-v1.74.3-windows-amd64\rclone.exe` |
| rclone 配置文件 | `D:\softs\rclone-v1.74.3-windows-amd64\rclone.conf` |

OpenList Desktop 当前未设置自动启动 OpenList 核心服务，但应用自身开启了自动更新；启动应用时显示主窗口。

#### 4.1.2 OpenList 服务端配置

| 项目 | 当前值 |
|------|--------|
| HTTP 监听 | `0.0.0.0:5244` |
| HTTPS | 未启用 |
| HTTP/2 Cleartext、HTTP/3 | 未启用 |
| 数据库 | SQLite，表前缀 `x_` |
| 日志 | 已启用，单文件上限 50 MB，最多 30 个备份，保留 28 天，不压缩 |
| 最大并发 | `64` |
| 内存映射阈值 | `4 MB` |
| 下载/传输/上传/复制/解压任务线程 | 均为 `5` |
| 下载重试 | `1` 次 |
| 传输、复制、解压重试 | `2` 次 |
| 上传重试 | `0` 次 |
| S3 / FTP / SFTP | 均未启用 |
| CORS | 来源、方法、请求头均允许 `*` |

> [!warning] 网络暴露
> 服务监听在 `0.0.0.0` 且未启用 HTTPS，局域网设备可直接访问 5244 端口。仅本机使用时可改为 `127.0.0.1`；需要局域网访问时，应配合防火墙、强密码或反向代理 HTTPS。

#### 4.1.3 已添加存储

| 挂载路径 | 驱动 | 状态 | WebDAV 策略 | Web 代理 | 缓存时间 |
|----------|------|------|---------------|----------|----------|
| `/夸克` | Quark | 工作中 | `native_proxy` | 开启 | 30 分钟 |
| `/pikpak` | PikPak | 工作中 | `302_redirect` | 关闭 | 30 分钟 |
| `/baidu` | BaiduNetdisk | 工作中 | `native_proxy` | 开启 | 30 分钟 |

三个存储均未禁用、允许索引且未启用签名；全局配置另行启用了“所有文件签名”和“隐藏存储详情”。

#### 4.1.4 用户与站点设置

| 项目 | 当前值 |
|------|--------|
| 管理员 | `admin`，根目录 `/`，已启用，拥有全部权限 |
| 访客 | `guest`，已禁用，无权限 |
| 站点标题 | `OpenList` |
| 挂载访问 | 允许 |
| 搜索索引 | 未启用，自动更新索引关闭，最大索引深度 20 |
| 单页数量 | 30，使用全量分页 |
| 存储详情 | 前台和管理页均隐藏 |
| 压缩包预览 | 默认开启 |
| 打包下载 | 开启 |
| 音频/视频自动播放 | 开启 |
| WebAuthn / SSO / LDAP | 均未启用 |
| 客户端与服务端限速 | 不限速 |

> [!warning] 凭据安全
> 当前挂载配置使用管理员账户连接 WebDAV。配置中保存了明文凭据，且密码强度偏低。建议新建仅具备所需目录与读写权限的专用 WebDAV 用户，并更换为随机强密码；笔记中不记录实际密码。

#### 4.1.5 rclone 挂载配置

| Remote | WebDAV 地址 | 目标盘符 | 自动挂载 | 当前状态 |
|--------|-------------|----------|----------|----------|
| `all` | `http://127.0.0.1:5244/dav/` | `Z:` | 是 | 正在运行，盘符可访问 |
| `pikpak` | `http://127.0.0.1:5244/dav/pikpak` | `P:` | 否 | 未挂载 |
| `夸克` | `http://localhost:5244/dav/kk` | `K:` | 否 | 未挂载 |

当前运行中的聚合盘命令等价于：

```powershell
rclone mount --config "D:\softs\rclone-v1.74.3-windows-amd64\rclone.conf" all: Z: `
  --vfs-cache-mode=full `
  --progress `
  --vfs-cache-max-age=24h `
  --timeout=5m `
  --buffer-size=32M `
  --vfs-read-chunk-size=128M `
  --transfers=4
```

> [!warning] 待整理项
> - `all` 的原始参数同时包含 `--transfers=8` 和 `--transfers=4`，存在重复；当前按后出现的 `4` 理解，建议删除前一个参数。
> - OpenList 中夸克的实际路径是 `/夸克`，但单独的 rclone Remote 指向 `/dav/kk`。若以后启用 `K:`，应先将地址核对为 `http://127.0.0.1:5244/dav/夸克`。
> - OpenList Desktop 目录下的默认 `rclone.conf` 是空文件，当前实际使用的是 `D:\softs\rclone-v1.74.3-windows-amd64\rclone.conf`，维护时不要改错文件。

---

### 4.2 绿联 NAS SMB 接入

适用场景：OpenList 安装在 Windows，文件实际存放在绿联 NAS。整体链路是：

```text
绿联 NAS 的 SMB 共享 → Windows 盘符或 UNC 路径 → OpenList 本地存储 → Z:\绿联NAS
```

OpenList 的“本地存储”可以挂载 Windows 当前能够访问的目录，具体字段参见[OpenList 本地存储官方说明](https://doc.oplist.org/guide/drivers/local.html)。

> [!warning] 盘符说明
> 当前 `Z:` 已用于 rclone 挂载 OpenList 聚合根目录，不能再分配给绿联 NAS。以下示例使用空闲的 `Y:`；实际操作前应先确认盘符未被占用。

#### 4.2.1 绿联 NAS 准备

1. 在绿联 NAS 中开启 SMB 文件服务。
2. 为需要访问的共享文件夹创建或选择专用账户。
3. 根据用途授予只读或读写权限，避免直接使用 NAS 管理员账户。
4. 建议在路由器中为 NAS 设置 DHCP 地址保留，避免 IP 地址变化导致挂载失效。

在 Windows 文件资源管理器地址栏输入 NAS 的 UNC 地址进行测试：

```text
\\绿联NAS的IP
```

例如：

```text
\\192.168.31.100
```

能够正常看到并打开目标共享文件夹后，再配置 OpenList。

#### 4.2.2 方案一：OpenList 由当前用户手动运行

此方案适用于当前使用 OpenList Desktop、由登录用户启动 OpenList 的情况。

1. 在文件资源管理器中打开 `\\绿联NAS的IP`。
2. 右键目标共享文件夹，选择“映射网络驱动器”。
3. 分配一个空闲盘符，例如 `Y:`。
4. 勾选“登录时重新连接”。
5. 输入绿联 NAS 的专用用户名和密码，并保存凭据。
6. 确认在资源管理器中可以正常读写 `Y:\`。
7. 在 OpenList 后台进入“存储 → 添加”，填写：

| 配置项 | 值 |
|--------|----|
| 驱动 | 本地存储 |
| 挂载路径 | `/绿联NAS` |
| 根文件夹路径 | `Y:\` |

保存后，在 OpenList 首页打开 `/绿联NAS`，确认可以浏览文件；由于 `Z:` 挂载的是 OpenList 根目录，最终也可从 `Z:\绿联NAS` 访问。

#### 4.2.3 方案二：OpenList 作为 Windows 服务运行

Windows 服务通常运行在独立会话中，可能看不到普通登录用户映射的 `Y:` 网络盘。这种情况下应直接使用 UNC 路径：

```text
\\192.168.31.100\共享文件夹名称
```

例如：

```text
\\192.168.31.100\影视
```

同时需要让 OpenList 服务使用有权访问 NAS 的 Windows 用户运行：

1. 按 `Win + R`，输入 `services.msc`。
2. 找到 OpenList 服务并打开“属性 → 登录”。
3. 选择“此账户”，填写对应的 Windows 用户和密码。
4. 使用该 Windows 用户访问一次 NAS，并选择记住 NAS 共享凭据。
5. 重启 OpenList 服务。
6. 在 OpenList 的“本地存储”中，将根文件夹路径填写为 UNC 路径。
7. 保存后验证目录浏览、文件读取以及必要的写入操作。

> [!tip] 选择建议
> - OpenList Desktop 手动启动：优先用 `Y:\`，配置直观，便于排查。
> - Windows 服务运行：优先用 UNC 路径，避免服务无法识别用户映射盘。
> - 如果重启电脑后目录为空、盘符失效或出现 `permission denied`，从盘符方案切换为 UNC 路径，并检查服务登录账户与 NAS 共享权限。

#### 4.2.4 验证清单

- [ ] Windows 可以访问 NAS 的 SMB 共享。
- [ ] OpenList 运行账户拥有 NAS 目录权限。
- [ ] OpenList 首页可以打开 `/绿联NAS`。
- [ ] `Z:\绿联NAS` 可以列出相同文件。
- [ ] 根据实际需要验证新建、上传、重命名和删除权限。
- [ ] Windows 重启后映射或 UNC 访问仍然有效。

---

## 附录：关键信息速查

| 项目 | 内容 |
|------|------|
| 开源协议 | AGPL-3.0 |
| GitHub | https://github.com/OpenListTeam/OpenList |
| 官方文档 | https://doc.oplist.org/ |
| 默认端口 | 5244 |
| WebDAV 根路径 | `http://<ip>:5244/dav` |
| 与 AList 兼容性 | 配置文件完全兼容，可直接迁移 |
| 支持网盘数 | 80+ 存储驱动 |

### 必开参数速查卡片

```
┌────────────────────────────────────────────────────────────┐
│                    rclone mount 必开参数                      │
├────────────────────────────────────────────────────────────┤
│  --vfs-cache-mode full          ← WebDAV 必开，防写入异常    │
│  --buffer-size 32M               ← 提升读取性能              │
│  --timeout 5m                    ← 网络波动容错              │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                    性能调优参数                              │
├────────────────────────────────────────────────────────────┤
│  --vfs-cache-max-size 10G        ← 缓存上限                 │
│  --vfs-cache-max-age 24h         ← 缓存过期                  │
│  --transfers 4                   ← 并行传输                  │
│  --checkers 8                    ← 并行检查                  │
│  --vfs-read-chunk-size 128M      ← 读取块大小                │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                    带宽控制参数                              │
├────────────────────────────────────────────────────────────┤
│  --bwlimit 10M                   ← 全局限速                  │
│  --bwlimit 10M:100M             ← 上传:下载分别限速         │
│  --bwlimit "08:00,512k 23:00,off" ← 分时段限速              │
└────────────────────────────────────────────────────────────┘
```
