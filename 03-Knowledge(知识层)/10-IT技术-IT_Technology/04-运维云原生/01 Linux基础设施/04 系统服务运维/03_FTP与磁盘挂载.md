## 1. FTP相关内容

### 1.1. 文件传输协议FTP

FTP（File Transfer Protocol） 是一种用于在网络上进行文件传输的协议，允许用户通过客户端和服务器之间上传、下载文件。

![[附件/958af2917d.png]]

### 1.2. FTP的两种工作模式

- 1- 主动模式（Active Mode）

- 在主动模式下，**客户端** 发起控制连接到服务器，而服务器用来传输数据的端口是由 **服务器** 发起的连接到客户端。
- 工作流程：

```
1- 客户端与服务器之间建立 控制连接，通常是通过端口 21（即 FTP 的默认控制端口）

2- 当客户端准备接收数据时，它会通过 随机端口（通常是 20 以外的端口）向服务器请求建立数据连接

3- 服务器通过控制连接得知客户端的端口号后，从端口 20（服务器的 FTP 数据端口） 发起一个连接到客户端指定的端口，用于数据传输
```

![[附件/c17f38d54e.png]]

![[附件/2025c69784.png]]

- 优势：

```
服务器主动向客户端发起数据连接，通常对大多数服务器来说，这种方式较容易实现。
```

- 弊端：

```
因为客户端通常位于防火墙或 NAT 后面，防火墙可能阻止来自服务器的外部连接，所以这种模式可能会受到网络环境的限制，尤其在客户端位于 NAT 后时，可能无法建立连接。
```

- 2- 被动模式（Passive Mode）

- 在被动模式下，**客户端** 仍然发起控制连接，但在传输数据时，**客户端** 会请求服务器开放一个随机的端口来进行数据传输，服务器只负责监听数据连接，客户端主动发起连接。
- 工作流程：

```
客户端与服务器之间建立 控制连接（通常是端口 21）。
客户端请求服务器在某个端口（一个随机端口）上等待数据连接。
服务器响应并告知客户端该数据端口号。
客户端随后向该端口发起连接进行数据传输。
```

![[附件/90f0e98f00.png]]

- 优点:

```
被动模式能更好地穿越防火墙和 NAT，因为所有连接都是由客户端发起的，服务器只是监听连接，不会主动连接客户端。
```

- 弊端

```
需要服务器配置和开放更多的端口（通常是端口范围），可能会导致一些安全隐患。
```

区别说明：

|   |   |   |
|---|---|---|
|特性|主动模式（Active Mode）|被动模式（Passive Mode）|
|控制连接|客户端连接服务器的端口 21|客户端连接服务器的端口 21|
|数据连接|服务器从端口 20 发起连接到客户端的随机端口|客户端连接服务器提供的随机端口|
|适用网络环境|客户端需要有公网 IP 或不在防火墙后|客户端位于 NAT 或防火墙后时较为适用|
|防火墙问题|可能无法穿越客户端防火墙或 NAT|由于客户端发起数据连接，较易穿越防火墙|

总结：

- **主动模式**：服务器发起数据连接，适合客户端有公网 IP 的情况，但可能受到客户端防火墙或 NAT 的限制。

- 需要感知到客户端 公网ip
- 防火墙会导致连接失败

- **被动模式**：客户端发起数据连接，适用于客户端位于防火墙或 NAT 后时，能够绕过这些网络限制，安全性和兼容性更高。

- 服务器开放更多端口 安全性下降
- 只要用户连接服务器即可

### 1.3. FTP服务器搭建

准备二台服务器，一台用于客户端（node1），另一台用于服务端（node2）

#### 1.3.1. 服务端配置

- 1- 第一步：在node2上安装vsftpd服务（FTP服务器）

```
dnf install vsftpd
```

- 2- 第二步：启动并配置 **vsftpd** 服务

```
systemctl start vsftpd
systemctl enable vsftpd
# 校验
systemctl status vsftpd
```

![[附件/a3a35b3be4.png]]

