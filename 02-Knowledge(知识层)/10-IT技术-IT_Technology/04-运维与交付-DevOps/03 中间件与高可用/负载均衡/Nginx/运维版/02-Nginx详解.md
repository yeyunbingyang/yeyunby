# 学习目标

1、Nginx重装与升级（平滑升级）

2、Nginx企业级服务配置（基于域名的虚拟机配置）

3、了解Nginx常用一些官方模块

4、Nginx日志管理（error.log 与 access.log）

5、location区块（负责url规则匹配）

6、URL rewrite重写机制

## 运行原理

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251161-ab6383f3-dca6-4ec0-a749-1299171993d6.png "null")

运行时、开启主进程读取配置文件、无错误后会开启子进程。

请求时、会由子进程进行读取配置文件解析请求、读取文件响应资源。

# 一、重装与升级

作用：Nginx重装与Nginx平滑升级（不停服升级）

在实际业务场景中，需要使用软件新版本的功能、特性，就需要对原有软件进行升级或者重装操作。

旧statble稳定版1.24

stable稳定版1.26

mainline主线版本最新的1.27

如下图所示：

![[b2c217d646.png]]

## 1、信号参数

kill命合 传输信号给进程

kil不仅仅可以杀死进程，其底层核心是给进程传递一个信号！因为kill-9与kill-15使用较多，给大家带来错觉！

![[66a92fa219.png]]

### Nginx 进程管理信号说明

以下信号需发送给 Nginx 的主进程（Master Process）。

|   |   |
|---|---|
|**信号**|**功能描述**|
|**TERM, INT**|**快速关闭**：立即终止所有进程，正在处理的请求会被中断。|
|**QUIT**|**优雅关闭**：等待所有工作进程完成当前请求后，再退出。|
|**HUP**|**重载配置**：使用新配置文件启动新工作进程，并优雅关闭旧的工作进程。|
|**USR1**|**重新打开日志文件**：用于日志切割（如配合 `logrotate`<br><br>）。|
|**USR2**|**平滑升级二进制文件**：拉起一个主进程 旧主进程不停止。|
|**WINCH**|**优雅关闭工作进程**：尤雅的关闭worker进程|

---

### 重点：平滑升级操作流程

1. **启动新的主进程**（继承监听端口）：

```
kill -USR2 <旧主进程PID>
```

2. **优雅关闭旧的工作进程**（旧主进程仍存在，可回退）：

关闭master下面的所有work（子进程）

```
kill -WINCH <旧主进程PID>
```

3. **优雅退出旧的主进程**（完成升级）：优雅的退出master

```
kill -QUIT <旧主进程PID>
```

### 基本语法

```
kill 选项参数 pid
#快速关闭
kill -INT pid
#优雅关闭
kill -QUIT pid
```

## 2. 重新安装（了解）

1. 停止 Nginx 服务。
2. 删除原有的安装目录与文件：`rm -rf /usr/local/nginx`。
3. 下载新版本源码包，解压后重新编译并安装。

**注意**：操作前请务必备份配置文件 (`nginx.conf`) 及网站资源目录。

适合：开发或者测试环境，停机升级

## 3. 平滑升级（重点）

虽然通过上面的方式可以实现Nginx的升级，但是如果直接把旧版本的服务停止掉，会影响线上业务的使用。那我们该如何进行升级呢？

答：可以采用平滑升级，大致可以分为以下三个步骤

```
①旧的先不停掉
②新的又可以起来
③旧的和新的同时提供服务，|旧的请求完成之后，就停掉旧进程

-USR2 平滑启动新一个进程（平滑升级）
-WINCH 优雅的关闭子进程
-QUIT 优雅关闭主进程
```

**流程总结**：`USR2` → `WINCH` → `QUIT`

图解：

![[8bfa6f6226.png]]

**第一步：编译安装新软件**

注意：systemctl管理的nginx软件，没办法使用平滑升级，只有原生启动的Nginx才可以使用平滑升级。

原生启动命合：cd/usr/local/nginx；sbin/nginx

- **停止旧服务并检查**

```
[root@webo1]# systemctl stop nginx
[root@webo1]# cd /usr/local/nginx/
[root@webo1]# sbin/nginx
[root@webo1]# ps -ef | grep nginx
root       371609       1  0 11:16 ?        00:00:00 nginx: master process sbin/nginx
root       371610  371609  0 11:16 ?        00:00:00 nginx: worker process
root       371672  315645  0 11:16 pts/0    00:00:00 grep --color=auto nginx
```

- **编译安装新版本**

```
[root@web01]# tar xvf nginx-1.26.2.tar.gz
[root@web01]# cd nginx-1.26.2
yum install openssl-devel -y
[root@webo1]# ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module
[root@webo1]# make && make install
```

```
yum install openssl-devel -y
```

为什么一定要通过 systemctl stop nginx?

答：systemd 内部的管理机制没有完全支持Nginx平滑升级！！！

**第二步：升级新版本，需要把软件的安装路径，指定到旧版本上**

注：以上操作完成之后，会把原来的旧版本备份为nginx.old

![[9b53b6769b.png]]

**查看版本信息**

```
[root@webo1]# sbin/nginx -V
```

```
[root@webo1]# sbin/nginx.old -V
```

**第三步：平滑升级（新旧版本同时运行）**‍

```
[root@webo1]# kill -USR2 <旧的主进程号>
```

![[acc9372d57.png]]

**第四步：关闭旧进程**

1. **查看旧的主进程号**，然后执行以下命令：

```
# 优雅关闭旧的worker进程
[root@webo1]# kill -WINCH <旧的主进程号>

# 优雅退出旧的主进程
[root@webo1]# kill -QUIT <旧的主进程号>
```

2. **信号说明**：

- `-WINCH`：让旧的主进程优雅地关闭其下的所有worker子进程。
- `-QUIT`：让旧的主进程自身优雅退出。

![[78a2d6f467.png]]

注意：如果-QUIT以后两个master进程同时腿出，只有一种可能，Systemctl 与sbin/nginx混乱了！

小结：

工作中经常需要对旧版本程序进行升级操作，如MySQL、Nginx等等，但是Nginx本身有两种升级方式。

重装升级：需要停服，然后删原目录，重新编译安装！

平滑升级：不需要停服，直接在原有基础上进行升级！kill-USR2平滑升级

kill-WINCH移除当前进程的所有子进程（worker进程）kill-QUIT代表优雅的关闭master主进程

# 二、企业级服务配置

## 1、nginx.conf配置文件

nginx.conf存储位置有两种情况：

- **包管理器安装**（如 `dnf`/`yum`/`apt`）：  
    配置文件通常位于 `**/etc/nginx/nginx.conf**`。  
    此外，站点配置通常放在 `/etc/nginx/conf.d/` 或 `/etc/nginx/sites-enabled/` 目录下。
- **源码编译安装**（默认路径）：  
    配置文件位于 `**/usr/local/nginx/conf/nginx.conf**`。

![[43d09ebbdf.png]]

编译的nginx默认的配置文件位置：

