

## 一、 Nginx 接入 Prometheus 监控实战

监控 Nginx 通常有两种主流方式：

### 1. 方案选择

- **方式 A：官方** `**nginx-prometheus-exporter**`

- **原理**：利用 Nginx 原生的 `with-http_stub_status_module` 模块，导出基础的连接数、请求数等指标。
- **优点**：部署极其简单，官方支持。

- **方式 B：基于 VTS 模块的 Exporter**

- **原理**：需编译 `nginx-module-vts` 模块。
- **优点**：提供极详细的虚拟主机、上游服务器、缓存命中率等指标。

### 2. 部署步骤（以官方 Exporter 为例）

1. **配置 Nginx 状态页**：

在 Nginx 配置文件的 `server` 段添加：

Nginx

```
location /metrics {
    stub_status on;
    allow 127.0.0.1; # 仅允许本地或 Exporter 访问
    deny all;
}
```

2. **启动 Exporter**：

Bash

```
docker run -p 9113:9113 nginx/nginx-prometheus-exporter:latest -nginx.scrape-uri=http://<NGINX_IP>:80/metrics
```

3. **修改 Prometheus 配置**：

在 `prometheus.yml` 中添加 Job：

YAML

```
- job_name: 'nginx_monitor'
  static_configs:
    - targets: ['localhost:9113']
```

---

## 二、 核心监控指标分类详解【面试高频】

### 1. 系统层面监控 (System Level)

针对服务器基础资源的监控，通常配合 `node_exporter` 使用。

|   |   |   |
|---|---|---|
|**监控大类**|**核心监控指标 (Metrics)**|**业务意义**|
|**CPU**|`node_cpu_seconds_total`<br><br>(idle/system/user)|监控 **CPU 使用率、系统调用占比、用户进程占比**。高 System 占比通常意味着内核态压力大。|
|**内存**|`node_memory_MemAvailable_bytes`<br><br>/ `SwapTotal`|监控 **物理内存可用率、交换分区(Swap)使用量、缓存/缓冲区(Cache/Buffer)大小**。防止 OOM。|
|**磁盘**|`node_disk_read_bytes_total`<br><br>/ `node_filesystem_avail_bytes`|监控 **磁盘 IOPS、读写吞吐量、文件系统剩余空间百分比**。预防磁盘满导致的系统崩溃。|
|**网络**|`node_network_receive_bytes_total`<br><br>/ `errs`|监控 **网卡实时带宽、网络收发包速率、丢包与错包率**。排查网络拥塞或硬件故障。|

### 2. 应用层面监控 (Application Level)

针对具体中间件的业务性能指标。

#### A. MySQL 监控 (mysqld_exporter)

- **QPS/TPS**：通过 `com_select` 等查询增量计算，反映数据库瞬时吞吐压力。
- **当前连接数**：监控 `Threads_connected`，防止因连接数满导致的 `Too many connections` 报错。
- **慢查询数量**：监控 `Slow_queries` 计数器，评估索引优化效果与 SQL 性能稳定性。
- **主从延迟 (Seconds_Behind_Master)**：关键的高可用指标，反映从库同步数据的实时性。

#### B. Nginx 监控 (nginx_exporter)

- **活跃连接数 (Active Connections)**：当前所有状态的连接总数。
- **请求速率 (Requests per Second)**：单位时间内处理的 HTTP 请求量。
- **状态码分布 (Status Codes)**：监控 4xx (客户端错误) 和 5xx (服务端错误) 的占比，快速定位故障。

#### C. Redis 监控 (redis_exporter)

- **内存使用率 (used_memory)**：Redis 是内存数据库，此指标是防宕机的核心。
- **Key 命中率**：通过 `keyspace_hits` 和 `keyspace_misses` 计算，反映缓存设计的合理性。
- **已连接客户端数 (connected_clients)**：监控突发连接，防止因达到 `maxclients` 限制而拒绝服务。

---

## 三、 PromQL 语言扩展建议

PromQL (Prometheus Query Language) 是 Prometheus 的灵魂，面试中常考以下进阶用法：

1. **瞬时向量 vs 区间向量**：

- `node_cpu_seconds_total`：瞬时值。
- `node_cpu_seconds_total[5m]`：过去 5 分钟内的数据序列。

2. **常用聚合函数**：

- `rate()`：计算计数器（Counter）在一段时间内的每秒平均增长率（最常用）。
- `increase()`：计算一段时间内的增量。
- `sum(by (instance) (...))`：按维度进行求和统计。

3. **标签匹配**：

- `mysql_up{job="mysql", env="prod"}`：通过标签（Label）精确筛选特定环境的指标。

---

_注：本笔记由技术学习者整理，重点侧重于生产环境中的实际应用与排障。_