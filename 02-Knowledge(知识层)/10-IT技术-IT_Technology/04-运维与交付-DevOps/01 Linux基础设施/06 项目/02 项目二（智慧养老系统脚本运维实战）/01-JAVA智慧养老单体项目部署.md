## 1. 【了解】项目基本介绍

中国老龄化程度加深，我国老龄事业和养老服务体系的发展得到了国家的高度重视，在国家政策的支持下，我国智慧养老产业主体持续增多，产业链不断整合，发展前景较好。我国正在形成一个多元化“互联网+养老”的智慧老年护理服务系统，智慧养老是我国的必然趋势

整体业务流程:

中州养老系统为养老院量身定制开发专业的养老管理软件产品；涵盖来访管理、入退管理、在住管理、服务管理、财务管理等功能模块，涉及从来访参观到退住办理的完整流程。

![[f7c1e9dccc.png]]

**项目原型**访问地址：https://codesign.qq.com/s/459277624064324 密码: FSTI

中州养老项目分为两端，一个是管理后台，另外一个是家属端

- 管理后台：养老院员工使用，入住、退住，给老人服务记录等等
- 家属端：养老院的老人家属使用，查看老人信息，缴费，下订单等等

![[995d0857b7.png]]

业务主页效果：

![[29503164dd.png]]

![[6395b46d5d.png]]

## 2.【了解】技术架构

下图展现了中州养老项目主要使用的技术：

![[2fb48f99fb.png]]

- 前端主要使用的Vue3+Element Plus
- 后端主要使用的是若依框架作为基础架构，当然后端也集成了很多其他的技术，比如有Springboot、Mybatis、Swagger、Spring cache、Spring Security、Mybatis-plus等
- 数据存储主要使用到了MySQL和Redis
- 使用了nginx来作为反向代理和前端的静态服务器
- 其他技术：阿里云物联网平台IOT、对象存储OSS、微信登录、百度千帆大模型、AI工具辅助开发等

项目采用**前后端分离的开发模式**， 在部署的时候， 需要单独对项目前端服务和后端服务进行部署操作

技术选型

```
1 系统环境
Java EE 8  ---> jdk 11
Servlet 3.0
Apache Maven 3

2 主框架
Spring Boot 2.2.x
Spring Framework 5.2.x
Spring Security 5.2.x   安全框架

3 持久层
Apache MyBatis 3.5.x
Hibernate Validation 6.0.x   校验框架
Alibaba Druid 1.2.x

4 视图层
Vue 2.6.x   ---->  Vue3
Axios 0.21.x
Element 2.15.x  ---->  Element Plus
```

## 3. 【理解】什么是前后端分离开发

**前后端分离开发**，就是在项目开发过程中，对于前端代码的开发由专门的前端人员负责，后端代码则由后端开发人员负责，这样可以做到分工明确、各司其职、提高开发效率，前后端代码并行开发，可以加快项目开发进度。目前，前后端分离开发方式已经被越来越多的公司所采用，成为当前项目开发的主流的方式

前台和后台部署在不同的服务器上，开发的时候约定一个接口，然后各自去开发，并且可以单独进行测试用例。在开发的途中前后台可以不相互依赖，并且上线后前后台的耦合度也比较低。

前后端开发，从项目工程结构也发发生变化， 即前后端代码不再混合在同一个项目工程中，而是分为前端工程和后端工程；

![[5dfb264bbf.png]]

开发流程：

前后端分离开发后， 面临的一个问题就是前端人员和后端人员如何来进行配合共同开发一个项目

![[1e59a073f7.png]]

接口 （API接口）：就是一个HTTP请求，主要就是去定义： 请求路径、请求方式、请求参数、响应数据等内容

例如：

![[2e064c4222.png]]

## 4. 智慧养老项目打包全过程

部署打包操作, 在实际运维场景中, 关于项目打包工作一般都是开发人员进行处理, 由开发人员对前端和后端项目进行打包,然后交由运维人员,最后协同运维人员一同完成线上环境部署并进行测试,确保上线稳定运行

