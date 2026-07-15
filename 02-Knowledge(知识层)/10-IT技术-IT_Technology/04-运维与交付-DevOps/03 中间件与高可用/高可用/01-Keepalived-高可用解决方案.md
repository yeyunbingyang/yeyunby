# 学习目标

1、能够描述高可用 HA 的作用  
2、能够理解 VIP（虚拟 IP）的漂移  
3、能够描述 keepalived 作用  
4、能够理解主 master 和备 backup 服务器关系  
**5、能够实现主备服务器高可用配置（重点）**  
6、能够实现模拟业务宕机服务切换（FailOver、扩展：VIP 脑裂）

# 一、背景描述及其方案设计

## 1、业务背景描述

- 时间：2016.6-2017.9
- 发布产品类型：互联网动态站点商城
- 用户数量：2000-4000（用户量猛增了 4 倍）
- PV：8000-50000（24 小时访问次数总和）
- DAU：1500（每日活跃用户数）

随着用户量增多，总的页面数量持续增加，WEB 服务器压力也会越来越大。虽然单台 WEB 服务器完全可以完成工作任务，但一旦宕机，用户将完全失去服务，用户体验特别差，这就是所谓的单点故障。

解决方案：

- 需要备用一台服务器，在主服务器宕机时，能够切换到备用服务器。

## 2、模拟运维设计方案

![[fe5c950e62.png]]

针对业务背景下的需求，升级为以下架构：

![[c772edcf71.png]]

主备切换

![[dc59207f50.png]]

![[d478244524.png]]

# 二、数据库服务器的迁移

## 1、克隆虚拟机

|   |   |   |   |   |
|---|---|---|---|---|
|角色|IP|主机名|功能|备注|
|web01|192.168.88.104|web01.itcast.cn|master|主|
|web02|192.168.88.105|web02.itcast.cn|backup|备|
|mysql01|192.168.88.106|mysql01.itcast.cn|数据节点|数据迁移|

第一步：把 node4 机器进行克隆，生成 node5 服务器，更改网卡的 MAC 地址

第二步：更改 node5 服务器 IP 地址与主机名称

```
# 修改网卡 IP 地址
vim /etc/NetworkManager/system-connections/ens33.nmconnection
# 将 addresses= 改为：
addresses=192.168.88.105/24

# 修改主机名
hostnamectl set-hostname web02.itcast.cn

# 使配置生效
bash
```

第三步：把 node2 做一个快照还原，还原到运维系统初始化阶段，然后对其进行克隆

```
# 修改网卡 IP 地址
vim /etc/NetworkManager/system-connections/ens33.nmconnection
# 将 addresses= 改为：
addresses=192.168.88.106/24

# 修改主机名
hostnamectl set-hostname mysql01.itcast.cn

# 使配置生效
bash
```

## 2、修改主机名和 hosts

```
# hostnamectl set-hostname web01.itcast.cn

# cat /etc/hosts
127.0.0.1       localhost localhost.localdomain localhost4 localhost4.localdomain4
::1             localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.88.101 server 
192.168.88.102 agent1
192.168.88.103 grafana
192.168.88.104  web01 web01.itcast.cn
192.168.88.105  web02 web02.itcast.cn
192.168.88.106  mysql01 mysql01.itcast.cn

```

## 3、关闭防火墙与SELinux

```
# 停止防火墙服务
sudo systemctl stop firewalld

# 禁止开机启动
sudo systemctl disable firewalld

# 检查状态
sudo systemctl status firewalld

关闭 SELinux
sudo vim /etc/selinux/config
SELINUX=disabled
# 可选值：
# enforcing → 强制模式
# permissive → 宽容模式
# disabled → 永久关闭
sudo setenforce 0 
```

## 4、设置网络（忽略）

```
# 查看网络连接配置文件
ls /etc/NetworkManager/system-connections/

# 编辑指定网卡配置
sudo vi /etc/NetworkManager/system-connections/ens33.nmconnection

# 设置开始
[ipv4]
method=manual
addresses=192.168.88.101/24
gateway=192.168.88.2
dns=8.8.8.8

[ipv6]
method=ignore
# 设置结束

# 重启网络服务并查看网卡信息
sudo systemctl restart NetworkManager
nmcli device show ens33
```

