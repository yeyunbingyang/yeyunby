---
title: 运维云原生 MOC
domain: IT_Technology
tags: [MOC, 运维, 云原生, DevOps]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "运维云原生子域地图，覆盖 Linux 系统管理、容器化、Kubernetes、CI/CD 与监控体系"
---

# 运维云原生

从裸机 Linux 到云原生容器编排的完整运维知识域，核心是"基础设施即代码"与"可观测性优先"。

## 学习路径

`Linux 基础` → `Docker 容器化` → `Kubernetes 编排` → `CI/CD 自动化` → `监控告警体系`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| 进程与信号 | Linux 进程生命周期与 kill/systemd 管理 |
| 容器镜像 | Docker 分层文件系统与镜像构建最佳实践 |
| Pod | K8s 最小调度单元，共享网络命名空间 |
| 声明式配置 | 描述期望状态而非操作步骤（YAML manifest） |
| 服务发现 | Service/Ingress 实现容器间通信与外部路由 |
| 可观测性三支柱 | Metrics（指标）/ Logs（日志）/ Traces（链路追踪） |

## 关键知识点

### Linux 系统管理
- 文件系统与权限（chmod/chown/ACL）
- 进程管理（systemd/ps/htop/strace）
- 网络工具（ss/netstat/iptables/tcpdump）
- Shell 脚本自动化（Bash 变量/条件/循环）
- 性能调优（CPU/内存/IO/网络瓶颈分析）

### Docker 容器化
- 镜像构建（Dockerfile 多阶段构建）
- 容器网络（bridge/host/overlay 模式）
- 数据持久化（Volume/Bind Mount）
- Docker Compose 多服务编排
- 镜像安全扫描（Trivy/Snyk）

### Kubernetes 编排
- 核心资源（Pod/Deployment/Service/ConfigMap/Secret）
- 调度策略（nodeSelector/affinity/taint/toleration）
- 存储（PV/PVC/StorageClass）
- 网络（CNI/Ingress Controller/NetworkPolicy）
- 滚动更新与回滚策略

### CI/CD 流水线
- GitLab CI / GitHub Actions 流水线设计
- 构建缓存与镜像层优化
- 蓝绿部署 / 金丝雀发布
- GitOps（ArgoCD/Flux）

### 监控与告警
- Prometheus 指标采集与 PromQL 查询
- Grafana 仪表盘设计
- ELK/EFK 日志栈
- Jaeger/Tempo 链路追踪
- SLI/SLO/SLA 定义与告警阈值

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/01-运维云原生"
WHERE file.name != "运维云原生-MOC"
SORT updated DESC
```