这里主要是基于运维人员, 尤其对于经验相对更长久的运维人员, 或者未来大家慢慢走向运维开发方向的岗位,了解部署打包会让我们在工作中更加高效,还能帮助团队提高整体的交付质量。同时了解这项内容对运维的CI/CD持续交付以及DevOPS开发与运维高度融合的重要组成部分

### 4.1 后端开发环境搭建

#### 4.1.1 在win安装Java11环境

![[46c39691ef.png]]

![[5e256ac8b9.png]]

![[1d2d06bccc.png]]

![[99f2238487.png]]

安装后， 配置Java环境变量，让Windows全局可加载到Java环境

![[881c715445.png]]

![[cc5a3b5c26.png]]

![[53214362da.png]]

![[f636b66477.png]]

![[0b344c2c80.png]]

注意： **配置完成后， 所有的都要点击确认， 否则会导致配置失效**

验证： win + r 输入 cmd 回车

![[e564023bfc.png]]

#### 4.1.2 在win安装IDEA环境

本次我们安装的IDEA为2023 商业版本（专业版）

![[f5ee15f600.png]]

![[b544782fc5.png]]

![[cbd619839d.png]]

![[37c7b51da0.png]]

![[7d1e535638.png]]

![[8f3cfcad0c.png]]

尝试打开IDEA：

第一次可能会弹出以下界面:

![[0667cf48d4.png]]

![[f6c3b4e9b9.png]]

非第一次安装idea,直接跳入该界面:

![[482885bf6b.png]]

![[f1547a0b4d.png]]

![[2358153ef7.png]]

#### 4.1.3 尝试激活方案

请先将刚刚需要输入激活的界面关闭

【注意】本激活仅为后续使用方便，生产环境中请选择购买IDEA商业授权版本

- 1- 下载激活包：

- 首先打开这个网址 https://3.jetbra.in/ 等待测试延迟后选择一个进入

![[050edd8519.png]]

- 页面上方有一个jetbra.zip，点击下载

![[22a5713656.png]]

- 2- 下载后将其解压到IDEA的bin目录，**解压出来后ja-netfilter.jar应该是和idea64.exe在同一个目录**。

![[b857347c1f.png]]

- 3- 随后进入到scripts目录，执行`install-all-user.vbs`或者`install-current-user.vbs`会弹出一个提示框，点确定。

- **注意， 必须在IDEA的bin目录下的script目录中**

![[bff817fe48.png]]

![[0ceafc6696.png]]

**耐心等待一下**，这个花的时间可能会比较久，可能要好几分钟，之后会弹出提示框提示已完成。

![[b55b20fe37.png]]

- 4- 从刚刚下载ZIP包的页面中， 找到IDEA， 复制其激活码

![[b0191ce5b9.png]]

