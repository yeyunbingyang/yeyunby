# 1.【了解】应用部署方式演变

**学习目标**  
基础目标：了解应用部署从传统物理机到现代容器化的主要阶段。  
进阶目标：能对比各阶段部署方式的特点。

## 1 传统应用部署方式

传统企业早期采用物理机部署业务系统，面临硬件成本高、部署周期长的问题。

优点：简单  
缺点：不能为应用程序定义资源使用边界，程序之间容易互相影响

## 2 虚拟化部署方式

可以在一台物理机上运行多个虚拟机，每个虚拟机都是独立的一个环境。

优点：程序环境不会相互产生影响，提供了一定程度的安全性  
缺点：增加了操作系统，浪费了部分资源

## 3 容器化部署方式

与虚拟化类似，但是共享了操作系统。

优点：  
可以保证每个容器拥有自己的文件系统、CPU、内存、进程空间等运行应用程序所需要的资源都被容器包装，并和底层基础架构解耦  
容器化的应用程序可以跨云服务商、跨 Linux 操作系统发行版进行部署

![[536080414f.png]]

容器化部署方式给带来很多的便利，但是也会出现一些问题，比如说：

- 一个容器故障停机了，怎么样让另外一个容器立刻启动去替补停机的容器
- 当并发访问量变大的时候，怎么横向扩展容器数量

这些容器管理的问题统称为容器编排问题，为了解决这些容器编排问题，就产生了一些容器编排的软件：

- Swarm：Docker 自己的容器编排
- Mesos：Apache 的一个资源统一管控的工具，需要和 Marathon 结合使用
- Kubernetes：Google 开源的容器编排工具

![[463477dda5.png]]

总结

1、回顾软件应用程序部署方式的演变，可以发现容器化发展的必然性;

2、学习和掌握Kubernetes，有助于适应当前容器市场的技术发展;

# 2.【了解】 认识kunbernetes

## 学习目标

**基础目标**

- 了解 Kubernetes 的介绍和主要功能。
- 牢记 Master 节点和 Node 节点各组件的名称。
- 知晓 Kubernetes 常见的集群部署方式。

**进阶目标**

- 理解 Kubernetes 产生的行业背景和解决的核心问题。
- 深入理解各组件的功能及它们之间的交互流程，能画出架构示意图。
- 对比不同部署方式的优缺点和适用场景。

## 1 什么是 Kubernetes

![[5dd99c1c51.png]]

希腊语：舵手、飞行员

