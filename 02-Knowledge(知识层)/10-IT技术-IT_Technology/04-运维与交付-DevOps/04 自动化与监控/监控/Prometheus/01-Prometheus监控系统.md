学习目标

- 能够通过node_exporter采集系统信息
- 能够通过mysqld_exporter采集MySQL信息
- 了解Grafana作用及其安装
- 能够基于Grafana实现CPU负载监控
- 能够基于Grafana+OneAlert睿象云实现监控告警

# **Prometheus+Grafana监控系统**

# **一、Prometheus概述**

作用：能够基于Prometheus+Grafana搭建企业级监控系统，实现系统层面监控与数据库层面监控。

## **1.** 什么是Prometheus？

Prometheus(普罗米修斯)是一套开源的监控&报警&时间序列数据库的组合, 由go语言开发。适合监控容器平台, 因为Kubernetes(俗称k8s)的流行带动了Prometheus的发展。

官网：[Prometheus - Monitoring system & time series database](https://prometheus.io/)

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296677763-34064d00-c8fa-4cf5-b2d1-48259c563d56.jpg "null")

Prometheus应用场景：解决运维环境中（AI大模型、传统Web项目、大数据项目）服务的监控操作！

## **2.** 时间序列数据库？

数据库分类

- 关系型 mysql,oracle,sql server,sybase,db2,access等
- 非关系型(nosql)

- key-value memcache redis etcd
- 文档型 mongodb elasticsearch
- 列式 hbase
- 时序 prometheus
- 图形数据库 neo4j
- 时间序列数据(TimeSeries Data) : 按照时间顺序记录系统、设备状态变化的数据被称为时序数据.

时序数据库特点

- 数据带有时间属性，且数据量随着时间递增
- 大都为插入操作较多且无更新需求，插入数据多，每秒钟插入数据可到达千万甚至上亿条
- 分析过去时序数据可以做成多纬度报表，揭示其趋势性、规律性、异常性
- 分析时序数据趋势可以做大数据分析，机器学习，实现预测和预警
- 能够按照条件筛选数据, 也可以按照时间范围统计,聚合,展示数据

常用应用场景

- 无人驾驶车辆运行中要记录的经度，纬度，速度，方向，旁边物体距离等等，每时每刻都要将数据记录下来做分析。
- 某一个地区的各车辆的行驶轨迹数据
- 传统证券行业实时交易数据
- 实时运维监控数据等

## **3.** Prometheus主要特性

Prometheus的主要特性有:

- 多维度数据模型
- 灵活的查询语言
- 不依赖分布式存储，单个服务器节点是自主的
- 以HTTP方式，通过pull模型拉取时间序列数据
- 也可以通过中间网关支持push模型
- 通过服务发现或者静态配置, 来发现目标服务对象
- 支持多种多样的图表和界面展示

## **4.** Prometheus架构图

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296677997-b1f44925-dd4a-4379-b587-34931a11af3d.jpg "null") 拉取数据到数据库

推送到告警模块进行

promql时序数据库查询 grafana数据可视化

# **二、Prometheus环境搭建**

## **1.** 实验环境准备

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678094-d6773241-0116-4aaa-aa13-537d86006ee7.jpg "null")

a. 所有服务器静态ip(要求能上外网)

b. 所有服务器各配置主机名并绑定

各自配置好主机名

```
# node1
hostnamectl set-hostname --static server

# node2
hostnamectl set-hostname --static agent1

# node3
hostnamectl set-hostname --static grafana
```

三台都互相绑定IP与主机名

```
# vim /etc/hosts
192.168.88.101 server
192.168.88.102 agent1
192.168.88.103 grafana
```

c. 所有服务器关闭防火墙与SELinux

```
# systemctl stop firewalld
# systemctl disable firewalld
# iptables -F
# setenforce 0
# 把/etc/selinux/config文件中的SELINUX设置为disabled
SELINUX=disabled
```

d. 安装必备软件

```
dnf install vim wget rsync net-tools -y 
```

