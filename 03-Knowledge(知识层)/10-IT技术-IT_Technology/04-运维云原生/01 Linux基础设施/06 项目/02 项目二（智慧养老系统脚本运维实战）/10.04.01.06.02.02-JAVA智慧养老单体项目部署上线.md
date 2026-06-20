## 1- 部署架构说明

![[附件/c51ef44285.png]]

## 2- 各节点部署说明

![[附件/e6edfaef10.png]]

本次共计采用三台服务器完成部署任务:

|   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|服务器节点|数据库服务|redis服务|Nginx服务|Tomcat|DNS服务|日志服务|时间同步服务器||
|node1(192.168.88.101)|√|√||||√|node3同步||
|node2(192.168.88.102)||||√(安装JDK)|||node3同步||
|node3(192.168.88.103)|||√||√||√||

## 3- 各节点初始化环境

- 1- 确保三台服务器的网卡配置要求

```
ip： 
    节点一： 192.168.88.101
    节点二： 192.168.88.102
    节点三： 192.168.88.103

网关： 192.168.88.2

子网掩码： 255.255.255.0

DNS： 8.8.8.8

通过Ping 测试网络是否通畅
```

- 2- 确保三台服务器的主机名

```
节点一主机名： node1.itcast.cn
节点二主机名： node2.itcast.cn
节点三主机名： node3.itcast.cn

三个节点的hosts文件统一添加：
192.168.88.101 node1 node1.itcast.cn
192.168.88.102 node2 node2.itcast.cn
192.168.88.103 node3 node3.itcast.cn
```

- 3- 确保三个节点SSH互通
- 4- 关闭SELinux深层防火墙

![[附件/3b61acada0.png]]

## 4- 时间同步服务器配置

需求: node3为NTP服务器，需要连接外部互联网进行时间同步， node1和node2均与node3进行时间同步操作

```
外部数据源： 
    阿里云与腾讯云
```

- 1- 配置node3的NTP的服务器： chrony 服务 默认存在的

```
修改NTP服务器核心配置文件：
vim /etc/chrony.conf

# 时间源配置：
# pool 2.centos.pool.ntp.org iburst
pool ntp.aliyun.com iburst
pool ntp.tencent.com iburst

# 允许88网段客户端， 向时间同步服务器同步时间
#allow 192.168.0.0/16
allow 192.168.88.0/24

# 打开最后一行 详细日志记录
log measurements statistics tracking
```

- 2- 重启NTP服务

```
systemctl restart chronyd
```

![[附件/d1a3df72b9.png]]

- 3- node3节点， 放行NTP服务

```
# 添加ntp服务放行规则
firewall-cmd --add-service=ntp --permanent

# 重新加载规则
firewall-cmd --reload

# 查看规则是否生效
firewall-cmd --list-all
```

![[附件/a73f14c579.png]]

- 4- 修改 node1和node2的NTP核心配置文件，让其时间源指向node3服务

```
# node1和ndoe2都要修改
vim /etc/chrony.conf

# 数据源：
# pool 2.centos.pool.ntp.org iburst
pool 192.168.88.103 iburst


注意： 如果该配置文件， 之间有污染（改动）建议将之前的内容修改回来
```

![[附件/d4e6cc486b.png]]

- 5- 重启node1和node2的NTP服务

```
# node1 和 node2都要执行
systemctl restart chronyd
```

- 6- 测试操作： 观察 node1和node2是否连接到node3ntp服务

```
chronyc sources
```

node1界面：

![[附件/5d4cd00c10.png]]

node2界面：

![[附件/1db193a7de.png]]

## 5- 配置数据库服务【node1】

### 5.1 安装MySQL

- 1- 安装MySQL官方dnf(yum)仓库:

```
dnf install -y https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm

# 原因： 默认的dnf仓库存在更新不及时，版本可能会老旧的情况
```

![[附件/a82cd87912.png]]

- 2- 查看是否启用MySQL8.0仓库

```
dnf repolist enabled | grep mysql
```

![[附件/a256beff75.png]]

- 3- 安装MySQL8

```
dnf install -y mysql-community-server --nogpgcheck

--nogpgcheck : 跳过 GPG 检查,当安装链接是可信的，建议直接跳过，避免由于网络等跟其他原因导致无法安装
        GPG（GNU Privacy Guard）是一种开源的加密工具，用于保障数据的安全性和真实性，主要用于加密、解密和数字签名验证。它的核心作用是通过公钥和私钥的机制提供数据完整性和防篡改验证。
```

