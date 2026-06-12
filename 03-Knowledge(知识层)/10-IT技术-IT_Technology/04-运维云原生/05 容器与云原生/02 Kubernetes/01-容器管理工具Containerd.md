# 1.【了解】Containerd 发展历史

为什么要学它？

· 核心地位：  
Containerd 处于容器技术栈的基础层面，负责容器的生命周期管理，包括容器的创建、启动、停止、销毁等操作。  
· 技术基石：  
它是理解更高级容器编排工具（如 Kubernetes）的基础，了解 Containerd 有助于你更好地理解 Kubernetes 是如何与底层容器进行交互的。

## 学习目标

了解 Containerd 和 Docker 之间的关系  
了解云计算、云原生、Containerd 的发展历史  
熟悉 Containerd 的基本架构  
能使用 Containerd 的基本操作

## 1 Containerd 的前世今生

云计算背景

2006 年，亚马逊公司宣布推出 AWS（Amazon Web Service）平台。次年又推出了在线存储服务 S3（Simple Storage Service）和弹性计算云 EC2（Elastic Compute Cloud）等服务。但当年亚马逊并没有谷歌和 IBM 的影响力，并未引起业界震动。后来随着云计算的爆发，亚马逊在商业模式上的积累，奠定了 AWS 的高速发展和领军地位。

2006 年，谷歌推出了 “Google 101 计划”，并正式提出 “云” 的概念和理论。该计划基于谷歌员工比希利亚的设想，初衷是设置一门课程，着重引导学生们进行 “云” 系统的程序开发。

2007 年 10 月，谷歌、IBM 联合了美国 6 所知名大学，帮助学生在大型分布式计算系统上进行开发。当时 IBM 发言人指出，这种所谓的 “大型分布式计算系统” 就是云计算，明确提出 “云计算” 这一新概念。

2008 年 10 月，微软公司的 Windows Azure Platform 公共云计算平台发布，开始了微软公司的云计算之路。

2010 年 7 月，美国太空总署联合 Rackspace、AMD、Intel、戴尔等厂商共同宣布 “OpenStack” 开源计划，成立了 OpenStack 开源云平台。

【初次邀约】  
2013 年 Docker 公司推出 Docker 产品后，由于其对全球技术产生了一定的影响力，Google 公司明显感觉到自己的江湖地位受到了威胁，希望 Docker 公司能够与自己联合打造一款开源的容器运行时，作为 Docker 核心依赖，但 Docker 公司拒绝了。

【成立开放容器倡议社区】  
接着 Google 公司联合 RedHat、IBM 等公司，说服 Docker 公司把其容器核心技术 libcontainer 捐给中立社区（OCI，Open Container Initiative），并更名为 runC。

【成立云原生基金会】  
2015年，为了进一步遏制 Docker 在未来技术市场的影响力，避免在容器市场上 Docker 一家独大，Google 公司联合 RedHat、IBM 等成立 CNCF（**Cloud Native** Computing Foundation）基金会，即云原生计算基金会。

【甩出秘密武器】  
CNCF 的目标很明确：既然在容器应用领域无法与 Docker 抗衡，那就转向 Google 更有经验的技术市场——大规模容器编排应用场景。Google 公司将其内部使用的 Borg 系统开源为 Kubernetes，也就是我们今天所说的云原生技术生态。

容器编排是一项能够完成容器部署、调度、伸缩以及健康监控等（全生命周期）任务的自动化管理技术。

Borg  
Borg 是《星际迷航》中的虚构宇宙种族——博格人。每个博格人没有自主意识，整体受 Borg Queen 控制，集群拥有高度智慧和战斗能力。

命名来源  
受电影启发，Google 内部使用 Borg 命名公司的集群管理系统。

2015 年 Docker 公司推出了 Docker Swarm，意在一统 Docker 生态，让 Docker 既可以实现容器应用管理，也可以实现大规模容器编排。

经过近 1 年左右的市场验证后，发现在容器编排方面无法独立抗衡 Kubernetes，所以 Docker 公司于 2017 年正式宣布原生支持 Kubernetes。

至此，Docker 在大规模容器编排应用市场败下阵来。

但是 Docker 依然不甘心失败，将 Docker 核心依赖 Containerd 捐给了 CNCF，以此说明 Docker 依旧是一个 PaaS 平台（目的是为了在容器生态中占有一席之地）。

![[附件/0e7d71e28f.png]]

2020 年 CNCF 基金会宣布 Kubernetes 1.20 版本将不再仅支持 Docker 容器管理工具，因此接下来 Kubernetes 容器运行时的主角是 Containerd，涵盖整个容器运行时管理的所有需求。

补充  
· 运行时（Runtime）  
在计算机中，是指程序的运行阶段、运行所依赖的环境，以及在运行过程中可能出现的各种情况。

![[附件/e27adc2634.png]]

从下面这张图，我们可以看出，

- Containerd主要是作为底层容器与上层容器编排系统进行交互的容器运行时工具。
- 只要是符合OCI规范的容器，都可以由containerd进行调用管理。

![[附件/b1889a7b40.png]]

小结

Containerd是Container Daemon的缩写，daemon表示______守护进程；

顾名思义，它就是一个container的运行时管理工具。

## 2 Containerd 架构

### 1 整体架构

Containerd 设计的目的是为了嵌入到 Kubernetes 中使用，它是一个工业级的容器运行时，不提供给开发人员和终端用户直接使用。

![[附件/8c1d0ab79f.png]]

云原生架构

- 1️⃣ Platform 层（平台层）

