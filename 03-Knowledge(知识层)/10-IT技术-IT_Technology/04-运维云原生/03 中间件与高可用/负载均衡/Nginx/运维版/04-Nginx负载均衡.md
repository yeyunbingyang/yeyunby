# 学习目标

学习目标

1、能够描述负载均衡的作用

2、能够了解负载均衡常见实现方式

3、能够使用Nginx实现负载均衡

4、能为开源Nginx软件安装健康检查模块

5、能够描述Nginx的常见负载均衡算法（掌握3种常见的负载均衡算法）

# 一、背景描述及方案设计

## 1、业务背景描述

- **时间**：2018.6 – 2020.9
- **发布产品类型**：互联网动态站点商城
- **用户数量**：4,000 – 8,000
- **PV**：300,000 – 500,000（24小时访问总次数）
- **DAU**：3,000（每日活跃用户数）

随着业务量骤增，原来的单点服务器已无法满足业务需求：

- 主服务器宕机时，备服务器提供服务，但流量过大时备服务器也可能宕机
- 因此需要多台服务器同时提供服务，形成高可用架构。

## 2、模拟运维场景

![[附件/ad43f8154e.png]]

上述架构服务器，已经不能够满足以上提到的业务需求，架构发生如下变化，怎么办呢？

答：负载均衡技术

# 二、引入负载均衡技术

## 1、讲个故事

有一天上班，老板把我叫进办公室，一边舒服地喝茶，一边说：  
“我们公司开发的这个网站，现在怎么越来越慢了？”

我也注意到了这个问题，一脸无奈地回答：  
“唉，我昨天检查了一下系统，现在的访问量越来越大，无论CPU、硬盘还是内存都不堪重负，高峰期响应速度越来越慢。”

我试探地问道：  
“老板，要不咱买两台好点的机器，把现在的老服务器替换掉吧。我听说IBM的服务器性能挺强的，要不要来一台？”

老板问：“大概多少钱？”  
我说：“大概两万左右，性能足够，咱们这点流量轻轻松松能承受。”

老板委婉地说：  
“好你个鬼，我们小公司，钱要花在刀刃上，我最多给你1万元，你得想办法解决。一周内弄不好，你可以换家公司。”

冷汗直流，心里默默谴责一下万恶的资本家啊。

## 2、解决方案

- 思考问题：现在有两台服务器，但真正工作的只有一台，另一台处于待机状态。能否把它也利用起来，干点活？
- 答：可以，使用负载均衡技术。

## 3、负载均衡技术（LB）

- **定义**：负载均衡（Load Balance）是一种将用户请求平均分配到多台服务器上的技术、分发给后端真实服务器。
- **原理**：将流量或请求分发到不同服务器，使流量平均分配，降低单台服务器压力。

**负载均衡作用**：流量分发，服务器容灾（借助健康检查模块）

1. 流量分发，请求平均分配，降低单台服务器压力
2. 提高安全性，隐藏后端真实服务
3. 屏蔽非法请求（七层负载均衡）http/https协议，实现请求转发【应用层】

**示例**：

- 图片请求 `http://www.itcast.cn/images/1.jpg`
- 负载均衡将请求调度到后端的图片服务器处理

## 4、负载均衡业务架构图

![[附件/678d6384c9.png]]

![[附件/341f871132.png]]

![[附件/7539c623dd.png]]

## 5、负载均衡分类

![[附件/331ca9592a.png]]

**1）二层负载均衡（MAC）**

- 根据OSI模型划分的二层负载均衡
- 一般使用虚拟MAC地址
- 外部请求虚拟MAC地址，由负载均衡器接收后，分配到后端实际**MAC地址**进行响应

**2）三层负载均衡（IP）**

- 一般使用**虚拟IP地址（VIP）**
- 外部请求虚拟IP地址，由负载均衡器接收后，分配到后端实际IP地址进行响应

**3）四层负载均衡（TCP）**

- 基于网络层的负载均衡
- 在三层基础上，通过`IP + Port`接收请求并转发到对应服务器
- 示例：  
    `www.shop.com` → 负载均衡器（192.168.88.200）→ 根据IP+端口转发请求

**4）七层负载均衡（HTTP）**

- 智能型负载均衡（应用层）
- 根据URL进行请求转发（反向代理）
- 示例：

- `www.shop.com/index.php`

```
location \.php$ {
    proxy_pass xxx;
}
```

