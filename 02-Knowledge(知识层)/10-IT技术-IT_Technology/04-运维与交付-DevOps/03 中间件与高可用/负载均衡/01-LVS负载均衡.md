**四层负载均衡：** 仅通过 **IP + 端口** 进行流量转发，不拆解应用层协议，像极了只看快递单地址而不拆包裹的顺丰分拣中心，具有 **极高并发、极低延迟** 的近硬件级性能。

# 学习目标

1、能够了解 LVS 的基本工作方式  
2、能够安装配置 LVS 实现负载均衡  
3、能够了解 VS-NAT 的配置方式  
4、能够了解 VS-DR 的配置方式  
5、了解 LVS 的调度算法

---

# 一、LVS 概述

## 1、什么是 LVS

LVS 是 Linux Virtual Server 的简称，也就是 **Linux 虚拟服务器**。这是一个由章嵩博发起的开源项目，它的官方网站是 [http://www.linuxvirtualserver.org。现在](http://www.linuxvirtualserver.org.xn--3dsv77d/) LVS 已经是 Linux 内核标准的一部分。

使用 LVS 可以达到的技术目标是：通过 LVS 实现负载均衡技术，并基于 Linux 操作系统构建高性能高可用的服务器集群。它具有良好的可靠性、可扩展性和可操作性，从而以较低的成本实现较优的性能。

LVS 是一个实现负载均衡集群的开源软件项目，LVS 架构从逻辑上可以分为三层：

- 调度层
- Server 集群层
- 共享存储层

记住一句话：LVS就是一个四层负载均衡器，性能最强。

## 2、LVS 工作原理

Linux 底层有防火墙（四表五链）以及 IPVS 两个内核模块：

① iptables（firewalld）：四表五链 => 防火墙规则设定，应用场景：安全防护

② IPVS：也可以直接使用五链，主要用于请求转发，应用场景：负载均衡

![[f2e70cad3d.png]]

LVS 工作流程

内置集群定义进行请求转发到目标服务器

第一步：当用户向负载均衡调度器（Director Server）发起请求，调度器将请求发往至内核空间

第二步：PREROUTING 链首先会接收到用户请求，判断目标 IP 确定是本机 IP，将数据包发往 INPUT 链

第三步：IPVS 是工作在 INPUT 链上的，当用户请求到达 INPUT 时，IPVS 会将用户请求和自己已定义好的集群服务进行比对，如果用户请求的就是定义的集群服务，那么此时 IPVS 会强行修改数据包里的目标 IP 地址及端口，并将新的数据包发往 POSTROUTING

第四步：POSTROUTING 链接收数据包后发现目标 IP 地址刚好是自己的后端服务器，那么此时通过选路，将数据包最终发送给后端的服务器

## 3、LVS 的组成

LVS 由 2 部分程序组成，包括 ipvs 和 ipvsadm

① ipvs（ip virtual server）：一段代码工作在内核空间，叫 ipvs，是真正实现调度的代码（类似 Nginx 中的 proxy_pass）

② ipvsadm：另外一段是工作在用户空间，叫 ipvsadm，负责为 ipvs 内核框架编写规则，定义谁是集群服务，谁是后端真实的服务器（Real Server），类似 Nginx 中的 upstream

LVS 组成 = ipvs（内核，负载均衡调度代码） + ipvsadm（ipvs 管理器，负责提供集群 / Real Server 后端服务器等信息）

## 4、LVS 相关术语

负载均衡（1 台） + Web 服务器（2 台）

DS：Director Server，指的是前端负载均衡器节点（负载均衡服务器）

RS：Real Server，后端真实的服务器（Web 服务器）

**VIP**：Virtual IP，面向外部用户请求的 IP 地址（负载均衡对外提供的访问地址）

**DIP**：Director Server IP，主要用于和内部主机通信的 IP 地址（负载均衡与 Web 服务器交互的内部 IP）

**RIP**：Real Server IP，后端服务器的 IP 地址

CIP：Client IP，访问客户端的 IP 地址

![[d6d67e28eb.png]]

## 5、LVS 三种工作模式

① NAT 模式（重点 => 使用量次之）

**② DR 模式（重点 => 使用量最多）**

③ Tun 模式（了解） => IP 隧道模式

# 二、LVS / NAT 原理和特点

## 1、NAT 工作原理图

基础网络知识：数据包

数据包头部（Header）

- 作用：类似信封上的地址和标记，告诉网络设备如何处理这个数据包。
- 内容：

- 源 IP 地址：发送方的 IP（如 192.168.1.100）
- 目标 IP 地址：接收方的 IP（如 10.0.0.1）
- 源端口：发送方的端口（如 5000）
- 目标端口：接收方的端口（如 80）
- 协议类型：指明是 TCP、UDP 或 ICMP 等协议

有效载荷（Payload）

- 作用：实际传递的数据内容，类似信件的正文。
- 示例：

- 如果是网页请求，可能是 `GET /index.html HTTP/1.1`
- 如果是下载文件，可能是文件内容的一部分

尾部（Footer）

- 作用：校验数据完整性（如 CRC 校验码），确保传输过程中未被破坏

重点理解NAT方式的实现原理和数据包的改变

DS压力大需高配置

宏观：

![[68a05e4e43.png]]

微观：

![[72693cfa70.png]]

讲个故事：

Client（客户），需求：盖个房=>找专业公司

DirectorServer（恒大）

合同：客户端：标端

恒大本身不具备建筑能，有办法，后面有很多小包工队。包工队(A=>Web01）、包工队(B=>Web02)

Client找到DirectorServer（CIP:VIP）=>恒判断合同目标是否为自己，如果是，把合同转发给内部审核调整，审核完成后，调整下合同的标，找下下包队承接这个业务，但是对外，客户不能知道。内部调整后，把任务转发给包队B，包队B拿到合同后，干活。任务结束后，不能把结束直接转给客户端。要直接转回给恒，确认合同，稍作修改，把承办变更为恒（VIP），然后把最终结果交回给Client客户端。

微观图：www.shop.com=>192.168.16.100

## 2 NAT模型的特性

- RS 应该使用私有地址，RS 的网关必须指向 DIP，
- DIP 和 RIP 必须在同一网段内
- 请求和响应报文都需要经过 Director Server，负载场景中 Director Server 易成为性能瓶颈
- 支持端口映射
- RS 可以使用任意操作系统
- 缺陷：对 Director Server 压力较大，请求和响应都需经过 Director Server

![[c5a16a774c.png]]

正常情况下：如果要搭建 LVS NAT 模式  
Web01、Web02、DS 服务器的网卡应使用仅主机模式（仅限内部通信，作为内网环境）  
DS 服务器另外添加一张网卡连接外网（可以使用 NAT 模式）  
域名解析指向该外网 IP 地址

但是：由于 Web01、Web02 已经搭建完成、本次操作直接为其添加一张 NAT 或桥接网卡即可模拟外网环境。本次课程中使的VIP卡采桥接模式（和NAT模式的内地址区分开）。

# 三、LVS-NAT 模式实践

## 1、环境规划

|   |   |   |
|---|---|---|
|角色|作用|IP|
|NAT|负载均衡调度服务器 DS|192.168.39.*（对外访问的 VIP）192.168.88.10（DIP）|
|Web01|真实服务器 Web 服务器 RS|192.168.88.104（RIP）|
|Web02|真实服务器 Web 服务器 RS|192.168.88.105（RIP）|

准备工作：

先给 Web01 服务器以及 Web02 服务器拍摄一个快照！！！

给 NAT 增加一块网卡，命名为 ens37，桥接模式，自动或手动获取 IP 均可，本例中 IP 获取为 192.168.39.*

理论上：  
NAT 模式对应的 DS 服务器应该有两张网卡

- 一张绑定 VIP（对外提供服务，需使用公网 IP，虚拟机中一般使用 NAT 模式）
- 一张绑定 DIP（内网 IP，局域网地址，对应仅主机模式）

第一步：  
克隆 CentOS Stream 9，生成 NAT 模式机器

![[a0c696d19b.png]]

第二步：设置主机名称

```
# hostnamectl set-hostname nat.itcast.cn
# su
```

第三步：更改 IP 地址

```
# vim /etc/NetworkManager/system-connections/ens33.nmconnection

addresses=192.168.88.10/24
```

第四步：额外添加一张网卡，选择对外提供服务的桥接模式或 NAT 模式均可，这里采用桥接模式

```
# cd /etc/NetworkManager/system-connections/
# cp ens33.nmconnection ens37.nmconnection

# vi /etc/NetworkManager/system-connections/ens37.nmconnection
# 记得提前删除uuid
[connection]
id=ens37
type=ethernet
interface-name=ens37
autoconnect-priority=-999
timestamp=1728748536

[ethernet]

[ipv4]
method=manual
addresses=192.168.39.88/24
gateway=192.168.39.1
dns=8.8.8.8;

[ipv6]
method=ignore

[proxy]

# nmcli connection reload
# nmcli connection up ens37
# nmcli connection modify ens37 connection.autoconnect yes
```

随着环境不同，如教室、宿舍、家，对应网段都可能发生变化，需要根据实际情况进行设计

遇到问题 1：有的同学添加网卡以后，无法 ping 通  
① Windows 防火墙未关闭  
② Linux 防火墙未关闭  
③ 可能与 VMware 虚拟网卡配置有关，具体修改如下：

![[5bebcd69b8.png]]

![[5e52414e70.png]]

![[07a3056315.png]]

![[edd18f5244.png]]

## 2、LVS-NAT 模式负载均衡搭建

### ☆ DS 服务器操作

第一步：安装 ipvsadm 工具

```
# yum install ipvsadm -y
```

第二步：在 DS 调度器服务器上，使用 ipvsadm 编写负载均衡代码

```
① 定义一个虚拟服务（负载均衡）
# ipvsadm -A -t 192.168.39.150:80 -s rr

选项说明：
-A：定义一个虚拟服务
-t：定义虚拟服务地址及端口号
-s：定义调度算法，rr 代表轮询算法

② 添加 Real Server（Web01、Web02）并指定工作模式为 NAT
# ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.104:80 -m
# ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.105:80 -m

选项说明：
-a：添加真实的后端服务器
-t：指定服务器地址及端口号（NAT 模式支持端口映射，可以是非 80 端口）
-m：NAT 模式
-g：DR 模式
```

常见错误汇总

问题 1：Zero port specified for non-persistent service  
解决方案：未设置端口

问题 2：Memory allocation problem  
解决方案：信息输入错误

第三步：使用 ipvsadm 查看调度规则

```
# ipvsadm -L -n
```

第四步：在 NAT 模式的 DS 服务器上开启 ip_forward 转发功能

```
# vim /etc/sysctl.conf
net.ipv4.ip_forward=1

# sysctl -p
```

sysctl.conf代表内核配置文件！！！

### ☆ RS 服务器操作（Web01 / Web02）

唯一需要做的一件事：就是把 Web01 / Web02 的默认网关指向 DIP

```
# yum install net-tools -y
# route del default
# route add default gw 192.168.88.10
# route -n
```

如果想删除（可选）

```
# route del default gw 192.168.88.10
```

### ☆ 劫持 [www.shop.com](http://www.shop.com/) 域名

windos也域名劫持

```
# vim /etc/hosts
192.168.39.150 www.shop.com
```

### 核心脚本

DS 服务器：

```
yum install ipvsadm -y

ipvsadm -A -t 192.168.39.150:80 -s rr
ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.104:80 -m
ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.105:80 -m

vim /etc/sysctl.conf
# 尾部追加，开启 forward 转发
net.ipv4.ip_forward=1

sysctl -p

# 如果写错了，清空规则重新来
ipvsadm -C
```

Web01 / Web02：

```
route del default
route add default gw 192.168.88.10
route -n
```

测试：在 DS 服务器上

```
vim /etc/hosts
192.168.39.150 www.shop.com
```

192.168.39.150 要改成你们自己的 VIP！！！

## 3、LVS-NAT 模式负载均衡修改

① 修改 DS 服务器（删除再重建）

```
# ipvsadm -C
```

② 修改 RS 服务器（删除再重新创建）

```
# ipvsadm -d -t 192.168.39.150:80 -r 192.168.88.104
```

③ 更改调度算法（不用操作）

```
# ipvsadm -E -t 192.168.39.150:80 -s wrr

# ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.104:80 -m -w 8
# ipvsadm -a -t 192.168.39.150:80 -r 192.168.88.105:80 -m -w 2
```

# 四、LVS/DR 原理和特点

响应不需要 DR

作用：LVS/DR 负载均衡效率最高，且解决了 NAT 模式的缺陷

宏观：

![[5664a24f44.png]]

### 1、DR 工作原理图

注意：**重点理解** 请求报文的目标 MAC 地址会被修改为选定 RS 的 MAC 地址（ARP 协议 => 广播 旬问谁有VIP，如果某台服务器响应了，则告知客户端，你的Mac地址））

微观：

- NAT 模式：通过修改目标 IP 实现负载均衡
- DR 模式：通过目标 IP + 目标 MAC 地址调整实现负载均衡

- **包到达 DS：** 客户端请求 VIP。此时包的 `目标IP = VIP`，`目标MAC = DS的MAC`。
- **DS 转发：** DS 发现是一个负载均衡请求，它**不修改 IP**，而是把包的 `目标MAC` 改写成其中一台 RS（比如 WEB01）的 MAC 地址。
- **RS 直接回包：** 重点来了！RS 处理完后，直接把响应包发给客户端，**不经过 DS**。此时 `源IP = VIP`。

DS服务器: mac地址=>00:ad:13:56 (VIP-MAC)

WEB01: mac地址=>11:b2:66:33 (VIP-MAC

WEB02: mac地址=>22:c5:77:22 (VIP-MAC)

![[fc8e7871fa.png]]

疑问点：MAC 地址发生改变，客户端是否会知道？

```
TCP/IP 协议工作原理：
在网络通信中，IP 地址负责逻辑寻址，而 MAC 地址负责实际的物理传输。
客户端在解析 IP 地址时，只关心目的 IP 不变即可，而 MAC 地址的变化不影响整个 TCP/IP 数据包的完整性。

现实网络环境：
即使在通常情况下，网络设备可能因为网络路径选择或跳转而导致 MAC 地址变化（如路由器转发时）。
因此，设计上 TCP/IP 协议对此有容忍。
```

LVS-DR 模式数据报文处理流程

(a) 当用户请求到达 Director Server，此时请求的数据报文会先进入内核空间的 **PREROUTING 链**

- 报文源 IP：CIP
- 报文目标 IP：VIP

(b) PREROUTING 检查发现数据包目标 IP 为本机，将数据包送至 **INPUT 链**

(c) IPVS 比对数据包请求的服务是否为集群服务

- 若是，将请求报文的 **源 MAC 地址修改为 DIP 的 MAC**
- 将 **目标 MAC 地址修改为 RIP 的 MAC**
- 数据包发至 **POSTROUTING 链**
- 此时源 IP 和目标 IP **未修改**，仅 MAC 地址被修改

(d) 由于 DS 和 RS 在同一网络中，数据通过二层传输

- POSTROUTING 链检查目标 MAC 地址为 RIP 的 MAC
- 数据包被发送至 Real Server

(e) RS 接收报文

- 因目标 MAC 为自己，RS 处理请求
- 处理完成后，响应报文通过 eth0/ens33 网卡发出
- 源 IP 为 VIP，目标 IP 为 CIP

(f) 响应报文最终送达客户端

**普及网络知识点：ARP 协议（ARP 广播）**

**ARP 全称**：Address Resolution Protocol，中译为“地址解析协议”

- 作用：在计算机网络中，将 IP 地址和物理地址（MAC 地址）相互映射
- 在现代网络中，ARP 是网络通信的关键部分

**简单比喻解释 ARP**：

- 公司场景：

- 每个员工有一个桌子（物理位置）
- 每个桌子上有一个名字牌（IP 地址）

- 如果你想送文件（数据包）给某位员工，只知道名字牌还不够，需要知道桌子位置（MAC 地址）

**ARP 工作过程**：

1. **喊人**

- 你只知道员工的名字牌（IP 地址），不知道桌子（MAC 地址）
- 大声问：“谁能告诉我，名字牌为 IP 地址 192.168.1.5 的员工在哪个桌子上坐？”
- 响应：如果是那位员工，他会说：“哦，那是我，我的桌子号（MAC 地址）是 00-14-22-01-23-45。”
- 这样你就知道了目标桌子（MAC 地址）

2. **传输**

- 拿到正确的桌子号后，你就可以精准把文件送到目标桌子（数据包发送完成）

**在 LVS-DR 模式中的作用**：

- ARP 协议在 Direct Routing 模式中非常关键
- 它负责 IP 地址到 MAC 地址的映射
- 正确处理 ARP 是确保负载均衡器（DS）和真实服务器（RS）之间通信正常的基础

**VIP 的唯一性问题（LVS-DR 模式）**

在 DR 模式下，多个真实服务器（Real Servers）共享同一个 VIP（虚拟 IP），都需要接收来自 Director Server 的流量。

问题点：

- 如果每个 RS 都对网络上的 ARP 请求进行响应，会造成 IP 地址冲突
- 网络终端（客户端等）无法确定 VIP 对应的正确 MAC 地址，导致通信混乱

**解决方案：ARP 响应控制**

1. **ARP 抑制（ARP Suppression）**

- 在所有真实服务器上配置 ARP 忽略
- 真实服务器不会响应来自外部网络的 ARP 请求
- 这样只有 LVS Director 响应 VIP 的 ARP 请求

2. **配置 LVS Director**

- LVS Director 对外提供 VIP 的统一 ARP 回复
- 所有客户端请求首先到达 Director，再由其根据负载均衡算法路由到合适的 RS

3. **回环接口绑定 VIP**

- 真实服务器将 VIP 绑定到回环接口（lo）上
- 不对外广播，保证不会发送 ARP 响应
- 避免多点 ARP 响应引起的冲突

这样可以确保 VIP 在 DR 模式下的唯一性，并保证负载均衡通信稳定可靠。

### 2、LVS-DR 模型的特性

**特点**：

1. 前端路由保证所有目标地址为 VIP 的报文都发送给 **Director Server**，而不是直接到 RS
2. RS 可以使用私有地址，也可以**公网地址**

- 若使用公网地址，可通过互联访问 RIP
- RS 与 Director Server 必须在同一物理网络中

3. 所有请求报文都经过 Director Server，但响应报文 **不经过 Director Server**

- 不进行地址转换
- 不进行端口映射

4. RS 可以运行大多数常见操作系统
5. RS 的默认网关 **绝不允许指向 DIP**（不允许响应经过 Director）
6. RS 上的接口绑定 VIP 的 IP 地址

**缺陷**：

- RS 与 DS 必须在同一机房或局域网环境中

### 3、特点 1 的解决方案

**问题**：前端路由器需将 VIP 的流量路由到 Director Server，但用户未必有路由配置权限（如由运营商管理），因此需要在服务器端控制

**解决方案**：

1. **arptables**

- 在 ARP 层面上实现防火墙规则
- 过滤 RS 响应 ARP 请求，避免多点响应

2. **修改 RS 内核参数**

- `arp_ignore` 和 `arp_announce`
- **将 VIP 配置在 RS 的回环接口（lo）别名上**
- 限制 RS 不响应外部网络对 VIP 的 ARP 请求

这样可以保证 VIP 的 ARP 响应只由 Director Server 提供，避免 DR 模式下的 IP 冲突与通信异常。

![[88741e2120.png]]

# 五、LVS-DR 模式实践

## 1、环境规划

|   |   |   |
|---|---|---|
|角色|作用|IP 地址|
|DS|负载均衡调度服务器|192.168.88.110 (DIP) 192.168.88.200 (VIP)|
|web01|真实服务器 RS1|192.168.88.101 (RIP) 192.168.88.200 (VIP)|
|web02|真实服务器 RS2|192.168.88.103 (RIP) 192.168.88.200 (VIP)|

**准备工作**：

- 克隆 CentOS，生成 DR01 服务器
- 更改 MAC 地址
- 修改主机名称
- 配置 IP 地址
- 修改 `/etc/hosts` 文件绑定主机名与 IP
- 关闭防火墙和 SELinux
- 时间同步
- 安装依赖包

**更改主机名称**

```
hostnamectl set-hostname dr.itcast.cn
yum install vim wget rsync net-tools -y
```

## 2、LVS-DR 模式负载均衡搭建

### ☆DS 服务器操作

**第一步：安装 ipvsadm 工具**

```
# yum install ipvsadm -y
```

**第二步：在 ens33 网卡上挂载 VIP 地址**

```
# ifconfig ens33:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up
```

![[1e64c85be6.png]]

**添加主机路由**

```
# route add -host 192.168.88.200 dev ens33:0
```

**第三步：创建 IPVS 调度规则**

```
# ipvsadm -C
# ipvsadm -A -t 192.168.88.200:80 -s rr
# ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.104 -g
# ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.105 -g
```

**说明**：

- `-C`：清空已有调度规则
- `-A`：添加虚拟服务（VIP）
- `-t`：指定 VIP 地址及端口
- `-s rr`：调度算法为轮询（Round Robin）
- `-a`：添加真实服务器（RS）
- `-g`：指定 DR 模式
- `-m`：NAT 模式（此处未使用）

**测试查看规则**

```
# ipvsadm -Ln --stats
```

### ☆RS 服务器操作（Web01/Web02）

**第一步：抑制 RS 服务器上的网卡对 VIP 的 ARP 响应**

```
echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce
```

**永久生效设置**

```
# vim /etc/sysctl.conf
net.ipv4.conf.all.arp_ignore=1
net.ipv4.conf.lo.arp_ignore=1
net.ipv4.conf.all.arp_announce=2
net.ipv4.conf.lo.arp_announce=2

# sysctl -p
```

**第二步：在 RS 服务器上挂载 VIP（挂在回环接口 lo 上）**

```
# ifconfig lo:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up
```

添加主机路由

```
# route add -host 192.168.88.200 dev lo:0
```

### ☆劫持 [www.shop.com](http://www.shop.com/) 域名

```
# hosts
192.168.88.200 www.shop.com
```

### 核心脚本

DR01/DR02 服务器操作

```
# 安装 ipvsadm 工具
yum install ipvsadm -y

# 挂载 VIP，并添加主机路由
ifconfig ens33:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up
route add -host 192.168.88.200 dev ens33:0

# 清空现有 IPVS 规则
ipvsadm -C

# 创建 IPVS 调度规则（轮询算法）
ipvsadm -A -t 192.168.88.200:80 -s rr

# 添加真实服务器 RS，并指定 DR 模式
ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.104 -g
ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.105 -g
```

---

永久生效设置

```
# vim /etc/sysctl.conf
net.ipv4.conf.all.arp_ignore=1
net.ipv4.conf.lo.arp_ignore=1
net.ipv4.conf.all.arp_announce=2
net.ipv4.conf.lo.arp_announce=2

# sysctl -p
```

Web01/Web02 服务器操作

```
# 抑制 VIP 的 ARP 响应
echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce

# 挂载 VIP 到回环接口
ifconfig lo:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up

# 添加主机路由
route add -host 192.168.88.200 dev lo:0

# 可选替代方式：
# ip addr add 192.168.88.200/32 dev lo
# route add -host 192.168.88.200 dev lo:0
```

## 3、答疑解惑

```
# ifconfig ens33:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up
# 广播地址和VIP设置为相同的地址通常用于防止在局域网内产生不必要的广播活动，因为这个地址只用于点对点通信。
# 配置广播地址为192.168.88.200意味着在逻辑上将这个地址的作用范围限制在自己，不对外发起ARP广播。
# 这与设置netmask为255.255.255.255（主机路由）结合使用时，常用于确保只有精确的流量（即针对此IP的数据包）才被处理，而不会对整个子网进行响应。

# route add-host 192.168.88.200 dev ens33:0
# 将一个静态路由添加到系统的路由表中，指定任何要访问192.168.88.200的流量都通过ens33:0接口处理。
# 这确保任何本地进程（如应用或服务）发出的对于192.168.88.200的请求都用这个接口，而不是可能的其他配置。
```

抑制ARP响应

```
# 配置ARP忽略与通告策略
echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce

# 配置本地回环接口别名IP
ifconfig lo:0 192.168.88.200 broadcast 192.168.88.200 netmask 255.255.255.255 up
```

为什么 Windows 可以通过 `www.shop.com` 域名实现请求转发，而自己访问自己不？

**答**：DR 模式的本质是 LVS 只转发来自外部主机的请求流量，不处理本机自己发出的流量。

**执行流程说明**：

```
# 你在 LVS 上执行：
curl http://www.shop.com

# 解析 /etc/hosts 得到 VIP：192.168.88.200

# 系统看到这个 IP 是本地地址（绑定在 lo 或其它接口上），就直接走本地路由，
# 不会再交给 LVS 处理！而且 LVS 是基于内核 hook 的 PREROUTING 链工作，
# 本地发出的包根本不会经过 PREROUTING 链，所以 LVS 无法给自己发出的请求做负载均衡。
```

# 六、LVS/Tun 原理和特点（了解）

**作用**：LVS/Tun【隧道模式】 用于跨区域负载均衡。  
**缺点**：完全依赖外部网络（公网）访问，所以效率略低。

---

## 1、Tun 工作原理

```
# 在原有的 IP 报文外再次封装一层 IP 首部

# 内层 IP 首部：
# 源地址：CIP（客户端 IP）
# 目标地址：VIP（虚拟 IP）

# 外层 IP 首部：
# 源地址：DIP（调度器 IP）
# 目标地址：RIP（真实服务器 IP）
```

---

对比总结

```
# NAT：网络地址转换（修改 IP 地址）
# DR：修改目标 MAC（基于二层转发）
# Tun：IP 隧道（二次封装）跨区域DR 都有VIP 不由 DS响应
```

![[21128f9528.png]]

LVS/Tun 执行流程

```
# (a) 当用户请求到达 Director Server，此时请求的数据报文先到内核空间的 PREROUTING 链，
#     源 IP 为 CIP，目标 IP 为 VIP。

# (b) PREROUTING 检查发现目标 IP 是本机，将数据包送至 INPUT 链。

# (c) IPVS 判断该请求是否为集群服务，若是，则在原请求报文外再次封装一层 IP 报文：
#     外层源 IP 为 DIP，目标 IP 为 RIP，然后发送至 POSTROUTING 链。
#     此时：源 IP 为 DIP，目标 IP 为 RIP。

# (d) 因为在外层多封装了一层 IP 首部，所以该过程称为 IP 隧道（Tun 模式）。

# (e) RS 接收到报文后，发现目标 IP 是自己，接收该报文并拆除外层 IP 首部，
#     得到内层报文（源 IP 为 CIP，目标 IP 为 VIP）。
#     由于 VIP 绑定在 lo 接口上，RS 开始处理请求，
#     处理完成后通过 lo 接口转发到 eth0 网卡并向外发送。
#     此时：源 IP 为 VIP，目标 IP 为 CIP。

# (f) 响应报文最终返回客户端。
```

## 2、LVS-Tun 模型的特性

```
# RIP、VIP、DIP 全部为公网地址

# RS 的网关不会也不可能指向 DIP

# 所有请求报文必须经过 Director Server，
# 但响应报文不能经过 Director Server（直接返回客户端）

# 不支持端口映射（如 80 => 80）

# RS 必须支持 IP 隧道（Tun）

# 注：
# 企业中最常用的是 DR 模式，
# NAT 模式配置相对简单、使用方便，
# 后续实践中重点掌握 DR 和 NAT 的配置过程
```

# 七、LVS 的十种调度算法

## 1、Fixed Scheduling Method（静态调度）

### ①⭐ RR（Round Robin）轮询（常用）

服务器性能相当

调度器通过“轮询”算法将外部请求按顺序轮流分配到集群中的真实服务器上。  
它均等地对待每台服务器，不考虑服务器当前的连接数和系统负载。

Web01  
Web02

代码块

```
ipvsadm -A -t 192.168.88.200:80 -s rr
```

---

### ② WRR（Weighted Round Robin）加权轮询（常用）=> Weight

服务器性能不一

调度器通过“加权轮询”算法，根据真实服务器的处理能力分配不同权重。  
性能强的服务器会处理更多请求。

Web01  
weight=8

Web02  
weight=2

调度效果：按权重比例分配请求（8:2 ≈ 80% : 20%）

```
ipvsadm -A -t 192.168.88.200:80 -s wrr

ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.101:80 -g -w 3
ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.102:80 -g -w 1
```

### ③ DH（Destination Hashing）目标地址哈希

**应用场景**：缓存服务器（提高缓存命中率，使用较少）

同一个目标地址（目标 IP）始终会被分配到同一台后端服务器处理。

**举例说明：**  
假设你是仓库管理员：

- 所有寄往“北京市朝阳区”的包裹 → 永远放进 1 号车
- 所有寄往“上海市浦东新区”的包裹 → 永远放进 2 号车

不管是谁寄的，只看“目标地址”，每次都进入同一台服务器。

代码块

```
ipvsadm -A -t 192.168.88.200:80 -s dh
```

### ④⭐ SH（Source Hashing）源地址哈希

**应用场景**：类似 `ip_hash`，用于解决 Session 共享问题（也可结合 NoSQL）

该算法与目标地址哈希（DH）相反，是根据**源 IP 地址（客户端 IP）**进行哈希分配。

**工作原理：**  
将客户端的源 IP 作为 HashKey，通过哈希表找到固定的后端服务器：

- 如果该服务器可用且未超载 → 直接转发请求
- 否则 → 返回空（或重新调度）

**特点：**

- 同一个客户端（同一源 IP）始终访问同一台 RS
- 保证 Session 粘性（会话保持）
- 算法逻辑与 DH 基本一致，只是将“目标 IP”换成“源 IP”

**补充：**  
在实际应用中，SH 和 DH 可以结合使用，例如在防火墙集群中，保证流量进出路径一致。

代码块

```
ipvsadm -A -t 192.168.88.200:80 -s sh
```

## 2、Dynamic Scheduling Method（动态调度）

动态调度算法除了参考调度策略本身外，还需要结合后端服务器的实际运行状态（如连接数、负载等）。

### ① LC（Least Connections）最少连接（常用）

性能相当

调度器通过“最少连接”算法，将新的请求分配给当前活跃连接数最少的服务器。  
活跃连接数是指当前正在处理的连接数量，由 LVS 连接表维护。

**核心：**  
只比较每台服务器的活跃连接数，选择连接数最少的服务器分配新请求；不考虑服务器性能差异（权重默认相等或不使用权重）。相近性能

**示例场景：**  
假设一个 LVS 负载均衡器管理 3 台后端服务器处理 HTTP 请求：

- 服务器 A：高性能（权重 = 4）
- 服务器 B：中等性能（权重 = 2）
- 服务器 C：低性能（权重 = 1）

当前活跃连接数如下：

- 服务器 A：10 个连接
- 服务器 B：8 个连接
- 服务器 C：5 个连接

LC 不考虑权重，只比较连接数：

- 活跃连接数最少的是服务器 C（5 个）

因此，新请求会分配给服务器 C。  
分配后，服务器 C 的活跃连接数变为：6。

问题：LC 算法的局限性

LC（最少连接）没有考虑服务器性能差异。  
例如：服务器 C 虽然连接数最少，但权重只有 1（性能较低），可能无法高效处理更多请求；而服务器 A（权重 = 4）性能更强，可能仍有处理余量，但不会被优先选中。

```
ipvsadm -A -t 192.168.88.200:80 -s lc
```

### ② ⭐WLC 加权最少连接（常用）

在 LC 的基础上引入权重，通过计算归一化连接数（活跃连接数 / 权重），选择归一化连接数最小的服务器。权重反映服务器的处理能力，权重高的服务器能处理更多连接。

```
归一化连接数 = 活跃连接数 / 权重
```

如果权重为 0，服务器被视为不可用，跳过分配。  
比较所有服务器的归一化连接数，选择值最小的服务器。  
如果有多台服务器的归一化连接数相等，可以随机选择或根据其他规则（如服务器 ID 顺序）决定。

举例

假设有 3 台后端服务器：

服务器 A：活跃连接数 = 10，权重 = 4  
服务器 B：活跃连接数 = 8，权重 = 2  
服务器 C：活跃连接数 = 5，权重 = 1

计算归一化连接数：

服务器 A：10 / 4 = 2.5  
服务器 B：8 / 2 = 4.0  
服务器 C：5 / 1 = 5.0

结果：服务器 A 的归一化连接数最小（2.5），新连接分配给服务器 A。

```
ipvsadm -A -t 192.168.88.200:80 -s wlc

ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.104:80
ipvsadm -a -t 192.168.88.200:80 -r 192.168.88.105:80
```

### ③ SED 最少期望延迟（特殊的 WLC 算法）

SED 算法通过估算每台服务器的期望延迟（基于活跃连接数和权重），将新连接分配给预计处理最快的服务器。

```
期望延迟 = （活跃连接数 + 1） / 权重
```

说明：  
“+1”表示新连接加入后的连接数。  
权重越大，期望延迟越小，说明性能越强。

作用：更精确评估服务器处理新连接的能力，优先选择响应更快的服务器。

**举例**

假设有 3 台后端服务器：

服务器 A：活跃连接数 = 10，权重 = 4  
服务器 B：活跃连接数 = 8，权重 = 2  
服务器 C：活跃连接数 = 5，权重 = 1

计算期望延迟：

服务器 A：（10 + 1）/ 4 = 2.75  
服务器 B：（8 + 1）/ 2 = 4.5  
服务器 C：（5 + 1）/ 1 = 6.0

结果：选择服务器 A（期望延迟最小 2.75）

```
ipvsadm -A -t 192.168.88.200:80 -s sed
```

### ④ NQ 永不排队

优先分配空闲服务器，避免复杂计算。

• 如果存在空闲服务器（活跃连接数 = 0），直接分配  
• 如果没有空闲服务器，则退化为 RR（轮询）  
• 不考虑权重或复杂计算（如 WLC、SED）

适用场景：轻负载或希望快速分配、降低延迟的场景

举例

优先选择活跃连接数 = 0 的服务器；否则 RR

A：10  
B：8  
C：5（无空闲服务器）

退化为 RR：假设上次分配给 B，则下一次分配给 C

```
ipvsadm -A -t 192.168.88.200:80 -s nq
```

### ⑤ LBLC 基于本地的最少连接（针对缓存服务器）

将来自同一客户端（源ip）的连接尽可能分配到同一台后端服务器（本地性），同时在多个候选服务器中选择活跃连接数最少的服务器（最少连接）。

本地性：通过哈希（如基于客户端 IP 或目标 IP）将相同来源的连接映射到同一服务器，减少缓存丢失（cache miss），提高缓存命中率。  
最少连接：在满足本地性条件的候选服务器中，选择活跃连接数最少的服务器。  
适用于有状态服务（如需要缓存的应用，例如 Web 服务或数据库查询）。

适用场景：适合需要缓存一致性（如 Web 缓存、数据库查询）且服务器性能相近的场景。

举例

假设哈希（192.168.1.100）映射到候选子集 {A，B}：

A：10  
B：8

选择活跃连接数最少的服务器：服务器 B（8 < 10）

结果：分配给服务器 B。

特点：  
优先本地性（同客户端倾向于同服务器）。  
在候选服务器中选择连接数最少的，类似 LC，但受哈希约束。

```
ipvsadm -A -t 192.168.88.200:80 -s lblc
```

### ⑥ LBLCR 带复制的基于本地的最少连接（针对缓存服务器）

本地性：通过哈希（如基于目标 IP）将同一目标（destination IP）的请求映射到一组服务器（ServerSet），提高缓存命中率。  
最少连接：在目标服务器组中，选择活跃连接数最少的服务器。  
动态复制：当服务器组过载时，添加新的低负载服务器；当负载降低时，移除高负载服务器，控制复制程度。

特点：  
维护一个从目标 IP 到服务器组的映射（ServerSet[dest_ip]），例如 {A，B}。  
当目标（如热门网站）请求激增时，动态扩展服务器组，添加低负载服务器。  
定期检查服务器组，若长时间未修改，移除最忙服务器，避免过度复制。

适用场景：缓存集群（如 Web 缓存），需要高缓存命中率，同时应对热点目标的动态负载。

举例

假设 LVS 管理一个 Web 缓存集群，有 3 台后端服务器：

服务器 A：活跃连接数 = 10，权重 = 4  
服务器 B：活跃连接数 = 8，权重 = 2  
服务器 C：活跃连接数 = 0，权重 = 3（空闲）

目标 IP：192.168.1.100（例如客户端请求访问某个热门网站）

哈希映射：  
hash(192.168.1.100) → ServerSet[192.168.1.100] = {A，B}（初始服务器组）

过载阈值：  
假设服务器活跃连接数超过权重视为过载（A：10 > 4，B：8 > 2）

清理时间：  
假设服务器组未修改超过时间 T = 60 秒，移除最忙服务器

由于 {A，B} 过载，LBLCR 从全局服务器 {A，B，C} 中选择活跃连接数最少的服务器：

A：10  
B：8  
C：0

选择服务器 C（0 个连接最少）

将服务器 C 添加到 ServerSet[192.168.1.100] = {A，B，C}  
更新服务器组最后修改时间：ServerSet[192.168.1.100].lastmod = Now

```
ipvsadm -A -t 192.168.88.200:80 -s lblcr
```

### 简化版

```
LC（Least Connections，最少连接）：
基本概念：选择当前连接数最少的服务器。
简单理解：谁排队人少就选谁。

WLC（Weighted Least Connections，加权最少连接）：
基本概念：在最少连接基础上加入权重（性能），选择“连接数/权重”最小的服务器。
简单理解：又快又不忙的优先。

SED（Shortest Expected Delay，最短期望延迟）：
基本概念：综合连接数和处理能力，选择预计等待时间最短的服务器。
简单理解：谁能最快处理完就选谁。

NQ（Never Queue，永不排队）：
基本概念：如果有空闲服务器直接分配，否则再按规则选。
简单理解：有空位就直接上，不排队。

LBLC（Locality-Based Least Connections，基于局部性的最少连接）：
基本概念：同一客户端优先分配到同一服务器，再在候选中选连接最少的。
简单理解：尽量去“熟悉的那台机器”。

LBLCR（Locality-Based Least Connections with Replication，带复制的LBLC）：
基本概念：在LBLC基础上，热点请求会扩展服务器组（复制），动态分担压力。
简单理解：热门服务多开几台一起扛。
```

## 常用算法：

```
静态：
rr（轮询）
wrr（加权轮询）
sh（源地址哈希 / ip_hash）

动态：
lc（最少连接）
wlc（加权最少连接）
sed（最短期望延迟）
```

## 源地址哈希 vs 目标地址哈希

|   |   |   |
|---|---|---|
|**特性**|**源地址哈希 (Source IP Hash)**|**目标地址哈希 (Destination IP Hash)**|
|**英文缩写**|**SH** (Source Hash)|**DH** (Destination Hash)|
|**Hash 的对象**|客户端的 IP (`src_ip`<br><br>)|服务器/目标的 IP (`dst_ip`<br><br>)|
|**解决的问题**|客户端的“登录状态”不要丢。|后端缓存的“命中率”要高。|
|**谁获益？**|**服务器**（更方便管理 Session）。|**客户端/链路**（更快速拿到缓存数据）。|
|**典型案例**|保持购物车、登录态。|运营商缓存、防火墙集群、代理服务器。|

- 源地址哈希 (Source Hashing / Source IP Hash)

- **术语：**`sh` (Source Hashing)
- **口语化解释：** “认准这台客户端，它所有的请求都发往同一台后端服务器。”

- **主要目的：Session Persistence (会话保持)**。

- 目标地址哈希 (Destination Hashing / Destination IP Hash)

- **术语：**`dh` (Destination Hashing)
- **口语化解释：** “认准这个目标，所有找它的请求都走同一条路。”
- **主要目的：Cache Affinity (缓存亲和性)**。

- **常用于 正向代理服务器集群（比如公司内网访问外网）。**
- **如果成千上万个员工都要访问** `**google.com**`**，负载均衡器发现“目的地”是一样的，就始终把请求发往专门缓存了 Google 内容的 Proxy01。这样可以极大提高缓存命中率。**