## **2.** 安装Prometheus

下载地址: [https://prometheus.io/download/](https://prometheus.io/download/) (请使用共享的软件版本，以免出现不兼容问题)

第一步：解压Prometheus压缩包

```
[root@server ~]# tar xf prometheus-2.51.2.linux-amd64.tar.gz -C /usr/local/
[root@server ~]# mv /usr/local/prometheus-2.51.2.linux-amd64/ /usr/local/prometheus
配置文件说明：
[root@server ~]# egrep -n : /usr/local/prometheus/prometheus.yml | awk -F'#' '{print $1}'

2:global:															  全局配置段
3:  scrape_interval:   15s								每15s抓取(采集)数据一次
4:  evaluation_interval: 15s					    每15秒计算一次规则
8:alerting:															 Alertmanager报警相关
9:  alertmanagers:
10:  - static_configs:
11:   - targets:
12:
15:rule_files:													   规则文件列表
19:
21:scrape_configs:										   抓取的配置文件(也就是监控的实例)
23:  - job_name: 'prometheus'				   监控的实例名称
28:   static_configs:
29:   - targets: ['192.168.88.101:9090']	监控的实例IP与端口,在这里为监控服务器本身
```

第二步：直接使用默认配置文件启动, 建议加 & 后台符号

```
[root@server ~]# nohup /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &
[root@server ~]# jobs
[1] +  运行中        /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &
```

扩展：nohup代表不展示信息在终端，而是把所有的数据追加到nohup.out文件中

第三步：验证9090端口

```
[root@server ~]# netstat -ntlup |grep :9090
tcp6   0  0 :::9090      :::*       LISTEN    64950/prometheus
```

扩展：后台服务管理

```
# 可以使用jobs命令查看所有后台运行的进程
jobs
[1] +  运行中        /usr/local/prometheus/prometheus ...

# 在以上查看到的信息中，[]方括号中的数字就是一个服务编号，我们可以通过kill %服务编号，删除后台运行的任务
kill %1
```

## **3.** Prometheus界面

① 通过浏览器访问 http://服务器IP:9090 就可以访问到prometheus的主界面

![[f8bd72ba5d.png]]

② 点Status --》点Targets --》可以看到只监控了本机 (默认只监控了本机一台)

![[ca4f11e13b.png]]

![[26b033ad9b.png]]

③ 通过 http://服务器IP:9090/metrics 可以查看到监控的数据

![[9b08e03273.png]]

④ 在web主界面可以通过关键字查询metrics, 并显示图形

![[d3a07ef3d8.png]]

![[aa42b99c39.png]]

![[68072c84e0.png]]

虽然Prometheus服务器通过9090端口能监控一些metrics，但像cpu负载等这些linux常见的监控项却没有，需要node_exporter组件。

node_exporter组件可以安装在本机或远程Linux主机上。

# **三、监控远程Linux主机**

作用：通过Prometheus完成Linux主机监控

## **1.** 安装node_exporter

在远程linux主机(被监控端agent1)上安装node_exporter组件

下载地址: [https://prometheus.io/download/](https://prometheus.io/download/) (请使用共享的软件版本，以免出现不兼容问题)

```
[root@agent1 ~]# tar xf node_exporter-1.7.0.linux-amd64.tar.gz -C /usr/local/
[root@agent1 ~]# mv /usr/local/node_exporter-1.7.0.linux-amd64/ /usr/local/node_exporter
[root@agent1 ~]# ls /usr/local/node_exporter/
LICENSE  node_exporter  NOTICE
```

## **2.** 启动node_exporter服务

```
[root@agent1 ~]# nohup /usr/local/node_exporter/node_exporter &
```

说明: 如果把启动node_exporter的终端给关闭,那么进程也可能会随之关闭。nohup命令可以挂起在后台，除非杀掉相关进程，否则不会随终端关闭而关闭进程。

## **3.** 验证9100端口

```
[root@agent1 ~]# netstat -tunlp |grep 9100
tcp6   0  0 :::9100     :::*      LISTEN    74755/node_exporter
```

nohup命令: 如果把启动node_exporter的终端给关闭,那么进程也可能会随之关闭。nohup命令可以挂起在后台，除非杀掉相关进程，否则不会随终端关闭而关闭进程。

## **4.** 在被监控端收集metrics

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678591-b0f2f01d-ff17-46be-a4dc-46b134742228.jpg "null")

## **5.** 修改Prometheus配置文件

说明：其它都不变,只添加了最后3行配置，注意YAML格式要求。

```
[root@server ~]# egrep -n : /usr/local/prometheus/prometheus.yml | awk -F'#' '{print $1}'
2:global:
3:  scrape_interval:   15s
4:  evaluation_interval: 15s
8:alerting:
9:  alertmanagers:
10:  - static_configs:
11:   - targets:
12:
15:rule_files:
19:
21:scrape_configs:
23:  - job_name: 'prometheus'
24:   static_configs:
25:   - targets: ['192.168.88.101:9090']
26:  - job_name: 'agent1'				最后加上这三行，取一个job名称来代表被监控的机器
27:   static_configs:						
28:   - targets: ['192.168.88.102:9100']	这里改成被监控机器的IP，后面端口接9100
```

注意事项：YAML比传统配置文件更加严格，不能使用Tab键进行缩进。尽量保持同级内容，缩进相同，缩进只能通过Space空格实现，在YAML文件中，-代表列表，其后面必须保留一个空格，:右边也可以保留一个空格。否则语法都会报错。

## **6.** 重启Prometheus服务

说明: 没有服务脚本，直接kill杀掉进程,再重启即可。(或者kill -HUP PID)

```
[root@server ~]# pkill prometheus
[root@server ~]# netstat -ntlup |grep 9090			确认端口没有进程占用
[root@server ~]# /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &
[root@server ~]# netstat -ntlup |grep 9090			确认端口被占用，说明重启成功
tcp6   0   0 :::9090    :::*     LISTEN    32651/prometheus
```

## **7.** 查看监控结果

回到Web管理界面 --》点Status --》点Targets --》可以看到多了一台监控目标

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678716-603950f9-6b83-421a-8d03-fcd4e2d02075.jpg "null")