如果想重启所有网络接口，可以使用以下命令：

```
sudo nmcli networking off
sudo nmcli networking on
```

## 5、chrony 时间同步

**第一步：安装 chrony**

```
sudo dnf install -y chrony
```

**第二步：安装并启用 chronyd 服务**

```
sudo systemctl enable --now chronyd
```

**第三步：配置 NTP 时间服务器**

```
# 编辑 chrony 配置文件
sudo vi /etc/chrony.conf

# 在文件中添加或修改 NTP 服务器，例如使用阿里云的 NTP 服务器：
# server ntp1.aliyun.com iburst
# server ntp2.aliyun.com iburst
```

将 chrony 配置文件中的 NTP 服务器替换为阿里云服务器：

```
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (https://www.pool.ntp.org/join.html).
# pool 2.centos.pool.ntp.org iburst

server ntp1.aliyun.com iburst
server ntp2.aliyun.com iburst
server ntp3.aliyun.com iburst
server ntp4.aliyun.com iburst
server ntp5.aliyun.com iburst
server ntp6.aliyun.com iburst
```

保存并退出编辑器。

**第四步：重启 chronyd 服务**

```
sudo systemctl restart chronyd
```

## 6、安装必备软件

```
yum install vim wget rsync net-tools -y
```

## 7、数据备份和迁移

Shell做哪些功能？答：日常巡检、软件自动化安装部署、日志分析

前提：在192.168.88.106服务器上提前安装MySQL5.7

`mysql5.sh` 脚本如下

```
#!/bin/bash

echo "正在安装依赖软件..."
yum install libaio -y

echo "执行解压缩操作..."
tar -xf mysql-5.7.31-linux-glibc2.12-x86_64.tar.gz -C /usr/local/
mv /usr/local/mysql-5.7.31-linux-glibc2.12-x86_64 /usr/local/mysql

# 创建 mysql 用户
useradd -r -s /sbin/nologin mysql

# 删除已有 my.cnf
rm -rf /etc/my.cnf

echo "进入 MySQL 目录，对其进行初始化操作..."
cd /usr/local/mysql

# 创建 mysql-files 目录
mkdir mysql-files
chown mysql:mysql mysql-files
chmod 750 mysql-files

# 初始化数据库并获取临时密码
temp_password=$(bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql 2>&1 | grep 'temporary password' | awk '{print $NF}')
echo "临时密码: $temp_password"

echo "配置 my.cnf 文件..."
cat >/etc/my.cnf <<EOF
[mysqld]
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
socket=/tmp/mysql.sock
port=3306
log-error=/usr/local/mysql/data/mysql.err
log-bin=/usr/local/mysql/data/binlog
server-id=10
character_set_server=utf8mb4
gtid-mode=ON
log-slave-updates=1
enforce-gtid-consistency
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
EOF

# 设置 SSL/RSA
bin/mysql_ssl_rsa_setup --datadir=/usr/local/mysql/data

# 配置 systemd 服务
cat >/etc/systemd/system/mysqld.service <<EOF
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

echo "刷新后台服务并启动 mysqld..."
systemctl daemon-reload
systemctl start mysqld
systemctl enable mysqld
sleep 5

# 添加 mysql 命令到系统 PATH
echo 'export PATH=$PATH:/usr/local/mysql/bin' >> /etc/profile
source /etc/profile

# 解决库文件兼容
ln -s /lib64/libncurses.so.6 /lib64/libncurses.so.5
ln -s /lib64/libtinfo.so.6 /lib64/libtinfo.so.5

# 重置 MySQL root 密码
echo "正在重置 MySQL 管理员密码..."
bin/mysqladmin -uroot -p"$temp_password" password '123456'

echo "MySQL 安装成功，软件安装路径：/usr/local/mysql，数据库初始密码：123456！"

# source mysql5.sh
```

第一步：web01 源数据库服务器导出数据

```
# 导出 niushop 数据库
mysqldump -uroot -p --databases niushop > ~/niushop.sql
```

第二步：将导出的数据传输到 mysql01 新数据库服务器

```
# 使用 rsync 传输 SQL 文件
rsync -av ~/niushop.sql root@192.168.88.102:/root/
```

