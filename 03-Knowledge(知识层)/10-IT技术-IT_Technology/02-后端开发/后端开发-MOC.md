---
title: 后端开发 MOC
domain: IT_Technology
tags: [MOC, 后端, 数据库, API]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "后端开发子域地图，覆盖编程语言、框架、数据库、消息队列与系统设计"
---

# 后端开发

服务端软件工程的核心知识域，从语言基础到分布式系统设计，关注性能、可靠性与可扩展性。

## 学习路径

`语言基础` → `框架与 API 设计` → `数据库与缓存` → `消息队列` → `系统设计与高并发`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| RESTful API | 基于 HTTP 动词的无状态接口设计规范 |
| ORM | 对象-关系映射，将代码对象映射到数据库表 |
| 缓存穿透/击穿/雪崩 | 缓存层三类典型故障模式及防护策略 |
| 幂等性 | 相同请求执行多次结果相同，接口容错设计基础 |
| 分布式事务 | 跨服务/库的数据一致性问题（Saga/TCC/2PC） |

## 关键知识点

### 编程语言
- **Python**：异步（asyncio/aiohttp）、类型注解、GIL 限制
- **Go**：goroutine/channel 并发模型、interface 设计、内存逃逸
- **Java**：JVM 调优、Spring 生态、泛型与反射

### 框架与 API 设计
- FastAPI / Flask（Python）
- Gin / Echo（Go）
- Spring Boot（Java）
- gRPC vs REST vs GraphQL 选型
- OpenAPI 文档规范

### 数据库
- **关系型**：MySQL 索引原理（B+树）、事务（ACID/隔离级别）、慢查询优化
- **NoSQL**：Redis 数据结构与持久化、MongoDB 文档模型
- **搜索**：Elasticsearch 倒排索引与全文检索

### 消息队列
- Kafka：分区/副本/消费者组/Offset 管理
- RabbitMQ：Exchange 类型与路由
- 消息可靠性：At-least-once vs Exactly-once

### 系统设计
- 限流（令牌桶/漏桶）、熔断（Circuit Breaker）
- 分布式锁（Redis/Zookeeper）
- 微服务拆分原则与服务治理
- 读写分离与分库分表

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/02-后端开发"
WHERE file.name != "后端开发-MOC"
SORT updated DESC
```
