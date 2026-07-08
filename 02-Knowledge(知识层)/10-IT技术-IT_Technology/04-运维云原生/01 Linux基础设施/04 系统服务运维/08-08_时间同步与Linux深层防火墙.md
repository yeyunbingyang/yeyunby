## 1. NTP时间同步服务

### 1.1 什么是NTP

NTP是网络时间协议(Network Time Protocol)，它是用来同步网络中各个计算机的时间的协议。

在机房中，各个服务器的时间务必要保持一致，同时也要和实际的时间保持一致

```
保持一致性的必要性原因：

1: 保证分布式系统的一致性: 多个服务器需要协同工作。如果时间不同步，可能导致：
        日志时间线混乱，难以排查问题。
        数据写入顺序错误，影响数据一致性

2: 保障安全性:时间同步对服务器安全机制至关重要：
        认证和加密：许多安全协议（如 TLS/SSL、Kerberos）依赖精确的时间戳来验证会话有效性。如果时间不同步，认证可能失败。
        防止重放攻击：时间戳是防止数据包重放的重要依据，时间不一致会导致安全漏洞。

3: 日志管理和故障排查
        日志对比: 在多台服务器上排查问题时，需要通过日志时间线分析故障原因。如果时间不同步，日志无法对齐，排查问题变得困难。
        事件追踪: 跟踪用户行为、事务处理等需要精确的时间戳。

....
```

### 1.2 NTP同步服务器原理

获取系统时间的基本命令：

```
date
```

获取系统时间并定制时间的显示格式：

```
date +"%F"                年月日
date +"%T"                时分秒
date +"%F %T"             年月日 时分秒
# 其他格式，如%Y年，%m月，%d日，%H时，%M分，%S秒
# 例如: date  +"%Y-%m-%d %H:%M:%S"
# 输出: 2024-12-26 14:49:31
```

问题：当Linux系统时间出现混乱时，我们如何校对这个时间？答：通过标准时间

标准时间是哪里来的？

现在的标准时间是由原子钟报时的国际标准时间UTC（Universal Time Coordinated，世界协调时)，所以NTP获得UTC的时间来源可以是原子钟、天文台、卫星，也可以从Internet上获取。

在NTP中，定义了时间按照服务器的等级传播，**Stratum层的总数限制在15以内**

工作中，**通常我们会直接使用各个组织提供的，现成的NTP服务器**

![[附件/c6b903b7e1.png]]

### 1.3 获取国内最稳定的NTP服务器

到哪里去找NTP服务器？答：可以通过NTP授时网站：http://www.ntp.org.cn/

![[附件/8d66d37236.png]]

如何查看当前我们的服务器采用的那个NTP服务器来完成的同步呢?

```
查看当前正在使用的时间源: chronyc sources
```

![[附件/4ac61437d7.png]]

```
MS：显示时间源的同步状态：
    +：表示候选的时间源
    *：表示当前服务器正在使用的时间源
    -：表示时间源可用，但未被选中
    ?：表示无法与时间源通信或时间源无效
Name/IP address： 显示时间源的域名或 IP 地址，例如 time.neu.edu.cn

Stratum：显示时间源的层级：
    层级 1 表示直接连接到原子时钟的服务器
    层级 2 表示从层级 1 的服务器同步，依此类推

Poll：显示时间同步的轮询间隔，以秒为单位的指数（如 6 表示 2^6 = 64 秒轮询一次）

Reach：表示与时间源的通信状态，8 位二进制值（显示为八进制）
        377 表示最近的 8 次尝试均成功（满分状态），值越低表示通信失败次数越多

LastRx：显示上一次从该时间源接收数据的时间（以秒为单位）

Last sample： 显示上一次时间样本的偏差值（单位为微秒 us 或毫秒 ms），格式为 [偏差] +/- [精度] 方括号中的值是未经校正的时间偏差
```

检查同步状态: 系统当前时间同步的详细信息