第三步：在 mysql01 主机创建数据库并导入数据

```
-- 登录 MySQL
mysql -uroot -p

-- 创建数据库
create database niushop;

-- 切换到 niushop 数据库
use niushop;

-- 导入 SQL 文件
source /root/niushop.sql;
```

第四步：在 mysql01.itcast.cn 主机中创建授权用户，允许远程连接（不要直接使用 root 账号）

```
-- 登录 MySQL
mysql -uroot -p

-- 创建远程访问用户
create user 'niushop'@'%' identified with mysql_native_password by '123';

-- 授权该用户对 niushop 数据库的所有权限
grant all on niushop.* to 'niushop'@'%';

-- 刷新权限使配置生效
flush privileges;
```

第五步：更改 `web01.itcast.cn` 主机的数据库配置文件 `/www/wwwroot/www.shop.com/niushop/config/database.php`

```
return [
    'hostname' => '192.168.88.106',
    'database' => 'niushop',
    'username' => 'niushop',
    'password' => '复杂的实际密码',  // 实际使用中请设置更复杂的密码
];
```

![[68519cea2d.png]]

![[429f0cb163.png]]

第六步：访问页面，查看业务恢复情况

![[f5ed123c61.png]]

## 常见问题

常见错误说明

**问题 1：MySQL 密码不对（web01/web02）**

- 192.168.88.104 => web01（BT 宝塔 => nginx/mysql/php）
- 192.168.88.105 => web02（BT 宝塔 => nginx/mysql/php）
- 192.168.88.106 => mysql01
- 明确在哪台机器的宝塔上修改密码，就在该机器上执行，不要交叉操作。不同宝塔可能对应的 MySQL 密码不同。

**问题 2：数据库命名不一致**

```
# mysqldump -uroot --databases niushop > ~/niushop.sql -p
```

- 导出语句中的数据库名必须与实际数据库名一致。
- 数据库名区分大小写，例如 `niushop` ≠ `NiuShop`。
- 不要随意修改数据库名，如 new、shop、ns 等，否则会提示数据库不存在。

**问题 3：忘记创建** `**niushop**` **用户**

```
mysql> create user 'niushop'@'%' identified with mysql_native_password by '123';
mysql> grant all on niushop.* to 'niushop'@'%';
mysql> flush privileges;
```

- 如果没有创建该用户，远程连接数据库会失败。

**问题 4：database.php 配置**

- 必须严格按照 MySQL 服务器的实际情况设置：

- hostname、database、username、password 都要对应正确。

- 错误的配置会导致网站无法连接数据库。

**问题 5：授权异常，由于数据库更名导致授权异常**

- 如果数据库名称被修改，原先针对 `niushop.*` 的授权会失效。
- 授权语句需要与实际数据库名一致，例如数据库名为 `db_itheima`、`shopping` 或 `admin`，则授权语句如下：

```
mysql> create user 'niushop'@'%' identified with mysql_native_password by '123';
mysql> grant all on db_itheima.* to 'niushop'@'%';
mysql> flush privileges;
```

- 如果实在搞不定，也可以授权该用户访问所有数据库（不太建议，安全性低）：

```
mysql> grant all on *.* to 'niushop'@'%';
mysql> flush privileges;
```

**问题 6：动态代码（如 Web 程序）如何排查错误**

- 当程序异常时，首先查看后台日志或者动态页面。
- 动态页面往往会直接显示相关错误信息，便于定位问题。
- 示例访问地址：

```
http://www.shop.com/shop/
```

- 建议排查步骤：

1. 打开浏览器访问动态页面，观察报错信息。
2. 检查 Web 服务器日志（如 Nginx 或 Apache 错误日志）。
3. 检查 PHP 或程序自身日志（如 `/www/wwwroot/www.shop.com/log/`）。
4. 对照数据库连接配置和权限，确认是否可正常连接数据库。

![[09352e3ad6.png]]

# 三、HA 高可用服务搭建

## 1、HA Cluster 高可用集群

- HA 是 High Available 缩写。
- HA Cluster 是指高可用性集群，是保证业务连续性的有效解决方案，一般有两个或两个以上的节点，且分为活动节点及备用节点。

