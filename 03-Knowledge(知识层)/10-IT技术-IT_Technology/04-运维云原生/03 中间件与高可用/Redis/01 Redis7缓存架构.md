# 学习目标

1. 能够描述 Redis 作用及其业务适用场景
2. 能够安装配置启动 Redis
3. 能够使用命令行客户端简单操作 Redis
4. 能够实现操作基本数据类型
5. 能够理解描述 Redis 数据持久化机制
6. 能够操作安装 PHP 的 Redis 扩展
7. 能够操作实现 Redis7 主从模式（Redis 新版集群以及哨兵模式）

# 一、背景描述及其方案设计

## 1、业务背景描述

- 时间：2021.9 - 2022.6
- 发布产品类型：互联网动态站点商城
- 用户数量：25000（用户量猛增）
- PV：1000000 - 5000000（24 小时访问次数总和）
- DAU：12000（每日活跃用户数）

数据访问 瓶颈在数据库 【受到磁盘IO限制】

## 2、模拟运维设计方案

![[附件/b2aab926c0.png]]

根据以上业务需求，准备加入 **memcache / redis 缓存中间件服务器**，可以使用 Redis 更加丰富的功能在商城业务中实现：

① 实现活跃用户数的统计（使用 set 集合）  
② session 存储到 redis  
③ 防刷、防攻击软件开发：使用 openresty（nginx + lua）动态限制 IP 访问，实现 WAF（web application firewall）

# 二、Redis概述

## 1、什么是Redis

NoSQL 非关系数据库，key => value 键值对。

Redis 是 Remote Dictionary Server（远程数据服务）的缩写。

由意大利人 antirez（Salvatore Sanfilippo，萨尔瓦托·桑菲利波）开发的一款内存高速缓存数据库。该软件使用 C 语言编写，它的数据模型为 key-value。

它支持丰富的数据结构，比如：

- string
- list（双向链表）
- hash（哈希）
- set（集合）
- sorted set（zset，有序集合）

可持久化（保存数据到磁盘中），保证了数据安全。

## 2、业务使用场合

① **[SortSet]** 排行榜应用，取 topN 操作，例如 sina 微博热门话题（取最热的前 10 个话题）② **[List]** 获得最新 N 个数据或某个分类的最新数据③ **[String]** 计数器应用④ **[Set]** SNS（social network site）获得共同好友⑤ **[Set]** 防攻击系统（IP 判断），黑白名单等等

---

# 三、安装与配置 Redis

