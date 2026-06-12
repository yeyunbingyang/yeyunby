---
title: "RuView WiFi空间智能感知"
tags: [GitHub, 开源, IoT, WiFi, 空间智能, 健康监测, HomeAssistant, 物理AI]
type: 工具
status: 待评估
created: 2026-05-26
updated: 2026-05-26
source: https://github.com/ruvnet/RuView
related: []
summary: "将普通WiFi信号转化为空间智能——隔墙感知人体存在/呼吸/心率/跌倒，$9 ESP32节点+边缘AI，零摄像头零穿戴，66.1k Stars"
---

# RuView WiFi空间智能感知

https://github.com/ruvnet/RuView

## 基本信息

**类型：** 工具（边缘传感平台）
**链接：** https://github.com/ruvnet/RuView
**主页：** https://Cognitum.One/RuView
**适用领域：** 智能家居、老人监护、空间智能、无接触健康监测、物理 AI
**推荐程度：** ★★★★★
**Stars：** ~66.1k | Fork 8.8k
**语言：** Rust
**许可证：** MIT
**硬件成本：** ESP32 节点 ~$9/个

## 是什么

RuView 把普通 WiFi 信号变成**空间智能感知系统**——用 $9 的 ESP32 芯片捕获 WiFi 信号在人体上的反射（CSI），通过脉冲神经网络分析，实现：

- 🧑 隔墙探测人体存在、计数、出入追踪
- 🫁 无接触测量呼吸率和心率
- 🏃 行为识别：行走、坐下、手势、跌倒
- 😴 睡眠质量监测（分期+呼吸暂停筛查）
- 📡 房间 RF 指纹识别（检测家具移动、异物入侵）

**零摄像头、零穿戴设备、零云端**——纯物理信号，隐私天然保护。

## 快速开始

```bash
git clone https://github.com/ruvnet/RuView
# 硬件：ESP32-S2/S3 + Cognitum Seed（或 Raspberry Pi）
# 接入 Home Assistant：一个 --mqtt 参数即可
```

集成：Home Assistant · Apple Home · Google Home · Alexa · Matter Bridge

## 核心功能

### 感知能力

| 维度 | 能力 | 说明 |
|------|------|------|
| 存在检测 | 隔墙探测、人数统计、出入追踪 | 100% 存在检测准确率（验证集） |
| 生命体征 | 呼吸率、心率 | 无接触，睡觉/坐着均可 |
| 行为识别 | 行走、坐下、手势、跌倒 | 时序 CSI 模式识别 |
| 睡眠监测 | 睡眠分期+呼吸暂停筛查 | 整夜监测 |
| 环境感知 | 房间指纹、家具变动、异物检测 | RF 指纹比对 |

### 10 个语义状态（每节点 21 个 HA 实体）

有人睡觉 · 可能异常 · 房间活跃 · 老人久坐异常 · 会议中 · 卫生间占用 · 跌倒风险 · 离床 · 无移动 · 多房间穿行

### 技术架构

```
ESP32-S2/S3 节点 ($9)
    ↓ CSI 子载波采集（6 WiFi 信道 × 多节点 Mesh）
Cognitum Seed（边缘计算 + Ed25519 加密认证）
    ↓ 脉冲神经网络（30 秒自适应学习）
WiFi DensePose 模型（8KB，4-bit 量化）
    ↓
Home Assistant / Apple Home / Google Home / MCP Server
```

### Agent 集成

- **rvagent MCP Server**：6 个感知工具 + 5 个治理工具
  - `ruview.presence.now` — 当前存在状态
  - `ruview.vitals.get_breathing` / `get_heart_rate` / `get_all` — 生命体征
  - `ruview.bfld.last_scan` / `subscribe` — 空间扫描
- **Claude Code / Codex Plugin**：`/ruview-*` 命令
- `npx @ruvnet/rvagent stdio` 一键启动

## 适用场景

- 智能家居——替代摄像头和 PIR 传感器，隐私友好
- 老人监护——跌倒检测、生命体征异常告警、久坐预警
- 睡眠健康——无接触整夜监测
- 办公空间——会议室占用、工位使用率
- 物理 AI Agent——让 Agent 感知物理世界的人和空间

## 评价

- **优点**：WiFi→空间智能思路极其创新、$9 硬件门槛极低、零摄像头隐私天然保护、Home Assistant 深度集成、脉冲神经网络边缘运行无云端依赖、MCP Server 让 AI Agent 可直接感知物理世界、66k Stars 社区火爆
- **局限**：ESP32-C3/原版 ESP32 不支持（需 S2/S3）、单节点空间分辨率有限（建议 2+ 节点）、摄像头级姿态估计精度有限（PCK@20 ≈ 2.5%，正在改进中）
- **是否值得长期保留**：✅ 重点关注——物理 AI 赛道的现象级项目，MCP 桥接让 AI Agent 首次能「感知」物理空间