## 2、为什么要引入 HA 高可用

- 我们之前使用 LNMP 架构属于单点服务器，一台服务器完成所有工作。
- 单点往往是系统高可用最大的风险和敌人，应该尽量在系统设计的过程中避免单点。
- 方法论上，高可用保证的原则是“集群化”，或者叫“冗余”：只有一个单点，挂了服务会受影响；如果有冗余备份，挂了还有其他 backup 能够顶上。
- 保证系统高可用，架构设计的核心准则是：冗余。有了冗余之后，还不够，每次出现故障都需要人工介入恢复，但是这样势必会增加系统的不可用服务时间。
- 最好的解决办法是通过 **FailOver 自动故障转移** 来实现系统的高可用。

3、实现高可用的核心点

- 冗余（多台服务器）中，当 master 发生故障时，backup 可以自动切换（FailOver：故障自动切换）。

4、备份服务器

- **冷备**：服务器不启用（域名不解析），使用时再启动，需要手动切换
- **热备**：服务器处于等待状态（监控主服务器状态），一旦主机故障，备机接管，自动切换实现热备，并引入 VIP 的切换

实现热备，引I入VIP【虚拟ip】【的切换

看门狗 心跳监测 数据表响应

![[269977e39a.png]]

## 3、Keepalived 软件概述

- Keepalived 软件最初专为 LVS 负载均衡设计，用来管理并监控 LVS 集群中各个服务节点的状态。
- 后来加入了实现高可用的 VRRP 功能。
- 除了管理 LVS，Keepalived 也可用于其他服务（如 Nginx、HAProxy、MySQL 等）的高可用解决方案。

## 4、Keepalived 组成和原理

- Keepalived 主要通过 **VRRP 协议** 实现高可用功能（故障切换方式）。

- VRRP（Virtual Router Redundancy Protocol，虚拟路由器冗余协议）用于解决静态路由单点故障问题，保证个别节点宕机时网络仍能不间断运行。

- **FailOver + VIP 漂移**：使用 Keepalived 管理虚拟 IP（VIP），所有服务器共享同一个 VIP，实现高可用。
- VRRP 原理：

- 将 N 台功能相同的路由器组成一个路由器组，其中一个为 master，其他为 backup。
- master 提供对外服务的 VIP，并在组播中发送 VRRP 包。
- backup 收不到 VRRP 包时认为 master 宕机，根据 VRRP 优先级选举一个 backup 为新的 master。

- 这样可以保证路由器及服务的高可用性。

![[27b3c262ae.png]]

Keepalived的功能体系结构，大致分两层：用户空间（userspace）和内核空间（kernel space）。

- **用户空间**：大部分内容可以在keepalived.conf配置文件中进行配置【服务监测 调用RRP切换】
- **内核空间**：大部分是系统底层自动发生的，不需要用户参与【VIP转移】

Keepalived本身有两层作用：  
① 高可用效果  
② keepalived+Ivs（高可用+负载均衡）

- **IPVS**：主要用于实现LVS负载均衡器，把用户的请求平均分发给后端服务器（减压目的）
- **Netlink**：高级路由，可以借助于VRRP协议，生成VIP、转移VIP等等
- **Watchdog**：看门狗，当keepalived启动后，看门狗自动检测服务器状态（web01、web02）
- **Checkers**：检查器，用于检测服务器状态(如nginx、mysql 、Ivs)
- **VRRPStack**：当检查器检测到服务器出现故障时，则VIP发生漂移

**内核空间**

- 主要包括 IPVS（IP 虚拟服务器，用于实现网络服务的负载均衡）和 Netlink（提供高级路由及其他相关的网络功能）两个部分

**用户空间**

1. **WatchDog**：监控 Checkers 和 VRRP 进程的状况
2. **VRRP Stack**：负责负载均衡器之间的失败切换（Failover），如果只用一个负载均衡器，则 VRRP 不是必须的
3. **Checkers**：负责真实服务器的健康检查（healthchecking），是 Keepalived 最主要的功能。换言之，可以没有 VRRP Stack，但健康检查必须存在
4. **IPVS Wrapper**：用户发送设定的规则到内核 IPVS 代码
5. **Netlink Reflector**：用来设定 VRRP 的 VIP 地址等

