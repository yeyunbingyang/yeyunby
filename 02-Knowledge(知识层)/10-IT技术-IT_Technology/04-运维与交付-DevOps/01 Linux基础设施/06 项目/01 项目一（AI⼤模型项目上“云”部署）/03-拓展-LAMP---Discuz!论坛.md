![[66b479b4ae.png]]![[ac79372677.png]]

Apache：Apache是世界使用排名第一的Web服务器软件。

PHP：一种专门用于Web开发的编程语言。

MySQL：MySQL是一个关系型数据库管理系统，主要用于永久存储项目数据。

![[27fe0d6b92.png]]

# LAMP环境准备（阿里云）

要想部署一个互联网上可以访问到的环境，必须先具备以下内容 ：

服务器（IP、帐号密码、终端）、相应的软件、域名（备案、解析）、代码等。

## 1、注册阿里云账号

阿里云官网：[https://www.aliyun.com/](https://www.aliyun.com/)

![[cc5a735175.jpg]]![[b1c817eac8.jpg]]![[80efeabef3.jpg]]![[821026d85e.jpg]]![[2bdd3be39c.jpg]]

## 2、实名认证

步骤1：鼠标移动到屏幕右上角的头像，在弹出菜单中选择实名认证

![[6f12d0a3a3.jpg]]

步骤2：在认证页面，需选择个人实名认证

![[e353a5af38.jpg]]

步骤3：选择支付宝授权认证

![[242d323540.jpg]]

步骤4：勾选同意，点击提交

![[b521ad36fd.jpg]]

步骤5：支付宝扫描二维码，手机上选择确认登录

![[d9bd9bb1d3.jpg]]

步骤6：填写相关信息，点击确认

![[5dff627c68.jpg]]![[ec9b70d9ad.jpg]]

## 3、进入管理控制台

![[59fdd50a3e.jpg]]![[2902854258.jpg]]![[53a1972bb2.jpg]]

## 4、购买阿里云服务器

![[cfbb8c09e8.jpg]]![[38cbb6991c.jpg]]![[aaac161a97.jpg]]![[ab5d7f46f1.jpg]]![[ab5d7f46f1.jpg]]![[26eab85782.jpg]]![[edd2fe8ce7.jpg]]![[18d8fb2933.jpg]]![[6977f707b1.jpg]]

## 5、MobaXterm连接服务器

![[d460924e8d.jpg]]

# 部署LAMP环境

## 1、部署前的环境准备

### 1）关闭防火墙和selinux

```
#systemctl stop firewalld

#setenforce 0
临时关闭

#getenforce
查看当前是否关闭了selinux

#vim /etc/selinux/config
编辑selinux配置文件，永久关闭
```

![[97c8e50206.jpg]]![[ad580f0a53.jpg]]

### 2）查询当前服务器是否安装Apache

使用rpm命令

![[f73501df31.jpg]]![[c21d55b809.jpg]]

### 3）查询当前服务器是否安装MySQL

使用rpm命令

![[80901ec279.jpg]]

### 4）查询当前服务器是否安装PHP

使用rpm命令

![[4f2f7eeb24.jpg]]

```
建议使用一台新装的Linux，因为卸载如果有残留，也容易给后续搭建带来未知的问题。
```

## 2、LAMP环境之Apache安装

① 使用yum命令安装httpd软件包

![[e498c482b7.jpg]]![[eddd9bafa3.jpg]]![[f64fc44778.jpg]]![[f6fcd9f3e6.jpg]]

② 配置/etc/httpd/conf/httpd.conf文件

![[bb634da29d.jpg]]

搜索ServerName，在下面添加一行：

ServerName Localhost:80

```
#vim /etc/httpd/conf/httpd.conf

ServerName localhost:80
```

![[ecdd2f4d69.jpg]]![[9d3e4e90bf.jpg]]![[2905ad07db.jpg]]

问题：保存退出用什么命令？

答：

③ 使用systemctl命令重启httpd服务,使用netstat -ntlp命令，查看是否有80端口监听

![[dc6b14e3e3.jpg]]![[2c1b440f4c.jpg]]

④ 设置httpd服务开机启动

![[0b8ca1acee.jpg]]![[34768668f3.jpg]]

⑤ 查看本机的IP地址,阿里云服务器从控制台可以看到

![[3abbd6d035.jpg]]

⑥在浏览器中，输入本机IP地址，如下图所示：

![[5e3fe6918b.jpg]]![[8563f4d547.jpg]]

```
注意：自己的服务器在设置时，一定要管理防火墙与SELinux，避免产生异常
① 关闭防火墙    命令：# service iptables stop
② 关系SELinux  命令：# setenforce 0
```

## 3、LAMP环境之MySQL安装

### 1）下载mysql的yum源

由于yum源上默认没有mysql-server。所以必须去官网下载后在安装

```
# wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
含义：下载mysql的yum源
```

![[161cadd9aa.jpg]]![[941ddff6d0.jpg]]

### 2)添加mysql的yum源存储库

```

# rpm -ivh mysql-community-release-el7-5.noarch.rpm
含义：安装mysql的yum源存储库包
```

![[6ee4cbf035.jpg]]![[3cf49291b8.jpg]]

### 3）安装MYSQL

```
# yum -y install mysql-community-server
```

![[8764ee396b.jpg]]![[7508c5c421.jpg]]![[ba09052ef3.jpg]]![[185a623838.jpg]]![[f27bd5868e.jpg]]

### 4）启动mysql

```
#systemctl restart mysqld.service

#netstat -ntlp
```

![[06d7c169b4.jpg]]![[e40bdad14d.jpg]]

### 5）初始化数据库

#### ①初始化数据

默认情况下，数据库没有密码，也没有任何数据，必须要初始化

```
# mysql_secure_installation
含义：mysql自己带的初始化程序
```

![[068f89cd00.jpg]]![[247454a29f.jpg]]

设置超级管理员root密码，注：默认为空，直接回车即可

![[72ff29ffaa.jpg]]![[1e5fdf997e.jpg]]

移除匿名账户：

![[55c1e69a3a.jpg]]

不禁用root远程连接：

![[d7b47e6bd4.jpg]]

不移除默认数据库（测试用例）：

![[0e0cf11c2e.jpg]]

重新加载权限：Y

提示已完成，感谢使用MySQL

![[29d6e42624.jpg]]![[8b7b345d74.jpg]]

#### ②把mysqld添加到开机启动

默认已经开机启动，这里可以跳过

#### ③连接,MySQL数据库

```
#mysql -uroot -p
含义：-u是参数，后面跟用户名，没有空格
-p表示密码
看到mysql>表示已经连接到mysql
```

![[80a4196d1e.jpg]]![[e79b30f384.jpg]]

#### ④查看数据库

```
myslq> show databases;
含义：显示所有数据库
注意：命令结尾要有“;”
```

![[74b1d4ecd9.jpg]]![[924feea636.jpg]]

mysql>下输入exit，退出mysql，回到#提示符

## 4、LAMP环境之PHP安装

① 使用yum命令安装php

```
#yum -y install php

#systemctl restart httpd
```

![[11fc0812f2.jpg]]![[36c3a050ae.jpg]]

② 重启httpd服务

更改php配置一定要重启httpd服务

![[559bf9fed2.jpg]]

③ 测试LAMP环境是否可以使用

第一步：使用cd命令进入/var/www/html目录

第二步：使用vim命令创建index.php文件

第三步：编写php代码

```
代码示例：
#cd /var/www/html/
#vim index.php

<?php
    echo 'hello world';
?>
```

![[11fc0812f2.jpg]]![[6aa8b8d77c.jpg]]![[a177dc75a5.jpg]]

第四步：在浏览器，输入公网IP，如下图所示：

![[3e0e5a24f5.jpg]]![[093a0c91e7.jpg]]

# 部署Discuz!论坛

## 1、Discuz!论坛概述

Discuz!是一套开源的社区论坛软件系统。

![[b691aa2047.png]]

## 2、下载源代码

下载地址：[https://gitee.com/ComsenzDiscuz/DiscuzX](https://gitee.com/ComsenzDiscuz/DiscuzX)

![[276a7942af.jpg]]

## 3、使用MobaXterm上传代码

1）把ComsenzDiscuz-DiscuzX-master.zip文件通过MobaXterm上传到ECS服务器的/usr/local目录

2）安装unzip命令并且解压缩论坛代码

```
#yum -y install unzip
#unzip ComsenzDiscuz-DiscuzX-master.zip
含义：解压缩ComsenzDiscuz-DiscuzX-master.zip文件
#ll
```

![[4940e96949.jpg]]![[d4700f8b4b.jpg]]![[322a1ea6ec.jpg]]

解压缩后，得到DiscuzX目录，其中upload文件夹下是真正的网站代码文件

![[f070622f80.jpg]]

3）将网站代码拷贝到/var/www/html下

```
示例代码：
#cp -r /usr/local/DiscuzX/upload/* /var/www/html/

#cd /var/www/html/
#ll
```

![[9282c71c52.jpg]]![[c3aeea7cdb.jpg]]

# 安装Discuz!论坛

## 1、安装Discuz!前期准备

首先查看Discuz!源代码文件是否已经上传完成，必须完成后，才可以进行Discuz!论坛安装。

## 2、使用服务器IP地址访问论坛

看到下面的页面表示访问成功，点击我同意

![[fc22630806.jpg]]

## 3、设置目录权限

![[9b2bdf4182.jpg]]

如上图所示，系统提示很多文件没有可写权限，设置如下：

```
#chmod -R a+w /var/www/html/
```

![[6587916760.jpg]]

重新刷新，如下图所示：

![[3d9f169ef4.png]]

## 4、安装PHP扩展

![[629147c18f.png]]

如上图所示：以上结果代表系统缺少php-mysqli扩展，安装后即可解决。

① 使用yum命令安装php-mysqli扩展

```
#yum -y install php-mysqli
```

![[70ae13a062.jpg]]

② 重启httpd服务

![[5357050343.jpg]]

重新刷新网页，如下图所示：

![[34cbd9150f.png]]

## 5、设置运行环境

开始安装页面已经没有任何报错，点击下一步，进入设置运行环境页面

![[43373ce9d0.png]]

## 6、设置数据库信息与管理员信息

![[d6cfdd0f74.png]]

## 7、访问安装后的论坛

![[eaa66b72e6.jpg]]

进入论坛首页，如下图所示：

![[da9350e8f7.jpg]]

到此，关于LAMP环境配置与开源Discuz!项目实战就全部搞定了！

# 通过域名访问网站（扩展）

## 1、为什么需要域名

我们现在访问论坛是通过IP地址实现的，但是IP地址比较复杂，更重要的是不方便用户记忆。

## 2、购买域名

1)登录阿里云控制台

[https://account.aliyun.com/](https://account.aliyun.com/)

![[a0dfae85e1.jpg]]

2）登录后选择阿里云首页右上角的控制台，鼠标移动到左上角会出现如下菜单，选择域名

![[0848f0def2.jpg]]

3）点击域名注册：

![[7bc92007e7.jpg]]

输入一个想注册的域名名称，例如ityunweiketangyanshi

如下图所示：

![[2a4c19854a.jpg]]

加入清单，立即结算：

![[038f36d0f1.jpg]]

配置域名持有者，学习环境直接选择个人即可：

现在国家要求实名制，所以还要创建信息模板，点击创建信息模板

![[e627d8d1b2.jpg]]

点击页面右上角，创建新信息模板

![[8b8da16060.jpg]]

添加完个人信息后，回到订单页面刷新，重新选择个人，会看到自己添加的信息模板，还要认证邮箱，就是往你注册的邮箱里发一封邮件，需要登录邮箱，点击验证链接，最终完成信息登记

看到如下页面：

![[1382ee0401.jpg]]

勾选：我已阅读，理解并接受，然后单击立即购买，支付，如下图所示：

![[c8f256d564.png]]

## 3、域名解析

① 点击控制台，右侧菜单选择域名，进入域名管理页面

点击解析按钮

![[c77497bb8a.jpg]]

② 添加A记录

将[www.ketangyanshi.com](http://www.ketangyanshi.com) 指向公网IP

![[97f3ade2ef.jpg]]

点击确定，完成设置。几分钟后就可以通过域名访问刚刚搭建的网站了。

注意：由于国家要求，域名解析需要首先实名制认证，所以目前我这个域名无法实际使用，我还没有完成实名制认证