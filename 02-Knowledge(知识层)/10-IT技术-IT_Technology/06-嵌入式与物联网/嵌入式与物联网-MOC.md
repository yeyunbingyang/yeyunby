---
title: 嵌入式与物联网 MOC
domain: IT_Technology
tags: [MOC, 嵌入式, 物联网, IoT]
status: 稳定
created: 2026-07-15
updated: 2026-07-15
summary: "嵌入式系统与物联网子域地图，涵盖嵌入式开发、物联网架构、网络协议与安全基础"
---

# 嵌入式与物联网

嵌入式系统和物联网（IoT）是连接物理世界与数字世界的桥梁。本域覆盖从底层嵌入式开发到上层物联网架构，以及与之紧密相关的网络通信与安全基础。

> 本 MOC 合并了原「网络与安全」子域内容——嵌入式与物联网天然涉及网络通信与设备安全，故在此统一管理。

## 学习路径

`嵌入式基础（MCU/RTOS）` → `物联网通信协议` → `网络协议栈（TCP/IP）` → `设备安全与防护`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| TCP 三次握手 | 建立可靠连接的状态机协商过程（SYN/SYN-ACK/ACK） |
| TLS 握手 | HTTPS 会话密钥协商与证书验证流程 |
| NAT | 网络地址转换，私有 IP 复用公网 IP 的机制 |
| VLAN | 逻辑隔离同物理网络的广播域 |
| OWASP Top 10 | Web 应用最常见的 10 类安全漏洞分类 |
| 零信任 | 默认不信任任何内部网络，持续验证身份与权限 |

## 关键知识点

### 嵌入式基础
- MCU 与 SoC 选型（STM32 / ESP32 / ARM）
- RTOS（FreeRTOS / Zephyr）
- 外设驱动（GPIO / I2C / SPI / UART）
- 低功耗设计

### 物联网架构
- IoT 分层架构（感知层 / 网络层 / 平台层 / 应用层）
- MQTT / CoAP / LwM2M 协议
- 边缘计算与云边协同
- 设备管理（OTA / 远程配置）

### 网络协议
- **OSI 七层模型** vs TCP/IP 四层模型对应关系
- **IP 寻址**：子网划分（CIDR）、路由表、ARP
- **TCP vs UDP**：可靠传输机制、拥塞控制、适用场景
- **HTTP/2 vs HTTP/3**：多路复用、QUIC 协议

### HTTPS 与 TLS
- 证书链验证（CA/中间证书/叶证书）
- TLS 1.3 握手简化流程
- HSTS / Certificate Pinning
- 常见 TLS 攻击（降级/重放/中间人）

### DNS
- 解析流程（递归/迭代查询）
- DNS 记录类型（A/CNAME/MX/TXT）
- DNS over HTTPS（DoH）
- DNS 劫持与防护

### 防火墙与访问控制
- iptables/nftables 规则链
- 安全组 vs NACL（云环境）
- VPN（IPSec/WireGuard/OpenVPN）
- WAF 原理与绕过思路

### 安全攻防基础
- OWASP Top 10（SQL注入/XSS/SSRF/IDOR等）
- 渗透测试方法论（侦察/扫描/利用/后渗透）
- 常用工具：nmap/burpsuite/metasploit 基础
- 日志审计与 SIEM

### IoT 安全
- 设备身份认证与安全启动
- 固件加密与防篡改
- 通信加密（TLS / DTLS）
- 固件更新安全（签名验证 / 回滚保护）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/06-嵌入式与物联网"
WHERE file.name != "嵌入式与物联网-MOC" AND file.name != "网络安全-MOC"
SORT updated DESC
```
