# **Ansible配置自动化**（重点）

作用：掌握Ansible配置自动化工具，能实现多服务器批量管理！

# **一、场景说明**

## **1.** 任务背景

公司的服务器越来越多, 维护一些简单的事情都会变得很繁琐。用Shell脚本来管理少量服务器效率还行, 服务器多了之后Shell脚本无法实现高效率运维。这种情况下，我们需要引入自动化运维工具, 对多台服务器实现高效运维。

## **2.** 任务要求

通过管理服务器能够按照需求灵活高效地管理所有应用服务器的运维操作

## **3.** 任务拆解

① 需要一台服务器做管理端, 来连接管理所有的应用服务器

② 考虑如果只针对一部分应用服务器进行运维操作如何实现(服务器分组)

③ 学会将平台烂熟于心的Linux操作命令转化为自动化运维的方式(常见模块的学习)

④ 如果操作非常的冗长, 学会使用playbook和roles的方式来管理(自动化编排)

## **4.** 学习目标

① 能够安装ansible服务器和客户端

② 能够定义ansible主机清单进行服务器分组

③ 掌握常用模块使用

④ 了解playbook的编写

⑤ 能够使用playbook实现软件安装部署

⑥ 扩展ansible roles功能

简历体现技能：能通过Ansible/SaltStack自动化工具实现超大型服务器集群管理工作=>项目都可以体现Ansible这个技能点=>Ansible也可以单独作为一个项目（自动化运维管理）

# 二、Ansible环境搭建

## **5.** 自动化运维

问题：假设我要去1000台服务上做一个操作（如mysql数据库服务器修改配置文件里的某一个参数), 下面两种方法缺点明显:

第一种方案：按传统的方法, 一台连着一台服务器的ssh上去手动操作。

缺点: 效率太低。

第二种方案：写个Shell脚本来做。

缺点: 管理的机器平台不一致，脚本可能不具备通用性。传密码麻烦(在非免密登录的环境下, 需要expect来传密码)，效率较低，循环1000次也需要一个一个的完成，如果用&符放到后台执行，则会产生1000个进程。

第三种方案：自动化运维

将日常IT运维中大量的重复性工作，小到简单的日常检查、配置变更和软件安装，大到整个变更流程的组织调度，由过去的手工执行转为自动化操作，从而减少乃至消除运维中的延迟，实现"零延时"的IT运维。

## **6.** 自动化运维需要关注内容

假如管理很多台服务器，主要关注以下几个方面:

- 管理机与被管理机的连接(管理机如何将管理指令发送给被管理机)

- 服务器信息收集 (如果被管理的服务器有centos外还有其它linux发行版,如suse,ubuntu等。当你要做的事情在不同

OS上有所不同,你需要收集信息,并将其分开处理)

- 服务器分组：因为有些时候我要做的事情不是针对所有服务器,可能只针对某一个分组

- 管理内容的主要分类

- 文件目录管理 (包括文件的创建,删除,修改,查看状态,远程拷贝等)

- 用户和组管理

- cron时间任务管理

- yum源配置与通过yum管理软件包

- 服务管理

- 远程执行脚本

- 远程执行命令

## **7.** 常见运维工具对比

- puppet

- 基于ruby语言，成熟稳定。适合于大型架构，相对于ansible和saltstack会复杂些。

- saltstack

- 基于python语言，简单、并发能力比ansible要好, 需要维护被管理端的服务。如果服务断开，连接就会出问题。【需要维护被管理端】

- ansible

- 基于python语言。简单快捷，被管理端不需要启服务。直接走ssh协议,需要验证所以机器多的话速度会较慢。

## **8.** Ansible概述⭐

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773726473420-6c4efcde-78c0-4405-adb2-b851df6a4d6d.jpg "null")

ansible是一种由Python开发的自动化运维工具，集合了众多运维工具（puppet、cfengine、chef、func、fabric）的优点，实现了批量系统配置、批量程序部署、批量运行命令等功能。

特点：

- 部署简单

- 默认使用ssh进行管理，基于python里的paramiko模块开发

- 管理端和被管理端不需要启动服务

- 配置简单，功能强大，扩展性强

- 能过playbook(剧本)进行多个任务的编排
- ![[附件/47e71f8e7f.png]] Host1~HostN：被管理机（不需要额外安装任何服务，Ansible直接走SSH协议）
- Ansible=>ConnectionPlugins（连接插件）=>连接所有的被管理机（走SSH协议）
- **HostInventory：主机清单（就是通过一个配置文件把所有被管理机进行分组，如分成web组、mysql组、redis组等等）**
- **Modules：CoreModules（核心模块）、CustomModules（自定义模块）=>重点学习内容=>通过模块实现管理被管理机（copy模块=>文件上传、user模块可以进行用户管理、yum模块实现管理安装卸载...）**
- **Plugins：插件，连接被管理机，结合email邮件、logging日志等实现一些额外功能**
- Playbook：剧本（演电影都要有剧本），把我们管理工作变成剧本，可以Ansible可以有逻辑的执行
- Users：用户管理，由于Ansible底层走SSH协议，所以连接被管理机，要么通过账号+密码，要么通过（Public/Private）免密操作

大致流程：Ansible首先需要配置主机清单（配置要连接机器以及进行提前分组），然后通过Connection连接插件连接所有的被管理机，底层走SSH协议，连接后，可以通过模块以及插件的方式对所有被管理机进行管理操作。针对于复杂的业务场景，还可以配合Playbook、Roles实现任务编排（让任务有逻辑的执行），这个就是Ansible核心原理了。

## **9.** Ansible环境搭建

实验准备: 三台机器，一台管理，两台被管理

|   |   |   |
|---|---|---|
|编号|IP|角色|
|node1|192.168.88.101|管理机master|
|node2|192.168.88.102|被管理机1|
|node3|192.168.88.103|被管理机2|

配置说明：

- 静态ip -

- 主机名及IP互相绑定 - /etc/hosts

- 关闭防火墙, selinux -vim /etc/selinux/config
- 安装 vim rsync wget