![[附件/31d5a51721.png]]

![[附件/1dc247ac8c.png]]

- 4- 启动MySQL相关服务

```
systemctl start mysqld
systemctl enable mysqld
systemctl status mysqld
```

![[附件/01cfdf5b36.png]]

- 5- 获取MySQL初始root密码

安装 MySQL 后，会生成一个随机的 root 密码, 可以通过MySQL的启动日志来查看

```
日志放置位置： /var/log/mysqld.log

grep password /var/log/mysqld.log
```

![[附件/be2d086485.png]]

- 6- 登陆MySQL，重新设置密码

```
mysql_secure_installation
```

![[附件/1d420584c7.png]]

- 7- 测试登陆

```
mysql -uroot -p[密码]   可以省略密码 直接回车，然后输入密码  

注意：此密码就是最新设置的 Aa123456.
```

![[附件/92aa617c37.png]]

```
-- 配置远程连接访问的root用户密码【直接执行即可，暂时不需要关心】：
CREATE USER 'root'@'%' IDENTIFIED BY 'Aa123456.';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;


执行完成后，可以直接quit退出或者使用ctrl +D 即可退出
```

- 8- 开放防火墙服务/端口号

```
# 允许 MySQL 服务
firewall-cmd --zone=public --add-service=mysql --permanent

# 或者开放 3306 端口
firewall-cmd --zone=public --add-port=3306/tcp --permanent

# 让规则立即生效
firewall-cmd --reload

# 验证防火墙规则
firewall-cmd --list-all
```

![[附件/40987f26ca.png]]

- 9- 通过远程可视化工具访问：

![[附件/ac14312d47.png]]

- 添加数据库的驱动包： 用于连接数据库

![[附件/81926392e0.png]]

![[附件/60ad6ae7bb.png]]

![[附件/1e252cecd9.png]]

![[附件/3b70dd3c1c.png]]

![[附件/d687c3e3f9.png]]

### 5.2 导入基础数据

- 1- 显示所有的数据库信息

![[附件/b3a376de0f.png]]

- 2- 运行SQL脚本, 导入初始化数据

![[附件/b29092a8aa.png]]

![[附件/f12835b482.png]]

![[附件/1256ada3f7.png]]

![[附件/d4a6311367.png]]

## 6- 配置Redis服务【node1】

部署操作:

- 步骤一: 安装Redis服务

```
# 更新dnf相关软件包 【可选】  时间较长 预计20分钟
dnf update -y
# 安装redis操作
dnf install redis -y
```

![[附件/453548c1c1.png]]

- 步骤二： 修改Redis相关配置

```
vim  /etc/redis/redis.conf
# 83行附件， 修改为  * -::*  任意的服务都可以连接redis服务
bind * -::*

#908行附近： 打开requirepass，设置其密码为123456 【可选】
requirepass 123456
```

- 步骤三： 启动redis进程

```
systemctl start redis
systemctl enable redis

查看状态：
systemctl status redis
```

![[附件/335c520fa2.png]]

- 步骤四： 测试redis服务

```
redis-cli 【-a 密码】

或
redis-cli  命令 进入客户端， 然后输入 auth 123456

退出客户端： quit 或 ctrl +d
```

![[附件/9d4ca4be3b.png]]

- 步骤五：开放防火墙

```
firewall-cmd --add-service=redis --permanent
或
firewall-cmd --add-port=6379/tcp --add-port=6379/udp --permanent

重新加载：
firewall-cmd --reload

#查看规则信息
firewall-cmd --list-all
```

![[附件/e26c6023cd.png]]

## 7- 部署阿里云OSS

阿里云的 **OSS**（Object Storage Service）是一个 **云端对象存储服务**，简单来说，它就像是一个 **网上的硬盘**，用来存储和管理各种文件（比如图片、视频、文档等）。你可以把它理解为一个 **可以随时访问、随时上传文件的网盘**，不过它比普通网盘更强大，专门为大规模的数据存储和管理设计。

特点：

- **像硬盘，但在云上**：你把文件存到阿里云的OSS上，就像把文件放进云端的一个“网盘”中，而这个网盘可以存很多很多数据。
- **可以随时随地访问**：无论你身处哪里，只要有网络，就可以随时上传、下载、管理这些文件。
- **适合大规模数据存储**：不仅可以存普通文件，还能处理海量数据，比如网站的图片、视频，甚至是备份文件等。

---

- 步骤一：在阿里云中开通OSS服务

![[附件/9864109939.png]]

购买中： 仅需要选择开通服务即可