- 3- 第三步： 配置防火墙

```
firewall-cmd --permanent --add-service=ftp
firewall-cmd --reload

# 校验
firewall-cmd --list-all

注意： 如果直接将防火墙彻底关闭，此部分可以跳过
```

![[附件/f005670c64.png]]

- 4- 第四步： 基本访问配置

```
前置：创建一个用于共享的目录,已经在目录下创建几个文件
mkdir -p /anon
echo 'hello' >> /anon/a.txt
echo 'hi' >> /anon/b.txt

修改配置：
vi /etc/vsftpd/vsftpd.conf

设置以下几个配置项：
anonymous_enable=YES # 允许匿名用户访问
anon_root=/anon   # 设置匿名用户默认的根目录 
anon_upload_enable=YES # 允许匿名用户上传文件
anon_mkdir_write_enable=YES  # 允许匿名用户创建文件夹
anon_other_write_enable=YES  # 允许匿名用户删除和重命名文件

注意：修改配置文件， 记得重启下FTP服务
systemctl restart vsftpd

# 校验：
systemctl status vsftpd
```

#### 1.3.2. 客户端配置

- 1- 第一步： 在node1上安装FTP客户端

```
dnf install lftp
 
 说明：
    安装 lftp（命令行 FTP 客户端）或 FileZilla（图形化客户端）
    
    我们是无界面化的，故安装lftp即可
```

- 2- 第二步：连接FTP服务器

```
lftp ftp://192.168.88.102
```

![[附件/0e794a45c1.png]]

#### 1.3.3. windows浏览器访问

- 1- 打开windows文件资源管理器（window + e）

![[附件/186cf0b4c4.png]]

- 2- 地址栏中输入：

```
ftp://192.168.88.102
```

![[附件/e3ba9b6ce6.png]]

创建文件夹：

![[附件/2d982d20ec.png]]

上传文件：

在node2上创建一个目录，并设置权限为777，允许所有人有对文件夹的全部权限

目前使用的是匿名用户 如果新增修改操作 用户需要在服务器有对应权限

```
mkdir -p /anon/test01
chmod 777 -R /anon/test01/
```

![[附件/bf037e2f18.png]]

![[附件/8ca7e079bb.png]]

![[附件/fd3d8cfdf7.png]]

### 1.4. 禁止匿名用户访问

- 第一步：在 node2 修改FTP的相关配置

```
vi /etc/vsftpd/vsftpd.conf

修改以下配置：
anonymous_enable=NO  # 禁用匿名用户访问

local_enable=YES # 允许本地用户登录
write_enable=YES # 允许写入操作（上传文件）

保存文件并退出，重启服务
systemctl restart vsftpd
```

- 2- 第二步： 创建一个普通用户用于后续访问FTP 【可选】

- 由于开启了允许本地用户访问， 但是系统中仅有一个root超级用户， 故需要创建普通用户，便于客户端连接（注意：由于root用户权限过高，FTP无法直接使用root来让客户端访问）

```
useradd smartgouser

echo 123 | passwd --stdin smartgouser


--stdin 参数允许 passwd 命令从标准输入读取新密码，而不是交互式提示
```

- 3- node1 客户端访问查看

```
格式：
lftp ftp://用户名[:密码]@ftp服务器主机地址

示例：
lftp ftp://smartgouser:123@192.168.88.102
```

![[附件/7a444a7864.png]]

![[附件/17a9cf3627.png]]

一旦登录成功后， 即可使用该账号来操作文件系统了， 此时可以理解为该用户直接访问了对应服务器系统， 只要这个用户对相关的文件或目录有权限， 即可进行直接操作（依赖与该用户在服务器的权限）

### 1.5. 禁锢在指定的数据目录中

- 1- 创建一个本地用户的数据目录 【node2】

```
mkdir -p /data/kefu

说明： 该目录将会作为共享上下传目录
```

- 2- 修改配置文件