```
以下提供一个激活码： 如果页面中的无法复制，可以直接复制这里
FV8EM46DQYC5AW9-eyJsaWNlbnNlSWQiOiJGVjhFTTQ2RFFZQzVBVzkiLCJsaWNlbnNlZU5hbWUiOiJtZW5vcmFoIHBhcmFwZXQiLCJsaWNlbnNlZVR5cGUiOiJQRVJTT05BTCIsImFzc2lnbmVlTmFtZSI6IiIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiIiLCJjaGVja0NvbmN1cnJlbnRVc2UiOmZhbHNlLCJwcm9kdWN0cyI6W3siY29kZSI6IlBDV01QIiwiZmFsbGJhY2tEYXRlIjoiMjAyNi0wOS0xNCIsInBhaWRVcFRvIjoiMjAyNi0wOS0xNCIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQUlIiLCJmYWxsYmFja0RhdGUiOiIyMDI2LTA5LTE0IiwicGFpZFVwVG8iOiIyMDI2LTA5LTE0IiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlBEQiIsImZhbGxiYWNrRGF0ZSI6IjIwMjYtMDktMTQiLCJwYWlkVXBUbyI6IjIwMjYtMDktMTQiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUFNJIiwiZmFsbGJhY2tEYXRlIjoiMjAyNi0wOS0xNCIsInBhaWRVcFRvIjoiMjAyNi0wOS0xNCIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJJSSIsImZhbGxiYWNrRGF0ZSI6IjIwMjYtMDktMTQiLCJwYWlkVXBUbyI6IjIwMjYtMDktMTQiLCJleHRlbmRlZCI6ZmFsc2V9XSwibWV0YWRhdGEiOiIwMjIwMjQwNzAyUFNBWDAwMDAwNVgiLCJoYXNoIjoiMTIzNDU2NzgvMC01NDE4MTY2MjkiLCJncmFjZVBlcmlvZERheXMiOjcsImF1dG9Qcm9sb25nYXRlZCI6ZmFsc2UsImlzQXV0b1Byb2xvbmdhdGVkIjpmYWxzZSwidHJpYWwiOmZhbHNlLCJhaUFsbG93ZWQiOnRydWV9-cH8qBniG31nF8954hthJJuzF6Fk4RQ9T03IfNxsFkuxUcwaAGHKOcRudvBZIAbLwDDFw63q2QZsnpwthBb/6IqBYnJrjRC83a8wkYKGN8HqAyDtbqdLOxLjcaiAiSKzektfAXn6nGNfDeygcFr/WzMfI0on/43ByuwxmSrjwYc4M8SCR0nkDAi0XwXNnFp3vSp0gJQd+lJtkSHO2KR7gUyNDZOPVduljJGbdLJUK6UcUjrlAd6NrTNqpu5P7hcYRaNzjoJ0KeIx5k9KmMCdcfQBia/zSHUbwZiecFsyjxqtIU0C3TDaX1OM4siJVDpgrXi+ocY86hiiYE79ygJf2IA==-MIIETDCCAjSgAwIBAgIBDTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTIwMTAxOTA5MDU1M1oXDTIyMTAyMTA5MDU1M1owHzEdMBsGA1UEAwwUcHJvZDJ5LWZyb20tMjAyMDEwMTkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCUlaUFc1wf+CfY9wzFWEL2euKQ5nswqb57V8QZG7d7RoR6rwYUIXseTOAFq210oMEe++LCjzKDuqwDfsyhgDNTgZBPAaC4vUU2oy+XR+Fq8nBixWIsH668HeOnRK6RRhsr0rJzRB95aZ3EAPzBuQ2qPaNGm17pAX0Rd6MPRgjp75IWwI9eA6aMEdPQEVN7uyOtM5zSsjoj79Lbu1fjShOnQZuJcsV8tqnayeFkNzv2LTOlofU/Tbx502Ro073gGjoeRzNvrynAP03pL486P3KCAyiNPhDs2z8/COMrxRlZW5mfzo0xsK0dQGNH3UoG/9RVwHG4eS8LFpMTR9oetHZBAgMBAAGjgZkwgZYwCQYDVR0TBAIwADAdBgNVHQ4EFgQUJNoRIpb1hUHAk0foMSNM9MCEAv8wSAYDVR0jBEEwP4AUo562SGdCEjZBvW3gubSgUouX8bOhHKQaMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0GCCQDSbLGDsoN54TATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIBABKaDfYJk51mtYwUFK8xqhiZaYPd30TlmCmSAaGJ0eBpvkVeqA2jGYhAQRqFiAlFC63JKvWvRZO1iRuWCEfUMkdqQ9VQPXziE/BlsOIgrL6RlJfuFcEZ8TK3syIfIGQZNCxYhLLUuet2HE6LJYPQ5c0jH4kDooRpcVZ4rBxNwddpctUO2te9UU5/FjhioZQsPvd92qOTsV+8Cyl2fvNhNKD1Uu9ff5AkVIQn4JU23ozdB/R5oUlebwaTE6WZNBs+TA/qPj+5/we9NH71WRB0hqUoLI2AKKyiPw++FtN4Su1vsdDlrAzDj9ILjpjJKA1ImuVcG329/WTYIKysZ1CWK3zATg9BeCUPAV1pQy8ToXOq+RSYen6winZ2OO93eyHv2Iw5kbn1dqfBw1BuTE29V2FJKicJSu8iEOpfoafwJISXmz1wnnWL3V/0NxTulfWsXugOoLfv0ZIBP1xH9kmf22jjQ2JiHhQZP7ZDsreRrOeIQ/c4yR8IQvMLfC0WKQqrHu5ZzXTH4NO3CwGWSlTY74kE91zXB5mwWAx1jig+UXYc2w4RkVhy0//lOmVya/PEepuuTTI4+UJwC7qbVlh5zfhj8oTNUXgN0AOc+Q0/WFPl1aw5VV/VrO8FCoB15lFVlpKaQ1Yh+DVU8ke+rt9Th0BCHXe0uZOEmH0nOnH/0onD
```