- 注意： 这里不用写立即购买， 选择立即开通即可， 一旦开通了， 就没有这个按钮了

![[附件/27f771eefc.png]]

如果是第一次使用， 可以直接选择免费试用

![[附件/cc5350c6fe.png]]

- 步骤二： 进入到对象存储管理控制台

![[附件/b145a7fbd5.png]]

![[附件/5a9d1d6c2f.png]]

- 步骤三： 创建存储backet桶（容器）

![[附件/d989424ad6.png]]

- 步骤四： 进入bucket， 设置为公用， 方便访问

![[附件/539a6585f4.png]]

![[附件/c2d4d59fac.png]]

- 生成访问accessKey，用于授权访问OSS服务

![[附件/603a419f3c.png]]

![[附件/80aac0a6bb.png]]

![[附件/fb1a614e4e.png]]

![[附件/34a837faaa.png]]

![[附件/246f0f1705.png]]

- 步骤五： 修改项目中关于OSS服务的配置信息

```
accessKeyId: 授权ID
  accessKeySecret: 授权Secret
  bucketName: 刚刚在oss创建的bucket
```

![[附件/4bb451446a.png]]

## 8- 申请百度千帆大模型授权【可选】

项目中, 主要是基于百度千帆大模型来分析用户的体检报告, 故需要注册百度千帆大模型APK, 从而对接百度千帆大模型. 生产环境中, 此位置一般选择为公司生产环境的百度千帆账号

- 注册地址：https://qianfan.cloud.baidu.com/

![[附件/baa61f4d07.png]]

**实名认证**:

有了账号之后，我们需要**个人实名认证，**不然大模型调用不了，其中实名认证大家需要在手机端进行操作

1. 在手机上下载一个百度智能云app

![[附件/a961cde673.png]]

1. 使用刚刚注册的账号进行登录，找到**我的**，**个人中心**，可以进行实名认证操作

![[附件/942a45bbe2.png]]

注册后, 赠送20元优惠卷, 有效期1个月

**创建应用**

实名认证成功之后，我们继续在PC端来访问千帆大模型，地址：https://qianfan.cloud.baidu.com/

进入到管理平台

![[附件/71cf76904c.png]]

进入管理平台后，找到**应用接入**，我们需要创建新的应用，只有创建了应用，后面才能让大模型来绑定应用使用

![[附件/16552b3b4b.png]]

应用创建之后，可以查看自己的应用信息，其中就包含了一些秘钥信息，不要随意泄漏，如下图

![[附件/e917fef78b.png]]

---

设置应用到项目中:

```
accessKey: API KEY
  secretKey: 对应的secret key
  qianfanModel: ERNIE-4.0-8K-Preview(模型选择)
```

![[附件/70aff97e54.png]]

## 9- 后台管理系统打包部署

### 9.0 在打包部署前, 先在IDEA单独启动, 确定是否可以正常驱动

![[附件/1363acb81f.png]]

![[附件/d656a1d0bb.png]]

可能常见错误:

在错误界面 按下 ctrl+f 搜索 caused 查看最后1~2个 caused by 内容即可, 找关键词

- 错误一: 看到有OSS的错误

![[附件/46794f9ef0.png]]

```
原有: 大概率是由于阿里云的OSS的配置失败导致, 不管之前是否有配置,都重新配置一遍,尤其生成acccess key相关内容【建议：重新生成， 重新填写】

需要注意： 修改的 zzyl-admin --> resources -->  application-prod.yml  

千万别改错配置文件了,否则改了也是白改
```

- 错误二: 关键词 MYSQL JDBC

![[附件/35bb725eeb.png]]

```
此时, 一定是跟MySQL相关的问题:  
    通过一个错误, connection time out  连接超时 , 说明程序无法连接到MySQL服务器
    
    可能得原因:
        1- 远端MySQL服务器宕机了
        2- 防火墙没有放行MySQL
        3- application-prod.yml 配置文件中写错了连接数据库的信息了, 比如IP写错了 或者写错了端口号
    
    解决方案:
        1- 重启MySQL服务 -- 看安装MySQL笔记去
        2- 放行MySQL的服务
        3- 拿错了改哪里了
```

- 错误三: access password SQL

![[附件/64e40207c7.png]]

