---
title: Bat脚本详解
domain: IT_Technology
tags:
  - Bat
  - 批处理
  - 自动化
  - Windows
status: 稳定
created: 2026-05-27
updated: 2026-05-27
source: "博客园-秋落雨微凉"
related: []
summary: "Bat批处理是Windows原生脚本语言，通过变量/条件/循环/函数实现自动化，配合重定向、管道和组合命令，可快速构建系统配置、文件处理和部署脚本"
---

# Bat脚本详解

> **总结**：Bat（批处理）是 Windows 原生脚本语言，以 `.bat` 为后缀、双击即可执行。它基于 CMD 命令，核心语法包括 `set` 变量、`if` 条件、`for` 循环、`call` 函数调用，配合重定向（`>`/`>>`）、管道（`|`）和组合命令（`&&`/`||`），能快速构建轻量级自动化任务。短板是字符串处理和算术能力弱，复杂逻辑建议改用 PowerShell 或 Python。

---

## 一、脚本介绍

### 脚本通用优势
- 语言简单易学，可快速掌握
- 任何文本编辑器都能创建和修改
- 一次书写、多次执行，避免重复劳动
- 可封装为双击执行的自动化工具

### Bat 脚本特点
- 全称 Batch 脚本（批处理文件），Windows 默认支持
- 以 `.bat`（或 `.cmd`）结尾，双击即运行
- 本质是对 CMD 命令的顺序编排

### 最简示例
```batch
@echo off
set name=123
echo %name%
pause
```

---

## 二、基本语法

### 2.1 注释：`@` / `REM` / `::`
| 方式    | 作用     | 说明                            |
| ----- | ------ | ----------------------------- |
| `@`   | 隐藏本行回显 | 仍会执行，仅不显示命令行本身                |
| `REM` | 注释     | 不显示不执行；在 `@echo on` 时会回显      |
| `::`  | 注释     | `:` 后跟任意符号均可作为标签，惯用 `::` 表示注释 |

> **注意**：`::` 在 `for` 循环的 `()` 块内会导致语法错误，块内注释请用 `REM`。

### 2.2 输出：`echo`
| 用法 | 说明 |
|------|------|
| `echo text` | 直接输出文本 |
| `echo.` | 输出空行（换行） |
| `echo text > file` | 覆盖写入文件 |
| `echo text >> file` | 追加写入文件 |
| `echo on/off` | 控制命令回显的开关 |
| `@echo off` | 关闭回显且本行也不显示（惯用作脚本首行） |

### 2.3 暂停：`pause`
暂停脚本，显示"请按任意键继续..."，常用于查看中间结果或等待用户确认。

### 2.4 窗口标题：`title`
```batch
title 这是窗口标题
```

### 2.5 清屏：`cls`
清除当前控制台所有输出。

### 2.6 颜色：`color`
```batch
color 0A          REM 黑色背景 + 亮绿色文字
color             REM 恢复默认颜色
```
颜色代码为两位十六进制：**第一位背景，第二位前景**。

| 代码 | 颜色 | 代码 | 颜色 |
|------|------|------|------|
| 0 | 黑 | 8 | 灰 |
| 1 | 深蓝 | 9 | 亮蓝 |
| 2 | 深绿 | A | 亮绿 |
| 3 | 淡蓝 | B | 淡青 |
| 4 | 深红 | C | 亮红 |
| 5 | 紫色 | D | 淡紫 |
| 6 | 深黄 | E | 淡黄 |
| 7 | 白 | F | 亮白 |

---

## 三、变量系统

### 3.1 定义与取值：`set`
```batch
set name=value              REM 定义变量（等号前后不能有空格）
echo %name%                 REM 用 %% 取值

set /P name=请输入:          REM 交互式输入（/P = Prompt）
echo 你输入的是: %name%

set /A result=5+3           REM 算术运算（/A = Arithmetic）
echo %result%               REM 输出 8
```