- `www.shop.com/images/avatar.png`

```
location \.(jpg|jpeg|png|gif)$ {
    proxy_pass yyy;
}
```

**面试：四层与七层负载均衡区别**

**① 底层实现不同**

- 四层负载均衡：基于网络层和传输层，通过`IP + Port`实现请求转发
- 七层负载均衡：基于应用层，通过URL地址进行请求转发

**② 性能不同**

- 四层：类似转发器，仅做转发，效率更高
- 七层：需要解析URL后再转发，处理逻辑更多，性能相对较低

**③ 安全性不同**

- 四层：不解析具体请求内容，安全控制能力较弱
- 七层：可以根据URL进行判断，能够屏蔽异常请求，相对更加安全

## 6、常见负载均衡实现方式

- **硬件级别**

- F5 BIG-IP：性能强，价格高（几万到几十万不等）
- ![[附件/987d12450c.png]]

- **软件级别（性价比高）**

- LVS：Linux下的四层负载均衡（IP + Port），基于内核IPVS实现调度（支持NAT等模式）
- Nginx：

- 主要用于七层负载均衡（HTTP应用层）
- 通过`upstream`实现请求分发
- 新版本也支持四层负载均衡

- HAProxy：支持四层和七层负载均衡

- 性能介于lvs 与nlginx之间

![[附件/9cc860f3be.png]]

**四层负载均衡（L4）原理**

- 主要根据报文中的**目标IP地址和端口（IP + Port）**，结合负载均衡策略，选择后端服务器。
- 以TCP为例：

- 当负载均衡设备接收到客户端的第一个SYN请求时，选择一个后端服务器
- 修改报文中的目标IP地址（改为后端服务器IP），转发请求
- TCP三次握手由客户端与服务器直接建立

- 负载均衡设备类似于**路由器/转发器**
- 在某些场景下，为保证回包正常返回，可能还会修改源IP地址

**七层负载均衡（L7）原理**

- 又称为**内容交换（Content Switching）**
- 根据应用层内容（如**HTTP请求中的URL、Header等**）进行转发决策
- 工作流程：

- 负载均衡设备先与客户端建立TCP连接
- 再与后端服务器建立TCP连接
- 获取应用层数据后，根据内容选择后端服务器

- 本质上类似于**代理服务器（反向代理）**

**对比总结：**

- **性能**：

- 四层：只做转发，性能高
- 七层：需要解析应用层数据，性能较低

- **功能**：

- 四层：仅基于IP+端口转发
- 七层：可根据URL、文件类型等智能调度

- 如：图片请求转发到图片服务器

- **安全性**：

- 七层可以识别并过滤异常请求（如部分SYN Flood攻击防护能力更强）

- **适用场景**：

- 七层：主要用于HTTP/HTTPS网站、B/S系统
- 四层：适用于通用TCP/UDP服务（如数据库、RPC等）

①底层不一样，基于IP+Port、基于URL或者主机IP

②性能有所不同，四层性能最好，七层性能要略低一些，因为七层需要额外的数据处理

③安全型，七层安全性更高

今天主要给大家介绍一下Nginx七层负载均衡，主要通过以下两个步骤来完成：

①环境准备

②Nginx负载均衡配置（核心）

# 三、服务器基本环境部署

## 1、克隆复制虚拟机（LB）

|   |   |   |   |   |
|---|---|---|---|---|
|角色|IP|主机名|功能|备注|
|web01 移除keepalived|192.168.88.104|web01.itcast.cn|master|主|
|web02 移除keepalived|192.168.88.105|web02.itcast.cn|backup|备|
|mysql|192.168.88.106|mysql01.itcast.cn|数据节点||
|lb01+ keepalived|192.168.88.107|lb01.itcast.cn|load balance|主|
|lb02+ keepalived|192.168.88.108|lb02.itcast.cn|load balance|备|

web服务器不需要keepalived 维持监测 使用健康模块

## 2、修改虚拟机Mac地址、IP地址、IP与主机名绑定

![[附件/c0b328e5d5.png]]

![[附件/789a8a58f8.png]]

```
# 设置主机名
hostnamectl set-hostname web01.itcast.cn
hostnamectl set-hostname web02.itcast.cn
hostnamectl set-hostname mysql01.itcast.cn
hostnamectl set-hostname lb01.itcast.cn
hostnamectl set-hostname lb02.itcast.cn
```