```
看到这些关键词, 也跟MySQL有关, 一般是由于数据库的密码写错了导致的原因

当然还有特殊情况: 比如没有开启远程访问操作
    也就是说: 以下三行没有在MySQL中执行操作
        CREATE USER 'root'@'%' IDENTIFIED BY 'Aa123456.';
        GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
        FLUSH PRIVILEGES;

解决方案:
    如果是密码写错了, 更改为正确密码
    
    如果不是这个错误, 就在linux中 通过mysql -uroot -p密码  登录成功后, 输入上面的三行SQL语句即可
```

- 错误四: SQL Ubknown database

![[附件/ddb07f8553.png]]

```
该错误, 也是由于MySQL的错误, 由于安装完mysql 没有即使将数据导入导致的问题, 此时只需要查看我们课件中5.2的位置, 将数据导入即可
```

- 错误五: 关键词 6379 connection refused(连接拒绝)

![[附件/bce159a3e0.png]]

```
看到 6379的错误, 一般与redis服务器有关系

可能出现的错误的原因:
    由于redis没有开启支持远程访问的监听方案, 导致远端无法访问
    
    解决访问:
        修改linux的 /etc/redis/redis.conf 中 bind配置, 具体可以参考redis安装
        
    大家的主要原因: 很多同学是新增了 bind配置, 没有把原有bind给删除掉(注释掉)
    
    
    注意, 我们redis是安装到192.168.88.101 如果显示的IP不是这个IP地址, 说明 application-prod.yml 配置文件中关于redis的地址配置错误
```

- 错误五: 关键词 6379 unable to connect(无法连接)

![[附件/4a9bc334bd.png]]

```
该错误, 表示客户端无法连接到redis服务器, 一般是由于防火墙导致的原因, 将防火墙开启即可


注意, 我们redis是安装到192.168.88.101 如果显示的IP不是这个IP地址, 说明 application-prod.yml 配置文件中关于redis的地址配置错误
```

### 9.1 在node2中部署JDK11

- 1- 在node2中创建放置jdk11的安装包目录

```
mkdir -p /export/software
```

- 2- 将资料中提供的jdk11的安装包上传到此目录下

![[附件/702cf78345.png]]

- 3- 对jdk11安装包进行解压： 解压到 /opt

```
tar -xzf openjdk-11.0.0.2_linux-x64.tar.gz -C /opt/

cd /opt/

输入 ll 查看
```

![[附件/26f3b2d70d.png]]

- 4- 配置JDK的环境变量

```
vim /etc/profile

在文件的尾部添加： 
# JAVA_HOME
export JAVA_HOME=/opt/jdk-11.0.0.2



保存退出后，执行加载操作：
source /etc/profile


校验:
java -version
```

![[附件/9d450c16d0.png]]

### 9.2 生产环境配置操作

- 1- 调整运行模式为生产环境配置

![[附件/e53aa2f207.png]]

- 2- 修改生产环境配置连接信息， 确保可以正常连接到生产环境服务器

![[附件/03b59fcac8.png]]

![[附件/bbd7501c18.png]]

![[附件/96f218c3f4.png]]

### 9.3 方式一：jar包运行

由于该项目是基于Spring Boot框架开发的， Spring Boot 提供了嵌入式的 Web 容器（如 Tomcat、Jetty、Undertow），使得应用无需外部容器即可运行。

当打包为 JAR 时，Spring Boot 会将嵌入式服务器作为依赖一起打包到 JAR 中。

应用通过 `main` 方法启动时，嵌入式服务器会随之启动，从而直接运行。

如何实现呢？

![[附件/adbcc55b85.png]]

执行打包操作：

对于Maven项目来说， 本身提供了关于项目管理的相关命令，这里就包括打包命令

![[附件/157654ca0f.png]]

本项目结构：

![[附件/23b1f710fa.png]]

对项目进行打包： 由于项目之间存在依赖关系， 我们无法直接仅在程序入口工程进行打包， 此时可以选择直接针对父工程打包

注意： 项目不能时启动的状态， 一定要停止项目

![[附件/3b190a9e13.png]]

- 第一步： 先执行清理操作， 确保项目无杂质历史信息

![[附件/0e296b5d3b.png]]

执行日志可以看到:

![[附件/02823a5c7e.png]]

- 第二步： 去除test命令

- 默认情况下, 在执行打包之前, 会先运行编辑和测试操作, 建议在正式打包前,将测试命令从流程中删除

![[附件/0b2098fa9c.png]]

- 第三步: 执行打包操作

![[附件/45d25af7aa.png]]

![[附件/948bb24c6d.png]]

查看核心工程: zzyl-admin的包

![[附件/b1f42243ae.png]]

打开该jar包路径：

![[附件/3fccc77693.png]]

![[附件/ec52cba3a2.png]]

