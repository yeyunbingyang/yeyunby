---
title: 运维云原生 MOC
domain: IT_Technology
tags: [MOC, 运维, 云原生, DevOps]
status: 稳定
created: 2026-05-07
updated: 2026-05-11
summary: "运维云原生子域地图，覆盖 Linux 基础设施、数据库 DBA、中间件与高可用、自动化监控、容器云原生、交付自动化、大数据运维 7 大模块，合计约 60 篇笔记"
---

# 运维云原生

从裸机 Linux 到云原生容器编排的完整运维知识域，核心是"基础设施即代码"与"可观测性优先"。笔记以**任务驱动**方式组织，每篇从实际场景出发，包含背景、目标拆解和操作步骤。

## 模块总览

| 编号 | 模块 | 笔记数 | 核心内容 |
|------|------|--------|----------|
| 00 | 快速知识 | 2 | CentOS yum源更改、时间同步等常用速查 |
| 01 | Linux 基础设施 | ~30 | 系统管理、核心命令、网络、服务、Shell、项目实战 |
| 02 | 数据库运维 DBA | 5 | MySQL8 安装/管理/备份恢复/主从架构/高可用集群 |
| 03 | 中间件与高可用 | ~17 | Redis 缓存、Nginx 负载均衡、LVS/SLB、Keepalived |
| 04 | 自动化与监控 | ~10 | Prometheus、Zabbix、ELK、Ansible、Python 运维开发 |
| 05 | 容器与云原生 | ~9 | Docker 容器化、Kubernetes 编排、Containerd |
| 06 | 交付与自动化 | ~7 | Git/GitLab、Jenkins CI/CD、Pipeline 流水线 |
| 07 | 大数据运维 | 1 | 大数据概念、离线/实时开发方向、技术栈概览 |

## 学习路径

```
Linux 基础命令与服务管理
    ↓
Shell 脚本自动化
    ↓                        ← 至此可独立完成传统运维部署项目
MySQL 数据库运维
    ↓
Nginx + Redis + Keepalived   ← 中间件与高可用层
    ↓
Docker 容器化
    ↓
Kubernetes 编排              ← 云原生核心
    ↓
Jenkins CI/CD + Prometheus   ← 交付自动化 + 可观测性闭环
```

## 00 快速知识

日常运维常用配置速查，不归属特定学习路径，按需查阅。

- CentOS Stream yum源更改
- CentOS9 时间同步

## 01 Linux 基础设施（~30 篇）

### 01 运维基本导论与 Linux 系统部署

- Linux 云计算运维基本导论：运维六大职责、云计算三种服务模式（IaaS/PaaS/SaaS）
- 初始化网络配置
- 安装文档：CentOS Stream 9 / Ubuntu Server 安装与配置（PDF）

### 02 Linux 运维核心命令（7 篇）

- 系统说明（发行版与内核）
- 文件管理（ls/cp/mv/find/tar）
- 用户和组管理（useradd/passwd/sudo）
- 权限管理（chmod/chown/ACL/suid）
- 软件包管理（yum/dnf/rpm）
- 系统服务管理（systemd/systemctl）
- 系统性能监控（top/htop/free/iostat/netstat）

### 03 网络运维（2 篇）

- 网络基础：TCP/IP 协议栈、子网划分、路由基础
- 网络进阶：iptables 防火墙、tcpdump 抓包分析

### 04 系统服务运维（8 篇）

- SSH 服务（远程管理、密钥认证）
- Rsync 数据同步
- FTP 与磁盘挂载
- NFS/Samba 共享文件服务
- DNS 服务器
- RSYSLOG 日志管理
- 磁盘管理（LVM、分区、挂载）
- 时间同步与 Linux 深层防火墙（firewalld）

### 05 Shell 脚本编程（5 篇 + 练习）

- Shell 脚本编程基础（变量、运算符）
- Shell 流程结构（if/for/while/case）
- Shell 函数与正则表达式
- Shell 三剑客（grep/sed/awk）
- 实战：中州养老 Web 一键部署脚本
- 练习：grep + 正则日志分析 30 个实战案例
- 练习：Awk 实战应用 — 从日志分析到数据统计

### 06 项目（5 篇）

**项目一：AI 大模型项目上"云"部署**
- 基于云平台博客系统部署与监控运维实战（LAMP 架构）
- 基于 Ubuntu Server 部署开源 AI 大模型聊天机器人（非必选拓展）
- 拓展：LAMP + Discuz! 论坛搭建

**项目二：智慧养老系统脚本运维实战**
- JAVA 智慧养老单体项目部署
- JAVA 智慧养老单体项目部署上线（生产环境完整流程）

## 02 数据库运维 DBA — MySQL（5 篇）

以 MySQL 5.7 → 8.0 迁移为业务背景，覆盖安装到高可用全链路。

- MySQL8 安装与配置：CentOS Stream 9 上安装部署，Shell 脚本封装
- MySQL 数据服务管理：用户权限、字符集、日志管理
- MySQL 备份与恢复（重点）：mysqldump/Xtrabackup 全量+增量方案
- MySQL 主从架构设计（重点）：GTID 主从复制与延迟监控
- MySQL8 新特性与高可用集群架构：窗口函数、CTE、角色管理、MGR

## 03 中间件与高可用（~17 篇）

### Redis 缓存架构（4 篇）

- Redis7 缓存架构：数据类型、持久化 RDB/AOF、主从模式
- Redis5 缓存架构：旧版架构对比
- Redis 哨兵模式：Sentinel 自动故障转移
- Redis 集群模式：Cluster 分片与水平扩展

### Nginx 负载均衡 — 运维版（4 篇 + 5 细节）