小结：

Prometheus默认只采集Prometheus本身，但是我们可以借助于(xxx_exporter)组件采集各种系统、应用层面的信息。

系统层面 => 官网下载 => node_exporter采集系统

如果官网没有对应的采集组件，可以到（github）去获取

![[383dcf1c8d.png]]

练习：

前面实现了prometheus监控本机9090, 但是还有很多metrics无法监控，比如cpu负载信息等。这个时候我们在prometheus服务器上也安装node_exporter，并监控。

请自行实现，最终配置文件如下:

```
[root@server ~]# egrep -n : /usr/local/prometheus/prometheus.yml | awk -F'#' '{print $1}'
2:global:
3:  scrape_interval:   15s
4:  evaluation_interval: 15s
8:alerting:
9:  alertmanagers:
10:  - static_configs:
11:   - targets:
12:
15:rule_files:
19:
21:scrape_configs:
23:  - job_name: 'prometheus'
24:   static_configs:
25:   - targets: ['localhost:9090']
26:  - job_name: 'agent1'
27:   static_configs:
28:   - targets: ['192.168.88.102:9100']
29:  - job_name: 'server'					其它不变,添加了最后3行
30:   static_configs:
31:   - targets: ['192.168.88.101:9100']
```

## 排错

![[d25c6dae6a.png]]

# **四、监控远程MySQL服务器**

作用：能通过mysqld_exporter实现应用数据库监控。（既可以监控MariaDB，还可以监控MySQL5~MySQL8）

## **1.** 在agent1安装mariadb

