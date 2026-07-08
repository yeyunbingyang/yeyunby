---
title: 网络与安全 MOC
domain: IT_Technology
tags: [MOC, 网络, 安全, 协议]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "网络与安全子域地图，覆盖网络协���栈、HTTP/TLS、防火墙策略与安全攻防基础"
---

# 网络与安全

计算机网络的工作原理与安全防护体系，从协议底层到渗透测试思维，核心是"理解攻击才能做好防御"。

## 学习路径

`网络协议栈（OSI/TCP-IP）` → `HTTP/HTTPS 与 TLS` → `DNS 与路由` → `防火墙与访问控制` → `安全攻防基础`

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

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "02-Knowledge(知识层)/10-IT技术-IT_Technology/04-网络与安全"
WHERE file.name != "网络安全-MOC"
SORT updated DESC
```