- Nginx 单机部署：编译安装、基础配置
- Nginx 详解：虚拟主机、location 匹配规则
- 电商项目部署：前后端分离 + Nginx 代理实战
- Nginx 负载均衡：upstream、权重、健康检查、会话保持
- 细节补充：HTTPS 配置 / Keepalived 高可用 / 动静分离 / 前缀转发策略 / include 拆分配置

### Nginx — 全栈版（1 篇）

- 从开发视角覆盖 Nginx 全栈使用场景

### 负载均衡（2 篇）

- LVS 负载均衡：DR/NAT 模式原理与配置
- 阿里云 SLB：云平台负载均衡实践

### Tomcat 中间件

目录已建，内容待补充。

### 高可用（2 篇）

- Keepalived 高可用解决方案：VRRP 协议 + 浮动 IP
- MySQL 读写分离设计：ProxySQL/Atlas 中间件方案

## 04 自动化与监控（~10 篇）

### 监控

- **Prometheus 监控系统**（3 篇）：
  - Prometheus 监控系统：node_exporter + mysqld_exporter 数据采集
  - Prometheus 核心监控体系：PromQL 查询、告警规则、Alertmanager
  - Grafana 常用模板编号记录：常用 Dashboard ID 速查
- **Zabbix 监控系统**（1 篇）：传统行业监控方案，适用于物理机和传统架构

### 日志分析

- ELK 日志分析：Elasticsearch + Logstash + Kibana 统一日志平台搭建

### 自动化运维

- **Ansible 配置自动化**（1 篇）：多服务器批量管理，playbook 编排
- **Python 运维开发**（4 篇）：
  - Python 基础语法（运维向）
  - Python 文件操作与 Nginx 日志读取
  - Nginx 日志分类统计与分析
  - 系统资源监控与数据采集（重点）：CPU/内存/磁盘指标采集 + 告警接口对接

## 05 容器与云原生（~9 篇）

### Docker 容器化

- **运维版**（2 篇）：
  - Docker 基础命令及镜像构建：Dockerfile 多阶段构建
  - Docker 网络与 Docker Compose：bridge/host 模式、多服务编排
- **Java 版**（1 篇）：Linux 环境搭建（面向 Java 开发者的 Docker 前置）
- **软件清单**（1 篇）：MySQL 容器化部署参数参考
- **总结**（1 篇）：Docker 知识点汇总

### Kubernetes 编排

- Containerd 容器运行时：历史发展、与 Docker 关系、基本架构
- Kubernetes 集群安装部署
- Kubernetes 资源管理与 Pod 基础：Pod/Deployment/Service/ConfigMap
- Kubernetes 资源管理与 Pod 进阶：调度策略、存储卷、滚动更新

## 06 交付与自动化（~7 篇）

### Git 版本控制

- GIT 基础：分支策略、工作流
- gitlab 实践问题：常见故障处理

### GitHub 与 GitLab

- GitHub 与 GitLab 使用：远程仓库管理、协作流程

### Jenkins CI/CD

- Jenkins 快速入门：安装与基础配置
- Jenkins 详解：Job 配置、参数化构建
- Jenkins Pipeline 流水线：Declarative Pipeline 语法、多阶段构建
- 实践问题总结：常见 CI/CD 故障排查

## 07 大数据运维（1 篇）

- 大数据运维概述：大数据概念（海量存储+计算）、离线开发与实时开发两个方向、主流技术栈介绍（Hadoop/Spark/Flink）

---

## 核心概念速查

| 概念 | 一句话定义 | 所在模块 |
|------|-----------|----------|
| 进程与信号 | Linux 进程生命周期与 kill/systemd 管理 | 01 |
| Shell 三剑客 | grep 过滤 / sed 流编辑 / awk 文本处理 | 01 |
| MySQL 主从复制 | 基于 binlog 的数据同步，GTID 保证一致性 | 02 |
| Redis 持久化 | RDB 快照 + AOF 日志，平衡性能与安全 | 03 |
| 负载均衡 | upstream 调度算法分发流量到后端节点 | 03 |
| 高可用 | Keepalived VRRP 虚拟 IP 漂移实现故障转移 | 03 |
| Prometheus 三件套 | node_exporter 采集 → Prometheus 存储 → Grafana 展示 | 04 |
| 容器镜像 | Docker 分层文件系统与多阶段构建最佳实践 | 05 |
| Pod | K8s 最小调度单元，共享网络命名空间 | 05 |
| 声明式配置 | 描述期望状态而非操作步骤（YAML manifest） | 05 |
| CI/CD Pipeline | 代码提交 → 构建 → 测试 → 部署的自动化流水线 | 06 |

## 当前建设状态

| 模块            | 富集度    | 说明                                  |
| ------------- | ------ | ----------------------------------- |
| 01 Linux 基础设施 | ██████ | 内容完整，6 个子模块齐备，含项目实战                 |
| 02 数据库 DBA    | ████░  | MySQL 体系完整，待补充 PostgreSQL/MongoDB   |
| 03 中间件与高可用    | ████░  | Nginx/Redis/Keepalived 完善，Tomcat 待填 |
| 04 自动化与监控     | ███░░  | Prometheus 为核心，ELK 可深化              |
| 05 容器与云原生     | ████░  | Docker + K8s 基础完善，待补 Helm/Istio     |
| 06 交付与自动化     | ████░  | Jenkins 体系完整，待补 ArgoCD/GitOps       |
| 07 大数据运维      | █░░░░  | 仅概念概览，待建设                           |

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-运维云原生"
WHERE file.name != "运维云原生-MOC"
SORT updated DESC
```
