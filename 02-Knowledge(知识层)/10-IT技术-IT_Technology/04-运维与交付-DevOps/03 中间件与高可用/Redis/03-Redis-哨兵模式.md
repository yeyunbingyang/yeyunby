# 一、Redis 哨兵概述

主从切换技术的方法是：当主服务器宕机后，需要手动将一台从服务器切换为主服务器，这种方式需要人工干预，费时费力，并且会导致一段时间服务不可用，因此不推荐。在实际生产中，通常优先使用哨兵模式。

哨兵作用：就是当主服务器岩机后，自动把从服务器升级为主服务器过程。（健康检查、故障切换）

---

## 1、什么是哨兵

哨兵模式是一种特殊模式。Redis 提供了哨兵相关命令，哨兵是一个独立运行的进程。

其原理是：哨兵通过发送命令并等待 Redis 服务器响应，从而对多个 Redis 实例进行监控。

![[9d0fcf4ebd.png]]

## 2、哨兵的作用

哨兵在 Redis 中有两个主要作用：

1. **监控作用**

- 通过发送命令，让 Redis 服务器返回其运行状态，包括主服务器和从服务器的状态。

2. **故障转移（Failover）作用**

- 当哨兵监测到 Master 宕机，会自动将某个 Slave 切换成 Master。
- 然后通过发布/订阅机制通知其他从服务器修改配置，实现切换主机。

---

**多哨兵模式**

- 单个哨兵进程监控 Redis 可能出现误判，为此可部署多个哨兵进程进行监控。
- 哨兵之间也会互相监控，从而形成多哨兵模式，提高可靠性。

---

**故障切换（Failover）过程描述**

1. 假设 Master 宕机，哨兵 1 首先检测到异常，它主观认为 Master 不可用，这个状态称为 **主观下线（Subjective Down, SDOWN）**。
2. 后续其他哨兵也检测到 Master 不可用，当达到一定数量时，哨兵之间开始 **投票**。
3. 投票结果由某个哨兵发起 **Failover 操作**：选举一个 Slave 升级为 Master。
4. 切换完成后，通过发布/订阅机制通知其他哨兵，使它们监控的从服务器也完成主从切换，这个状态称为 **客观下线（Objective Down, ODOWN）**。
5. 对客户端而言，整个切换过程是透明的，无需人工干预。

## 3、前期准备

为了演示哨兵模式，需要配置 **1 主 2 从 + 3 个哨兵** 的 Redis 环境。

|   |   |   |   |
|---|---|---|---|
|服务类型|是否主服务器|IP 地址|端口|
|Redis|是|192.168.88.111|6379|
|Redis|否|192.168.88.112|6379|
|Redis|否|192.168.88.113|6379|
|Sentinel|—|192.168.88.111|26379|
|Sentinel|—|192.168.88.112|26379|
|Sentinel|—|192.168.88.113|26379|

说明：哨兵服务可以与 Redis 服务同机部署，也可以单独部署。每个哨兵监控 Master 的状态并参与故障转移投票。

![[bab20dfcf5.png]]

特别注意：使用Redis哨兵模式，最少需要3个节点（一主多从结构）

# 二、Redis 主从复制搭建

---

## 1、Redis 主从配置

### ① 安装 Redis

```
# 安装 wget
dnf install wget -y

# 下载 Redis 7.4.0 安装包
wget https://download.redis.io/releases/redis-7.4.0.tar.gz

# 解压并进入目录
tar -zxvf redis-7.4.0.tar.gz
cd redis-7.4.0

# 编译安装
make
make PREFIX=/usr/local/redis install
```

### ②redis01/redis02/redis03修改配置

```
# redis01 / redis02 / redis03 修改配置

sudo mkdir -p /usr/local/redis/conf
sudo cp redis.conf /usr/local/redis/conf/

# 修改配置
sudo vim /usr/local/redis/conf/redis.conf
```

```
# 88 行
bind 127.0.0.1 -::1
--> bind 0.0.0.0

# 1050 行
# requirepass foobared
--> requirepass 123

# 310 行
daemonize no
--> daemonize yes
```

```
# 添加 redis 到环境变量
sudo vim /etc/profile

export PATH="$PATH:/usr/local/redis/bin"
source /etc/profile
```

```
# 设置内存分配策略
sudo vim /etc/sysctl.conf

vm.overcommit_memory = 1
sysctl -p
```