MariaDB 是一个开源的关系型数据库管理系统（RDBMS），由 MySQL 的原始开发者创建，旨在保持与 MySQL 的高度兼容性，同时提供增强的性能、安全性和功能。你可以把它看作是 MySQL 的一个强大分支和替代品。用于测试，有mysql MariaDB无法启动 端口占用

在agent1上安装mariadb并启动,用于被监控

```
[root@agent1 ~]# yum install mariadb-server mariadb -y
[root@agent1 ~]# systemctl restart mariadb
[root@agent1 ~]# systemctl enable mariadb
```

## **2.** 创建账号并授权

说明: 授权ip为localhost，因为不是prometheus服务器来直接找mariadb获取数据，而是prometheus服务器找mysqld_exporter,mysqld_exporter再找mariadb。所以这个localhost是指的mysql_exporter的IP

MariaDB配置：

```
[root@agent1 ~]# mysql
mysql> grant all ON *.* to 'mysql_monitor'@'localhost' identified by '123';
mysql> flush privileges;
mysql> quit

'mysql_monitor'@'%'：任意主机均可通过mysql_monitor访问MariaDB
'mysql_monitor'@'localhost'：只有在当前主机上才可以通过mysql_monitor访问MariaDB
```

MySQL8配置：

```
[root@agent1 ~]# mysql -uroot -p
mysql> create user 'mysql_monitor'@'localhost' identified with mysql_native_password by '123';
mysql> grant all ON *.* to 'mysql_monitor'@'localhost';
mysql> flush privileges;
mysql> quit
```

## **3.** 安装mysqld_exporter组件

```
下载地址: https://prometheus.io/download/ (请使用共享的软件版本，以免出现不兼容问题)
[root@agent1 ~]# tar xf mysqld_exporter-0.15.1.linux-amd64.tar.gz -C /usr/local/
[root@agent1 ~]# mv /usr/local/mysqld_exporter-0.15.1.linux-amd64/ /usr/local/mysqld_exporter
[root@agent1 ~]# ls /usr/local/mysqld_exporter/
LICENSE  mysqld_exporter  NOTICE
```

## **4.** 创建连接mariadb配置文件

说明: 配置文件里写上连接mariadb的用户名与密码(和上面的授权的用户名和密码要对应)

```
[root@agent1 ~]# vim /usr/local/mysqld_exporter/.my.cnf
[client]
user=mysql_monitor
password=123
```

## **5.** 启动mysqld_exporter

```
[root@agent1 ~]# nohup /usr/local/mysqld_exporter/mysqld_exporter --config.my-cnf=/usr/local/mysqld_exporter/.my.cnf &
[root@agent1 ~]# netstat -ntlup |grep 9104
tcp6  0   0 :::9104    :::*      LISTEN    73358/mysqld_export
```

## **6.** 修改Prometheus配置文件

```
[root@server ~]# egrep -n : /usr/local/prometheus/prometheus.yml | awk -F'#' '{print $1}'
2:global:
3:  scrape_interval:   15s
4:  evaluation_interval: 15s
8:alerting:
9:  alertmanagers:
10:  - static_configs:
11:   - targets:
12:
15:rule_files:
19:
21:scrape_configs:
23:  - job_name: 'prometheus'
24:   static_configs:
25:   - targets: ['192.168.88.101:9090']
26:  - job_name: 'agent1'
27:   static_configs:
28:   - targets: ['192.168.88.102:9100']
29:  - job_name: 'server'
30:   static_configs:
31:   - targets: ['192.168.88.101:9100']
32:  - job_name: 'agent1_mariadb'	      加上这1句,取一个job名称来代表被监控的mariadb
33:   static_configs:
34:   - targets: ['192.168.88.102:9104']	这里改成被监控机器的IP，后面端口接9104
```

## **7.** 重启服务

```
[root@server ~]# pkill prometheus
[root@server ~]# netstat -ntlup |grep 9090
[root@server ~]# nohup /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &

[root@server ~]# netstat -ntlup |grep 9090
tcp6   0   0 :::9090    :::*     LISTEN    76661/prometheus
```