```
/usr/local/nginx/conf/nginx.conf
```

nginx的配置文件(conf/nginx.conf)整体上分为三部分: 全局块、events块、http块。这三块的分别配置什么样的信息呢，看下表：

|   |   |
|---|---|
|区域|职责|
|全局块|配置和nginx运行相关的全局配置|
|events块|配置和网络连接相关的配置|
|http块|配置代理、缓存、日志记录、虚拟主机、静态资源配置等配置|

具体结构图如下:

![[02-Knowledge(知识层)/10-IT技术-IT_Technology/04-运维与交付-DevOps/03 中间件与高可用/负载均衡/Nginx/运维版/附件/5480ce8794.png]]

在全局块、events块以及http块中，我们经常配置的是http块。

在http块中可以包含多个server块,每个server块可以配置多个location块。0

使用grep删除注释与空行：

```
grep -Ev '#|^$' conf/nginx.conf > nginx.conf
```

![[3bd958fbeb.png]]

![[be8ab453c2.png]]

第一行：配置与机器核心数一致

servername localhost;【域名地址】

每个server对应一个项目

**http=>server=>location**

配置里有且只有一个http区块，可以有多个server区块（类似apache中的vhost虚拟主机），一个server里，可以有多个location区块。

http区块代表接收所有http请求，在nginx.conf中有且仅有1个！！！

1个http区块中可以有多个server区块，每个server区块就相当于一个项目配置！！！

1个server区块中可以有多个location，每个location区块就相当于一个url链接匹配规则！！！

|   |   |   |   |
|---|---|---|---|
|**区块**|**数量**|**类比**|**核心作用**|
|`**http**`|全局唯一|网络总管道|定义影响所有 HTTP 服务的全局配置（如 MIME 类型、日志格式、连接超时等）。|
|`**server**`|一个 `http`<br><br>下可有多个|**虚拟主机 (vhost)**|**核心配置单元**。通过监听不同的 `端口`<br><br>或 `服务器名称（域名）`<br><br>，来承载和管理一个独立的网站或应用。|
|`**location**`|一个 `server`<br><br>下可有多个|**URI 路由规则**|根据请求的 URI（路径），指定具体的处理逻辑（如返回静态文件、代理到后端应用等）。|

重点：学会配置server区块（虚拟主机板块）

```
server {
    # 1. 监听指令：监听本机所有IPv4地址的80端口（HTTP默认端口）
    listen 80;
    
    # 2. 服务器名称：指定此虚拟主机响应的域名，localhost代表本机访问
    server_name localhost;
    
    # 3. 根目录：设置网站文件的根目录。‘html’是相对于Nginx安装目录的相对路径
    root html;
    
    # 4. 默认请求处理规则：匹配所有未被其他更具体location匹配的请求
    location / {
        # 4.1 默认首页文件，按顺序查找
        index index.html index.htm;
    }
    
    # 5. 错误页面配置：当出现500、502、503、504状态码时，内部重定向到/50x.html
    error_page 500 502 503 504 /50x.html;
    
    # 6. 精准匹配：只处理 exactly 为 ‘/50x.html’ 的请求
    location = /50x.html {
        # 此处的根目录继承自 server 块的 root 指令
    }
    
    # 7. 正则匹配：处理所有以 ‘.php’ 结尾的请求（PHP动态脚本）
    location ~ \.php$ {
        # 7.1 将请求转发到后端的PHP-FPM处理器，地址为127.0.0.1:9000
        fastcgi_pass 127.0.0.1:9000;
        
        # 7.2 设置FastCGI默认索引文件
        fastcgi_index index.php;
        
        # 7.3 关键参数：告诉PHP-FPM要执行的脚本文件路径
        # $document_root 即上面 ‘root html’ 定义的路径
        # $fastcgi_script_name 是请求的PHP文件名
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        
        # 7.4 引入一组预定义的FastCGI参数
        include fastcgi_params;
    }
}

listen：监听端口，默认为80

server_name：很重要，可以绑定域名（更多一些）、可以绑定IP，localhost本机虚拟域名，底层IP地址就是127.0.0.1

root html：代表Nginx项目目录，从安装目录开始算起

location：url匹配规则，location =/50x.html精准匹配， location ~\.php$正则匹配，location /代表如果刚才那些匹配规则都没有生效，则默认匹配location/

error_page 500 502 503 504 /50x.html：如果服务器端响应500、502、503、504，则自动跳转到/50x.html这个错误页面

fastcgi_pass：请求转化给后面的地址
fastcgi_index：动态请求中的默认首页
fastcgi_param：参数设计，SCRIPT_FILENAME代表脚本名称。$document_root代表root指定的项目目录，$fastcgi_script_name请求的文件名称。

```

## 2、server区块配置 (虚拟主机）

### ☆基于域名虚拟机 (重要)

在实际生产业务环境中，一台web服务器，需要使用多个网站部署。搭建vhost虚拟机主机实现不同域名，解析绑定到不同的目录。

- www.shop.com => /usr/local/nginx/html/shop
- www.devops.com => /usr/local/nginx/html/devops

```
server {
    listen 80;
    server_name localhost;
    root html;
    
    location / {
        index index.html index.htm;
    }
    
    error_page 500 502 503 504 /50x.html;
    
    location = /50x.html {
        root html;
    }
    
    location ~ \.php$ {
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

**案例：添加一个www.devops.com**

**解析到/usr/local/nginx/html/devops项目命令**

第一步：编辑nginx.conf，添加虚拟主机

```
server {
    #监听端口
    listen 80;
    #配置域名
    server_name www.devops.com;
    #配置目录
    root html/devops;
    #配置uri匹配规则
    location / {
        #默认索引页
        index index.html index.htm;
    }
}
```

注意：每行配置完成之后，一定要注意结束标记符号。

```
sbin/nginx -t
```

第二步：在Windows电脑中，解析hosts域名，设置IP与域名映射，强制让DNS把www.devops.com指向虚拟机IP

①Windows+R，然后输入drivers回车如下图所示

![[77f556c454.png]]

②进入etc，找到hosts文件，然后拖拽到桌面

![[c53bb675fc.png]]

③在文件中添加以下内容（注意：IP要改成虚拟机对应的IP地址）

```
192.168.88.104 www.devops.com
```

第三步：在/usr/local/nginx/html目录下创建devops文件夹，然后在其目录下创建index.html文件

```
# cd /usr/local/nginx/html
# mkdir devops
# vim index.html
```

写入内容：

```
<html>
  <head>
    <title>devops</title>
  </head>
  <body>
    This is Web Page!
  </body>
