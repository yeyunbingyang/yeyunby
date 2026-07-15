---
title: 逆向工程 MOC
domain: IT_Technology
tags: [MOC, 逆向, 安全, 二进制]
status: 计划
created: 2026-07-15
updated: 2026-07-15
summary: "逆向工程子域骨架，覆盖二进制分析、反汇编、调试、协议逆向与安全研究基础"
---

# 逆向工程

> 🚧 **骨架 — 待建设**

逆向工程是通过分析软件/硬件的运行结果或二进制产物，推导其实现原理与技术细节的过程。核心应用包括：漏洞挖掘、恶意软件分析、竞品研究、兼容性实现。

## 规划内容

### 基础
- 可执行文件格式（PE / ELF / Mach-O）
- 汇编基础（x86/x64 / ARM）
- 静态分析（IDA Pro / Ghidra / radare2）
- 动态调试（x64dbg / GDB / Windbg）

### 进阶
- 反混淆与脱壳
- 协议逆向
- 固件逆向
- 移动端逆向（Android / iOS）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/07-逆向"
WHERE file.name != "逆向工程-MOC"
SORT updated DESC
```