- 5- 打开IDEA，输入激活码即可激活完成

![[9132fb2703.png]]

![[809d111d28.png]]

### 4.2 基于IDEA挂载后端项目

- 1- 将资料中的zzyl_后端.zip文件解压到一个没有中文和空格目录下

- 建议： 在IDEA的安装目录下，创建workspace目录， 然后将项目解压到此目录

![[4c95bd1d51.png]]

打开zzyl,即可看到项目的完整结构,如果看到里面还是zzyl目录, 解压去除最外层的结果,保持一层结构即可

![[c3de494409.png]]

- 2- 通过IDEA打开项目

![[bb4fd835ef.png]]

![[4005f24e48.png]]

![[f2c558707a.png]]

![[9f524f1edf.png]]

### 4.3 运行后端项目

由于该Java项目环境采用Maven进行构建的, 故需要先安装Maven环境

#### 4.3.1 Maven的基本介绍

![[3ab01ee237.png]]

Maven 是一个工具，专门用来帮 Java 程序员 **管理项目** 和 **处理依赖关系** 的。

**Maven 能干什么？**

- **自动下载依赖**： 写 Java 程序需要用到很多别人写好的工具包，Maven 能自动帮你找到并下载这些工具包，而不用你手动去找。
- **一键打包**： 写完代码后，Maven 可以帮你把代码打包成可以运行的文件（比如 `.jar` 或 `.war`），你不用自己一个个整理文件。
- **统一项目管理**： 用 Maven，项目的结构和流程都按照固定规则来，非常清晰，团队协作会更方便。
- **运行测试**： Maven 能自动运行代码里的测试，帮你检查代码是否有问题。
- **自动化构建**： 从编译代码到生成最终程序，Maven 能一条龙服务，不需要你一步步手动来。

Maven的仓库说明:

|   |   |
|---|---|
|仓库名称|作用|
|本地仓库|相当于缓存, 工程会从远程仓库(互联网)去下载jar包,将jar包存在本地仓库(在程序员的电脑上)。第二次不需要从远程仓库去下载。先从本地仓库找,如果找不到才会去远程仓库找|
|中央仓库|就是远程仓库, 仓库中jar由专业团队(maven团队)唯一维护。中央仓库的地址: https://mvnrepository.com/|
|远程仓库|在公司内部假设一台私服, 其他公司假设一台仓库, 对外公开|

![[310999a1dd.png]]

```
1.maven 自身运行所需要的插件
2.第三方框架(spring/mybatis/springmvc) 和 工具类的jar包
3.我们自己开发的maven下那个么安装后的jar包
```

#### 4.3.2 安装Maven

![[b973b546ab.png]]

- 1- 将其解压到一个没有中文和空格的目录下

![[18d02361d0.png]]

- 2- 配置系统环境变量

![[9eea5b1cef.png]]

![[871a6d27af.png]]

测试:

![[90cd570407.png]]

#### 4.3.3 配置本地仓库

![[e3e16cf157.png]]

- 1- 解压到一个没有中文和空格的目录下

![[8cb578e0e5.png]]

- 2- 在maven中配置仓库地址