</html>
```

第四步：重载Nginx

```
systemctl reload nginx
```

运行效果：

![[7d38c65b87.png]]

常见问题说明：

问题1：启动脚本比较混乱，Nginx有两种启动方式：systemctl或sbin/nginx，两者不能混用，每一种都有自己的语法

systemctl管理：

```
systemctl start nginx
systemctl reload nginx
systemctl stop nginx
```

sbin/nginx管理：

```
nginx -c /usr/local/nginx/conf/nginx.conf
nginx -s reload
nginx -s stop
```

### ☆基于IP虚拟机

多个IP访问同一台服务器主机，不同的IP解析到不同的vhost虚拟机中。核心：ens33绑定多个IP地址（选做一个临时绑定ip或者配置文件绑定ip）

第一步：使用ifconfig为ens33临时绑定一个虚拟网卡IP【模拟第二张网卡】

```
dnf install net-tools -y
ifconfig ens33:1 192.168.88.200
```

ifconfigens33:1down可以实现对其进行删除，然后systemctlrestartNetworkManager重后网络

实际服务器有两张网卡 ens33 ens37...

运行结果：

```
ifconfig
```

第二步：建立一个虚拟主机，绑定虚拟网卡IP

![[3a074f1ba5.png]]

第三步：重载Nginx

```
systemctl reload nginx
```

![[789bbab439.png]]

疑问：如果在nginx.conf配置文件中，只绑定了192.168.88.200这个IP，没有绑定192.168.88.104这个IP。则当在浏览器中访问

192.168.88.104，默认会转向哪里？

答：如果IP地址与配置文件中的serVer区块相匹配，匹配后就会直接显示匹配显示。如果IP地址与配合文件的server区块不匹配，则会默认指向

第一个server区块。

补充：CentOS Stream 9网卡添加IP与移除IP

- nmclient => nm (networkmanager) => cli(client)
- con => connection
- mod => modify
- up/down=>up开启/down关闭

```
#添加
nmcli con mod ens33 +ipv4.addresses 192.168.88.200/24
nmcli con up ens33

#查看
nmcli device show ens33

#移除
nmcli con mod ens33 ipv4.addresses "192.168.88.104/24"
nmcli con down ens33 && nmcli con up ens33
```

### ☆基于端口虚拟机

优势：默认不占用80端口，能够稍微隐秘一些

第一步：编辑nginx.conf配置文件

![[45b2c7ccfc.png]]

![[1511b34dc3.png]]

![[31e4994e66.png]]

小结：

在同一个Nginx中，我们可以配置多个主机（多个项目）

目前一共有三种方案：（基于域名虚拟主机）、（基于IP地址配置虚拟主机）、（基于端口号）

## 3、Nginx配置常见问题说明

问题1：需要交叉定义配置文件，如server区块中又嵌入了一个server区块。

答：会导致nginx.conf配置文件解析失败，语法错误=>Nginx无法启动。编写完配置文件，一定要使用/usr/local/nginx/sbin/nginx-t检查语法

问题2：sbin/nginx原生管理方式与systemctl管理方式混用

答：默认情况下，sbin/nginx原生管理不能使用systemctl方式进行管理；反之依然。两者必须明确选择一种

![[63e194415f.png]]

![[fa68b4d54d.png]]

问题3：不喜欢看错误，不喜欢记录错误

nginx无法启动，要看两个地方

```
journalctl -xeu nginx.service
#如果以上找不到具体的错误原因，还可以查看/var/log/messages
tail -100 /var/log/messages
```

journal 日志

英/ˈdʒɜːn(ə)l/

不喜欢记录错误

```
0.0.0.0:80 failed（98：Address already in use）=> 错误原因代表Nginx本身已经启动了，无法在二次启动，考虑已经有nginx进程了打开nginx网页会报错

正常打开=>200=>正常响应

打开显示找不到页面=>404=>网页未找到=>可能项目目录中没有找到与之对应的文件html/devops=>如果devops目录都没有

打开网页network gateway =>500=〉出现后端页面情况较多，请求动态页面，报错=>可能代码有异常，导致无法返回处理结果

