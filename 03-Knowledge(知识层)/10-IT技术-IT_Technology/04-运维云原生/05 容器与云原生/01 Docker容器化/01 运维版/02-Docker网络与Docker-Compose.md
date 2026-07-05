# Docker网络与Docker Compose

# 一、单宿主机容器互联方式

有些时候我们希望容器与容器之间也要能通迅,而实现服务的连接(如nginx连远程mysql等)。

nginx容器

mysql容器

## 通过link连接

使用link方式可以实现两个容器的连接,但是方向是**单向**的。

**在docker宿主机上准备2个终端**

**终端一**

```
[root@daniel ~]# docker run -it --name c1 centos /bin/bash
[root@551b2985d420 /]# ip a |grep inet
    inet 127.0.0.1/8 scope host lo
    inet 172.17.0.4/16 brd 172.17.255.255 scope global eth0
    
可以看到c1容器的IP为172.17.0.4/16
```

**终端二**

使用`--link c1:alias1`来连接c1容器;**db为c1容器的别名**

```
[root@daniel ~]# docker run -it --link c1:db --name c2 centos /bin/bash

[root@1e8cd36da3af /]# tail -1 /etc/hosts
172.17.0.4      vm1 	d64d657b4e1f c1 
可以看到c2容器把c1容器的IP与别名db进行了绑定

[root@1e8cd36da3af /]# ping vm1
PING haha (172.17.0.4) 56(84) bytes of data.
64 bytes from vm1 (172.17.0.4): icmp_seq=1 ttl=64 time=0.280 ms
64 bytes from vm1 (172.17.0.4): icmp_seq=2 ttl=64 time=0.137 ms
64 bytes from vm1 (172.17.0.4): icmp_seq=3 ttl=64 time=0.130 ms
```

**小结:**

- c2容器使用`--link c1:vm1`创建,其实就是在c2容器内的`/etc/hosts`文件里增加了c1的主机名别名绑定

- link实现单向通讯

## 通过网络连接

默认创建的容器都在同一个网络上,宿主机的docker0网卡也连接在此网络。

docker inspect 容器名称：获取容器信息，通过IPAddress可以获取容器对应的IP地址

再开一个终端

**终端三**

```
查看容器c1和c2的IP地址，发现这两个容器默认就在一个网络,所以直接用这两个IP就可以直接互相通迅了
[root@daniel ~]# docker inspect c1 |grep IPAddress |tail -1
                    "IPAddress": "172.17.0.4",
[root@daniel ~]# docker inspect c2 |grep IPAddress |tail -1
                    "IPAddress": "172.17.0.5",
[root@daniel ~]# ifconfig docker0 |head -2
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
```

**终端一**

```
容器c1里ping容器c2的IP,可以通
[root@551b2985d420 /]# ping -c 4 172.17.0.5
PING 172.17.0.5 (172.17.0.5) 56(84) bytes of data.
64 bytes from 172.17.0.5: icmp_seq=1 ttl=64 time=0.237 ms
64 bytes from 172.17.0.5: icmp_seq=2 ttl=64 time=0.394 ms
64 bytes from 172.17.0.5: icmp_seq=3 ttl=64 time=0.118 ms
64 bytes from 172.17.0.5: icmp_seq=4 ttl=64 time=0.081 ms
```

**终端二**

```
容器c2里ping容器c1的IP,可以通
[root@1e8cd36da3af /]# ping -c 4 172.17.0.4
PING 172.17.0.4 (172.17.0.4) 56(84) bytes of data.
64 bytes from 172.17.0.4: icmp_seq=1 ttl=64 time=0.340 ms
64 bytes from 172.17.0.4: icmp_seq=2 ttl=64 time=0.077 ms
64 bytes from 172.17.0.4: icmp_seq=3 ttl=64 time=0.054 ms
64 bytes from 172.17.0.4: icmp_seq=4 ttl=64 time=0.100 ms
```

# 二、Docker本地网络

## docker本地有4种类型的网络:

1. bridge这里的bridge和虚拟机里的桥接网络类型不太一样。你可以把这个看作与虚拟机里的NAT类型相似。宿主机能上公网,那么连接此网络的容器也可以上公网。此为**默认网络类型**(也就是说运行容器时不指定网络，默认都属于这种类型)。宿主机上的docker0网卡就是属于此网络.

2. host 和宿主机共享网络。连接此网络的容器使用ifconfig查看的信息和宿主机一致,没有做NAT转换，类似跑在宿主机上一样。

3. none 连接此网络的容器没有IP地址等信息，只有lo本地回环网卡。无法连接公网网络。

