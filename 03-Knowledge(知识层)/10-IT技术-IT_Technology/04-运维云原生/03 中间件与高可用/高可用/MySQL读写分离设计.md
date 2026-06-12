# 学习目标

1. 能够理解读写分离的目的
2. 能够描述读写分离的常见实现方式
3. 能够通过项目框架配置文件实现读写分离
4. 能够通过中间件实现读写分离（学习的重点）

# 一、MySQL 读写分离

## 1. 业务背景描述

- 时间：2016.6-2017.9
- 发布产品类型：互联网动态站点商城
- 用户数量：2000-4000（用户量猛增了4倍）
- PV：8000-50000（24小时访问次数总和）
- DAU：1500（每日活跃用户数）

之前是单台 MySQL 提供服务，后来使用多台 MySQL 数据库服务器，降低单台压力，实现集群架构的稳定性和高可用性，并保证数据的一致性和完整性（replication）。

通过业务比对和分析发现，随着用户活跃增多，读取数据的请求量增加，因此重点解决读取数据的压力。

## 2、模拟运维设计方案

![[附件/2827aa7699.png]]

根据以上业务需求，在之前业务架构的基础上实现数据的读写分离。

![[附件/adfe14884e.png]]

![[附件/f4b7ba702a.png]]说明：

实现MySQL主从架构=>解决单点故障问题

引入MyCAT不仅可以实现高可用，MyCAT软件还能实现读写分离技术（master既可以承担写操作也可以承担一部分读操作，slave从服务器可以承担部分读操作）

# 二、MySQL 读写分离介绍

## 1. 什么是读写分离

- 读写分离：读写操作分发到不同的服务器，读操作分发到对应的服务器（slave），写操作分发到对应的服务器（master）。
- **Master（主节点）**、**Slave（从节点）**

- 写操作 => 只能在 master 节点执行（主从架构中，只有主节点能实现写入）
- 读操作 => 可以在 master 主节点，也可以在 slave 从节点（由调度算法决定的，默认肯定是slave从节点）

- 在生产环境中，一般配置一主多从架构：

- 主节点只负责写入操作
- 从节点专门负责读操作

## 2. 读写分离的目的

- 将读写业务分配到不同的服务器上，让服务器专注于特定操作，无需不断切换工作模式，提高工作效率（写主服务器，读从服务器）
- 降低主服务器压力，在正常业务中，读操作通常比写操作多，比例大约写 3/7，读 7/10
- 读写分离的架构优势：

1. **M-S 架构**：读写必须分离，否则业务可能不可用
2. **M-M 架构**：虽然可以随意读写，但将特定操作交给特定服务器，工作效率更高【多主】

## 3. 读写分离的实现基础和原理

- **实现基础**：通过主从复制机制实现数据的一致性和完整性
- **原理**：

- SQL 语句按类型分配 - 把用户执行的sgl语句分为读操作以及写操作

- **Master（主数据库）**：响应事务性操作（`INSERT`、`UPDATE`、`DELETE`、`CREATE`、`DROP`）
- **Slave（从数据库）**：响应 `SELECT` 非事务性操作

- 通过主从复制将 Master 上的事务性操作同步到 Slave 数据库
- 没有主从复制，就无法实现业务上的读写分离

## 4. 读写分离常见的实现方式

### ① 业务代码的读写分离（了解）

- 需要在业务代码中判断数据操作是读还是写

- 读操作连接从数据库
- 写操作连接主数据库

- 以 MySQL01/MySQL02 为例（LNMP 环境），在 PHP 代码中实现读写分离
- 在 ThinkPHP 6.0 代码端对数据库操作进行判断，例如：

增加：

```
mysql> INSERT INTO 数据表
VALUES (字段值, 字段值, ...);
```

删除：

```
mysql> DELETE FROM 数据表 WHERE 字段=字段值;

mysql> DELETE FROM 数据表
WHERE 字段 IN (字段值1, 字段值2, ...);
```

修改：

```
mysql> UPDATE 数据表
SET 字段=字段的值
WHERE 字段=字段值;
```

查询：

```
mysql> SELECT * /*或字段列表*/
FROM 数据表;
```

- 如果 `INSERT`/`UPDATE`/`DELETE` 操作，自动连接 **Master 主数据库**；
- 如果 `SELECT` 操作，自动连接 **Slave 从数据库**。

### ② 中间件代理方式的读写分离

- 在业务代码中，数据库操作不直接连接数据库，而是先请求到 **中间件服务器（代理）**
- 由代理服务器判断：

- 读操作 => 转发到从数据库
- 写操作 => 转发到主数据库