### ③启动

```
sudo vim /etc/systemd/system/redis.service

[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/conf/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

```
# 启动 Redis
systemctl start redis
```

```
# 添加 Redis 到环境变量
sudo vim /etc/profile

export PATH="$PATH:/usr/local/redis/bin"
source /etc/profile
```

```
# 设置内存分配策略
sudo vim /etc/sysctl.conf

vm.overcommit_memory = 1
sysctl -p
```

使用info命令，查看一下slave主机的状态：

![[73aec40885.png]]

我们可以看到，Redis 当前角色是 **master**。

**Master 主节点配置：**

```
bind 0.0.0.0
# 允许所有 IP 连接

protected-mode no
# 禁用保护模式（确保访问受防火墙控制）

requirepass 123
# 设置访问密码

masterauth 123
# 从节点连接主节点时使用的认证密码
```

**说明：**

- `protected-mode` 默认只允许 `127.0.0.1` 访问，在主从、哨兵、集群模式中必须关闭。

## 2、配置slave

和上面配置master一样，我们需要修改端口号和pid文件，在修改完之后，我们有两种方法配置从服务。

### ①在配置文件中配置从服务

```
replicaof 192.168.88.111 6379
```

### ② 配置从服务器连接主服务器

我们可以在配置文件中直接修改slaveof属性，我们直接配置主服务器的IP地址和端口号，如果这里主服务器有配置密码。

可以通过配置masterauth来设置链接密码：

```

# 如果主服务器设置了 requirepass，需要在从服务器配置 masterauth
masterauth 123
```

---

### ③ 启动 Redis 服务

```
# 创建 systemd 服务文件
sudo vim /etc/systemd/system/redis.service
```

```
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/conf/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

```
# 启动服务
systemctl start redis

# 将 redis 添加到环境变量
sudo vim /etc/profile
export PATH="$PATH:/usr/local/redis/bin"
source /etc/profile

# 设置内存过量分配策略
sudo vim /etc/sysctl.conf
vm.overcommit_memory = 1
sysctl -p
```

---

### ④ 查看从服务器状态

```
# 连接从服务器，执行 info replication
# 关键字段
# Replication role: slave
# master_host: 127.0.0.1
# master_port: 6379
# master_link_status: up
# slave_repl_offset: 71
# slave_read_only: 1
```

- 从服务器现在处于 **slave** 角色，连接主服务器 6379。

---

### ⑤ 查看主服务器状态

```
# 连接主服务器，执行 info replication
# 关键字段
# Replication role: master
# connected_slaves: 2
# slave0: ip=192.168.88.112, port=6379, state=online, offset=785, lag=0
# slave1: ip=192.168.88.113, port=6379, state=online, offset=785, lag=0
# master_repl_offset: 785
# repl_backlog_active: 1
# repl_backlog_size: 1048576
```

- 主服务器连接了两个从服务器，并维持主从复制状态。

---

## 3、常见问题！！！

```
# Redis01 / Redis02 / Redis03 => redis.conf

bind 0.0.0.0

protected-mode no
# 哨兵模式必须关闭 protected-mode，允许外部网络连接 Redis 服务
```

---

## 4、核心代码归纳

**Master：**

```
wget https://download.redis.io/releases/redis-7.4.0.tar.gz

tar -zxvf redis-7.4.0.tar.gz
cd redis-7.4.0

make
make PREFIX=/usr/local/redis install

mkdir -p /usr/local/redis/conf
cp redis.conf /usr/local/redis/conf

# 修改配置
bind 0.0.0.0
daemonize yes
protected-mode no
# 允许所有 IP 连接
# 后台运行
# 关闭安全模式

requirepass 123
masterauth 123
# 从服务器连接需要的密码
# 主从认证密码

# 内存分配策略
sudo vim /etc/sysctl.conf
vm.overcommit_memory = 1
sysctl -p
```

---

**Slave：**

```
wget https://download.redis.io/releases/redis-7.4.0.tar.gz

tar -zxvf redis-7.4.0.tar.gz
cd redis-7.4.0

make
make PREFIX=/usr/local/redis install

mkdir -p /usr/local/redis/conf
cp redis.conf /usr/local/redis/conf

# 修改配置
bind 0.0.0.0
daemonize yes
protected-mode no
# 允许所有 IP 连接
# 后台运行
# 关闭安全模式

replicaof 192.168.88.111 6379
requirepass 123
# 配置连接 master 主服务器

masterauth 123
# 从服务器连接主节点需要的密码

# 内存分配策略
sudo vim /etc/sysctl.conf
vm.overcommit_memory = 1
sysctl -p
```