4. container 多个容器连接到此网络，那么容器间可以互相通讯，不和宿主机共享。

```
[root@daniel ~]# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
6f92ca98b6e7        bridge              bridge              local
658477d11b2c        host                host                local
411dc19aef37        none                null                local


[root@daniel ~]# docker inspect bridge
查看bridge网络相关的信息
```

## bridge模式（默认）

1, 创建一个名为bridge0的bridge类型的网络,指定网段为10.3.3.0/24(**此网段不能和宿主机已有的网段冲突**),网关为10.3.3.1

```
[root@daniel ~]# docker network create -d bridge --subnet "10.3.3.0/24" --gateway "10.3.3.1" bridge0

可以查看到bridge0这个网络,要删除的话使用docker network rm bridge0命令
[root@daniel ~]# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
6f92ca98b6e7        bridge              bridge              local
39fe88f034d6        bridge0             bridge              local
658477d11b2c        host                host                local
411dc19aef37        none                null                local
```

2, 运行容器，指定使用刚创建的网络

```
[root@daniel ~]# docker run -it -d --name c4 --network bridge0 centos:latest /bin/bash
```

3, 验证并测试此容器的网络

```
[root@daniel ~]# docker inspect c4 |grep IPAddress |tail -1
                    "IPAddress": "10.3.3.2",

可以ping通网关
[root@daniel ~]# docker exec c4 ping -c1 10.3.3.1
PING 10.3.3.1 (10.3.3.1) 56(84) bytes of data.
64 bytes from 10.3.3.1: icmp_seq=1 ttl=64 time=0.319 ms

可以上网
[root@daniel ~]# docker exec c4 ping -c1 www.baidu.cn
PING www.a.shifen.com (14.215.177.39) 56(84) bytes of data.
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=1 ttl=55 time=7.51 ms
```

4, 宿主机上会产生一个网卡名为**br-xxxxx**, IP地址为设置的网关10.3.3.1

```
[root@daniel ~]# yum install net-tools -y
[root@daniel ~]# ifconfig |head -2
br-39fe88f034d6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.3.3.1  netmask 255.255.255.0  broadcast 0.0.0.0

如果想改名的话，可按下面步骤来做
[root@daniel ~]# ifconfig br-39fe88f034d6 down
[root@daniel ~]# ip link set dev br-39fe88f034d6 name docker1
[root@daniel ~]# ifconfig docker1 up
[root@daniel ~]# ifconfig docker1 |head -2
docker1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.3.3.1  netmask 255.255.255.0  broadcast 0.0.0.0
[root@daniel ~]# systemctl restart docker        
```

## host模式

1, **宿主机只能拥有一个host模式网络**(和docker-host共享网络),再创建会报错

```
[root@daniel ~]# docker network create -d host host0
Error response from daemon: only one instance of "host" network is allowed
```

2，运行容器, 指定使用host网络

```
[root@daniel ~]# docker run -it -d  --name c5 --network host centos:latest /bin/bash
```

以上命令执行完毕后，c5容器就直接共享Linux宿主机的网络！

3, 验证并测试此容器的网络

```
可以上公网
[root@daniel ~]# docker exec c5 ping -c1 www.baidu.com
PING www.a.shifen.com (14.215.177.39) 56(84) bytes of data.
64 bytes from 14.215.177.39 (14.215.177.39): icmp_seq=1 ttl=55 time=7.51 ms

[root@daniel ~]# docker exec c5 yum install net-tools -y
容器里ifconfig得到的信息和宿主机上ifconfig得到的信息一致
[root@daniel ~]# docker exec c5 ifconfig 
```

## none模式

不能与外网通讯，只有lo本地通迅

```
[root@daniel ~]# docker run -itd --name c6 --network=none centos:latest /bin/bash
```

## container模式

```
[root@daniel ~]# docker run -itd --name c7 --network=container:c5 centos:latest /bin/bash
```

说明:

- c7容器与c5容器的网络一致(包括IP) => 克隆其他容器网络

## **总结表格**

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**网络模式**|**IP 类型**|**网络隔离**|**性能**|**端口管理**|**适用场景**|
|`bridge`（默认）|容器独立 IP|部分隔离|一般|需手动映射端口（`-p`）|常规应用（Web、数据库）|
|`host`|共享宿主机 IP|无隔离|**最高**|直接占用宿主机端口|高性能需求或本地快速调试|
|`none`|无 IP|**全隔离**|最低|无法通信|极端安全场景或手动网络配置|
|`container:<name>`|复用其他容器 IP|共享网络|一般|依赖其他容器端口|紧密关联的辅助服务（如日志收集）|

# 三、Docker compose

难度：不大，指令类似dockerfile。