```
vi /etc/vsftpd/vsftpd.conf

# 添加以下内容
local_root=/data/kefu   # 设置默认访问的路径地址 ,如果不指定， 默认访问的是该用户的家目录
# 修改以下内容： 前面的#去除即可
chroot_local_user=YES  # 限制所有本地用户（即服务器上的普通用户）只能访问他们的 home 目录

保持退出后，重启vsftpd服务
systemctl restart vsftpd
```

![[附件/f633add776.png]]

- 3- 创建用户， 指定用户的家目录为禁锢的数据目录下

```
useradd -m  ftpuser

echo 123 | passwd --stdin ftpuser
```

- 4- 客户端测试访问

```
lftp ftp://ftpuser:123@192.168.88.102
```

![[附件/0406787f52.png]]

---

通过上述的配置，可以将所有的用户禁锢在指定的目录下， 但是某些特殊的用户需要具备访问其他目录的权限， 如何办呢？

```
步骤一： 修改配置文件 
vi /etc/vsftpd/vsftpd.conf

步骤二： 修改以下配置 （打开对应行注释即可）
chroot_list_enable=YES   # 开启允许访问其他的目录的功能
# (default follows)
chroot_list_file=/etc/vsftpd/chroot_list  # 设置那些用户可以例外，需要将可以例外的用户放置到 /etc/vsftpd/chroot_list文件中


步骤三： 编辑 /etc/vsftpd/chroot_list 文件
vi /etc/vsftpd/chroot_list

输入i 进入插入模式

然后添加需要例外的用户名即可， 一个用户名为一行，例如添加 itheima
itheima


添加后， :x 保存退出即可


步骤四： 重启vsftpd. 重启后测试使用
```

### 1.6. 用户名单列表使用

把上一实验中禁锢用户数据目录功能关闭后再做下面的实验

操作方式， 将 禁锢操作中相关配置前面全部添加 # (表示注释)

- 观察现象： 当采用root直接访问ftp服务

![[附件/1b51dd3db6.png]]

会被拒绝访问， 权限不够，原因： FTP默认不允许root访问

在node2中的/etc/vsftpd目录下，有二个文件：ftpusers和user_list，主要是用来控制哪些用户可以或不能访问 FTP 服务，管理用户访问权限，防止某些用户登录FTP服务器

- ftpusers 文件：`ftpusers` 文件用于列出不允许访问 FTP 服务的用户。任何列在这个文件中的用户都将被拒绝登录到 FTP 服务器，即使这些用户的用户名和密码是正确的

![[附件/78b35dcbb3.png]]

- user_list文件：`user_list` 文件的作用和 `ftpusers` 文件相似，但有一些区别。`user_list` 文件控制哪些用户可以访问 FTP 服务，具体取决于配置文件中 `userlist_enable` 和 `userlist_deny` 的设置

- **userlist_enable=YES** 启用或禁用 `**vsftpd**` 服务的**系统用户列表**功能。
- **userlist_deny=YES** 默认情况下，列在 `user_list` 文件中的用户会被拒绝访问。
- **userlist_deny=NO** 列在 `user_list` 文件中的用户将被允许访问，除非在 `ftpusers` 中显式禁止。

![[附件/8a6cd5adb2.png]]

应用场景： 通过这两个文件，可以为FTP服务器设置黑名单和白名单用户

需求： 将root从黑名单释放出来，允许root用户正常访问

- 1- 开启白名单功能

```
vi /etc/vsftpd/vsftpd.conf

# 修改以下内容：
userlist_enable=YES  # 开启user_list权限设置功能

# 添加一下内容：
userlist_deny=NO   # 开启白名单，运行文件中的用户


保存后，重启一下FTP服务
systemctl restart vsftpd
```

![[附件/08d77ac431.png]]

- 2- 在ftpusers 文件（黑名单）中去除root用户

![[附件/7bbb0a7313.png]]

- 3- 访问FTP服务器

```
lftp ftp://root:123456@192.168.88.102
```

![[附件/128a75d307.png]]

### 1.7. 常见错误

vsftpd: refusing to run with writable root inside chroot()

![[附件/cd833fdcd5.png]]