# 三、Sentinel 哨兵

## 1、配置 Sentinel 端口

在 `sentinel.conf` 配置文件中，通过 `port` 属性设置 Sentinel 端口。一般至少部署 3 个哨兵进行监控。

```
cd /root/redis-7.4.0

cp sentinel.conf /usr/local/redis/conf/
vim /usr/local/redis/conf/sentinel.conf
```

```
protected-mode no
port 26379
daemonize no
```

**说明：**

- `daemonize no` 仅用于测试环境
- 生产环境需要设置为：

```
daemonize yes
```

## 2、配置主服务器的IP和端口

（redis01/redis02/redis03都要配置）：  
[https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)

```
# sentinel monitor <master-name> <ip> <redis-port> <quorum>

# Tells Sentinel to monitor this master, and to consider it in o_Down
# (objectively Down) state only if at least <quorum> sentinels agree.

# Note that whatever is the oDown quorum, a Sentinel will require to
# be elected by the majority of the known Sentinels in order to
# start a failover, so no failover can be performed in minority.

# slaves are auto-discovered, so you don't need to specify slaves in
# any way. Sentinel itself will rewrite this configuration file adding
# the slaves using additional configuration options.

# Also note that the configuration file is rewritten when a
# slave is promoted to master.

# Note: master name should not include special characters or spaces.
# The valid charset is A-z 0-9 and the three characters ".-"

sentinel monitor mymaster 192.168.88.111 6379 2
sentinel auth-pass mymaster 123
```

注：

- 2权值/阀值，代表至少需要2个哨兵确认才能客观下线。
- 原理：首先某个哨兵发现master主节点无法连接（无法响应），则会标记为主观下线；如果超过2台哨兵确认master节点故障，则标记为客观下线，并触发故障转移。
- 高可用：在一个集群中（最少2台及以上节点），某个节点出现故障，集群依然可以对外提供相关服务（可用）。
- 故障转移：failover，当主节点宕机，从节点升级为主节点。
- 高可用往往包含健康检查以及故障转移等特性。

## 3、启动所有的Sentinel进程

```
[root@yunwei ~] # redis-sentinel /usr/local/redis/conf/sentinel.conf
```

redis 和 sentinel 是不同的，两者相互独立。redis 有一个进程 redis-server，sentinel 有一个进程 redis-sentinel。

## 4、手工关闭 master

新创建一个窗口，针对 redis01，然后手工关闭 redis，模拟 redis 主节点故障。

```
pkill redis-server
```

我们手动关闭 Master 之后，sentinel 在监听到 master 确实断线后，将会开始计算权值，然后重新分配主服务器。

```
128799:x 29 May 12:08:35.657# +failover-end master mymaster 192.168.88.111 6379
128799:x 29 May 12:08:35.657# +switch-master mymaster 192.168.88.111 6379 192.168.88.113 6379
```

查看状态，发现已经发生故障转移，88.113 升级为主节点。

一旦 failover 发生时，系统会自动调整两个文件：

- redis.conf：更改主节点信息
- sentinel.conf：最末端会写入一些选举等信息

![[f1edf91f98.png]]

## 5、重连 master

大家可能会好奇，如果 master 重连之后，会不会抢回属于他的位置，答案是否定的。就比如你被一个小弟抢了你老大的位置，他不会再把位置还给你。因此当 master 恢复之后，只能作为从节点（slave）加入集群。

## 6、Sentinel 小结

① Master 状态监测

② 如果 Master 异常，先主观下线；当超过设定节点数（quorum）后，则客观下线。随后进行 Master-Slave 转换，将其中一个 Slave 提升为新的 Master，将原来的 Master 变为 Slave

③ Master-Slave 切换后，master_redis.conf、slave_redis.conf 和 sentinel.conf 的内容都会发生改变：

- master_redis.conf 中会新增一行 slaveof 配置
- sentinel.conf 的监控目标会随之发生变化

哨兵模式：就是在主从架构的基础上，增加了一个failover故障切换功能，可以在秒级实现故障转移。从而实现Redis高可用架构。

![[407229c06e.png]]