- Kubernetes 云厂商（阿里云 / AWS）
- 作用：下发任务（部署应用） 资源调度（CPU / 内存） 集群管理
- 面向最终用户或集群管理员。

- 2️⃣ Client 层（客户端）

- 作用：调用 API 将指令转化为具体的容器操作（如：启动容器）。
- 组件：

- **kubelet / CRI Runtime**：Kubernetes 用的容器接口。
- **Docker Container Engine / Pouch**：容器客户端工具，内部通过 `containerd client` 调用 containerd。
- **BuildKit / ctr**：构建或管理容器镜像的工具。

- 3️⃣ containerd 层（核心容器运行时）

- 接口层（API）

- Containerd 暴露标准接口（gRPC），不直接操作内核
- 组件

- **CRI**：Kubernetes 的容器运行接口。
- **containerd**：提供 gRPC 服务接口和 Service Handlers。
- **Prometheus**：提供 metrics 监控。

- 核心层 (Core) —— 大脑

- **Services**：管理容器、镜像、任务（Tasks）的逻辑。
- **元数据 (Metadata)**：保存容器名称、镜像 ID 等配置，支持 **Namespaced (命名空间隔离)**。

- backend 后端层
- 数据存储与快照（Snapshotter），管理镜像分层。

- **Content Store**：存储容器镜像和内容，支持 plugin 和 local。
- **Snapshotter**：存储容器文件系统快照，支持 overlay、btrfs、devmapper、native、windows、
- **Runtime**：v2 shim client，连接底层容器运行时。

- containerd-shim

- 用于隔离和管理容器进程生命周期，支持多种底层 runtime：

- runc、runhcs、kata、Firecracker、gVisor、shim

- 4️⃣ System 层（系统底层） 支持的硬件/操作系统：

- Linux 内核 本质：操作系统核心

- Linux 指内核 Linux操作系统指使用了Linux内核

- CPU 架构

- ARM（精简指令集） 应用：手机、嵌入式设备 代表：高通骁龙
- x86（复杂指令集）应用：服务器、PC

### 2 架构缩略

Containerd被分为三个大块：Storage，Metadata 和 Runtime

![[附件/a5928cfd82.png]]

容器运行时 管理容器的全过程生命周期

### 3 性能对比

这是使用 bucketbench 对 Docker、crio 和 Containerd 的性能测试结果。包括启动、停止和删除容器，以比较它们所耗的时间：

- **Bucket（桶）**

- 常见于对象存储（如 S3、OSS）
- 类似一个“文件夹容器”

- **Bench（Benchmark）**

- 性能测试（压测）

分批次数据性能压测

![[附件/39501f7aa6.png]]

结论： Containerd 在各个方面都表现好，总体性能优于 Docker 和 crio。

## 总结

1、云计算的概念是在 2007 年正式被提出来的；

2、runC 的前身，是 Docker 公司开发的 libcontainer；是 Docker 公司的核心技术；

3、Cloud Native Computing Foundation 的中文翻译是 云原生计算基金会；

4、云原生的概念是由 CNCF 基金会在 2015年Kubernetes 推广过程中提出的；

5、containerd 中的 d 对应的英文单词是 daemon；表示运行时管理工具；

6、除了 Google 公司开放出的 K8S，Apache 基金会还发布了 Mesos，Docker 公司还发布了 Swarm 容器编排工具。

思考

Kubernetes经常被称为K8S，这是为什么？ 对应的，i18n表示什么?

中间字母/ i18n 国际化

# 2 【掌握】 Containerd安装

## 1 环境准备

```
# 修改主机名，如果修改完，执行 bash 生效
hostnamectl set-hostname 新主机名 && bash

# 修改 IP 地址
vi /etc/NetworkManager/system-connections/ens33.nmconnection
改动如下部分
[ipv4]
method=manual
addresses=192.168.88.111/24
gateway=192.168.88.2
dns=8.8.8.8

# 重启
reboot
```

## 2 dnf 安装

### 1 获取阿里源

在 CentOS Stream 9 系统中，我们可以从阿里云获取适用于该系统的 Docker DNF 源，该源包含了 Containerd 软件的相关信息，便于后续安装。

```
# 先查看当前的镜像源
dnf repolist -v

# 如果不是阿里源，再执行以下命令，从阿里云下载 Docker DNF 源配置文件到系统指定目录
# ce 表示 Community Edition，社区版
dnf install -y wget

# -O 输出到指定文件
wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 再次查看
dnf repolist -v
```

![[附件/bf48494297.png]]

![[附件/4838bb1ec0.png]]

### 2 dnf 命令行安装

通过上一步获取到 Containerd 软件信息后，使用 dnf 命令进行安装。

```
# 安装 containerd.io 软件
dnf -y install containerd.io
```

![[附件/72e7e26009.png]]

如果已经安装的有了，则是下面的提示：

![[附件/1e95abf09e.png]]

### 3 启动服务

下载完成后，查看dnf 源中containerd软件的相关信息。

```
# 使用 dnf list 命令列出所有软件包，并通过 grep 过滤出包含 containerd 的软件包信息
dnf list | grep containerd
```

正常情况下，会显示类似如下信息：

![[附件/edce0387d2.png]]

执行以下系统命令

```
# 设置 containerd 服务启动及开机自启动
systemctl enable containerd

# 启动命令
systemctl start containerd

# 查看 containerd 服务启动状态
systemctl status containerd
```

![[附件/a9d6bbfdf6.png]]

**思考**  
1、我们提到过，service 后面的 enabled 表示服务自启动；那么 preset 后面显示 disabled，表示什么？