打开网页403Forbidden=》403=》出现以上问题的原因多在于项目目录下找不到index对应的首页文件，如没有index.html/index.htm/index.phpl
```

### `server_name` 匹配规则：

- **完整匹配**：  
    `server_name` 可以指定多个域名，多个域名之间用空格分隔。例如：

```
server_name vod.mmban.com www1.mmban.com;
```

这表示该 `server` 配置块会匹配 `vod.mmban.com` 和 `www1.mmban.com` 两个域名。

- **通配符匹配**：  
    通配符可以用来匹配一类域名。例如：

```
server_name *.mmban.com;
```

这表示匹配所有以 `.mmban.com` 为后缀的子域名。

- **通配符结束匹配**：  
    如果通配符放在域名的结尾部分，则会匹配任意前缀。例如：

```
server_name vod.*;
```

这表示匹配所有以 `vod.` 开头的域名。

- **正则匹配**：  
    `server_name` 也支持正则表达式匹配。使用 `~` 表示正则匹配。例如：

```
server_name ~^[0-9]+\.mmban\.com$;
```

这表示匹配所有以数字开头并且以 `.mmban.com` 结尾的域名。

---

##### 总结：

通过虚拟主机和 `server_name` 的配置，Nginx 可以根据请求的域名或 IP 来匹配不同的 `server` 块，从而实现一个服务器上同时提供多个网站服务的功能。配置时，`server_name` 支持多种匹配方式，包括完整匹配、通配符匹配和正则匹配。

## 【拓展】虚拟主机与域名映射

http携带 域名

**Nginx（仓库管理员）**：当请求进来时，Nginx 会查看请求头里的 `**Host**` **字段**。如果 `Host: a.com`，它就按 A 的配置处理；如果是 `Host: b.com`，就按 B 的处理。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251692-3c8f9c59-e76b-4c11-acf9-569a3688aac8.png "null")

##### 域名、DNS、IP 地址的关系

1. **域名**：

- 域名是互联网上用于标识网站和网络资源的名称，旨在使人们更容易记住和访问网站。域名通常由几个部分组成，比如顶级域（TLD），如 `.com`、`.org`，以及子域名，如 `www`。
- 例如：`www.example.com` 是一个域名，其中 `example` 是二级域名，`com` 是顶级域。

2. **DNS（Domain Name System）**：

- DNS 是一种将域名转换为 IP 地址的系统。它通过分布式的域名解析服务将用户输入的域名解析为服务器的 IP 地址。
- 用户输入域名后，DNS 系统会查询与该域名关联的 IP 地址，从而找到目标服务器并建立连接。

3. **IP 地址**：

- IP 地址是互联网上每个设备的唯一标识符。它用于确定设备的位置，并在计算机之间进行通信。IP 地址有 IPv4 和 IPv6 两种形式，分别表示为四个数字（如：`192.168.1.1`）和八组十六进制数（如：`2001:0db8:85a3:0000:0000:8a2e:0370:7334`）。

**关系**：DNS 是一个中介，将易于记忆的域名转换为机器能够理解和使用的 IP 地址。浏览器通过域名找到对应的 IP 地址，从而访问服务器上的资源。

---

##### 浏览器、Nginx 与 HTTP 协议

1. **浏览器**：

- 浏览器是用户与互联网之间的交互工具，负责请求和显示网页内容。它使用 HTTP 协议来从 Web 服务器（如 Nginx）获取网页数据。
- 用户在浏览器中输入 URL，浏览器会通过 HTTP 协议向目标服务器发送请求，服务器返回响应并呈现网页。

2. **Nginx**：

- Nginx 是一个高效的 Web 服务器和反向代理服务器，它支持处理 HTTP 请求，提供负载均衡、缓存、静态文件服务等功能。
- Nginx 监听 HTTP 请求并将请求转发到后端应用服务器（如 Tomcat、Node.js）或直接返回静态资源。

3. **HTTP 协议**：

- HTTP（Hypertext Transfer Protocol）是浏览器与服务器之间通信的协议，主要用于请求和传输网页内容。
- HTTP 协议是无状态的，意味着每次请求都是独立的，服务器不会记住之前的请求。
- https上存在加密

---

##### 虚拟主机原理

虚拟主机允许一台物理服务器通过不同的配置支持多个网站或应用。它根据不同的域名、IP 地址或端口号，将请求导向不同的应用或网站。

配置不同域名解析不同资源目录

- **基于域名的虚拟主机**：根据客户端请求中的 `Host` 头部信息将请求分发到不同的站点。每个站点都有不同的 `server_name` 配置。
- **基于 IP 地址的虚拟主机**：根据不同的 IP 地址将请求分发到不同的站点。
- **基于端口的虚拟主机**：通过不同的端口号来区分多个站点。

Nginx 配置的虚拟主机通过 `server` 块定义，每个 `server` 块代表一个虚拟主机。

---

##### 域名解析与泛域名解析实战

1. 域名解析：

- 域名解析是 DNS 服务器将域名转换为 IP 地址的过程。当用户请求某个网站时，DNS 查询该域名的记录并返回相应的 IP 地址。
- 【本地】本机可以更改host文件解析ip地址![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251749-0abf28c0-b435-4878-af87-9e35bcfcddaf.png "null")
- 公网域名![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251812-a048193a-6012-4630-ba4c-b3f525c5e875.png "null")

2. 泛域名解析：

- 泛域名解析允许所有子域名指向同一 IP 地址。它可以通过 DNS 配置 `*.example.com` 来实现，将所有以 `example.com` 为后缀的子域名解析为相同的 IP 地址。

3. 实战：

- 在 Nginx 配置文件中，可以通过配置 `server_name *.example.com` 来实现泛域名解析，支持多个子域名指向同一资源。

---

##### 域名解析相关企业项目实战技术架构

1. **技术架构**：

- **DNS 服务**：部署内部 DNS 服务器与外部 DNS 服务，确保企业内部和外部网络能够快速地解析域名。
- **CDN 加速**：结合 CDN（内容分发网络）来加速域名解析和内容交付，尤其是对于全球分布的用户。
- **负载均衡**：使用 DNS 负载均衡或者反向代理（如 Nginx）来分配流量，确保网站高可用性和负载均衡。

2. **实战案例**：

- 企业常常为不同的服务设置子域名，如 `api.example.com`、`shop.example.com`，并通过 DNS 配置解析到不同的服务器或者服务实例。

---

###### 多用户二级域名

反向代理到业务服务器数据库中查询映射信息

多用户二级域名是将一级域名分配给多个用户，每个用户都有自己的二级域名。例如，`user1.example.com`、`user2.example.com` 等。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251915-8dc940ae-d80d-46d9-a456-d6db17bd2a6f.png "null")

- 在 Nginx 中，可以使用泛域名解析将所有二级域名指向相同的服务器，然后根据 `server_name` 进行分发处理。

---

###### 短网址

反向代理到业务服务器数据库中查询映射信息

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300251971-8e0b79ad-4217-4bd1-986f-1ce32c76e850.png "null")

短网址服务通过将长 URL 转换为短 URL 来节省空间和提高链接的可分享性。例如，将 `https://www.example.com/product/12345` 转换为 `https://short.ly/abc123`。

- 实现方式通常是使用数据库存储长网址与短网址的映射关系，在用户访问短网址时，进行重定向。

---

###### HTTPDNS

HTTPDNS 是通过 HTTP 协议来实现 DNS 查询，绕过传统的 DNS 解析过程，避免了运营商 DNS 的污染和劫持。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300252035-c9813e85-73f0-47b7-9c93-55f7587273ec.png "null")

- **原理**：HTTPDNS 服务提供一个 API，客户端通过 HTTP 请求获取域名解析结果，而不是直接通过系统的 DNS 进行查询。
- **优点**：提高解析的稳定性，避免 DNS 被劫持，确保获取到最新的解析信息。

---

# 三、Nginx默认官方模块

## 1、GZIP压缩