---

尝试上传运行：

- 1- 在node2中创建目录，用于放置该jar包

```
mkdir -p /opt/zzyl_project
```

- 2- 上传jar包到此目录下

![[附件/34d54c8a28.png]]

- 3- 执行jar包

```
格式：
    java -jar  运行的jar包

例如：
    cd /opt/zzyl_project
    java -jar zzyl-admin.jar
```

![[附件/cd73fe6df5.png]]

![[附件/885c726619.png]]

当后台可以正常启动后，可以通过在vscode中启动前台界面， 查看是否可以正常访问

- 服务器开启防火墙： 由于占用了前面窗口， 导致无法输入命令 需要重新复制一个新的标签页输入

```
开放 9000 端口
firewall-cmd --zone=public --add-port=9000/tcp --permanent  

# 让规则立即生效
firewall-cmd --reload

验证防火墙规则
firewall-cmd --list-all
```

- 修改前端代码

![[附件/d1cd322207.png]]

- 启动访问：

![[附件/87a0446c0d.png]]

即可看到：

![[附件/ee43df2b4f.png]]

---

没啥问题后， 即可将其挂载到后台运行：

```
先 crtl + c 退出当前jar包

然后执行：
nohup java -jar zzyl-admin.jar 2>&1 >/dev/null &

校验：
jps ： 查看Java的进程
ps -ef | grep java 查看java进程
```

![[附件/79c63bebfb.png]]

---

思考： 通过 >/dev/null 将全部日志取消了， 如何查看日志呢？

```
说明：
    对于本项目， 项目本身提供的日志记录的方案， 在项目中，专门有一个配置文件logback.xml  记录了日志的记录行为
```

![[附件/72f9f9bcbb.png]]

查看该目录下的日志：

![[附件/7fdb7691a7.png]]

在配置文件，对这几个配置文件的滚动行为也做了记录（轮替）

- 系统（项目）的普通日志

![[附件/2fa85be310.png]]

- 系统（项目）的错误日志

![[附件/44b9232f51.png]]

- 系统（项目）的用户日志

![[附件/15e8e29530.png]]

---

创建错误:

![[附件/01032057dd.png]]

表示: 当前环境中, 已经有一个程序启动了, 如果在重复启动, 就会报这个错误

解决方案: 通过 ps -ef | grep java 查看对应java进程, 查看后使用kill -9 将其杀死, 然后就可以正常启动了

### 9.4 方式二：基于tomcat运行

在配置之前， 请先将基于jar包的运行的对应程序直接kill掉， 可以通过jps命令查看对应进程ID，然后使用kill -9 杀死

如何实现呢？

![[附件/2648ba63f6.png]]

执行打包操作：

对于Maven项目来说， 本身提供了关于项目管理的相关命令，这里就包括打包命令

![[附件/ecba5fdf65.png]]

本项目结构：

![[附件/95ab7427a0.png]]

对项目进行打包： 由于项目之间存在依赖关系， 我们无法之间仅在程序入口工程进行打包， 此时可以选择之间针对父工程打包

- 第一步： 先执行清理操作， 确保项目无杂质历史信息

![[附件/87f8acf32f.png]]

执行日志可以看到:

![[附件/bc28a7a1a2.png]]

- 第二步： 去除test命令

- 默认情况下, 在执行打包之前, 会先运行编辑和测试操作, 建议在正式打包前,将测试命令从流程中删除

![[附件/2244f9be92.png]]

- 第三步: 执行打包操作

![[附件/7570140209.png]]

![[附件/1e5948d759.png]]

查看核心工程: zzyl-admin的包

![[附件/61b1200dd4.png]]

打开该jar包路径：

![[附件/88e491118d.png]]

![[附件/dcf71f521f.png]]

![[附件/daa86a246b.png]]

---

尝试运行：

- 1- 安装Tomcat服务器：

![[附件/291b133624.png]]

- 1.1 上传Tomcat到node2的 /export/software下

![[附件/75aa1f0013.png]]

- 1.2- 解压Tomcat服务器到/opt目录下

```
cd /export/software/
tar -xzf apache-tomcat-9.0.97.tar.gz -C /opt/

cd /opt/
```

![[附件/d91a18a34e.png]]

tomcat目录介绍：

![[附件/f9f2764281.png]]

- 1.3- 启动Tomcat服务器

```
cd /opt/apache-tomcat-9.0.97/bin
./startup.sh
```

![[附件/105840e694.png]]

- 如何查看是否启动？