```
说明： 此错误表示的当前FTP文件系统的根目录的权限过大，存在写权限， 一般就会爆出如上错误， 因为FTP默认情况下，不允许文件系统根目录存在写权限， 以保证根目录的文件安全（根目录下可能会放置一些系统文件信息， 担心出现破坏）
```

![[附件/7105017c7c.png]]

```
当在ftp中看到550错误的时候， 一般就是当前这个用户没有权限操作这个文件或目录，如果想要操作， 请赋予相应权限
```

### 1.8 如何删除ftp服务

```
node1: 
    dnf -y remove lftp
    dnf clean all

node2:
    dnf -y remove vsftpd
    dnf clean all
    rm -rf /etc/vsftpd/
    
    firewall-cmd --permanent --remove-service ftp
    firewall-cmd --reload
    firewall-cmd --list-all
    
    rm -rf /anon
    userdel -rf smartgouser
    userdel -rf ftpuser
```

### 1.9 综合案例

操作案例之前，请先将node1和node2关于ftp的相关内容全部删除

需求：

```
1- 请将node1作为ftp的服务器， node2为ftp的客户端，并完成服务端ftp和客户端ftp的安装操作

在node1执行：
    dnf -y install vsftpd
    # 启动服务
    systemctl start vsftpd
    systemctl status vsftpd
在node2执行：dnf -y install lftp


2- FTP服务器要求如下：
    2.1 不允许匿名用户访问
    2.2 将用户禁锢在 /export/public 目录下
    2.3 在FTP服务器端的/export/public目录下， 创建logs、src目录，并将目录的权限所有用户设置写入权限
    2.4 在客户端的家目录下， 创建 a.log   hello.java文件， 并将这两个文件通过ftp客户端上传到服务器刚刚创建的logs和src目录， a.log放置到logs目录， hello.java放置到src目录
    2.5 设置黑白名单： 
            在服务器端 创建 zhangsan lisi wangwu 三个用户， 并设置密码均为123456
            将zhangsan放置到黑名单，lisi和wangwu用户放置到白名单， 验证zhangsan无法访问，lisi和wangwu可以正常访问
            
服务器端的操作：
node1执行：
    # 创建禁锢的目录
    mkdir -p /export/public
    # 完成需求2.3
    cd /export/public
    mkdir -p logs src
    chmod a+w logs
    chmod a+w src
    # 完成需求2.5 服务器添加用户
    useradd zhangsan
    useradd lisi
    useradd wangwu
    passwd zhangsan
    passwd lisi
    passwd wangwu
    
vsftpd.conf中：
    # 需求2.1 ： 禁用匿名登录
    anonymous_enable=NO
    local_enable=YES
    write_enable=YES
    
    # 需求 2.2 禁锢操作
    local_root=/export/public
    chroot_local_user=YES
    
    # 需求2.3 黑马名单设置
    # 修改配置， 开启白名单
    userlist_enable=YES
    userlist_deny=NO

黑白名单文件设置：    
    # 注意： 一定要使用 >> 追加的方式
    echo 'wangwu' >> /etc/vsftpd/ftpusers
    echo 'lisi' >> /etc/vsftpd/user_list
    echo 'lisi' >> /etc/vsftpd/user_list
    

完成后： 记得重启vsftpd服务器
systemctl restart vsftpd
systemctl status vsftpd

最后，防火墙放行 ftp服务
firewall-cmd --add-service ftp --permanent
firewall-cmd --reload
firewall-cmd --list-all



客户端操作：
node2执行：
    cd ~
    touch a.log hello.java
    
    # 通过ftp客户端上传文件到ftp服务器
    lftp ftp://lisi:123456@192.168.88.101
    # 执行上传
    put ~/a.log -o /logs/
    put ~/hello.java -o /src/
    
    
    注意：
        由于我们已经在服务端设置禁锢操作，将用户已经锁定到/export/public目录下， 所以当客户端登录成功后， 其实就已经进入/export/public中， 客户端会直接将此目录当做为根目录操作， 在客户端中 我们的/ 其实表示的就是/export/public
```