作用：实现容器编排，比如我们部署一个博客项目，web容器、数据库容器、redis容器

规定容器的启动运行，连接方式等等。

## docker-compose介绍

用容器运行一个服务,需要使用`docker run`命令。但如果我要运行多个服务呢?

假设我要运行一个web服务,还要运行一个db服务,那么是用一个容器运行,还是用多个容器运行呢?

一个容器运行多个服务会造成镜像的复杂度提高,**docker倾向于一个容器运行一个应用**。

那么复杂的架构就会需要很多的容器,并且需要它们之间有关联(容器之间的依赖和连接)就更复杂了。

这个复杂的问题需要解决,这就涉及到了**容器编排**的问题了。

docker-compose就是可以做容器编排的小工具，它可以在一个文件中定义多个容器,只用一行命令就可以让一切就绪并运行。

## docker-compose部署

安装方法(其它安装方法参考前面harbor章节)

[https://github.com/docker/compose/tags](https://github.com/docker/compose/tags)

```
[root@harbor ~]# mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
[root@harbor ~]# chmod +x /usr/local/bin/docker-compose
```

卸载方法:

```
# rm /usr/local/bin/docker-compose
```

**安装完后验证**

```
# docker-compose -v
Docker Compose version v2.23.3
```

## 使用docker-compose的三个步骤

Docker Compose将所管理的容器分为三层

1. **工程**（project）【文件夹】

2. **服务**（service）【yml】

3. **容器**（contaienr）

Docker Compose运行的目录下的所有文件（docker-compose.yml, extends文件或环境变量文件等）组成一个工程，若无特殊指定工程名即为当前目录名。

一个工程当中可包含多个服务，每个服务中定义了容器运行的镜像，参数，依赖。

一个服务当中可包括多个容器实例

使用Compose基本上分为三步：

1. **Dockerfile 定义应用的运行环境（镜像)**

2. **docker-compose.yml 定义组成应用的各服务**

3. **docker-compose up -d构建并启动整个应用**

## docker compose常见语法

docker compose使用**YAML格式**文件来编排

参考: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

## 核心指令速查表及五字真诀

|   |   |   |   |
|---|---|---|---|
|分类|指令|简单解释|常用示例|
|**基础配置**|`image`|使用的Docker镜像|`image: mysql:5.7`|
||`build`|从Dockerfile构建|`build: ./app`|
||`container_name`|指定容器名称|`container_name: my-web-app`|
||`restart`|重启策略|`restart: always`|
|**网络**|`ports`|端口映射(主机:容器)|`ports: - "8080:80"`|
||`expose`|暴露端口但不映射到主机|`expose: - "3306"`|
||`networks`|加入指定网络|`networks: - backend`|
|**存储**|`volumes`|挂载卷(主机:容器)|`volumes: - "./data:/data"`|
||`tmpfs`|临时文件系统|`tmpfs: /tmp`|
|**依赖**|`depends_on`|服务启动顺序|`depends_on: - db`|
||`links`|连接到其他容器(旧)|`links: - db`|
|**环境**|`environment`|环境变量|`environment: - KEY=VALUE`|
||`env_file`|从文件加载环境变量|`env_file: .env`|
|**命令**|`command`|覆盖默认命令|`command: npm start`|
||`entrypoint`|覆盖镜像入口点|`entrypoint: /app/start.sh`|
|**健康检查**|`healthcheck`|容器健康检查|`healthcheck: test: ["CMD", "curl", "-f", "http://localhost"]`|
|**资源限制**|`deploy`|资源限制和部署配置|`deploy: resources: limits: cpus: '0.5'`|
|**其他**|`user`|指定用户|`user: nginx`|
||`working_dir`|工作目录|`working_dir: /app`|

五字真诀：镜卷环网控

1. **镜** - **镜像选择** (image/build)

- 选哪个镜像，或者从哪构建

- _例_: `image: nginx:latest`

2. **卷** - **卷和持久化** (volumes/restart)

- 数据放哪里，挂哪个目录

- _例_: `volumes: - "./data:/app/data"`

- _关联_: `restart: always` (确保服务始终运行)

3. **环** - **环境配置** (environment/env_file)

- 容器内部的环境变量

- _例_: `environment: - DB_HOST=mysql`

4. **网** - **网络设置** (ports/networks)

- 如何访问和连接服务

- _例_: `ports: - "8080:80"`

5. **控** - **控制启动** (depends_on/command)

- 启动顺序和执行命令

- _例_: `depends_on: - db`

举个例子：想象你在搭建一个房子

1. 先选材料(**镜**像)

2. 确定储物空间(**卷**)