```
可以通过进程，查看是否有Tomcat进程信息：
ps -ef | grep tomcat
```

![[附件/3ba2de7397.png]]

- 1.4- 添加防火墙配置，允许tomcat请求正常访问

```
开放 8080 端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent  

# 让规则立即生效
firewall-cmd --reload

验证防火墙规则
firewall-cmd --list-all
```

![[附件/ca198fd6f4.png]]

- 1.5- 浏览器测试访问：http://192.168.88.102:8080

![[附件/14b9028431.png]]

说明： Tmcat默认展示的页面其实就是来源于Tomcat目录下的webapps中，有一个ROOT目录的内容

![[附件/8009cacc2e.png]]

如果是其他的项目，在访问的时候， 就需要添加上对应的目录的名称（也就是项目的名称）

- 1.6 上传中州养老后台管理系统项目到webapps目录下

- 6.0 关闭tomcat服务器

```
cd  /opt/apache-tomcat-9.0.97/bin/
./shutdown.sh

验证：ps -ef | grep tomcat  确保tomcat进程已经关闭了
```

![[附件/80ffe75ba4.png]]

- 6.1 上传至webapps目录下

![[附件/defd09669f.png]]

- 6.2 启动tomcat服务器

```
cd /opt/apache-tomcat-9.0.97
./bin/shutdown.sh
./bin/startup.sh
```

![[附件/481439bac8.png]]

查看日志： tail -100f logs/catalina.out

即可看到：

![[附件/16f9af1cdc.png]]

![[附件/ee03916b52.png]]

可以通过日志， 观察启动过程中是否有报错即可

此时我们再看webapps目录下

![[附件/0db18d5516.png]]

```
说明：这时候就有了一个zzyl-admin的目录。 注意： 后续访问该项目 需要增加zzyl-admin的名称 才可以

例如：http://192.168.88.102:8080/zzyl-admin 这是项目的标准路径


如果希望为：http://192.168.88.102:8080/

可以将项目的名称更改为ROOT即可，类似于我们基础班，但是由于该项目仅为后台服务， 并无前端页面，对用户访问不会产生影响， 故本次不设置也OK
```

当tomcat可以正常启动后，可以通过在vscode中启动前台界面， 查看是否可以正常访问

- 修改前端代码： **记得保存哈**

![[附件/d022eb0e3c.png]]

- 启动访问：

![[附件/b76590de32.png]]

即可看到：

![[附件/1b04d56185.png]]

## 10. 前端系统部署操作

### 10.1 在Linux中安装Nginx服务器

Nginx（发音为“Engine-X”）是一款高性能的**Web服务器**和**反向代理服务器**。它最初是为了提供更高效的静态文件处理而设计的，但现在广泛应用于**负载均衡**、**反向代理**、**缓存**等多种用途。基于C语言开发，在合适的硬件上（如多核 CPU 和足够的内存），Nginx 可以处理 **50,000 到 100,000 个并发连接**，甚至更多。

![[附件/f89cbe1e46.png]]

**Nginx 能做什么？**

1. **Web 服务器**：它可以处理并响应来自用户的 HTTP 请求，展示网站内容。
2. **反向代理服务器**：它接收用户的请求，然后将请求转发给其他服务器来处理。这对于负载均衡和保护后端服务器很有用。
3. **负载均衡**：它可以把用户的请求分配到多个后端服务器上，从而减少单一服务器的负担，提高网站的稳定性和处理能力。
4. **缓存**：它可以缓存常用的内容，提高网站响应速度，减轻后端服务器的压力。
5. **SSL/TLS 加密**：支持 HTTPS，保护网站与用户之间的通信安全。
6. **反向代理 + 负载均衡的组合**：常用于大规模网站，将用户请求分配到不同的服务器，增强性能和可扩展性。

```
做网站的“服务员”：当你输入网址，Nginx 就像一个服务员，快速地把网页内容从服务器里拿出来，展示出来。

分担工作量：如果网站的流量非常大，Nginx 会把请求分发给多个后端服务器，这样每个服务器的负担不至于太重，网站也更稳定。这就像是有多个服务员来分担工作，避免一个服务员忙不过来。

缓存加速：Nginx 还会记住一些常用的网页，直接从记忆中取出来给你，避免每次都从头开始拿，提高访问速度。

保安：Nginx 也能充当网站的“保安”，通过 HTTPS（加密通信）保护用户和网站之间的信息安全。
```

如何部署Nginx服务器呢？ 【node3】

- 1- 安装Nginx服务器

```
dnf install nginx -y
```