### 3.2 变量作用域与延迟扩展
Bat 默认在**解析时**展开 `%var%`，循环体内变量不会实时更新。需要 `setlocal enabledelayedexpansion` + `!var!` 语法：
```batch
@echo off
setlocal enabledelayedexpansion
set count=0
for /l %%i in (1,1,5) do (
    set /A count=!count!+1
    echo !count!            REM 使用 ! 实时展开，输出 1 2 3 4 5
)
REM 如果用 %count%，循环内永远显示展开时的值（0）
```

### 3.3 字符串操作
```batch
set str=HelloWorld

REM 截取子串：%变量:~起始,长度%
echo %str:~0,5%             REM Hello
echo %str:~5%               REM World（省略长度 = 取到末尾）
echo %str:~-5%              REM World（负数 = 从末尾倒数）

REM 替换子串：%变量:旧=新%
echo %str:World=China%      REM HelloChina

REM 删除子串：替换为空
echo %str:Hello=%            REM World

REM 获取长度（间接法：利用字符偏移）
```

### 3.4 算术运算：`set /A`
```batch
set /A a=10+5               REM 加法: 15
set /A b=10-5               REM 减法: 5
set /A c=10*5               REM 乘法: 50
set /A d=10/3               REM 除法(取整): 3
set /A e=10%%3              REM 取模: 1（%% 是转义后的 %）
set /A f=(2+3)*4            REM 支持括号: 20
set /A g+=1                 REM 自增（g 需先定义）
```

### 3.5 常用系统变量
| 变量 | 含义 |
|------|------|
| `%CD%` | 当前工作目录 |
| `%DATE%` | 当前日期 |
| `%TIME%` | 当前时间 |
| `%RANDOM%` | 0~32767 随机整数 |
| `%ERRORLEVEL%` | 上一命令退出码（0=成功） |
| `%USERNAME%` | 当前登录用户名 |
| `%COMPUTERNAME%` | 计算机名称 |
| `%USERPROFILE%` | 用户主目录（如 `C:\Users\h2967`） |
| `%APPDATA%` | 应用数据目录 |
| `%TEMP%` | 临时文件目录 |
| `%PATH%` | 系统 PATH 环境变量 |
| `%OS%` | 操作系统名称 |

### 3.6 命令行参数
```batch
REM script.bat arg1 arg2 arg3
echo %0          REM 脚本自身名称
echo %1          REM 第1个参数
echo %2          REM 第2个参数
echo %*          REM 所有参数（空格分隔）

REM 参数修饰符（非常实用）
echo %~dp0       REM 脚本所在目录的完整路径（末尾带 \）
echo %~nx0       REM 脚本文件名 + 扩展名
echo %~fs0       REM 完整短路径（8.3 格式）
echo %~f1        REM 第1个参数的完整路径
echo %~n1        REM 第1个参数的文件名（无扩展名）
echo %~x1        REM 第1个参数的扩展名
```

---

## 四、流程控制

### 4.1 条件判断：`if`
```batch
REM 字符串比较（/I = 忽略大小写）
if "hello"=="hello" echo 相等
if /I "ABC"=="abc" echo 忽略大小写比较相等

REM 数值比较（需要 == 和数值本身）
set /A n=10
if %n%==10 echo n等于10
if %n% GEQ 5 echo n大于等于5

REM 比较运算符：EQU(等于) NEQ(不等) LSS(小于) LEQ(小于等于) GTR(大于) GEQ(大于等于)

REM 文件/目录存在判断
if exist "C:\test.txt" echo 文件存在
if not exist "C:\test.txt" echo 文件不存在

REM 变量是否已定义
if defined name echo name 已定义

REM 错误级别判断
some_command
if errorlevel 1 echo 命令失败（errorlevel >= 1）
if not errorlevel 1 echo 命令成功（errorlevel < 1）
REM 注意：if errorlevel N 是 >= N 而非 == N
REM 精确判断：if %ERRORLEVEL% EQU 0
```

