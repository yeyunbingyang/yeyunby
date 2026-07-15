# 任务背景

运维人员需要对系统和业务日志进行精准把控，便于分析系统和业务状态。日志分布在不同的服务器上，传统方法需要依次登录每台服务器查看日志，既繁琐又效率低下。

因此，需要集中化的日志管理工具，将位于不同服务器上的日志统一收集后进行分析与展示。

前面我们学习过 rsyslog，它可以实现日志的集中化管理，但在集中后的日志统计与检索方面存在不足。虽然可以使用 wc、grep、awk 等命令实现基础统计与检索，但在复杂场景下难以满足需求，因此需要一套专业的日志收集、分析与展示系统。

![[885b8e77a8.png]]

## 日志统计需求升级

获取 PV 信息：

```
cat /usr/local/nginx/logs/access.log | wc -l
```

获取 UV 信息：

```
awk '{print $1}' /usr/local/nginx/logs/access.log | sort | uniq | wc -l
```

---

## 新需求

**问题1：**  
需要按时间周期（如分钟 / 小时 / 天）统计 PV 和 UV，且时间范围可动态调整。

**问题2：**  
由于 LB 负载均衡将日志分散到多个 Real Server，需要先进行日志汇总再统一统计。

**问题3：**  
统计结果需要以图形化方式展示，提高可读性和说服力。

---

## 解决方案

基于以上需求，需要引入专业的日志分析系统：

- **ELK**  
    Elasticsearch（NoSQL） + Logstash（采集工具） + Kibana（日志分析工具）
- **EFK**  
    Elasticsearch（NoSQL） + Filebeat（轻量级采集工具） + Kibana（日志分析工具）
- **ELFK**  
    Elasticsearch（NoSQL） + Logstash（日志清洗） + Filebeat（轻量级采集工具） + Kibana（日志分析工具）

数据库运维 / 数据库 DBA

MySQL + Oracle + Redis + MongoDB + Elasticsearch + 国产数据库（TiDB、达梦、人大金仓）

LogStash 类似 Fluentd、Rsyslog

Kibana类似 GoAccess

# 任务要求

1. 搭建 ELK 集群
2. 收集日志信息并进行展示

# 任务拆解

1. 认识 ELK
2. **部署 Elasticsearch 集群并了解其基本概念**
3. 安装 Cerebro（适合多数版本）/ Elasticsearch-head（早期版本）实现图形化操作
4. 安装 Logstash 收集日志
5. 安装 Kibana 进行日志展示
6. 安装 Filebeat 实现轻量级日志收集

# 学习目标

- 能够说出 ELK 的应用场景
- 能够区分 ELK 架构中 Elasticsearch、Logstash、Kibana 三个组件的主要功能
- 能够单机部署 Elasticsearch
- 能够部署 Elasticsearch 集群
- 理解 ELK 中索引的概念
- 能够部署 Logstash
- 能够使用 Logstash 进行日志采集
- 能够部署 Kibana 并连接 Elasticsearch 集群
- 能够通过 Kibana 查看 Elasticsearch 索引信息
- 了解使用 Filebeat 收集日志相对于 Logstash 的优点
- 能够安装 Filebeat
- 能够使用filebeat收集日志并传输给logstash

# 一、ELK 概述

ELK 是一套开源的日志分析系统，由 Elasticsearch + Logstash + Kibana 组成。