## **8.** 查看监控结果

回到web管理界面 --》点Status --》点Targets --》可以看到监控mariadb了

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678797-d9240c8d-9f75-4f4e-8467-d179dbaf9107.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678878-1bd1832e-a371-41ca-9afe-dc186dd59793.jpg "null")

小结：

基于（mysqld_exporter）组件实现了mysqld（mariadb-server）数据库监控

因为数据库通常需要账号和密码访问，首先建立监控之前，我们必须先创建授权账号，允许exporter组件采集MySQL信息

# **五、Grafana数据可视化**

作用：把Prometheus采集到的系统信息、应用信息（MySQL）通过图形化方式进行数据呈现。

## **1.** Grafana介绍

Grafana是一个开源的度量分析和可视化工具，可以通过将采集的数据分析，查询，然后进行可视化的展示,并能实现报警。

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296678961-626532b3-e94e-426c-861b-c915a5fd8848.jpg "null")

官方网址: [https://grafana.com/](https://grafana.com/)

## **2.** Grafana安装与登录

在grafana服务器上安装grafana

下载地址：[https://grafana.com/grafana/download](https://grafana.com/grafana/download) (请使用共享的软件版本，以免出现不兼容问题)

第一步：拷贝软件包到grafana服务器上安装

```
[root@grafana ~]# yum install grafana-10.4.2-1.x86_64.rpm -y
```

第二步：启动服务

```
[root@grafana ~]# systemctl start grafana-server
[root@grafana ~]# systemctl enable grafana-server
```

第三步：验证端口

```
[root@grafana ~]# netstat -ntlup |grep :3000
tcp6  0  0 :::3000      :::*      LISTEN    60845/grafana-server
```

第四步：通过浏览器访问 [http://grafana服务器IP:3000](http://`grafana服务器IP`:3000) 登录,使用默认的admin用户,admin密码就可以登陆了

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679047-c2fb95e1-ed5d-4376-b5be-0e508bf4db2a.jpg "null")

## **3.** 设置prometheus为grafana数据源

把prometheus服务器收集的数据做为数据源添加到grafana，让grafana可以得到prometheus的数据。

![[cc778bb006.png]]

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679133-f7bfa446-57cb-4eb5-942e-d90bf89259ea.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679224-d9d4e51a-30b5-448a-8d66-157049f80b43.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679382-733135e8-dbd8-404b-ade3-204710f05bb3.jpg "null") ![[ba9bc28279.png]]

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679484-90d4ad83-13b0-411f-9f5c-dbeda6773c96.jpg "null") ![[1285fc7e9b.png]]

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679574-0b057abc-19e8-44d7-97fa-3cda21bd6a3f.jpg "null")

小结：

把Prometheus作为Grafana数据源。

侧重点：名称 + IP地址 + 请求

## **4.** Grafana实现自定义监控CPU负载

为添加好的数据源做图形显示

![[bdd122be05.png]]

![[3f65657e1f.png]]

选择数据源

![[591904f29b.png]]

![[0e6f2803cf.png]]

① 添加cpu 1分钟负载

node_load数字![[32212895b7.png]]

job配置名称

in ip端口

![[dcdf6c24fe.png]]

![[0d6cf0378f.png]]

② 添加cpu 5分钟负载

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679908-cff86316-f81f-4ec8-a604-ed6e50cba599.jpg "null")

③ 添加cpu 15分钟负载

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296679988-33b4fe3c-5945-4af8-bdc4-252ffc9d6ef4.jpg "null")

添加Run query

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680073-1a4a1579-8491-485c-8217-3952d1e0b61b.jpg "null")

匹配条件显示

![[796d901578.png]]

模板另存为

![[754f039397.png]]

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680254-9dea2139-0560-43e6-8d48-5e8f499065e2.jpg "null")

以上设置完成后，我们还可以通过stress-ng压测工具对平台负载进行测试

```
dnf install stress-ng
stress-ng --cpu 4 --timeout 60s
```