### 4.2 选择菜单：`choice`
```batch
@echo off
choice /C YNC /M "是否继续 (Y=是, N=否, C=取消)"
REM %ERRORLEVEL% 返回用户选择的索引：1=Y, 2=N, 3=C
if errorlevel 3 goto cancel
if errorlevel 2 goto nope
if errorlevel 1 goto yes

choice /C 123 /N /T 5 /D 1 /M "请选择 (默认选1，5秒后自动确认)"
REM /N = 隐藏选项列表 /T 5 = 5秒超时 /D 1 = 默认选第1项
```

### 4.3 跳转：`goto` 与标签
```batch
@echo off
echo 开始处理...
goto skip_this

echo 这行不会执行

:skip_this
echo 跳过了中间内容
goto:eof          REM 等价于 exit /b 0，结束当前脚本
```

### 4.4 函数（子程序）：`call :label`
```batch
@echo off
call :greet "张三"              REM 调用函数并传参
call :greet "李四"
goto:eof                        REM 主流程结束

:greet
echo 你好，%~1                  REM 函数内 %1 为传入的第一个参数
goto:eof                        REM 返回调用处
```

> **关键约定**：函数名以 `:` 开头；用 `call :name args` 调用；函数末尾必须 `goto:eof`；函数内 `%1`~`%9` 访问参数。

### 4.5 带返回值的函数
```batch
@echo off
call :add 3 5
echo 结果: %result%
goto:eof

:add
set /A result=%~1+%~2
goto:eof
```

### 4.6 循环：`for` 完整参考

**基本格式**：`FOR %%var IN (set) DO command`

| 参数 | 用途 | 示例 |
|------|------|------|
| 无 | 遍历空格/逗号分隔的列表 | `for %%i in (a,b,c) do echo %%i` |
| `/D` | 遍历指定目录下的**子目录** | `for /d %%i in (*) do echo %%i` |
| `/R` | 递归遍历目录树 | `for /r . %%i in (*.txt) do echo %%i` |
| `/L` | 数字序列 `(start,step,end)` | `for /l %%i in (1,2,10) do echo %%i` |
| `/F` | 文件解析 / 命令输出 / 字符串处理 | 见下方详表 |

```batch
REM /D：遍历当前目录下所有子文件夹
for /d %%i in (*) do echo %%i

REM /L：1~10 每隔 2 输出 → 1 3 5 7 9
for /l %%i in (1,2,10) do echo %%i

REM /R：递归查找所有 .txt
for /r %%i in (*.txt) do echo %%i
```

#### `for /F` 详解（最强大的模式）

| 选项 | 含义 | 示例 |
|------|------|------|
| `delims=` | 列分隔符（默认空格/Tab） | `delims=,` |
| `tokens=` | 取第几列 | `tokens=1,3` 或 `tokens=1-3` |
| `skip=N` | 跳过前 N 行 | `skip=1` 跳过标题行 |
| `eol=` | 行注释符（默认 `;`） | `eol=#` 跳过 `#` 开头的行 |
| `usebackq` | 允许用反引号执行命令 | `('command')` |

```batch
REM 解析文件（默认以空格/Tab分割，只取第1列）
for /f %%i in (data.txt) do echo %%i

REM 跳过首行，取第1和第3列
for /f "skip=1 tokens=1,3" %%a in (data.csv) do echo %%a -- %%c

REM 指定逗号为分隔符，取第1~3列
for /f "tokens=1-3 delims=," %%a in (data.csv) do echo %%a %%b %%c

REM 执行命令并解析输出（使用 usebackq + 反引号）
for /f "usebackq tokens=*" %%i in (dir /b *.txt) do echo %%i

REM tokens=* 表示整行不分割
for /f "tokens=*" %%i in (data.txt) do echo %%i
```

---

## 五、符号系统