![[a8eacaf2c4.png]]

![[eabf69b27b.png]]

- 3- 添加阿里云的私有仓库地址： 额外的特殊的包下载， 通过此仓库下载更快速

```
<mirrors>
    <mirror>
        <id>aliyunmaven</id>
        <mirrorOf>*</mirrorOf>
        <name>阿里云公共仓库</name>
        <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
</mirrors>
```

![[c14e7ec914.png]]

#### 4.3.4 IDEA中调整项目环境

##### 4.3.4.1 调整Maven环境

![[cbbe068e99.png]]

![[69c02dfca6.png]]

##### 4.3.4.2 修改编码

![[86b9d138e0.png]]

##### 4.3.4.3 调整JDK

![[2c72ae520a.png]]

![[70905ea032.png]]

##### 4.3.4.4 刷新maven环境

![[62fa1c7769.png]]

刷新后， 如果没有任何红色的波浪线报错， 说明就没问题了

#### 4.3.5 项目依赖环境

![[1bd9ebca74.png]]

在开发环境中, 我们可以看到,目前需要依赖了那些第三方的软件:

常规依赖内容: 持久化数据库、WEB服务器、缓存数据库服务（redis）、消息服务等

本项目所依赖内容：

- 1- 数据库服务：

![[b68e6e21e7.png]]

- 2- 缓存数据库服务：

![[d94341a893.png]]

- 3- OSS存储服务

![[cb275c29e7.png]]

- 4- 百度千帆大模型

![[c9f4421192.png]]

##### 4.3.5.1 部署MySQL8

###### 4.3.5.1.1 安装MySQL

- 1- 安装MySQL官方dnf(yum)仓库:

```
dnf install -y https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm

# 原因： 默认的dnf仓库存在更新不及时，版本可能会老旧的情况
```

![[b5445abe59.png]]

- 2- 查看是否启用MySQL8.0仓库

```
dnf repolist enabled | grep mysql
```

![[880067e737.png]]

- 3- 安装MySQL8

```
dnf install -y mysql-community-server --nogpgcheck

--nogpgcheck : 跳过 GPG 检查,当安装链接是可信的，建议直接跳过，避免由于网络等跟其他原因导致无法安装
        GPG（GNU Privacy Guard）是一种开源的加密工具，用于保障数据的安全性和真实性，主要用于加密、解密和数字签名验证。它的核心作用是通过公钥和私钥的机制提供数据完整性和防篡改验证。
```

![[ba0338c437.png]]

![[88d0a7f571.png]]

- 4- 启动MySQL相关服务

```
systemctl start mysqld
systemctl enable mysqld
systemctl status mysqld
```

![[d45f71fef3.png]]

- 5- 获取MySQL初始root密码

安装 MySQL 后，会生成一个随机的 root 密码, 可以通过MySQL的启动日志来查看

```
日志放置位置： /var/log/mysqld.log

grep password /var/log/mysqld.log
```

![[8e4501cd5f.png]]

- 6- 登陆MySQL，重新设置密码

```
mysql_secure_installation
```

![[06a8893aff.png]]

- 7- 测试登陆，并设置远程连接密码

```
mysql -uroot -p[密码]   可以省略密码 直接回车，然后输入密码  

注意：此密码就是最新设置的 Aa123456.
```

![[05a3bc79a9.png]]

```
-- 配置远程连接访问的root用户密码【直接执行即可，暂时不需要关心】：
CREATE USER 'root'@'%' IDENTIFIED BY 'Aa123456.';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;


执行完成后，可以直接quit退出或者使用ctrl +D 即可退出
```

![[ccaae20d1d.png]]

- 8- 开放防火墙服务/端口号

```
允许 MySQL 服务
firewall-cmd --zone=public --add-service=mysql --permanent

或者开放 3306 端口
firewall-cmd --zone=public --add-port=3306/tcp --permanent

# 让规则立即生效
firewall-cmd --reload

验证防火墙规则
firewall-cmd --list-all
```

![[1221f47fa7.png]]