## **5.** 导入json模板实现linux主机与mysql监控

根据上面的思路，我们可以将 mysql_global_status_threads_connected 这个metrics加到dashboard实现对mysql数据库的当前连接数的监控。

但是mysql需要监控的状态非常的多(`mysql> show status`得到的状态信息几乎都可以监控)，一个个的手动添加太累了。有没有类似zabbix里的模板那种概念呢?

答案是有的,需要开发人员开发出相应的json格式的模板,然后导入进去就可以了。那么问题来了,谁开发?

有这么几种途径:

a. 如果公司有这方面的专业开发支持，就可以实现定制化的监控, 运维工程师配合就好

b. 当然运维工程师也可以学习并实现这方面的开发

c.寻找别人开发好的开源项目

grafana-dashboards就是这样的开源项目

参考网址: [https://github.com/percona/grafana-dashboards](https://github.com/percona/grafana-dashboards)

第一种方案：下载grafana-dashboards开源项目

```
yum install git -y
git clone https://github.com/percona/grafana-dashboards.git
```

第二种方案：在grafana图形界面搜索要导入的模板![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680359-d1b60c32-06d3-483d-9610-c8a5d78b86de.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680467-6cd62956-e0a2-4eea-a9e7-562b4e859793.jpg "null")

搜索需要使用的json模板

Prometheus模板：

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680556-17df122c-107e-4e32-b34b-93ecc9d28efc.jpg "null")

下载Prometheus模板

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680647-d65e0c38-4f00-4450-b27e-b0d6c3296f52.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680769-e7ed2704-639b-4c17-909d-0ae28928bac6.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680886-0135df4c-af21-4357-af7d-4b37af5de061.jpg "null")

点击Load

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296680968-2b7424e9-eb54-4e84-8022-f44186cc97fe.jpg "null")

运行效果：

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296681075-f76a81b1-7cf2-4a63-a0ba-2f3fac041390.jpg "null")

MySQL模板：

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296681176-9bf68992-9236-4904-a88a-e97e86aa53ac.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296681261-41f41850-b69c-4fe5-b591-0c2c0f52ecdc.jpg "null")

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296681356-fd2caf93-47e5-4f03-a956-e5755d7adea7.jpg "null")

运行效果：

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296681507-dbad8f33-f288-48fe-8703-f2f08fe2fce0.jpg "null")

## 开放式作业

开放式作业

把Nginx纳入Prometheus监控中，方式不限=>尝试使用Typora写成MarkDown格式笔记！

把Prometheus监控内容划分为两大类：【面试频率高】

系统层面监控：CPU（CPU繁忙绿、空闲率、系统使用CPU情况、用户使用CPU情况）、内存（物理使用率、交换内存、使用情况、空闲情况）、磁盘、网络

应用层面监控：MySQL、Nginx、Redis

作业：总结一下，每个监控项具体监控了哪些指标，不少于3个。如MySQL（运行时长、当前连接数、QPS、InnoDB缓存池大小、慢查询数量、主从状态、主从延迟时间等等）

# 六、PromQL语言扩展

## 1、PromQL概述

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296681647-f700fcd2-281b-47c5-87e3-edd9779c721f.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296681737-1d4eeb64-1747-4d0c-bd62-0869fb081e93.png "null")

PromQL（Prometheus Query Language）是 Prometheus 内置的数据查询语言，它能实现对事件序列数据的查询、聚合、逻辑运算等。它并且被广泛应用在 Prometheus 的日常应用当中，包括对数据查询、可视化、告警处理当中。

简单地说，PromQL 广泛存在于以 Prometheus 为核心的监控体系中。所以需要用到数据筛选的地方，就会用到 PromQL。例如：监控指标的设置、报警指标的设置等等。

## 2、快速入门