- 2- 启动并启用 Nginx 服务

```
systemctl start nginx
systemctl enable nginx
# 查看状态信息
systemctl status nginx
```

![[附件/29a15e4dfc.png]]

- 3- 配置防火墙：

```
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --zone=public --add-service=https --permanent

或者：
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent

# 重新加载规则信息
firewall-cmd --reload

# 查看规则信息
firewall-cmd --list-all
```

![[附件/b77cb03379.png]]

- 4- 测试是否可以访问

```
http://192.168.88.103
```

![[附件/5d5755cddd.png]]

能看到Nginx 的欢迎页面，说明 Nginx 已成功部署

---

Nginx的目录结构介绍

- /etc/nginx/ 目录 【重要】

这是 Nginx 的 主配置目录，存放所有与 Nginx 配置相关的文件。主要包括：

```
nginx.conf：
    Nginx 的主配置文件。这里配置了全局设置、HTTP 服务设置、加载的模块等。
conf.d/：
    存放额外配置文件的目录，通常用于配置虚拟主机等。你可以在这里添加 .conf 文件来定义多个站点的配置。

mime.types：
    定义了不同文件类型（MIME类型）与扩展名之间的映射，通常 Nginx 会根据这个文件来判断文件的类型。
```

- /var/www/目录 【重要】

默认情况下，Nginx 的网站文件（例如 HTML、图片等）通常存放在这个目录下

```
/var/www/html/：这是 Nginx 默认的根目录。你放置的静态文件会从这个目录提供给客户端。默认情况下，index.html 会作为首页展示
```

- /usr/share/nginx/目录

这个目录通常包含与 Nginx 程序相关的文件

```
/usr/share/nginx/html/ ：
    Nginx 默认的网页目录，通常安装时会有一个默认的 index.html 文件，用来验证 Nginx 是否成功安装。
```

- /var/log/nginx/目录 【重要】

Nginx 会把日志文件存放在这个目录下。日志文件帮助你监控 Nginx 的运行情况，排查问题

```
access.log：记录所有的客户端请求，包括请求的 URL、响应状态码、请求来源等。
error.log：记录 Nginx 在运行时遇到的错误信息、警告等。
```

### 10.2 对前端项目进行打包

- 1- 在终端中， 执行打包命令

```
npm run build:prod
```

![[附件/521eda9af8.png]]

使用当前命令的原因： 开发人员在package.json 这个核心配置文件中， 定义了如何打包， 使用什么命令

![[附件/a4706abbac.png]]

```
package.json 中的 scripts 配置， 主要是为了简化和标准化常用的命令操作，项目已经定义了多个构建命令，分别为：

dev: 启动开发服务器，使用 Vite（运行 vite 命令）。
build:prod: 打包项目用于生产环境（运行 vite build）。 
build:stage: 打包项目用于 staging 环境（运行 vite build --mode staging） 构建预发布（阶段环境）代码
preview: 预览生产构建后的内容（运行 vite preview）。
```

---

打包执行完成后， 在项目中就会出来一个dist目录，该文件夹内将包含 HTML、CSS、JavaScript 等资源文件，准备部署到生产环境。

![[附件/0c800eefc5.png]]

![[附件/08ab7dd10c.png]]

### 10.3 在Nginx中配置操作

- 1- 将dist目录上传到/var/www/目录下，如果目标路径不存在， 手动创建

```
mkdir -p /var/www/

将disk上传到此目录下
```

![[附件/db1983aa4c.png]]

- 2- 配置Nginx的配置文件

```
vim /etc/nginx/nginx.conf

# 添加相关内容：
# 在HTTP的目录下， 添加以下三个add_header   CORS 配置
add_header Access-Control-Allow-Origin *;
add_header Access-Control-Allow-Methods "GET, POST, OPTIONS, PUT, DELETE";
add_header Access-Control-Allow-Headers "Origin, X-Requested-With, Content-Type, Accept, Authorization";


作用：
    这几行配置用于设置 跨域资源共享（CORS），它们在 Nginx 中用来允许其他域名访问你的资源。CORS 是一种机制，允许通过浏览器发起跨域 HTTP 请求，常用于 Web 应用与不同域名的 API 交互时，解决浏览器的同源策略限制。
```

![[附件/90c35a054c.png]]