官网：[https://www.elastic.co/cn/products](https://www.elastic.co/cn/products)

先用一句话简单了解 E、L、K 这三个软件：

- Elasticsearch：分布式搜索引擎
- Logstash：日志收集与过滤，并输出给 Elasticsearch
- Kibana：图形化展示工具

![[51e554f2cf.png]]

## ELK 下载地址

[https://www.elastic.co/cn/downloads](https://www.elastic.co/cn/downloads)

环境准备：

![[d4d0836a65.png]]

## 环境准备

推荐6g内存

1. 静态 IP（要求能上公网，建议使用虚拟机 NAT 网络模式）
2. 主机名及主机名绑定

```
192.168.88.211 kibana
192.168.88.212 vm1.cluster.com
192.168.88.213 vm2.cluster.com
192.168.88.214 vm3.cluster.com

# 组件规划
vm1.cluster.com  elasticsearch
vm2.cluster.com  logstash
vm3.cluster.com  filebeat
vm4.cluster.com  elasticsearch
```

3. 关闭防火墙和 SELinux

```
# 关闭防火墙
systemctl stop firewalld
systemctl disable firewalld
iptables -F

# 关闭 SELinux
setenforce 0
# 提示：setenforce: SELinux is disabled
```

---

4. 时间同步

5. yum 安装依赖软件（可选）

```
yum install -y vim wget rsync net-tools
```

# 二、Elasticsearch

## Elasticsearch 简介

Elasticsearch（简称 ES）是一个开源的分布式搜索引擎，同时也是一个分布式文档数据库（NoSQL）。它具备海量数据存储能力，以及快速的搜索与分析能力。

提到搜索，大家通常会想到百度、谷歌、必应等搜索引擎。当然，在实际业务中也存在多种搜索场景。

![[eaca1e6838.png]]

## Elasticsearch 部署

第 1 步：确认 JDK 环境（使用系统自带 OpenJDK 即可）

```
[root@vm2 ~]# java -version
openjdk version "1.8.0_362"
OpenJDK Runtime Environment (build 1.8.0_362-b08)
OpenJDK 64-Bit Server VM (build 25.362-b08, mixed mode)
```

第 2 步：Elasticsearch 安装与配置

```
# 下载
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.16.0-x86_64.rpm

# 安装
dnf install elasticsearch-8.16.0-x86_64.rpm -y
```

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.3.3-x86_64.rpm

第 3 步：单机 Elasticsearch 配置与服务启动

```
# 编辑配置文件
cat /etc/elasticsearch/elasticsearch.yml

cluster.name: my-cluster
node.name: 192.168.88.212

path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch

network.host: 0.0.0.0
http.port: 9200
transport.port: 9300

xpack.security.enabled: false
xpack.security.http.ssl.enabled: false
xpack.security.transport.ssl.enabled: false

discovery.type: single-node
```

```
# 启动并设置开机自启
systemctl start elasticsearch
systemctl enable elasticsearch
```

```
# 查看端口（启动较慢，约 1 分钟）
netstat -ntlup | grep java

tcp6  0  0 :::9200  :::*  LISTEN
tcp6  0  0 :::9300  :::*  LISTEN
```

9200：HTTP 数据传输端口  
9300：集群通信端口（当前为单机模式）

错误排查

- 服务日志
- 应用日志
- 系统日志 masage

配置项可能错误：集群配置

第 4 步：查看状态

使用 curl 命令访问 Elasticsearch：

```
curl "http://192.168.88.212:9200/_cluster/health?pretty"
记住关键命令：_cluster，health代表健康情况，pretty格式化输出
```

或通过浏览器访问：

```
http://192.168.88.212:9200/_cluster/health?pretty
```

## Elasticsearch 集群部署

### 集群部署注意事项

- 集群配置参数
- 节点发现机制

Elasticsearch 8.x 默认使用 Cluster Coordination Service（CCS）进行节点发现和集群形成，替代了之前的 Zen Discovery。

配置示例：

```
# 指定初始 master 节点（集群首次启动时必须配置）
cluster.initial_master_nodes:
  - node1
  - node2
  - node3

# 配置主机发现列表（推荐静态设置）
discovery.seed_hosts:
  - 192.168.88.211
  - 192.168.88.212
  - 192.168.88.213
  - 192.168.88.214
  - 192.168.88.215
  - 192.168.88.216

# 设置发现时等待超时时间（默认 30 秒，可调整）
discovery.find_peers_interval: 30s
```

### 避免脑裂问题

为防止脑裂（split-brain）现象，需要设置以下参数：

```
# 集群中需要选举 master 的最少节点数，推荐 (N/2)+1
cluster.voting_only_nodes: 3
```

这表示集群中设置了 3 个“仅投票节点”（voting-only nodes）。这些节点不作为 master 候选，只参与 master 选举的投票过程。

1、什么是 master 选举的最小节点数？  
Elasticsearch 的 master 选举依赖仲裁机制，推荐设置最小 master 数为 (N/2)+1，其中 N 是投票节点（包含 master-eligible 节点和 voting-only 节点）的总数。

```
node.roles: [master]
```

2、voting_only_nodes 是什么？这些节点：  
不会当选为 master（即使 master 节点宕机，它们不会接管）  
只用于维持集群仲裁，提高选举容错能力

```
node.roles: [voting_only]
```

### 集群节点设置

Elasticsearch 8.x 支持以下节点类型，建议按业务需求分配：

- Master 节点：负责集群管理和协调，建议单独部署。
- Data 节点：存储和处理索引数据。
- Coordinating 节点（仅协调节点）：用于客户端负载均衡（视场景）。
- Ingest 节点：用于预处理数据。

```
# Master 节点
node.master: true
node.data: false
node.ingest: false
node.roles: ["master"]

# Data 节点
node.master: false
node.data: true
node.ingest: false
node.roles: ["data"]
```

注意：

- Master 节点与 Data 节点分离：Master 需保证稳定性，Data 节点可能因 IO 负载而不稳定。
-   
    数量建议：建议至少有 3 个 Master 节点（避免脑裂），Data 节点根据数据量规划。

### 内存设置

Elasticsearch 默认堆内存大小为 1GB，需要根据实际业务进行调整：

建议为物理内存的一半

```
# 比如服务器内存为 32GB，设置堆内存大小为系统内存的一半，但不超过 32GB
export ES_JAVA_OPTS="-Xms16g -Xmx16g"
```

修改配置文件

```
vim /etc/elasticsearch/jvm.options

-Xms16g
-Xmx16g
```

注意：

堆内存分配过会导致垃圾回收延迟过，建议不超过32GB。

JVM预留的直接内存可以通过-XX:MaxDirectMemorySize 参数调整。

### 硬盘空间规划

数据路径  
Elasticsearch 的数据默认存储在 `/var/lib/elasticsearch`，可以通过配置文件修改：

```
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
```

磁盘性能优化  
挂载高性能存储（如 NVMe SSD）后可启用数据压缩：

```
index.codec: best_compression
```

配置磁盘分层存储（冷热分层）：在集群中配置冷热节点，热节点处理实时写入，冷节点处理长期存储：

```
# 热节点
node.roles: ["data_hot"]

# 冷节点
node.roles: ["data_cold"]
```

### 网络与监听设置

配置 Elasticsearch 接收外部连接：

```
# 允许 HTTP 客户端从任何地方访问（生产环境需限制）
http.host: 0.0.0.0

# 配置传输层监听所有节点
transport.host: 0.0.0.0
```

配置参考文档：[https://www.elastic.co/guide/en/elasticsearch/reference/index.html](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)  
首先在 ES 集群所有节点都安装 ES（步骤省略）

可以使用两台或两台以上 ES 组成集群，以下是两台 ES 做集群的配置

elasticsearch master：

```
[root@vm2 ~]# dnf install elasticsearch-8.16.0-x86_64.rpm -y

[root@vm2 ~]# cat /etc/elasticsearch/elasticsearch.yml | grep -v "#"
cluster.name: my-cluster
node.name: 192.168.88.212

path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
network.host: 0.0.0.0

http.port: 9200
transport.port: 9300

xpack.security.enabled: false
xpack.security.http.ssl.enabled: false
xpack.security.transport.ssl.enabled: false

# cluster.initial_master_nodes注释重新编写
discovery.seed_hosts: ["192.168.88.211", "192.168.88.212"]
cluster.initial_master_nodes: ["192.168.88.212"]
#discovery.type: single-node 这一行在集群模式一定要注释
```

elasticsearch data：

```
[root@vm1 ~]# dnf install elasticsearch-8.16.0-x86_64.rpm -y

[root@vm1 ~]# cat /etc/elasticsearch/elasticsearch.yml | grep -v "#"
cluster.name: my-cluster
node.name: 192.168.88.211

path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
network.host: 0.0.0.0

http.port: 9200
transport.port: 9300

xpack.security.enabled: false
xpack.security.http.ssl.enabled: false
xpack.security.transport.ssl.enabled: false

# cluster.initial_master_nodes注释重新编写
discovery.seed_hosts: ["192.168.88.211", "192.168.88.212"]
cluster.initial_master_nodes: ["192.168.88.212"]
```

启动或重启服务

```
[root@vm1 ~]# systemctl restart elasticsearch
[root@vm1 ~]# systemctl enable elasticsearch

[root@vm2 ~]# systemctl restart elasticsearch
```

查看状态，浏览器输入地址：  
[http://192.168.88.212:9200/_cluster/health?pretty](http://192.168.88.212:9200/_cluster/health?pretty)

![[ce434ca1c8.png]]

## elasticsearch 基础概念

主要的基础概念有：Node、Index、Type、Document、Field、Shards 和 Replicas。

- Node（节点）：运行单个 ES 实例的服务器
- Cluster（集群）：一个或多个节点构成集群
- Index（索引）：索引是多个文档的集合（类似办公室的柜子）
- Type（类型）：一个 Index 可以定义一种或多种类型，将 Document 逻辑分组（类似柜子中的文件夹）
- Document（文档）：Index 里每条记录称为 Document（类似文件夹中的一张 A4 纸）
- Field（字段）：ES 存储的最小单元（类似 A4 纸中的每一列）
- Shards（分片）：ES 将 Index 分为若干份，每一份就是一个分片
- Replicas（副本）：Index 的一份或多份副本（用于数据备份和高可用）

为了便于理解，可以和 MySQL 这种关系型数据库做对比：

关系型数据库（如 MySQL、Oracle 等）  
  

|   |   |   |
|---|---|---|
|**关系型数据库 (MySQL)**|**Elasticsearch (ES)**|**核心说明**|
|**Database** (数据库)|**Index** (索引)|逻辑容器，存储相关数据的集合。|
|**Table** (表)|**~~Type~~** (已废弃)|以前 ES 允许一个索引下有多个 Type，现在**一个 Index 对应一个逻辑表**。|
|**Row** (行)|**Document** (文档)|ES 的最小存储单位，通常是 JSON 格式。|
|**Column** (列)|**Field** (字段)|数据的属性，ES 中每个字段都有自己的 Mapping 类型。|
|**Schema** (结构定义)|**Mapping** (映射)|定义字段类型（如 `text`<br><br>, `keyword`<br><br>, `date`<br><br>等）。|
|**SQL**|**DSL** (Query DSL)|ES 使用 JSON 风格的查询语句。|
|**Primary Key** (主键)|**_id**|唯一标识文档的标识符。|

💡 深度解析：为什么 ES 要删掉 Type？

在 MySQL 中，两个不同的表（Table A 和 Table B）即使有同名的字段 `name`，它们也是完全独立的。

但在 Elasticsearch 中：

1. **底层存储限制**：同一个 Index 下的所有 Document，最终是存储在同一个物理 Lucene 索引中的。
2. **字段冲突**：如果你在 `Type1` 中定义 `name` 为“日期型”，在 `Type2` 中定义 `name` 为“长整型”，Lucene 无法处理这种冲突。

**结论**：为了性能和逻辑的清晰，ES 强制要求 **一个 Index = 一个逻辑表**。解决同名冲突

ES 是分布式搜索引擎，每个索引有一个或多个分片（shard），索引的数据会被分配到各个分片上，可以理解为一份数据被拆分成多份存储在不同节点。

当 ES 集群增加或删除节点时，shard 会在多个节点之间自动进行均衡分配。

默认是 5 个 primary shard（主分片）和 1 个 replica shard（副本，用于容错）。

## Elasticsearch 基础 API 操作（重点、记住）

前面我们通过  
`http://192.168.88.212:9200/_cluster/health?pretty`  
查看 ES 集群状态，其实就是它的一种 API 操作。

---

什么是 API？

API（Application Programming Interface，应用程序编程接口），就是**无需访问程序源码或理解内部工作机制，就能实现相关功能的接口**。

---

API 的理解

所谓的 API 就是日常生活中的 **URL 地址**：

- 别人已经编写好程序或代码
- 我们不需要了解底层原理
- 只需要通过 URL 就可以获取数据

---

**返回数据格式**

通常返回数据格式有两种：

- XML 格式
- JSON 格式

### RestFul API 格式

```
curl -X <verb> '<protocol>://<host>:<port>/<path>?<query_string>' -d '<body>'
```

---

参数说明

|   |   |
|---|---|
|参数|描述|
|verb|HTTP 方法，比如 GET、POST、PUT、HEAD、DELETE|
|host|ES 集群中的任意节点主机名|
|port|ES HTTP 服务端口，默认 9200|
|path|索引路径|
|query_string|可选的查询请求参数，例如 `?pretty`<br><br>参数将返回 JSON 格式数据|
|-d|里面放一个 JSON 格式请求主体|
|body|自己编写的 JSON 格式请求主体|

---

elasticseearch 的 API 很多，我们运维人员主要用到以下几个较简单的 API。  
更多 API 参考：  
[https://www.elastic.co/guide/en/elasticsearch/reference/8.17/index.html](https://www.elastic.co/guide/en/elasticsearch/reference/8.17/index.html)

### 查看节点信息

通过 `curl` 或浏览器访问 `http://192.168.88.212:9200/_cat/nodes?v`（`ip` 为 ES 节点 IP，如果有 ES 集群，则为 ES 任意节点 IP）。

Bash

```
[root@vm2 ~]# curl http://192.168.88.212:9200/_cat/nodes?v
ip             heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
192.168.88.212           29          94   2    2.33    1.88     0.85 mdi       * 192.168.88.212
192.168.88.211           26          92   1    0.24    0.37     0.33 mdi       -      192.168.88.211
```

---

关于 Curl

**Curl** 是 Linux 命令行浏览器，没有图形界面，通过命令方式发起 HTTP 请求。它支持多种请求方法：

- **GET 请求**：默认方式。例如 `curl http://www.baidu.com`。
- **POST 请求**：使用 `-X` 参数。例如 `curl -X POST http://www.baidu.com/login.php`。
- **其他支持**：同样支持 `PUT`、`DELETE` 等 RESTful 常用动作。

### 查看索引信息

通过 `curl` 或浏览器访问 `http://192.168.88.212:9200/_cat/indices?v`。

```
[root@vm2 ~]# curl http://192.168.88.212:9200/_cat/indices?v
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size
```

**注**：默认状态下没有任何索引。

---

### 新增索引

```
[root@vm2 ~]# curl -X PUT http://192.168.88.212:9200/nginx_access_log
{"acknowledged":true,"shards_acknowledged":true,"index":"nginx_access_log"}
```

**再次查看索引信息：**

```
[root@vm2 ~]# curl http://192.168.88.212:9200/_cat/indices?v
health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   nginx_access_log 90Z7DvInTz6seXMBYhHVAw   5   1          0            0     2.2kb          1.1kb
```

![[cd6c7777cf.png]]

索引健康状态说明

- **green**：所有的主分片和副本分片都已分配。你的集群是 **100% 可用**的。
- **yellow**：所有的主分片已经分配，但**至少还有一个副本分片是缺失的**。不会有数据丢失，所以搜索结果依然是完整的。不过，你的可用性在某种程度上被弱化。如果更多的分片消失，你就会丢数据了。把 yellow 想象成一个需要及时调查的警告。
- **red**：**至少一个主分片（以及它的全部副本）缺失**。这意味着你在丢失数据：搜索只能返回部分数据，分配到这个分片上的写请求会返回一个异常。

### 删除索引

```
[root@vm2 ~]# curl -X DELETE http://192.168.88.212:9200/nginx_access_log
{"acknowledged":true}
```

---

核心概念：节点角色

在 Elasticsearch 中，主节点与数据节点的关系与 MySQL/Redis 的主从架构有所不同。

- **主节点 (Master Node)**

- **职责**：负责管理和协调整个集群，例如创建/删除索引、追踪集群节点状态、决定分片的分配。
- **特点**：通常不负责处理数据的存储和搜索，以保证其管理职能的响应速度。

- **数据节点 (Data Node)**

- **职责**：实际存储数据（分片）并执行搜索、聚合等 CPU/IO 密集型操作。
- **特点**：处理所有数据的增删改查请求。

**架构建议**：在小型或测试环境中，一个节点可能既是主节点也是数据节点。但在生产或复杂环境中，通常会将主节点和数据节点角色分离，以确保集群的效率和稳定性：主节点专注于**集群管理**，数据节点专注于**数据处理**。

## ES 查询语句（重点、记住）

ES 提供了一种基于 JSON 格式的查询语言，被称为 **Query DSL**（Domain Specific Language）。在实际操作中，它表现为：**URL 地址 + JSON 数据体**。

---

### Query DSL 基础架构

针对 Elasticsearch 的操作，通常分为**增、删、改、查**四个动作。以下是查询中常用的匹配条件：

#### 1. 核心查询逻辑

- **match_all**: 查询所有文档，是最简单的查询。
- **match**: 模糊匹配查询，会对查询内容进行分词。
- **bool**: 布尔查询，用于组合多个查询条件（如 `must`, `should`, `must_not`）。
- **range**: 范围查询，常用于日期或数值的筛选（如 `gt`, `lt`, `gte`, `lte`）。

#### 2. 分页控制

- **from**: 跳过前 N 条文档，默认从 `0` 开始。
- **size**: 返回的文档数量，默认为 `10`。

---

### 查询应用案例：

导入数据源

使用官方提供的示例数据：

![[700a963009.png]]

1.下载并导入 Elasticsearch

```
[root@vm2 ~]# ll accounts.json
```

---

#### 导入进 Elasticsearch

```
[root@vm2 ~]# curl -H "Content-Type: application/x-ndjson" -X POST "192.168.88.212:9200/bank/_bulk" --data-binary "@accounts.json"
```

---

说明：

_bulk是Elasticsearch的RESTAPI路径的一部分，意思是“批量处理”。适用于需要一次提交多条数据的场景，比如导入大批数据、批量更新文档等。批量操作可以显著提高性能，避免一次一条数据地发送HTTP请求。

查询确认

```
[root@vm2 ~]# curl http://192.168.88.212:9200/_cat/indices?v
health status index uuid pri rep docs.count docs.deleted store.size pri.store.size
green  open   bank  CzFQ_Gu1Qr2-bpV5MF00Bg 5   1   1000        0            874.7kb     434.4kb
```

2，查询 bank 索引的数据（使用查询字符串进行查询）

RestFul：所有内容聚集在同一个 URL 中

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?q=*&sort=account_number:asc&pretty"
```

---

说明：

- 默认结果为 10 条
- `_search` 属于一类 API，用于执行查询操作
- `q=*`：查询 ES 索引中的所有文档
- `sort=account_number:asc`：根据 account_number 按升序排序
- `pretty`：调整返回结果的显示格式

3，查询 bank 索引的数据（使用 JSON 格式进行查询）=> 推荐使用 QueryDSL 风格

通过 JSON 来实现数据查询操作

```
[root@vm2 ~]# curl \
-X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
'

说明：

`-X GET`：请求方法

 API 接口：
  `http://192.168.88.212:9200/bank/_search?pretty`
  注意 `pretty` 表示返回格式为 JSON 且更易读

 `-H`：请求头，告诉服务器发送的数据格式
  `-H 'Content-Type: application/json'`

 `-d`：data 的缩写，代表要发送的请求数据

```

---

注意：最后为单引号

注意：在Linux终端中，空格+\，代表这条语句还没有执行结束，下面的一行也是这个命令的一部分。

**查询指定数量的数据（使用** `**from、size**` **参数）**

类似 SQL 中的 `SELECT * FROM bank;`，除了 `query` 参数外，还可以传递其他参数影响查询结果，如前面提到的 `sort`，这里使用 `size` 限制返回条数。

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { "match_all": {} },
  "size": 1
}
'
```

---

说明：查询返回 **1 条数据**

**指定位置与查询条数**

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { "match_all": {} },
  "from": 0,
  "size": 2
}
'
```

---

说明：

- `from: 0` 表示从第 1 条数据开始
- `size` 指定查询的条数
- 类比 SQL：

- 只有 `size` → `SELECT * FROM bank LIMIT size;`
- 既有 `from` 又有 `size` → `SELECT * FROM bank LIMIT from, size;`

- 默认情况下，`from` 从 0 开始

**匹配查询字段**

返回 `_source`（内置）字段中的指定字段

- 类比 SQL：

- `SELECT * FROM bank;` → 查询所有字段
- `SELECT account_number, balance FROM bank;` → 查询指定字段

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { "match_all": {} },
  "_source": ["account_number", "balance"]
}
'
```

`**match**` **查询**

基本搜索查询，针对特定字段或字段集合进行搜索（类似模糊匹配，底层基于全文搜索）

示例：查询编号为 20 的账户

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { 
    "match": { 
      "account_number": 20 
    } 
  }
}
'
特殊：match默认属于模糊匹配，
但是如果是数字类型的匹配，相当于精准匹配，只有查询值为字符串类型，则相当于模糊匹配。
```

查询地址中包含 `mill` 的账户

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { 
    "match": { 
      "address": "mill" 
    } 
  }
}
'
```

`**term**` **查询**

基本搜索查询，针对特定字段或字段集合进行搜索（**类似精准匹配**）

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
  "query": { 
    "term": { 
      "account_number": 20 
    } 
  }
}
'
```

**查询地址包含** `**mill**` **或** `**lane**` **的所有账户**

---

bool 查询示例

1️⃣ `must` 查询（AND 查询）

字段必须同时存在，例如查询 **地址同时包含** `**mill**` **和** `**lane**` 的账户：

```
curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '{
  "query": {
    "bool": {
      "must": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

2️⃣ `should` 查询（OR 查询）

字段只需满足其中一个条件，例如查询 **地址包含** `**mill**` **或** `**lane**` 的所有账户：

```
curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" \
-H 'Content-Type: application/json' \
-d '{
  "query": {
    "bool": {
      "should": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

---

💡 **总结：**

- `must` → AND，字段必须全部匹配
- `should` → OR，只需满足一个匹配即可

这样就清晰区分了 AND/OR 查询在 Elasticsearch 中的使用。

**range 查询**

指定区间内的数字或者时间。  
**操作符**：

- `gt`：大于
- `gte`：大于等于
- `lt`：小于
- `lte`：小于等于

**示例：查询余额大于等于 20000 且小于等于 30000 的账户**

```
[root@vm2 ~]# curl -X GET "http://192.168.88.212:9200/bank/_search?pretty" -H 'Content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "must": { "match_all": {} },
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}'
```

类比 SQL：

- 比较运算符 (`>`, `>=`, `<`, `<=`)
- `filter` 相当于 `WHERE`
- `range` 相当于 `BETWEEN ... AND ...`

## 扩展：AI大模型带你玩转elasticsearch查询如何设计提示词，让AI更懂你？

①尽量给AI搜索进分类，相同类型的放在一起查询（同提问）

②给AI个定位，提前喂些数据，规定模型返回的数据格式

参考：

提示：你是个ELK运维工程师，擅长ELK搭建、分析以及ES DSL查询操作  
问：查看bank索引中前10条记录，然后按照account_num进行升序排列  
提示：记住数据集以及我们使用的查询习惯

# 三、elasticsearch-head 与 cerebro

## elasticsearch-head

- **说明**：功能类似 cerebro，只不过是浏览器插件版
- **第一步**：下载插件（科学上网，可到 Google 商店）

![[4e1b4bb433.png]]

- 第二步：打开GoogleChrome浏览器，找到扩展程序管理，如下图

![[69513e69ab.png]]

第三步：打开开发者模式

![[06d03408be.png]]

第四步：拖拽插件到浏览器中，安装后如下图所示

![[cba0f1116f.png]]

第五步：点击插件，输ES集群信息

![[7189ec021b.png]]

连接成功后，如下图所示

![[79256e83b5.png]]

## 扩展：Cerebro

### Cerebro 简介

Cerebro 是一个开源的 Elasticsearch 集群管理工具，提供了直观的 Web 界面，用于监控和管理 Elasticsearch 集群。它轻量级、功能强大，适合开发和生产环境中的 Elasticsearch 管理工作。

### 配置 JDK

```
sudo yum install java-1.8.0-openjdk
sudo alternatives --config java
```

### 安装 Cerebro

```
wget https://github.com/lmenezes/cerebro/releases/download/v0.9.4/cerebro-0.9.4.tgz
tar -xf cerebro-0.9.4.tgz
cd cerebro-0.9.4
```

### 配置 Cerebro

#### 打开配置文件

```
vim conf/application.conf
```

#### 配置 Cerebro 添加 Elasticsearch 集群

```
# 添加 Elasticsearch 集群
hosts = [
  {
    host = "http://192.168.88.212:9200"
    name = "My Elasticsearch Cluster"
  }
]
```

### 启动 Cerebro

```
./bin/cerebro
```

```
[info] play.api.Play - Application started (Prod) (no global state)
[info] p.c.s.AkkaHttpServer - Listening for HTTP on /0:0:0:0:0:0:0:0:9000
```

### cerebro基本使用

![[e46a338846.png]]![[911fa595bf.png]]

# 四、Logstash

## Logstash 简介

Logstash 是一个开源的数据采集工具，通过从数据源采集数据，进行过滤处理，并自定义格式输出到目标位置。

数据分为：

1. 结构化数据：如 MySQL 数据库的表等
2. 半结构化数据：如 XML、YAML、JSON 等
3. 非结构化数据：如文档、图片、音频、视频等

Logstash 可以采集任何格式的数据，这里主要用于采集系统日志、服务日志等日志类型数据。

官方产品介绍：[https://www.elastic.co/cn/products/logstash](https://www.elastic.co/cn/products/logstash)

![[36a0e16b67.png]]

input 插件：用于导入日志源（必须配置）

[https://www.elastic.co/guide/en/logstash/current/input-plugins.html](https://www.elastic.co/guide/en/logstash/current/input-plugins.html)

filter 插件：用于过滤（不是必须的配置）=>对采集到的数据进清洗以及过滤操作

=> 类似 Fluentd 的 mongo 等插件  
[https://www.elastic.co/guide/en/logstash/current/filter-plugins.html](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html)

output 插件：用于导出（必须配置）

[https://www.elastic.co/guide/en/logstash/current/output-plugins.html](https://www.elastic.co/guide/en/logstash/current/output-plugins.html)

## Logstash 部署

ES 3台

Logstash 与业务服务器同台 【内存6到8g】

在 Logstash 服务器上确认 OpenJDK 安装

```
[root@vm3 ~]# java -version
```

在 Logstash 服务器上安装 Logstash

下载地址：[https://www.elastic.co/downloads/past-releases/logstash-8-16-0](https://www.elastic.co/downloads/past-releases/logstash-8-16-0)

```
[root@vm3 ~]# rpm -ivh Logstash-8.16.0.rpm
```

配置 Logstash 主配置文件

```
[root@vm3 ~]# cat /etc/logstash/logstash.yml | grep -v '#' | grep -v '^$'
path.data: /var/lib/logstash
path.config: /etc/logstash/conf.d/
api.http.host: "192.168.88.213"
path.logs: /var/log/logstash
```

启动测试

```
[root@vm3 ~]# cd /usr/share/logstash/bin
# 使用下面的空输入和空输出启动测试一下
[root@vm3 bin]# ./logstash -e 'input { stdin {} } output { stdout {} }'
```

运行后，输入字符将被 stdout 作为标准输出内容输出

**Logstash 插件配置格式：**

```
input {
  stdin {}
}

output {
  stdout {}
}
```

![[34eb35b452.png]]

**关闭启动**

测试能启动成功后，`Ctrl + C` 取消，则关闭了

**另一种验证方法：pipeline 配置文件编写与校检**

```
# 上述测试还可以使用如下方法进行：
[root@vm3]# vim /etc/logstash/conf.d/test.conf
```

```
input {
  stdin {}
}

filter {
}

output {
  stdout {
    codec => rubydebug
  }
}
```

```
[root@vm3 bin]# pwd
/usr/share/logstash/bin

[root@vm3 bin]# ./logstash --path.settings /etc/logstash -f /etc/logstash/conf.d/test.conf -t
```

```
Config Validation Result: OK. Exiting Logstash
```

```
--path.settings 指定 logstash 主配置文件目录
-f 指定片段配置文件
-t 测试配置文件是否正确
codec => rubydebug 这句可写可不写，默认就是这种输出方式
```

-r 动态装载

```
-r 参数很强大，会动态加载配置文件，也就是说启动后，可以不用重启而直接修改配置文件
```

```
[root@vm3 bin]# ./logstash \
--path.settings /etc/logstash \
-r -f /etc/logstash/conf.d/test.conf
```

```
hehe
"@timestamp" => xxxx-xx-xxT10:40:10.839Z,
"message" => "hehe",
"host" => "vm3.cluster.com",
"@version" => "1"

haha
"@timestamp" => xxxx-xx-xxT10:40:11.794Z,
"message" => "haha",
"host" => "vm3.cluster.com",
"@version" => "1"
```

## 日志采集

### 采集 messages 日志

Logstash 配置文件，如 test.conf、messages.conf，专业名词叫做 pipeline（logstash）  
这里以 `/var/log/messages` 为例，只定义 input 输入和 output 输出，不考虑过滤

```
[root@vm3 bin]# vim /etc/logstash/conf.d/messages.conf

input {
  file {
    path => "/var/log/messages"
    start_position => "beginning"
  }
}

output {
  elasticsearch {
    hosts => ["http://192.168.88.212:9200"]
    index => "messages-%{+YYYY.MM.dd}"
  }
}
```

```
[root@vm3 bin]# vim /etc/logstash/conf.d/messages.conf

input {
  file {
    path => "/var/log/messages"
    start_position => "beginning"
  }
}

output {
  elasticsearch {
    hosts => ["http://192.168.88.212:9200"]
    index => "messages-%{+YYYY.MM.dd}"
  }
}
```

```
# 运行稳定后，可以直接放入后台运行
[root@vm3 bin]# nohup ./logstash --path.settings /etc/logstash/ -r -f /etc/logstash/conf.d/messages.conf &
```

```
# 后台运行如果要杀掉，请使用
pkill java
# 或 ps 查看 PID 再 kill -9 清除
```

请自行练习验证：

1、在 logstash 那台服务器上做些操作（如：重启 sshd 服务），让 `/var/log/messages` 有新的日志信息，然后验证 cerebro 的数据。结果：会自动更新，浏览器刷新就能在 cerebro 上看到更新的数据。

2、kill 掉 logstash 进程（相当于关闭），也做一些操作让 `/var/log/messages` 日志有更新，然后再次启动 logstash。结果：会自动连上 ES 集群，cerebro 也能查看到数据的更新。

### 采集多日志源

```
[root@vm3 bin]# vim /etc/logstash/conf.d/test.conf

input {
  file {
    path => "/var/log/messages"
    start_position => "beginning"
    type => "messages"
  }

  file {
    path => "/var/log/dnf.log"
    start_position => "beginning"
    type => "dnf"
  }
}

filter {
}

output {
  if [type] == "messages" {
    elasticsearch {
      hosts => ["http://192.168.88.212:9200"]
      index => "messages-%{+YYYY.MM.dd}"
    }
  }

  if [type] == "dnf" {
    elasticsearch {
      hosts => ["http://192.168.88.212:9200"]
      index => "dnf-%{+YYYY.MM.dd}"
    }
  }
}
```

### **Logstash 插件安装**

```
cd /usr/share/logstash/bin

./logstash-plugin install logstash-filter-geoip
./logstash-plugin install logstash-filter-mutate
./logstash-plugin install logstash-filter-useragent
```

注：如果加载过慢，则更换国内 Ruby 源

```
yum install -y ruby

gem sources --remove https://rubygems.org/
gem sources --add https://mirrors.aliyun.com/rubygems/

gem sources -l
```

---

放置 GeoIP 数据库

```
ls /etc/logstash/GeoLite2-City.mmdb
```

资料中

---

说明

**该插件主要用于 IP 地址转城市信息，功能有：**

1. **可以把 IP 转换为经纬度**
2. **可以把 IP 转换为具体城市（如北京、巴黎等）**

# 五、Kibana

## Kibana 介绍

安装之前，建议把Kibana（VM1）服务器内存可以调整为6~8G左右

**Kibana 是一个开源的可视化平台，可以为 Elasticsearch 集群的管理提供友好的 Web 界面，帮助汇总、分析和搜索重要的日志数据。**

**文档路径：**[**https://www.elastic.co/guide/en/kibana/current/setup.html**](https://www.elastic.co/guide/en/kibana/current/setup.html)

---

## Kibana 部署

第 1 步：在 Kibana 服务器（VM1）上安装 Kibana

**下载地址：**[**https://www.elastic.co/downloads/past-releases#kibana**](https://www.elastic.co/downloads/past-releases#kibana)

```
[root@vm1 ~]# rpm -ivh kibana-8.16.0-x86_64.rpm
```

第2步：配置 Kibana

```
[root@vm1 ~]# cat /etc/kibana/kibana.yml | grep -v '#' | grep -v '^$'
```

```
server.port: 5601   # 端口

server.host: "0.0.0.0"   # 监听所有地址，允许所有人访问

elasticsearch.hosts: ["http://192.168.88.212:9200"]

logging:
  appenders:
    file:
      type: file
      fileName: /var/log/kibana/kibana.log
      layout:
        type: json

  root:
    appenders:
      - default
      - file

pid.file: /run/kibana/kibana.pid
```

第3步：启动 Kibana 服务

```
[root@vm1 ~]# systemctl start kibana
[root@vm1 ~]# systemctl enable kibana
```

```
[root@vm1 ~]# ps -ef | grep kibana
kibana   127115 1 98 12:17 ?        00:01:23 /usr/share/kibana/bin/../node/glibc-217/bin/node /usr/share/kibana/...
root     127655 125756 0 12:18 pts/1 00:00:00 grep --color=auto kibana
```

---

第4步：访问 Kibana

在浏览器访问：

```
http://kibana服务器IP:5601
```

![[765ea456ac.png]]

## Kibana 汉化

Kibana 8.16.0 版本中内置了中文语言支持。如果希望将 Kibana 界面设置为中文，可以按以下步骤配置：

---

### 修改 Kibana 配置文件

```
vim /etc/kibana/kibana.yml
```

---

### 添加或修改以下配置

```
i18n.locale: "zh-CN"
```

---

### 重启 Kibana

```
systemctl restart kibana
```

![[b2af958627.png]]

## Kibana 连接 Elasticsearch

第一步 进入 Kibana 左侧菜单：  
**分析 → 发现（Discover）**，如下图所示：

![[81552c128b.png]]

第步：创建Elasticsearch视图

![[3aaba5a57d.png]]

第三步：根据需要获取数据

![[e580b5da0e.png]]

![[29fe08d44f.png]]

![[21026866e2.png]]

时间拉长

第四步：根据个需要，获取ES中的数据

![[12d1d38c80.png]]

第五步：如果确认数据没有任何问题，则单击右上保存，便后期设计仪表板

![[4fe0358301.png]]

## kibana基于数据视图构建仪表板

第一步：选择分析菜单下面的Dashboards（仪表板）

![[b37951fca9.png]]

![[ee658e2598.png]]

第二步：了解可视化设计面板

![[4e676a70c1.png]]

第三步：拖入可用字段，选择合适图形

![[22fcd4ae80.png]]

第四步：保存并返回

![[c3e4d90fa0.png]]

![[424f6a057f.png]]

# 六、ELK 项目实践

## Web 服务器准备

在 Logstash 所在机器安装 Nginx 软件（采集 Web 服务器项目，如 NiuShop 电商项目中的 web01/web02 上的 Nginx 访问日志 access.log）。如果资源有限，也可以在 Logstash 所在机器安装 Nginx 进行实践。

```
yum install nginx -y

echo 'web server' > /usr/share/nginx/html/index.html
systemctl start nginx
```

使用浏览器访问 nginx，然后查看 nginx 访问日志（access.log）

```
ls /var/log/nginx/access.log
```

## Logstash 编写 pipeline【拓展】

（采集 access.log + 解决时区问题）

```
input {
  file {
    path => "/var/log/dnf.log"
    start_position => "beginning"
  }
}

filter {

  # 自定义字段 timestamp，并将 @timestamp + 8小时
  ruby {
    code => "event.set('timestamp', event.get('@timestamp').time.localtime + 8*60*60)"
  }

  # 将 timestamp 赋回 @timestamp
  ruby {
    code => "event.set('@timestamp', event.get('timestamp'))"
  }

  # 删除临时字段
  mutate {
    remove_field => ["timestamp"]
  }
}

output {

  stdout {
    codec => rubydebug   # 用于调试输出（生产环境建议移除）
  }

  elasticsearch {
    hosts => ["http://192.168.88.212:9200"]
    index => "dnf-log-%{+YYYY.MM.dd}"
  }
}
```

## 更改 Nginx 访问日志格式为 JSON 格式

```
vim /etc/nginx/nginx.conf
```

---

修改 nginx.conf（覆盖原有日志配置部分）

```
user nginx;
worker_processes auto;

error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {

    ### 配置开始 ###
    log_format json_geo escape=json
        '{'
        '"@timestamp":"$time_iso8601",'
        '"client_ip":"$proxy_add_x_forwarded_for",'
        '"remote_addr":"$remote_addr",'
        '"status":"$status",'
        '"method":"$request_method",'
        '"url":"$request_uri",'
        '"user_agent":"$http_user_agent"'
        '}';

    access_log /var/log/nginx/access.log json_geo;
    ### 配置结束 ###

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;

    keepalive_timeout 65;

    types_hash_max_size 4096;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen 80;
        listen [::]:80;

        server_name _;
        root /usr/share/nginx/html;

        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;

        location = /404.html {}

        error_page 500 502 503 504 /50x.html;

        location = /50x.html {}
    }
}
```

---

说明

- `log_format json_geo`：定义 JSON 格式日志
- `escape=json`：保证 JSON 不被转义破坏
- `access_log`：指定使用该格式写入日志
- 日志内容包含：时间、IP、状态码、请求方法、URL、User-Agent

设置完成后，重启 Nginx 并验证

```
systemctl restart nginx
```

访问 Nginx 后查看日志效果（JSON 格式）：

```
tail -f /var/log/nginx/access.log
```

---

## 安装 Logstash 插件（解析 Nginx IP 地址）

### 安装 Logstash 插件（解析 Nginx IP 地址）

```
cd /usr/share/logstash/bin

./logstash-plugin install logstash-filter-geoip
./logstash-plugin install logstash-filter-mutate
./logstash-plugin install logstash-filter-useragent
```

---

### 放置 GeoLite2-City 数据库

```
ls /etc/logstash/GeoLite2-City.mmdb
```

该插件主要用于 IP 地址转城市信息，功能包括：

1. 将 IP 转换为经纬度
2. 将 IP 转换为具体城市（如北京、巴黎等）

---

## 编写 Logstash Pipeline（采集 Nginx 日志到 Elasticsearch）

vim /etc/logstash/conf.d/nginx.conf

```
input {
  file {
    path => "/var/log/nginx/access.log"
    start_position => "beginning"
  }
}

filter {

  # 先尝试解析 JSON
  json {
    source => "message"
    skip_on_invalid_json => true
    tag_on_failure => ["_jsonparsefailure"]
    remove_field => ["tags"]
  }

  # 如果 JSON 解析失败，则走 grok 解析
  if "_jsonparsefailure" in [tags] {

    mutate {
      remove_tag => ["_jsonparsefailure"]
    }

    grok {
      match => {
        "message" => "%{IPORHOST:remote_addr} - %{USER:remote_user} \[%{HTTPDATE:time}\] \"%{WORD:method} %{NOTSPACE:url} HTTP/%{NUMBER:http_version}\" %{NUMBER:status} %{NUMBER:body_bytes_sent} \"%{NOTSPACE:referrer}\" \"%{DATA:user_agent}\" \"%{NOTSPACE:forwarded_for}\""
      }
    }

    date {
      match => ["time", "dd/MMM/yyyy:HH:mm:ss Z"]
      target => "@timestamp"
      timezone => "Asia/Shanghai"
    }

    mutate {
      add_field => { "client_ip" => "%{remote_addr}" }
    }

  } else {

    # JSON 格式时间处理
    date {
      match => ["@timestamp", "ISO8601"]
      target => "@timestamp"
      timezone => "Asia/Shanghai"
    }

    if (![client_ip] or [client_ip] == "") and [remote_addr] {
      mutate {
        replace => { "client_ip" => "%{remote_addr}" }
      }
    }
  }

  # 统一处理 real_ip
  if [client_ip] {
    if [client_ip] =~ /,/ {
      mutate {
        split => { "client_ip" => "," }
        add_field => { "real_ip" => "%{[client_ip][0]}" }
      }
    } else {
      mutate {
        add_field => { "real_ip" => "%{client_ip}" }
      }
    }
  }

  # GeoIP 解析（过滤内网IP）
  if [real_ip] and
     [real_ip] !~ /^%{/ and
     [real_ip] !~ /^(127\.0\.0\.1|::1|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.)/ {

    geoip {
      source => "real_ip"
      target => "geoip"
      database => "/etc/logstash/GeoLite2-City.mmdb"
      fields => ["country_name", "region_name", "city_name", "location"]
    }
  }

  # 字段类型转换
  mutate {
    convert => {
      "status" => "integer"
    }
  }

  # 清理异常字段
  if [real_ip] =~ /^%{/ {
    mutate { remove_field => ["real_ip"] }
  }

  if [client_ip] =~ /^%{/ {
    mutate { remove_field => ["client_ip"] }
  }

  mutate {
    remove_tag => ["_dateparsefailure", "_geoip_lookup_failure", "_jsonparsefailure"]
  }
}

output {

  elasticsearch {
    hosts => ["http://192.168.88.212:9200"]
    index => "nginx-%{+YYYY.MM.dd}"
  }

  stdout {
    codec => rubydebug
  }
}
```

配置完成后，重新启动logstash采集，查看效果

grok负责日志解析等操作，mutate负责标签增删改

返回kibana，创建数据视图

删除之前的视图，避免对我们项目产生影响

![[2f90580eb2.png]]

![[fc69553c1c.png]]

后续还可以添加一些图形，项自最终展示效果：

![[3d6fbd71ec.png]]

# 七、扩展：Filebeat

Filebeat 作用

Filebeat 与 Logstash 基本等价（用于日志采集链路中的数据收集）。

---

ELK 架构说明

- **ELK** = Elasticsearch + Logstash + Kibana

---

EFK 架构说明

- **EFK** = Elasticsearch + Filebeat + Kibana

---

EFLK 架构说明

- **EFLK** = Elasticsearch + Filebeat + Logstash + Kibana

---

说明

由于 Logstash 消耗内存等资源较大，如果在每一台需要采集日志的服务器上都部署 Logstash，会导致服务器压力变大，因此需要使用更轻量级的日志采集工具，提高效率并节省资源。

![[4829541917.png]]

Beats 简介

- Beats 是轻量级的日志收集与处理工具，占用资源少。
- Packetbeat：网络数据（收集网络流量数据）
- Metricbeat：指标（收集系统、进程和文件系统级别的 CPU 和内存使用情况等数据）
- Filebeat：文件（收集日志文件数据）
- Winlogbeat：Windows 事件日志（收集 Windows 事件日志数据）
- Auditbeat：审计数据（收集审计日志）
- Heartbeat：运行时间监控（收集系统运行时间的数据）

我们主要是收集日志信息，所以只讨论 Filebeat。

Filebeat 可以直接将采集的日志数据传输给 ES 集群（EFK），也可以发送给 Logstash（5044 端口接收）。

![[05fa968c5c.png]]

## filebeat收集日志直接传输给ES集群

---

第1步：下载并安装 Filebeat

（再开一台虚拟机 vm4 模拟 Filebeat，内存 1G 即可）

下载地址：[https://www.elastic.co/cn/beats/filebeat](https://www.elastic.co/cn/beats/filebeat)

```
[root@vm4 ~]# rpm -ivh filebeat-8.16.0-x86_64.rpm
```

---

第2步：配置 Filebeat 收集日志

```
filebeat.inputs:
  - type: filestream
    id: custom-logs
    enabled: true
    paths:
      - /var/log/*.log

# 关闭所有可能自动设置数据流的模块
filebeat.config.modules:
  enabled: false

# 彻底禁用模板和 ILM

# 禁用内置模板
setup.template.enabled: false
setup.template.overwrite: true

# 禁用 ILM
setup.ilm.enabled: false
setup.ilm.rollover_alias: ""
setup.ilm.pattern: ""
setup.ilm.policy_name: ""

# Elasticsearch 输出
output.elasticsearch:
  hosts: ["http://192.168.88.212:9200"]

  # 使用与 Filebeat 不同的索引名前缀，避免触发数据流机制
  index: "filebeat1-%{+yyyy.MM.dd}"

  # 显式禁用 ILM
  ilm.enabled: false

# 禁用任何自动索引设置
indices:
  - index: "filebeat1-%{+yyyy.MM.dd}"
    lifecycle:
      enabled: false
    name: ""
    data_stream:
      enabled: false
```

第3步：启动服务

```
[root@vm4 ~]# systemctl start filebeat
[root@vm4 ~]# systemctl enable filebeat
```

## filebeat 传输给 logstash

ELFK  
作用：  
① filebeat 负责日志采集  
② logstash 负责接收 filebeat 采集到的日志，然后进行过滤处理等操作 => ES 集群

---

第1步：在 logstash 上进行配置

开放 5044 端口给 filebeat 连接，并重启 logstash 服务（5044：logstash 默认端口）

filebeat 可以把日志发送到 logstash 节点对应的 5044 端口，这样 logstash 就可以获取到 filebeat 采集的日志信息

```
[root@vm3 ~]# pkill java
```

```
[root@vm3 ~]# vim /etc/logstash/conf.d/filebeat.conf

input {
  beats {
    port => 5044
  }
}

# 如需设置时区，在此处添加过滤器
filter {
  # 创建一个具有上海时区的时间戳字段供索引使用
  ruby {
    code => "event.set('indexDate', Time.now.getlocal('+08:00').strftime('%Y.%m.%d'))"
  }
}

output {
  elasticsearch {
    hosts => ["192.168.88.212:9200"]
    index => "filebeat2-%{indexDate}"
  }

  stdout {
  }
}
```

```
[root@vm3 ~]# cd /usr/share/logstash/bin/

# 如果前面有使用后台跑过 logstash 实例的请 kill 掉先
[root@vm3 bin]# pkill java
[root@vm3 bin]# ./logstash --path.settings /etc/logstash/ -r -f /etc/logstash/conf.d/filebeat.conf
```

注意：后期需要后台运行，可以使用nohup+&后台运行符

第2步：配置 filebeat 收集日志

```
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/*.log

filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false

# 禁用模板设置，避免数据流问题
setup.template.enabled: false

# 禁用 kibana 自动设置
setup.kibana.enabled: false

output.logstash:
  # 这两句非常重要，表示日志输出给 logstash
  hosts: ["192.168.88.213:5044"]

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
```

第3步：启动服务

```
[root@vm4 ~]# systemctl stop filebeat
[root@vm4 ~]# systemctl start filebeat
```

---

第5步：去 cerebro 上验证

![[b9bdb3a92b.png]]

第5步:在kibana创建索引模式(过程省略，参考上的笔记操作),然后点发现验证

![[11cc6f7676.png]]

## filebeat 收集 nginx 日志

---

### 1、在 filebeat 服务器上安装 nginx 并启动服务

（模拟产生日志，实际生产环境应在 nginx 服务器上部署 filebeat）

```
[root@vm4 ~]# yum install epel-release -y
[root@vm4 ~]# yum install nginx -y
[root@vm4 ~]# systemctl restart nginx
[root@vm4 ~]# systemctl enable nginx
[root@vm4 ~]# echo 'filebeat server nginx' > /usr/share/nginx/html/index.html
```

---

### 2、修改 filebeat 配置文件并重启服务

```
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      # 将 nginx 日志路径单独指定
      - /var/log/nginx/access.log

filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false

setup.template.settings:
  index.number_of_shards: 1

setup.kibana:

output.logstash:
  hosts: ["192.168.88.213:5044"]

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
```

```
[root@vm4 ~]# systemctl stop filebeat
[root@vm4 ~]# systemctl start filebeat
```

---

### 3、验证

在 kibana 或 es-head 上查询（建议使用 kibana，显示更详细）