- 官方网址：[https://redis.io/](https://redis.io/)
- GitHub：[https://github.com/antirez/redis](https://github.com/antirez/redis)

准备Redis服务器，更改Mac地址，更改IP以及主机名称，在hosts绑定IP与主机，时间同步，安装必备软件。

## 1、安装方式

可以通过 yum 方式在线安装，也可以通过源码编译方式安装【推荐】。  
这里，采用源码编译方式安装：

```
第一步：找到对应的安装包资源，使用 wget 命令下载，这里安装的 7.4.0 版本。  
安装包资源地址：https://download.redis.io/releases/

第二步：上传 Redis 到 Linux 系统中  

wget https://download.redis.io/releases/redis-7.4.0.tar.gz

第三步：配置 => 编译 => 安装  

tar -zxvf redis-7.4.0.tar.gz
cd redis-7.4.0
make
make PREFIX=/usr/local/redis install
```

安装成功后，Redis 的可执行文件将被安装到 `/usr/local/redis`

---

![[附件/bd95256e0f.png]]

## 2、修改配置

```
sudo mkdir -p /usr/local/redis/conf
sudo cp redis.conf /usr/local/redis/conf/

# 修改配置
sudo vim /usr/local/redis/conf/redis.conf
# 可远程访问
88: bind 127.0.0.1 -::1 daemonize no
--> bind 0.0.0.0

# 后台运行
310:
--> daemonize yes


# 添加redis到环境变量 
sudo vim /etc/profile

export PATH="$PATH:/usr/local/redis/bin"
source /etc/profile

# 面试 是否调整过内核参数
  # LVS 开启IP转发
# 调整内核参数，redis内存分配策略
sudo vim /etc/sysctl.conf
vm.overcommit_memory = 1
sysctl -p
```

说明：  
vm.overcommit_memory

- 这个参数是Linux系统在分配内存时的一种策略控制，直接关系到Redis这样的应用能不能顺利启动、正常运行。默认值为0：系统会根据当前内存使用情况、总内存和交换空间的比例，“评估”是否允许分配内存。如果它“觉得”你分配太多内存了，就拒绝了，哪怕物理内存其实还够。Redis启动时会尝试申请大量内存，比如它的最大内存限制值（maxmemory），即使暂时还没用到。这时Linux系统“评估”你内存不够，就会阻止Redis启动，报错：
- 参数值设为1：系统不管三七二十一，你说要分配内存，它就答应。哪怕内存其实根本不够，它也会先允许你申请下来。如果设置为1，系统允许进程分配“看起来够但实际上不够”的内存。如果很多程序都这么做，等真正用内存时可能会爆掉系统（内存溢出或OOM）。但Redis一般是你可控的服务，设置maxmemory限制总量就没事。
- Redis推荐设置vm.overcommit_memory=1，就是为了避免系统“瞎担心内存不够”导致Redis启动失败。

![[附件/2ae442d469.png]]

## 3、启动Redis手工实现服务验证

```
# 查看版本
redis-cli -v

# 启动
redis-server /usr/local/redis/conf/redis.conf

# 查看服务进程
ps -ef | grep redis
```

![[附件/f3087d00e4.png]]

封装redis.service脚本

```
sudo vim /etc/systemd/system/redis.service

[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/conf/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

配置完成后，以后我们就可以直接使用systemctl start redis来实现redis启动操作。

```
systemctl start redis
```

## 4、6379端口

![[附件/f44189abdd.png]]

Redis默认端口 **6379** 并不是随机选择的，而是来源于手机键盘上的字母映射：

- 6379 → MERZ（手机按键字母）

而 **MERZ** 则来源于意大利女星：Alessia Merz

## 5、命令行客户端简单使用

redis属于c/s架构软件，telnet可以连接redis，没有本身redis-cli更加好用

①简单的数据操作  
string类型：字符串类型、文本类型，用于保存文本信息

```
# redis-cli

127.0.0.1:6379> set name devops
OK

127.0.0.1:6379> get name
"devops"
```

②查看操作语法帮助

```
127.0.0.1:6379> help
127.0.0.1:6379> help set
```

③系统状态信息

```
127.0.0.1:6379> info
```

④退出redis

```
127.0.0.1:6379> quit
```

# 四、数据结构类型操作

## 1、key（键名）

内存：NoSQL数据库，存储形式为键值对，类似身份证（不能重复，必须唯一）

key的命名规则不同于一般语言，键盘上除了空格、`\n`换行符外，其他的大部分字符都可以使用。但是像 `"mykey"` 和 `"mykey\n"` 这样包含空格和换行的key是不允许的。

我们在使用的时候可以自己定义一个key的格式，但是要特别注意：

- key不要太长，占内存，查询慢
- key不要太短，如 `u:1000:pwd:123456` 不如 `user:1000:password:123456` 可读性好

![[附件/484fd4cc53.png]]

默认在redis配置文件redis.conf中，提供了16库，查看配置文件：

```
# databases 16
# 数据库的编号都是从0开始，最大值为16-1
```

☆判断key是否存在

```
# exists key
# 存在1，不存在0
```

☆删除key

```
# del key
```

☆获取type类型

```
# type key
```

☆显示所有key

```
# keys *
```

☆设置过期时间（单位s）

```
# expire name 8
```

☆查看剩余时间

```
# ttl name
```

☆切换数据库（共16个库，index=number-1）

```
# select 0-15
```

☆flushdb清空当前库（删除所有key，慎重！！！）

```
# flushdb
```

☆清空所有库（删除所有数据库的所有key，慎重！！！）

```
# flushall
```

## 2、string

string是redis最基本的类型

redis的string可以包含任何数据，包括jpg图片的base64编码或者序列化的对象，单个value值最大上限是512MB

如果只使用string类型，redis就可以被看作是加上持久化特性的memcached

![[附件/25719675af.png]]

☆设置string

```
# set name itheima
```

☆批量设置string

```
# mset name cndws age 18 address beijing
```

☆批量获取

```
# mget name age address
```

☆增加与减少（+1与-1）（计数器）

```
# incr age
# decr age

# incrby age 2
# decrby age 3
```

☆尾部追加

```
# append name 123
```

![[附件/d58676b78a.png]]

☆截取

```
# substr name start end

# start：从哪里开始截取，默认从0第一个字符开始
# end：到哪里截取结束，必须要添加结束字符的索引号
```

小结：

string字符串类型是redis中最常用数据类型，其可以保存任何数据！！！单个value值最大上限是512MB

## 3、list

key value（value1,value2,value3）

list类型其实就是一个双向链表，通过push、pop操作从链表的头部或者尾部添加、删除元素，这使得list既可以用作栈，也可以用作队列

同一端进出：先进后出，后进先出 ==> 栈  
一端进，另一端出：先进先出 ==> 队列

![[附件/4b140f34db.png]]

首部（左left）尾部（右right）

需求：显示系统中最新（最近）登录的几个用户

设计实现：  
① 登录一个用户，把用户名称或者id存储在list中  
② 从左侧取第一个元素

特点：同一端进，同一端出（大部分以左为主）

用户：xiaohua xiaoming xiaobaitu  
key名称：lastlogin

![[附件/8423987b7d.png]]

案例：获取最后登录的用户

```
# lpush lastlogin xiaohua
# lpush lastlogin xiaoming
# lpush lastlogin xiaobaitu
```

栈操作：获取最后登录的用户

```
# lrange lastlogin 0 0
```

小结：

栈可以用于模拟获取最后登录用户

队列可以用于模拟秒杀功能实现=>电商平台=>秒杀（5个产品，打骨折价格），100个用户报名，最终到底谁获取这个商品呢？

生产环境下，秒杀功能，都要结合redis，秒杀开始时，把点击的用户放入redis里面，秒杀结束，从redis队列中取出前5个用户id，这就是秒杀功能实现。丨

## 4、set

作用：求交集、并集、差集！！！

redis的set是string类型的无序集合，集合里不允许有重复的元素，set元素最大可以包含（2的32次方-1）个元素。

关于set集合类型，除了基本的添加、删除操作，其他常用的操作还包含集合的：

- 并集（union）
- 交集（intersection）
- 差集（difference）

通过这些操作可以很容易实现SNS中的功能：

- 共同好友
- 好友推荐

TIP：MySQL连表文氏图  
[https://www.cnblogs.com/sunjie9606/p/4167190.html](https://www.cnblogs.com/sunjie9606/p/4167190.html)

![[附件/adba383ebb.png]]

案例1：实现朋友圈的存储和共同好友的计算

设计：  
key value  
xiaomingFR xiaohong xiaoqiang xiaogang xiaobai xiaohei  
xiaohongFR xiaoming xiaolv xiaolan xiaobai xiaohei

第一步：使用sadd添加xiaomingFR与xiaohongFR

```
# sadd xiaomingFR xiaohong xiaoqiang xiaogang xiaobai xiaohei
# sadd xiaohongFR xiaoming xiaolv xiaolan xiaobai xiaohei
```

第二步：求交集（共同好友）

```
# sinter xiaomingFR xiaohongFR
```

第三步：求并集（所有好友）

```
# sunion xiaomingFR xiaohongFR
```

第四步：求差集（互相推荐好友）

```
# sdiff xiaomingFR xiaohongFR
```

![[附件/2473469257.png]]

案例2：使用set实现制作IP黑名单（白名单）

使用：sismember，判断这个元素是否出现在集合中

```
# sadd ips 10.1.1.11 10.1.1.12
# sismember ips 10.1.1.11
# sismember ips 10.1.1.100
```

![[附件/48718c7f39.png]]

小结：  
set：无序且天生去重的数据集合 string类型的集合  
核心：求交集、并集、差集

## 5、sorted set

和set一样，sorted set也是string类型元素的集合 ⇒ 有序集合，元素不允许重复

不同的是每个元素都会关联一个权值（分值）

通过权值可以有序地获取集合中的元素，还可以根据权值进行排序

![[附件/bf911d66e7.png]]

需求：实现手机APP市场的软件排名  
key：hotTop

id score name  
1 2 qq  
2 3 wechat  
3 5 alipay  
4 7 taobao  
5 10 king  
6 8 jd

第一步：插入数据

```
# zadd hotTop 2 qq 3 wechat 5 alipay 7 taobao 10 king 8 jd
```

第二步：排序，从小到大（qq ⇒ wechat ⇒ alipay ⇒ taobao ⇒ jd ⇒ king）

```
# zrange hotTop 0 5
```

第三步：排序，从大到小

```
# zrevrange hotTop 0 5
```

![[附件/6fba46a909.png]]

扩展：获取某个软件的score值

```
# zscore hotTop jd
# zscore hotTop taobao
```

扩展：更新某个软件的score值

```
# zincrby hotTop -2 jd
# zrange hotTop 0 5
```

小结：  
和set一样，zset也是集合的一种；不同点在于zset是有序集合，set是无序集合。

Sortedset集合类型要求每个元素都有一个权重值（分值），依靠这个分值就可以实现排序等操作。丨

## 6、hash（哈希）

作用：redis不仅可以做缓存，还可以做数据库。除了可以使用string，还可以使用hash结构，比string压缩效率和使用效率更高。

hash存储数据和关系型数据库（MySQL）中存储一条数据的结构极为相似：

key : value（field : value）

示例（类似MySQL一条记录）：

insert into table(id,name,sex,age,address) values (null,'王维','男',18,'北京市昌平区')

在redis中的表示：

id：1  
name：王维  
sex：男  
age：18  
address：北京市昌平区

![[附件/1ad48fef4e.png]]

☆设置hash数据

```
# hmset devops username cndws age 18 email cndws@itcast.cn
```

☆获取指定的field字段信息

```
# hget devops username
# hmget devops username age email
```

☆更新devops的age字段信息

```
# hincrby devops age 1
```

☆获取某个key的所有field的所有value信息

```
# hvals devops
```

☆删除指定的field字段

```
# hdel devops age
```

☆获取devops的key数量

```
# hlen devops
```

☆查询指定field是否存在

```
# hexists devops name
```

小结：  
redis既可以作为缓存使用，也可以作为NoSQL数据库使用

存储数据时：

- 如果数据之间关联度不太大 ⇒ 使用string
- 如果数据之间关联度比较大 ⇒ 使用hash

相对而言，hash拥有更高的压缩比！！！

后期对Redis数据类型感兴趣，可以参考官方文档进行操作：[https://redis.io/docs/latest/develop/data-types/](https://redis.io/docs/latest/develop/data-types/)

数据库运维岗：技能包含MySQL、Oracle、Redis、MongoDB、国产数据库 。

# 五、数据持久化操作（重点）

目标：能够说出什么是持久化？RDB持久化和AOF持久化区别即可！

## 1、什么是数据持久化

数据持久化：数据在服务或者软件重启之后不丢失

如果数据只存在内存中，肯定会丢失，实现持久化就需要把数据存储到磁盘中（HDD / SSD）

Redis持久化：  
[https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

![[附件/b7a765ebab.png]]

## 2、Snapshotting（快照） ⇒ RDB持久化（全量）

默认情况下，RDB持久化的快照功能是开启的，并且有一个“拍照”频率（触发条件）。

### ☆RDB自动备份

前提：只有满足触发条件，才会自动备份！通过查看配置文件可以看到：

```
save 900 1
save 300 100
save 60 10000
```

含义：

- 15分钟内最少有1个key改变
- 5分钟内最少有100个key改变
- 1分钟内最少有10000个key改变

秒数 = redis事务型操作（增删改）的次数

暂时设置示例：

```
446行: save 10 2
```

快照文件：

```
dbfilename dump.rdb
```

从Redis 6版本开始，引入了 **dir** 参数 ⇒ 代表默认保存路径

- 之前版本默认安装路径：/usr/local/redis

```
dir ./       # 相对路径，redis启动目录
cd /usr/local/redis
bin/redis-server conf/redis.conf dump.rdb

127.0.0.1:6379> config get dir   # 查看默认保存路径
```

建议直接更改配置（517行）：

```
dir /usr/local/redis
```

文件名称并不是固定的，可以修改，如 `dump_port.rdb`  
设置完成后，一定要记得重启Redis

```
pkill redis-server
cd /usr/local/redis
bin/redis-server config/redis.conf
127.0.0.1:6379> config get dir
127.0.0.1:6379> bgsave
```

测试备份频率：

测试RDB持久化

```
systemctl stop redis

cd /usr/local/redis
vim conf/redis.conf      # 446行，更改 save 10 2
                         # 517行，更改 dir /usr/local/redis

bin/redis-server conf/redis.conf
```

  
在10秒内，进行2个key的改变，查看备份效果：

```
set num1 1
set num2 2
```

![[附件/1f4ca853c2.png]]

测试结果：查看 `dump.rdb` 文件大小的变化

RDB可能遇到的缺点：

- 必须要满足触发条件（如10秒内有2个key改变）才能拍照
- 如果10秒内只有1个key改变，而第11秒Redis宕机，则这部分数据会丢失
- 损失的数据仅限于上次快照到宕机前的数据，非常小概率事件

### ☆手工快照备份

```
127.0.0.1:6379> save
# 或者
# 工作中只能使用bgsave
127.0.0.1:6379> bgsave
```

`save`：

- 在主程序中执行，会阻塞当前 Redis 服务器，直到持久化完成
- 执行期间，Redis不能处理其他命令
- 线上环境禁止使用 `save`，否则可能导致严重后果。
- `bgsave`：后台异步保存，不阻塞Redis服务

![[附件/8e73fa09ae.png]]

bgsave

- Redis会在后台异步对所有数据进行快照操作
- 不阻塞Redis服务，同时还能响应客户端请求
- 实现方式：Redis会fork一个子进程，由子进程完成持久化操作
- 父进程继续处理客户端请求，可以同时修改数据
- 优点：不会影响线上服务的正常运行

![[附件/916bd4a5a1.png]]

☆扩展：lastsave

```
127.0.0.1:6379> LASTSAVE
(integer) 1694745433
```

说明：

- `LASTSAVE` 命令可以获取最后一次成功执行快照的时间（Unix时间戳）
- 获取到的时间戳需要转换成人类可读时间

```
date -d @[redis内获取的时间戳]
# 例如：date -d @1694745433
```

### ☆RDB优劣势

**优点**：

- RDB是Redis数据的一个非常紧凑的单文件时间点表示
- RDB文件非常适合备份，例如对最近24小时内的RDB文件每小时存档，并保存30天内每天的RDB快照，可在灾难发生时轻松恢复数据集的不同版本
- 适合大规模数据恢复
- 按照业务定时备份
- 对数据的完整性和一致性要求不高
- RDB文件在内存中加载速度比AOF快很多

**缺点**：

- 需要在一定间隔时间做一次备份，如果Redis意外宕机，可能丢失从当前至最近一次快照期间未保存的数据
- 内存数据全量同步，如果数据量太大，会导致I/O严重影响服务器性能
- 为了使用子进程持久化到磁盘，RDB经常需要fork，如果数据集很大，fork可能耗时，CPU性能不好时可能导致Redis短暂停止为客户端服务几毫秒甚至一秒
- AOF也需要fork，但不太频繁，可通过调整重写日志频率，无需权衡持久性

### ☆修复dump.rdb文件与恢复dump.rdb文件

在生产环境下，如果Redis出现故障，可以实时备份 `dump.rdb` 文件到指定位置。修复Redis后，将 `dump.rdb` 文件拷贝到Redis配置的RDB保存目录，即可完成数据恢复。

注意：在新版本Redis（如Redis 5-7）中，恢复之前，需要对 `dump.rdb` 文件进行修复操作。

命令：`redis-check-rdb`，路径在 `/usr/local/redis/bin/`

```
# redis-check-rdb [dump.rdb文件名称]
# 例如：
bin/redis-check-rdb /usr/local/redis/dump.rdb
```

### ☆哪些情况可以触发RDB快照

a）满足配置文件默认的快照配置  
b）手动 `save` / `**bgsave**` 命令  
c）执行 `flushall` 清空数据库并持久化，会生成一个空的RDB文件（无意义）d）执行 `shutdown` 且没有开启AOF持久化e）主从复制时自动触发

### ☆禁用RDB快照

**方式一**：

```
bin/redis-cli config set save ""
```

**方式二**：在配置文件中手动添加

```
save ""
```

### ☆配置文件 redis.conf 中 snapshotting 模块

**a) stop-writes-on-bgsave-error**

- 默认：yes
- 配置成 no 表示在快照写入失败时，Redis仍然接受新的写请求，不在乎数据不一致或通过其他手段控制不一致

![[附件/ce16595dfa.png]]

**b) rdbcompression**

- 控制 RDB 快照文件是否启用压缩

![[附件/acead60d55.png]]

默认：yes

- 对于存储到磁盘中的快照，可以设置是否进行压缩存储
- 如果开启，Redis会采用LZF算法进行压缩
- 如果不想消耗CPU进行压缩，可以关闭此功能

**c) rdbchecksum**

![[附件/12fa31c8c2.png]]

- 默认：yes
- 存储快照后，Redis使用CRC64算法进行数据校验
- 会增加大约10%的性能消耗
- 如果希望获得最大性能提升，可以关闭此功能

**d) rdb-del-sync-files**

![[附件/5dba4858fe.png]]

默认：no

在没有持久性的情况下删除复制中使用的RDB文件。默认情况下no，此选项是禁用的。

### ☆小结

![[附件/31e3c211a4.png]]

**优势**：

- RDB是一个非常紧凑的文件
- 保存RDB文件时，父进程只需fork出子进程，之后的持久化工作由子进程完成，父进程无需进行额外I/O操作
- 最大化Redis性能
- 与AOF相比，**恢复大数据集时，RDB方式更快**

**缺点**：

- 数据丢失风险大
- RDB需要频繁fork子进程保存数据集到硬盘
- 数据集较大时，fork过程耗时，可能导致Redis**短时间（毫秒级）无法响应客户端请求**

## 3、append only file（AOF）

相同点：RDB和AOF都是Redis持久化的一种方式。

不同点：RDB采用快照持久化（全量备份）、AOF（Appendonly file）把用户对Redis的DML操作（事务型操作）追加到AOF文件中

### ☆AOF介绍

- **AOF（Append Only File）：记录服务器****接收到的每个写操作**
- **这些操作可以在服务器重启时重放，重建原始数据集**
- **命令以与Redis协议相同的格式记录**

**通俗易懂：**

- **以****日志形式记录每个写操作****（读操作不记录）**
- **文件只追加，不改写**
- **Redis启动时会读取AOF文件，按顺序执行写指令完成数据恢复**
- **类似于MySQL的relay log（中继日志）效果**

### ☆工作流程

![[附件/22f921de43.png]]

步骤详解

1. **Client发送命令**

- Client作为命令的来源，可能有多个源头，并不断发送写操作命令到Redis Server

2. **AOF缓冲区缓存命令**

- 命令到达Redis Server后，并不是直接写入AOF文件
- Redis先将命令放入AOF缓冲区（内存区域）
- 缓冲区目的是累积一定量的命令后再写入磁盘，避免频繁的磁盘I/O

3. **写入AOF文件**

- AOF缓冲区的内容根据配置的同步策略，将命令写入磁盘上的AOF文件

4. **AOF重写（文件压缩）**

- 随着写入内容增加，为避免AOF文件膨胀
- Redis会根据规则进行命令合并（AOF重写），压缩文件大小

5. **数据恢复**

- 当Redis Server重启时，会从AOF文件按顺序载入并执行写操作，恢复数据集

### ☆AOF缓冲区三种写回策略

AOF写入策略

```
# appendfsync always
# 每次收到写命令就立即强制写入磁盘
# 最慢，但保证完全持久化，不推荐使用

appendfsync everysec
# 每秒强制写入一次磁盘
# 在性能和持久化之间做了很好的折中，推荐使用

# appendfsync no
# 完全依赖操作系统刷新
# 性能最好，但持久化没有保证
```

三种AOF写回策略小结

|   |   |   |   |
|---|---|---|---|
|配置项|写回时机|优点|缺点|
|always|同步写回|可靠性高，数据基本不丢失|每个写命令都要落盘，性能影响大|
|everysec|每秒写回|性能适中|宕机时可能丢失1秒内的数据|
|no|操作系统控制写回|性能最好|宕机时可能丢失较多数据|

### ☆AOF持久化配置

**第一步：开启AOF**

- 默认情况下，Redis没有开启AOF
- 开启AOF需要在配置文件中设置

```
1399行: appendonly yes
```

**第二步：设置AOF写入频率**

```
1458行: appendfsync everysec
```

AOF 文件配置说明：

- Redis 6 或之前版本：AOF 文件位置与 RDB 文件位置相同，通过 `dir` 配置指定
- Redis 7：除了 `dir`，新增属性 `appendfilename`【文件】 和 `appenddirname`【路径】

```
vim redis.conf

dir /usr/local/redis/
appendfilename "appendonly.aof"
appenddirname "appendonlydir"

# 查看目录
# ll /usr/local/redis/appendonlydir

# 重启Redis
pkill redis-server
bin/redis-server conf/redis.conf
```

第三步：写入测试数据

```
127.0.0.1:6379> set name devops
127.0.0.1:6379> set age 18
127.0.0.1:6379> set address beijing
```

第四步：查看测试结果

### ☆AOF生成文件说明

- Redis 6 或之前版本：AOF保存文件只有一个
- Redis 7：采用 Redis 7.0 MultiPart AOF（MP-AOF）设计，AOF保存文件分为三类

- **BASE**：基础AOF，由子进程通过重写产生，最多只有一个
- **INCR**：增量AOF，由AOFRW开始执行时创建，可能存在多个
- **MANIFEST**：清单文件，记录BASE和INCR文件信息

![[附件/ee834d4105.png]]

MP-AOF实现

- MP-AOF（MultiPart AOF）就是将原来的单个AOF文件拆分成多个文件
- AOF文件类型：

1. **BASE**：基础AOF，由子进程通过重写产生，最多只有一个【现有内容】
2. **INCR**：增量AOF，由AOFRW执行时创建，可能存在多个
3. **HISTORY**：历史AOF，由BASE和INCR的变化生成

- 每次AOFRW成功完成后，本次之前的BASE和INCR会变成HISTORY
- HISTORY类型AOF会被Redis自动删除

- **MANIFEST**（清单文件）

- 跟踪和管理BASE、INCR、HISTORY文件

![[附件/ab0487b5a7.png]]

- 所有AOF文件及MANIFEST文件放入单独目录，由 `appenddirname` 配置指定
- 便于AOF文件备份和拷贝

### ☆正常恢复

**方式一**：

提前在Redis中 `SET` 值

![[附件/1dfa64453b.png]]

此时AOF文件会生成

![[附件/20f96fc8fc.png]]

重启Redis服务，重新登录，数据依然存在

**方式二**：

将appendonlydir备份一下

```
cd /usr/local/redis
cp -r appendonlydir appendonlydir.bak
```

执行 `flushdb` 清空当前库后，再查询数据为空、执行 `shutdown` 关闭Redis

![[附件/6484cbe3c8.png]]

重启Redis后，执行 `keys *`，发现数据仍为空

原因：`flushdb` 是写操作，会更新AOF文件

恢复数据需要删除现有的AOF文件，用备份的 `appendonlydir.bak` 替换

```
rm -rf appendonlydir
mv appendonlydir.bak appendonlydir
```

重后Redis，重新登录后，发现数据已恢复！

![[附件/bb9eff5558.png]]

### ☆异常恢复

故意在正常的 **AOF 文件**乱写，模拟网络闪断文件写入的 error。【写入数据异常或写入异常数据】  
由于正常的 **AOF 文件**写入的是 `appendonly.aof.1.incr.aof`，所以只需修改该文件即可。

```
vim appendonly.aof.1.incr.aof
```

随便写入一些内容，保存并退出。  
再次重新登录时出现如下报错：拒绝连接。

由此可知，当 AOF 文件错误时，Redis 启动会失败。

修复措施：使用如下命令

```
# AOF 文件修复命令，切记一定要加上 “--fix”
redis-check-aof --fix appendonly.aof.1.incr.aof
```

![[附件/a9b747dad3.png]]

出现如上图，则修复AOF文件成功！

查看appendonly.aof.1.incr.aof 文件，发现错误语法的内容已删除。重新启动Redis，一切正常。

### ☆AOF 重写机制

AOF 一共生成 3 个文件：基础文件（base）、增量文件（incr）、清单文件（manifest，用于记录本次备份包含哪些文件）。

实际上，AOF 只有持续写入 `incr` 增量文件，随着时间增长文件会越来越大。为了解决这个问题，可以使用 AOF 重写来减小文件大小。

由于 AOF 持久化是 Redis 不断将写命令记录到 AOF 文件中，随着 Redis 持续运行，AOF 文件会越来越大。文件越大，占用服务器内存越多，并且 AOF 恢复所需时间越长。

为了解决这一问题，Redis 引入了 AOF 重写机制：

- 当 AOF 文件大小超过配置的阈值时，Redis 会自动压缩 AOF 文件内容，只保留恢复数据所需的最小指令集。
- 也可以手动执行命令 `bgrewriteaof` 来触发重写。

触发机制：通过修改 Redis 配置文件 `redis.conf` 进行设置。

![[附件/41c61fcb80.png]]

参数解析：

1. 假设 `auto-aof-rewrite-min-size` 设置为 64MB，`auto-aof-rewrite-percentage` 设置为 100：

- 当 AOF 文件首次达到 64MB 时，Redis 会进行第一次重写。重写完成后，新生成的 AOF 文件大小仍为 64MB。

2. 假设新生成的 AOF 文件大小为 64MB：

- 当 AOF 文件再次增长到 128MB（即原文件大小的 200%）时，由于当前 AOF 大小超过上次重写后的 100%（64MB * 1 + 64MB = 128MB），并且也超过了 `min-size` 的 64MB，此时会触发第二次重写。

自动触发条件：

- 同时满足 `min-size` 和 `percentage` 配置时，才会触发重写机制。
- 官方默认 AOF 文件阈值为 64MB，可手动修改。

手动触发：

- 客户端向服务端发送命令：

```
bgrewriteaof
```

#### a）自动触发机制

1. 开启 AOF 功能

```
appendonly yes
```

2. 修改 AOF 文件峰值大小为 1KB，便于测试

```
auto-aof-rewrite-min-size 1kb
```

![[附件/abf5a3de68.png]]

3. 关闭 RDB 和 AOF 混合持久化

- 默认：`yes`
- 修改为：

```
aof-use-rdb-preamble no
```

![[附件/677bfc293b.png]]

4. 删除之前所有的 RDB 和 AOF 文件，防止受外界因素影响
5. 重启 Redis 服务，执行写入操作，检查 AOF 文件是否正常
6. 查看三大相关配置

```
# 几种文件类型的前缀，后跟相关序列和类型的附加信息
appendfilename "appendonly.aof"

# Redis 7 新增加的目录配置
appenddirname "appendonlydir"

# AOF 相关文件
# 1、基本文件
appendonly.aof.1.base.rdb

# 2、增量文件
appendonly.aof.1.incr.aof
appendonly.aof.2.incr.aof

# 3、清单文件
appendonly.aof.manifest
```

7. 不停地 `set k1`，让 AOF 文件变大，一直增大到 1024KB。查看发现，`base` 文件增大，`base` 文件和 `incr` 文件名称修改为序号 2。此时，自动重写机制已触发。

注：查看 `base` 文件内容发现，不管之前怎么给 `k1` 赋值，最终 `base` 文件中只会保存最后一次赋值命令。

#### b）手工触发机制

①提前给k1赋一个其他的值

![[附件/2bad14f30a.png]]

②使用命合：bgrewriteaof

```
bgrewriteaof
```

此时发现，`base` 文件大小变化，`incr` 文件大小归 0，说明重写机制已手动触发。

AOF 文件重写并不是对原文件进行整理，而是直接读取服务器现有的键值对，然后用一条命令替代之前记录的该键值对的多条命令，生成一个新的文件后替换原来的 AOF 文件。

**AOF 重写触发机制**：  
通过 `redis.conf` 配置文件中的：

- `auto-aof-rewrite-percentage`（默认值 100）
- `auto-aof-rewrite-min-size`（默认值 64MB）

也就是说，Redis 会记录上一次重写时的 AOF 文件大小，默认配置为：当 AOF 文件大小达到上次重写后的 1 倍且文件大于 64MB 时触发。

#### C) 重写原理：

1. 在重写开始前，Redis 会创建一个**重写子进程**，该子进程不会读取现有的 AOF 文件，而是读取当前服务器上的数据库内容，将其包含的指令分析压缩后写入一个临时文件。
2. 与此同时，主进程会将新接收到的写命令一边累积到内存缓冲区中，一边继续写入原有的 AOF 文件，以保证原 AOF 文件可用，避免重写过程中出现数据丢失。
3. 当重写子进程完成工作后，会向父进程发送信号，父进程收到信号后将内存中缓存的写命令追加到新 AOF 文件中。
4. 追加完成后，Redis 用新 AOF 文件替换旧 AOF 文件，之后新的写命令都追加到新 AOF 文件中。
5. 重写 AOF 文件的操作，并没有读取旧 AOF 文件，而是将整个内存中的数据库内容用命令方式重写成新 AOF 文件，这一点和快照类似。

### ☆小结

![[附件/268a13114d.png]]

**优势**：

- AOF 文件是一个只进行追加的日志文件。
- 当 AOF 文件体积过大时，Redis 可以自动在后台进行重写。
- AOF 文件有序地保存了对数据库执行的所有写入操作，这些操作以 Redis 协议格式保存，因此内容易读，分析方便。

**缺点**：

- 对于相同的数据集，AOF 文件体积通常大于 RDB 文件体积。
- 根据所使用的 `fsync` 策略，AOF 的写入速度可能慢于 RDB。

生产环境 一般使用混合模式

## 5、扩展：No persistence（了解）

**No persistence**：完全禁用持久化。有时用于缓存，属于纯净模式。

需要同时禁用 RDB 和 AOF。

注：禁用 RDB 和 AOF 只会禁用自动触发，手动输入命令仍然可以触发 RDB 和 AOF。

### ☆禁用 RDB

- 配置文件：`save`
- 即使禁用 RDB，仍然可以手动执行命令 `SAVE` 或 `BGSAVE` 来生成 RDB 文件。

![[附件/66d91848db.png]]

### ☆禁用 AOF

- 配置文件：`appendonly no`
- 即使禁用 AOF，仍然可以手动执行命令 `BGREWRITEAOF` 来生成 AOF 文件。

![[附件/7d9e5ea68a.png]]

## 6、扩展：RDB+AOF（生产环境）

RDB+AOF：在同一个实例中同时使用AOF和RDB

### ☆共存优先级

![[附件/4ad65ea916.png]]

AOF和RDB持久化可以同时启用，不会有问题。如果启动时启用了AOF，Redis将加载AOF，即文件具有更好的持久性保证。则AOF的优先级高于RDB

### ☆数据恢复顺序及加载流程

同时开后RDB 和AOF 时，Redis 默认先优加载 AOF ，则不去加载 RDB加载RDB（可以说和RDB毫无关系）。如果AOF文件不存在，再去加载RDB

### ☆开启 RDB 和 AOF 混合模式

- 混合模式结合了 RDB 和 AOF 的优点，既能快速加载，又能避免丢失过多数据，被称为“鸳鸯锅”。
- 配置文件中 `aof-use-rdb-preamble` 的默认值为 `yes`：

- `yes` 表示开启
- `no` 表示禁用

![[附件/051d31e04d.png]]

**RDB + AOF 的混合方式**

- **原理**：RDB 用于全量持久化，AOF 用于增量持久化。
- **流程**：

1. 先使用 RDB 进行快照存储。
2. 再使用 AOF 持久化记录所有写操作。
3. 当重写策略满足或手动触发重写时，将最新数据存储为新的 RDB 记录。

- **效果**：重启服务时，Redis 会从 RDB 和 AOF 两部分恢复数据，既保证数据完整性，又提高恢复性能。
- **文件特点**：混合持久化方式生成的文件一部分是 RDB 格式，一部分是 AOF 格式，即 AOF 文件包括 RDB 头部 + AOF 指令混写。

## 5、总结

- **掌握重点**：学会开启与恢复 RDB、学会开启与恢复 AOF 即可。
- **适用场景**：

- RDB：适用于一般数据持久化，效率高，数据迁移方便。
- AOF：适合增量备份，对数据实时性要求高的场景。

- **RDB 和 AOF 同时开启**：

1. 默认加载 AOF 文件，即 Redis 会以 AOF 为准。
2. 对相同数据集，AOF 文件通常远大于 RDB 文件，恢复速度慢于 RDB。
3. AOF 写入效率低于 RDB，但同步策略效率高，异步效率与 RDB 相当。

- **概括**：

- 生产环境多为混合模式：RDB 负责全量备份，AOF 负责增量备份。
- RDB 恢复速度快，文件小。
- 如果只能选择一个：

- 一般场景用 RDB
- 对实时性要求高的场景用 AOF

# 六、Redis实际案列

## 1、主从模式

![[附件/fc045f31d0.png]]

![[附件/3ec8918d49.png]]

准备 `redis02`，需要提前安装 Redis

（如果是VMware也可以直接对redis01进行克隆）

不管以上哪种方式，都需要更改网卡Mac地址。

```
# 下载 Redis 7.4.0 源码包
wget https://download.redis.io/releases/redis-7.4.0.tar.gz

# 解压并进入目录
tar -zxvf redis-7.4.0.tar.gz
cd redis-7.4.0

# 编译
make

# 安装到指定目录
make PREFIX=/usr/local/redis install

# 创建配置目录并拷贝默认配置文件
mkdir -p /usr/local/redis/conf
cp redis.conf /usr/local/redis/conf

# 修改配置
vim /usr/local/redis/conf/redis.conf
# bind 0.0.0.0        # 允许所有 IP 连接
# daemonize yes       # 允许后台运行

# 设置内存过量分配策略，避免低内存环境下后台保存失败
sudo vim /etc/sysctl.conf
# 添加或修改
vm.overcommit_memory = 1
# 生效配置
sysctl -p
```

操作之前，可以对 `redis01` 和 `redis02` 拍摄快照，以便回滚。

**第一步：配置 Master**

```
# 编辑 Redis 配置文件
vim /usr/local/redis/conf/redis.conf
```

- 开启监听，bind 的 IP 指主机在网络中与其他服务器通讯的网卡 IP（例如 ens33）：

```
bind 0.0.0.0       # 允许所有 IP 连接
protected-mode no  # 关闭 Redis 安全保护机制，允许主从、哨兵、集群节点之间相互访问
```

---

**第二步：配置 Slave**

```
# 编辑 Redis 配置文件
vim /usr/local/redis/conf/redis.conf
```

- 设置主从信息（Redis 5/6/7 版本）：

```
replicaof 192.168.88.111 6379
```

---

**第三步：重启 Redis 服务器并查看是否成功**

```
bin/redis-cli
127.0.0.1:6379> info replication
```

---

**第四步：测试 Redis 主从（主写从读）**

```
# Master 写入
127.0.0.1:6379 master> set title itheima

# Slave 读取
127.0.0.1:6379 slave> keys *
127.0.0.1:6379 slave> get title
```

注：Slave 不允许写操作，因为从服务器配置了 `replica-read-only`，符合业务需求

```
replica-read-only yes
```

## 2、安全限制

Redis 完成基本配置后，还需要做安全配置，如 IP 限制和密码限制。

---

**① Master 配置 IP 限制**

- 注意：如果有防火墙，先关闭防火墙或放行 Redis 端口。
- `bind` 配置绑定网卡 IP：

```
# 编辑 Redis 配置文件
vim /usr/local/redis/conf/redis.conf

# 示例配置
bind 127.0.0.1       # 只允许本机连接
bind 192.168.88.111  # 同一网段内通过该 IP 访问的主机可以连接
bind 0.0.0.0         # 允许任意主机访问，公网环境必须加密码
```

- 修改后重启 Redis 服务。

---

**② Slave 远程连接测试**

```
# 远程连接 Redis
bin/redis-cli -h <远程IP地址>

# 如果设置了密码，可使用 -a 指定密码
bin/redis-cli -h <远程IP地址> -a <密码>
```

---

**③ Master 配置密码限制**

- 编辑配置文件添加 `requirepass`：

```
# vim /usr/local/redis/conf/redis.conf
requirepass <密码>   # 约在 1051 行
```

- 重启 Redis 服务后，在 Slave 测试密码是否可用：

```
127.0.0.1:6379> set name devops
# 报错: (error) NOAUTH Authentication required.
127.0.0.1:6379> auth <密码>
# 密码通过后可以正常操作
```

注意：如果开启了密码限制，搭建主从时必须在 Slave 配置中填写 Master 密码

```
# vim /usr/local/redis/conf/redis.conf
masterauth <密码>   # 约在 547 行
```

## 3、Redis 日志设置

默认情况下，Redis 没有独立日志，日志信息会写入 `/var/log/messages`。可以通过配置文件单独指定日志文件。

```
mkdir -p /var/log/redis
```

```
# 编辑配置文件
vim /usr/local/redis/conf/redis.conf

# 设置日志文件（约 356 行）
logfile "/var/log/redis/redis-server.log"
```

## 4、PHP Redis 扩展

项目：LNMP（PHP） => `.so` 扩展文件 => Redis源码安装 LNMP 后，需要手动编译安装 `redis.so` 扩展。

---

**第一步：安装 redis.so 扩展**

```
# 下载并解压 phpredis 扩展
tar xvf redis-5.3.7.tgz
cd redis-5.3.7

# 生成 configure 文件
phpize  =>PHP扩展都需要使用phpize生成./configure

# 编译并安装
./configure
make
make install
```

---

**第二步：配置 php.ini**

```
vim /usr/local/php/etc/php.ini
```

```
extension=redis.so
```

访问如下地址，查看Redis扩展是否生效[http://www.shop.com/demo.php](http://www.shop.com/demo.php)

![[附件/aba4f86c5d.png]]

**第三步：重启 php-fpm**

```
systemctl restart php-fpm
```

---

**第四步：测试 phpredis 是否安装成功**

```
vim /www/wwwroot/www.shop.com/niushop/demo.php
```

```
<?php
phpinfo();
```

---

**宝塔面板安装扩展（以 node4 / Web01 为例）**

**第一步：登录宝塔，进入软件商店**

**第二步：选择安装扩展，找到redis，单击安装**

![[附件/f5afd1f8d3.png]]

![[附件/ec71eac314.png]]

![[附件/0b2a2d8ef7.png]]

![[附件/49f26a751b.png]]

## 5、redis应用场景：niushop数据缓存与session入redis

扩展：Redis可视化软件=>Another-Redis-Desktop-Manager软件

双击安装即可

![[附件/9d75505b69.png]]

使用Another-Redis-Desktop-Manager连接Redis服务器（88.111)

![[附件/c8d1afd084.png]]

缓存设计：减少Web对MySQL的访问，减轻数据库压力

与之前session存储到file文件的方式不同，将session存储到redis中，不仅可以让我们使用各种负载调度算法，还可以实现session共享以及单点登录（sso)的操作。

www.baidu.com

pan.baidu.com

image.baidu.com

music.baidu.com

① 更改缓存保存方式

```
vim /www/wwwroot/www.shop.com/niushop/config/cache.php
```

```
return [
    // 默认缓存驱动
    'default' => Env::get('cache.driver', 'redis'), // 修改这里！！！

    // 缓存连接方式配置
    'stores' => [

        'file' => [
            // 驱动方式
            'type' => 'File',
            // 缓存保存目录
            'path' => '',
            // 缓存前缀
            'prefix' => '',
            // 缓存有效期 0 表示永久缓存
            'expire' => 0,
            // 缓存标签前缀
            'tag_prefix' => 'tag:',
            // 序列化机制
            'serialize' => [],
        ],

        // redis 缓存
        'redis' => [
            // 驱动方式
            'type' => 'redis',

            // 服务器地址
            'host' => '192.168.88.111', // 修改这里！！！

            // redis 密码
            'password' => '123456',

            // 缓存有效期
            'expire' => 604800,
        ],

    ],
];
```

---

② 更改 Session 存储位置

```
vim /www/wwwroot/www.shop.com/niushop/config/session.php
```

```
<?php

// 会话设置
return [

    // session name
    'name' => 'PHPSESSID',

    // SESSION_ID 的提交变量，解决 flash 上传跨域
    'var_session_id' => '',

    // 驱动方式 支持 file、cache
    'type' => 'cache',   // 修改这里

    // 存储连接标识（当 type 使用 cache 时有效）
    'store' => 'redis',  // 修改这里

    // 过期时间
    'expire' => 1440 * 1000,

    // 前缀
    'prefix' => 'think', // 修改这里

];
```

![[附件/1b8150e9e0.png]]

**6、nginx + lua + redis 实现访问攻击黑名单 WAF（扩展）**

WAF（Web Application Firewall）：根据 Nginx 访问流量判断是否为恶意攻击，例如 1 秒内超过一定请求数则判定为攻击。

![[附件/6741cc4a62.png]]

---

**① 安装 OpenResty（redis01）**

```
#!/bin/bash

dnf -y install pcre-devel zlib-devel openssl-devel
tar -zxf openresty-1.25.3.2.tar.gz
cd openresty-1.25.3.2
./configure
make
make install
```

---

**② 编写 Lua 脚本**

```
mkdir -p /usr/local/lua
vim /usr/local/lua/access_limit.lua
```

```
-- 释放 Redis 连接
local function close_redis(red)
    if not red then
        return
    end

    local pool_max_idle_time = 10000 -- 毫秒
    local pool_size = 100            -- 连接池大小

    local ok, err = red:set_keepalive(pool_max_idle_time, pool_size)
    if not ok then
        ngx.log(ngx.ERR, "set redis keepalive error:", err)
    end
end

-- 连接 Redis
local redis = require "resty.redis"
local red = redis:new()
red:set_timeout(1000)

local ip = "192.168.88.111" -- redis IP
local port = 6379           -- redis 端口

local ok, err = red:connect(ip, port)
red:auth("123") -- redis 密码

if not ok then
    return close_redis(red)
end

-- 获取客户端 IP
local clientIp = ngx.req.get_headers()["x-real-ip"]
if clientIp == nil then
    clientIp = ngx.req.get_headers()["x-forwarded-for"]
end
if clientIp == nil then
    clientIp = ngx.var.remote_addr
end

-- 定义 key
local incrKey = "user:" .. clientIp .. ":freq"
local blockKey = "user:" .. clientIp .. ":block"

-- 判断是否被封禁
local is_block, err = red:get(blockKey)
if tonumber(is_block) == 1 then
    ngx.exit(ngx.HTTP_FORBIDDEN)
    return close_redis(red)
end

-- 请求计数
local res, err = red:incr(incrKey)

if res == 1 then
    red:expire(incrKey, 1)
end

-- 超过阈值进行封禁（测试可设为 3~5）
if res > 100 then  
    red:set(blockKey, 1)
    red:expire(blockKey, 600) -- 设置解封时间

close_redis(red)
```

②在Nginx中添加Lua脚本：

```
# 编辑 Nginx 配置文件
vim /usr/local/openresty/nginx/conf/nginx.conf

worker_processes 1;

error_log logs/error.log;
pid logs/nginx.pid;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name localhost;

        access_log logs/host.access.log main;

        location / {
            root html;
            index index.html index.htm;

            # 引入 Lua 脚本
            access_by_lua_file /usr/local/lua/access_limit.lua;
        }

        error_page 404 /404.html;

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            root html;
        }
    }
}
```

```
# openresty = nginx + Lua 模块，本质仍是 nginx，管理命令一致