```
chronyc tracking

结果为:
Reference ID    : CA760151 (time.neu.edu.cn)  这是系统当前正在同步的时间源的标识符。

Stratum         : 3 表示时间源的层级

Ref time (UTC)  : Tue Dec 24 16:30:58 2024  这是当前时间源提供的参考时间（UTC，协调世界时）。表示 time.neu.edu.cn 服务器最后一次更新时间的时刻

System time     : 0.000350876 seconds fast of NTP time  表示当前系统时间与 NTP 时间之间的偏差。这个值表示系统时间比 NTP 时间快了 0.000350876 秒。

Last offset     : +0.000258952 seconds  上一次时间同步时的偏差，表示系统时钟与 NTP 服务器时间的差值。此值为正，意味着系统时间在上次同步时比 NTP 时间快了 0.000258952 秒

RMS offset      : 0.001568094 seconds RMS (Root Mean Square) 偏差，表示系统时钟与 NTP 服务器时间之间的平均偏差。该值越小，表示时间同步越准确。

Frequency       : 8.446 ppm fast  频率偏差，表示系统时钟的增速或减速。ppm 是 "每百万分之一"（parts per million）的单位。

Residual freq   : +0.031 ppm 剩余频率偏差，表示调整后系统时钟的频率偏差。+0.031 ppm 表示系统时钟仍然比 NTP 时间快 0.031 个百万分之一。

Skew            : 1.666 ppm 时钟偏差的变化率，即时钟偏差变化的速率。如果这个值较大，表示系统时钟的频率不稳定，可能需要更频繁地进行同步。

Root delay      : 0.023006978 seconds 根延迟，指从本地系统到时间源服务器的网络延迟。0.023 秒表示从本机到 time.neu.edu.cn 服务器的往返延迟。

Root dispersion : 0.000833949 seconds 根扩散，表示时间源的不确定性，指的是时间源本身的误差范围。这个值越小，表示时间源的精度越高。

Update interval : 129.9 seconds 更新时间间隔，表示系统每次同步时间的间隔。129.9 秒表示大约每 2 分钟同步一次。

Leap status     : Normal 跳秒状态，表示当前是否有跳秒调整。Normal 表示没有发生跳秒调整。
```

![[附件/ae3ac39cf4.png]]

### 1.4 chrony时间同步服务

Chrony 是一个高效的时间同步服务，主要用于在 Linux 系统中通过网络时间协议 (NTP) 进行时间同步。

特点:

- **轻量高效：**

- 启动速度快，适合间歇性连接到网络的设备。

- **低延迟**：

- 在不需要长期运行的环境中，快速同步时间。

- **适配性强**：

- 支持虚拟化环境（如虚拟机）和频繁断网的设备。

#### 1.4.1 安装与基本配置

Chrony 通常默认安装在 CentOS Stream 9 上。如果未安装，可以通过以下命令安装：

```
dnf install chrony -y
```

设置开机启动

```
systemctl start  chronyd
systemctl enable  chronyd

查看状态: systemctl status  chronyd
```

![[附件/ea3b7fe159.png]]

---

Chrony 的配置文件位于 `/etc/chrony.conf`，可以通过编辑该文件来调整时间源、访问权限等。

```
vim /etc/chrony.conf

默认内容如下:
# 配置 chronyd 使用 pool.ntp.org 提供的公共时间源进行同步
# pool：使用多个时间源进行负载均衡。
# iburst：当服务器不可达时，发送 4 个快速请求包以加速连接。
# 2.centos.pool.ntp.org  ntp服务器地址
pool 2.centos.pool.ntp.org iburst

# 从 DHCP 服务中动态获取 NTP 服务器地址,如果是静态网络可忽略
sourcedir /run/chrony-dhcp

# 记录系统时钟的频率偏差（增/减速），以便重启后快速调整。
driftfile /var/lib/chrony/drift

# 允许 chronyd 在系统启动的前 3 次同步中直接调整时间（如果时间偏差超过 1 秒）。
makestep 1.0 3

# 启用系统时钟与硬件时钟 (RTC) 的自动同步。
rtcsync

# 启用支持硬件时间戳的网络接口。注释掉，通常用于高精度时间同步场景（如金融行业）。
#hwtimestamp *

# 设置最少需要的时间源数量。
# 默认状态：注释掉，chronyd 自动选择。
#minsources 2

# 允许指定 IP 段的设备访问本机时间服务。默认不支持
#allow 192.168.0.0/16

# 允许本机在没有时间源时，充当时间服务器（Stratum 10）。一般注释掉
#local stratum 10

# 启用 NTP 数据包的认证功能。 注释掉，如使用,需生成密钥文件 /etc/chrony.keys。
#authselectmode require
keyfile /etc/chrony.keys

# 用于指定存储 NTS（Network Time Security）密钥和 cookie 的目录。
ntsdumpdir /var/lib/chrony

# 通过调整时间速度而非直接跳秒的方式插入/删除闰秒。
#leapsecmode slew

# 从系统时区数据库中获取闰秒和 TAI-UTC 偏移信息。
leapsectz right/UTC

# 指定 Chrony 的日志存储路径。
logdir /var/log/chrony
# 启用更多日志 如果需要记录时间同步详细信息，可取消注释以下选项
#log measurements statistics tracking
```

#### 1.4.2 实施配置操作

需求如下: 基于原有的node1服务器

```
1- 完成调整公共时间源, 使用 中国国家授时中心时间服务器 阿里云和腾讯云提供的统一ntp服务
ntp.org.cn(中国国家授时中心时间服务器)
ntp.aliyun.com(阿里云NTP时间服务器)
ntp.tencent.com(腾讯云NTP时间服务器)

2- 开启允许局域网访问, 统一为 192.168.88.0/24 开放

3- 启用详细日志

4- 打开 硬件时钟同步

5- 让node2连接node1完成时间同步
```

实现操作：

- 1- 修改 node1的ntp核心配置文件