3. 调整室内环境(**环**境变量)

4. 规划门窗出入口(**网**络)

5. 设定开关和遥控器(**控**制命令)

## 常用指令详解

**build**

指定镜像构建时的dockerfile目录,格式一般为绝对路径目录或相对路径目录(dockerfile需要命名为Dockerfile)

```
build: /path/to/build/dir
或者
build: ./dir
```

**image**

指定要启动容器的镜像

```
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd
```

如果镜像不存在,compose尝试拉它.

如果指定了构建, 可以使用指定的选项构建它,并使用指定的tag进行标记。

**environment**

设置镜像变量，它可以保存变量到镜像里面，也就是说启动的容器也会包含这些变量设置

`environment` 和 Dockerfile 中的 `ENV` 指令一样会把变量一直保存在镜像,容器中

**格式**

```
environment:
  RACK_ENV: development
  SHOW: 'true'
或
environment:
  - RACK_ENV=development
  - SHOW=true
```

**expose**

这个标签与Dockerfile中的 `EXPOSE` 指令一样，用于指定暴露的端口，但只将端口暴露给连接的服务，而不暴露给主机.

```
expose:
 - "3000"
 - "8000"
```

**ports**

映射端口，可以使用 `HOST:CONTAINER` 的方式指定端口，也可以指定容器端口（选择临时主机端口），宿主机会随机映射端口

```
ports:
 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
 - "6060:6060/udp"
```

**restart**

指定Docker容器的重启策略

默认值为 `no` ，即在任何情况下都不会重新启动容器

当值为 `always` 时，容器退出时总是重新启动,(会随着docker服务启动而启动容器)；

当值为 `on-failure`时，当出现 `on-failure` 报错（非正常退出，退出状态非0）,才会重启容器

当值为`unless-stopped`时, 在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器

```
restart: "no"
restart: always
restart: on-failure
restart: on-failure:3
restart: unless-stopped
```

**volume**

数据卷挂载，可以直接使用 `HOST:CONTAINER` 这样的格式

或者使用 `HOST:CONTAINER:ro` 这样的格式，ro代表数据卷是只读的，rw代表数据卷可读写的

```
volumes:
  # 只是指定一个路径，Docker 会自动在创建一个数据卷（这个路径是容器内部的）。
  - /var/lib/mysql

  # 使用绝对路径挂载数据卷
  - /opt/data:/var/lib/mysql

  # 以Compose配置文件为中心的相对路径作为数据卷挂载到容器。
  - ./cache:/tmp/cache

  # 使用用户的相对路径（~/ 表示的目录是 /home/<用户目录>/ 或者 /root/）。
  - ~/configs:/etc/configs/:ro

  # 已经存在的命名的数据卷。
  - datavolume:/var/lib/mysql
```

**depends_on**

此标签解决了容器的依赖、启动先后的问题

```
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: mysql
```

使用`docker-compose up web`启动,会先启动redis和db,再启动web

**links**

链接到其它服务的中的容器, 与`link`连接一样效果，会连接到其它服务中的容器

```
web:
  links:
   - db
   - db:database
   - redis
```

## 命令行操作

- **启动**: `docker compose up` (添加 `-d` 后台运行)

- **停止**: `docker compose down` (添加 `--volumes` 删除卷)

- **查看**: `docker compose ps`

- **日志**: `docker compose logs`

- **执行**: `docker compose exec 服务名 命令`

## docker-compose基础应用案例