【preset - 预设】

**答案：**  
preset 表示**系统预设策略（默认策略）**。

- **enabled**：表示该服务已经被手动或命令设置为开机自启动
- **preset: disabled**：表示在系统的**默认规则中，这个服务是不建议开机自启的**

👉 关键区别：

- enabled：**当前状态（你现在的配置）**
- preset：**默认策略（系统建议的状态）**

📌 举例：

- enabled + preset: disabled  
    → 说明你**手动开启了自启动**，但系统默认其实是“不建议开机启动”的

📌 补充：如果执行：

```
systemctl preset containerd
```

系统会按照 preset 规则，把服务恢复为默认策略（这里会变成 disabled）。

### 4 验证测试

```
# 安装 containerd 时 ctr 命令亦可使用，ctr 命令主要用于管理容器及容器镜像等。
# 使用 ctr 命令查看 containerd 客户端及服务端相关信息。
ctr version
```

![[附件/0877fba3cc.png]]

ctr | less

![[附件/fca8c0378c.png]]

## 总结

1、dnf 安装方式 Containerd 的执行方法为：

```
dnf install -y containerd.io
```

2.mkdir 和 mkdir -p 的区别

- mkdir：创建目录（父目录不存在会报错）
- mkdir -p：递归创建目录（父目录不存在会自动创建）