提示上传命令为：

```
put 本地路径 -o 远端的路径

注意：路径不需要带地址， 直接写对应的路径即可

例如：node1是服务器端  node2是客户端 将node2的家目录下的hello.java 上传到 logs目录
# 因为 /export/public 本身就是根目录
put ~/hello.java -o logs/
```

## 2. 磁盘挂载命令(mount)

![[附件/e2531fb85b.png]]

`mount` 命令用于将设备（如硬盘、分区、网络文件系统等）挂载到文件系统中

- 挂载设备到指定目录

```
挂载命令的基本格式为：

mount <设备> <挂载点>

示例: 挂载硬盘分区 /dev/sda1 到 /mnt 目录
mount /dev/sda1 /mnt
```

- 挂载指定文件系统类型

```
可以使用 -t 选项指定文件系统类型（如 ext4、xfs、ntfs 等）。如果未指定类型，系统会自动检测。

挂载一个 NTFS 格式的设备：
mount -t ntfs /dev/sdb1 /mnt
```

- 挂载使用特定选项

```
可以使用-o来设置来控制挂载的行为，如 ro（只读）、rw（读写）、noexec（禁止执行）、user（允许普通用户挂载）等。

挂载为只读模式：
mount -o ro /dev/sda1 /mnt
使用用户选项挂载（允许普通用户挂载）:
mount -o user /dev/sda1 /mnt
```

- 查看和配置 `/etc/fstab`【永久】

`/etc/fstab` 是一个配置文件，包含了系统在启动时自动挂载的文件系统信息。你可以编辑该文件来设置自动挂载的设备和选项。

```
示例

vim /etc/fstab
在此文件中，添加一行：
/dev/sda1  /mnt  ext4  defaults  0  0

这表示系统启动时会自动挂载 `/dev/sda1` 到 `/mnt`，使用 `ext4` 文件系统。

/dev/sda1：设备名称。
/mnt/data：挂载点目录。
ext4：文件系统类型。
defaults：挂载选项（默认设置：读写模式、同步、允许执行文件等）。
0 0：
第一位 0：是否需要转储备份，通常设置为 0。
第二位 0：是否检查文件系统，0 表示不检查，1 表示优先检查根文件系统，2 表示检查其他文件系统。
```

- 卸载设备

使用 `umount` 命令卸载设备。需要指定挂载点或设备。

```
示例： 卸载 /mnt 目录上的设备：
umount /mnt
```

- 查看和监控挂载信息

使用 `df` 或 `lsblk` 命令查看挂载的设备和磁盘使用情况。

```
查看磁盘空间使用情况：
df -h

查看磁盘和分区信息：
lsblk
```

## 3. 【案例】挂载一块新磁盘

建议： 挂载操作建议重新克隆一台新的服务器来学习， 如果服务器损坏了， 直接删除重新再克隆即可

### 3.1. 在VMware中增加一块磁盘

![[附件/e6fc7ed9d4.png]]

![[附件/baf9a41dfc.png]]

![[附件/eb6831ee0a.png]]

![[附件/9eb41ece44.png]]

![[附件/cdffa44763.png]]

![[附件/0e398fc33a.png]]

### 3.2. 挂载

![[附件/3fd0f402a2.png]]

步骤一: 插入新磁盘后，首先用以下命令查看磁盘信息：

```
lsblk

如果没有看到新磁盘，运行以下命令重新扫描：
echo "- - -" > /sys/class/scsi_host/host0/scan
```

![[附件/bc07f19545.png]]

步骤二: 分区和格式化磁盘

```
fdisk /dev/nvme0n2


# /dev 是设备存储位置
```

![[附件/ca35194df3.png]]

输入 n 进行分区操作

![[附件/6b93dd4d79.png]]

输入w 保存分区

![[附件/4288087a49.png]]1

再次使用 lsblk 查看分区信息

![[附件/0b0f5b00a3.png]]

格式化分区: mkfs.xfs -f 磁盘名称