参考: [https://github.com/docker/awesome-compose](https://github.com/docker/awesome-compose)

### **案例1: wordpress应用**

1, 创建一个名为wordpress的project(工程)

```
[root@daniel ~]# mkdir -p /docker-compose/wordpress
[root@daniel ~]# cd /docker-compose/wordpress
```

2, 创建docker-compose.yml

```
[root@daniel wordpress]# vim docker-compose.yml
services:
  db:
    # We use a mariadb image which supports both amd64 & arm64 architecture
    image: mariadb:10.6.4-focal
    # If you really want to use MySQL, uncomment the following line
    #image: mysql:8.0.27
    command: '--default-authentication-plugin=mysql_native_password'
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=somewordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
    expose:
      - 3306
      - 33060
  wordpress:
    image: wordpress:latest
    ports:
      - 80:80
    restart: always
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress
volumes:
  db_data:
```

说明:

这个应用定义了两个容器服务：db, wordpress

db容器通过mysql/mariadb镜像启动

- MySQL的数据目录挂载到当前目录./data，此目录不存在会自动创建

- 容器重启策略为always

- 设置了连接mysql的4个变量

wordpress容器通过wordpress:latest启动

- 需要db容器先启动再启动wordpress容器

- wordpress容器要link连接db容器

- wordpress容器将80端口映射到宿主机的8010端口

- 容器重启策略为always

- 设置连接数据库的变量

3, 启动

```
[root@daniel wordpress]# docker-compose up -d
```

如果本地没有镜像,下载的两个镜像比较大

```
[root@daniel wordpress]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mysql               5.7                 e9c354083de7        3 days ago          373MB
wordpress           latest              4ba1e63bd20c        8 days ago          501MB
```

4, 访问

访问容器主机的80端口

5, 不用了可以关闭并删除

```
[root@daniel wordpress]# docker-compose stop
Stopping wordpress_wordpress_1 ... done
Stopping wordpress_db_1        ... done

[root@daniel wordpress]# docker-compose rm
Going to remove wordpress_wordpress_1, wordpress_db_1
Are you sure? [yN] y									输入y确认删除容器
Removing wordpress_wordpress_1 ... done
Removing wordpress_db_1        ... done
```

### 案例2: python记数小应用

创建一个Python应用， 使用Flask，将数值记入Redis

1、建立工程目录并在工程目录里创建Python脚本

```
[root@daniel wordpress]# mkdir -p /docker-compose/python_count
[root@daniel wordpress]# cd /docker-compose/python_count
[root@daniel python_count]#

[root@daniel python_count]# vim app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

```
[root@daniel python_count]# vim requirements.txt
flask
redis
```

2、创建 Dockerfile  
在同一目录下，创建Dockerfile

```
[root@daniel python_count]# vim Dockerfile
FROM python:3.9
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
```

说明:

- 容器使用Python3.9的镜像

- 将当前目录下文件拷贝到容器内/code

- 指定工作目录为/code

- 安装python需要的库：flask, redis,flask默认为5000端口

- 容器执行命令 :python app.py

3, 创建编排脚本  
在同一目录下，创建 docker-compose.yml

```
[root@daniel python_count]# vim docker-compose.yml
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
    depends_on:
     - redis
     
  redis:
    image: redis:latest
```

说明:

- 这个应用定义了两个服务：web, redis

- web容器通过当前路径下的Dockerfile生成

- web容器内的5000端口映射到docker宿主机的5000端口

- 将当前目录挂载到web容器内/code

- web容器依赖于redis容器

- redis容器使用redis:latest镜像启动

4, 启动应用  
执行编排脚本，分别制作和拉取web，redis镜像，启动容器

```
[root@daniel python_count]# docker-compose up -d
```

5, 访问http://`docker宿主机IP`:5000

### 案例3: haproxy应用

1, 创建一个工程目录haproxy

```
[root@daniel ~]# mkdir -p /docker-compose/haproxy
[root@daniel haproxy]# cd /docker-compose/haproxy
```

2, 准备haproxy.cfg配置文件

```
[root@daniel haproxy]# vim haproxy.cfg
global
  log 127.0.0.1 local0
  log 127.0.0.1 local1 notice

defaults
  log global
  mode http
  option httplog
  option dontlognull
  timeout connect 5000ms
  timeout client 50000ms
  timeout server 50000ms
  stats uri /status

frontend balancer
    bind 0.0.0.0:80
    mode http
    default_backend web_backends

backend web_backends
    mode http
    option forwardfor
    balance roundrobin
    server web1 web1:80 check
    server web2 web2:80 check
    server web3 web3:80 check
    option httpchk GET /
    http-check expect status 200
```

3, 创建编排脚本

```
[root@vm1 haproxy]# vim docker-compose.yml
services:
  web1:
    image: httpd:latest
    volumes:
      - ./httpd1:/usr/local/apache2/htdocs/
    expose:
      - 80
  web2:
    image: httpd:latest
    volumes:
      - ./httpd2:/usr/local/apache2/htdocs/
    expose:
      - 80
  web3:
    image: httpd:latest
    volumes:
      - ./httpd3:/usr/local/apache2/htdocs/
    expose:
      - 80
  haproxy:
    image: haproxy:latest
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - web1
      - web2
      - web3
    ports:
      - "80:80"
    expose:
      - "80"
```

4, 启动应用

```
[root@daniel haproxy]# docker-compose up -d
```

5, 在挂载目录建立不同的主页用于测试

```
[root@daniel haproxy]# echo web1 > httpd1/index.html
[root@daniel haproxy]# echo web2 > httpd2/index.html
[root@daniel haproxy]# echo web3 > httpd3/index.html
```

6, 访问http://`docker宿主机IP`:80 验证是否负载均衡调度

访问http://`docker宿主机IP`:80/status 验证是否有状态页面