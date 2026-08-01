---
title: "Apache Cassandra 高可扩展分布式数据库"
tags: [GitHub, 开源, 数据库, 分布式, NoSQL, Java]
type: 工具
status: 待评估
created: 2026-07-28
updated: 2026-07-28
verified: 2026-07-28
review_after: 2027-01-28
source: https://github.com/apache/cassandra
related: [Github优质项目-MOC]
summary: "9.9k⭐ · 今日新增34⭐——Apache Cassandra 是面向高可用与线性扩展的分布式宽列数据库，可跨多节点自动分区并避免单点故障"
---

# Apache Cassandra 高可扩展分布式数据库

## 项目定位

Apache Cassandra 是分区式宽列存储，数据按必须包含主键的表组织，可在增加或移除节点时自动重新分区。

## 适用场景

- 写入规模大、需要水平扩展的业务。
- 跨节点或跨数据中心容错。
- 能围绕查询模式提前设计分区键和数据模型的系统。

## 注意事项

- Cassandra 不适合直接照搬关系数据库的数据建模方式。
- 分区键、复制因子、一致性级别、压缩和修复策略会直接影响稳定性。
- 引入前应验证查询模式、热点分区、容量和运维复杂度。

**许可证：** Apache-2.0  
**推荐程度：** ★★★★☆  

## 相关导航

- [[Github优质项目-MOC]]
