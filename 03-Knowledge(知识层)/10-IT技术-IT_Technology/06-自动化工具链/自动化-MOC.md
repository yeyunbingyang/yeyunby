---
title: 自动化工具链 MOC
domain: IT_Technology
tags: [MOC, 自动化, Shell, Ansible, Terraform]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "自动化工具链子域地图，覆盖Shell脚本、Python自动化、配置管理、基础设施即代码与任务调度"
---

# 自动化工具链

消除重复手工操作，让系统配置、部署和任务执行变得可重复、可审计、可扩展。核心原则：**凡是做了两次的事，第三次必须自动化**。

## 学习路径

`Shell 脚本基础` → `Python 自动化` → `配置管理（Ansible）` → `基础设施即代码（Terraform）` → `任务调度（Airflow/Cron）`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| 幂等性 | 脚本运行多次结果相同，不产生副作用 |
| IaC | 基础设施即代码，用版本化配置文件管理云资源 |
| 配置漂移 | 实际状态与期望状态不一致，配置管理工具防止漂移 |
| DAG | 有向无环图，任务调度中表达依赖关系的数据结构 |
| Dry Run | 预演执行不实际修改，用于验证脚本/配置正确性 |

## 关键知识点

### Shell 脚本
- Bash 变量/数组/条件/循环/函数
- 错误处理（set -euo pipefail）
- 文本处理三件套（grep/awk/sed）
- 进程替换与命令组合（xargs/tee/trap）
- 脚本健壮性（参数校验/日志/幂等设计）

### Python 自动化
- 文件系统操作（pathlib/shutil）
- 网络请求（requests/httpx）
- 系统调用（subprocess/os）
- 定时任务（schedule 库）
- CLI 工具开发（Click/Typer/argparse）

### Ansible 配置管理
- Playbook 结构与执行顺序
- Role 组织最佳实践
- Inventory 动态与静态主机管理
- 模块生态（command/shell/file/template/service）
- Vault 加密敏感变量

### Terraform 基础设施即代码
- Provider/Resource/Data/Output/Variable
- State 文件管理与远程后端（S3/Terraform Cloud）
- 模块化与复用
- terraform plan/apply/destroy 工作流
- 多云资源管理（AWS/GCP/阿里云）

### 任务调度
- Cron 表达式与 crontab 管理
- Apache Airflow DAG 定义与 Operator
- 任务依赖、重试与告警
- 轻量替代（Celery/APScheduler）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/06-自动化工具链"
WHERE file.name != "自动化-MOC"
SORT updated DESC
```
