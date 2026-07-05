---
title: C盘空间管理解决方案
domain: Core_Ability
tags: [Windows, 磁盘管理, 系统优化, SpaceSniffer]
status: 改进
created: 2026-04-15
updated: 2026-07-01
source: ""
related: []
summary: "通过诊断→清理→迁移→预防四步法，系统性地解决并预防 Windows C 盘空间不足问题，适配任意机器"
---

# C 盘空间管理解决方案

> **目标**：系统性地解决 C 盘空间不足问题，并建立长期机制防止再次爆满。
> 本方案**适配任意 Windows 机器**，不依赖特定用户名、盘符或软件清单。所有路径使用环境变量，命令可直接复制执行。

---

## 一、诊断方法：先看清谁在吃空间

在动手清理之前，必须先搞清楚"到底是什么占了 C 盘"。不同机器的"元凶"完全不同——有人是微信聊天记录，有人是 Docker 镜像，有人是 IDE 缓存。

### 1.1 推荐扫描工具

| 工具                | 类型       | 特点                        | 获取方式                                                      |
| ----------------- | -------- | ------------------------- | --------------------------------------------------------- |
| **WizTree**       | 免费       | 极快（直接读 MFT），可视化方块图，支持右键操作 | `winget install WizTree` 或 [官网](https://diskanalyzer.com) |
| **SpaceSniffer**  | 免费       | 可视化方块图，轻量免安装              | [官网](http://uderzo.it/main_products/space_sniffer/)       |
| **TreeSize Free** | 免费（有付费版） | 树状层级视图，可导出报告              | `winget install TreeSize.Free` 或官网                        |

> 💡 **强烈推荐 WizTree**：扫描 500GB 硬盘只需 5 秒。打开后直接看到每个文件夹的"方块大小"——哪个文件夹方块最大，就是清理的重点。

### 1.2 命令行快速扫描（无需安装工具）

```powershell
# PowerShell：查看 C 盘根目录各文件夹大小（管理员权限）
Get-ChildItem C:\ -Directory -ErrorAction SilentlyContinue |
    ForEach-Object {
        $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue |
                  Measure-Object -Property Length -Sum).Sum / 1GB
        [PSCustomObject]@{ 路径=$_.FullName; 大小GB=[math]::Round($size, 1) }
    } | Sort-Object 大小GB -Descending | Format-Table -AutoSize
```

```cmd
:: CMD：查看用户目录下前 10 大文件夹
dir "%USERPROFILE%" /s | findstr /i "File(s)" | more
:: 更推荐直接用 WizTree，直观得多
```

### 1.3 判断标准

| C 盘剩余    | 状态    | 行动              |
| -------- | ----- | --------------- |
| < 10 GB  | 🔴 危险 | 立即执行第二章紧急清理     |
| 10-25 GB | 🟡 警戒 | 执行第二章 + 规划第四章迁移 |
| 25-50 GB | 🟢 健康 | 定期维护即可          |
| > 50 GB  | ✅ 充足  | 建立长期预防习惯        |

### 1.4 典型"元凶"速查（用 WizTree 重点看这些路径）

| 路径（环境变量）            | 通常是什么   | 常见占用                 |
| ------------------- | ------- | -------------------- |
| `%USERPROFILE%`     | 用户全部数据  | 通常最大                 |
| `%LOCALAPPDATA%`    | 软件本地缓存  | IDE/浏览器/聊天软件         |
| `%APPDATA%`         | 软件配置与数据 | 部分软件数据存这里            |
| `C:\ProgramData`    | 全局程序数据  | NVIDIA 驱动/Adobe/各类服务 |
| `C:\Windows\WinSxS` | 系统组件存储  | 通常 10-20 GB          |
| `C:\Windows\Temp`   | 系统临时文件  | 可安全清理                |

---

## 二、安全清理（风险分级）

### Level 1：零风险——随时随地可执行

> ✅ 这些操作完全安全，无需关闭任何程序，不会影响任何软件功能。

#### 2.1.1 临时文件清理

```powershell
# PowerShell（推荐）
Remove-Item "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
```

```cmd
:: CMD 方式
rmdir /s /q "%TEMP%"
mkdir "%TEMP%"
rmdir /s /q "%LOCALAPPDATA%\Temp"
mkdir "%LOCALAPPDATA%\Temp"
rmdir /s /q "C:\Windows\Temp"
mkdir "C:\Windows\Temp"
```

> 💡 正在使用的临时文件会自动跳过，安全无风险。

#### 2.1.2 回收站清空

```powershell
# PowerShell
Clear-RecycleBin -Force -ErrorAction SilentlyContinue
```

```cmd
:: CMD
rd /s /q C:\$Recycle.Bin
```

#### 2.1.3 浏览器缓存

各浏览器自带清理更安全：

| 浏览器 | 操作路径 | 清理项 |
|--------|----------|--------|
| **Chrome** | `chrome://settings/clearBrowserData` | 缓存的图片和文件 |
| **Edge** | `edge://settings/clearBrowserData` | 缓存的图片和文件 |
| **Firefox** | `about:preferences#privacy` | 缓存 |

> 💡 浏览器缓存是"可再生的"——清理后访问网站时会自动重建，不影响使用。

#### 2.1.4 下载文件夹

```powershell
# 按大小排序查看下载文件夹（不直接删，让你判断）
Get-ChildItem "$env:USERPROFILE\Downloads" -Recurse -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object -First 20 Name, @{N='大小MB';E={[math]::Round($_.Length/1MB,1)}}
```

> 💡 很多"安装包、压缩包、镜像文件"下载完就忘在 Downloads 里了。手动检查后删除即可。

---

### Level 2：可控清理——确认后可执行

> 🔧 这些操作同样安全，但会清除可重建的缓存。执行后首次启动相关软件可能稍慢（需重建缓存），不影响数据和配置。

#### 2.2.1 Windows 磁盘清理工具

```cmd
:: CMD（管理员）
:: 第一步：选择要清理的项目（勾选所有选项，包括"Windows 更新清理"）
cleanmgr /sageset:1

:: 第二步：执行清理
cleanmgr /sagerun:1
```

> 💡 首次 `/sageset:1` 弹出选择窗口，勾选所有项后关闭；后续直接 `/sagerun:1` 静默执行。
> "Windows 更新清理"是最大的单项，可能回收 5-15 GB。

#### 2.2.2 包管理器缓存

```bash
# npm 缓存
npm cache clean --force

# pip 缓存
pip cache purge

# pnpm 缓存（如果使用）
pnpm store prune
```

```powershell
# 也可直接删目录
Remove-Item "$env:LOCALAPPDATA\npm-cache" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\pip\cache" -Recurse -Force -ErrorAction SilentlyContinue
```

#### 2.2.3 Docker 清理

```bash
# 清理所有未使用的镜像、容器、网络、构建缓存
docker system prune -a --volumes

# 如果 Docker Desktop 的磁盘镜像太大，在设置中调整
# Docker Desktop → Settings → Resources → Advanced → Disk image location
```

> ⚠️ `-a` 会删除**所有**未使用镜像（不只是 dangling），确认后再执行。

#### 2.2.4 IDE / 开发工具缓存（通用思路）

WizTree 扫描后，在 `%LOCALAPPDATA%` 和 `%APPDATA%` 下找到对应厂商目录，删除其缓存子目录即可：

```
常见位置（通过 WizTree 确认）：
%LOCALAPPDATA%\JetBrains       → IDE 缓存（安全删除，IDE 重建）
%LOCALAPPDATA%\Programs        → 各类编辑器/IDE 缓存
%APPDATA%\<编辑器名>           → 编辑器用户数据（注意区分缓存 vs 配置）
```

> ✅ **判断原则**：目录名含 `Cache`/`Temp`/`Logs`/索引 → 安全删除。含 `Settings`/`Config`/`Plugins` → 谨慎，先备份。

#### 2.2.5 国内软件缓存（腾讯/阿里/字节等）

这些软件的缓存通常在应用内清理更安全：

| 软件类型 | 通用清理路径 | 方式 |
|----------|-------------|------|
| **即时通讯类**（微信/QQ/飞书/钉钉） | 设置 → 存储管理/文件管理 → 清理缓存 | **应用内**（最安全） |
| **文档协作类**（语雀/石墨/腾讯文档） | 设置 → 缓存清理 | 应用内 |
| **网盘类**（百度/阿里/夸克） | 设置 → 传输 → 清理缓存 + 改下载路径 | 应用内 |

> ⚠️ 聊天软件的"聊天记录"（而非缓存）删除前请确认已备份。缓存（图片缩略图、视频预览等）则可安全清理。

---

## 三、系统级精简

> ⚙️ 这些操作面向系统本身，回收量较大但需要管理员权限。按需选择。

### 3.1 关闭休眠功能（回收 = 内存大小的磁盘空间）

如果使用 SSD + 快速启动已经够用，可以关闭休眠：

```cmd
:: CMD（管理员）——关闭休眠，删除 hiberfil.sys 文件
powercfg /h off
```

```powershell
# PowerShell（管理员）
powercfg /h off
```

> 💡 关闭后回收的空间 = 物理内存大小（如 32GB 内存回收 ~32GB）。
> ⚠️ 关闭后**快速启动也会失效**（快速启动依赖休眠文件）。如果在意开机速度，可以缩小而非关闭：
> `powercfg /h /size 50`（将休眠文件缩小到内存的 50%）

### 3.2 调整虚拟内存

```powershell
# 查看当前虚拟内存设置
Get-WmiObject Win32_PageFile | Select-Object Name, InitialSize, MaximumSize
```

**手动调整**：
1. `Win + Pause` → 高级系统设置 → 高级 → 性能 → 设置 → 高级 → 虚拟内存 → 更改
2. 取消"自动管理" → 选择 C 盘 → 选择"无分页文件" → 设置
3. 选择 `<数据盘>` → 选择"自定义大小" → 初始 = 2048 MB，最大 = 物理内存的 1-2 倍 → 设置
4. 重启生效

> ⚠️ 不要把虚拟内存完全禁用——部分老程序会崩溃。只是把它从 C 盘挪到数据盘。

### 3.3 WinSxS 组件清理

```cmd
:: CMD（管理员）
:: 分析当前 WinSxS 大小
dism /online /Cleanup-Image /AnalyzeComponentStore

:: 清理可回收的组件（安全，不删除当前更新）
dism /online /Cleanup-Image /StartComponentCleanup
```

```powershell
# PowerShell（管理员）
dism /online /Cleanup-Image /StartComponentCleanup
```

> 💡 通常可回收 3-10 GB。
> ⚠️ **不要加 `/ResetBase`**——那会让你无法卸载已安装的 Windows 更新。确认系统运行稳定后再考虑。

### 3.4 系统还原点管理

```cmd
:: CMD（管理员）——查看当前还原点占用
vssadmin list shadowstorage
```

```powershell
# PowerShell（管理员）——限制还原点空间上限（如 10 GB）
vssadmin resize shadowstorage /on=C: /for=C: /maxsize=10GB
```

> 💡 系统还原点默认可能占用 10-20 GB，限制到 5-10 GB 即可满足日常恢复需求。

---

## 四、用户程序数据迁移方案 ⭐

> 🎯 **本章是解决 C 盘问题的核心——清理只能治标，迁移才能治本。**

### 4.0 迁移前安全准备

**无论选择哪种迁移方案，请先完成以下步骤：**

```powershell
# 1. 创建系统还原点（管理员 PowerShell）
Checkpoint-Computer -Description "C盘数据迁移前" -RestorePointType MODIFY_SETTINGS
```

```cmd
:: CMD 管理员方式
wmic.exe /namespace:\\root\default Path SystemRestore Call CreateRestorePoint "C盘数据迁移前", 100, 7
```

2. **记录原始路径**：新建一个文本文件，记录你要迁移的每个文件夹的**原始路径 → 目标路径**，方便后续排查问题。
3. **关闭所有正在运行的程序**：尤其是 IDE、聊天软件、浏览器、Docker Desktop。
4. **确保使用管理员权限的 CMD**：部分操作在 PowerShell 中无法正确执行（如 `mklink`）。

---

### 4.1 三层迁移策略总览

| 层级 | 方案 | 风险 | 覆盖范围 | 推荐场景 |
|------|------|------|----------|----------|
| **🟢 轻量** | Windows 原生文件夹移动 | 零风险 | Downloads/Desktop/Documents 等 6 个 | 所有人，首先执行 |
| **🟡 中度** | 软件配置改路径 / 局部 Junction | 低风险 | 各软件缓存/数据目录 | 开发者和重度软件用户 |
| **🔴 重度** | Junction 整个 AppData | 高风险 | 全部用户应用数据 | 仅 C 盘极小 + 有备份 + 有动手能力 |

---

### 4.2 轻量方案：Windows 原生文件夹移动 ✅ 最推荐

Windows 自带功能，操作最简单、最安全、完全可逆。

覆盖这 6 个文件夹，基本把用户数据的 **80% 日常增量** 都挪走了：

| 文件夹 | 环境变量路径 | 优先度 | 说明 |
|--------|-------------|--------|------|
| **Downloads** | `%USERPROFILE%\Downloads` | ⭐⭐⭐ | 浏览器/软件下载——增量最大 |
| **Desktop** | `%USERPROFILE%\Desktop` | ⭐⭐⭐ | 防止桌面堆文件 |
| **Documents** | `%USERPROFILE%\Documents` | ⭐⭐ | IDE 项目 + 各类文档 |
| **Videos** | `%USERPROFILE%\Videos` | ⭐⭐ | 录屏 / 下载视频 |
| **Pictures** | `%USERPROFILE%\Pictures` | ⭐ | 截图 / 图片 |
| **Music** | `%USERPROFILE%\Music` | ⭐ | 音乐文件 |

**操作步骤**：
1. 在 `<数据盘>:` 上创建目标文件夹（如 `<数据盘>:\Users\<用户名>\Downloads`）
2. 在 C 盘右键目标文件夹（如 `C:\Users\<用户名>\Downloads`）→ **属性**
3. 切换到 **位置** 标签页
4. 点击 **移动** → 选择目标路径
5. 点击 **是**（移动已有文件）

> ✅ **效果**：之后任何软件往这些文件夹存东西，物理上实际存储在数据盘。对软件完全透明。
> 🔄 **回滚**：同样步骤，点"还原默认值"即可。

---

### 4.3 中度方案 A：逐软件修改数据/缓存路径

不改系统结构，只是告诉每个软件"把你的数据存到数据盘"。

#### 4.3.1 常见软件路径配置速查表

| 软件 / 工具            | 配置方式                | 具体操作或命令                                                                |
| ------------------ | ------------------- | ---------------------------------------------------------------------- |
| **微信**             | 应用内设置               | 设置 → 文件管理 → 更改文件存储路径 → `<数据盘>:\WeChatFiles`                            |
| **QQ**             | 应用内设置               | 设置 → 文件管理 → 更改存储路径                                                     |
| **飞书**             | 应用内设置               | 设置 → 存储管理 → 更改文件存储路径                                                   |
| **钉钉**             | 应用内设置               | 设置 → 通用 → 文件存储位置                                                       |
| **百度网盘**           | 应用内设置               | 设置 → 传输 → 下载路径 → `<数据盘>:\BaiduNetdiskDownload`                         |
| **Chrome / Edge**  | 应用内设置               | 设置 → 下载内容 → 位置 → `<数据盘>:\Downloads`                                    |
| **VS Code**        | 改快捷方式参数             | 快捷方式 → 目标 加 `--extensions-dir "<数据盘>:\VSCode\extensions"`              |
| **JetBrains IDE**  | 改 `idea.properties` | `idea.system.path=<数据盘>:/JetBrains/system`（各 IDE 略有不同）                 |
| **npm**            | 命令行                 | `npm config set cache "<数据盘>:\npm-cache"`                              |
| **pip**            | 环境变量                | 设置 `PIP_CACHE_DIR=<数据盘>:\pip-cache`                                    |
| **pnpm**           | 环境变量                | 设置 `PNPM_STORE_PATH=<数据盘>:\pnpm-store`                                 |
| **Docker Desktop** | 应用内设置               | Settings → Resources → Advanced → Disk image location                  |
| **WSL 发行版**        | 命令行                 | `wsl --export <发行版名> <数据盘>:\wsl-backup.tar` → 卸载 → `wsl --import` 到新位置 |
| **Steam**          | 应用内设置               | 设置 → 下载 → Steam 库文件夹 → 添加 `<数据盘>:\SteamLibrary`                        |
| **Epic Games**     | 应用内设置               | 设置 → 游戏库位置 → `<数据盘>:\EpicGames`                                        |

#### 4.3.2 通用查找方法

如果某软件不在上表中，用以下方法找到它的缓存/数据路径：

1. **WizTree 扫描** → 在 `%LOCALAPPDATA%` 或 `%APPDATA%` 下找到该软件的文件夹 → 看哪些子目录最大
2. **软件自身设置** → 几乎所有有数据的软件都会在"设置"中提供路径修改选项
3. **搜索引擎搜索**：`<软件名> change cache location Windows`
4. **便携化工具**：部分软件（如 VS Code / Sublime Text）本身支持便携模式，下载 zip 版直接解压到数据盘即可

---

### 4.4 中度方案 B：局部 Junction 重定向（单个缓存目录）

> ⚠️ **重要**：以下命令必须在 **CMD（管理员）** 中执行，**不要在 PowerShell 中执行**！
> - `mklink` 是 CMD 内置命令，PowerShell 无法直接识别
> - 在 PowerShell 中 `%变量%` 不会自动展开，会变成字面量

#### 适用场景

- 某软件的缓存目录巨大（如某个 IDE 缓存 10+ GB），但软件自身不提供改路径选项
- 只想重定向一两个特定目录，不想大动干戈

#### 完整操作流程（以迁移某个缓存目录为例）

假设要将 `C:\Users\<用户名>\AppData\Local\SomeApp\Cache` 迁移到 `<数据盘>:\AppData\SomeApp\Cache`：

```cmd
:: ========== CMD（管理员） ==========

:: 第 1 步：检查目标盘的目录结构
dir "<数据盘>:\AppData\SomeApp" 2>nul || mkdir "<数据盘>:\AppData\SomeApp"

:: 第 2 步：复制文件（/MIR 镜像 /R:0 不重试 /W:0 不等待）
robocopy "%LOCALAPPDATA%\SomeApp\Cache" "<数据盘>:\AppData\SomeApp\Cache" /MIR /R:0 /W:0

:: 第 3 步：确认 robocopy 无报错（Exit code 0-3 均为正常，≥8 为异常）
:: robocopy 返回码：0=无变化 1=有复制 2=有多余文件 3=1+2 都正常

:: 第 4 步：备份原目录（改名而非直接删除）
ren "%LOCALAPPDATA%\SomeApp\Cache" "Cache_backup_%date:~0,4%%date:~5,2%%date:~8,2%"

:: 第 5 步：建立 Junction 链接
mklink /J "%LOCALAPPDATA%\SomeApp\Cache" "<数据盘>:\AppData\SomeApp\Cache"

:: 第 6 步：验证链接
dir /al "%LOCALAPPDATA%\SomeApp\"
:: 应该看到 Cache [Junction] → 目标路径

:: 第 7 步：启动对应软件，测试功能正常后，删除备份
:: rmdir /s /q "%LOCALAPPDATA%\SomeApp\Cache_backup_YYYYMMDD"
```

#### 验证 Junction 是否正确

```cmd
:: 列出某目录下所有 Junction
dir /al /s "%LOCALAPPDATA%\SomeApp"

:: 检查文件是否可通过链接访问
dir "<数据盘>:\AppData\SomeApp\Cache"
```

```powershell
# PowerShell 方式查看链接
Get-ChildItem "$env:LOCALAPPDATA\SomeApp" -Attributes ReparsePoint -Recurse |
    ForEach-Object { $_.FullName + " → " + $_.Target }
```

#### 回滚（删除 Junction，恢复原目录）

```cmd
:: CMD（管理员）——误操作或出问题时的恢复步骤

:: 1. 删除链接（注意：rmdir 删除的是链接本身，不会删除目标内容！）
rmdir "%LOCALAPPDATA%\SomeApp\Cache"

:: 2. 恢复备份目录
ren "%LOCALAPPDATA%\SomeApp\Cache_backup_YYYYMMDD" "Cache"

:: 3. 验证恢复
dir "%LOCALAPPDATA%\SomeApp\Cache"
```

> ✅ **Junction 的安全性**：
> - `rmdir` 删除 Junction 链接时**只删除链接本身**，不会删除目标目录中的文件。
> - `del` / 资源管理器删除 Junction 内的文件时，**实际删除的是目标目录中的文件**——这是预期行为。
> - 这就是为何操作前先改名备份——随时可以恢复。

#### 适合 Junction 的典型目录

| 目录类型       | 示例路径                                                   | 理由             |
| ---------- | ------------------------------------------------------ | -------------- |
| **IDE 缓存** | `%LOCALAPPDATA%\JetBrains`、`%APPDATA%\Code\Cache`      | 大但不影响配置        |
| **浏览器缓存**  | `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache` | 纯缓存，安全         |
| **包管理器缓存** | `%LOCALAPPDATA%\npm-cache`、`%LOCALAPPDATA%\pip`        | 纯缓存，可重建        |
| **聊天软件数据** | 微信/QQ/飞书的 FileStorage 目录                               | 先确认软件不支持改路径后再用 |

---

### 4.5 重度方案：Junction 整个 AppData（高风险）

> 🔴 **仅当以下条件全部满足时才考虑：**
> - C 盘空间极小（< 128 GB SSD），物理上装不下开发工具链
> - 已经执行了轻量+中度方案，仍然不够
> - 有完整的系统备份或刚做完系统镜像
> - 理解 Junction 的工作原理和风险

#### 完整操作流程

```cmd
:: ========== CMD（管理员）——全程操作 ==========
:: ⚠️ 执行前：关闭所有程序！创建系统还原点！备份重要数据！

:: ====== 第 1 步：在数据盘创建目标目录 ======
mkdir "<数据盘>:\AppData\Local"
mkdir "<数据盘>:\AppData\Roaming"

:: ====== 第 2 步：复制文件（耗时较长，耐心等待） ======
robocopy "%LOCALAPPDATA%" "<数据盘>:\AppData\Local" /MIR /R:2 /W:5 /XJ
robocopy "%APPDATA%" "<数据盘>:\AppData\Roaming" /MIR /R:2 /W:5 /XJ

:: ====== 第 3 步：检查 robocopy 返回码 ======
:: 返回码 0-3 = 正常（复制完成，无未决错误）
:: 返回码 ≥ 8 = 有文件复制失败，不要继续！先排查原因

:: ====== 第 4 步：备份原目录（改名） ======
:: 这一步需要关闭所有程序，否则 AppData 中的文件会被锁定
ren "%LOCALAPPDATA%" "Local_backup_%date:~0,4%%date:~5,2%%date:~8,2%"
ren "%APPDATA%" "Roaming_backup_%date:~0,4%%date:~5,2%%date:~8,2%"

:: 如果 ren 失败（文件被占用），重启到安全模式再执行

:: ====== 第 5 步：建立 Junction ======
mklink /J "%LOCALAPPDATA%" "<数据盘>:\AppData\Local"
mklink /J "%APPDATA%" "<数据盘>:\AppData\Roaming"

:: ====== 第 6 步：验证 ======
dir /al "%USERPROFILE%\AppData"
:: 应看到 Local [Junction] 和 Roaming [Junction]
```

#### 风险说明

| 风险 | 可能性 | 影响 | 缓解措施 |
|------|--------|------|----------|
| 部分程序拒绝走 Junction 路径 | 低（但存在） | 软件启动失败 | 逐个排查，对特定软件回滚 |
| Windows 更新后链接失效 | 极低 | 系统异常 | 保留原目录备份 |
| 数据盘故障导致系统不稳定 | 中（取决于硬盘） | 大量软件无法使用 | 数据盘定期备份 |
| 用户 Profile 损坏 | 低 | 无法登录 | 创建系统还原点 |

#### 完整回滚方案

```cmd
:: ========== 回滚：恢复 AppData 到 C 盘（CMD 管理员） ==========

:: 1. 删除 Junction 链接（不会删除目标目录中的文件）
rmdir "%LOCALAPPDATA%"
rmdir "%APPDATA%"

:: 2. 恢复备份目录
ren "%USERPROFILE%\AppData\Local_backup_YYYYMMDD" "Local"
ren "%USERPROFILE%\AppData\Roaming_backup_YYYYMMDD" "Roaming"

:: 3. 重启计算机
shutdown /r /t 0
```

> ⚠️ **最关键的安全措施**：第四步的 `ren`（改名）而非 `rmdir`（删除）——这意味着你可以随时回滚。

---

### 4.6 迁移方案选择决策树

```
C 盘剩余空间不足？
├── 是 → 先执行第二章安全清理
│   └── 清理后还不足？
│       ├── 是 → 轻量方案（4.2）：移动 Downloads/Desktop 到数据盘
│       │   └── 还不够？
│       │       ├── 是 → 中度方案 A（4.3）：逐软件改缓存路径
│       │       │   └── 有软件不支持改路径？
│       │       │       └── 是 → 中度方案 B（4.4）：局部 Junction 单个缓存目录
│       │       └── C 盘 < 128 GB 且中度方案不够？
│       │           └── 是 → 慎重评估重度方案（4.5）
│       └── 否 → 建立第五章的长期预防习惯
└── 否 → 直接建立第五章的长期预防习惯
```

---

## 五、长期预防

### 5.1 开启 Windows 存储感知（自动清理）

**设置路径**：`Win + I` → 系统 → 存储 → 存储感知 → **开启**

| 选项              | 建议设置        |
| --------------- | ----------- |
| 临时文件清理          | 每天          |
| 回收站清理           | 14 天        |
| 下载文件夹清理         | 从不（手动管理更安全） |
| OneDrive 文件本地副本 | 仅保留最近使用的    |

### 5.2 限制系统还原点空间

```powershell
# PowerShell（管理员）——限制 10 GB
vssadmin resize shadowstorage /on=C: /for=C: /maxsize=10GB
```

### 5.3 养成习惯

#### 每周（30 秒）

```bash
npm cache clean --force   # 或 pip cache purge
```

#### 每月（2 分钟）

```powershell
# 清理所有临时文件
Remove-Item "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

# 执行 Windows 磁盘清理（静默）
cleanmgr /sagerun:1
```

#### 每季度（5 分钟）检查清单

- [ ] 用 WizTree 扫描 C 盘，关注比上季度明显增大的目录
- [ ] 各聊天软件/网盘内清理缓存
- [ ] 执行 WinSxS 精简：`dism /online /Cleanup-Image /StartComponentCleanup`
- [ ] 检查 C 盘剩余：**低于 25 GB 就要警觉，低于 10 GB 立即行动**
- [ ] 清理下载文件夹中不再需要的安装包、压缩包
- [ ] Docker Desktop → Troubleshoot → Clean / Purge data（如使用）

#### 安装新软件时

- [ ] 大型软件优先安装到数据盘（安装时选"自定义安装"）
- [ ] 首次启动后立即检查设置 → 将数据/缓存路径改到数据盘
- [ ] 游戏平台（Steam/Epic）默认库设为数据盘

---

## 六、常见问题

### 6.1 误删了重要文件怎么办？

1. **检查回收站** → 如果还在直接还原
2. **系统还原** → `Win + R` → `rstrui` → 选择迁移前创建的还原点
3. **文件恢复工具** → Recuva（免费）/ DiskGenius ——但**删除后越早操作恢复率越高**，删除后不要再往该盘写入新文件
4. **如果做了备份目录改名**（方案 B 的重度操作）→ 参照 4.4/4.5 的回滚步骤恢复

### 6.2 Junction 链接断了 / 失效了怎么办？

**症状**：软件报错"找不到文件"或启动失败。

**排查**：

```cmd
:: 检查链接是否还存在
dir /al "%USERPROFILE%\AppData"

:: 检查目标路径是否还存在
dir "<数据盘>:\AppData\Local"
```

**修复**：

```cmd
:: 1. 删除残留的失效链接
rmdir "失效的链接路径"

:: 2. 重新建立链接
mklink /J "链接路径" "目标路径"
```

### 6.3 为什么不在 PowerShell 中执行 mklink？

- `mklink` 是 **CMD 的内部命令**（不是独立的 .exe 文件），PowerShell 无法直接调用
- 在 PowerShell 中使用 `%LOCALAPPDATA%` 时，环境变量**不会自动展开**，会变成字面量
- 如果非要在 PowerShell 中用：`cmd /c mklink /J "链接" "目标"`
- **最佳实践**：涉及 Junction 的操作一律用管理员 CMD

### 6.4 休眠文件删了又出现了？

Windows 更新或某些系统操作可能重新创建 `hiberfil.sys`。重新执行即可：

```cmd
powercfg /h off
```

### 6.5 C 盘又满了，且 WizTree 显示的主要是"未知"或"系统"文件？

可能的原因和排查顺序：
1. **Windows 更新缓存** → `cleanmgr` → 勾选"Windows 更新清理"
2. **系统还原点** → `vssadmin list shadowstorage` 查看
3. **Windows Search 索引** → 服务中重启 Windows Search
4. **页面文件** → 检查 `C:\pagefile.sys` 大小
5. **磁盘错误** → `chkdsk C: /f`（需重启）

### 6.6 如何查看和管理所有已创建的 Junction？

```cmd
:: CMD：列出 C 盘所有 Junction
dir /al /s C:\ | findstr "<JUNCTION>"
```

```powershell
# PowerShell：列出用户目录下所有 Junction
Get-ChildItem "$env:USERPROFILE" -Attributes ReparsePoint -Recurse -ErrorAction SilentlyContinue |
    Select-Object FullName |
    ForEach-Object { Write-Output $_.FullName }
```

---

## 附录 A：Windows 环境变量速查

| 变量名                   | 实际路径示例                                | 用途             |
| --------------------- | ------------------------------------- | -------------- |
| `%USERPROFILE%`       | `C:\Users\<你的用户名>`                    | 用户主目录          |
| `%LOCALAPPDATA%`      | `C:\Users\<你的用户名>\AppData\Local`      | 本地应用数据（大文件多在这） |
| `%APPDATA%`           | `C:\Users\<你的用户名>\AppData\Roaming`    | 漫游应用数据         |
| `%TEMP%`              | `C:\Users\<你的用户名>\AppData\Local\Temp` | 用户临时文件         |
| `%SystemRoot%`        | `C:\Windows`                          | Windows 系统目录   |
| `%ProgramData%`       | `C:\ProgramData`                      | 全局程序数据         |
| `%ProgramFiles%`      | `C:\Program Files`                    | 64 位程序安装目录     |
| `%ProgramFiles(x86)%` | `C:\Program Files (x86)`              | 32 位程序安装目录     |
| `%HOMEDRIVE%`         | `C:`                                  | 系统盘符           |

> 💡 **使用环境变量的好处**：无需知道当前用户名，命令在任何 Windows 电脑上都能直接复制执行。`<数据盘>:` 为占位符，替换为你的实际盘符（如 `D:`、`E:` 等）。

## 附录 B：CMD vs PowerShell 命令对照

| 场景 | CMD（推荐用于 Junction） | PowerShell（推荐用于批量删除） |
|------|------------------------|---------------------------|
| 删除目录（含子目录） | `rmdir /s /q "路径"` | `Remove-Item "路径" -Recurse -Force` |
| 删除目录后重建 | `rmdir /s /q "路径" && mkdir "路径"` | — |
| 删除文件（通配符） | `del /q "路径\*.*"` | `Remove-Item "路径\*" -Force` |
| 复制目录（镜像） | `robocopy "源" "目标" /MIR /R:0` | — |
| **建立 Junction 链接** | `mklink /J "链接名" "目标路径"` | ❌ **不支持**（需 `cmd /c mklink /J ...`） |
| 查看 Junction | `dir /al` | `Get-ChildItem -Attributes ReparsePoint` |
| 磁盘清理 | `cleanmgr /sagerun:1` | — |
| 休眠管理 | `powercfg /h off` | `powercfg /h off` |
| WinSxS 清理 | `dism /online /Cleanup-Image /StartComponentCleanup` | 同 CMD |

> ⚠️ **关键区别**：
> - `mklink` 是 **CMD 内置命令**，PowerShell 中无法直接执行
> - 在 PowerShell 中使用 `%变量%` 时，环境变量**不会自动展开**，会变成字面量（如 `%LOCALAPPDATA%` 不会被替换为实际路径）
> - **所有 Junction 操作必须在 CMD 管理员中执行**
> - `rm -rf` 是 Linux/Git Bash 命令，在 Windows CMD/PowerShell 中**不生效**！

## 附录 C：快速扫描命令（免安装工具）

```powershell
# PowerShell：按大小排序显示 C 盘一级文件夹
Get-ChildItem C:\ -Directory -ErrorAction SilentlyContinue |
    ForEach-Object {
        $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue |
                  Measure-Object -Property Length -Sum).Sum / 1GB
        [PSCustomObject]@{ 路径=$_.FullName; 大小GB=[math]::Round($size, 1) }
    } | Sort-Object 大小GB -Descending | Format-Table -AutoSize

# 查看当前 C 盘剩余空间（GB）
Get-PSDrive C | Select-Object Used, Free |
    ForEach-Object { "已用: $([math]::Round($_.Used/1GB,1)) GB | 剩余: $([math]::Round($_.Free/1GB,1)) GB" }
```

```cmd
:: CMD：查看 C 盘剩余空间
wmic logicaldisk where "DeviceID='C:'" get Size,FreeSpace
```

---

## 附录 D：robocopy 返回码速查

| 返回码 | 含义 | 是否正常 |
|--------|------|----------|
| 0 | 无文件被复制 | ✅ 正常 |
| 1 | 有文件被复制 | ✅ 正常 |
| 2 | 有多余文件（目标有而源没有，/MIR 已删除） | ✅ 正常 |
| 3 | 1+2 同时发生 | ✅ 正常 |
| 4 | 有不匹配的文件（未复制完） | ⚠️ 检查 |
| 8 | 部分文件复制失败 | ❌ 异常——检查权限 |

> 💡 检查返回码：`echo %errorlevel%`（CMD）或 `$LASTEXITCODE`（PowerShell）