```
# /etc/hosts
127.0.0.1       localhost localhost.localdomain localhost4 localhost4.localdomain4 localhost6 localhost6.localdomain6
::1             localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.88.104  web01.itcast.cn
192.168.88.105  web02.itcast.cn
192.168.88.106  mysql01.itcast.cn
192.168.88.107  lb01.itcast.cn
192.168.88.108  lb02.itcast.cn
```

## 3、关闭防火墙与SELinux

```
# systemctl stop firewalld
# systemctl disable firewalld
# setenforce 0
# sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
```

## 4、安装依赖包及时间同步

**安装依赖包**

```
# yum install vim wget rsync net-tools epel-release -y
```

**时间同步操作**

**第一步：安装 chrony**

```
sudo dnf install -y chrony
```

**第二步：启动并启用 chronyd 服务**

```
sudo systemctl enable --now chronyd
```

**第三步：配置 NTP 时间服务器**

- 编辑 `/etc/chrony.conf` 配置文件，添加或修改 NTP 服务器地址
- 示例：使用阿里云 NTP 服务器

```
sudo vi /etc/chrony.conf
```

编辑 /etc/chrony.conf 文件，将原 NTP 服务器注释或替换

```
# 原内容：
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (https://www.pool.ntp.org/join.html).
pool 2.centos.pool.ntp.org iburst

# 替换为：
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

保存配置后，重启 chronyd 服务

```
sudo systemctl restart chronyd
```

# 四、Nginx负载均衡实现

## 1、停掉并删除 Web01/Web02 的 Keepalived

```
# 停止 keepalived 服务
systemctl stop keepalived

# 卸载 keepalived
yum remove keepalived -y
```

## 2、劫持域名

- 让 `www.shop.com` 指向 LB01
- 修改 Windows 主机的 `hosts` 文件：

```
# 文件路径：C:\Windows\System32\drivers\etc\hosts
192.168.88.107   www.shop.com
```

**注意事项**：

- Windows 11 对 `hosts` 文件有限制，修改前需先拖到桌面，修改后再放回原位置。

## 3、在 LB01 中安装 Nginx 软件

**安装依赖库**

```
[root@lb01]# yum -y install pcre-devel zlib-devel openssl-devel
```

**解压 Nginx 源码并进入目录**

```
[root@lb01]# tar -zxf nginx-1.26.2.tar.gz
[root@lb01]# cd nginx-1.26.2
```

**创建 Nginx 运行用户**

```
[root@lb01]# useradd -r -s /sbin/nologin www
```

**编译安装 Nginx**

```
[root@lb01]# ./configure --prefix=/usr/local/nginx --user=www --group=www \
--with-http_ssl_module --with-http_stub_status_module --with-http_realip_module
[root@lb01]# make && make install
```

**启动 Nginx**

```
[root@lb01]# cd /usr/local/nginx
[root@lb01]# sbin/nginx -c /usr/local/nginx/conf/nginx.conf
```

注：`-c` 参数相当于 `--config`，用于指定 Nginx 配置文件路径

打开浏览器，使用www.shop.com对LB01发起访问，如下图所示：

![[附件/f861c711c4.png]]

**配置 Nginx 为系统服务并加入开机启动**

```
# 停止正在运行的 Nginx（如果已有启动）
sbin/nginx -s stop

# 启动 Nginx 服务
systemctl start nginx

# 设置开机自启
systemctl enable nginx
```

![[附件/50aebcf6da.png]]

## 4、负载均衡配置详解（重点）

**第一步：备份配置文件并去掉注释与空行、编辑 nginx.conf**

```
# 进入 Nginx 目录
cd /usr/local/nginx

# 备份 nginx.conf 文件
cp conf/nginx.conf conf/nginx.conf.bak