### 5.1 常用符号速查表
| 符号 | 名称 | 说明 |
|------|------|------|
| `@` | 回显屏蔽 | 隐藏当前行命令回显 |
| `%...%` | 变量取值 | `%name%`；`%0` 为脚本名，`%1` 为第1个参数 |
| `>` | 覆盖重定向 | `echo text > file.txt` |
| `>>` | 追加重定向 | `echo text >> file.txt` |
| `<` | 输入重定向 | `sort < data.txt` |
| \| | 管道 | dir \| findstr ".txt" |
| `^` | 转义符 | `^>` 表示字面 `>`；行末 `^` 为续行符 |
| `&` | 无条件连执行 | `cmd1 & cmd2`，忽略 cmd1 成败 |
| `&&` | 成功连执行 | `cmd1 && cmd2`，仅 cmd1 成功时执行 cmd2 |
| \|\| | 失败连执行 | cmd1 \|\| cmd2，仅 cmd1 失败时执行 cmd2 |
| `""` | 双引号 | 包裹含空格的路径；字符串比较必须加引号 |
| `2>` | 错误重定向 | `command 2> err.log` 将 stderr 写入文件 |
| `2>&1` | 合并输出 | `command > log.txt 2>&1` stdout 和 stderr 全写入 log |
| `nul` | 空设备 | `command > nul 2>&1` 静默执行，无任何输出 |

### 5.2 典型组合用法
```batch
REM 静默执行（丢弃所有输出）
tasklist | findstr "notepad" > nul 2>&1
if %ERRORLEVEL%==0 echo 记事本正在运行

REM 仅捕获错误
some_command 2> error.log

REM 命令成功才继续
ping -n 1 127.0.0.1 > nul && echo 网络正常 || echo 网络异常

REM 多行续写
echo 这是一段很长的文本 ^
可以跨行书写 ^
非常方便
```

---

## 六、常用外部命令在脚本中的应用

| 命令 | 场景 | 示例 |
|------|------|------|
| `findstr` | 文本搜索/过滤 | `findstr /I "error" log.txt` |
| `reg` | 注册表读写 | `reg query HKCU\...` / `reg add` / `reg delete` |
| `schtasks` | 计划任务 | `schtasks /create /tn "备份" /tr "backup.bat" /sc daily` |
| `net` | 服务/用户管理 | `net start 服务名` / `net stop 服务名` |
| `sc` | 服务配置 | `sc query 服务名` / `sc config` |
| tasklist | 进程查询 | tasklist \| findstr "java" |
| `taskkill` | 终止进程 | `taskkill /F /IM notepad.exe` |
| `ping` | 连通性检测 | `ping -n 1 192.168.1.1 > nul` |
| `shutdown` | 关机/重启 | `shutdown /r /t 60`（60秒后重启） |
| `wmic` | 系统信息 | `wmic os get LastBootUpTime` |
| `robocopy` | 高级文件复制 | `robocopy 源 目标 /MIR /Z`（镜像同步） |
| `compact` | 文件压缩 | `compact /C 文件`（NTFS 压缩） |

---

## 七、错误处理与健壮性

```batch
@echo off
setlocal enabledelayedexpansion

REM 定义日志函数
set LOGFILE=%~dp0\script.log
call :log "脚本启动"

REM 错误即退出（逐行检查 ERRORLEVEL）
copy "source.txt" "dest.txt"
if %ERRORLEVEL% NEQ 0 (
    call :log "复制失败，错误码: %ERRORLEVEL%"
    goto :error
)

REM 使用 || 简化
mkdir "backup" 2> nul || call :log "目录已存在，跳过创建"

call :log "脚本完成"
exit /b 0

:error
call :log "脚本异常终止"
pause
exit /b 1

:log
echo [%DATE% %TIME%] %~1 >> "%LOGFILE%"
goto:eof
```

---

## 八、中文编码处理

| 编码 | `chcp` 代码 | 说明 |
|------|--------------|------|
| **GBK (ANSI)** | `936` | 中文 Windows 默认，bat 文件用 ANSI 保存时正常工作 |
| **UTF-8** | `65001` | 若 bat 文件以 UTF-8 保存，脚本开头加 `chcp 65001 > nul` |
| **ASCII** | `437` | 英文默认 |

