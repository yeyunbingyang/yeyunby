---
title: "bitchat 蓝牙 Mesh 去中心化聊天"
tags: [GitHub, 开源, 通信, 蓝牙, Mesh, 隐私]
type: 工具
status: 待评估
created: 2026-07-28
updated: 2026-07-28
verified: 2026-07-28
review_after: 2026-10-28
source: https://github.com/permissionlesstech/bitchat
related: [Github优质项目-MOC]
summary: "31.9k⭐ · 今日新增2344⭐——bitchat 以蓝牙低功耗 Mesh 支持离线多跳聊天，并以 Nostr 中继扩展互联网通信，无需账号或手机号"
---

# bitchat 蓝牙 Mesh 去中心化聊天

## 项目定位

bitchat 是面向 iOS 与 macOS 的去中心化通信应用，本地优先使用 Bluetooth LE Mesh，在无法联网时通过附近设备多跳转发；有网络时可切换到 Nostr 中继。

## 核心特点

- 无需账号、手机号和中心服务器。
- 蓝牙 Mesh 最多支持 7 跳转发，适合灾害、偏远地区和临时现场。
- 私聊使用 Noise Protocol 或项目自定义的 Nostr 私密信封加密。
- 支持基于 geohash 的位置频道、IRC 风格命令和紧急数据清除。

## 注意事项

- “去中心化”不代表没有元数据泄露，附近设备仍可能观察无线标识与通信行为。
- Nostr 私密信封是 bitchat 自有格式，不与 NIP-17、NIP-44 或 NIP-59 互操作。
- 安装包应来自 App Store 或可验证源码，避免使用无法核验的镜像构建。

**许可证：** Unlicense  
**推荐程度：** ★★★★☆  

## 相关导航

- [[Github优质项目-MOC]]