```
在server中， 添加以下三行内容， 删除原有的server_name 和root
client_max_body_size 60m; # 限制客户端请求体的最大大小。
client_body_buffer_size 512k; # 设置 Nginx 用于缓冲客户端请求体的内存大小。
client_header_buffer_size 2k; # 设置 Nginx 用于缓冲请求头的内存大小。

说明
    这些配置项与 Nginx 处理客户端请求的请求体大小、请求头缓冲区等相关，主要用于控制 Nginx 在处理上传文件、请求体内容和请求头时的行为
```

![[附件/e1c1f4ec61.png]]

```
在server中，继续添加以下内容， 注意根据图片 确定放置位置
       # 处理 静态页面
       location / {
                root   /var/www/dist;
                index  index.html index.htm;
                proxy_set_header   Upgrade          $http_upgrade;
                proxy_set_header   Connection       upgrade;
                try_files $uri $uri/ /index.html;
        }
        # 处理反向代理
        location /prod-api/ {
                proxy_pass http://192.168.88.102:8080/zzyl-admin/;
                proxy_set_header   Upgrade          $http_upgrade;
                proxy_set_header   Connection       upgrade;
        }
```

![[附件/21e88aae52.png]]

- 3- 重启Nginx服务

```
重启 Nginx：
systemctl restart nginx

或
重新加载 Nginx 配置（不停止服务）：
nginx -s reload
```

![[附件/8d24c1119b.png]]

- 4- 刷新浏览器： 访问192.168.88.103想qa

![[附件/f43780b5c9.png]]

## 11. 配置DNS服务器

域名:

后台管理系统域名 Nginx: www.zzyl-itcast.cn 或 zzyl-itcast.cn

DNS服务器域名: ns.zzyl-itcast.cn

时间同步服务器域名: ntp.zzyl-itcast.cn

```
顶级域名:
    zzyl-itcast.cn

子域名:  www  ns  ntp  


域名对应要映射的IP地址:
    www.zzyl-itcast.cn :  192.168.88.103
    zzyl-itcast.cn  :  192.168.88.103
    
    ns.zzyl-itcast.cn : 192.168.88.103
    ntp.zzyl-itcast.cn : 192.168.88.103


注意: 在DNS中配置域名, 都是针对顶级域名配置正反向, 然后在正反向配置文件中, 配置顶级域名所对应的子域名
```

需求： 在node3配置DNS服务器， 完成最终解析操作， 同时windows连接服务器的DNS， 实现域名访问

## 12. 日志服务

需求： 要求在node1节点中，单独挂载一块磁盘， 用于存储中州养老的日志数据，同时支持后续扩容使用

```
初始磁盘大小： 50GB
采用LVM方案
挂载点： /mnt/zzyl_logs

日志需求说明： 
    日志：
        Nginx node3的access.log和error.log: 开启日志轮替方案， 每日轮替一次，至少保留6个版本【轮替文件时存在的， 只需要将版本调整为6即可】
        

        后台系统 node2： /home/ruoyi/logs/  已自动有轮替，无需配置
                 sys-info.2024-12-28.log
                 sys-user.2024-12-28.log
                 sys-error.2024-12-28.log
                         

对日志，进行周期性同步， 每日凌晨1点， 准时同步之前（不含当天日志）的 Nginx和后台系统日志到/mnt/zzyl_logs

注意： 涉及到名字的命名， 要求见名知意即可，可以任意定义


需求: 只能同步上一天及其之前的数据
数据同步:
    数据源:
        node2: /home/ruoyi/logs/  有三个日志文件
            sys-info.2024-12-28.log
            sys-user.2024-12-28.log
            sys-error.2024-12-28.log
        node3:  /var/log/nginx 有二个日志文件
            access.log-20250331
            error.log-20250331
        
    
    目的地: 
        node1: /mnt/zzyl_logs
        
        

命令操作: 
    同步远端 node2:  在node1执行同步命令
    rsync -avz --delete  root@192.168.88.102:/home/ruoyi/logs/sys-*.*.log  /mnt/zzyl_logs

    同步远端 node3:  在node1执行同步命令
    rsync -avz --delete  root@192.168.88.103:/var/log/nginx/*.log-*  /mnt/zzyl_logs


配置定时操作: 仅在node1即可    每日凌晨1点


编写定时器: crontab -e
输入 i 进入插入模式:
添加以下二行内容:
0 1 * * * /usr/bin/rsync -avz --delete  root@192.168.88.102:/home/ruoyi/logs/sys-*.*.log  /mnt/zzyl_logs
0 1 * * * /usr/bin/rsync -avz --delete  root@192.168.88.103:/var/log/nginx/*.log-*  /mnt/zzyl_logs
```

![[附件/3071337ed7.png]]