**Keepalived 主要模块**

- **Core**：Keepalived 的核心，负责主进程的启动、维护以及全局配置文件的加载和解析
- **Check**：负责健康检查，包括常见的各种检查方式
- **VRRP**：实现 VRRP 协议

---

## 5、安装 Keepalived

- **官网地址**：[https://www.keepalived.org/](https://www.keepalived.org/)
- Keepalived 可以通过 **yum 安装** 或 **源码编译** 的方式实现。

- 在目前案例中，通过 **yum 安装** 的版本即可。

使用 yum 安装

- **注意**：master 和 backup 节点都需要安装
- 给 web01 和 web02 安装 Keepalived

```
# yum -y install keepalived
```

配置文件

```
# /etc/keepalived/keepalived.conf
```

日志文件

```
# /var/log/messages
```

注意事项：启动之前，一定要配置下/etc/keepalived/keepalived.conf：

![[d984636527.png]]

选举 ：比较依赖权重 、自身优先级高成为master、再比较真实ip地址值大成为master

详细配置：

![[be554845d7.png]]

设置 VIP 注意事项

```
① 用户可以访问 VIP，VIP 所在的机器没有限制外网访问  
② VIP 没有被占用
```

keepalived发送的组播（主要向自己组内的其他主机发送通告）

VIP脑裂、服务之间无法通信确认 都会成为vip结点

以下实现，VIP选择同网段的。

## 6、启动Keepalived

通过yum方式安装的Keepalived，直接使用`systemctl`命令进行管理；如果是通过源码包安装的，可以使用`keepalived -D`参数启动。

```
systemctl stop firewalld
# systemctl start keepalived
```

查看主备服务器的网卡信息（不要使用`ifconfig`）：

**master的网卡信息：**

```
# ipa
```

**backup的网卡信息：**

```
# ipa
```

通过Keepalived的主备模式，实现默认VIP绑定到了master服务器。  
当master服务器宕机（关机、断电、网线断开）时，VIP会切换到backup。

**常见问题说明：**

- **问题1：Keepalived启动了，但是没有产生VIP**  
    答：大部分情况是因为网卡名称写错，配置前最好使用`ipa`确认物理网卡名称：`eth0`、`ens33`或`ens160`。
- **问题2：Keepalived启动了，但是两台机器上都有VIP（脑裂）**  
    答：在同一个HA Cluster组中有两个VIP，每台机器都认为自己是Master，核心原因是网络通信异常，无法意识到对方的存在。

- 可能原因：

1. 网络故障
2. 防火墙未关闭，VRRP协议默认无法通过防火墙

```
firewall-cmd --add-protocol=vrrp
```

详细参考文档下方VIP脑裂解决方案。

- **问题3：脑裂的危害**  
    答：如果一个组中有两个VIP，就会出现资源争抢情况。  
    示例：注册请求到`node4`，提交写入数据库可能被`node5`处理，导致数据不一致。
- **问题4：抢占模式**  
    默认Master和Backup模式，Master优先；如果Master恢复，会把VIP重新切回Master。  
    为提高用户体验，可以关闭抢占，让Master恢复后不争抢VIP，将两台服务器状态都设置为Backup。

**Master节点配置示例：**

```
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    virtual_router_id 51
    priority 100
    nopreempt
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.88.200
    }
}
```

**Backup节点配置示例：**

```
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    virtual_router_id 51
    priority 90
    nopreempt
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.88.200
    }
}
```

## 7、让Keepalived与NiuShop产生联系

**第一步：更改Windows中的域名劫持（hosts文件）**

```
192.168.88.200 www.shop.com
```

**第二步：修改Keepalived配置**

- 注释掉Keepalived配置文件中的`vrrp_strict`。
- 特别注意：Keepalived 1.3及以后版本必须注释`vrrp_strict`，否则虚拟IP无法ping通。

![[0d0d3380ae.png]]

# 四、实现Nginx服务HA

**作用**

到目前为止，VIP漂移只能针对硬件故障。如果是服务问题，如Nginx宕掉，VIP也应该发生漂移，否则项目无法使用。【实现软件监控】

开发一个脚本，通过这个脚本，监控系统故障以及Nginx服务故障，只要有一种发生，则VIP漂移。

## 1、解析域名到VIP

在Windows的hosts文件，把192.168.88.200绑定www.shop.com域名。

以后就可以通过www.shop.com访问电商平台。

记得把keepalived.conf配置文件进行修改如下：|

![[d6b453368e.png]]

## 2、模拟宕机实现服务切换

真实业务环境下，可能是服务器整机没有宕机，但Nginx服务宕掉。

监控Nginx服务，如果服务down，就关闭Keepalived。

**① 配置服务检测脚本**  
在多台服务器的Keepalived配置文件目录，建立一个检测Nginx服务的脚本，作用是在检测到Nginx服务宕机时，关闭Keepalived。

定义chek_nginx.sh文件

```
vim /etc/keepalived/checknginx.sh
```

![[143b24be0f.png]]

![[21e5cc2b4f.png]]

```
#!/bin/bash

nginx_status=$(ps -C nginx --no-header | wc -l)

if [ $nginx_status -eq 0 ]; then
    systemctl stop keepalived
fi
```

注：9版本中，使用systemctl stop keepalived

**② 赋予执行权限**

脚本需要实际测试是否可以在Nginx宕机时关闭Keepalived：

```
# chmod +x /etc/keepalived/check_nginx.sh
```

**③ 在多台服务器中配置Keepalived定时触发检测Nginx的脚本模块**

```
vrrp_script 名称 {        # [方便调用的名称]
    script /etc/keepalived/check_nginx.sh
    interval 2             # 检测时间间隔（单位：秒）
    weight 50              # 检测失败时降低的优先级权重值
}
```

定义一个脚本模块：

vrrp_script脚本名称

![[e28294cc53.png]]

在`vrrp_instance`里调用检测脚本示例：

```
vrrp_instance VI_1 {
    track_script {
        check_nginx
    }
}
```

当Nginx服务不可用时，`check_nginx`脚本会触发关闭Keepalived，VIP将发生漂移。

Tip：priority权重在多备情况，会根据权重选择成为Master的BACKUP

最终配置代码：

![[3000d57510.png]]

![[852bea5364.png]]

注意：以上配置完成后，nginx与keepalived启动顺序，一定是要先启动nginx，然后在启动keepalived，否则过3s，keepalived会自动关闭。

**常见问题说明**

**问题：**  
当Nginx宕机后，Keepalived怎么重启都没有VIP？

**答：**  
并不是Keepalived配置出现问题，Keepalived本身是正常工作的。原因在于：

- Keepalived配置文件中，每隔3秒会检测一次Nginx服务。
- 一旦发现Nginx未启动，就让VIP发生漂移。
- 如果某台或几台Nginx出现故障，即使重启Keepalived，也不会生成VIP。
- Keepalived启动后，会再次检测Nginx状态，发现未存活，则VIP继续漂移。

**解决方案：**

1. 停止所有Keepalived
2. 启动所有Nginx
3. 重启所有Keepalived

## 3、Keepalived选举原理（面试）

Keepalived的选举机制主要依赖于**优先级（Priority）****和****VRRP报文**的交互。

**（1）优先级（Priority）**

- 每个VRRP实例（VRID，虚拟路由器ID）在Keepalived配置文件中都会配置一个优先级值（范围0-255，默认为100）。
- 优先级最高的节点将成为Master，其他节点为Backup。
- 如果多个节点的优先级相同，则比较真实IP地址，IP地址值较大的节点优先成为Master。

**（2）VRRP通告报文（Advertisement）**

- Master节点会定期（通常每秒）向组播地址`224.0.0.18`发送VRRP通告报文，包含以下关键信息：

- 虚拟路由器ID（VRID）
- 优先级（Priority）
- 虚拟IP地址（VIP）
- Master节点的真实IP地址

- Backup节点通过监听这些通告报文来判断Master的状态。如果Backup节点在一定时间内（通常为3倍通告间隔+偏移时间）未收到Master的通告报文，则认为Master故障，触发选举。

**（3）选举过程**

**初始选举：**

- 所有节点启动时，进入Backup状态，并监听VRRP通告报文。
- 如果在一段时间内未收到任何通告报文，节点会发送自己的通告报文，声明自己为Master。
- 如果收到其他节点的通告报文，则比较优先级：

- 若收到报文的优先级高于自身，保持Backup状态。
- 若收到报文的优先级低于或等于自身，且自身优先级最高，则发送通告报文，尝试成为Master。

**故障切换：**

- 当Master节点故障（停止发送通告报文），Backup节点会在超时后进行选举。优先级最高的Backup节点会接管VIP，成为新的Master，并开始发送通告报文。
- 如果配置了抢占模式（Preempt），原Master恢复后会重新比较优先级，可能重新夺回Master角色。

# 五、Keepalived的配置补充

## 1、非抢占模式

**作用：**

- 不争抢VIP，避免用户请求HTTP时受到影响，提高客户体验。

**第一步：在vrrp_instance块下增加nopreempt指令**

```
vrrp_instance VI_1 {
    virtual_router_id 51
    nopreempt
    priority 100
}
```

**第二步：节点的state都设置为BACKUP**

```
vrrp_instance VI_1 {
    state BACKUP
}
```

**说明：**

- 两个Keepalived节点启动后，默认都是BACKUP状态。
- 双方发送组播信息后，根据优先级选举一个MASTER。
- 配置了`nopreempt`后，MASTER从故障恢复时不会抢占VIP。
- 非抢占模式主要为了改善用户体验，确保服务恢复后不影响正在提供服务的VIP。

## 2、VIP脑裂

**定义（split-brain）：**

- 在高可用（HA）系统中，当两个节点失去联系时，原本作为整体的系统分裂为两个独立节点。
- 两个节点同时争抢共享资源，可能导致系统混乱和数据损坏。
- 典型表现：MASTER-BACKUP模式下，两台机器同时拥有VIP。

**主要原因：**

- 网络通信故障、防火墙未关闭或防火墙规则未正确设置。

**查看日志：**

```
# tail -f /var/log/messages
```

**抓取VRRP数据包：**

```
# yum install tcpdump -y
# tcpdump -i ens33 vrrp -n
# 说明：
# -i：指定网卡
# -n：以数字形式显示IP地址
```

**数据包流向示意：**  
VIP所在主机 → 发送VRRP数据包 → 组播地址 224.0.0.18

![[c9bf4657f8.png]]

**防火墙配置：**  
（需确保允许VRRP协议通过）

```
# 允许VRRP协议
firewall-cmd --permanent --add-rich-rule='rule protocol value="vrrp" accept'

# 添加组播地址
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" destination address="224.0.0.18" accept'

# 允许Keepalived服务
firewall-cmd --permanent --add-service=high-availability

# 重新加载防火墙
firewall-cmd --reload
```

**firewall-cmd命令说明**

- `--permanent`：永久生效
- `--add-rich-rule`：添加防火墙规则
- `rule family="ipv4" destination address="224.0.0.18" accept`：针对组播地址`224.0.0.18`允许流量
- `--add-service`：根据服务名称设置防火墙规则

- `high-availability`：防火墙预定义服务名，包括Keepalived在内的所有高可用软件

- `--add-port`：根据端口号设置防火墙规则
- `firewall-cmd --reload`：刷新防火墙，使新增规则立即生效

**小结**

- **什么是脑裂？**  
    答：在一个集群中，可能出现两个VIP，同时向组播地址发送通告报文（通过tcpdump抓包可发现）。
- **产生脑裂的根本原因？**  
    答：集群中的各个节点由于网络通信故障，无法连接到主节点。
- **脑裂的影响？**  
    答：两个VIP同时存在，所有请求会出现争抢情况，严重时可能造成数据损坏。
- **解决方案：**  
    恢复网络通信，确保防火墙规则正确设置。

**3、单播模式（广播 > 组播 > 单播）**

- **广播（Broadcast）**：类似屏幕广播，把信息发送到广播地址（本网段的 `.255`）。
- **组播（Multicast）**：范围略小于广播，只有同组节点才能收到组播信息（Keepalived默认使用 `224.0.0.18`）。
- **单播（Unicast）**：范围最小，仅限点对点传输信息（Master → Backup）。

- **物理服务器**：不会受到影响，组播地址可以正常使用
- **云平台**：如阿里云ECS01、ECS02，平台禁用组播地址，只能使用单播模式

**问题与原因：**

- 在组播模式下，Keepalived会向 `224.0.0.18` 发送所有信息，产生大量无用信息，可能引起干扰和冲突。
- 某些环境（如云服务器）禁止组播，导致无法获取Master的VRRP数据包。

**解决方案：单播模式**

- 将组播改为单播，安全可靠，避免局域网内大量Keepalived节点造成VIP冲突（VIP脑裂）。
- 配置要求：

- 关闭 `vrrp_strict` 选项
- 在VIP实例配置段加入单播的源地址和目标地址

- 注意：单播模式需使用 Keepalived 1.2.10 及以上版本。

```
vrrp_instance VI_1 {
    unicast_src_ip 192.168.88.101
    unicast_peer {
        ## 本地IP地址
        192.168.88.103
        ## 对端IP地址，此地址一定不能忘记，支持多台机器
    }
}
```

**注：**

- 针对 web01，`unicast_src_ip` 是 192.168.88.101
- 针对 web02，`unicast_src_ip` 是 192.168.88.103
- `unicast_peer` 对应对端IP：

- web01: 192.168.88.103
- web02: 192.168.88.101

**版本说明：**

- 单播模式需要较高版本的Keepalived（1.2.11及以上）
- 目前通过yum安装，版本已升级为2.2.8，无需手动编译

**手动安装示例（如需旧版本）：**

```
# cd /root/soft
# tar xvf keepalived-1.2.11.tar.gz
# cd keepalived-1.2.11
# ./configure --prefix=/usr/local/keepalived
# make && make install
```

**第二步：查看目录、配置文件和启动文件**

- 注意：如果使用Keepalived 1.3以上版本，需要注释`vrrp_strict`选项，否则VIP无法正常ping通

**启动命令示例：**

```
# /usr/local/keepalived/sbin/keepalived -f /usr/local/keepalived/etc/keepalived/keepalived.conf -D
```

- `-f`：指定配置文件路径
- `-D`：以守护进程方式运行

**master : keepalived.conf**

```
vrrp_instance VI_1 {
    unicast_src_ip 192.168.88.104
    unicast_peer {
        192.168.88.105
        ## 对端IP地址，此地址一定不能忘记，支持多台机器
    }
}
```

```
vrrp_instance VI_1 {
    unicast_src_ip 192.168.88.104
    unicast_peer {
        192.168.88.105
        ## 对端IP地址，此地址一定不能忘记，支持多台机器
    }
}
```

**注：**

- 针对 web01，`unicast_src_ip` 是 192.168.88.101
- 针对 web02，`unicast_src_ip` 是 192.168.88.103
- `unicast_peer` 对应对端IP：

- web01: 192.168.88.103
- web02: 192.168.88.101

**backup:keepalived.conf**

node5 :

```
vrrp_instance VI_1 {
    unicast_src_ip 192.168.88.105
    unicast_peer {
        192.168.88.104
        ## 对端IP地址，此地址一定不能忘记，支持多台机器
    }
}
```

**注：**

- 针对 web01，`unicast_src_ip` 是 192.168.88.104
- 针对 web02，`unicast_src_ip` 是 192.168.88.105
- `unicast_peer` 对应对端IP：

- web01: 192.168.88.105
- web02: 192.168.88.101

**VIP脑裂原因：**

- VIP出现在多台机器上
- 网络不通畅或禁用组播/单播数据包
- 主备服务器无法通信，Backup节点误以为Master不可用，绑定VIP
- 主服务器的VIP不会释放，导致脑裂问题

- **① 双备或多备模式**

- 多个Backup节点通过`priority`权重来区分谁的优先级更高，优先级高的Backup节点在Master宕机时接管VIP。

- **②单播的方式**

- Backup节点和Master节点通过单播方式通信，确保在禁止组播的环境下（如云平台）仍能正常进行VIP漂移。

- **③ 时间不同步**

- 服务器时间不同步可能导致VRRP状态判断异常，需要通过时间校准（如NTP）保证各节点时间一致。