**推荐方案**：
- **简单脚本**：用 **ANSI/GBK** 编码保存 `.bat` 文件（记事本保存时选"ANSI"），无需额外处理
- **UTF-8 脚本**：文件保存为 UTF-8，脚本首行加 `chcp 65001 > nul`
- **终极方案**：如果中文乱码频繁，改用 **PowerShell**，天然 UTF-8 友好

```batch
REM ANSI 脚本（推荐，最省事）
@echo off
echo 中文正常显示

REM UTF-8 脚本（需要切换代码页）
@echo off
chcp 65001 > nul
echo 中文正常显示
```

---

## 九、数组模拟

Bat 无原生数组，两种模拟方式：

```batch
@echo off
setlocal enabledelayedexpansion

REM 方式1：下标伪数组（不可直接遍历，需配合 /L）
set arr[0]=apple
set arr[1]=banana
set arr[2]=cherry
for /l %%i in (0,1,2) do echo !arr[%%i]!

REM 方式2：空格分隔列表（for 直接遍历）
set fruits=apple banana cherry
for %%f in (%fruits%) do echo %%f
```

---

## 十、实战示例

### 10.1 文件批量重命名（加前缀）
```batch
@echo off
setlocal enabledelayedexpansion
set PREFIX=backup_
for %%f in (*.txt) do (
    ren "%%f" "%PREFIX%%%f"
    echo 已重命名: %%f → %PREFIX%%%f
)
echo 完成！& pause
```

### 10.2 服务状态监控脚本
```batch
@echo off
setlocal enabledelayedexpansion
set SERVICES=Spooler WSearch BITS
for %%s in (%SERVICES%) do (
    sc query %%s | findstr /I "RUNNING" > nul
    if !ERRORLEVEL!==0 (
        echo [OK   ] %%s 正在运行
    ) else (
        echo [STOP ] %%s 已停止，尝试启动...
        net start %%s
    )
)
pause
```

### 10.3 定时备份脚本
```batch
@echo off
setlocal enabledelayedexpansion

set SOURCE=C:\data
set BACKUP=D:\backup
set DATE=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
set TIME=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set TIME=%TIME: =0%
set DEST=%BACKUP%\data_%DATE%_%TIME%

if not exist "%BACKUP%" mkdir "%BACKUP%"

echo 正在备份 %SOURCE% → %DEST%
robocopy "%SOURCE%" "%DEST%" /E /Z /R:3 /W:5

if %ERRORLEVEL% LEQ 3 (
    echo [%DATE% %TIME%] 备份成功 >> "%BACKUP%\backup.log"
) else (
    echo [%DATE% %TIME%] 备份失败，错误码: %ERRORLEVEL% >> "%BACKUP%\backup.log"
)
pause
```

### 10.4 批量检测主机存活
```batch
@echo off
setlocal enabledelayedexpansion
set SUBNET=192.168.1

for /l %%i in (1,1,254) do (
    ping -n 1 -w 100 %SUBNET%.%%i > nul
    if !ERRORLEVEL!==0 (
        echo [LIVE] %SUBNET%.%%i
    )
)
echo 扫描完成！& pause
```

---

## 十一、Bat 的限制与替代建议

| 场景 | Bat 是否合适 | 替代方案 |
|------|-------------|---------|
| 简单文件操作 / 复制粘贴部署 | ✅ 合适 | — |
| 调用系统命令 / 启动服务 | ✅ 合适 | — |
| 复杂字符串处理 / JSON/XML 解析 | ❌ 吃力 | PowerShell |
| 网络 API 调用 | ❌ 不适合 | PowerShell / Python |
| 复杂业务逻辑 / 大量计算 | ❌ 不适合 | Python / Go |
| GUI 相关操作 | ❌ 不支持 | PowerShell + WPF / C# |

> **一句话**：Bat 擅长"把 CMD 命令串起来"，超出这个范围请果断换工具。