|   |   |
|---|---|
|名称|描述|
|**MySQL Proxy**|MySQL 官方测试版，不再维护|
|**Atlas**|奇虎360 基于 MySQL Proxy [文档链接](https://github.com/Qihoo360/Atlas/blob/master/README_ZH.md)|
|**DBProxy**|美团点评|
|**Amoeba**|早期阿里巴巴|
|**Cobar**|阿里巴巴|
|**MyCat**|基于阿里开源的 Cobar|
|**Kingshard**|Go 语言开发 [文档链接](https://github.com/flike/kingshard)|

也就是如下图所示架构

![[附件/b0dec3ef24.png]]

问：如何选择？

① **业务上实现**

- 优点：实现方便，成本低
- 注意：如果开发框架不支持分布式数据库部署模式，业务 SQL 可能需要修改，需要改代码（程序猿操作）

② **中间件代理服务器**

- 优点：适合管理更多的数据库服务器集群
- 功能：可以查看服务器是否可用，不仅实现读写分离，还可以实现分库、分表操作（运维操作）

# 三、MySQL 读写分离的具体实现

**前提条件**：

- MyCAT2本身内存不得低于 6GB
- MySQL5 配合 MyCAT 比较消耗资源，两台 MySQL 服务器内存不得低于 4GB，否则配置完成后会报错
- MySQL8 配合 MyCAT 比较消耗资源，两台 MySQL 服务器内存不得低于 6GB，否则配置完成后会报错

## 1. 配置主从

- **主从复制原理**：

- 主服务器开启 **bin-log**（记录写操作）
- 从服务器获取主服务器的 bin-log 并写入 **relay-log**
- 从服务器通过异步线程对 relay-log 进行重放操作

- **流程**：

1. **IO 线程**：从主服务器拷贝 bin-log 日志 => 写入从服务器的 relay-log
2. **SQL 线程**：根据 relay-log 的变化，自动执行复制过来的 DML 语句

- **概念对应**：

- 主服务器：**bin-log**
- 从服务器：**relay-log**

- **操作流程**：

1. DML 操作 => 执行在 MASTER SQL => 记录在 bin-log
2. SLAVE SQL 监听 MASTER bin-log 日志变化
3. 一旦监测到主服务器发生变化，通过网络 IO 线程复制到 SLAVE，从服务器的 relay-log 中
4. SLAVE 使用 SQL 线程重演 MASTER SQL 操作

准备 mysql02 服务器（192.168.88.109）

```
hostnamectl set-hostname mysql02.itcast.cn
```

绑定 IP 与主机、关闭防火墙与 SELINUX、配置时间同步、安装必备软件（wget、vim、rsync、net-tools 等）。

配置MySQL主从

master.sh ：

```
# vim master.sh
#!/bin/bash

echo "正在安装依赖软件.."
yum install libaio -y

echo "执行解压缩操作.."
tar -xf mysql-5.7.31-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.31-linux-glibc2.12-x86_64 /usr/local/mysql
useradd -r -s /sbin/nologin mysql

rm -rf /etc/my.cnf

echo "进入mysql目录，对其进行初始化操作..."
cd /usr/local/mysql
mkdir mysql-files
chown mysql:mysql mysql-files
chmod 750 mysql-files

bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql 2>&1 | tee /tmp/mysqld.log | grep password | awk '{print $NF}' > /root/mysql_temp_password.txt

echo "设置my.cnf与mysqld.service文件"
cat > /etc/my.cnf <<EOF
[mysqld]
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
socket=/tmp/mysql.sock
port=3306
log-error=/usr/local/mysql/data/mysql.err
log-bin=/usr/local/mysql/data/binlog
server-id=10
character_set_server=utf8mb4
gtid-mode=on
log-slave-updates=1
enforce-gtid-consistency
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
EOF

bin/mysql_ssl_rsa_setup --datadir=/usr/local/mysql/data

cat <<EOF > /etc/systemd/system/mysqld.service
[Unit]
Description=MySQL Server
After=network.target
After=syslog.target

[Service]
User=mysql
Group=mysql
ExecStart=/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf
LimitNOFILE=5000
PrivateTmp=false

[Install]
WantedBy=multi-user.target
EOF

echo "正在刷新后台服务，然后启动mysqld.."
systemctl daemon-reload
systemctl start mysqld
systemctl enable mysqld

sleep 5

echo 'export PATH=$PATH:/usr/local/mysql/bin' >> /etc/profile
source /etc/profile

ln -s /lib64/libncurses.so.6 /lib64/libncurses.so.5
ln -s /lib64/libtinfo.so.6 /lib64/libtinfo.so.5

echo "正在重置mysql管理员密码.."
cd /usr/local/mysql
temp_password=$(cat /root/mysql_temp_password.txt)
bin/mysqladmin -S /tmp/mysql.sock -uroot -p"$temp_password" password '123456'

echo "MySQL安装成功，软件安装路径：/usr/local/mysql，数据库初始密码：123456！"

# source master.sh
```

slave.sh (重点):

slave.sh ：

```
#!/bin/bash

echo "正在安装依赖软件.."
yum install -y libaio

echo "解压MySQL二进制文件.."
tar -xf mysql-5.7.31-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.31-linux-glibc2.12-x86_64 /usr/local/mysql

echo "创建MySQL系统用户..."
useradd -r -s /sbin/nologin mysql

rm -rf /etc/my.cnf

echo "准备目录权限.."
cd /usr/local/mysql
mkdir -p mysql-files
chown mysql:mysql mysql-files
chmod 750 mysql-files

# 注意：不进行初始化！
# bin/mysqld --initialize

echo "设置my.cnf和mysqld.service文件..."
cat > /etc/my.cnf <<EOF
[mysqld]
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
socket=/tmp/mysql.sock
port=3306
log-error=/usr/local/mysql/data/mysql.err
log-bin=/usr/local/mysql/data/binlog
server-id=20
character_set_server=utf8mb4
gtid-mode=on
log-slave-updates=1
enforce-gtid-consistency
read_only=1
relay_log=/usr/local/mysql/data/relaylog
log_slave_updates=1
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
EOF

# 生成SSL（可选）
# bin/mysql_ssl_rsa_setup --datadir=/usr/local/mysql/data

cat <<EOF > /etc/systemd/system/mysqld.service
[Unit]
Description=MySQL Server
After=network.target
After=syslog.target

[Service]
User=mysql
Group=mysql
ExecStart=/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf
LimitNOFILE=5000
PrivateTmp=false

[Install]
WantedBy=multi-user.target
EOF

echo "刷新服务.."
systemctl daemon-reload

echo "添加到开机启动项.."
systemctl enable mysqld

echo 'export PATH=$PATH:/usr/local/mysql/bin' >> /etc/profile
source /etc/profile

ln -s /lib64/libncurses.so.6 /lib64/libncurses.so.5
ln -s /lib64/libtinfo.so.6 /lib64/libtinfo.so.5

echo "MySQL从服务器环境已配置完成。请确认数据目录已从主库复制或使用备份恢复后再启动服务。"

# source slave.sh
```

主从配置：

```
# master服务器操作
systemctl stop mysqld
rm -rf /usr/local/mysql/data/auto.cnf
rsync -av /usr/local/mysql/data/* root@192.168.88.109:/usr/local/mysql/data/
systemctl start mysqld
```

```
-- master数据库中执行
CREATE USER 'slave'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%';
```

```
# slave服务器操作
systemctl start mysqld
```

```
-- slave数据库中执行
CHANGE MASTER TO
MASTER_HOST='192.168.88.106',
MASTER_PORT=3306,
MASTER_USER='slave',
MASTER_PASSWORD='123',
MASTER_AUTO_POSITION=1;

START SLAVE;
SHOW SLAVE STATUS\G
```

![[附件/173c2bc2dc.png]]

## 2、代码层级的读写分离（了解）

Java ShardingSphere-JDBC

- 筛选：

- `insert / update / delete` 操作 => 传输到主服务器
- `select` 操作 => 传输到从服务器

NiuShop 底层采用 ThinkPHP 框架

```
vim database.php

return [
    'type'        => 'mysql',
    'hostname'    => '主IP,从IP',  // 设置服务器列表，逗号隔开，第1台默认为主服务器
    'deploy'      => 1,            // 开启分布式数据库（多台数据库，默认为0）
    'rw_separate' => true,         // 开启读写分离模式（主写，从读）
];
```

测试：可以 down 掉主库，看从库是否可以访问；在 NiuShop 配置中，如果 slave 宕机，master 仍可提供读服务。

## 3、MyCAT2 中间件（重点）

MyCAT一共有两个版本：MyCAT（支持MySQI5.7及以下版本）、MyCAT2（不仅支持MySQL5.7，还支持MySQL8.0等版本）

官方网址：[http://www.mycatone.top/](http://www.mycatone.top/)

![[附件/10adac9640.png]]

MyCAT2 是 Mycat 社区开发的一款分布式关系型数据库中间件。它支持分布式 SQL 查询，兼容 MySQL 通信协议，以 Java 生态支持多种后端数据库，通过数据分片提高数据查询处理能力。

MyCAT2 在架构中的定位：

- 位于应用服务器与数据库服务器之间（中间件层）
- 对上：对接应用（如 NiuShop、ThinkPHP）
- 对下：连接多个 MySQL 数据库（主从、分库分表）
- 作用：

- 实现读写分离
- 实现分库分表
- 屏蔽底层数据库复杂性
- 统一数据库访问入口

![[附件/fb7f612d07.png]]

特点：

a. **代码开源**

- 学习中间件技术、数据库技术，代码是必须具备的

b. **兼容 MySQL 语法的分布式查询引擎**

- 兼容 MySQL 语法
- 兼容 MySQL 值类型
- 使用基于规则优化与代价的优化器
- 拥有独立的物理执行引擎

c. **自定义功能算法开发**

- 分片算法、序列号算法、负载均衡算法等都可自定义加载
- 查询引擎可脱离网络框架运行

d. **自定义处理过程**

- 自研 DSL 操纵物理查询计划
- 支持 SQL 转发,支持缓存结果集

## 4、MyCAT2工作原理图

![[附件/98ad118576.png]]

**MyCAT 数据库中间件**

- 国内最活跃、性能最好的开源数据库中间件
- 官方网址：[http://www.mycatone.top/](http://www.mycatone.top/)
- 由于 MyCAT2 是用 **Java** 语言开发，必须在 **Java 运行环境** 下启动和操作

## 5、准备机器

- 建议配置：**4 核 CPU / 6GB 以上内存**，因为 MyCAT2 占用内存和 CPU 较大
- 更改 IP 地址以及 MAC 地址
- 绑定 IP 与 HOSTNAME 到 `/etc/hosts` 文件

```
192.168.88.10  nat nat.itcast.cn
192.168.88.20  dr dr.itcast.cn
192.168.88.101 server
192.168.88.102 agent1
192.168.88.103 grafana
192.168.88.104 web01 web01.itcast.cn
192.168.88.105 web02 web02.itcast.cn
192.168.88.106 mysq101 mysql01.itcast.cn
192.168.88.107 lb01 lb01.itcast.cn
192.168.88.108 lb02 lb02.itcast.cn
192.168.88.109 mysq102 mysq102.itcast.cn
192.168.88.110 mycat mycat.itcast.cn
```

- 配置时间同步，具体操作参考 **CentOS 9 时间同步文档**

**安装必备软件**

```
dnf install vim wget rsync net-tools -y
```

## 6、JDK 安装

- **Java** 是一种编程语言，类似还有 Python、Go、PHP 等
- **编译与运行**

- `javac`：编译 Java 代码生成字节码（机器码）
- `java`：运行编译好的字节码（JRE 环境）

- **JDK 与 JRE 区别**

- **JRE**（Java Runtime Environment）：Java 解析运行环境，只能运行已经编译好的 Java 程序
- **JDK**（Java Development Kit）：包含 JRE + 编译环境 `javac`，可编译并执行 Java 源代码
- **选择原则**：【公司服务器部署的java环境是jdk还是jre？】

- 服务器只运行编译好的 Java 程序 => 安装 JRE 即可
- 服务器需要编译源代码 => 安装 JDK

- **主流版本**

- **Oracle JDK**（原 Sun 公司，现 Oracle 收购）
- **OpenJDK**（完全免费的 JDK 环境）

- 下载链接：[Oracle JDK 8 下载](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

## 7、上传 MyCAT2 和 JDK 到 Linux

**第一步：解压安装 JDK**

```
tar xvf jdk-8u192-linux-x64.tar.gz
mkdir -p /usr/local/java
mv jdk1.8.0_192 /usr/local/java/
```

- 注：最终完整路径为 `/usr/local/java/jdk1.8.0_192`

**第二步：配置环境变量**

```
# 卸载系统自带 openjdk（可选）
rpm -e java-1.8.0-openjdk-headless-1.8.0.362.b09-4.el9.x86_64 --nodeps

# 编辑 profile 文件添加 JDK 路径
vim /etc/profile
export PATH=$PATH:/usr/local/java/jdk1.8.0_192/bin

# 生效配置
source /etc/profile
```

最终脚本：jdk.sh

```
#!/bin/bash

# 解压 JDK 并移动到 /usr/local/java
tar xvf jdk-8u192-linux-x64.tar.gz
mkdir -p /usr/local/java
mv jdk1.8.0_192 /usr/local/java/

# 卸载系统自带 openjdk（可选）
rpm -e java-1.8.0-openjdk-headless-1.8.0.362.b09-4.el9.x86_64 --nodeps

# 配置环境变量
echo 'export PATH=$PATH:/usr/local/java/jdk1.8.0_192/bin' >> /etc/profile
source /etc/profile
```

执行

```
source jdk.sh
```

## 8、MyCAT2 安装

- 下载地址：[MyCAT2 GitHub](https://github.com/MyCATApache/Mycat2)
- 可以直接使用提供的软件包，无需自行编译

**第一步：安装 MyCAT**

```
# 创建目录并上传软件包
mkdir mycat2
cd mycat2/

# 解压安装模板
unzip mycat2-install-template-1.21.zip

# 移动 MyCAT 到 /usr/local/
mv mycat /usr/local/

# 拷贝依赖 Jar 包
cp mycat2-1.21-release-jar-with-dependencies.jar /usr/local/mycat/lib/

# 进入 MyCAT 目录
cd /usr/local/mycat/
```

**第二步：设置数据源（前提：使用管理员账号）**

```
-- 在 mysql01 服务器上执行
CREATE USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL ON *.* TO 'root'@'%';
```

第二步：设置数据源

前提：使用管理员账号（mysql01 服务器）

```
mysql> CREATE USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123';
mysql> GRANT ALL ON *.* TO 'root'@'%';
```

配置数据源

```
cd conf/datasources

# 修改 MyCAT 自带的数据源配置
vim prototypeDs.datasource.json
```

```
{
  "dbType":"mysql",
  "idleTimeout":60000,
  "initsqls":[],
  "initsqlsGetConnection":true,
  "instanceType":"READ_WRITE",
  "maxCon":1000,
  "maxConnectTimeout":3000,
  "maxRetryCount":5,
  "minCon":1,
  "name":"prototypeDs",
  "password":"123",
  "type":"JDBC",
  "url":"jdbc:mysql://192.168.88.106:3306/mysql?useUnicode=true&serverTimezone=Asia/Shanghai&characterEncoding=UTF-8",
  "user":"root",
  "weight":0
}
```

需要修改位置：

1. `"password":"123"` => 连接 MySQL 的密码
2. `"url":"jdbc:mysql://192.168.88.106:3306/niushop?...` => 连接 MySQL 的地址和数据库
3. `"user":"root"` => 连接 MySQL 的账号

## 9、目录说明

```
bin   ：mycat 二进制文件目录
conf  ：配置文件目录
logs  ：日志目录（可查看错误日志）
```

## 10、启动 MyCAT2

默认不进行任何配置，MyCAT 也可以启动：

```
chmod +x /usr/local/mycat/bin/*

/usr/local/mycat/bin/mycat console

# 查看端口确认是否启动成功
ss -naltp | grep 8066
```

- 8066：MyCAT 客户端端口【web服务接口】
- 9066：MyCAT 管理端端口【查看集群信息】

如果启动不成功，报错：`Ignoring option MaxPermSize; support was removed in 8.0`

原因分析：因为系统不能够在规定时间内启动 MyCAT，可以设置启动等待时间延长（配置较低时）。部署好 MyCAT 之后，先启动一次确认是否能够正常启动，若正常则不需要修改。

```
# vim conf/wrapper.conf

wrapper.startup.timeout=300
wrapper.ping.timeout=120
```

常见错误就几种情况：

① 配置低，服务无法启动，报错：`Ignoring option MaxPermSize: support was removed in 8.0`

- 解决思路：增大内存或者调整配置文件中的启动超时时间

```
# vim conf/wrapper.conf

wrapper.startup.timeout=300   # 添加这一行
wrapper.ping.timeout=120      # 默认存在
```

② 数据源报 Access Denied

- 排查路径：`/usr/local/mycat/conf/datasources/prototypeDs.datasource.json`
- 常见原因：

- 账号密码不正确
- 连接地址不正确
- 账号没有权限

- 解决：严格按照数据源配置逐项检查

## 11、配置 MyCAT2（重点）

**第一步：进入数据源配置目录**

```
cd /usr/local/mycat/conf/datasources/
```

配置 `prototypeDs.datasource.json` 文件

```
{
  "dbType":"mysql",
  "idleTimeout":60000,
  "initsqls":[],
  "initsqlsGetConnection":true,
  "instanceType":"READ_WRITE",
  "maxCon":1000,
  "maxConnectTimeout":3000,
  "maxRetryCount":5,
  "minCon":1,
  "name":"prototypeDs",
  "password":"123",
  "type":"JDBC",
  "url":"jdbc:mysql://192.168.88.106:3306/mysql?useUnicode=true&serverTimezone=Asia/Shanghai&characterEncoding=UTF-8",
  "user":"root",
  "weight":0
}
```

**第二步：重新启动 MyCAT**

```
/usr/local/mycat/bin/mycat start
```

**第三步：DataGrip 连接 MyCAT，配置信息如下：**

mycat 服务器：

```
yum install mysql -y

mysql-server：服务器端mysql：客户端

安装客户端以后，我们就可以使用mysql命令

连接mysql客户端，mycat本身有密码，密码为123456，如果我们连接的mycat客户端，必须要使用这个密码

连接客户端
mysql -h127.0.0.1 -ur0ot -p123456 -P8066
```

端口：8066

密码保存在

![[附件/0b89e5e0dc.png]]

![[附件/3f75444054.png]]

默认账号：root  
默认密码：123456

补充说明

问题1：

```
/usr/local/mycat/bin/mycat console
```

没有任何反应？

答：  
① 可能是由于 JDK 没有安装或者配置没有立即生效，缺少 `source /etc/profile`，如果 MyCAT 找不到 JDK 也会出现无法启动的问题。  
② 可能安装异常，这种情况可以移除 `/usr/local/mycat` 文件夹，重新解压，重新配置。③ 可能后台 MyCAT 服务卡死，没有正常启动导致的。重启 Linux 操作系统后，往往可以解决。

问题2：  
MyCAT 启动成功，但是查看不到 8066 和 9066 端口，这种情况要学会查看报错日志。

```
tail -100 /usr/local/mycat/logs/wrapper.log
```

![[附件/5de015efce.png]]

第四步：创建 db1 数据库并设置数据源

为了让MyCAT可以识别到数据库，如果没有设置数据源，则MyCAT无法查看到指定数据库）

```
CREATE DATABASE db1 DEFAULT CHARSET=utf8;
```

创建完成后，系统会自动在 `/usr/local/mycat/conf/schemas` 目录下生成 `db1.schema.json`

MyCat 安全机制 只有暴漏连接的数据库源 才能看到对应数据库

```
ls -l /usr/local/mycat/conf/schemas/
-rw-r--r-- 1 root root 607 Nov 14 19:46 db1.schema.json
```

![[附件/a793d19d5b.png]]

编辑 schema.json 文件

```
vim /usr/local/mycat/conf/schemas/db1.schema.json
```

![[附件/d1d80e7997.png]]

![[附件/766f469279.png]]

通过配置文件连接到集群prototype、节点需要一个个添加

第五步：添加数据源

```
-- 创建主数据库连接（负责写操作）
/*+ mycat:createDatasource{
"name":"rwSepw",
"url":"jdbc:mysql://192.168.88.106:3306/db1?useSSL=false&characterEncoding=UTF-8&useJDBCCompliantTimezoneShift=true",
"user":"root",
"password":"123"
}*/;

-- 创建从数据库连接（负责读操作）
/*+ mycat:createDatasource{
"name":"rwSepr",
"url":"jdbc:mysql://192.168.88.109:3306/db1?useSSL=false&characterEncoding=UTF-8&useJDBCCompliantTimezoneShift=true",
"user":"root",
"password":"123"
}*/;

-- 查看数据源
/*+ mycat:showDatasources{} */;
```

![[附件/5fb23e31da.png]]

![[附件/245fb8732d.png]]

扩展：删除数据源操作（不需要操作）

```
/*+ mycat:dropDatasource{"name":"rwSepw"} */;
/*+ mycat:dropDatasource{"name":"rwSepr"} */;
```

第六步：添加数据集群（关键）

```
/*! mycat:createcluster{
"name":"prototype",
"masters":["rwSepw"],
"replicas":["rwSepr"]
} */;

/*+ mycat:showclusters{} */;
```

说明：

1. `/*! */` 语法：

- MySQL 兼容的注释语法。
- 注释中的内容会被 MySQL 服务器执行，但被其他数据库忽略。
- 在 MyCAT 中表示需要执行的管理命令，例如创建集群。
- 简单理解：`/*! */` 主要用于写操作。

2. `/*+ */` 语法：

- 通常用于查询提示（Query Hints）。
- 在 MyCAT 中用于执行查询类命令，如显示信息。
- 简单理解：`/*+ */` 主要用于读操作。

![[附件/48b04fb48b.png]]

扩展：删除数据集群（不需要操作）

```
/*+ mycat:dropcluster{"name":"prototype"} */ ;
```

第七步：启动MyCAT

```
shell > /usr/local/mycat/bin/mycat restart
```

通过查看端口或者进程的方式，确认是否启动：

![[附件/b99444b397.png]]

启动不了，一定要看错误日志：

1. 翻译错误
2. 养成看日志的习惯：自身存在日志看自身；自身不存在的看 `messages` 日志

```
cat /usr/local/mycat/logs/wrapper.log
```

配置完成服务启动不了，常见问题：

```
1. master 和 slave 没有对应用户给 MyCAT 操作的 user/password/host
2. 配置文件语法错误
3. wrapper.log 查看错误并解决
```

![[附件/acc253f900.png]]

2.配置主从数据库源

## 12、读写分离集群测试

**第一步：测试之前**

- 对 node6（mysql01）、node9（mysql02）、MyCAT 机器进行**快照**

**第二步：创建测试表**

```
-- 选择数据库并创建表
USE db1;

CREATE TABLE test_table (
    id INT AUTO_INCREMENT,
    hostname VARCHAR(255),
    PRIMARY KEY(id)
);
```

**第三步：插入数据与读取数据测试**

```
-- 插入数据（@@hostname 表示当前主机名）
INSERT INTO test_table(hostname) VALUES (@@hostname);

-- 查询数据
SELECT * FROM test_table;
```

- 注意：

- 一定要返回 mysql02 终端执行以下语句（不要在 MyCAT 中执行）
- 选择 db1 数据库，向 test_table 表插入一条数据（人为破坏主从结构）

```
USE db1;
INSERT INTO test_table(hostname) VALUES (@@hostname);
```

- 返回 MyCAT 再次查询，验证读写分离：

```
SELECT * FROM test_table;
```

- 结果说明：

- MyCAT 已经实现读写分离
- 默认采用轮询算法：一次访问 mysql01，一次访问 mysql02

常见问题：

1. 遇到问题不要紧张，翻译错误，看日志。如果实在翻译有问题，可以使用大模型读取错误或者日志的最后 50 行左右或具体报错的内容。
2. 注意事项：MyCAT、MySQL8 都属于高内存型应用。MyCAT（Java 开发）、MySQL8（不低于 6G 内存），如果 MyCAT、MySQL8 内存低于 6G，MyCAT 本身无法启动，Java 异常，端口 8066 打开，但就是连接不上！
3. MyCAT 与 mysql01、mysql02 数据不一致，比如 MyCAT 有一个 db1 数据库，但是 mysql01 和 mysql02 没有，就会导致异常，MyCAT 无法启动。

解决思路：

因为数据不一致，只能对 MyCAT 进行重置，清理一些文件：

```
cd /usr/local/mycat/conf
rm -rf clusters/prototype.cluster.json
rm -rf datasources/rwSep*
rm -rf schemas/db1.schema.json
```

删除完成后，重启 MyCAT。

## 13、Cluster 集群配置选项说明

```
vim /usr/local/mycat/conf/clusters/prototype.cluster.json
```

**readBalanceType：查询负载均衡策略**

代码块

```
可选值：

BALANCE_ALL（默认值）
获取集群中所有数据源，读取操作轮询所有机器

BALANCE_ALL_READ（一主多从）
获取集群中允许读的数据源（从服务器），在这些机器上轮询

BALANCE_READ_WRITE
获取集群中允许读写的数据源，但优先选择从服务器，所有机器参与读操作

BALANCE_NONE
只获取主节点，所有读操作都直接打到主服务器
```

**switchType：主从切换**

```
NOT_SWITCH：不进行主从切换
SWITCH：进行主从切换
```

**MyCAT 不仅可以实现读写分离，还能实现高可用操作。**

- **SWITCH（默认）**：

- 如果主从服务器中的主服务器宕机，从服务器会自动升级为主服务器

- **NOT_SWITCH**：

- 如果主服务器宕机，从服务器不会升级为主服务器

这里说的 MyCAT 主从切换和 MGR 中的主从切换有所不同：

- **MGR 主从切换**：

- 属于真正意义的主从切换
- 主节点宕机后，从节点通过选举产生新的主节点
- 选举完成后，其他从节点会自动重定向到新的主节点，成为其从节点

- **MyCAT 主从切换**：

- 强调的是请求路由层面的切换
- 当主节点心跳检测失败时，系统会自动移除此节点
- 将所有写入操作转发到从节点
- 在 MyCAT 层面实现了主从切换，但 MySQL 本身并没有发生真实的主从角色切换

总结：

- MyCAT：逻辑层切换（代理层路由）
- MGR：数据库层切换（真实主从切换）

MyCAT 可以配合以下组件实现高可用 + 读写分离集群：

- Shell 脚本
- Keepalived
- MGR

# 四、MyCAT 客户端与管理端

## 1、客户端

测试查看代理客户端 8066，负责对接 Web

直接面向客户（MySQL软件、DataGrip软件、Web服务器）

```
# 安装 mysql 客户端（mysql-server 为服务端，mysql 为客户端）
yum install mysql -y

# rm -rf /etc/my.cnf
```

启动 MyCAT => 通过 8066 端口代理连接真实数据库服务器：

![[附件/853029296a.png]]

使用showdatabases以及showtables操作，查看数据信息。

## 2、管理端

```
ss -naltp | grep 9066
```

```
LISTEN 0 4096 [::ffff:127.0.0.1]:9066 users:(("java",pid=101467,fd=51))
```

说明：

- MyCAT2 和 MyCAT 有所不同
- 早期 MyCAT：9066 可登录，通过管理端查看集群等信息
- MyCAT2：所有功能已集成到 8066 端口
- 9066 虽然被占用，但不需要用户参与管理

# 五、MyCAT2 其他配置

## 1、修改 MyCAT2 登录密码

```
cd /usr/local/mycat/conf/users
vim root.user.json
```

```
{
  "dialect":"mysql",
  "ip":null,
  "password":"itheima123@",
  "transactionType":"xa",
  "username":"root"
}
```

## 2、修改服务器 server 配置

隐藏服务器信息

```
cd /usr/local/mycat/conf/
vim server.json
```

```
{
  "loadBalance":{
    "defaultLoadBalance":"BalanceRandom",
    "loadBalances":[]
  },
  "mode":"local",
  "properties":{},
  "server":{
    "ip":"0.0.0.0",
    "mycatId":1,
    "port":8066,
    "serverVersion":"8.0.40-mycat-2.0",
    "reactorNumber":8,
    "bufferPool":{},
    "idleTimer":{
      "initialDelay":3,
      "period":60000,
      "timeUnit":"SECONDS"
    },
    "workerPool":{
      "corePoolSize":1
    }
  }
}
```

![[附件/ec6b4c6ad1.png]]

# 六、整合 MyCAT2 到 NiuShop 项目

```
vim conf/schemas/niushop.schema.json
```

```
{
  "customTables":{},
  "globalTables":{},
  "normalTables":{},
  "schemaName":"niushop",
  "shardingTables":{},
  "views":{}
}
```

修改 schema 配置

```
/*+ mycat:createschema{
"customTables":{},
"globalTables":{},
"normalTables":{},
"schemaName":"niushop",
"shardingTables":{},
"targetName":"prototype"
}*/;
```

动态添加数据源【联系数据库】

```
/*+ mycat:createDatasource{
"name":"rw_master",
"type":"JDBC",
"dbType":"mysql",
"instanceType":"READ_WRITE",
"url":"jdbc:mysql://192.168.88.106:3306/niushop?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai",
"user":"root",
"password":"123"
}*/;

/*+ mycat:createDatasource{
"name":"rw_slave",
"type":"JDBC",
"dbType":"mysql",
"instanceType":"READ",
"url":"jdbc:mysql://192.168.88.109:3306/niushop?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai",
"user":"root",
"password":"123"
}*/;
```

![[附件/e1232ef84b.png]]

![[附件/b2e88d4771.png]]

动态创建读写集群

```
/*+ mycat:createcluster{
"name":"niushop_cluster",
"clusterType":"MASTER_SLAVE",
"masters":["rw_master"],
"replicas":["rw_slave"],
"readBalanceType":"BALANCE_ALL"
}*/;
```

动态创建 schema 并指定集群

```
/*+ mycat:createschema{
"schemaName":"niushop",
"targetName":"niushop_cluster",
"customTables":{},
"globalTables":{},
"normalTables":{},
"shardingTables":{},
"views":{}
}*/;
```

查看已有配置【测试】

```
/*+ mycat:showDatasources{} */;
/*+ mycat:showclusters{} */;
/*+ mycat:showSchemas{} */;
```

动态删除数据源 / 集群 / schema【测试】

```
/*+ mycat:dropDatasource{"name":"rw_master"} */;
/*+ mycat:dropcluster{"name":"niushop_cluster"} */;
/*+ mycat:dropschema{"schemaName":"niushop"} */;
```

更改 web01 和 web02 中 database.php 配置，指向 MyCAT，这样 NiuShop 电商项目就可以实现数据库读写分离 + 高可用架构

```
vim /www/wwwroot/www.shop.com/niushop/config/database.php
```

![[附件/3b0a85eabc.png]]