- 9- 通过远程可视化工具访问：

![[df006ef4ed.png]]

- 添加数据库的驱动包： 用于连接数据库

![[dab5240745.png]]

![[706e59b49d.png]]

![[e4d040675a.png]]

![[7821c27268.png]]

![[b1ae6eac71.png]]

###### 4.3.5.1.2 导入基础数据

- 1- 显示所有的数据库信息

![[7dac103e5e.png]]

- 2- 运行SQL脚本, 导入初始化数据

![[da94888ff4.png]]

![[4f506081ef.png]]

![[f04caa51db.png]]

![[62bac601c3.png]]

###### 4.3.5.1.3 修改配置文件

![[525caa330e.png]]

##### 4.3.5.2 部署redis服务

Redis 是一个 **超级快** 的 **数据存储工具**，它可以把数据保存在**内存**里，类似于一个**高速缓存**。它被广泛用于需要 **快速读写数据** 的场景。

Redis 能干什么？

- **缓存数据**： Redis 常被用来缓存一些常用的数据，减少数据库的负担，提升应用的响应速度。比如，你访问一个网站时，网站的首页内容可能会被 Redis 缓存，当下次你访问时，Redis 直接返回缓存的数据，速度超快。
- **存储简单的数据结构**： Redis 不仅能存储简单的键值对，还支持很多高级的数据结构，比如：

- **列表**（List）：存储一组有顺序的数据。
- **集合**（Set）：存储一组没有重复的数据。
- **哈希**（Hash）：存储一组键值对，但不同于普通的键值对，哈希内部还可以存很多字段。
- **有序集合**（Sorted Set）：每个元素有一个分数，可以用来做排行榜。

- **实时数据分析**： Redis 支持快速的增减操作，非常适合用来做 **计数器**，比如统计网站的访问量、点赞数等。
- **消息队列**： Redis 可以用作消息队列，帮助不同的系统或服务之间传递消息。比如，你可以把任务放到 Redis 的队列里，其他程序取出任务并处理。
- **持久化数据**： Redis 默认将数据保存在内存中，但它也可以定期将数据存储到硬盘，以保证数据不丢失。

---

部署操作:

- 步骤一: 安装Redis服务

```
# 更新dnf相关软件包 【可选】  时间较长 预计20分钟
dnf update -y
# 安装redis操作
dnf install redis -y
```

![[082820e333.png]]

- 步骤二： 修改Redis相关配置

```
vim  /etc/redis/redis.conf
# 83行附件， 修改为  * -::*  任意的服务都可以连接redis服务
bind * -::*

#908行附近： 打开requirepass，设置其密码为123456 【可选】
requirepass 123456

如果找不到, 请在794行,添加即可
#794 行附近： 添加 requirepass，设置其密码为123456 【可选】  如果不涉及密码, 访问redis不需要输入密码,建议设置,因为项目中配置有对应密码
requirepass 123456
```

- 步骤三： 启动redis进程

```
systemctl start redis
systemctl enable redis

查看状态：
systemctl status redis
```

![[8eb8157fae.png]]

- 步骤四： 测试redis服务

```
redis-cli 【-a 密码】

或
redis-cli  命令 进入客户端， 然后输入 auth 123456

退出客户端： quit 或 ctrl +d
```

![[aa18d81245.png]]

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

![[645efed476.png]]

- 步骤六: 项目中设置redis的地址

![[423d86294a.png]]

##### 4.3.5.3 部署阿里云OSS

阿里云的 **OSS**（Object Storage Service）是一个 **云端对象存储服务**，简单来说，它就像是一个 **网上的硬盘**，用来存储和管理各种文件（比如图片、视频、文档等）。你可以把它理解为一个 **可以随时访问、随时上传文件的网盘**，不过它比普通网盘更强大，专门为大规模的数据存储和管理设计。

特点：