[https://www.cnblogs.com/chanshuyi/p/04_quick_start_of_promql.html](https://www.cnblogs.com/chanshuyi/p/04_quick_start_of_promql.html)

## 3、利用Kimi/DeepSeek/通义千问编写PromQL

Kimi：[https://kimi.moonshot.cn/](https://kimi.moonshot.cn/)

DeepSeek：[www.deepseek.com/](http://www.baidu.com/link?url=p7oVz_nFgPBGtD5ai7aZqXNQbMS2fVBB1ax5pMqHHs00PGHXkOmhgSXJNwRGFrEC)

通义千问：[https://tongyi.aliyun.com/](https://tongyi.aliyun.com/)

第一步：首先找到Prometheus采集到的指标信息

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296682127-a553bfe0-9bda-44e6-9460-4c16fb420239.png "null")

第二步：复制对应的指标信息，如下获取系统相关指标

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296682200-f5d0aa91-f960-4702-bb6e-d92f12f4b39f.png "null")

第三步：把以上指标信息拷贝到大模型中，提出需求，结果以PromQL进行展示

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296682271-ee26e1da-a3ff-453d-a034-aa0adcc15ba6.png "null")

第四步：把生成的PromQL粘贴到Prometheus或者Grafana进行验证

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773296682342-87a5eb61-b8d9-42be-a12b-03a7f5774392.png "null")

# **七、Grafana+OneAlert（睿象云）告警【重点】**

## **1.** Grafana对接OneAlert

第一步：注册onealert平台[http://www.onealert.com](http://www.onealert.com)

第二步：在onealert里添加grafana应用

![[5390fa235d.png]]

设置通知策略（重要）

![[6a0f609c27.png]]

设置分发策略（重要）

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773296683915-6a9cd168-0372-4cb0-a234-c3389753f460.jpg "null")

![[90f0cdd403.png]]

绑定监控工具

![[9cc5eac8e2.png]]

![[5868ccfafd.png]]

![[68094113ac.png]]

第三步：在grafana增加contact point

![[c1551d09c6.png]]

URL填写名称，选择 contact points type为webhook,填写自己的url：[http://api.aiops.com/alert/api/event/grafana/v1/换成自己的appkey秘钥/](http://api.aiops.com/alert/api/event/grafana/v1/换成自己的appkey秘钥/)

![[0b83433ac9.jpg]]

![[e09a369582.png]]![[46c1a6ff75.jpg]]

添加notification policies

![[13ea0f2d04.png]]

![[5df027e2c5.png]]

第四步：设置告警

![[146d2f476e.png]]

## **2.** 测试CPU负载报警

添加rule规则

![[318f8f41f5.jpg]]![[51eb3de536.jpg]]![[7ca04551fc.jpg]]

以上代表当Pending持续1m分钟（可以根据需求调整），则触发报警！

![[bd3254f877.jpg]]

配置完成后，在agent1节点进行压力测试

```
cat /dev/urandom | gzip -9 > /dev/null
或
stress-ng --cpu 4 --timeout 4m
```

运行结果：

![[b69a95f531.jpg]]

等待1分钟

![[34029c1f96.jpg]]

邮件、电话、微信告警，如下图所示：

![[5327b01317.jpg]]

## **3.** 总结报警不成功的可能原因

各服务器之间时间不同步，这样时序数据会出问题，也会造成报警出问题

必须写通知内容，留空内容是不会发报警的

修改完报警配置后，记得要点右上角的保存

保存配置后，需由Normal状态变为Pending状态才会报警，然后Pending持续一定时间，直到状态变更为Firing发起告警

grafana与onealert通信有问题

# 今日重点

- [x] MySQL逻辑备份、物理备份、在线热备（推荐GTID、MGR）
- [x] Prometheus监控系统 => 安装部署、监控Linux、监控MySQL、尝试监控其他应用（如Nginx）、配置监控
- [x] 面试宝典刷一刷尤其MySQL
- [x] 系统层面（cpu、磁盘、内存、网络、io、负载等系统命令回顾回顾）
- [x] 预习：Nginx软件

![[2af94ea911.png]]

上线生产需要上报领导并严格测试