```
mkfs.ext4 是一个用来格式化分区为 EXT4 文件系统 的命令。EXT4（第四代扩展文件系统）是 Linux 系统中使用最广泛的文件系统类型，兼具性能、可靠性和兼容性，适用于大多数场景。

XFS 是一种高性能的日志文件系统，广泛用于企业级场景，特别是对大文件和高并发 I/O 的处理有明显优势。它是 CentOS Stream 9 等现代 Linux 发行版的默认文件系统类型
```

![[附件/d619e930a1.png]]

步骤三: 挂载磁盘

- 首先: 创建一个用于挂载磁盘的路径

```
例如:  将磁盘挂载到/mnt/data 目录下
mkdir -p /mnt/data
```

- 执行挂载操作:

```
mount /dev/nvme0n2p1 /mnt/data
```

后续将数据写入到/mnt/data目录下, 相当于写数据到新磁盘中存储了

挂载成功后， 也可以使用df -h 查看是否挂载成功

---

永久挂载: 为了让挂载在系统重启后仍然生效，需要将挂载信息写入 `/etc/fstab` 文件

方式一：基于UUID进行挂载

- 步骤一: 获取分区的 UUID

```
blkid /dev/nvme0n2p1
```

![[附件/054ee9f34d.png]]

- 步骤二: 编辑 `/etc/fstab` 文件

```
vim /etc/fstab

添加:
UUID=f6402f30-865f-4d46-b8a4-5b7d333aa502  /mnt/data  xfs  defaults  0  0

保存退出后， 使用 mount -a  来检查， 如果没有任何的提示， 说明配置文件正常，没有异常错误，然后才可以重启， 如果弹出信息， 说明有问题， 千万不要重启， 先解决问题
```

- 步骤三： 重启后, 通过df -h 查看是否依然存在

方式二： 基于磁盘的路径挂载

- 步骤一：需要查看磁盘的路径

```
lsblk
```

![[附件/d3816cabf7.png]]

```
在磁盘的名称前面，添加 /dev/磁盘分区名称  即可

建议写好后， 可以校验一下：
ll /dev/磁盘分区名称

如果可以查看到， 说明这个路径写对了
```

![[附件/8f2336954c.png]]

- 步骤二： 编辑 `/etc/fstab` 文件

```
vim /etc/fstab

添加:
/dev/磁盘分区名称  挂载点路径  xfs  defaults  0  0

保存退出后， 使用 mount -a  来检查， 如果没有任何的提示， 说明配置文件正常，没有异常错误，然后才可以重启， 如果弹出信息， 说明有问题， 千万不要重启， 先解决问题
```

### 3.3. 取消挂载

- 方式一： 临时取消

```
格式： umount 设备名/挂载点

示例：
umount /dev/nvme0n2p3


说明：
    如果该磁盘已经在/etc/fstab配置过了 此操作只能临时取消， 重启后就会自动恢复
```

- 方式二： 永久取消

```
通过 vi /etc/fstab 打开文件，将需要取消磁盘对应行之间删除即可， 如果想要保证当前和下次开机都没有， 可以将方式一和方式二同时执行即可
```

## 4. 磁盘挂载综合案例

需求： 请挂载一块40GB磁盘， 要求对磁盘划分2个区，一个区为10GB， 一个区为30GB （可以有微小出入），并将磁盘分别挂载到/mount/f1 和/mount/f2中，并配置好永久挂载方案。

**计算 10G 分区的结束位置：**

- **起始扇区**：2048
- **目标大小**：10GB = 10×1024×1024×1024 字节 = 10,737,418,240 字节

- G = 1024 M
- M = 1024 KB
- KB = 1024B

- **扇区大小**：通常为 512 字节（部分新硬盘为4096，但兼容模式多为512）
- **计算过程**：

1. 先算 10G 包含多少个扇区： 10,737,418,240÷512=20,971,52010,737,418,240÷512=20,971,520 个扇区。
2. 结束扇区 = 2048+20,971,520−1=20,973,5672048+20,971,520−1=20,973,567