# 去掉注释行和空行
grep -Ev '#|^$' conf/nginx.conf > conf/nginx.conf.clean
```

```
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout 65;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page 500 502 503 504 /50x.html;

        location = /50x.html {
            root html;
        }
    }
}
```

说明：

- `worker_processes`：工作进程数
- `worker_connections`：每个进程最大连接数
- `keepalive_timeout`：保持长连接时间
- `server` 块配置监听端口、根目录、首页文件及错误页

**第二步：配置 Nginx 负载均衡**

```
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile      on;
    keepalive_timeout 65;

    # 上游服务器组
    upstream shop {
        server 192.168.88.104:80;
        server 192.168.88.105:80;
    }

    # 前端负载均衡服务器
    server {
        listen 80;
        server_name www.shop.com;

        location / {
            proxy_pass http://shop;
            proxy_set_header Host $host;
        }

        error_page 500 502 503 504 /50x.html;

        location = /50x.html {
            root html;
        }
    }
}
```

说明：

- `upstream shop` 定义后端 Web01/Web02 服务器组
- `proxy_pass http://shop;` 将请求转发给 upstream 组
- `proxy_set_header Host $host;` 保留原请求 Host 头，保证后端识别正确的域名

**第三步：重载 Nginx 配置**

```
# 重载 Nginx，使配置生效
sbin/nginx -s reload
```

**验证请求转发是否正常**

- 在 Web01 和 Web02 上分别准备相同位置、相同名称的测试文件，例如 `index.html`
- 通过访问 LB01 的 `www.shop.com`，确认请求能够被均匀分发到 Web01 和 Web02，确保负载均衡生效

**验证请求转发是否正常**

- 在 Web01 上创建测试文件：

```
echo web01 > /www/wwwroot/www.shop.com/niushop/demo.html
```

- 在 Web02 上创建测试文件：

```
echo web02 > /www/wwwroot/www.shop.com/niushop/demo.html
```

说明：

- 通过访问 LB01 的 `www.shop.com/niushop/demo.html`，观察返回内容
- 如果请求轮询到 Web01，返回 `web01`；请求轮询到 Web02，返回 `web02`
- 这样即可确认 Nginx 负载均衡配置已经生效

**第四步：解决 Web01/Web02 访问日志显示问题（获取客户端真实 IP）**

**① 在 LB01 中设置请求头，将客户端 IP 转发给后端**

```
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile      on;
    keepalive_timeout 65;

    upstream shop {
        server 192.168.88.104:80;
        server 192.168.88.105:80;
    }

    server {
        listen 80;
        server_name www.shop.com;

        location / {
            proxy_pass http://shop;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        error_page 500 502 503 504 /50x.html;

        location = /50x.html {
            root html;
        }
    }
}
```

```
# 重载 Nginx 配置
sbin/nginx -s reload
```

|   |   |   |
|---|---|---|
|**配置指令**|**作用说明**|**为什么需要它？**|
|`**proxy_pass http://shop;**`|将请求转发到名为 `shop`<br><br>的上游服务器组（upstream）。|定义数据流向，通常配合 `upstream shop { ... }`<br><br>使用。|
|`**proxy_set_header Host $host;**`|将原始请求中的 `Host`<br><br>头部传给后端。|如果后端服务器有多个虚拟主机，它需要靠这个头来判断用户访问的是哪个域名。|
|`**proxy_set_header X-Real-IP $remote_addr;**`|把直接连接 Nginx 的 IP 传给后端。|默认情况下，后端看到的 IP 是 Nginx 的内网 IP，这行能让后端看到“上一跳”的 IP。|
|`**proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;**`|将客户端 IP 追加到 `X-Forwarded-For`<br><br>链路中。|**最重要的一行**。它会保留原始用户 IP 以及路径中所有代理的 IP 列表。|

---

**② 在 Web01 和 Web02 上配置日志格式，显示真实客户端 IP**

```
# 编辑网站 Nginx 配置
vim /www/server/panel/vhost/nginx/www.shop.com.conf

http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log logs/access.log main;
}
```

```
# 重载 Web01/Web02 Nginx 配置
sbin/nginx -s reload
```

说明：

- `X-Real-IP` 和 `X-Forwarded-For` 请求头传递客户端真实 IP
- 日志格式 `$http_x_forwarded_for` 可记录客户端真实 IP，而非 LB01 的 IP
- 配置完成后，通过访问测试，可以在 Web01/Web02 的 access.log 中看到客户端真实 IP

**BT 宝塔安装 Nginx 配置日志并添加测试文件**

**配置日志格式显示真实客户端 IP**

```
# 编辑网站 Nginx 配置
vim /www/server/panel/vhost/nginx/www.shop.com.conf

http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log logs/access.log main;
}
```

```
# 重载 Nginx 配置
sbin/nginx -s reload
```

---

效果：

![[附件/7293a27f6d.png]]

**添加 Web01 测试文件**