- 时间同步 [CentOS9时间同步](https://www.yuque.com/yeyunbingyang/nf463c/btmg1kinst407cs2 "CentOS9时间同步")

- dnf install -y chrony
- sudo systemctl enable --now chronyd
- sudo vi /eyt/chrony.config

- 绑定时间服务器

- 重启
- date验证

- 确认和配置yum源

全服务器时间同步：

```
# dnf install epel-release -y
# dnf install ntpsec -y
# ntpdate cn.ntp.org.cn
```

第1步: 管理机上安装ansible，被管理节点必须打开ssh服务

注意：ansible不需要再每一台机器上安装，只需要在node1主节点安装即可。

node1服务器：

CentOSStream9中，早期版本中镜像仓库自带了ansible。新版本仓库进行了更新，移除了ansible软件。所以软件安装需要通过epel-release扩展镜像仓库实现。

```
# yum install ansible -y
# ansible --version
ansible [core 2.14.17]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.9/site-packages/ansible
  ansible collection location = /root/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.9.19 (main, Aug 23 2024, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] (/usr/bin/python3)
  jinja version = 3.1.2
  libyaml = True
```

在 **CentOS** **Stream** **9 /** **10**之后：

- `ansible`（老包） ❌ 已被废弃
- 官方推荐使用：

```
ansible-core

dnf install ansible-core -y
```

第2步: 实现master对agent的免密登录，只在master上做。(如果这一步不做，则在后面操作agent时都要加-k参数传密码;或者在主机清单里传密码)

```
master# ssh-keygen
master# ssh-copy-id 192.168.88.102
master# ssh-copy-id 192.168.88.103
```

如果是CentOS7采用ssh-copy-id -i IP地址，如果CentOS Stream 9系列，要去掉-i参数，否则报错！！！

第3步: 在master上定义主机组,并测试连接性

```
master# vim /etc/ansible/hosts 

主机清单设置
[group1]
192.168.88.102
192.168.88.103
或
[group1]
192.168.88.[100:200]

-m 代表模块 => module

master# ansible -m ping group1
192.168.88.103 | SUCCESS => {
  "changed": false, 
  "ping": "pong"
}

192.168.88.102 | SUCCESS => {
  "changed": false, 
  "ping": "pong"
}   
```

```
master# ansible -m ping all
192.168.88.103 | SUCCESS => {
  "changed": false, 
  "ping": "pong"
}

192.168.88.102 | SUCCESS => {
  "changed": false, 
  "ping": "pong"
}
```

## **10.** 服务器分组（重点理解）

[https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)

Ansible通过一个"主机清单"功能来实现服务器分组。

Ansible的默认主机清单配置文件为`/etc/ansible/hosts`

案例1：

[起始值:结束值]，包含起始值也包含结束值【重点】

```
[nginx]					组名
apache[1:10].aaa.com	表示apache1.aaa.com到apache10.aaa.com这10台机器
nginx[a:z].aaa.com		表示nginxa.aaa.com到nginxz.aaa.com共26台机器
192.168.88.[161:165]	表示192.168.88.161到192.168.88.165这5台机器
```

案例2：非默认ssh端口

```
[nginx]
10.1.1.13:2222			表示10.1.1.13这台，但ssh端口为2222
```

案例3：定义10.1.1.12:2222这台服务器的别名为nginx1

```
nginx1 ansible_ssh_host=10.1.1.13 ansible_ssh_port=2222
```

案例4：没有做免密登录的服务器可以指定用户名与密码 => paramiko模块【记住】

```
nginx1 ansible_ssh_host=10.1.1.13 ansible_ssh_port=2222 ansible_ssh_user=root ansible_ssh_pass="123456"

注意：
nginx1别名
ansible_ssh_host：要连接的主机的IP地址
ansible_ssh_port：ssh对应的端口号
ansible_ssh_user：用户名
ansible_ssh_pass：密码
```

补充：

临时：ANSIBLE_HOST_KEY_CHECKING=False ansible -m ping nginx1

永久：ssh-keyscan -H 192.168.88.104 >> ~/.ssh/known_hosts

案例5：

```
nginx1  ansible_ssh_host=10.1.1.13 ansible_ssh_port=2222 ansible_ssh_user=root ansible_ssh_pass="123456"
nginx2  ansible_ssh_host=10.1.1.12 ansible_ssh_port=3333 ansible_ssh_user=root ansible_ssh_pass="123456"
 
[nginx]
nginx1
nginx2
```

小结：

/etc/ansible/hosts => 主机清单 => Ansible是通过主机清单实现服务器分组

主机清单的作用: 服务器分组。

主机清单的常见功能:

① 可以通过IP范围来分, 主机名名字的范围来分

② 如果ssh端口不是22的，可以传入新的端口。

③ 没有做免密登录，可以传密码。

# **三、Ansible模块****（重点理解）**

## **1.** 求帮助

```
# ansible-doc -l		
fortios_router_community_list                      Configure community lists...
azure_rm_devtestlab_info                     		   Configure community lists...
ecs_taskdefinition			                       				 Configure community lists...
avi_alertscriptconfig                     						Configure community lists...
tower_receive                                        				 Configure community lists...
netapp_e_iscsi_target       		                  		Configure community lists...
azure_rm_acs				                       					Configure community lists...
......
```

如果要查看ping模块的用法，使用下面命令（其它模块以此类推)

```
# ansible-doc ping
```

官网模块文档：[https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html)

中文文档：[https://ansible-tran.readthedocs.io/en/latest/docs/modules.html](https://ansible-tran.readthedocs.io/en/latest/docs/modules.html)

## **2.** hostname模块

hostname模块用于修改主机名（注意: 它不能修改/etc/hosts文件)

[https://docs.ansible.com/ansible/latest/modules/hostname_module.html#hostname-module](https://docs.ansible.com/ansible/latest/modules/hostname_module.html#hostname-module)

将其中一远程机器主机名修改为agent1.cluster.com

```
master# ansible  -m hostname -a 'name=agent1.cluster.com' 192.168.88.102
-m：模块名称
-a：具体参数和参数值
```

基本格式为: ansible 操作的机器名或组名 -m 模块名 -a "参数1=值1 参数2=值2"

---

扩展：在实际工作中，主机名称必须采用FQDN格式

功能名称.公司域名

web01.itcast.cn

web02.itcast.cn

mysql.itcast.cn

小结：

hostname在Linux操作系统中主要用于（获取或修改主机名称）

在Ansible里面，hostname专门用于主机名称，注意：Linux主机名必须要满足（FQDN）格式

## **3**. file模块（重点）

作用：file模块用于对文件相关的操作(创建, 删除, 软链接等)

[https://docs.ansible.com/ansible/latest/modules/file_module.html#file-module](https://docs.ansible.com/ansible/latest/modules/file_module.html#file-module)

① path=文件或文件夹路径

② state=状态（touch文件、directory文件夹、absent删除、recurse递归）

案例1：创建一个目录

```
master# ansible group1 -m file -a 'path=/test state=directory'
```

案例2：创建一个文件

```
master# ansible group1 -m file -a 'path=/test/111 state=touch'
```

案例3：递归修改owner,group,mode

```
master# ansible group1 -m file -a 'path=/test recurse=yes owner=bin group=daemon mode=0777'
```

案例4：删除目录（连同目录里的所有文件)

```
master# ansible group1 -m file -a 'path=/test state=absent'
```

案例5：创建文件并指定owner,group,mode等

```
master# ansible group1 -m file -a 'path=/tmp/111 state=touch owner=bin group=daemon mode=0777'
```

案例6：删除文件

```
master# ansible group1 -m file -a 'path=/tmp/111 state=absent'
```

案例7：创建软链接文件

```
master# ansible group1 -m file -a 'src=/etc/fstab path=/tmp/fstab state=link'
参数位置
src：源文件
path：快捷方式路径
state=link：代表创建软链接
```

小结：

Ansible中与文件管理相关的模块为（-m file）

基于file模块，我们可以创建文件、目录、软连接，也可以删除文件

**state=touch/file有区别：touch代表创建文件，file代表判断文件，判断文件是否存在且是否为文件状态**

## **4.** copy模块（重点）

作用：copy模块用于对文件的远程拷贝操作（如把本地的文件拷贝到远程的机器上)

本机：nginx.conf，copy模块：分发到所有web节点

[https://docs.ansible.com/ansible/latest/modules/copy_module.html#copy-module](https://docs.ansible.com/ansible/latest/modules/copy_module.html#copy-module)

在master上准备一个文件，拷贝此文件到group1的所有机器上【文件拷贝】

```
master# echo master > /tmp/file1
master# ansible group1 -m copy -a 'src=/tmp/file1 dest=/tmp/file2'
```

使用content参数直接往远程文件里写内容（会覆盖原内容）【写内容】

```
master# ansible group1 -m copy -a 'content="ansible\n" dest=/tmp/file3'
```

注意:ansible中-a后面的参数里也有引号时，记得要单引双引交叉使用，如果都为双引会出现问题

使用`force`参数控制是否强制覆盖

如果目标文件已经存在，则不覆盖

```
master# ansible group1 -m copy -a 'src=/tmp/file2 dest=/tmp/file3 force=no'
```

如果目标文件已经存在，则会强制覆盖

```
master# ansible group1 -m copy -a 'src=/tmp/file2 dest=/tmp/file3 force=yes'
```

使用backup参数控制是否备份文件

backup=yes表示如果拷贝的文件内容与原内容不一样，则会备份一份

group1的机器上会将/tmp/file3备份一份（备份文件命名加上时间），再远程拷贝新的文件为/tmp/file3

```
master# ansible group1 -m copy -a 'src=/etc/fstab dest=/tmp/file3 backup=yes owner=daemon group=daemon mode=0777'
```

简单理解：就是对目标文件进行备份操作

copy模块拷贝时要注意拷贝目录后面是否带"/"符号

/etc/yum.repos.d后面不带/符号，则表示把/etc/yum.repos.d整个目录拷贝到/tmp/目录下

```
master# ansible group1 -m copy -a 'src=/etc/yum.repos.d dest=/tmp/'
```

/etc/yum.repos.d/后面带/符号，则表示把/etc/yum.repos.d/目录里所有文件拷贝到/tmp/目录下

```
master# ansible group1 -m copy -a 'src=/etc/yum.repos.d/ dest=/tmp/'
```

小结：

Ansible有一个特殊模块，用于把本地文件拷贝到远程服务器，这个模块（copy）

copy模块有两个常用的参数：（src）、（dest）

扩展：

Ansiblecopy模块：把本地文件拷贝到远程服务器，底层基于SSH协议，所以每个拷贝文件都需要走SSH协议，建立连接，进行认证，然后实现文件传输，如果一个目录下有多个文件，则copy模块执行会比较缓慢。

Ansiblesynchronize模块：把本地文件拷贝到远程服务器，底层基于RSYNC实现文件传输，可以全量传输也可以增量传输，所以相对而言速度要快一些，但是要求机器上必须要提前安装rsync服务。【大文件传输】

dnf install rsync -y

synchronize模块其参数几乎与copy模块一模一样，都有src与dest参数，src代表源文件位置，dest代表目标文件位置。

ansible group1 -m synchronize -a "src=/etc/yum.repos.d dest=/tmp/"

## **5.** fetch模块

作用：fetch模块与copy模块类似，但作用相反。用于把远程机器的文件拷贝到本地，类似于收作业！！！

[https://docs.ansible.com/ansible/latest/modules/fetch_module.html#fetch-module](https://docs.ansible.com/ansible/latest/modules/fetch_module.html#fetch-module)

注意: fetch模块不能从远程拷贝目录到本地

第1步: 在两台被管理机上分别创建一个同名文件（但内容不同)

```
agent1# echo agent1 > /tmp/1.txt
agent2# echo agent2 > /tmp/1.txt
```

第2步: 从master上fecth文件(因为group1里有2台机器,为了避免同名文件文件冲突，它使用了不同的目录)

```
master# ansible group1  -m fetch -a 'src=/tmp/1.txt dest=/tmp/'
192.168.88.102 | CHANGED => {
  "changed": true, 
  "checksum": "d2911a028d3fcdf775a4e26c0b9c9d981551ae41", 
  "dest": "/tmp/192.168.88.102/tmp/1.txt",
  "md5sum": "0d59da0b2723eb03ecfbb0d779e6eca5", 
  "remote_checksum": "d2911a028d3fcdf775a4e26c0b9c9d981551ae41", 
  "remote_md5sum": null
}

192.168.88.103 | CHANGED => {
  "changed": true, 
  "checksum": "b27fb3c4285612643593d53045035bd8d972c995", 
  "dest": "/tmp/192.168.88.103/tmp/1.txt",
  "md5sum": "cd0bd22f33d6324908dbadf6bc128f52", 
  "remote_checksum": "b27fb3c4285612643593d53045035bd8d972c995", 
  "remote_md5sum": null
}
```

安装tree：

```
# yum install tree -y
# 以大树结构显示文件信息（包含多层）
# tree /tmp
```

小结：

fetch功能与copy功能正好相反，负责从远程服务器收集文件到本地

fetch里面一共有两个参数，src与dest

## **6.** user模块

作用：user模块用于管理用户账号和用户属性。

[https://docs.ansible.com/ansible/latest/modules/user_module.html#user-module](https://docs.ansible.com/ansible/latest/modules/user_module.html#user-module)

state参数有两个值：① present创建 ② absent删除

---

案例1：创建aaa用户,默认为普通用户,创建家目录

```
master# ansible group1 -m user -a 'name=aaa state=present'
```

案例2：创建bbb系统用户,并且登录shell环境为/sbin/nologin

```
master# ansible group1 -m user -a 'name=bbb state=present system=yes  shell="/sbin/nologin"'
```

案例3：创建ccc用户, 使用uid参数指定uid, 使用password参数传密码

```
master# echo 123456 | openssl passwd -1 -stdin
$1$DpcyhW2G$Kb/y1f.lyLI4MpRlHU9oq0

passwd可以使用-l选项，代表lock，锁定账号，不允许登录系统
openssl用于生成散列密码，openssl passwd生成密码并交给-stdin标准输入，openssl passwd -1相当于md5算法
```

下一句命令注意一下格式，密码要用双引号引起来，单引号的话验证时会密码不正确

```
master# ansible group1 -m user -a 'name=ccc uid=2000 state=present password="$1$DpcyhW2G$Kb/y1f.lyLI4MpRlHU9oq0"'
```

案例4：创建一个普通用户叫hadoop,并产生空密码密钥对

```
master# ansible group1 -m user -a 'name=hadoop generate_ssh_key=yes'
```

案例5：删除aaa用户,但家目录默认没有删除

```
master# ansible group1 -m user -a 'name=aaa state=absent'
```

案例6：删除bbb用户,使用remove=yes参数让其删除用户的同时也删除家目录

```
master# ansible group1 -m user -a 'name=bbb state=absent remove=yes'
```

小结：

user模块作用：创建用户 和 删除用户

创建用户（state=present）和删除用户（state=absent）

## **7.** group模块

作用：group模块用于管理用户组和用户组属性。

[https://docs.ansible.com/ansible/latest/modules/group_module.html#group-module](https://docs.ansible.com/ansible/latest/modules/group_module.html#group-module)

创建组

```
master# ansible group1 -m group -a 'name=yunwei gid=3000 state=present'
```

删除组（如果有用户的gid为此组，则删除不了)

```
master# ansible group1 -m group -a 'name=yunwei state=absent'
```

小结：

group模块比较简单，主要用于（创建用户组）和（删除用户组）

## **8.** cron模块

聊聊计划任务（定时器）=>（重点）

```
# crontab -l  查看定时器
# crontab -e	编辑定时器
分 时 日 月 周 要执行命令的绝对路径
*/1 * * * * /usr/sbin/ntpdate -u ntp4.aliyun.com
*/1：每分钟

如果不知道某个命令的绝对路径 => which 命令
# 每天凌晨4点执行某个命令 => 0 4 * * * 命令
# 每10分钟执行某个命令 => */10 * * * * 命令
# 每周3的凌晨2点执行某个命令 => 0 2 * * 3 命令
```

图解：

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773726473577-3ba35f5e-ccfd-44ad-8303-d96ddc698c82.jpg "null")

常见格式：

```
星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，"1,2,5,7,8,9"
中杠（-）：可以用整数之间的中杠表示一个整数范围，例如"2-6"表示"2,3,4,5,6"
正斜线（/）：可以用正斜线指定时间的间隔频率，例如"0-23/2"表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。
```

时间案例：

```
03 * * * *  每小时03分执行
01 02 * * * 每天两点01分执行
01 02 3 * * 每个月3号2点01分执行
01 02 3 1 * 每年1月3号2点01分执行
01 02 * * 0 每周日的2点01分执行
01,02,03 * * * * 每小时 01 02 03分执行
01,02,03 1,2,3 * * * 每天1 2 3点的  01 02 03分执行
*/10 * * * *   每隔10分执行
00 */2 * * *   每隔两小时执行
00 * */2 * *   每隔两天执行
2 8-20/3 * * *  从8点开始到20点结束，每隔3个小时的02分执行一次
```

案例：每分钟创建一个文件/root/file_202404171733.txt

```
# crontab -e
* * * * * touch /root/file_$(date +\%Y\%m\%d\%H\%M).txt
```

案例：针对/tmp目录定时压缩 => file_202404171733.tar.gz

```
# crontab -e
* * * * * /usr/bin/tar -zcf file_$(date +\%Y\%m\%d\%H\%M).tar.gz /tmp

问题：在crontab中如果出现了%百分号，默认无法执行
解决：添加反斜杠转义\%

# 如果crontab没有执行成功，可以通过cat /var/log/cron日志文件
```

cron模块用于管理周期性时间任务

[https://docs.ansible.com/ansible/latest/modules/cron_module.html#cron-module](https://docs.ansible.com/ansible/latest/modules/cron_module.html#cron-module)

创建一个cron任务,不指定user的话,默认就是root（因为我这里是用root操作的)。

如果minute,hour,day,month,week不指定的话，默认都为*

```
master# ansible group1 -m cron -a 'name="test cron1" user=root job="touch /tmp/111" minute=*/2' 
```

删除cron任务

```
master# ansible group1 -m cron -a 'name="test cron1" state=absent'
```

补充面试题：crond如何备份以及如何查看crond执行日志？

答：备份目录，/var/spool/cron，每个用户在这个目录下有一个对应文件

日志文件，/var/log/cron代表日志文件

所谓的计划任务备份就是把/var/spool/cron进行整体备份即可！！！

小结：

cron本身比较重要，叫做计划任务（定时器）=> ① 创建计划任务 ② 如何查看 ③ 如何查日志 ④ 如何备份

Ansible可以通过cron模块创建或者移除计划任务！

## **9.** yum/dnf模块（重点）

yum模块用于使用yum命令来实现软件包的安装与卸载。

[https://docs.ansible.com/ansible/latest/modules/yum_module.html#yum-module](https://docs.ansible.com/ansible/latest/modules/yum_module.html#yum-module)

使用yum安装一个软件（前提:group1的机器上的yum配置都已经OK）

```
master# ansible group1 -m yum -a 'name=vsftpd state=present'
或
master# ansible group1 -m dnf -a 'name=vsftpd state=present'
```

使用yum安装httpd,httpd-devel软件,state=latest表示安装最新版本

```
master# ansible group1 -m yum -a 'name=httpd,httpd-devel state=latest' 
或
master# ansible group1 -m dnf -a 'name=httpd,httpd-devel state=latest' 
```

使用yum卸载httpd,httpd-devel软件

```
master# ansible group1 -m yum -a 'name=httpd,httpd-devel state=absent' 
或
master# ansible group1 -m dnf -a 'name=httpd,httpd-devel state=absent' 
```

## **10.** service模块（重点）

作用：service模块用于控制服务的启动,关闭,开机自启动等。

[https://docs.ansible.com/ansible/latest/modules/service_module.html#service-module](https://docs.ansible.com/ansible/latest/modules/service_module.html#service-module)

启动vsftpd服务，并设为开机自动启动

```
master# ansible group1 -m service -a 'name=httpd state=started enabled=true'
```

state服务管理可以选参数："reloaded"、"restarted"、"started"、"stopped"

关闭vsftpd服务，并设为开机不自动启动

```
master# ansible group1 -m service -a 'name=httpd state=stopped enabled=false'
```

小结：

yum/dnf模块：主要负责（安装或卸载软件）

service模块：主要负责（服务的管理、启动、停止、重启、开机自启、开机不自启）

## **11.** script模块

作用：script模块用于在远程机器上执行master本地脚本。

[https://docs.ansible.com/ansible/latest/modules/script_module.html#script-module](https://docs.ansible.com/ansible/latest/modules/script_module.html#script-module)

在master上准备一个脚本

```
master# vim /tmp/1.sh
#!/bin/bash
mkdir /export/data -p
touch /export/data/file{1..9}
```

在group1的远程机器里都执行master上的/tmp/1.sh脚本（此脚本不用给执行权限)

```
master# ansible group1 -m script -a '/tmp/1.sh'
```

适用场景：对Shell脚本比较熟悉，然后希望通过Shell脚本完成所有机器的环境部署！

## **12.** comand与shell模块⭐

两个模块都是用于执行linux命令的,这对于命令熟悉的工程师来说，用起来非常high。

shell模块与command模块差不多（command模块不能执行一些类似$HOME,>,<,|等符号，但shell可以)

shell模块（重点）

[https://docs.ansible.com/ansible/latest/modules/command_module.html](https://docs.ansible.com/ansible/latest/modules/command_module.html)

[https://docs.ansible.com/ansible/latest/modules/shell_module.html](https://docs.ansible.com/ansible/latest/modules/shell_module.html)

```
master# ansible -m command group1 -a "useradd user2"
master# ansible -m command group1 -a "id user2"

master# ansible -m command group1 -a "cat /etc/passwd |wc -l"		--报错
master# ansible -m shell group1 -a "cat /etc/passwd |wc -l"		--成功

master# ansible -m command group1 -a "cd $HOME;pwd" --失败，echo可以输出，无法切换
master# ansible -m shell group1 -a "cd $HOME;pwd"	 --成功，echo可以输出，可以切换
```

回顾：wc命令

wc => wordcount统计

wc -c 字节数(统计大小）

wc -m 字符数（统计字符数量）

wc -l 统计总行数 => l == line（行）

wc -w 统计单词数

小结：shell与command

都能完成shell命令，shell模块会更强大一些，支持管道以及特殊符号！

注意：shell模块并不是百分之百任何命令都可以,比如vim或ll别名就不可以。不建议大家去记忆哪些命令不可以，大家只要养成任何在生产环境里的命令都要先在测试环境里测试一下的习惯就好。

# **四、Ansible Playbook**（重点）

作用：Playbook（剧本），主要用于实现一些较为复杂的自动化部署操作。软件安装配置，如Keepalived、MySQL集群、Redis集群、大数据集群、K8S集群。

## **1.** Playbook概述

playbook(剧本): 是ansible用于配置,部署,和管理被控节点的剧本。用于ansible操作的编排。

参考: [https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)

使用的格式为yaml格式（saltstack,elk,docker,docker-compose,kubernetes等也都会用到yaml格式)

## **2.** yaml格式

- 以.yaml或.yml结尾

- 文件的第一行以 "---"开始，表明YMAL文件的开始(可选的)

- 以#号开头为注释

- 列表中的所有成员都开始于相同的缩进级别, 并使用一个"- "作为开头(一个横杠和一个空格)

- 一个字典是由一个简单的 键（key）: 值（value）的形式组成(这个冒号后面必须是一个空格)

注意: 写这种文件不要使用Tab键，都使用空格

参考: [https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#yaml-syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#yaml-syntax)

看一个官方案例：

```
---
# 一位职工记录
name: Example Developer
job: Developer
skill: Elite
employed: True
foods:
  - Apple
  - Orange
  - Strawberry
  - Mango
languages:
  ruby: Elite
  python: Elite
  dotnet: Lame
```

## **3.** Playbook入门案例

[https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#playbook-syntax](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#playbook-syntax)

先直接来看一个实例，在Linux系统中安装Apache软件：① yum安装软件 ② 编辑httpd.conf配置文件

第1步: 创建一个存放playbook的目录(路径自定义)

```
master# mkdir /etc/ansible/playbook -p
```

第2步：准备httpd配置文件,并修改成你想要的配置

```
master# yum install httpd -y
```

按需要修改你想要的配置(为了测试可以随意改动标记一下)

```
master# vim /etc/httpd/conf/httpd.conf

【更改端口8080】
47行（监听端口）Listen 8080
124行（项目目录）DocumentRoot "/var/www/html"

#启动httpd软件
systemctl start httpd
#在浏览器访问http://192.168.88.101：8080/

#在浏览器访问http：//192.168.88.101:8080/#创建测试页面
echo 'test page' > /var/www/html/index.html
```

第3步：写一个playbook文件(后缀为.yml或.yaml)

```
# vim /etc/ansible/playbook/example.yaml
---
- hosts: group1
  remote_user: root
  tasks:
    - name: ensure apache is at the latest version
      yum:
        name: httpd,httpd-devel
        state: latest
    
    - name: write the apache config file
      copy:
        src: /etc/httpd/conf/httpd.conf
        dest: /etc/httpd/conf/httpd.conf
      notify:
        - restart apache

    - name: ensure apache is running (and enable it at boot)
      service:
        name: httpd
        state: started
        enabled: yes

  handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```

一组主机（hosts）

→ 用哪个用户执行（remote_user）

→ 执行哪些任务（tasks）

→ 如果有变更，触发处理器（handlers）

```
# vim /etc/ansible/playbook/example.yaml
---
# YAML 文件开始标识（建议保留）

- hosts: group1               # 指定要执行的主机组（来自 inventory）
  remote_user: root          # 使用 root 用户远程执行

  tasks:                     # 任务列表（按顺序执行）
    
    - name: ensure apache is at the latest version   # 任务说明：安装最新版 Apache
      yum:                                           # 使用 yum 模块
        name: httpd,httpd-devel                      # 要安装的软件包（多个用逗号分隔）
        state: latest                                # 状态：安装最新版本

    - name: write the apache config file             # 任务说明：复制 Apache 配置文件
      copy:                                          # 使用 copy 模块（从控制节点复制到目标主机）
        src: /etc/httpd/conf/httpd.conf              # 源文件路径（控制节点）
        dest: /etc/httpd/conf/httpd.conf             # 目标路径（远程主机）
      notify:                                        # 如果该任务发生变更，则触发 handler
        - restart apache                             # 触发名为“restart apache”的处理器

    - name: ensure apache is running (and enable it at boot)  # 任务说明：启动并设置开机自启
      service:                                               # 使用 service 模块
        name: httpd                                          # 服务名称
        state: started                                       # 状态：启动服务
        enabled: yes                                         # 开机自启

  handlers:                 # 处理器（只有被 notify 才会执行）

    - name: restart apache  # 处理器名称（必须与 notify 一致）
      service:              # 使用 service 模块
        name: httpd         # 服务名称
        state: restarted    # 动作：重启服务
```

注意：task任务格式

![[附件/cbe5a25360.png]]

```
- name: 任务执行时，打印的文本信息，可以是英文也可以是中文（类似注释，但是会打印输出）
   ansible模块，如file、copy、yum
     参数
   notify:与ansible模块是同级关系
     - restart apache，这个地方的名称与 handlers:中name标签同名，代表调用handlers中定义好的任务操作
```

第4步: 执行写好的palybook

会显示出执行的过程，并且执行的每一步都有ok,changed,failed等标识

执行如果有错误(failed)会回滚，解决问题后，直接再执行这条命令即可,并会把failed改为changed（幂等性)

```
# ansible-playbook /etc/ansible/playbook/example.yaml
```

小结：

Playbook剧本就是按照配置的Task任务流程，按顺序执行。

在工作中，主要编写Task任务，一定要完全按照Task任务格式，具体每个模块如何使用，可以参考官网文档。

## **4.** Playbook常见语法

hosts: 用于指定要执行任务的主机，其可以是一个或多个由冒号分隔主机组，一般可以是具体组名也可以是all

remote_user: 用于指定远程主机上的执行任务的用户.

```
- hosts: group1			
   remote_user: root	
```

tasks: 任务列表, 按顺序执行任务.

如果一个host执行task失败, 整个tasks都会回滚, 修正playbook 中的错误, 然后重新执行即可.

```
tasks:
  - name: ensure apache is at the latest version	
    yum: name=httpd,httpd-devel state=latest
    
  - name: write the apache config file		
    copy: src=/etc/httpd/conf/httpd.conf dest=/etc/httpd/conf/httpd.conf
```

handlers: 类似task，但需要使用notify通知调用。

注意：不管有多少个通知者进行了notify，等到play中的所有task执行完成之后，handlers也只会被执行一次.

handlers最佳的应用场景是用来重启服务,或者触发系统重启操作.除此以外很少用到了.

```
notify:				  
    - restart apache
    
  - name: ensure apache is running (and enable it at boot)
    service: name=httpd state=started enabled=yes
    
  handlers:
    - name: restart apache
      service: name=httpd state=restarted
```

英文单词 => variables: 变量 => playbook中简化了

① 定义变量：

vars:

- 变量名称: 变量的值

② 调用变量：

{{变量名称}}

定义变量可以被多次方便调用

```
master# vim /etc/ansible/playbook/example2.yaml
---
 - hosts: group1
   remote_user: root
   vars:
   - user: test1
   tasks:
   - name: create user
     user: name={{user}} state=present
```

执行Ansible Playbook

```
语法检查，没有真正执行
master# ansible-playbook /etc/ansible/playbook/example2.yaml --syntax-check

执行Playbook脚本
master# ansible-playbook /etc/ansible/playbook/example2.yaml
```

## **5.** Playbook案例

写一个playbook实现

a. 配置yum

b. 安装vsftpd包 => FTP服务 => 21号端口 => 专门用于上传和下载的

c. 修改配置文件(要求拒绝匿名用户登录)

d. 启动服务并实现vsftpd服务开机自动启动

```
---
- hosts: group1                 
  remote_user: root                     
  tasks:                                    
  - name: ensure vsftpd is at the latest version        
    yum: name=vsftpd state=latest
    
  - name: write the apache config file          
    copy: src=/etc/vsftpd/vsftpd.conf dest=/etc/vsftpd/vsftpd.conf 
    notify:                             
    - restart vsftpd
    
  - name: ensure vsftpd is running (and enable it at boot)
    service: name=vsftpd state=started enabled=yes
    
  handlers:                     
    - name: restart vsftpd              
      service: name=vsftpd state=restarted
```

扩展：循环结构

```
- name: write the apache config file
  copy:
    src: "{{ item.src }}"
    dest: "{{ item.dest }}"
  loop:
    - { src: "/etc/vsftpd/vsftpd.conf", dest: "/etc/vsftpd/vsftpd.conf" }
    - { src: "/etc/vsftpd/ftpusers", dest: "/etc/vsftpd/ftpusers" }
    - { src: "/etc/vsftpd/user_list", dest: "/etc/vsftpd/user_list" }
```

扩展：FTP软件的使用 => FTP服务

FTP服务：文件传输协议，在实际工作中主要上传下载服务，默认端口21

怎么样允许，用户连接呢？

第一步：在连接的机器上创建一个普通账号，如itheima，密码：123456

```
# useradd itheima
# passwd itheima
设置密码为123456
```

第二步：找到如下两个文件

![](https://cdn.nlark.com/yuque/0/2026/jpg/40487410/1773726473642-6e88b0a0-ae57-4721-a19d-605d292050c0.jpg "null")

去掉root账号（否则root无法登录）

第三步：使用课件中提供的FlashFXP连接FTP服务，如下图所示：

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773726473828-4f1e9641-1020-4a34-9ee5-49dd94322523.png "null")

**案例: 编排nfs搭建与客户端挂载**

回顾：NFS（Network File System）网络文件系统，在实际工作中，主要用于实现海量数据存储。

在NiuShop电子商城项目中，我们可以基于NFS/OSS实现静态文件存储 => 商品图片（海报、广告图）、文件、音频、视频。

NiuShop商城源码（服务器1） => 挂载NFS => （服务器2）文件服务器

工作职责：

① 负责整个项目环境搭建

② 基于NFS实现海量数据存储

③ 基于Redis实现数据缓存

④ 基于GTID全局事务实现主从架构设计

⑤ 基于Prometheus + Grafana实现监控报警

1, 在master上准备nfs配置文件

```
# vim /etc/exports
/share  *(rw)

说明：
/etc/exports：NFS默认配置文件
共享目录   *(rw)
*代表任意主机均可挂载访问/share目录
(ro)/(rw) ：read only只读/read write可读可写
```

2, 编写yaml编排文件

```
---
- hosts: 192.168.88.102
  remote_user: root
  tasks:
  - name: 安装nfs服务相关软件包
    yum: name=nfs-utils,rpcbind,setup  state=latest

  - name: 创建共享目录
    file: path=/share/ state=directory

  - name: 同步nfs配置文件
    copy: src=/etc/exports dest=/etc/exports

    notify: restart nfs

  - name: 启动rpcbind服务,并设置为开机自启动
    service: name=rpcbind state=started enabled=on

  - name: 启动nfs服务,并设置为开机自启动
    service: name=nfs-server state=started enabled=on

  handlers:
  - name: restart nfs
    service: name=nfs-server state=restarted

- hosts: 192.168.88.103
  remote_user: root
  tasks:
  - name: 安装nfs客户端软件包
    yum: name=nfs-utils state=latest

  - name: 挂载nfs服务器的共享
    shell: mount 192.168.88.102:/share /mnt
```

rpc一种网络协议，数据通信都需要依靠rpc；nfs本质就是一个rpc服务，所以安装使用nfs之前都需要安装rpcbind

3, 执行playbook

```
# ansible-playbook /etc/ansible/playbook/nfs.yaml
```

小结：

NFS全称：Network File System，网络文件系统，文件共享

服务器端必装软件：（nfs-utils） 和 （rpcbind）

注意：NFS服务全名（nfs-server）

# 五、Ansible Roles（仅供了解）

作用：把变量、任务、handlers分别作为角色，按文件夹来实现分离编写过程！

把Playbook进一步细化：原来所有操作都是放置于一个yaml文件，有了Roles，可以把变量、任务、handlers分别单独编写，适合团队实现Ansible脚本开发。|

## 1. roles介绍

roles(角色): 就是通过分别将variables, tasks及handlers等放置于单独的目录中,并可以便捷地调用它们的一种机制。

假设我们要写一个playbook来安装管理lamp环境(linux+apache+mysql+php =>wordpress博客），那么这个playbook就会写很长。所以我们希望把这个很大的文件分成多个功能拆分, 分成apache管理,php管理,mysql管理，然后在需要使用的时候直接调用就可以了，以免重复写。就类似编程里的模块化的概念，以达到代码复用的效果。

## 2. 创建roles的目录结构

```
files：用来存放由copy模块或script模块调用的文件。
tasks：至少有一个main.yml文件，定义各tasks。
handlers:有一个main.yml文件，定义各handlers。
templates：用来存放jinjia2模板。
vars：有一个main.yml文件，定义变量。
meta：有一个main.yml文件，定义此角色的特殊设定及其依赖关系，类似说明书。
```

**注意:** 在每个角色的目录中分别创建files, tasks,handlers,templates,vars和meta目录，用不到的目录可以创建为空目录.

## 3. 通过roles实现lamp

需定制三个角色: httpd,mysql,php

**第1步: 创建roles目录及文件,并确认目录结构**

```
master# cd /etc/ansible/roles/
master# mkdir -p {httpd,mysql,php}/{files,tasks,handlers,templates,vars,meta}
master# touch {httpd,mysql,php}/{tasks,handlers,vars,meta}/main.yml

master# yum install tree -y
master# tree /etc/ansible/roles/
/etc/ansible/roles/
├── httpd
│   ├── files
│   ├── handlers
│   │   └── main.yml
│   ├── meta
│   │   └── main.yml
│   ├── tasks
│   │   └── main.yml
│   ├── templates
│   └── vars
│       └── main.yml
├── mysql
│   ├── files
│   ├── handlers
│   │   └── main.yml
│   ├── meta
│   │   └── main.yml
│   ├── tasks
│   │   └── main.yml
│   ├── templates
│   └── vars
│       └── main.yml
└── php
    ├── files
    ├── handlers
    │   └── main.yml
    ├── meta
    │   └── main.yml
    ├── tasks
    │   └── main.yml
    ├── templates
    └── vars
        └── main.yml
```

**第2步: 准备httpd服务器的主页文件,php测试页和配置文件等**

```
master# echo "test main page" > /etc/ansible/roles/httpd/files/index.html

master# echo -e "<?php\n\tphpinfo();\n?>" > /etc/ansible/roles/httpd/files/test.php 


master# yum install httpd -y
按需求修改配置文件后,拷贝到httpd角色目录里的files子目录
master# vim /etc/httpd/conf/httpd.conf
master# cp /etc/httpd/conf/httpd.conf /etc/ansible/roles/httpd/files/
```

**第3步: 编写httpd角色的main.yml文件**

```
master# vim /etc/ansible/roles/httpd/tasks/main.yml
---
- name: 安装httpd
   yum: name=httpd,httpd-devel state=present

- name: 同步httpd配置文件
   copy: src=/etc/ansible/roles/httpd/files/httpd.conf dest=/etc/httpd/conf/httpd.conf
   notify: restart httpd

- name: 同步主页文件
   copy: src=/etc/ansible/roles/httpd/files/index.html dest=/var/www/html/index.html

- name: 同步php测试页
   copy: src=/etc/ansible/roles/httpd/files/test.php dest=/var/www/html/test.php

- name: 启动httpd并开机自启动
   service: name=httpd state=started enabled=yes
```

**第4步: 编写httpd角色里的handler**

```
master# vim /etc/ansible/roles/httpd/handlers/main.yml
---
- name: restart httpd
  service: name=httpd state=restarted
```

**第5步: 编写mysql角色的main.yml文件**

```
master# vim /etc/ansible/roles/mysql/tasks/main.yml
---
- name: 安装mysql
  yum: name=mariadb,mariadb-server state=present

- name: 启动mysql并开机自启动
  service: name=mariadb state=started enabled=yes
```

**第6步: 编写php角色的main.yml文件**

```
master# vim /etc/ansible/roles/php/tasks/main.yml
---
- name: 安装php及依赖包
  yum: name=php,php-gd,php-ldap,php-odbc,php-pear,php-xml,php-mbstring,php-snmp,php-soap,curl,curl-devel,php-bcmath,php-mysqlnd state=present

  notify: restart httpd
```

**第7步:编写lamp的playbook文件调用前面定义好的三个角色**

```
master# vim /etc/ansible/playbook/lamp.yaml
---
- hosts: group1
  remote_user: root
  roles:
    - httpd
    - mysql
    - php
```

**第8步: 执行lamp的playbook文件**

```
master# ansible-playbook /etc/ansible/playbook/lamp.yaml
```

小结：

Ansible Roles：把大的yaml文件拆解为若干个小的main.yml文件，好处：方便调试，每个文件都比较小

缺点：文件夹太多，过于冗余

常见问题：

问题1：YAML语法有错误，千万不要按Tab键，如果出错了，可以借助于YAML校检工具

[https://www.bejson.com/validators/yaml_editor/index.html](https://www.bejson.com/validators/yaml_editor/index.html)

问题2：Roles脚本是一个整体，不要单独执行某个yaml文件应该统一执行最终的yaml，如lamp.yaml

单独执行某个main.yml，报错信息如下：

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1773726473878-329b6079-368f-4488-af89-7d1f8ddb5b01.png "null")

以上其实不是错误，而是也能为main.yml文件不完整导致的！

## 拓展案例: 通过roles实现lamp并安装discuz

作用：基于Ansible Roles搭建Web项目（BBS论坛为例）=> 国内做的最好的BBS论坛 => Discuz

**第1步: 创建roles目录及文件,并确认目录结构**

```
master# cd /etc/ansible/roles/
master# mkdir -p {httpd,mysql,php}/{files,tasks,handlers,templates,vars,meta}
master# touch {httpd,mysql,php}/{tasks,handlers,vars,meta}/main.yml
```

**第2步: 准备httpd相关文件**

```
master# cp /etc/httpd/conf/httpd.conf /etc/ansible/roles/httpd/files/
master# ls /etc/ansible/roles/httpd/files/
Discuz_X3.5_SC_UTF8.zip  					Discuz相关软件包
httpd.conf 										              配置好的httpd.conf配置文件
```

**第3步: 编写httpd角色的main.yml文件**

```
master# vim /etc/ansible/roles/httpd/tasks/main.yml
- name: 安装httpd相关软件包
  yum: name=httpd,httpd-devel state=latest

- name: 同步配置文件
  copy: src=/etc/ansible/roles/httpd/files/httpd.conf dest=/etc/httpd/conf/httpd.conf

  notify: restart httpd

- name: 拷贝discuz压缩包
  copy: src=/etc/ansible/roles/httpd/files/Discuz_X3.5_SC_UTF8.zip dest=/tmp/

- name: 解压并mv网站文件到httpd家目录
  shell: rm -rf /var/www/html/*  && rm -rf /test/ && mkdir -p /test/ &&  unzip /tmp/Discuz_X3.5_SC_UTF8.zip -d /test/ &> /dev/null  && mv /test/upload/* /var/www/html/ && chown -R apache.apache /var/www/html/
# 上面的命令有点多,可以写成脚本,然后使用script模块来调用执行

- name: 启动httpd并开机自启动
  service: name=httpd state=started enabled=on
```

**第4步: 编写httpd角色里的handler**

```
master# vim /etc/ansible/roles/httpd/handlers/main.yml
---
- name: restart httpd
  service: name=httpd state=restarted
```

**第5步: 编写mysql角色的main.yml文件**

```
master# vim /etc/ansible/roles/mysql/tasks/main.yml
---
- name: 安装mariadb相关软件包
  yum: name=mariadb-server,mariadb state=latest

- name: 启动mariadb服务并设置开机自启动
  service: name=mariadb state=started enabled=on

- name: 执行建库脚本
  script: /etc/ansible/roles/mysql/files/create.sh
```

**第6步: 编写mysql的建库脚本**

```
master# vim /etc/ansible/roles/mysql/files/create.sh

#!/bin/bash
mysql << EOF
create database if not exists discuz default charset=utf8;
grant all on discuz.* to 'discuz'@'localhost' identified by '123';
flush privileges;
EOF
```

**第7步: 编写php角色的main.yml文件**

```
master# vim /etc/ansible/roles/php/tasks/main.yml
---
- name: 安装php及依赖包
  yum: name=php,php-gd,php-ldap,php-odbc,php-pear,php-xml,php-mbstring,php-snmp,php-soap,curl,curl-devel,php-bcmath,php-mysqlnd state=present

  notify: restart httpd
```

**第8步:编写lamp的playbook文件调用前面定义好的三个角色**

```
master# vim /etc/ansible/playbook/discuz.yaml
---
- hosts: group1
  remote_user: root
  roles:
    - httpd
    - mysql
    - php
```

**第9步: 执行lamp的playbook文件**

```
master# ansible-playbook /etc/ansible/playbook/discuz.yaml
```

# 今日重点

- [ ] Ansible安装部署、主机清单、常用模块、Playbook做一个总结

- [ ] 做一个快照，把所有操作在执行一遍，尤其模块、Playbook！！！

- [ ] 梳理一下常用模块作用

- [ ] 把Playbook的几个案例：FTP、NFS、Apache安装部署自己在操作一遍

---

最近学了数据库、Nginx、Prometheus、Ansible，可以把这些技术点融合到简历中

简历中尽量去掉智慧养老项目，把项目库.pdf文件中的项目融合2-3个进去，今天9点30之前，把最新简历发到作业目录中