- **像硬盘，但在云上**：你把文件存到阿里云的OSS上，就像把文件放进云端的一个“网盘”中，而这个网盘可以存很多很多数据。
- **可以随时随地访问**：无论你身处哪里，只要有网络，就可以随时上传、下载、管理这些文件。
- **适合大规模数据存储**：不仅可以存普通文件，还能处理海量数据，比如网站的图片、视频，甚至是备份文件等。

---

- 步骤一：在阿里云中开通OSS服务

![[6609c25609.png]]

购买中： 仅需要选择开通服务即可

- 注意： 这里不用写立即购买， 选择立即开通即可， 一旦开通了， 就没有这个按钮了

![[6e7f45d884.png]]

**如果是第一次使用， 可以直接选择免费试用[直接跳转此处, 不需要先开通]**

![[473cee8888.png]]

- 步骤二： 进入到对象存储管理控制台

![[4083fb8b52.png]]

![[bca2243045.png]]

- 步骤三： 创建存储bucket桶（容器）

![[b579df9067.png]]

- 步骤四： 进入bucket， 设置为公用， 方便访问

![[2f4668c1a8.png]]

![[2d2d86fa65.png]]

- 生成访问accessKey，用于授权访问OSS服务

![[3ce0b62e4c.png]]

![[c0a98cfa23.png]]

![[ff52b2f9d1.png]]

![[c50463f97b.png]]

![[a2c7e1f86d.png]]

- 步骤五： 修改项目中关于OSS服务的配置信息

```
accessKeyId: 授权ID
accessKeySecret: 授权Secret
bucketName: 刚刚在oss创建的bucket
```

![[48f421c487.png]]

##### 4.3.5.4 申请百度千帆大模型授权【可选】

项目中, 主要是基于百度千帆大模型来分析用户的体检报告, 故需要注册百度千帆大模型APK, 从而对接百度千帆大模型. 生产环境中, 此位置一般选择为公司生产环境的百度千帆账号

- 注册地址：https://qianfan.cloud.baidu.com/

![[4be3364616.png]]

**实名认证**:

有了账号之后，我们需要**个人实名认证，**不然大模型调用不了，其中实名认证大家需要在手机端进行操作

1. 在手机上下载一个百度智能云app

![[34dfc6a19c.png]]

1. 使用刚刚注册的账号进行登录，找到**我的**，**个人中心**，可以进行实名认证操作

![[1f0c9c6ab8.png]]

注册后, 赠送20元优惠卷, 有效期1个月

**创建应用**

实名认证成功之后，我们继续在PC端来访问千帆大模型，地址：https://qianfan.cloud.baidu.com/

进入到管理平台

![[5dc67a26fe.png]]

进入管理平台后，找到**应用接入**，我们需要创建新的应用，只有创建了应用，后面才能让大模型来绑定应用使用

![[88fcdf4c7b.png]]

应用创建之后，可以查看自己的应用信息，其中就包含了一些秘钥信息，不要随意泄漏，如下图

![[32bd5afde8.png]]

---

设置应用到项目中:

```
accessKey: API KEY
  secretKey: 对应的secret key
  qianfanModel: ERNIE-4.0-8K-Preview(模型选择)
```

![[a97349806b.png]]

#### 4.3.6 启动运行

![[a186bf965a.png]]

等待一会:

![[4f2960385f.png]]

### 4.4 前端开发环境搭建

#### 4.4.1 安装node.js

Node.js 是一种基于 JavaScript 的运行环境，简单来说，它允许你在服务器端（而不是仅仅在浏览器中）运行 JavaScript 代码。你可以把它想象成一个让你用 JavaScript 做后端开发的工具。

**作用：**

- **构建服务器**：通过 Node.js，开发者可以使用 JavaScript 来创建网站的后端（服务器部分）。它能帮助处理网站的请求、发送数据、连接数据库等任务。
- **快速高效**：Node.js 使用非阻塞、事件驱动的架构，意味着它能同时处理大量的请求，效率很高，特别适合需要高并发的应用。
- **跨平台**：它可以在 Windows、Mac 和 Linux 系统上运行。

---

![[3bd7329251.png]]

- 1- 双击打开安装操作