# 启动 openresty
cd /usr/local/openresty
bin/openresty

# 关闭 openresty
bin/openresty -s stop
```

面试过程中，问：是否使用过其他版本的nginx

答：使用过，上一家公司使用过openrestry，支持lua脚本，支持定制功能开发。比原生nginx更加强大。

③测试验证黑名单效果

![[附件/323b307448.png]]

**今日重点**

- 掌握 Redis 软件安装
- 掌握常见数据类型的使用（知道有哪些、会查询、会简单写）
- 持久化：RDB、AOF（会配置，理解应用场景）
- 主从复制（必须掌握）
- 安全配置（公网环境安全第一）
- Redis 扩展：使用宝塔安装 `redis.so` 扩展
- 缓存 + Session 存入 Redis（避免仅用 `ip_hash`，可实现多种调度算法）
- WAF 防火墙：OpenResty + Redis
- 哨兵模式：完成主从集群搭建
- 拓展：了解阿里云数据库 Tair（兼容 Redis®）

- [云数据库 Tair（兼容 Redis®）-云数据库 Tair（兼容 Redis®）-阿里云](https://help.aliyun.com/zh/redis)
- 写文档
- 可以了解阿里云问题解决方案

- [如何处理数据倾斜](https://help.aliyun.com/zh/redis/user-guide/deal-with-data-skew-issues?spm=a2c4g.11186623.0.i2)