3、cp 命令 cp /root/* 中的 * 表示什么？

- 表示通配符，代表 /root/ 目录下的**所有文件（不包含隐藏文件）**

4、怎么把 /usr/local/bin 加入到永久环境变量？

```
# 打开家目录下的文件
vi ~/.bashrc

# 在 export PATH 后面另起一行，补上路径
export PATH=$PATH:/usr/local/bin

# 更新，使生效
source ~/.bashrc

# 重启电脑
reboot
```

5、 less 和 more 的区别

**分页器（Pager）**，但 `**less**` **比** `**more**` **更强大**。

# 3.【掌握】Containerd 镜像管理

## 学习目标

- 掌握 ctr 命令的基本用法
- 掌握 ctr image 的常见用法

---

## 1 帮助手册

不同环境下 Docker、Containerd 及 Kubernetes 管理镜像的命令工具解析：

- Docker 使用

```
docker images
```

命令管理镜像。

- 在单机环境下，Containerd 使用

```
ctr images
```

命令管理镜像，其中 ctr 是 Containerd 本身自带的命令行接口（CLI）工具。

- 在 Kubernetes（K8s）集群中，若使用 Containerd 作为容器运行时，可使用

```
crictl images
```

命令管理镜像，crictl 是 Kubernetes 社区开发的用于与容器运行时交互的专用命令行接口（CLI）工具。

### 1 ctr

```
# 获取命令帮助
ctr --help
ctr
```

![[附件/8bf8ec36fc.png]]

### 2 ctr images

```
# 获取命令帮助
ctr images
ctr i
```

![[附件/885316d875.png]]

## 2 镜像相关操作

在执行命令之前，我们先把虚拟机打一个快照，保存一下。

【打开 VMware】→【虚拟机】→【快照】→【拍摄快照】

### 1 查看镜像

```
ctr images ls
ctr i ls
```

![[附件/d162d4690a.png]]

![[附件/5a581486e3.png]]

### 2 拉取镜像

containerd 支持 OCI 标准的镜像，所以可以直接使用 Docker 官方或 Dockerfile 构建的镜像。

由于直接访问 Docker 本身的镜像网络受阻，我们从国内的阿里云镜像进行访问。操作步骤为：

1、通过账号，或者 APP 扫码的方式，登录阿里云官网；  
2、找到【容器镜像服务】菜单；  
3、点击【制品中心】，搜索相应的软件镜像；  
4、复制镜像的仓库地址；

![[附件/5afa471ea8.png]]

![[附件/69f8de4c22.png]]

```
# 从龙蜥社区进行下载安装
ctr images pull --all-platforms registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
```

![[附件/1d9254861c.png]]

### 3 镜像挂载

```
# 把已下载的容器镜像挂载至当前文件系统
ctr images mount registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 /mnt

# 查看挂载的内容
ls /mnt
```

![[附件/71f0f569ef.png]]

具体文件夹信息

![[附件/bdfa6e03c3.png]]

### 4 镜像卸载

```
# 卸载，注意，需要离开 /mnt 目录进行操作
ctr images unmount /mnt
```

![[附件/5011fe61b9.png]]

### 5 镜像导出

```
# 回到家目录
cd ~

# 把容器镜像导出 --all-platforms 表示导出所有平台镜像
# 注意，如果你拉取的时候没有加 --all-platforms 参数，那么导出的时候也不要加
ctr images export --all-platforms nginx.img registry.openanolis.cn/openanolis/nginx:1.14.1-8.6

# 查看镜像
ll -hrt

复习一下，ll 命令里的参数
● h 表示 human，用人能看懂的方式展示文件大小
● r 表示 reverse 逆序（倒序）
● t 表示 time（时间）
👉 合起来：按时间倒序排列，最近修改的文件会显示在最下方
```

![[附件/849ea837b3.png]]

### 6 镜像删除

```
# 删除指定容器镜像
ctr images rm registry.openanolis.cn/openanolis/nginx:1.14.1-8.6

# 再次查看容器镜像
ctr images ls
```

![[附件/c665ecb650.png]]![[附件/ec595e013e.png]]

### 7 镜像导入

```
# 导入容器镜像
ctr images import nginx.img
```

![[附件/7349b1fedc.png]]

### 8 修改镜像标签（常用）

```
# 把 registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
# 修改为 nginx:1.14.1-8.6
ctr images tag registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 nginx:1.14.1-8.6
```

![[附件/a2b2d64c39.png]]

```
# 修改后对容器镜像做检查比对
ctr image check
```

![[附件/be26aa338d.png]]

## 总结

1、ctr image / images 有区别吗？

- **没有本质区别**
- image 和 images 都可以使用，属于**同一命令的不同写法（别名）**  
    👉 实际使用中更推荐使用 **images（更规范、官方文档常用）**

---

2、熟悉以下命令的含义：

```
# 查看镜像
ctr images ls        # 列出本地镜像

# 拉取 / 推送镜像
ctr images pull      # 拉取镜像
ctr images push      # 推送镜像

# 镜像挂载 / 卸载
ctr images mount     # 挂载镜像到本地目录
ctr images unmount   # 卸载挂载点

# 镜像导出 / 导入
ctr images export    # 导出镜像为文件
ctr images import    # 从文件导入镜像

# 删除镜像
ctr images rm        # 删除镜像
#（remove / delete / del / rm 都是类似含义，常用 rm）

# 修改标签
ctr images tag       # 给镜像打新标签
```

👉 核心理解一句话：

- **images = 管镜像（查 / 拉 / 推 / 删 / 导入导出 / 打标签）**

**3大 镜像 容器 仓库**

# 4.【掌握】Containerd 容器管理

**学习目标**

- **掌握 ctr container / c、ctr task 的常见用法**
- **了解 ctr run 的用法**

---

## 1 帮助手册

前言

- **镜像（Image）**：镜像是一个只读的模板，它包含了运行应用程序所需的所有文件、依赖项、环境变量和配置信息等，**类似于软件安装包。**
- **容器（Container）**：**容器是镜像的运行时实例**。当使用镜像创建一个容器时，会在镜像的基础上添加一个可写层，用于存储容器运行过程中产生的数据和状态。只有当任务启动后，才会开始占用系统资源。

- 实例 绑定服务 端口号区分

- **任务（Task）**：任务是容器内具体的执行单元，它代表了**容器内正在运行的进程。**

```
# 获取帮助（两个命令等价）
ctr --help
ctr
```

## 2 ctr container

容器是一种轻量级的虚拟化技术。它将应用程序及其依赖项打包在一个独立的环境中，提供了隔离的运行空间。

```

NAME:
   ctr containers - Manage containers

USAGE:
   ctr containers [command options]

COMMANDS:
   create                   Create container
   delete, del, remove, rm  Delete one or more existing containers
   info                     Get info about a container
   list, ls                 List containers
   label                    Set and clear labels for a container
   checkpoint               Checkpoint a container
   restore                  Restore a container from checkpoint
   help, h                  Shows a list of commands or help for one command

OPTIONS:
   --help, -h  Show help (default: false)
```

### 1 查看容器

container 表示静态容器

- 可以用 c 缩写代表 container
- 可以用 ls 缩写代表 list

```
# 注意，以下几个命令是等价的
ctr container list
ctr containers list
ctr container ls
ctr containers ls
ctr c list
ctr c ls
```

![[附件/716a74eee6.png]]

### 2 创建容器

【操作类似安装软件】

```
# ctr c create 镜像名 容器ID
ctr c create registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 nginx1

# 查看容器
ctr c ls
```

![[附件/7d9bccc073.png]]

使用 ctr container create 命令创建容器后，容器并没有处于运行状态，其只是一个静态的容器。

【说明】  
这个 container 对象只是包含了运行一个容器所需的资源及配置的数据结构，例如：

- namespaces
- rootfs
- 容器的配置

都已经初始化成功了，只是用户进程（本案例为 nginx）还没有启动。需要使用 `ctr tasks` 命令才能获取一个动态容器。

我们在计算机中，线程的创建和运行也是类似的两个阶段。

### 3 查看容器详细信息

```
# 查看容器详细信息
ctr c info nginx1
```

### 4 删除容器

```
# 删除容器
ctr container rm 容器ID
```

![[附件/97b4ab869a.png]]

## 2 ctr task

```
ctr tasks --help
```

![[附件/3652107dfd.png]]

### 1.查看任务

```
# 查看容器所在宿主机进程，是以宿主机进程的方式存在的
# 可以用 t 缩写代表 task

ctr task ls
ctr t ls

[root@node001 ~]# ctr t ls
TASK    PID    STATUS
```

### 2.启动任务（重要）

```
# 启动任务（重要）

# 启动容器，-d 表示 daemon（守护进程，后台运行）
# 注意，如果不加 -d，会卡住终端
ctr t start -d nginx1

# 查看容器的进程（都是物理机的进程）
ctr t ps nginx1

# 物理机查看对应进程
ps -ef | grep 3395
```

![[附件/13953fda75.png]]

```
说明：为什么会看到两个？
 涉及到父子进程的概念

 第一列：表示进程用户（如 root）
 第二列：表示进程号（PID，Process ID）
 第三列：表示父进程号（PPID，Parent Process ID），例如 2381 是由 2362 创建的
 第四列：表示 CPU 使用率
```

### 3.停止任务

```
# 使用 k 命令停止容器中运行的进程，即停止容器
ctr tasks kill nginx1

# 查看容器停止后状态（STATUS 为 STOPPED）
ctr tasks ls
```

![[附件/d692cdaccd.png]]

### 4 删除任务

```
# 删除任务
ctr t rm nginxl
ctr t del nginxl
```

![[附件/39ebfe4f69.png]]

### 5 暂停容器

```
# 暂停容器
ctr tasks pause nginx1
```

### 6 恢复容器

```
# 使用 resume 命令恢复容器
ctr tasks resume nginx1

# 再次查看容器状态，看到其状态为 RUNNING，表示已恢复
ctr tasks ls
```

![[附件/a519104820.png]]

### 7 进入容器（重要）

```
# 为 exec 进程设定一个 id，可以随意输入，只要保证唯一即可，也可使用 $RANDOM 变量
# -t 是 --tty 的简写，其作用是为执行的命令分配一个伪终端（TTY）
ctr t exec --exec-id 1 -t nginxl /bin/sh
```

```
# 进入 sh 之后，执行 ip a 操作
sh-4.4# ip a    # 查看网卡信息

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
    valid_lft forever preferred_lft forever

# 继续执行 curl 127.0.0.1 操作，访问本地提供的 web 服务
sh-4.4# curl 127.0.0.1
```

  
  

## 4 ctr run

运行一个动态容器

```
# -d 代表 daemon，后台运行
# --net-host 代表容器的 IP 就是宿主机的 IP（相当于 docker 里的 host 类型网络）
# 镜像必须已经拉取下来了
# --net-host 是一个完整的参数
ctr run -d --net-host registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 nginx_3
```

```
# 进入到容器中
ctr t exec --exec-id 10 -t nginx_3 /bin/bash

# 为容器中运行的网站添加网站文件
echo "Hello Nginx" > /usr/share/nginx/html/index.html
exit

# 在宿主机上访问网站（改成自己的虚拟机 IP）
curl 192.168.88.128
```

### 总结

1、ctr container 和 ctr task 搭配，可以创建容器，并启动一个任务  
2、ctr run 一步到位，从镜像直接拉起容器和任务  
3、如果进入容器？

```
ctr t exec --exec-id ID号 -t 容器名 /bin/bash
# 或
ctr t exec --exec-id ID号 -t 容器名 /bin/sh
```

## 5.【掌握】Containerd 命名空间管理

**学习目标**  
掌握 ctr namespace 命令的相关用法

### 1.帮助手册

Containerd 中 namespace 的作用为：隔离运行的容器，可以实现运行多个容器。

```
# 查看命令帮助
ctr namespaces --help

NAME:
ctr namespaces - manage namespaces

USAGE:
ctr namespaces command [command options] [arguments...]

COMMANDS:
create, c   create a new namespace
list, ls    list namespaces
remove, rm  remove one or more namespaces
label       set and clear labels for a namespace

OPTIONS:
--help, -h  show help
```

![[附件/5e2129be37.png]]

### 2 ctr namespace

#### 1 查看命名空间

```
# 列出已有 namespace
ctr namespaces ls
ctr namespace ls
ctr ns ls
```

![[附件/636791eaf1.png]]

#### 2 创建命名空间

```
# 创建命名空间
ctr namespace create itheima
# 或者
ctr ns create itheima
```

![[附件/03377bf65a.png]]

#### 3 删除命名空间

```
# 删除命名空间
ctr ns rm itheima
```

![[附件/17ba0b0cde.png]]

#### 4 查看命名空间中的进程

```
ctr -n itheima tasks ls
```

![[附件/5988754fe4.png]]

没有-n是默认空间的镜像

#### 5 在指定命名空间中下载容器镜像

```
ctr -n itheima i pull registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
```

![[附件/bd2546b26d.png]]

## 6.【扩展】Containerd 使用 Harbor 镜像仓库

**学习目标**

- 熟悉 ctr 命令推、拉镜像到私有仓库 Harbor 的相关操作

### 1 Harbor 准备

Harbor 分为离线包和在线包两种。在线包较小，但需要联网下载。我这里使用离线包下载地址：  
[https://github.com/goharbor/harbor/releases](https://github.com/goharbor/harbor/releases)

我这里提供了 harbor-offline-installer-v2.12.2.tgz，拷贝到 Harbor 服务器上，准备一台机器，专门用来安装 Harbor 仓库。

```
# 安装 Docker
wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo
dnf install docker-ce -y

# 启动 Docker
systemctl start docker

# 设置开机自启（防止重启后 Harbor 无法自动拉起）
systemctl enable docker

# 检查服务状态（确认状态为 Active: active (running)）
systemctl status docker

# 解压 Harbor
tar xf harbor-offline-installer-v2.15.0.tgz -C /usr/local/
cd /usr/local/harbor/

# 修改配置文件
cp harbor.yml.tmpl harbor.yml
vim harbor.yml

# 修改 hostname 为 harbor 服务器主机名称
hostname: harbor.itcast.cn

# http 相关配置
http:
  port: 80

# 关闭 https（注释相关配置）
# https:
#   port: 443
# certificate: /your/certificate/path
# private_key: /your/private/key/path

# 修改 admin 密码
harbor_admin_password: 123

# 安装 Harbor
./install.sh

# 安装完成提示
# ----Harbor has been installed and started successfully.---
# Now you should be able to visit the admin portal at http://192.168.88.20
# For more details, please visit https://github.com/goharbor/harbor
```

![[附件/2a59d7b84e.png]]

usr： unix system resource 系统资源

### 2 配置 Containerd

#### 1 Harbor 主机名解析

在安装 containerd 的主机上，添加此配置信息。

```
# 编辑 hosts 文件
vim /etc/hosts

# 查看 hosts 文件
cat /etc/hosts

127.0.0.1   localhost
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

# 添加以下映射（IP 改成自己的 Harbor 主机 IP，域名自定义）
192.168.88.128   itheima.harbor.com
```

![[附件/26833ffa8b.png]]

**说明**  
192.168.10.165 是 Harbor 的 IP，需修改为自己的 IP 地址  
harbor.itheima.com 是这里设置的域名，也可以改成自己设定的

#### 2 修改 Containerd 配置

1 添加config.toml中的[plugins:cri.registry]选项

```
# 生成配置文件
containerd config default > /etc/containerd/config.toml

# 修改配置文件
vim /etc/containerd/config.toml

# 修改 config_path
sed -i 's/config_path = ""/config_path = "\/etc\/containerd\/certs.d\/"/g' /etc/containerd/config.toml

# 最终效果
[plugins.cri.registry]
config_path = "/etc/containerd/certs.d"
```

2 在/etc/containerd/目录下，创建一个cerst.d目录

```
cd /etc/containerd

# 域名改成自己配置的
mkdir -p certs.d/itheima.harbor.com

touch /etc/containerd/certs.d/itheima.harbor.com/hosts.toml
```

![[附件/d3710ac070.png]]

3 执行以下命令

```
# 编辑 hosts.toml
vi /etc/containerd/certs.d/harbor.yeyunby.com/hosts.toml

# 粘贴以下内容（域名改成自己配置的）
server = "http:///harbor.yeyunby.com"

[host."http:///harbor.yeyunby.com"]
capabilities = ["pull", "resolve"]
```

![[附件/31205e3bfa.png]]

4 重启 containerd，以便重新加载配置文件

```
systemctl restart containerd
```

#### 3 ctr 上传镜像

```
# 重新生成新的 tag
ctr images tag nginx:1.14.1-8.6 harbor.itcast.cn/library/nginx:1.14.1-8.6

# 或者
ctr images tag registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 
itheima.harbor.com/library/nginx:1.14.1-8.6

# 如果之前拉取过，这两个本地应该都有
```

![[附件/9b22e1bb05.png]]

```
# 查看已生成容器镜像
ctr images ls
```

![[附件/941ba66178.png]]

```
# 推送容器镜像至 Harbor
ctr images push --platform linux/amd64 --plain-http -u admin:Harbor12345 itheima.harbor.com/library/nginx:1.14.1-8.6
```

![[附件/13def1fb82.png]]

**说明**  
1、推镜像的时候，要先 tag 再 push  
2、因为 Harbor 是 http 协议，不是 https 协议，所以一定要加上 `--plain-http`  
3、`-u admin:Harbor12345` 是指定 Harbor 的用户名与密码，密码改成自己的

#### 4 ctr 下载镜像

```
# 先把本地的删掉一下
ctr i rm itheima.harbor.com/library/nginx:1.14.1-8.6

# 查看已下载容器镜像
ctr images ls

# 下载容器镜像，pull 表示拉取
# --plain-http 指的是通过 http 协议，即不走 443 端口，而是走 80 端口
ctr images pull --plain-http itheima.harbor.com/library/nginx:1.14.1-8.6
```

![[附件/4cb3960917.png]]

### 总结

1、我们 Harbor 用的是 80 端口的 HTTP 协议，所以 pull 和 push 的时候，必须带上 `--plain-http` 参数2、Containerd 1.7.25 中，使用了 config_path 字段，表示从指定目录下加载配置文件  
3、说出下面命令的含义：

- ctr i pull：拉取镜像
- ctr i push：推送镜像

4、推镜像的时候，要先 tag，再 push

## 7.【了解】Docker 集成 Containerd 实现容器管理

**学习目标**  
熟悉 Docker 集成 Containerd 实现容器管理的方式

### 1 原理

当你使用 Docker 命令创建、启动、停止或删除容器时：

- Docker 客户端会将这些请求发送给 Docker 守护进程（dockerd）
- Docker 守护进程会调用 Containerd 的 API 来完成实际的容器操作，如创建容器的命名空间、挂载文件系统等
- Containerd 则会进一步调用 runc 来创建和管理容器的 Linux 内核级资源

### 2 配置

目前 Containerd 主要任务还在于解决容器运行时的问题，对于其周边生态还不完善。所以可以借助 Docker 结合 Containerd 来实现 Docker 完整的功能应用。

```
# 首先确认 docker-ce 是否安装
dnf list installed | grep docker
```

![[附件/ec192f0975.png]]

```
# 如果安装过了，下面的这两个操作就跳过

# 1 下载并配置阿里云的 Docker CE YUM 源
wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 2 安装 Docker CE
dnf -y install docker-ce
```

配置文件修改

```
# 修改 Docker 服务文件，以便使用已安装的 containerd
vim /etc/systemd/system/multi-user.target.wants/docker.service

# 修改前
[Service]
Type=notify

# the default is not to use systemd for cgroups because the delegate issues still exists
# and systemd currently does not support the cgroup feature set required for containers run by docker
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
ExecReload=/bin/kill -s HUP $MAINPID
TimeoutStartSec=0
RestartSec=2
Restart=always

# 修改后
[Service]
Type=notify

# the default is not to use systemd for cgroups because the delegate issues still exists
# and systemd currently does not support the cgroup feature set required for containers run by docker
ExecStart=/usr/bin/dockerd --containerd /run/containerd/containerd.sock --debug
ExecReload=/bin/kill -s HUP $MAINPID
TimeoutSec=0
RestartSec=2
Restart=always
```

![[附件/b54ea76c92.png]]

```
# 重新加载配置并启动 Docker
systemctl daemon-reload

systemctl enable docker
systemctl start docker
```

```
# 查看其启动后进程
ps -ef | grep docker
```

![[附件/ed034965a0.png]]

### 3 验证测试

```
# 使用 docker 运行容器
docker run -d registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
```

![[附件/93747855c4.png]]

```
# 使用 docker ps 命令查看正在运行的容器
docker ps
```

![[附件/c3c1919516.png]]

```
# 使用 ctr 查看是否添加一个新的 namespace
ctr namespace ls
```

```
NAME        LABELS
default
k8s.io
itheima
moby
```

![[附件/5ab97139db.png]]

```
# 查看 moby 命名空间，发现使用 docker run 运行的容器包含在其中
ctr -n moby container ls
```

![[附件/167c34f34a.png]]

```
# 使用 ctr 查看正在运行的容器，说明 docker run 的容器由 containerd 管理
ctr -n moby tasks ls
```

![[附件/f2c3524254.png]]

```
# 使用 docker stop 停止容器，并使用 docker rm 删除容器
docker stop 076b76b3f9d49485147b90b6d6bcb8e34aa63e3cd59bb7addcf2ab411dacd35d
docker rm 076b76b3f9d49485147b90b6d6bcb8e34aa63e3cd59bb7addcf2ab411dacd35d
```

![[附件/6ce90536af.png]]

```
ctr -n moby container ls
ctr -n moby tasks ls
```

![[附件/0a8627c22a.png]]

## 8【课下作业】二进制安装

Containerd 有两种安装包：  
第一种是 containerd-xxx，这种包用于单机测试没问题，不包含 runc，需要提前安装。  
第二种是 cri-containerd-cni-xxx，包含 runc 和 k8s 里需要的相关文件。k8s 集群里需要用到此包。虽然包含 runc，但是依赖系统中的 seccomp（安全计算模式，是一种限制容器调用系统资源的模式）。

#### 手动组合（最推荐，版本最可控）

虽然没有了“全家桶”包，但你可以通过下载以下三个核心组件来手动构建：

1. **Containerd 核心版** [containerd-2.2.2-linux-amd64.tar.gz](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/containerd/containerd/releases/download/v2.2.2/containerd-2.2.2-linux-amd64.tar.gz)
2. **Runc**: 从 [opencontainers/runc](https://github.com/opencontainers/runc/releases) 下载二进制文件。
3. **CNI Plugins**: 从 [containernetworking/plugins](https://github.com/containernetworking/plugins/releases) 下载插件包。

4. [GitHub - containernetworking/cni: Container Network Interface - networking for Linux containers](https://github.com/containernetworking/cni)

### **1 安装 containerd**

#### 1.获取安装包

```
# 获取安装包
https://github.com/containerd/containerd/releases
```

![[附件/cc3252aa60.png]]

1 搜索containerd

2 点进release

![[附件/b3e762f944.png]]

3 找到1.7.25版本

![[附件/10337480f6.png]]

4 找到Assets，展开

5 找到指定的资源版本，右键复制资源链接。那个带sha256sum的是它对应的哈希值，用作验签的。

![[附件/2df45c9566.png]]

![[附件/3586938108.png]]

[https://github.com/containerd/containerd/releases/download/v2.2.2/containerd-2.2.2-linux-amd64.tar.gz](https://github.com/containerd/containerd/releases/download/v2.2.2/containerd-2.2.2-linux-amd64.tar.gz)

6 使用wget，在Linux虚拟机中的家目录，下载

```
# 回到家目录，下载 Containerd 安装包（网速慢可使用课件提供的包）
cd ~

wget https://github.com/containerd/containerd/releases/download/v1.7.25/cri-containerd-1.7.25-linux-amd64.tar.gz
```

#### 2 安装containerd

```
# 创建目录
mkdir cri-containerd-1.7.25

# 解压软件包（-C 指定目录）
tar -C ./cri-containerd-1.7.25 -zxf cri-containerd-1.7.25-linux-amd64.tar.gz
```

![[附件/df2a35bddf.png]]

```
cd ./cri-containerd-1.7.25
ll -R  【递归展示】

# etc 目录主要是一些服务管理配置文件
# opt（Optional software，额外的软件）目录包含 gce 配置和 cni 网卡配置
# usr（Unix System Resources，Unix 系统资源）目录包含 containerd 运行时文件，包含 runc
```

![[附件/e214876631.png]]

![[附件/9ed2ec4421.png]]

![[附件/0f0ce31604.png]]

```
# 安装 tree 命令
dnf install -y tree
```

#### 3 复制containerd运行时文件

```
# 查看宿主机 /usr/local/bin 目录，里面没有任何内容
ls /usr/local/bin/
```

![[附件/0ecccc7f0a.png]]

```
# 查看解压后 usr/local/bin 目录，里面包含 containerd 运行时文件
ls /root/cri-containerd-1.7.25/usr/local/bin
```

![[附件/6d96aef343.png]]

```
# 复制 containerd 文件至 /usr/local/bin 目录（可复制全部或仅 containerd）
cp /root/cri-containerd-1.7.25/usr/local/bin/* /usr/local/bin/

# 查看目录
ls /usr/local/bin/
```

![[附件/7aef22b9e9.png]]

#### 4 添加containerd.service文件至系统

查看containerd.service安装位置

```
# 查看 containerd.service 文件，了解 containerd 文件安装位置
cat /root/cri-containerd-1.7.25/etc/systemd/system/containerd.service
```

```
# 复制 containerd 服务管理配置文件至 /usr/lib/systemd/system/ 目录中
cp /root/cri-containerd-1.7.25/etc/systemd/system/containerd.service /usr/lib/systemd/system/containerd.service

# 查看复制后结果
ls /usr/lib/systemd/system/containerd.service
```

![[附件/6b9a8e5ab3.png]]

```
# 查看帮助
containerd --help
```

![[附件/637054df2c.png]]

#### 5 生成 containerd 模块配置文件

1 **生成默认模块配置文件**

Containerd 的默认配置文件为 /etc/containerd/config.toml，可以使用 containerd config default > /etc/containerd/config.toml 命令创建一份模块配置文件。

```
# 创建配置文件目录
mkdir /etc/containerd

# 生成配置文件
containerd config default > /etc/containerd/config.toml

# 查看配置文件
cat /etc/containerd/config.toml
```

2 替换默认配置文件（可选）

```
vim /etc/containerd/config.toml
```

```
# 把下面内容粘贴进去

root = "/var/lib/containerd"
state = "/run/containerd"
oom_score = -999

[grpc]
  address = "/run/containerd/containerd.sock"
  uid = 0
  gid = 0
  max_recv_message_size = 16777216
  max_send_message_size = 16777216

[debug]
  address = ""
  uid = 0
  gid = 0
  level = ""

[metrics]
  address = ""
  grpc_histogram = false

[cgroup]
  path = ""

[plugins]
  [plugins.cgroups]
    no_prometheus = false

  [plugins.cri]
    stream_server_address = "127.0.0.1"
    stream_server_port = "0"
    enable_selinux = false
    sandbox_image = "easzlab/pause-amd64:3.2"
    stats_collect_period = 10
    systemd_cgroup = false
    enable_tls_streaming = false
    max_container_log_line_size = 16384

  [plugins.cri.containerd]
    snapshotter = "overlayfs"
    no_pivot = false

  [plugins.cri.containerd.untrusted_workload_runtime]
    runtime_type = ""
    runtime_engine = ""
    runtime_root = ""

  [plugins.cri.cni]
    bin_dir = "/opt/kube/bin"
    conf_dir = "/etc/cni/net.d"
    conf_template = "/etc/cni/net.d/10-default.conf"

  [plugins.cri.x509_key_pair_streaming]
    tls_cert_file = ""
    tls_key_file = ""

[plugins.diff-service]
  default = ["walking"]

[plugins.linux]
  shim = "containerd-shim"
  runtime = "runc"
  runtime_root = ""
  no_shim = false
  shim_debug = false

[plugins.opt]
  path = "/opt/containerd"

[plugins.restart]
  interval = "10s"

[plugins.scheduler]
  pause_threshold = 0.02
  deletion_threshold = 0
  mutation_threshold = 100
  schedule_delay = "0s"
  startup_delay = "100ms"
```

#### 6 启动 containerd 服务

```
# 设置开机自启动
systemctl enable containerd

# 启动服务
systemctl start containerd

# 查看服务状态
systemctl status containerd
```

#### 7 验证可用性

```
# 验证 containerd 可用性
ctr version
```

![[附件/bd9701bcff.png]]

图上的信息，是提示有些属性，将会在后续版本中不建议使用并最终移除。

Deprecated 是开发和运维中常遇到的一个词语，中文意思是：不赞成的、废弃的。

软件版本不断迭代优化，有些功能或语法将会在新版本中舍弃，为此，软件开发者会通知使用人员，用 Deprecated 标注的地方，表示：  
1、这些语法或功能还能用  
2、但不建议再使用了  
3、在指定的后续版本中将会被 removed，到时候软件如果报错，需要提前适配

![[附件/3e14567843.png]]

### 2 安装 runc

由于二进制包中提供的 runc 默认需要系统中安装 seccomp（Security Compute，安全计算）支持，若系统未安装则需要单独安装，且不同版本 runc 对 seccomp 版本要求不一致，所以建议单独下载 runc 二进制包进行安装，其内置了对 seccomp 的支持。

#### 1 获取 runc

![[附件/99c731297c.png]]

```
# 下载 runc 二进制包
wget https://github.com/opencontainers/runc/releases/download/v1.1.12/runc.amd64
```

这里可以发现，runc，就是run containers的缩写，中文意思是，运行容器。对应上了我们之前在【前言】部分介绍的内容。

![[附件/bf03df485c.png]]

[https://github.com/opencontainers/runc/releases/download/v1.3.5/runc.amd64](https://github.com/opencontainers/runc/releases/download/v1.3.5/runc.amd64)

#回到家目录cd

#使用wget下载

#### 2 安装runC

```
# 查看已下载文件
ls run*
```

![[附件/043612f97d.png]]

```
# 安装 runc
mv runc.amd64 /usr/sbin/runc

# 为 runc 添加可执行权限
chmod +x /usr/sbin/runc


# -rW-r--r-- 644
# drwxr-xr-X 755
```

#### 3 验证可用性

```
# 使用 runc 命令验证是否安装成功
runc -V
```

![[附件/e88d411d70.png]]

### 总结

1、从 github 上获取 Containerd 软件包的时候，流程是什么？  
1、搜索相应软件  
2、点击 Releases 模块  
3、找到指定的版本  
4、展开 Assets 模块  
5、右键点击指定的版本，复制链接  
6、执行 wget 命令，下载链接文件

2、containerd 包含三个目录，分别是 etc、opt、usr

3、对于像 ctr 这种新的命令，如何查看帮助手册？  
执行 `ctr --help`