- 注意: 如果无法双击打开安装, 在此目录下 打开CMD

![[a59fdc5036.png]]

```
在窗口中执行:
msiexec /i node-v18.20.3-x64.msi
```

![[4a8b4605d6.png]]

即可打开

![[4956e1ca92.png]]

![[65324f9998.png]]

![[b3db4bd2fe.png]]

![[92dee6d5f7.png]]

![[481d8f4e6a.png]]

![[1d29ddb473.png]]

![[f310dd208f.png]]

#### 4.4.2 安装VSCODE软件

Visual Studio Code（简称 VSCode）是一个非常流行的 **代码编辑器**，它可以帮助程序员编写代码。你可以把它想象成一个非常智能的文本编辑器，比起普通的文本编辑器（比如记事本），它具备很多为编程设计的功能，比如高亮显示代码、自动完成代码、调试功能等等。

安装操作:

![[9f6fe7fbdf.png]]

- 1- 双击即可

![[92c6711ac3.png]]

![[8208e331e5.png]]

![[d8ac8c46de.png]]

![[a89023c18a.png]]

![[fa644527f7.png]]

![[8345dbef1a.png]]

![[e505f1d69d.png]]

![[8a3a5329c4.png]]

添加中文插件：

![[6029e65a37.png]]

![[45ac19d260.png]]

![[b1644b0af0.png]]

#### 4.4.3 挂载前端项目

![[e65b4378f5.png]]

- 第一步： 将其解压到一个没有中文和空格的目录下

- 建议： 在vs code的安装目录下， 创建一个workspace目录，然后项目解压到此目录下

![[0b186be60a.png]]

- 第二步：使用vscode打开该项目

![[0d90c7ff43.png]]

![[1c6994425c.png]]

#### 4.4.4 运行项目

- 安装依赖和项目运行

- 进入到代码的根目录，然后执行以下命令：

```
npm install --registry=https://registry.npmmirror.com
```

![[2036a415d0.png]]

![[d407a47d46.png]]

- 修改配置

打开前端根目录下的**vite.config.js**文件，把mock地址改为若依后端的服务地址，如下图：

![[0787e1da84.png]]

- 启动项目

```
npm run dev
```

![[3b521ef1ff.png]]

- 访问地址：

```
http://localhost:8801/
```

![[50e054bf0f.png]]

### 4.5 小程序环境搭建

- 前提：在资料文件夹中找到”微信开发者工具安装包”安装到本地，也可以直接到[官网下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/stable.html)
- 在当天资料文件夹中找到”养老-小程序”的压缩包，解压到一个没有中文和空格的目录
- 打开微信开发者工具，需要使用微信扫描登录

![[566123ba95.png]]

登录成功后，点击“+”号，找到刚才解压的小程序代码的目录，然后打开

![[02b21f14bf.png]]

![[7449a82363.png]]

打开之后，需要信任该项目，加载完毕之后的效果如下：

![[dc1ec64acc.png]]

现在大家需要每人注册一个微信小程序的测试号：小程序AppId申请

- **前提：确保自己的微信与手机号已经绑定**
- 申请小程序测试号：https://mp.weixin.qq.com/wxamp/sandbox?doc=1
- 打开手机微信，扫描二维码，申请小程序测试号

![[100455bd24.png]]

- 注册成功以后，打开以下页面进行扫码登录

https://mp.weixin.qq.com/

![[889d762786.png]]

**特别注意**：扫码之后，在手机中选择**小程序**测试号

![[4f35cadff3.png]]

登录成功之后，就可以看到小程序的开发者ID，包含两部分，如下图

![[a0c3c5cbb4.png]]

- AppID(**小程序ID**)
- AppSecret(**小程序秘钥**)

---

1. 修改请求的路径

```
路径端口为9000
```

![[b5d19dd5f7.png]]

1. 需要忽略https请求

![[1c67e51771.png]]

修改小程序环境的APPID

然后打开 -->详情-->修改**APPID**,改为自己申请的测试号APPID

![[023c54b2e3.png]]