压缩文件大小变小了，传输更快了。目前市场上大部分浏览器是支持GZIP的。IE6以下支持不好，会出现乱码情况。[http://nginx.org/en/docs/http/ngx_http_gzip_module.html](http://nginx.org/en/docs/http/ngx_http_gzip_module.html)

```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.1;
gzip_comp_level 5;
gzip_types text/plain text/css text/javascript application/x-javascript image/jpeg image/gif image/png image/x-ms-bmp;
gzip_vary on;
gzip_disable "MSIE [1-6]\.";

第1行：开启Gzip
第2行：不压缩临界值，大于1K的才压缩，一般不用改
第3行：gzip_buffers number,size，压缩文件时使用的缓存空间的大小，默认128
第4行：用了反向代理的话，末端通信是HTTP/1.0，默认是HTTP/1.1
第5行：压缩级别，1-10，数字越大压缩的越好，时间也越长
第6行：进行压缩的文件类型，建议js|css|图片,注：javascript有两种写法，最好都写上
第7行：跟squid等缓存服务有关，on的话会在Header里增加"Vary:Accept-Encoding"
第8行：IE6对Gzip不怎么友好，不给它Gzip了

gzip_vary off; 是 Nginx 配置中的一条指令，它用于控制是否在响应头中设置 Vary：Accept-Encoding 头部。具体来说:
gzip_vary on;： 启用时，Nginx 会在响应头中加入 Vary： Accept-Encoding，表示不同的客户端可能会根据是否支持 gzip 压缩来收到不同的响应内容。这有助于缓存服务器（如CDN）缓存压缩和未压缩的内容。
gzip_vary off;：禁用时，Nginx 不会在响应头中加入 Vary：Accept-Encoding，这意味着缓存服务器不会区分压缩与未压缩的内容。这样做通常会减少缓存的复杂性，但可能会导致某些情况缓存不一致。
```

![[0aa2ec65f2.png]]

gzip压缩文本、css（层叠样式表）丶js（浏览器端执行的脚本）、图片文件。

```
server {
    listen       80;
    server_name  localhost;

    # --- GZIP 压缩配置 (写在 server 块内，全局生效) ---
    gzip on;
    gzip_min_length 1k;        # 小于 1k 的文件不压缩
    gzip_comp_level 6;         # 压缩级别 (1-9)，6 是性能与压缩比的最佳平衡点
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
    gzip_vary on;              # 往响应头添加 Vary: Accept-Encoding
    gzip_disable "MSIE [1-6]\."; # 禁用 IE6 的 gzip

    location / {
        root   /data/www/mysite;
        autoindex on;
        autoindex_localtime on;
        charset utf-8;
    }
}
```

案例:

在/usr/local/nginx/html/devops目录上传fox.bmp图片文件创建一个index.html首页

![[b0675854d6.png]]

配置压缩后

重载nginx

```
sbin/nginx -s reload或
systemctl reload ng
```

![[13776645c1.png]]

![[09aae7739b.png]]

## 2、客户端缓存（优化手段）

告知浏览器获取的信息是在某个区间时间段是有效的，基本格式：

```
expires 30s；//表示把数据缓存30秒
expires 30m；//表示把数据缓存30分
expires 10h；//表示把数据缓存10小时
expires 3d；//表示把数据缓存3天
```

案例：缓存图片/js/css文件，缓存时间为1天

```
location ~ \.(jpg|jpeg|gif|png|js|css)$ {
    expires 1d;
}
```

![[e3b5bfae58.png]]

再次访问后

![[aafcbccdc3.png]]

结果为304（响应状态码），代表网页中的图片资源已被缓存。

## 3、反向代理

正向代理：

![[7e936ec5ee.png]]

![[3518de7945.png]]

特点：知道自己使用了代理，需要填写代理服务器的IP等相关连接信息

场景：常见于代理客户端上网等操作（翻墙）

反向代理：

![[ff67114474.png]]

![[79f224f5b2.png]]

特点：用户是无感知的，不知道使用了代理服务器。反向代理服务器是和真实访问的服务器是在一起的，有关联的。

作用：

①可以根据实际业务需求，分发代理页面到不同的解释器

②可以隐藏真实服务器的路径

③反向代理常用于转发请求或者负载均衡操作

location配置

翻译：位置 / 地点 / 定位 / 存储单元

```
server {
    listen 82;
    server_name localhost;
    location / {
        proxy_pass http://192.168.200.131:8080; 	#反向代理配置，将请求转发到指定服务
    }
}
```

上述配置的含义为: 当我们访问nginx的82端口时，根据反向代理配置，会将请求转发到 [http://192.168.200.131:8080](http://192.168.200.131:8080) 对应的服务上。

`location /` 中的 `/` 是一个匹配路径的模式，它表示 **匹配所有请求路径**，即根路径及其下的所有路径都会被此 `location` 块处理。

小结：

代理一共有两种：（正向代理）十（反向代理）

正向代理用户可以感知到，比较典型应用（科学上网）

反向代理用户无感知，比较典型的应用（请求转发，更多应用在于负载均衡技术）

## 4、基于IP的访问控制（安全限制）

基于ngx_http_access_module模块，默认可使用

语法：

```
deny ip  禁止IP访问
allow ip 允许IP访问
```

[https://nginx.org/en/docs/http/ngx_http_access_module.html](https://nginx.org/en/docs/http/ngx_http_access_module.html)

![[d188ea0f14.png]]

默认是允许所有IP访问。

案例 :

疑问：192.168.1.1这个IP，也满足下方allow192.168.1.0/24；那到底最终是允许还是不允许访问呢？

答：不允许访问，默认从上往下执行，一旦匹配到某个规则，则自动触发。不会继续往下匹配！！！

提示：403，禁止访问。

## 5、基于用户的访问控制（安全限制）

基于 `ngx_http_auth_basic_module` 模块，默认可用。

**语法：**

加密文本：由 htpasswd 命令实现

`htpasswd` 是 httpd 里的一个工具。如果没有，可以通过 `yum instal1 httpd-tools -y` 安装。

```
1. 创建密码文件：htpasswd -c 生成到的路径 用户名
2. -c 创建新文件，如果再次添加用户去掉 -c 参数，否则会被删除覆盖原来的

auth_basic "string";
auth_basic_user_file /path/to/passwd.db;

auth_basic "welcome to itheima!";
auth_basic_user_file /usr/local/nginx/conf/passwd.db;
```

![[4ff0ab0343.png]]

  
**第一步：生成 passwd 密钥文件**  
切换到 conf 目录。

```
cd /usr/local/nginx/conf
```

生成秘钥文件。

![[0b3d298ac7.png]]

第二步：在nginx.conf中配置密钥文件

![[c94487334e.png]]

设置完成后，重启nginx

```
sbin/nginx -c reload
或
systemctl reload nginx
```

第三步：打开浏览器，访问www.devops.com域名，运行效果：

![[97fc935d60.png]]

如果本次账号与密码输入不正确，则会提示：401，未授权！

![[8e85ab9747.png]]

![[9eaa6b5581.png]]

## 6、目录结构显示（了解）

作用：仅用于开发、测试环境，主要用于调试代码

应用：如果项目配置完毕后，一个目录下没有首页，则会显示403Forbidden。这个时候我们可以使用autoindexon，显示所在目录下的所有文件列表。

基本语法：

```
autoindex on;
```

![[4f0dd22a8d.png]]

注意：

如果你配置的目录 下面存在一个名为 `index.html` 的文件，**Nginx 会优先显示网页内容，而不是文件列表**。

```
server {
    listen       80;
    server_name  localhost;

    location / {
        root   /data/www/mysite;
        # index  index.html;  <-- 注意：如果要显示文件列表，建议注释掉 index 行
        
        autoindex on;             # 开启目录索引
        autoindex_exact_size off; # 默认为on，显示精确字节数；off则显示单位(KB/MB/GB)
        autoindex_localtime on;   # 默认为off，显示GMT时间；on则显示服务器本地时间
        charset utf-8;            # 防止中文文件名乱码
    }
}
```

打开浏览器，访问如下图所示：

![[3d99553690.png]]

小结：

autoindex on功能比较简单，就是为了显示Nginx对应项目录下的所有文件信息。

注意：由于autoindex会显示项目目录下的所有文件信息，所以其比较适合内部使用，不建议在外部环境使用！

好的，已为您将内容整理为结构更清晰的笔记格式。

# 四、日志管理⭐

**作用**  
了解 Nginx 日志管理，尤其是错误日志以及访问日志。

- **错误日志**：方便 Nginx 排错。
- **访问日志**：主要用于进行访问信息分析，可以结合 Python、GoAccess、ELK 等工具进行日志分析。

**Nginx 的两种默认日志**  
Nginx 默认会产生两种日志：

1. **access.log (访问日志)**：用于记录和查看统计用户的访问信息与流量。
2. **error.log (错误日志)**：用于记录错误信息以及重写信息。

![[0b68329b8e.png]]

**默认日志路径**

- **自定义编译安装**的默认路径通常为：`/usr/local/nginx/logs`
- **通过 yum 安装**的默认日志目录通常为：`/var/log/nginx`

**参考文档**

- 官方 ngx_http_log_module 模块文档：[http://nginx.org/en/docs/http/ngx_http_log_module.html](http://nginx.org/en/docs/http/ngx_http_log_module.html)

## 1、access.log访问日志

```
# cat /usr/local/nginx/logs/access.log
```

![[0dfc9b9a60.png]]

## 2、日志参数详解

```
vim /usr/local/nginx/conf/nginx.conf

http {
    ...

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log logs/access.log main;

    ...
}
```

![[d3cf72fa9c.png]]

|   |   |
|---|---|
|参数|意义|
|$remote_addr|客户端的IP地址（代理服务器，显示代理服务IP）|
|$remote_user|用于记录远程客户端的用户名称（一般为“-”）|
|$time_local|用于记录访问时间和时区|
|$request|用于记录请求的URL以及请求方法|
|$status|响应状态码，例如：200成功、404页面找不到等|
|$body_bytes_sent|给客户端发送的文件主体内容字节数|
|$http_user_agent|用户所使用的代理（一般为浏览器）[使用的浏览器]|
|**$****http_x_forwarded_for**|可以记录真实客户端IP，通过代理服务器来记录客户端的IP【真实源IP】|
|$http_referer|可以记录用户是从哪个链接访问过来的|

![[bf7b95009e.png]]

![[2448b0ccfa.png]]

## 3、错误日志

配置error_log：

```
# vim /usr/local/nginx/conf/nginx.conf
```

![[e507d7cf72.png]]

在配置 nginx.conf 的时候，有一项是指定错误日志的，默认情况下你不指定也没有关系，因为 nginx 很少有错误日志记录的。但有时出现问题时，是有必要记录一下错误日志的，方便我们排查问题。

error_log 级别分为 debug、info、notice、warn、error、crit，默认为 notice，该级别在日志名后边定义格式如下：

|   |   |
|---|---|
|错误级别|备注|
|debug|调试模式，记录的日志最多|
|info|信息|
|notice|提示 默认 >notice|
|warn|警告|
|error|错误|
|crit|记录的日志最少,致命、记录内容最少|

crit 记录的日志最少，而 debug 记录的日志最多。如果你的 nginx 遇到一些问题，比如 502 比较频繁出现，但是看默认的 error_log 并没有看到有意义的信息，那么就可以调一下错误日志的级别，当你调成 error 级别时，错误日志记录的内容会更加丰富。

小结：  
错误日志的作用：用来查看错误信息，通过提示的错误信息，排除错误。

## 4、日志轮转

  
作用：利用 Shell 脚本对日志进行切割，把大的访问日志切割为一个一个小日志，方便后期存储以及查看分析

```
# vim logrotate.sh

---------------华丽的分割线---------------
#!/bin/bash
date_info=$(date +%F-%H-%M)

mv /usr/local/nginx/logs/access.log /usr/local/nginx/logs/access.log.$date_info
/usr/local/nginx/sbin/nginx -s reload
---------------华丽的分割线---------------
# crontab -e
* */6 * * * /bin/sh /scripts/logrotate.sh &>/dev/null


说明：为什么备份日志文件以后，要重载Nginx呢? /usr/local/nginx/sbin/nginx -s reload
答：因为每次重载，没有access文件、系统都会产生一个新的access.log日志文件
```

![[cb364df51e.png]]

![[eccb022f99.png]]

![[8c149b4d6e.png]]

小结：  
日志轮转的本质就是把一个大的日志切割为若干个小文件，防止文件过大。

## 5、扩展：GoAccess轻量级日志分析

作用：针对 Apache/Nginx 访问日志进行分析，优点：轻量级、开源、带图形化界面。

大型：ELK

**什么是 GoAccess？**  
GoAccess 是一款开源且具有交互视图界面的实时 Web 日志分析工具，通过 Web 浏览器或 Linux 终端即可访问。它能为系统管理员提供快速且有价值的 HTTP 统计，并以在线可视化服务器的方式呈现。

**安装 GoAccess**

```
dnf install epel-release -y
dnf install goaccess -y
```

**运行 GoAccess 分析 access.log 日志**

```
cd /usr/local/nginx/
# 使用 GoAccess 分析日志
goaccess logs/access.log -o report.html --log-format=COMBINED
```

注意：GoAccess 分析的结果往往是一个 HTML 网页，如果想直接预览，建议将生成的 report.html 放置于 Nginx 的访问目录中。

① 离线分析

分析过去一段时间访问信息

```
goaccess -f logs/access.log --log-format=COMBINED > /usr/local/nginx/html/report.html
```

参数说明：

- `-f`：指定要分析的日志文件
- `--log-format`：指定日志格式

日志格式说明：

- `COMBINED`：组合日志格式（Apache/Nginx XLF/ELF）
- `COMMON`：通用日志格式（CLF，Apache）

② 实时分析

分析过去所有以及当前访问信息

```
goaccess logs/access.log --log-format=COMBINED -o /usr/local/nginx/html/report.html --real-time-html
```

说明：

- `--real-time-html`：启用实时更新 HTML 报告
- 生成的 report.html 可通过浏览器实时查看访问日志分析结果

更多参考：[GoAccess 官方文档](https://www.goaccess.cc/?mod=man)

![[7c79342d41.png]]

# 五、location 区块

作用：location 区块用于 URL 规则匹配，既支持精准匹配，也支持正则匹配  
[http://nginx.org/en/docs/http/ngx_http_core_module.html#location](http://nginx.org/en/docs/http/ngx_http_core_module.html#location)

## 1、location 的作用

location 指令的作用是根据用户请求的 URI 来执行不同的操作，也就是根据用户请求的网站 URL 进行匹配，匹配指定的请求 URI（请求 URI 不包含查询字符串，如 [http://localhost:8080/test?id=10，请求](http://localhost:8080/test?id=10%EF%BC%8C%E8%AF%B7%E6%B1%82) URI 是 /test）

[http://localhost:8080/test?id=10](http://localhost:8080/test?id=10)

http:// =>http协议，https协议

（https相比于http多了一个s，安全证书，有了证书配置以后，传输就采用加密传输）

url：整体称之为url=>localhost:8080/test?id=10

uri：域名后面的路径，一般就称之为uri=>/test?id=10：代表参数

## 2、location 基本语法

```
location [ = | ~ | ~* | ^~ ] uri {
    ...
}
# 指令匹配标识  匹配的网站网址  匹配 URI 之后要执行的配置段
```

![[e95e101bd7.png]]

① = 精确匹配

代表uri必须完全等于匹配规则才会被触发

```
location = / {
    # 规则
}
```

注意：以上匹配操作只能匹配首页！  
即只会匹配到 [http://www.example.com/](http://www.example.com/) 这种请求。

② 大小写敏感

```
location ~ /Example/ {
    # 规则
}
```

请求示例：

- [http://www.example.com/Example/](http://www.example.com/Example/) → 成功
- [http://www.example.com/example/](http://www.example.com/example/) → 失败

③ 大小写忽略

```
location ~* /Example/ {
    # 规则
}
```

请求示例：

- [http://www.example.com/Example/](http://www.example.com/Example/) → 成功
- [http://www.example.com/example/](http://www.example.com/example/) → 成功

④ `^~` 只匹配以 URI 开头

```
location ^~ /img/ {
    # 规则
}

说明：^~，也是严格区分大小写
```

请求示例：

- [http://www.example.com/img/a.jpg](http://www.example.com/img/a.jpg) → 成功
- [http://www.example.com/img/b.mp4](http://www.example.com/img/b.mp4) → 成功
- [http://www.example.com/bimg/b.mp4](http://www.example.com/bimg/b.mp4) → 失败
- [http://www.example.com/Img/b.mp4](http://www.example.com/Img/b.mp4) → 失败

## 3、location 优先级

优先级：当 location 有多个规则时，会按照以下顺序匹配执行

```
# ① 优先级最高：精确匹配
location = / {
    # 规则
}

# ② 前缀匹配（^~）
location ^~ /images/ {
    # 规则
}

# ③ 正则匹配（区分大小写或忽略大小写）
location ~* \.(gif|jpg|jpeg|png)$ {
    # 规则
}

# ④ 根据资源目录前缀匹配
location /documents/ {
    # 规则
}

# ⑤ 默认匹配（所有不满足以上规则的请求）
location / {
    # 规则
}
```

- 域名/ip 匹配不上、会以第一个显示server区块

# 六、URL 重写

## 1、`return`

用于返回服务器的状态码，基本语法：

```
return <状态码>;
```

常用状态码说明：

|   |   |
|---|---|
|状态码|含义|
|200 OK|请求成功，正常响应|
|301 Moved Permanently|永久重定向，常用于重写规则【域名变更】|
|302 Found|临时重定向，常用于重写规则【临时出现问题 切换】|
|304 Not Modified|请求资源内容没有改变，常用于缓存|
|404 Not Found|请求资源不存在，文件或路径不存在|
|500 Internal Server Error|服务器遇到无法处理的情况，常见于代码异常|
|502 BadGateway|错误网关，常出现反向代理中如果反向代理的服务器出现异常或者服务中断|
|503 Service Unavailable|服务器未准备好处理请求，常见于维护或重载停机|

更多状态码参考：[MDN HTTP 状态码](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)

永久重定向：域名变更 301

旧: www.oldn.com

新：www.new.com

## 2、`rewrite`

基本语法：

```
rewrite <匹配内容> <替代内容> <flag标记>;
```

**flag 标记说明**

|   |   |
|---|---|
|标记|作用|
|last|本条规则匹配完成后，继续向下匹配新的 location URL 规则|
|break|本条规则匹配完成即终止，不再匹配后面的任何规则|
|redirect|返回 302 临时重定向，浏览器地址栏显示跳转后的 URL|
|permanent|返回 301 永久重定向，浏览器地址栏显示跳转后的 URL|

**注意事项**

- 多条 `rewrite` 从上到下匹配，匹配到后即停止，不再匹配其他 `rewrite` 规则。
- `last` 与 `break` 重定向时，客户端 URL 地址不会改变。
- `redirect` 与 `permanent` 重定向时，客户端 URL 地址会发生改变。

官方文档：[NGINX rewrite 模块](http://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite)

### ☆案例一：资源重定向

要求：使用商城项目，把访问的 index.html 重定向到 index.php，实现伪静态

```
# vim /usr/local/nginx/conf/nginx.conf
location / {
    index index.html index.htm;
    rewrite /index.html /index.php last;
}
```

### ☆案例二：域名重定向

要求：公司的域名升级了，需要把所有请求重定向到新域名

```
# vim /usr/local/nginx/conf/nginx.conf
server {
    listen 80;
    server_name www.devops.com;
    rewrite ^/(.*)$ http://www.baidu.com/$1 permanent;
}

server_name www.devops.com; 
rewrite /http://www.baidu.com permanent;
```

`rewrite ^/(.*)$ http://www.baidu.com/$1 permanent;`

- **rewrite** 指令用来重写 URL。
- 正则解析：

- `^/(.*)$` → 匹配所有请求 URI，从 `/` 开始，捕获后面的所有内容。
- `(.*)` 捕获的内容会放到 `$1`。

- 重写目标：

- `http://www.baidu.com/$1` → 将请求重定向到百度，同时保留原请求路径。

- `permanent`：

- 表示返回 **301 永久重定向**。
- 浏览器会记住这个重定向，下次直接跳转到新地址。

#### 示例：

|   |   |
|---|---|
|原请求|匹配结果|
|[http://www.devops.com/](http://www.devops.com/)|重定向到 [http://www.baidu.com/](http://www.baidu.com/)|
|http://www.devops.com/news|重定向到 http://www.baidu.com/news|
|http://www.devops.com/images/logo.png|重定向到 http://www.baidu.com/images/logo.png|

注：永久重定向，适合域名更换的场景。而且一旦某个域名301重定向到其他页面，则老域名就会被搜索引擎所屏蔽。

### ☆案例三：防盗链原理和实现

作用：就是防止我们站点中资源被别人所使用=>主要针对资源文件，如（图片、音乐、视频)

![[9485b672c4.png]]

防盗链原理：

验证域名/ip 是否可访问

![[d7cda8957d.png]]

- web1.devops.com 用户可以访问 web1 域名的资源文件
- web2.devops.com 不可以访问

需求说明：

- web2 服务器经常链接 web1 服务器上的资源文件，用户访问 web2 图片时，以为 web2 拥有资源，但实际耗费了 web1 大量流量。

解决方案：

1. 图片加水印
2. 通过判断 referer 来源，确定是否返回对应的资源文件

基本语法：

```
location / {
    valid_referers web1.devops.com;
    if ($invalid_referer) {
        return 404;
    }
}
```

☆案例：图片防盗链

准备两个站点及域名www.devops.com（我们公司）、192.168.88.104（竞争对手）

192.168.88.104 => /usr/local/nginx/html/test.html

![[02c1c741dc.png]]

```
# 图片防盗链
location ~*\.(gif|jpg|jpeg|png|bmp)$ {
    valid_referers none blocked devops.com *.devops.com;
    if ($invalid_referer) {
        return 403;
        # 或返回默认图片
        # rewrite ^/ /images/default.jpg break;
    }
    expires 30d;
}
```

参数说明：

- `valid_referers`：设置允许访问资源的来源域名

- `none`：允许直接输入 URL 访问

- 【允许缺失的"Referer"头访问】

- `blocked`：允许没有 Referer 值的请求

- 允许"Referer"头部没有值的访问

- `devops.com`、`*.devops.com`：允许指定域名及子域名访问

- `$invalid_referer`：Nginx 内置变量，判断请求是否来自非法来源
- `return 403`：非法请求返回 403 禁止访问
- `rewrite ^/ /images/default.jpg break`：可选，非法请求返回默认图片

- ![[22599371b9.png]]
- rewrite ^/ /default.png last: 死循环， 访问landscape.png，匹配到location ~*\.(gifljipglipeg|png|bmp)$，rewrite重写default.png，重写后，后面是last还没有结束，default.png也满足location~*\.(gifljipgljpeglpng|bmp)$规则，继续rewrite，这就会导致一直不断的匹配 (死循环)

- `expires 30d`：设置浏览器缓存时间为 30 天

*.devops.com代表泛域名，可以匹配任何标记开头的域名，如www.devops.com，如bbs.devops.com

# 七、第三方模块【插件】

## 1、fancyindex

![[3bc59773b0.png]]

- Nginx 官方没有提供该功能，一些开源开发者定制开发了第三方模块，可以通过加载第三方模块使用新的功能。
- 官方第三方模块文档：[Nginx Third-Party Modules](https://docs.nginx.com/nginx/admin-guide/dynamic-modules/dynamic-modules/#nginx-plus-certified-modules)

编译安装第三方模块：

```
tar zxvf ngx-fancyindex-v0.5.2.tar.gz
tar xvf echo-nginx-module-0.63.tar.gz
cd /root/nginx-1.26.2
./configure --prefix=/usr/local/nginx \
            --user=www --group=www \
            --with-http_ssl_module \
            --with-http_stub_status_module \
            --with-http_realip_module \
            --add-module=/root/ngx-fancyindex-0.5.2/ \
            --add-module=/root/echo-nginx-module-0.63
make && make install && make upgrade
```

配置 nginx.conf：

```
cd /usr/local/nginx
vim conf/nginx.conf

location / {
    fancyindex on;                  # 启用 fancy index 功能
    fancyindex_exact_size off;      # 输出人性化的文件大小
}
```

## 2、echo

- **作用**：echo 模块常用于调试，例如输出 Nginx 默认的系统变量。

配置示例：

```
location / {
    default_type text/plain; # 防止成为下载
    echo $document_root;   # 输出当前请求的文档根目录
}
```

- `$document_root`：Nginx 内置变量，表示当前请求的根目录路径。
- echo 模块可以输出其他系统变量或自定义内容，用于快速调试 Nginx 配置。

有些时候通过浏览器访问Nginx的页面，会变成自动下载，什么原因？答：因为Nginx有默认支持的文件类型，也有不支持的文件类型，不支持的文件类型会自动变更为下载操作！

![[684550575e.png]]

![[e471c01fec.png]]

# 八、Nginx 安全管理

1、反向代理

- 作用：隐藏真实服务，实现安全防护和负载均衡（负载均衡章节详细讲解）。

2、隐藏版本号

利用版本漏洞攻击

前置知识点：curl 命令

- `curl http://192.168.88.104`

- 发起 HTTP 请求，获取响应内容。

- `curl -I http://192.168.88.104`

- 发起 HTTP 请求，不获取响应内容，只获取响应头信息，例如：

```
HTTP/1.1 200 OK
Server: nginx/1.26.2
Date: Fri, 21 Feb 2025 10:11:33 GMT
Content-Type: text/plain
Connection: keep-alive
Vary: Accept-Encoding
```

- 由上图可知，`Server: nginx/1.26.2` 显示了服务器的 Nginx 版本信息。
- 在 `http` 段加入配置，隐藏 Nginx 版本信息，防止被攻击者利用版本漏洞：

```
http {
    server_tokens off;
}
```

# 九、Nginx 发行版本

- **作用**：了解常见 Nginx 发行版本，方便后续选择使用。

1、**Nginx 社区免费版**

- 官网：[https://nginx.org](https://nginx.org/)

2、**NGINX+ 商业版 (Nginx Plus)**

- 官网：[https://www.nginx.com/](https://www.nginx.com/)

3、**淘宝的 Tengine【电商】**

- 官网：[http://tengine.taobao.org](http://tengine.taobao.org/)
- Tengine 由阿里巴巴公司在 Nginx 基础上开发定制，更加适合自身业务需求，后来进行了开源。

安装示例：

```
# tar xvf tengine-3.1.0.tar.gz
# cd tengine-3.1.0
# ./configure --prefix=/usr/local/tengine
# make && make install
```

4、OpenResty 【可拓展】⭐

- **作用**：在 Nginx 基础上，结合 Lua 脚本，实现**高并发 Web 平台开发。**
- 可用于 WAF（Web 应用防火墙），通过 Nginx + Lua + Redis 实现应用型防火墙。
- 官网：[http://openresty.org/cn/](http://openresty.org/cn/)

安装步骤：

```
# tar xvf openresty-1.25.3.2.tar.gz
# cd openresty-1.25.3.2
# ./configure --prefix=/usr/local/openresty
# make && make install
```

# 十、Prometheus 监控 Nginx

- **作用**：使用 Prometheus 实现对 Nginx 的应用监控。

## 1、启动 Prometheus

- 在对应的三台 Prometheus 服务器上启动服务。

## 2、配置 Nginx

```
vim /usr/local/nginx/conf/nginx.conf

worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile      on;
    keepalive_timeout 65;

    server {
        listen       80;
        server_name  localhost;
        root         html;

        location / {
            index index.html index.htm;
        }

        ############ 配置 Stub Status ############
        location = /stub_status {
            stub_status on;
            access_log off;
        }

        ############ PHP 支持 ######################
        location ~ \.php$ {
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            root html;
        }
    }
}
```

- `/stub_status`：用于暴露 Nginx 的状态指标，Prometheus 可通过该接口采集数据。
- `access_log off`：关闭访问日志，减少监控采集时的性能影响。
- PHP 配置部分保持原有 FastCGI 支持。

重启Nginx

sbin/nginx -s reload

![[93dde9ed37.png]]

## 3、安装 nginx_exporter

![[b75d434d1a.png]]

没有

![[b794b93751.png]]

![[df6013e1a8.png]]

![[a9a317db21.png]]

```
# 创建目录
mkdir /usr/local/nginx_exporter

# 解压安装包
tar -xf nginx-prometheus-exporter_1.4.1_linux_amd64.tar.gz -C /usr/local/nginx_exporter/

# 启动 nginx_exporter 并指定 Nginx stub_status 接口
nohup /usr/local/nginx_exporter/nginx-prometheus-exporter --nginx.scrape-uri=http://192.168.88.101/stub_status &
```

![[2a741896ba.png]]

## 4、在 Prometheus 中拉取 Nginx 数据

```
# prometheus.yml 配置示例
global:
  scrape_interval: 15s

alerting:
  alertmanagers:
    - static_configs: []

rule_files: []

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["192.168.88.101:9090"]

  - job_name: "nginx"
    static_configs:
      - targets: ["192.168.88.104:9113"]
```

- `job_name`：定义监控任务名称
- `targets`：指定 Prometheus 拉取数据的地址（nginx_exporter 默认端口 9113）

**重启 Prometheus**

```
nohup /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &
```

重启 Prometheus

```
nohup /usr/local/prometheus/prometheus --config.file="/usr/local/prometheus/prometheus.yml" &
```

![[2d88e36d87.png]]

## 5、Grafana 显示 Nginx 数据

- 使用 Grafana 导入模板 ID：12708，即可可视化显示 Nginx 监控指标。

**小结**

- Prometheus 不仅可以实现系统监控，还可以实现应用监控（如 MySQL、Nginx）。
- 面试提示：从 Grafana 图形中至少找出 3–5 个关键指标作为记忆点
- 记不住一些基础命令：查看服务是否运行？服务端口？应该查询哪些日志？
- 后台服务：jobs，杀死进程：kill%数字编号