官方网址 [https://kubernetes.io/](https://kubernetes.io/)

Kubernetes 源自 [Google 15 年生产环境的运维经验](http://queue.acm.org/detail.cfm?id=2898444)，同时凝聚了社区的最佳创意和实践。

中文社区：[http://docs.kubernetes.org.cn](http://docs.kubernetes.org.cn/232.html)

## 2 Kubernetes 优势

Kubernetes 的本质是一组服务器集群，它可以在集群的每个节点上运行特定的程序，来对节点中的容器进行管理，从而实现自动化。主要提供了如下功能：

- **自我修复**：一旦某一个容器崩溃，能够在 1 秒钟左右迅速启动新的容器。
- **弹性伸缩**：可以根据需要，自动对集群中正在运行的容器数量进行调整。
- **服务发现**：服务可以通过自动发现的形式找到它所依赖的服务。
- **负载均衡**：如果一个服务启动了多个容器，能够自动实现请求的负载均衡。
- **版本回退**：如果发现新发布的程序版本有问题，可以立即回退到原来的版本。
- **存储编排**：可以根据容器的需求自动挂载和管理存储资源。
- **存储卷**：提供持久化存储能力，使容器数据不会随容器销毁而丢失。

![[edea1bf247.png]]

## 总结

Kubernetes能够实现自我 弹性 负载 版本

## 3 Kubernetes架构⭐⭐⭐

kubernetes是具有中心节点的架构，也就是说有master管理节点。

一个kubernetes集群主要是由控制节点(master)、工作节点(node)组成。

每个节点上都会安装不同的组件。

### 1 节点组件介绍

**节点类型 / 组件 / 说明**

**Master 节点**

- **API Server**  
    作为集群的统一入口，处理 API 请求，提供认证、授权、API 注册和发现等机制。
- **Controller Manager**  
    控制器管理者，负责维护集群的状态，比如程序部署安排、故障检测、自动扩展、滚动更新等。
- **Scheduler**  
    负责集群资源调度，按照预定的调度策略将 Pod 调度到相应的 Node 节点上。
- **etcd**  
    负责存储集群中各种资源对象的信息。

- 数据存储作用：存储集群的关键配置和状态信息。
- 原理：分布式键值存储。

**Worker 节点**

- **kubelet**  
    管理功能：负责维护**容器**的生命周期，通过控制 Docker 等运行时来创建、更新、销毁容器。
- **kube-proxy**  
    代理功能：负责提供集群内部的服务发现和负载均衡。
- **Container Runtime**  
    运行容器的底层引擎，如 Docker、Containerd（>=1.24）。

核心术语 (Control Plane)

**API**

**Application Programming Interface**

**翻译：** 应用程序编程接口。它是集群的“唯一合法入口”。所有 `kubectl`

命令本质上都是在给它发 HTTP 请求。

**Controller**

**Control** (控制)

**翻译：** 控制器。源自自动化控制理论中的“反馈环”。它不停地在做：检查实际状态 $\rightarrow$ 对比期望状态 $\rightarrow$ 执行修复。

**Scheduler**

**Schedule** (调度/计划)

**翻译：** 调度器。决定“谁去哪”。它像一个排班员，根据 Node 的内存、CPU 剩余情况，给 Pod 分配宿舍。

**etcd**

**etc** (配置) + **d** (distributed)

**翻译：** 分布式配置库。在 Linux 中 `/etc`

是放配置的地方，加上 `d`

表示它是跨机器同步的“真理仓库”。

**kubelet**

**kube** + **-let** (微小后缀)

**翻译：** K8s 小管家。后缀 `-let`

常见于 `booklet`

(小册子)。它是驻扎在每个节点上的代理，只负责盯着本机的容器干活。

**Proxy**

**Proxy** (代理/中介)

**翻译：** 网络代理。它不处理业务，只负责“导流”。比如把发往 Service 的流量转发到具体的 Pod IP 上。

**Runtime**

**Run** + **Time** (运行时间/环境)

**翻译：** 运行时。指程序运行所需的软件环境。Containerd 就是一种运行时，负责把镜像文件“跑”起来。

**Pod**

**Pod** (豆荚/小群体)

**翻译：** 豆荚。K8s 的最小单位。一个豆荚里可以有多个豆子（容器），它们共享网络和存储。

### 2 组件间调用关系

![[9191037c65.png]]

**Kubernetes 组件调用关系（以部署 Nginx 为例）**

1. Kubernetes 集群启动之后，Master 和 Node 都会将自身的信息存储到 etcd 数据库中。
2. 一个 Nginx 服务的【安装】请求，会首先被发送到 Master 节点的 API Server 组件。
3. API Server 组件会调用 Scheduler 组件，决定将服务安装到哪个 Node 节点上。
4. API Server 调用 **Controller Manager**，对 Node 节点进行调度并下发安装 Nginx 服务的任务。
5. kubelet 接收到指令后，会通知 Docker（或 Container Runtime），由其启动一个 Nginx 的 Pod。  
    Pod 是 Kubernetes 的最小操作单元，容器必须运行在 Pod 中

6. 如果需要外部访问 Nginx，就需要通过 kube-proxy 对 Pod 提供访问代理，从而实现服务访问。这样，外界用户就可以访问集群中的 Nginx 服务了。

### 3 Add-ons（附件）介绍

除了上面介绍的组件，Kubernetes 集群中还有各类附加组件（Add-ons）。这些组件并非集群运行的必需部分，但可以与主体程序很好地结合使用。

**常见 Add-ons 举例：**

- **coredns / kube-dns**  
    负责为整个集群提供 DNS 服务。
- **Ingress Controller**  
    为服务提供集群外部访问（如：[www.itheima.com](http://www.itheima.com/) → Pod → 容器）。
- **Heapster / Metrics Server**  
    提供集群资源监控（容器监控也可以使用 Prometheus）。
- **Dashboard**  
    可视化管理，通过 Web 界面管理集群。
- **Federation**  
    提供跨可用区的集群管理能力。
- **Fluentd + Elasticsearch**  
    提供集群日志的采集、存储与查询能力。
- **Prometheus 和 Grafana**  
    Prometheus：开源的系统监控和告警工具。  
    Grafana：开源的可视化工具，可与 Prometheus 集成。
- **ELK Stack（Elasticsearch、Logstash、Kibana）**

- Elasticsearch：用于存储大量日志和监控数据。
- Logstash：收集各个 Pod 的日志和监控数据。
- Kibana：用于在 Elasticsearch 中查询和展示数据。

### 总结

1. Kubernetes 由 **Master** 节点组件和 **Worker** 节点组件组成；kubelet 属于 **Worker** 节点组件。
2. kube-proxy 属于 **Worker** 节点上的组件。
3. Add-ons 属于**附加组件**，没有它们，并不影响集群的正常运行。

# 4 【熟悉】集群部署方式

## 学习目标

- 掌握使用 kubeadm 进行 K8s 集群部署。

## 1 常见部署方式概述

目前部署 Kubernetes 集群主要有三种方式：

### 1. Minikube

- 单机简化安装（主要用于简单测试）。

### 2. kubeadm && kubeasz

- **kubeadm**  
    Kubernetes 官方提供的快速搭建集群工具，提供 `kubeadm init` 和 `kubeadm join`，用于快速部署集群。  
    官方地址：[https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/)  
    适合生产环境，支持多主集群。
- **kubeasz**  
    基于 Ansible 开发的开源工具集，用于在国内复杂网络环境下高效部署和管理 Kubernetes 集群。  
    官方地址：[https://github.com/easzlab/kubeasz](https://github.com/easzlab/kubeasz)

![[e44bbc2c69.png]]

### 3 二进制包

从 GitHub 下载发行版的二进制包，手动部署每个组件，组成 Kubernetes 集群。

---

### 4 各部署方式优缺点对比

- **kubeadm**  
    降低部署门槛，但屏蔽了很多细节，遇到问题较难排查。
- **二进制包部署**  
    部署过程相对复杂，但可控性更强。

---

### 总结

1. **kubeadm** 和 **kubeasz[扩展]** 是常用的集群部署工具；前者由官方维护，后者在国内访问更方便。

# 5.【实践】kubeadm 部署kubernets集群

## 1.准备环境

### 1硬件资源规划

![[3682406e53.png]]

三台2核+2G内存的CentOS Stream 9，单网卡（最小环境）

|   |   |
|---|---|
|IP|角色|
|192.168.88.135|master（单管理节点）|
|192.168.88.136|node1|
|192.168.88.137|node2|

### 2 软件资源规划

1 所有节点进行主机名绑定

```
# 修改主机名的命令
hostnamectl set-hostname master

# 修改完，执行 bash 进行更新
bash
```

```
# 打开主机名文件，把 master、node1、node2 添加上
vi /etc/hosts

127.0.0.1
::1 localhost localhost.localdomain localhost4 localhost4.localdomain4 localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.88.135 master
192.168.88.136 node1
192.168.88.137 node2
```

![[2eb6cf6de7.png]]

2 所有节点关闭 selinux，关闭 firewalld，安装 iptables 服务，并保存为空规则

```
# 永久关闭 SELinux，需要编辑配置文件
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

# 停止 firewalld 服务，禁止 firewalld 服务开机自启
systemctl stop firewalld
systemctl disable firewalld

# 安装 iptables 和 iptables-services，清空 iptables 规则并保存
dnf install iptables iptables-services -y
iptables -F
iptables -X
iptables -Z
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
service iptables save

# 所有节点时间同步
dnf install chrony -y
systemctl enable chronyd --now

# 关闭交换区 防止k8s集群延迟 【需要重启】
sed -i 's/.*swap.*/#&/g' /etc/fstab

swapoff -a

# 加载 br_netfilter 和 overlay 内核模块
modprobe overlay
modprobe br_netfilter

cat <<EOF | tee /etc/sysctl.d/k8s.conf > /dev/null
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

echo "br_netfilter" | tee /etc/modules-load.d/k8s.conf

# 生效命令
sysctl --system
```

3 所有节点准备 yum 源

```
# 安装 wget vim net-tools telnet epel-release tree
dnf install -y wget vim net-tools telnet epel-release tree

# 安装 pip 和 ansible（kubeasz 使用的）
# dnf install -y python3-pip
# pip3 install ansible -i https://mirrors.aliyun.com/pypi/simple/

# 如果不是阿里源，再执行以下命令，从阿里云下载 Docker DNF 源配置文件到系统指定目录
# ce 表示 Community Edition，社区版
wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 添加 k8s 源
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes-tencent]
name=Kubernetes Tencent Mirror
baseurl=https://mirrors.cloud.tencent.com/kubernetes_new/core:/stable:/v1.30/rpm/
enabled=1
gpgcheck=0

[kubernetes-aliyun]
name=Kubernetes Aliyun Mirror
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```

## 2 安装软件

### 1 安装 Containerd

#### 1 安装 Containerd（所有节点执行）

```
# 从阿里源拉取 containerd.io
dnf install -y containerd.io
```

#### 2 配置 Containerd

```
# 生成配置文件
containerd config default > /etc/containerd/config.toml

# 修改 SystemdCgroup 参数为 true 
#表示 containerd 使用 systemd 作为 cgroup 驱动程序。
sed -ri 's#SystemdCgroup = false#SystemdCgroup = true#' /etc/containerd/config.toml

grep -n "SystemdCgroup" /etc/containerd/config.toml

# 修改 sandbox 沙箱镜像
# 修改sandbox沙箱镜像，registry.k8s.io在某些网络环境下可能访问不稳定或受到限制，
# 而阿里云的镜像仓库registry.aLiyuncs.com在国内网络环境下通常具有更好的访问速度和稳定性。
sed -ri 's#registry.k8s.io\/pause:3.8#registry.aliyuncs.com\/google_containers\/pause:3.9#' /etc/containerd/config.toml

registry.k8s.io/pause:3.10.1

sed -ri 's#registry.k8s.io\/pause:3.10.1#registry.aliyuncs.com\/google_containers\/pause:3.9#' /etc/containerd/config.toml

grep -n "registry" /etc/containerd/config.toml


# 新增镜像源配置路径
sed -i 's/config_path = ''/config_path = "\/etc\/containerd\/certs.d\/"/g' /etc/containerd/config.toml

# 只修改第 54 行
sed -i '54s@config_path = ''@config_path = "/etc/containerd/certs.d/"@' /etc/containerd/config.toml


grep "config_path" /etc/containerd/config.toml
grep -n "config_path" /etc/containerd/config.toml
```

经验总结：当配置文件里有引时号怎么办？

在 Linux 运维中处理带有引号的配置文件，有两条**金科玉律**：

1. **能用** `**vim**` **手动改，就不强行用** `**sed**`**：** 只有一两行时，`vim 54G` 进去删掉多余字符只需 3 秒。
2. **非要用** `**sed**` **时，换个包裹方式：**

- 如果你要匹配的内容里有**单引号**，`sed` 命令外面就用**双引号**包裹：`sed -i "s@...''@...@"`。
- 如果你要匹配的内容里有**双引号**，`sed` 命令外面就用**单引号**包裹：`sed -i 's@...""@...@'`。

#### 3 关联 containerd 镜像源目录

```
mkdir -p /etc/containerd/certs.d/docker.io

cat > /etc/containerd/certs.d/docker.io/hosts.toml << 'EOF'
server = "https://docker.io"

[host."https://docker.m.daocloud.io"]
capabilities = ["pull","resolve"]

[host."https://dockerproxy.com"]
capabilities = ["pull","resolve"]

[host."https://docker.mirrors.sjtug.sjtu.edu.cn"]
capabilities = ["pull","resolve"]

[host."https://docker.mirrors.ustc.edu.cn"]
capabilities = ["pull","resolve"]

[host."https://docker.nju.edu.cn"]
capabilities = ["pull","resolve"]

[host."https://registry.docker-cn.com"]
capabilities = ["pull","resolve","push"]

[host."https://cf-workers-docker-io-38g.pages.dev"]
capabilities = ["pull","resolve","push"]
EOF

# 重启生效
systemctl enable containerd
systemctl restart containerd
```

```
# 查看状态
systemctl status containerd
```

#### 4 补充一下docker源

```
# 修改 docker 源
mkdir -p /etc/docker

cat <<EOF > /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "registry-mirrors": [
    "https://cf-workers-docker-io-38g.pages.dev",
    "https://registry.docker-cn.com",
    "https://docker.m.daocloud.io",
    "https://dockerproxy.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://docker.nju.edu.cn"
  ]
}
EOF

# 重启生效
systemctl daemon-reload

# 这里暂时还没有安装 docker，如果报错，直接忽略
systemctl restart docker
```

### 2 安装 kubeadm、kubelet、kubectl（所有节点）

```
# 安装 kubeadm、kubectl 和 kubelet
dnf install -y kubelet kubeadm kubectl

dnf list installed I grep -E 'kubeadm|kubectl|kubelet'

# 设置 kubelet 开机自启
# 注意：不是 start 启动，因为最后要在 master 节点上统一初始化
# 一旦提前启动，端口占用，就可能起不来
systemctl enable kubelet
systemctl status kubelet
```

### 3 初始化 master 节点（仅在 master 执行）

```
kubeadm init \
--apiserver-advertise-address=192.168.88.135 \  # 这里的地址，改成自己 master 节点的 IP 地址
--image-repository registry.aliyuncs.com/google_containers \
--pod-network-cidr=10.244.0.0/16 \  # 这里就这么写，是对应上后面 flannel 网络插件的默认值
--control-plane-endpoint=master     # 这里的主机名，就是 master 节点的主机名


kubeadm init --apiserver-advertise-address=192.168.88.161 --image-repository registry.aliyuncs.com/google_containers --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=master
```

```
kubeadm init --apiserver-advertise-address=192.168.88.135 --image-repository registry.aliyuncs.com/google_containers --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=master
```

如果执行成功，会产生如下日志：

![[1a0b102a95.png]]

```
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of control-plane nodes by copying certificate authorities
and service account keys on each node and then running the following as root:

  kubeadm join master:6443 --token t0vhic.ok6a1fwgng9zhupj \
        --discovery-token-ca-cert-hash sha256:ae558f4b543621b8d3bd3a580d7940931942d546295c48267e514bcc1bb8d7a9 \
        --control-plane

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join master:6443 --token t0vhic.ok6a1fwgng9zhupj \
        --discovery-token-ca-cert-hash sha256:ae558f4b543621b8d3bd3a580d7940931942d546295c48267e514bcc1bb8d7a9
```

node 节点加入集群【预备】

```
# 重点注意：请将最后这个命令保存下来，后面 node 节点加入集群需要使用。每个人的 token 不一样，不要复制笔记的。
kubeadm join master:6443 --token a7t18p.s20fr0u05nfed8ff \  # 这每个都不一样，不要复制笔记的
--discovery-token-ca-cert-hash sha256:477505d01c6c26903951cc25e448dbac584d0983e5ae5bf0b801b42b6ccf887c
```

如果你忘了复制，也没关系，执行以下命令，重新生成一个

```
kubeadm token create --print-join-command
```

如果初始化 init 不成功，解决方法：

```
# 在 master 节点上，解决配置或环境问题后，重置一下环境，然后再重新初始化
kubeadm reset
```

按照指导内容，在 master 节点上，继续执行命令

```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

验证 master 节点

```
# 在 master 节点上，执行操作
kubectl get node
```

![[8625e25bc1.png]]

### 4 安装 flannel 网络插件（在 master 节点操作）

```
# 方法一：使用 apply 命令，会创建相应的 namespace 和 pod
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# 方法二：如果 apply 一直提示拉取不下来，可以换成先拉取，再 apply
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
kubectl apply -f kube-flannel.yml

# 方法三：如果 wget 也拉不下来（网络刚好比较差），可以用离线文件
```

![[8d12566590.png]]

替换成先拉取，再apply

![[8987e62071.png]]

验证 flannel 的 pod 是否起来

```
# 验证 flannel 的 pod 是否起来
kubectl get pod -A
# -A 表示 ALL
```

![[5c768e05c3.png]]

### 5 加入 node 节点

Tips:  
选加入 node 节点，还是先安装 flannel 网络插件，这个顺序不影响；因为如果不安装网络插件的话，加入 node 节点，会显示未就绪（Not Ready）；所以只要保证两个都执行即可

在两个 node 节点上，都分别执行

```
# 重置一下，再加入
kubeadm reset

# 加入
kubeadm join master:6443 --token a7t18p.s20fr0u05nfed8ff \  # 这里每个都不一样，不要复制笔记的
--discovery-token-ca-cert-hash sha256:477505d01c6c26903951cc25e448dbac584d0983e5ae5bf0b801b42b6ccf887c
```

![[3cfb4ee87e.png]]

```
# 假如，你忘记了加入的命令，master执行
kubeadm token create --print-join-command
# 重新生成一下
```

### 6 验证集群

```
# 在 master 节点上，执行操作，验证节点状态
kubectl get node


kubectl get pod -A
```

![[ec140e5910.png]]

### 常见错误汇总

#### 1 加入 node 节点报错

```
# 解决办法：先重置一下 kubeadm，再次 join
kubeadm reset

# 在 master 或 node 节点上执行这个操作，相当于把对应节点之前的 kubeadm init 或 kubeadm join 操作移除
```

#### 2 服务未开机自启

![[9728b48674.png]]

1、【WARNING 部分的提示】需要在每个机器上执行

```
systemctl enable kubelet
```

2、【ERROR】提示的 containerd 报错，需要重新配置 containerd  
找到讲义的 containerd 安装部分，进行以下操作：

- 【配置 containerd】
- 【关联镜像源目录】
- 【服务重启】

#### 3 Swap 交换分区报错

![[e349164154.png]]

![[7b58a7838e.png]]

重启

#### 4 初始化失败，再次初始化

![[938e6533cd.png]]

```
# 执行以下
kubeadm reset
```

#### 5 kubeadm init 找不到

![[ece1873525.png]]

```
# 合并

kubeadm init \
--apiserver-advertise-address=192.168.88.135 \
--image-repository registry.aliyuncs.com/google_containers \
--pod-network-cidr=10.244.0.0/16 \
--control-plane-endpoint=master
```

#### 6 hostname 查看不对

发现是 master.itcast.cn，不是 master

#### 7 提示 8080 端口不通

初始化后

```
# 是没有创建配置文件导致的，认证不通过。执行以下命令：
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

#### 8 Pod启动崩溃

核心排查命令

```
# 查看 Pod 状态及最近事件（寻找警告信息）
kubectl describe pod <pod-name>

# 查看容器崩溃前的日志（最直接原因）
kubectl logs <pod-name> --previous
```

#### 9 init／join 等待了很久

常见原因及对策

A. 镜像拉取失败（最常见）

**解决：** 使用国内镜像源。

![[2b7f99e0c5.png]]

查看事件：

镜像方案

- 科学上网重新拉取
- 换国内镜像

```
# 查看 containerd 中的镜像（注意 k8s 使用的是 k8s.io 命名空间）
ctr -n k8s.io images list
```

![[8963fd6fb1.png]]

#### 10 国外镜像拉不下来，容器启动失败

![[83f855257c.png]]

```
# 【解决办法】

# 1、先，删除 flannel 资源
kubectl delete -f kube-flannel-kubeadm.yml

# 2、其次，强制删除剩下的终止中的三个容器
kubectl delete pod -n kube-flannel kube-flannel-ds-5wr9s --force
kubectl delete pod -n kube-flannel kube-flannel-ds-79lnq --force
kubectl delete pod -n kube-flannel kube-flannel-ds-v2qnh --force

# 3、重新 apply，再次验证
kubectl apply -f kube-flannel-kubeadm-cn.yml
```

### 【扩展】三种源

![[0641c6a2f7.png]]

- Yum 源

目的：针对 Linux 操作系统，安装软件包  
位置：/etc/yum.repos.d  
更新命令：

```
dnf update -y
```

- Containerd 镜像源

目的：针对 Containerd 拉取镜像  
位置：/etc/containerd/certs.d  
更新命令：

```
systemctl restart containerd
```

- Docker 镜像源

目的：拉取镜像  
位置：/etc/docker/daemon.json  
更新命令：

```
systemctl daemon-reload
systemctl restart docker
```

### 【扩展】安装步骤优化

![[8d228838d0.png]]

![[520849598e.png]]

![[0e48338dd1.png]]

使用 `./init.sh` 批量初始化，使用 `./install.sh` 批量安装组件。