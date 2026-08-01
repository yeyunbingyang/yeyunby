---
title: "Kronos 金融 K 线基础模型"
tags: [GitHub, 开源, AI, 金融, 时间序列, Transformer]
type: 模型
status: 待评估
created: 2026-07-28
updated: 2026-07-28
verified: 2026-07-28
review_after: 2026-10-28
source: https://github.com/shiyu-coder/Kronos
related: [Github优质项目-MOC]
summary: "34.5k⭐ · 今日新增442⭐——Kronos 将 OHLCV K线量化为分层离散Token，再用自回归Transformer统一处理金融市场预测与量化任务"
---

# Kronos 金融 K 线基础模型

## 项目定位

Kronos 是针对金融 K 线序列预训练的 decoder-only 基础模型，官方称训练数据覆盖 45 个以上全球交易所。

## 技术路线

1. 专用 Tokenizer 将连续、多维 OHLCV 数据量化为分层离散 Token。
2. 自回归 Transformer 在 Token 序列上预训练，用于预测及其他量化任务。

开源模型包括 4.1M 参数的 mini、24.7M 的 small 和 102.3M 的 base；499.2M 的 large 在官方表格中未开放权重。

## 注意事项

- 模型输出不构成投资建议，应进行独立回测、样本外验证和风险控制。
- 金融时序存在分布漂移、幸存者偏差和交易成本等现实约束。
- 不应以演示中的 BTC/USDT 预测替代真实策略评估。

**许可证：** MIT  
**推荐程度：** ★★★★☆  

## 相关导航

- [[Github优质项目-MOC]]
