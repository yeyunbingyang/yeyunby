---
title: 快速在当前目录打开PowerShell
domain: Core_Ability
tags: [Windows, PowerShell, 效率技巧]
status: 稳定
created: 2026-05-25
updated: 2026-05-25
source: ""
related: [[Windows使用-MOC]]
summary: "四种方法在文件资源管理器当前目录快速启动PowerShell，地址栏直接输入最快且全版本通用"
---

# 快速在当前目录打开 PowerShell

在文件资源管理器中，从当前路径直接打开 PowerShell 终端，省去手动 `cd` 的麻烦。

## 方法一：地址栏直接启动（最快，全版本通用）

1. 在文件资源管理器中，按 `Alt + D` 聚焦地址栏
2. 输入 `powershell`（或 `pwsh` 如果你装了 PowerShell 7+）
3. 按 `Enter`，即在该目录打开

## 方法二：Shift + 右键菜单

- **Windows 10**：按住 `Shift` 在文件夹空白处右键 → 选择「在此处打开 PowerShell 窗口」
- **Windows 11**：默认右键菜单显示「在终端中打开」（可在终端设置里把默认配置文件改为 PowerShell）

## 方法三：注册表恢复经典右键（Win11 专用）

Win11 右键菜单被折叠时，运行以下命令恢复经典菜单（含 PowerShell 选项）：

```powershell
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

重启资源管理器或电脑后生效。

## 方法四：快捷键组合

- `Win + X` → 按 `I` 打开 Windows PowerShell
- `Win + X` → 按 `A` 以管理员身份打开

> **提示**：如果你主要使用 PowerShell 7（PowerShell Core），建议安装 Windows Terminal 并将其设为默认终端，这样所有「在终端中打开」都会自动使用 PowerShell 7。