```
vim /etc/chrony.conf

修改以下内容：
# 注释掉原有的pool 新增三个pool (文件头部)
# pool 2.centos.pool.ntp.org iburst
pool ntp.org.cn iburst
pool ntp.aliyun.com iburst
pool ntp.tencent.com iburst

# 新增（第31行范围）
allow 192.168.88.0/24

# 新增（最后一行）
log measurements statistics tracking
```

- 2- 重启node1的NTP服务

```
systemctl restart chronyd
systemctl status chronyd
```

![[附件/7a728417cc.png]]

- 3- 校验是否生效：

![[附件/34fcd15d40.png]]

- 4- node1开放ntp防火墙

```
firewall-cmd --add-service=ntp --permanent
firewall-cmd --reload

firewall-cmd --list-all
```

![[附件/804dacf79b.png]]

- 5- node2 修改NTP核心配置文件

```
vim /etc/chrony.conf

修改以下内容：
# 注释掉原有的pool 新增一个pool (文件头部)
# pool 2.centos.pool.ntp.org iburst
pool 192.168.88.101 iburst


:x 保存退出
```

- 6- 重启node2的NTP服务

```
systemctl restart chronyd
systemctl status chronyd
```

- 7- 查看是否生效：

```
chronyc sources
```

![[附件/662f356234.png]]

### 1.5 【实战】完成多台服务器时间同步

公司内部有三台服务器, 需要我们进行时间同步配置操作, 公司要求,仅支持一台服务器可以连接外网获取时间, 另外的服务器均无法直接连接外部网络获取标准时间, 需要我们来进行配置

```
分析: 共计有三台服务器
    其中 一台服务器可以连接外部网络, 另外二台是无法连接外部网络
           一台服务器采用NAT上网方案
           另外两台服务器采用仅主机模式
    
    另外二台服务器需要连接 第一台服务器完成时间同步, 二台服务器要和第一台服务器进行互通
```

- 先准备三台服务器

![[附件/96b47c4efc.png]]

- 接着配置: 时间同步操作[与上面的案例一致]

## 2. Linux的SELinux深层防火墙

**SELinux（Security-Enhanced Linux）** 是一种强制访问控制（MAC）机制，提供了比传统的基于用户和组的权限控制（DAC）更强的安全性。它通过定义策略来限制进程对系统资源的访问，而不仅仅依赖文件系统权限。

用大白话来说，**SELinux 就是 Linux 系统的一套“安全防护网”，防止系统里的程序“胡作非为”**。它会根据提前写好的“规则表”（叫策略），限制每个程序能做什么，不能做什么。

举个例子：

- 假设你家有一间屋子，房东给了你钥匙，但是他还设了规矩：**你只能在客厅活动，不能进卧室和厨房。**
- 房东的这套规矩就是 SELinux 的“规则表”。
- 即使你有钥匙（就像程序有了权限），你也不能随意进屋的其他地方，因为房东（SELinux）会盯着你，一旦发现你不守规矩，就会阻止你。

SELinux 的目的就是：**即使黑客成功攻击了一个程序，他也无法轻易破坏整个系统，因为 SELinux 会限制这个****程序****的“活动范围”。**

### 2.1 SELinux配置和管理

- 查看 SELinux 状态：

```
sestatus
```

![[附件/2e99565770.png]]

- 临时切换 SELinux 模式： SELinux 具有三种工作模式：

- **Enforcing**：强制执行 SELinux 策略。
- **Permissive**：仅记录违反策略的行为，但不强制执行。
- **Disabled**：禁用 SELinux。

要临时切换 SELinux 模式（例如，切换为宽松模式以便调试）：

```
sudo setenforce 0  # 切换为 Permissive 模式
sudo setenforce 1  # 切换为 Enforcing 模式
```

- 查看和修改 SELinux 配置文件： 配置文件 `/etc/selinux/config` 用于设置系统的默认 SELinux 模式。

修改该文件中的 `SELINUX` 参数，设置为 `enforcing`、`permissive` 或 `disabled`，然后重启系统使设置生效。

```
vim /etc/selinux/config
```

![[附件/32a7afee3b.png]]

- 查看 SELinux 日志： SELinux 的相关日志通常存储在 `/var/log/audit/audit.log` 文件中。
- 可以使用 `ausearch` 或 `sealert` 工具来分析日志，排查访问控制问题。

```
ausearch -m avc
```

- SELinux 管理工具： 提供了如 `semanage`、`restorecon`、`chcon` 等工具，用于管理和调整 SELinux 策略。

- `semanage`：管理 SELinux 策略，如允许或禁止特定的端口、文件类型等。
- `restorecon`：恢复文件的 SELinux 上下文。
- `chcon`：修改文件的 SELinux 上下文。
- audit2allow: 帮助解析 SELinux 日志并自动生成允许或调整的 SELinux 策略规则

示例：将一个文件的 SELinux 上下文恢复为默认：

```
restorecon /path/to/file
```