```
echo 'web01' > /www/wwwroot/www.shop.com/niushop/demo.html
```

**添加 Web02 测试文件**

```
echo 'web02' > /www/wwwroot/www.shop.com/niushop/demo.html
```

![[附件/f0133f093e.png]]

## 5、负载均衡常见错误汇总

1. **请求转发不稳定**

- **现象**：请求已经转发，但访问一会正常、一会异常。
- **原因**：默认负载均衡使用轮询算法，Web01、Web02 轮流接收请求。如果某台 Web 服务器异常（如未安装宝塔或 Nginx 没有启动），就会出现访问不稳定。
- **解决**：检查各 Web 节点 Nginx 是否安装并启动。

2. **访问** [**www.shop.com**](http://www.shop.com/) **出现 SQL 错误**

- **原因**：某台服务器的 SQL 连接异常，例如 MyCAT2 配置错误（主机 IP、用户名、密码或端口 8066），或 node2 数据库未启动。
- **解决**：检查数据库连接配置并确保数据库服务运行。

3. **找不到 niushop 文件夹**

- **原因**：虚拟机未安装宝塔或被还原，导致项目目录丢失。
- **解决**：确认宝塔面板和项目目录存在。

4. **宝塔登录信息遗忘**

- **原因**：未记录宝塔账号、密码或面板地址。
- **解决**：安装、账号、密码、访问地址应记录在安全本子或密码管理工具中，以便随时查阅。

5. web01和web02都正常，但是访问时总是web01或者总是web02，不切换

- （可能并没有问题，而是因为浏览器缓存造成）
- F12=》开发工具中，停用缓存 按Ctrl+F5强制刷新，重新请求

## 6、负载均衡请求分发关键字说明

backup关键字：其他的没有backup标识的服务器都无响应，才分发到backup服务器。  
代码块

```
# vim conf/nginx.conf
http {
    upstream shop {
        server 192.168.88.104:80 backup;
        server 192.168.88.105:80;
    }
}
```

down关键字：任何时候，请求都不分发给配置了down关键字的服务器。  
代码块

```
# vim conf/nginx.conf
http {
    upstream shop {
        server 192.168.88.104:80;
        server 192.168.88.105:80 down;
    }
}
```

用的最多的还是backup，关键时刻起到热备作用！！！

遇到问题：在浏览器中输入 `http://www.shop.com` 经常变更为 `https`，导致服务无法访问，应该如何解决？

其实在 Linux 操作系统中，也有内置浏览器 `curl` 命令，主要作用，就是模拟 HTTP 发送 GET 或者 POST 请求，实现浏览器功能。

LB01 服务器：  
代码块

```
vim /etc/hosts
192.168.88.107 www.shop.com
```

使用 curl 模拟访问 demo.html  
代码块

```
curl http://www.shop.com/demo.html
```

## 7、负载均衡的3种调度算法（请求规则）

Nginx 官方默认 3 种负载均衡的算法：  
① Round-Robin（RR 轮询，默认）：一次一个的来（理论上的，实际实验可能会有间隔）  
② Weight（权重）：权重高多分发一些，服务器硬件更好的设置权重更高一些

```
# vim conf/nginx.conf
http {
    upstream shop {
        server 192.168.88.104:80 weight=4;
        server 192.168.88.105:80 weight=6;
    }
}
```

IP_HASH：代表把同一个 IP 来源的请求分到同一个后端服务器 => 没有 Redis 出现之前，使用 Nginx，大部分都使用 ip_hash

举个例子：比如登录操作（账号、密码、验证码）

普及一个概念：验证码 => Session 技术 => 在服务器端生成一个文件，然后保存了验证码上的文字。当用户登录时，手工输入验证码，输入完验证码需要与 session 文件中保存的文字相匹配。

问题出现场景：如果采用 RR 轮询，一次请求到 Web01，一次请求到 Web02

- 首次打开登录页面 => 生成一个验证码 => Web01 服务器上生成
- 当我们输入完验证码以后，单击登录 => 又发送了一次请求，这次请求可能定位到 Web02
- Web02 上没有 session 文件，最终导致验证失败

这个例子说明了为什么在涉及 **session 或验证码** 的场景下，通常会使用 **IP_HASH** 来保证同一个用户的请求总是落在同一台服务器上。

```
# vim conf/nginx.conf
http {
    upstream shop {
        ip_hash;
        server 192.168.88.104:80;
        server 192.168.88.105:80;
    }
}
```

小结：

- Round-Robin：RR 轮询算法，请求均分，支持
- `weight` ，例如 `weight=8`
- IP_HASH：淘宝、京东等场景使用，同一个 IP 的所有请求都由同一个服务器处理

## 8、Session 共享解决方案（调度算法）

① HTTP 协议：HTTP 是无状态协议，无法记录用户的浏览轨迹。  
② Cookie 技术：可以把用户的信息记录在浏览器的缓存中（缓存存在过期时间）。  
③ Session 技术：可以把用户的浏览轨迹保存在服务器端（默认保存在 `/tmp` 目录）。

- 验证码也是 Session 文件，其产生的验证码会保存在这个文件中。

模拟负载均衡与 Session 共享问题：

1. 配置负载均衡（默认算法使用轮询算法）。
2. 使用账号密码登录功能，登录后台管理界面（admin，123456）。

- 发现问题：无论怎么输入验证码，始终提示验证失败。
- 原因：使用轮询算法，生成验证码是一次请求，验证验证码是另一请求，两次请求可能分发到不同服务器，导致验证失败。

3. 解决办法：使用 IP_HASH 算法，让同一个 IP 的请求分发到同一台 Web 服务器，问题得到解决。

## 9、Nginx 健康检查模块（面试）

开源、社区版使用【商业版自带】

安装第3方模块 upstream_check_module

实现了后端接口的自动重试和故障隔离

默认情况下，我们使用的 Nginx 属于开源 Nginx，默认不支持健康检查。

影响示例：

- 用户请求 => Nginx 负载均衡 =>

- Web01
- Web02（异常，返回 404 文件未找到、500 服务器端错误）

- 认为所有业务服务器都正常

安装健康检查模块：

```
cd /root/nginx-1.26.2

./configure \
--prefix=/usr/local/nginx \
--user=www \
--group=www \
--with-http_ssl_module \
--with-http_stub_status_module \
--with-http_realip_module \
--add-module=/root/nginx_upstream_check_module-0.4.0

make && make install && make upgrade
```

配置：

```
http {
    upstream shop {
        server 192.168.88.104:80;
        server 192.168.88.105:80;

        check interval=3000 rise=2 fall=3 timeout=1000 type=http;
        check_http_send "GET / HTTP/1.0\r\n\r\n";
        check_http_expect_alive http_2xx http_3xx;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://shop;
        }
    }
}
```

参数说明：

1. **check interval=3000**

- 含义：检查间隔时间，单位毫秒（ms）。
- 解释：每隔 3000 毫秒（即 3 秒）进行一次健康检查。Nginx 会每 3 秒向后端服务器发送一次健康检查请求，以确认服务器是否正常运行。

2. **rise=2**

- 含义：连续成功检查的次数。
- 解释：当连续 2 次健康检查成功时，Nginx 认为后端服务器是正常的。例如，如果第一次检查失败，但接下来两次检查都成功，Nginx 会将该服务器标记为“正常”，并开始将流量转发到该服务器。

3. **fall=3**

- 含义：连续失败检查的次数。
- 解释：当连续 3 次健康检查失败时，Nginx 认为后端服务器是失败的。例如，如果连续三次检查都失败，Nginx 会将该服务器标记为“失败”，并停止将流量转发到该服务器，直到后续检查成功。

4. **timeout=1000**

- 含义：超时时间，单位毫秒（ms）。
- 解释：每次健康检查的超时时间为 1000 毫秒（即 1 秒）。如果在 1 秒内没有收到响应，这次检查将被视为失败，有助于快速识别无响应的服务器，避免流量被发送到不可用服务器。

5. **type=http**

- 含义：检查的类型。
- 解释：指定健康检查的类型为 HTTP。Nginx 会通过 HTTP 协议向后端服务器发送请求，并根据返回的 HTTP 状态码判断服务器是否正常。通常，返回状态码在 200-299 之间视为正常。

宝塔默认页面导致 健康监测出错

## 10、高可用负载均衡（keepalived+Ib）

架构图：

添加lb新节点 保证nginx高可用

![[附件/58d55e6de4.png]]

```
1. 克隆新lb
2. 配置域名劫持 本机DNS 域名 vip  
3. 安装keepalived 监控lb
4. 配置 无争抢HA
```