# **学习目标**

- 掌握常用的kubectl get命令，包括cluster、node、label；
- 掌握YAML基本语法；
- 在kubernetes集群中部署一个nginx服务，并且能够对其进行访问。

# 【了解】node节点管理

## 查看帮助

```
kubectl --help
```

![[50a904843c.png]]

```
kubectl get --help
```

![[a8e3bdd155.png]]

## 集群

查看集群信息

```
kubectl cluster-info
```

![[05a3f459bc.png]]

## 节点

- 1 查看节点（主机）信息

```
[root@master1 ~]# kubectl get nodes
NAME      STATUS                     ROLES    AGE     VERSION
master1   Ready,SchedulingDisabled   master   3h50m   v1.30.1
master2   Ready,SchedulingDisabled   master   3h50m   v1.30.1
node1     Ready                      node     3h45m   v1.30.1
node2     Ready                      node     3h45m   v1.30.1
```

- 2 查看节点详细信息

wide宽

```
kubectl get nodes -o wide
```

![[69e374a848.png]]

- 3 描述节点详细信息

经常用来定位节点错误信息

```
[root@master1 ~]# kubectl describe node master1
```

![[5786f83e8f.png]]

- 4 node节点管理集群

**如果是kubeasz安装，所有节点(包括master与node)都已经可以对集群进行管理**，在$HOME/.kube/config文件中配置的；

如果是kubeadm安装，有的情况下，在node节点上，管理时会报如下错误

```
[root@node1 ~]# kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

![[e3944b567b.png]]

只要把master上的管理文件/etc/kubernetes/admin.conf拷贝到node节点的$HOME/.kube/config就可以让node节点也可以实现kubectl命令管理

1, 在node节点的用户家目录创建.kube目录

```
[root@node1 ~]# mkdir /root/.kube
```

2, 在master节点做如下操作

```
[root@master ~]# scp /etc/kubernetes/admin.conf node1:/root/.kube/config
```

![[6dcfe67839.png]]

![[1226fe8782.png]]

3, 在node节点验证

```
[root@node1 ~]# kubectl get nodes
NAME     STATUS   ROLES    AGE    VERSION
master   Ready    master    2h    v1.15.1
node1    Ready    node      2h    v1.15.1
node2    Ready    node      2h    v1.15.1
```

![[44199c20b2.png]]

## 节点标签(label)

k8s集群如果由大量节点组成，可将节点打上对应的标签，然后通过标签进行筛选，查看

### 1 查看节点标签信息

```
kubectl get nodes --show-labels
```

![[02bc8a69a6.png]]

### 2 设置节点标签信息

为节点master1打一个region=huanan 的标签

```
kubectl label node master1 region=huanan
```

查看所有节点标签

```
kubectl get node --show-labels
```

![[b35a6c2d90.png]]

重复打标签，需要增加 --overwrite 参数

查看所有节点带region的标签

```
kubectl get nodes -L region
```

![[702c0a686c.png]]

```
kubectl get nodes -L region,locate
kubectl get node -L region -L locate
```

![[00d9aa06e8.png]]

标签定义时，大小写敏感

![[d4423d0663.png]]

### 3 **标签的修改**

```
# 加上--overwrite=true 覆盖原标签的value进行修改操作
kubectl label node 192.168.122.14 bussiness=ad --overwrite=true
```

![[442bad356d.png]]

按照官方帮助手册，标签名称只能以数字或字母做开头或结尾，比如 country-、-country都是非法的； coun-try是合法的；

![[48491d7ce5.png]]

```
# 查询节点，并指定标签列
[root@master1 ~]# kubectl get nodes -L bussiness
NAME             STATUS                     ROLES    AGE    VERSION   BUSSINESS
192.168.122.11   Ready,SchedulingDisabled   master   5d1h   v1.18.3
192.168.122.12   Ready,SchedulingDisabled   master   5d1h   v1.18.3
192.168.122.13   Ready                      node     5d1h   v1.18.3
192.168.122.14   Ready                      node     5d1h   v1.18.3   ad
```

![[0703757f66.png]]

### 5 **标签的删除**

使用key加一个减号的写法来取消标签

```
kubectl label node 192.168.122.14 region- zone- env- bussiness-
```

![[81ae721586.png]]

### 6 标签选择器

标签选择器主要有2类:

- 等值关系: =, !=
- 集合关系: KEY in {VALUE1, VALUE2......}

```
# 先赋值一个标签
kubectl label node 192.168.122.13 bussiness=game
node/192.168.122.13 labeled

# 先赋值一个标签
kubectl label node 192.168.122.14 bussiness=ad
node/192.168.122.14 labeled
```

```
# in 子句
[root@master1 ~]# kubectl get node -l "bussiness in (game,ad)"
NAME             STATUS   ROLES   AGE    VERSION
192.168.122.13   Ready    node    5d1h   v1.18.3
192.168.122.14   Ready    node    5d1h   v1.18.3
```

```
# 查询节点
kubectl get node -l kubernetes.io/role=master
```

![[f4ea2dd6e8.png]]

## 总结

k8s集群中, node是一种资源（后面还要学习很多的常见资源，如namespace,pod,deployment,service等) 很多资源类型都可以打标签 标签是为了更好的进行资源对象的相关选择与匹配 -l ？？？ -L ？？？ 在企业里，对K8S进行二开的时候，会封装Web界面，进行打标签和检索；

常用命令：

1、kubectl cluster-info

2、kubectl get node [-o wide]

3、kubectl describe node [node名称]

4、kubectl --help 自主学习

# 【掌握】资源管理介绍

## YAML语言介绍

YAML是一个类似 XML、JSON 的标记性语言。它强调以**数据**为中心，并不是以标识语言为重点。因而YAML本身的定义比较简单，号称"一种人性化的数据格式语言"。

### ☆ YAML vs XML

XML

```
<heima>
    <age>15</age>
    <address>Beijing</address>
</heima>
```

YAML

```
heima:
  age: 15
  address: Beijing
```

![[03d79f6be9.png]]

### ☆ 相关语法

YAML的语法比较简单，主要有下面几个：

- 大小写敏感；
- '#'表示注释；
- 缩进

- 使用缩进表示层级关系
- 缩进不允许使用tab，只允许空格( 低版本限制 )
- 缩进的**空格数不重要**，只要**相同层级的元素左对齐**即可

【历史背景】

1、早期编程当中，语言功能单一，全都是大写字母，在英文中也比较正式。后来新诞生的一些语言（比如1972年的C语言），支持了更多字符，也支持了大小写，并带来了书写习惯的改变。因此，为了和老代码兼容，许多新编译器，就支持自动转换成大写，进行词法解析，由此产生了大小写不敏感的风格；

2、在传统的编程中，大部分是{}形式表示代码块，而不是缩进形式；

3、为了防止tab（默认4个空格）和空格的误用和报错，现代的IDE对于YAML，基本上是**默认2个空格缩进**

### ☆ 数据类型

- 标量类型（Scalar Types）：单个的、不可再分的值
- 序列类型（Sequence Types）：一组按次序排列的值，又称为数组Array / 列表List
- 映射类型（Mapping Types）：键值对的集合，又称为映射Mapping/ 哈希Hash / 字典Dictionary

```
# 纯量, 就是指的一个简单的值，字符串、布尔值、整数、浮点数、null、时间、日期
# 1 布尔类型
c1: true (或者True，不区分大小写)

# 2 整型
c2: 234

# 3 浮点型
c3: 3.14

# 4 null类型 
c4: ~  # 使用~或者null，或者什么都不输入

# 5 日期类型
c5: 2018-02-17    # 日期必须使用ISO 8601格式，即yyyy-MM-dd

# 6 时间类型
c6: 2018-02-17T15:02:31+08:00  # 时间使用ISO 8601格式，时间和日期之间使用T连接，最后使用+代表时区

UTC 统一世界协调时


# 7 字符串类型
c7: heima     # 简单写法，直接写值，如果字符串中间有特殊字符，必须使用双引号或单引号包裹 

c8: line1
    line2     # 字符串过多的情况可以拆成多行，每一行前后的多个空格会被转化成一个空格
```

![[0d0cb59ebd.png]]

```
# 序列类型
# 形式一(推荐):
address:
  - 顺义
  - 昌平
  - 14.5

# 形式二(了解):
address: [顺义,昌平]
```

![[9b0e4b20e6.png]]

```
# 映射(Mapping)类型
# 形式一(推荐):
heima:
  age: 15
  address: Beijing

# 形式二(了解):
heima: {age: 15,address: Beijing}
```

学过的三种数据类型，可以随意组合嵌套，从而生成丰富的Yaml数据形式；

![[cebd2cde85.png]]

小提示：

1 书写yaml切记: 后面要加一个空格

2 如果需要将多段Yaml配置放在一个文件中，中间要使用---分隔

3 下面是一个yaml转json的网站，可以通过它验证yaml是否书写正确

https://www.json2yaml.com/convert-yaml-to-json

![[feb5d89274.png]]

总结 1、Yaml数据类型：____类型、____类型、____类型； 2、Yaml语法：大小写____、缩进要左____、注释是用____； 3、在搜索引擎上搜索 Yaml在线，就可以找到一些在线校验网站，进行自主学习。

## 资源管理方式

在kubernetes中，所有的内容都抽象为资源，用户需要通过操作资源来管理kubernetes。

```
kubectl --help
```

![[8bb41846ad.png]]

**【容器】**kubernetes的本质上就是一个集群系统，用户可以在集群中部署各种服务，所谓的部署服务，其实就是在kubernetes集群中运行一个个的容器，并将指定的程序跑在容器中。

**【Pod】**kubernetes的最小管理单元是pod而不是容器，所以只能将容器放在Pod中，而kubernetes一般也不会直接管理Pod，而是通过Pod控制器来管理Pod的（可以把Pod理解成一个个逻辑主机）。

Pod可以提供服务之后，就要考虑如何访问Pod中服务，kubernetes提供了Service资源实现这个功能。

**【存储】**当然，如果Pod中程序的数据需要持久化，kubernetes还提供了各种存储系统（ConfigMap、Secret）。

![[b220b5b7ed.png]]

在Kubernetes当中，对资源的管理方式，整体分为两大类——**命令式**和**声明式**；

- 命令式对象**管理**：直接使用命令去操作kubernetes资源

kubectl run nginx-pod --image=nginx:1.17.1 --port=80

- **命令式**对象**配置**：通过命令配置和配置文件去操作kubernetes资源

kubectl create/patch -f nginx-pod.yaml

- **声明式**对象**配置**：通过apply命令和配置文件去操作kubernetes资源

kubectl apply -f nginx-pod.yaml

|   |   |   |   |   |
|---|---|---|---|---|
|类型|操作对象|适用环境|优点|缺点|
|命令式对象管理|对象|测试|简单|只能操作活动对象，无法审计、跟踪|
|命令式对象配置|文件|开发|可以审计、跟踪|项目大时，配置文件多，操作麻烦|
|声明式对象配置|文件或目录|开发|支持目录操作|意外情况下难以调试|

**小结**

1、命令式和声明式是Kubernetes当中，常见的两种资源管理方式；

2、命令式适合测试和调试，由于没有审计和跟踪记录，生产上很少用； 3、声明式 apply 支持版本管理，操作记录；

### ☆ 命令式对象管理

#### **kubectl命令**

集群中的管理操作几乎都可以使用kubectl命令完成。

kubectl是kubernetes集群的命令行工具，通过它能够对集群本身进行管理，并能够在集群上进行容器化应用的安装部署。kubectl命令的语法如下：

kubectl [command] [type] [name] [flags]

**comand**：指定要对资源执行的操作，例如create、get、delete

**type**：指定资源类型，比如deployment、pod、service

**name**：指定资源的名称，名称大小写敏感

**flags**：指定额外的可选参数

```
[root@master ~]# kubectl get nodes
```

**资源类型**

kubernetes中所有的内容都抽象为资源，可以通过下面的命令进行查看:

```
kubectl api-resources
```

#### 资源

经常使用的资源有下面这些：

|   |   |   |   |
|---|---|---|---|
|资源分类|资源名称|缩写|资源作用|
|集群级别资源|**nodes**|no|集群组成部分|
|namespaces|**namespaces**|ns|隔离Pod|
|pod资源|**pods**|po|装载容器|
|pod资源控制器|replicationcontrollers|rc|控制pod资源|
||replicasets|rs|控制pod资源|
||**deployments**|deploy|控制pod资源|
||daemonsets|ds|控制pod资源|
||jobs||控制pod资源|
||cronjobs|cj|控制pod资源|
||horizontalpodautoscalers|hpa|控制pod资源|
||statefulsets|sts|控制pod资源|
|服务发现资源|**services**|svc|统一pod对外接口|
||**ingress**|ing|统一pod对外接口|
|存储资源|volumeattachments||存储|
||persistentvolumes|pv|存储|
||persistentvolumeclaims|pvc|存储|
|配置资源|**configmaps**|cm|配置|
||**secrets**||配置|

#### **操作**

kubernetes允许对资源进行多种操作，可以通过--help查看详细的操作命令

```
kubectl --help
```

经常使用的操作有下面这些：

|   |   |   |   |
|---|---|---|---|
|命令分类|命令|翻译|命令作用|
|基本命令|**create**|创建|创建一个资源|
||**edit**|编辑|编辑一个资源|
||**get**|获取|获取一个资源|
||**patch**|更新|更新一个资源|
||**delete**|删除|删除一个资源|
||explain|解释|展示资源文档|
|运行和调试|run|运行|在集群中运行一个指定的镜像|
||expose|暴露|暴露资源为Service|
||**describe**|描述|显示资源内部信息|
||**logs**|日志输出容器在 **pod** 中的日志|输出容器在 pod 中的日志|
||attach|缠绕进入运行中的容器|进入运行中的容器|
||**exec**|执行容器中的一个命令|执行容器中的一个命令|
||**cp**|复制|在Pod内外复制文件|
||rollout|首次展示|管理资源的发布|
||scale|规模|扩(缩)容Pod的数量|
||autoscale|自动调整|自动调整Pod的数量|
|高级命令|**apply**|应用|通过文件对资源进行配置|
||label|标签|更新资源上的标签|
|其他命令|cluster-info|集群信息|显示集群信息|
||version|版本|显示当前Server和Client的版本|

下面以一个namespace / pod的创建和删除简单演示下命令的使用：

```
# 创建一个namespace
[root@master ~]# kubectl create namespace dev
namespace/dev created

# 获取namespace
[root@master ~]# kubectl get ns
NAME              STATUS   AGE
default           Active   21h
dev               Active   21s
kube-node-lease   Active   21h
kube-public       Active   21h
kube-system       Active   21h

# 在此namespace下创建并运行一个nginx的Pod
# 由于 docker.io 和镜像代理，有时遇到网速问题，这里我们直接指明镜像源
[root@master ~]# kubectl run nginx --image=cf-workers-docker-io-38g.pages.dev/nginx:1.24.0 -n dev
# 下面是输出结果
pod/nginx created

# 查看新创建的pod
[root@master ~]# kubectl get pods -n dev
NAME   READY    STATUS    RESTARTS   AGE
nginx   1/1     Running   0          21s

# 查看详细信息
[root@master ~]# kubectl deacribe pod -n dev pod名字


# 删除指定的pod
[root@master ~]# kubectl delete pod nginx -n dev
pod "nginx" deleted

# 删除指定的namespace
[root@master ~]# kubectl delete ns dev
namespace "dev" deleted
```

![[4f22072447.png]]

### ☆ 命令式对象配置

命令式对象配置就是使用命令配合配置文件一起来操作kubernetes资源。

1） 创建一个pod-nginx.yaml，内容如下：

（AKMN写法） Manifest (资源清单)

```
apiVersion: v1                # API 版本  api-versions
kind: Namespace               # 资源类型
metadata:                     # 元数据
  name: dev                   # 名称

---

apiVersion: v1
kind: Pod
metadata:
  name: nginx  # pod名称
  namespace: dev
spec:
  containers:
  - name: nginx-containers  # pod中容器名称，可以与pod名称相同也可以不同
    image: registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 # 为了拉取镜像较快，我们特别地，指定了镜像源
    imagePullPolicy: IfNotPresent        # 默认值
```

2）执行create命令，创建资源：

```
[root@master ~]# kubectl create -f pod-nginx.yaml
namespace/dev created
pod/nginxpod created
```

此时发现创建了两个资源对象，分别是namespace和pod

![[c861da7a73.png]]

3）执行get命令，查看资源：

```
[root@master ~]#  kubectl get -f pod-nginx.yaml
NAME            STATUS   AGE
namespace/dev   Active   18s

NAME            READY   STATUS    RESTARTS   AGE
pod/nginxpod    1/1     Running   0          17s
```

这样就显示了两个资源对象的信息

![[8c096009e5.png]]

4）执行delete命令，删除资源：

```
[root@master ~]# kubectl delete -f pod-nginx.yaml
namespace "dev" deleted
pod "nginxpod" deleted
```

此时发现两个资源对象被删除了

![[6839036cc0.png]]

总结:

命令式对象配置的方式操作资源，可以简单的认为：命令 + Yaml配置文件（里面是命令需要的各种参数）

命令：

- create -f 创建
- get -f 查看
- delete -f 删除

### ☆ 声明式对象配置（推荐）

**声明式对象配置**跟**命令式对象配置**很相似，但是它只有一个命令apply。

```
# 首先执行一次kubectl apply -f yaml文件，发现创建了资源
[root@master ~]#  kubectl apply -f pod-nginx.yaml
namespace/dev created
pod/busybox created

# 再次执行一次kubectl apply -f yaml文件，发现说资源没有变动
[root@master ~]#  kubectl apply -f pod-nginx.yaml
namespace/dev unchanged
pod/busybox unchanged
```

总结:

其实声明式对象配置就是使用apply描述一个资源最终的状态（在yaml中定义状态）

使用apply操作资源：

如果资源不存在，就创建，相当于 kubectl create

如果资源已存在，就更新，相当于 kubectl patch

apply会记录历史数据，并存放到注解当中

![[65776080c6.png]]

或者使用

```
kubectl edit pod -n dev nginx
```

![[bac1a093d8.png]]

使用推荐: 三种方式应该怎么用 ?

- 创建/更新资源 使用声明式对象配置 kubectl apply -f XXX.yaml
- 删除资源 使用命令式对象配置 kubectl delete -f XXX.yaml
- 查询资源 使用命令式对象管理 kubectl get(describe) 资源名称
- 查看详情 使用 kubectl describe 资源名称

![[d9d02a3917.png]]

## 总结

1、Yaml语言以______为中心，没有复杂的标识语言；**数据 (Data)**

2、Yaml语言对大小写是否敏感？ **是 (Yes)**。

3、Yaml语言对缩进格数有没有要求？但是要求相同的缩进，必须左对齐； （通常习惯用 **2 个空格**），但**严禁使用 Tab 键**。

4、以下是常用的命令

kubectl get node/pod/namespace/secret/configmap xxx

kubectl edit pod/deployment -n kube-system xxx

kubectl describe pod -n kube-system xxx

kubectl delete pod -n kube-system

kubectl create/apply -f xxx.yaml

5、以下命令有什么区别？

kubectl get pod -n dev nginx

摘要式表格。

kubectl get pod -n dev nginx -o yaml

【yaml格式输出】

**输出：** 完整的资源定义。

![[4f94385857.png]]

# 【实践】部署Niginx服务

## Namespace

### 相关概念

Namespace是kubernetes集群中的一种非常重要资源，它的主要作用是用来实现**多套环境的资源隔离**或者**多租户的资源隔离**。

默认情况下，kubernetes集群中的所有的Pod都是可以相互访问的。但是在实际中，可能不想让两个Pod之间进行互相的访问，那此时就可以将两个Pod划分到不同的namespace下。kubernetes通过将集群内部的资源分配到不同的Namespace中，可以形成逻辑上的"组"，以方便不同的组的资源进行隔离使用和管理。

可以通过kubernetes的授权机制，将不同的namespace交给不同租户进行管理，这样就实现了多租户的资源隔离。

![[70d6fd7774.png]]

kubernetes在集群启动之后，会默认创建几个namespace

```
[root@master ~]# kubectl get namespace
NAME              STATUS   AGE
default           Active   45h     #  所有未指定Namespace的对象都会被分配在default命名空间
kube-node-lease   Active   45h     #  集群节点之间的心跳维护，v1.13开始引入
kube-public       Active   45h     #  此命名空间下的资源可以被所有人访问（包括未认证用户）
kube-system       Active   45h     #  所有由Kubernetes系统创建的资源都处于这个命名空间
```

![[3f4c30a72a.png]]

下面来看namespace资源的具体操作：

### **查看**

```
# 1 查看所有的ns  命令：kubectl get ns
[root@master ~]# kubectl get ns
NAME              STATUS   AGE
default           Active   45h
kube-node-lease   Active   45h
kube-public       Active   45h     
kube-system       Active   45h     

# 2 查看指定的ns   命令：kubectl get ns ns名称
[root@master ~]# kubectl get ns default
NAME      STATUS   AGE
default   Active   45h

# 3 指定输出格式  命令：kubectl get ns ns名称  -o 格式参数
# kubernetes支持的格式有很多，比较常见的是wide、json、yaml
[root@master ~]# kubectl get ns default -o yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: "2021-05-08T04:44:16Z"
  name: default
  resourceVersion: "151"
  selfLink: /api/v1/namespaces/default
  uid: 7405f73a-e486-43d4-9db6-145f1409f090
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
  
# 4 查看ns详情  命令：kubectl describe ns ns名称
[root@master ~]# kubectl describe ns default
Name:         default
Labels:       <none>
Annotations:  <none>
Status:       Active  # Active 命名空间正在使用中  Terminating 正在删除命名空间

# ResourceQuota 针对namespace做的资源限制
# LimitRange针对namespace中的每个组件做的资源限制
No resource quota.
No LimitRange resource.
```

### **创建**

```
# 创建namespace
[root@master ~]# kubectl create ns dev
namespace/dev created
```

### **删除**

```
# 删除namespace
[root@master ~]# kubectl delete ns dev
namespace "dev" deleted
```

### **Yaml形式**

首先准备一个yaml文件：ns-dev.yaml

```
apiVersion: v1
kind: Namespace
metadata:
  name: dev
```

然后就可以执行对应的创建和删除命令了：

创建：kubectl create -f ns-dev.yaml

删除：kubectl delete -f ns-dev.yaml

## Pod

### 相关概念

Pod是kubernetes集群进行管理的最小单元，程序要运行必须部署在容器中，而容器必须存在于Pod中。

Pod可以认为是容器的封装，一个Pod中可以存在一个或者多个容器。

![[dfbab22e8f.png]]

kubernetes在集群启动之后，集群中的各个组件也都是以Pod方式运行的。可以通过下面命令查看：

```
[root@master ~]# kubectl get pod -n kube-system
NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE
kube-system   coredns-6955765f44-68g6v         1/1     Running   0          2d1h
kube-system   coredns-6955765f44-cs5r8         1/1     Running   0          2d1h
kube-system   etcd-master                      1/1     Running   0          2d1h
kube-system   kube-apiserver-master            1/1     Running   0          2d1h
kube-system   kube-controller-manager-master   1/1     Running   0          2d1h
kube-system   kube-flannel-ds-amd64-47r25      1/1     Running   0          2d1h
kube-system   kube-flannel-ds-amd64-ls5lh      1/1     Running   0          2d1h
kube-system   kube-proxy-685tk                 1/1     Running   0          2d1h
kube-system   kube-proxy-87spt                 1/1     Running   0          2d1h
kube-system   kube-scheduler-master            1/1     Running   0          2d1h
```

### **创建并运行**

kubernetes没有提供单独运行Pod的命令，都是通过Pod控制器来实现的

```
# 命令格式： kubectl run (pod控制器名称) [参数] 
kubectl run nginx --image=registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 --port=80 --namespace dev 

# --image  指定Pod的镜像
# --port   指定端口
# --namespace  指定 namespace
# 具体参数，可以查看 
    kubectl run --help
    kubectl options
```

![[50cf166d19.png]]

### **查看**

```
# 查看Pod基本信息
[root@master ~]# kubectl get pods -n dev
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          43s

# 查看Pod的详细信息(排错)
[root@master ~]# kubectl describe pod nginx -n dev
Name:         nginx
Namespace:    dev
Priority:     0
Node:         node1/192.168.5.4
Start Time:   Wed, 08 May 2021 09:29:24 +0800
Labels:       pod-template-hash=5ff7956ff6
              run=nginx
Annotations:  <none>
Status:       Running
IP:           10.244.1.23
IPs:
  IP:           10.244.1.23
Controlled By:  ReplicaSet/nginx
Containers:
  nginx:
    Container ID:   docker://4c62b8c0648d2512380f4ffa5da2c99d16e05634979973449c98e9b829f6253c
    Image:          nginx:1.24.0
    Image ID:       docker-pullable://nginx@sha256:485b610fefec7ff6c463ced9623314a04ed67e3945b9c08d7e53a47f6d108dc7
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 08 May 2021 09:30:01 +0800
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-hwvvw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-hwvvw:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-hwvvw
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason     Age        From               Message
  ----    ------     ----       ----               -------
  Normal  Scheduled  <unknown>  default-scheduler  Successfully assigned dev/nginx-5ff7956ff6-fg2db to node1
  Normal  Pulling    4m11s      kubelet, node1     Pulling image "nginx:1.24.0"
  Normal  Pulled     3m36s      kubelet, node1     Successfully pulled image "nginx:1.24.0"
  Normal  Created    3m36s      kubelet, node1     Created container nginx
  Normal  Started    3m36s      kubelet, node1     Started container nginx
```

### **访问**

```
# 获取podIP
[root@master ~]# kubectl get pods -n dev -o wide
NAME    READY   STATUS    RESTARTS   AGE    IP             NODE    ... 
nginx   1/1     Running   0          190s   10.244.1.23   node1   ...

#访问POD
[root@master ~]# curl http://10.244.1.23:80
<!DOCTYPE html>
<html>
<head>
	<title>Welcome to nginx!</title>
</head>
<body>
	<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

### **删除**

```
# 删除指定Pod
[root@master ~]# kubectl delete pod nginx -n dev
pod "nginx" deleted

[root@master ~]# kubectl delete pod nginx -n dev --force
```

### **Yaml形式**

创建一个pod-nginx.yaml，内容如下：

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: dev
spec:
  containers:
  - image: registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
    name: pod
    imagePullPolicy: IfNotPresent
    ports:
    - name: nginx-port
      containerPort: 80
      protocol: TCP
```

然后就可以执行对应的创建和删除命令了：

创建：kubectl create -f pod-nginx.yaml

删除：kubectl delete -f pod-nginx.yaml

### 常见报错

#### **1、镜像拉取失败**

![[d14fef5483.png]]

![[85aff4b9c1.png]]

#### 2、命名空间没有创建

![[d119e81235.png]]

需要创建命名空间

```
kubectl create ns dev
```

#### 3、名称中包含下划线，提示无效

![[191830847f.png]]

把nginx_run改成nginx-run可以了，改成中划线。

## Label

Label是kubernetes系统中的一个重要概念。它的作用就是在资源上添加标识，用来对它们进行区分和选择。

### 相关特性

- 一个Label会以key/value键值对的形式附加到各种对象上，如Node、Pod、Service等等
- 一个资源对象可以定义任意数量的Label ，同一个Label也可以被添加到任意数量的资源对象上去
- Label通常在资源对象定义时确定，当然也可以在对象创建后动态添加或者删除

可以通过Label实现资源的多维度分组，以便灵活、方便地进行资源分配、调度、配置、部署等管理工作。

### 相关案例

- 版本标签："version":"release", "version":"stable"......
- 环境标签："environment":"dev"，"environment":"test"，"environment":"pro"
- 架构标签："tier":"frontend"，"tier":"backend"

## Deployment 部署

在kubernetes中，Pod是最小的控制单元，但是kubernetes很少直接控制Pod，一般都是通过Pod控制器来完成的。

### 相关概念

Pod控制器用于pod的管理，确保pod资源符合预期的状态，当pod的资源出现故障时，会尝试进行重启或重建pod。

在kubernetes中Pod控制器的种类有很多，本章节只介绍一种：Deployment。

![[0f8754594f.png]]

![[847b3166d7.png]]

![[2bfa28d9f9.png]]

### **命令操作**

```
# 命令格式: kubectl create deployment 名称  [参数] 
# --image  指定pod的镜像
# --port   指定端口
# --namespace  指定namespace
[root@master ~]# kubectl create deploy deploy-nginx --image=registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 -n dev
deployment.apps/nginx created

速查手册
    kubectl options
    kubectl run --help
    kubectl run pod-nginx --image=xxx -n dev
    kubectl create deploy --image=xxx -n dev
    kubectl get deploy -n dev
    kubectl get pod -n dev
    kubectl delete pod -n dev xxx


# scale       弹性扩容
# --replicas  指定创建pod数量
[root@master ~]# kubectl scale deployment deploy-nginx --replicas=3 -n dev


# 查看创建的Pod
[root@master ~]# kubectl get pods -n dev
NAME                     READY   STATUS    RESTARTS   AGE
nginx-5ff7956ff6-6k8cb   1/1     Running   0          19s
nginx-5ff7956ff6-jxfjt   1/1     Running   0          19s
nginx-5ff7956ff6-v6jqw   1/1     Running   0          19s


# 查看deployment的信息
[root@master ~]# kubectl get deploy -n dev
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   3/3     3            3           2m42s


# UP-TO-DATE：成功升级的副本数量
# AVAILABLE：可用副本的数量
[root@master ~]# kubectl get deploy -n dev -o wide
NAME    READY UP-TO-DATE  AVAILABLE   AGE     CONTAINERS   IMAGES              SELECTOR
nginx   3/3     3         3           2m51s   nginx        nginx:1.24.0        run=nginx

kubectl get all
kubectl describe deploy
kubectl describe pod
kubectl describe node

# 查看deployment的详细信息
[root@master ~]# kubectl describe deploy nginx -n dev
Name:                   nginx
Namespace:              dev
CreationTimestamp:      Wed, 08 May 2021 11:14:14 +0800
Labels:                 run=nginx
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               run=nginx
Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  run=nginx
  Containers:
   nginx:
    Image:        nginx:1.24.0
    Port:         80/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   nginx-5ff7956ff6 (3/3 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  5m43s  deployment-controller  Scaled up replicaset nginx-5ff7956ff6 to 3
  
# 删除 
[root@master ~]# kubectl delete deploy nginx -n dev
deployment.apps "nginx" deleted
```

![[acc69198df.png]]

### **Yaml形式**

创建一个deploy-nginx.yaml，内容如下：

```
kubectl create deploy nginx-deploy-wuhan --image=registry.openanolis.cn/openanolis/nginx:1.14.1-8.6 -n dev -r 3
```

```
apiVersion: v1
kind: Namespace
metadata:
  name: dev
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  namespace: dev
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
          protocol: TCP
```

```
---                        # 资源分隔符，用于在同一个 YAML 文件中定义多个对象
apiVersion: apps/v1        # 资源版本，Deployment 属于 apps 组的 v1 版本
kind: Deployment           # 资源类型：部署
metadata:                  # 元数据
  name: nginx              # Deployment 的名称
  namespace: dev           # 指定将该资源部署在之前定义的 "dev" 命名空间中
spec:                      # 规格定义（期望状态）
  replicas: 3              # 副本数：维持 3 个运行 Nginx 的 Pod
  selector:                # 选择器：定义 Deployment 如何找到它管理的 Pod
    matchLabels:           # 标签匹配规则
      app: nginx           # 匹配标签为 "app: nginx" 的 Pod
  template:                # Pod 模板：当副本数不足时，根据此模板创建新 Pod
    metadata:              # Pod 的元数据
      labels:              # Pod 的标签（必须与上面的 selector 匹配）
        app: nginx
    spec:                  # Pod 的内部规格
      containers:          # 容器配置（一个 Pod 可以包含多个容器）
      - name: nginx        # 容器名称
        # 镜像地址：使用龙蜥（Anolis）官方仓库的 Nginx 镜像
        image: registry.openanolis.cn/openanolis/nginx:1.14.1-8.6
        # 镜像拉取策略：IfNotPresent（如果本地已有镜像则不从远程仓库拉取）
        imagePullPolicy: IfNotPresent 
        ports:             # 容器暴露的端口
        - containerPort: 80 # 容器内部监听 80 端口
          protocol: TCP     # 使用 TCP 协议
```

更多参数，可以查看

kubectl explain pod

然后就可以执行对应的创建和删除命令了：

创建：kubectl create -f deploy-nginx.yaml

删除：kubectl delete -f deploy-nginx.yaml

### 【扩展】API Resources

有的写 apiVersion: apps/v1， 有的写 apiVersion: v1，怎么确定该选哪个

```
kubectl api-resources                      # 默认查看 

kubectl api-resources --help               # 帮助手册

kubectl api-resources --api-group=apps     # 筛选 apps 的组件
```

![[2be1959464.png]]

## Service 服务

通过上节课的学习，已经能够利用Deployment来创建一组Pod来提供具有高可用性的服务。

假设每个pod每天宕机的概率是10%，如果设置3个副本，每天服务宕机的概率是？ 10% * 10% * 10% = 0.1%

虽然每个Pod都会分配一个单独的Pod IP，然而却存在如下两问题：

- Pod IP 会随着Pod的重建产生变化
- Pod IP 仅仅是集群内可见的虚拟IP，外部无法访问

![[5166dff509.png]]

这样对于访问这个服务带来了难度。因此，kubernetes设计了Service来解决这个问题。

### 相关概念

Service可以看作是一组同类Pod**对外的访问入口**。借助Service，应用可以方便地实现服务发现和负载均衡。

![[5e85f6dc3c.png]]

### 命令操作

![[86b90dd203.png]]

#### **1、创建集群内部可访问的Service**

```
# 暴露Service
[root@master ~]# kubectl expose deploy nginx --name=svc-nginx1 --type=ClusterIP --port=80 --target-port=80 -n dev
service/svc-nginx1 exposed

# 查看service
[root@master ~]# kubectl get svc svc-nginx1 -n dev -o wide
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE     SELECTOR
svc-nginx1   ClusterIP   10.109.179.231   <none>        80/TCP    3m51s   run=nginx

# 这里产生了一个CLUSTER-IP，这就是service的IP，在Service的生命周期中，这个地址是不会变动的
# 可以通过这个IP访问当前service对应的POD
[root@master ~]# curl 10.109.179.231:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
</head>
<body>
<h1>Welcome to nginx!</h1>
.......
</body>
</html>
```

![[7d6dd0e338.png]]

#### **2、创建集群外部也可访问的Service**

```
# 上面创建的Service的type类型为ClusterIP，这个ip地址只用集群内部可访问
# 如果需要创建外部也可以访问的Service，需要修改type为NodePort
[root@master ~]# kubectl expose deploy nginx --name=svc-nginx2 --type=NodePort --port=80 --target-port=80 -n dev
service/svc-nginx2 exposed

# 此时查看，会发现出现了NodePort类型的Service，而且有一对Port（80:31928/TCP）
[root@master ~]# kubectl get svc svc-nginx2 -n dev -o wide
NAME          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE    SELECTOR
svc-nginx2    NodePort    10.100.94.0      <none>        80:31928/TCP   9s     run=nginx

# 接下来就可以通过集群外的主机访问 (任意)节点IP:31928访问服务了
# 例如在的电脑主机上通过浏览器访问下面的地址
http://192.168.88.135:31928/
```

#### **3、删除Service**

```
[root@master ~]# kubectl delete svc svc-nginx-1 -n dev
service "svc-nginx-1" deleted

或者
kubectl get all -n dev 
kubectl delete -n dev service/svc-nginx
```

### **Yaml形式**

创建一个svc-nginx.yaml，内容如下：

```
apiVersion: v1
kind: Service
metadata:
  name: svc-nginx
  namespace: dev
spec:
  ports:
  - port: 80                  # Service 端口
    protocol: TCP
    targetPort: 80            # Pod 端口
  selector:
    app: nginx
  type: ClusterIP
```

```
kubectl api-resources         # 可以查看资源版本
kubectl describe svc -n dev xxx
```

![[21f5fd8917.png]]

然后就可以执行对应的创建和删除命令了：

创建：kubectl apply -f svc-nginx.yaml

删除：kubectl delete -f svc-nginx.yaml

## **总结**

至此，已经掌握了Namespace、Pod、Deployment、Service资源的基本操作。

有了这些操作，就可以在kubernetes集群中实现一个服务的简单部署和访问了。

但是如果想要更好的使用kubernetes，就需要深入学习这几种资源的细节和原理。

![[30aed282e7.png]]

# 【掌握】Pod基础

## Pod基本概念

![[b38f611aa7.png]]

**Docker、Container、Pod之间的关系**

Dock表示码头。Docker表示在码头上的工人，码头工，他们干的事情就是搬运集装箱（调度容器）。

Container就是表示容器。

DotCloud公司开发了一款产品Paas云平台产品docker。由于docker太火了，干脆就把自己公司的名字改成了Docker。

- Pod是Kubernetes最小的管理单位,一个Pod可以封装**一个容器或多个容器**
- 一个Pod里的多个容器可以**共享存储和网络**, 可以看作一个逻辑的主机
- 多个容器共享同一个network namespace，由此在一个Pod里的多个容器共享Pod的IP和端口namespace，所以一个Pod内的多个容器之间可以通过localhost来进行通信,所需要注意的是不同容器要注意不要有端口冲突即可。不同的Pod有不同的IP,不同Pod内的多个容器之间通信，不可以使用IPC（如果没有特殊指定的话）通信，通常情况下使用Pod的IP进行通信。
- 一个Pod里的多个容器可以共享存储卷，这个存储卷会被定义为Pod的一部分，并且可以挂载到该Pod里的所有容器的文件系统上。

### ☆ 结构

![[c1bb736786.png]]

每个Pod中都可以包含一个或者多个容器，这些容器可以分为两类：

- 用户程序所在的容器，数量可多可少；
- Pause容器，这是每个Pod都会有的一个**根容器**，它的作用有两个：

- 可以以它为依据，评估整个Pod的健康状态
- 可以在根容器上设置IP地址，其它容器都使用此IP（Pod IP），以实现Pod内部的网路通信

这里是Pod内部的通讯，Pod的之间的通讯采用**虚拟二层网络技术**来实现，我们当前环境用的是Flannel

![[98deaed7bb.png]]

Pod -> 容器 == 逻辑主机 -> 进程

### ☆ 分类

pod可分为:

- **无控制器管理的自主式pod（不到10%）** 没有副本控制器控制，删除自主式pod后不会重新创建；
- **控制器管理的pod（大于90%）** 控制器会按照定义的策略控制pod的数量，发现pod数量少了，会立即自动建立出来新的pod；一旦发现pod多了，也会自动杀死多余的Pod；

有控制器(Controller)管理的 pod 也比较多，比如 Deployment、ReplicaSet、DaemonSet、StatefulSet 等。后续在讲到 Controller 时将会逐步学习。

- **Deployment** 用于部署无状态应用，管理 Pod 的创建、更新等；
- ReplicaSet 确保 Pod 副本数量（一般没有人主动创建它）；
- **DaemonSet** 保证每个节点都运行一个 Pod 副本；
- StatefulSet 用于管理有状态应用，为 Pod 提供稳定的网络标识和存储

## Pod的YAML格式

### ☆ 语法定义

先看一个yaml格式的pod定义文件解释

```
kubectl get pod -o yaml/wide/json
```

```
# yaml格式的pod定义文件完整内容：
apiVersion: v1       #必选，api版本号，例如v1
kind: Pod       	#必选，Pod
metadata:       	#必选，元数据
  name: string       #必选，Pod名称
  namespace: string    #Pod所属的命名空间,默认在default的namespace
  labels:     		 # 自定义标签
    - name: string     #自定义标签名字
  annotations:        #自定义注释列表
    - name: string
spec:         #必选，Pod中容器的详细定义(期望)
  containers:      #必选，Pod中容器列表
  - name: string     #必选，容器名称
    image: string    #必选，容器的镜像名称
    imagePullPolicy: [Always | Never | IfNotPresent] #获取镜像的策略 Alawys表示下载镜像 IfnotPresent表示优先使用本地镜像，否则下载镜像，Nerver表示仅使用本地镜像
    command: [string]    #容器的启动命令列表，如不指定，使用打包时使用的启动命令
    args: [string]     #容器的启动命令参数列表
    workingDir: string     #容器的工作目录
    volumeMounts:    #挂载到容器内部的存储卷配置
    - name: string     #引用pod定义的共享存储卷的名称，需用volumes[]部分定义的的卷名
      mountPath: string    #存储卷在容器内mount的绝对路径，应少于512字符
      readOnly: boolean    #是否为只读模式
    ports:       #需要暴露的端口号列表
    - name: string     #端口号名称
      containerPort: int   #容器需要监听的端口号
      hostPort: int    #容器所在主机需要监听的端口号，默认与Container相同
      protocol: string     #端口协议，支持TCP和UDP，默认TCP
    env:       #容器运行前需设置的环境变量列表
    - name: string     #环境变量名称
      value: string    #环境变量的值
    resources:       #资源限制和请求的设置
      limits:      #资源限制的设置
        cpu: string    #Cpu的限制，单位为core数，将用于docker run --cpu-shares参数
        memory: string     #内存限制，单位可以为Mib/Gib，将用于docker run --memory参数
      requests:      #资源请求的设置
        cpu: string    #Cpu请求，容器启动的初始可用数量
        memory: string     #内存清求，容器启动的初始可用数量
    livenessProbe:     #对Pod内个容器健康检查的设置，当探测无响应几次后将自动重启该容器，检查方法有exec、httpGet和tcpSocket，对一个容器只需设置其中一种方法即可
      exec:      #对Pod容器内检查方式设置为exec方式
        command: [string]  #exec方式需要制定的命令或脚本
      httpGet:       #对Pod内个容器健康检查方法设置为HttpGet，需要制定Path、port
        path: string
        port: number
        host: string
        scheme: string
        HttpHeaders:
        - name: string
          value: string
      tcpSocket:     #对Pod内个容器健康检查方式设置为tcpSocket方式
         port: number
       initialDelaySeconds: 0  #容器启动完成后首次探测的时间，单位为秒
       timeoutSeconds: 0   #对容器健康检查探测等待响应的超时时间，单位秒，默认1秒
       periodSeconds: 0    #对容器监控检查的定期探测时间设置，单位秒，默认10秒一次
       successThreshold: 0
       failureThreshold: 0
       securityContext:
         privileged:false
    restartPolicy: [Always | Never | OnFailure] # Pod的重启策略，Always表示一旦不管以何种方式终止运行，kubelet都将重启，OnFailure表示只有Pod以非0退出码退出才重启，Nerver表示不再重启该Pod
    nodeSelector: obeject  # 设置NodeSelector表示将该Pod调度到包含这个label的node上，以key：value的格式指定
    imagePullSecrets:    #Pull镜像时使用的secret名称，以key：secretkey格式指定
    - name: string
    hostNetwork:false      #是否使用主机网络模式，默认为false，如果设置为true，表示使用宿主机网络
    volumes:       #在该pod上定义共享存储卷列表
    - name: string     #共享存储卷名称 （volumes类型有很多种）
      emptyDir: {}     #类型为emtyDir的存储卷，与Pod同生命周期的一个临时目录。为空值
      hostPath: string     #类型为hostPath的存储卷，表示挂载Pod所在宿主机的目录
        path: string     #Pod所在宿主机的目录，将被用于同期中mount的目录
      secret:      #类型为secret的存储卷，挂载集群与定义的secret对象到容器内部
        scretname: string  
        items:     
        - key: string
          path: string
      configMap:     #类型为configMap的存储卷，挂载预定义的configMap对象到容器内部
        name: string
        items:
        - key: string
          path: string
```

#### ☆ 三大重启策略 restartPolicy

restartPolicy: [Always | Never | OnFailure]

Pod的重启策略，Always表示一旦不管以何种方式终止运行，kubelet都将重启，OnFailure表示只有Pod以非0退出码退出才重启，Nerver表示不再重启该Pod

|   |   |   |
|---|---|---|
|**策略类型**|**适用控制器**|**Pod终止后行为**|
|Always|Deployment/StatefulSet|自动重启（无限次）|
|OnFailure|Job/CronJob|非0退出码时重启（可设上限）|
|Never|Job/DaemonSet|不重启（记录失败状态）|

怎么对 OnFailture 设置失败上限呢？因为不能让它一直失败拉取。

```
apiVersion: v1
kind: Pod
metadata:
  name: standalone-task
spec:
  restartPolicy: OnFailure
  activeDeadlineSeconds: 100  # ← 总运行时间上限（秒）
  containers:
  - name: task-runner
    image: alpine
    command: ["/bin/sh", "-c", "custom_script.sh"]
```

![[fdcf623bc5.png]]

#### ☆ 三大拉取策略 imagePullPolicy

|   |   |   |
|---|---|---|
|**策略值**|**含义**|**适用场景**|
|Always|每次启动 Pod 都强制拉取镜像|用于开发测试环境或镜像常更新|
|IfNotPresent|本地有就用本地镜像，没有再拉|默认策略(非 :latest 镜像)|
|Never|从不拉镜像，只用本地已有镜像|离线部署、镜像预加载场景|

比如

|   |   |   |
|---|---|---|
|**镜像标签形式**|**默认策略**|**可覆盖策略**|
|nginx:latest|Always|可改为IfNotPresent/Never|
|nginx:1.25 \| nginx@sha256:...|IfNotPresent|可改为Always/Never，不建议改|
|-|Never|从不拉取，人为设置的|

推荐使用 IfNotPresent，生产中禁止使用 latest，想想为什么？

### ☆ api-versions 版本

查看api版本

```
[root@master ~]# kubectl api-versions
```

![[ac028f4c80.png]]

```
[root@master ~]#
```

![[1fac45ac2c.png]]

### ☆ explain 解释

`kubectl explain` 被誉为 **“内建的交互式文档”**。当你忘记 YAML 字段怎么写、某个字段是什么意思，或者需要查看字段的数据类型时，它是最权威的参考手册（直接从集群 API Server 获取数据）。

查看yaml资源写法

```
[root@master ~]# kubectl explain namespace
[root@master ~]# kubectl explain pod
[root@master ~]# kubectl explain pod.spec
[root@master ~]# kubectl explain pod.spec.containers
```

## 创建Pod

1, 准备yaml文件

```
[root@master ~]# vim pod1.yaml
apiVersion: v1					# api版本(不同版本语法有少量差异),这里为v1.
kind: Pod					# 资源类型为Pod
metadata:						
  name: memory-demo				# 自定义pod的名称
spec:
  containers:					# 定义pod里包含的容器
  - name: demo					# 自定义pod中的容器名
    # image: polinux/stress:1.0.4		        # 启动容器的镜像名
    image: polinux/stress:1.0.4
    command: ["stress"]			# 自定义启动容器时要执行的命令(类似dockerfile里的CMD)
    args: ["--vm", "1", "--vm-bytes", "150M", "--timeout", "20"] # 自定义启动容器执行命令的参数
    
# polinux/stress这个镜像用于压力测试,在启动容器时传命令与参数就是相当于分配容器运行时需要的压力，相关参数如下：
--vm-bytes 表示malloc分配多少内存
--vm-hang 表示malloc分配的内存多少时间后在free()释放掉
--vm 指定进程数量
--timeout 表示执行时间，单位为s，执行20s之后，进程结束
```

说明: 镜像拉取策略 imagePullPolicy

- Always : 不管本地有没有镜像，都要从仓库中下载镜像
- Never : 从来不从仓库下载镜像, 只用本地镜像,本地没有就算了
- IfNotPresent: 如果本地存在就直接使用, 不存在才从仓库下载

默认的策略是：

- 当镜像标签版本是latest，默认策略就是Always
- 如果指定特定版本，默认拉取策略就是IfNotPresent。

```
# 如果拉取镜像特别慢，也可以先拉取到本地，我们接下来介绍方法：
# 1、查看本地有哪些镜像的命名空间（我们用的 containerd 作为运行时）
[root@adm-master ~]# ctr ns ls
NAME    LABELS
default
k8s.io

# 2、拉取镜像到指定的命名空间，比如 k8s.io
ctr -n k8s.io i pull polinux/stress:1.0.4

# 3.1 、拉下来之后，就可以把上个章节 Yaml 中的 image 改成 
#  image: cf-workers-docker-io-38g.pages.dev/polinux/stress:1.0.4 

# 3.2 或者重新打一个标签 polinux/stress
ctr -n k8s.io i tag xxxx/polinux/stress:latest polinux/stress:1.0.4
```

2, 通过yaml文件创建pod

```
[root@master ~]# kubectl apply -f pod1.yaml
pod/memory-demo created
```

查看pod信息

```
[root@master ~]# kubectl get pod
NAME          READY   STATUS    RESTARTS   AGE
memory-demo   1/1     Running   0          25s
```

查看pod详细信息

```
[root@master ~]# kubectl get pod memory-demo -o wide

# 查看详细的信息
kubectl get pod memory-demo -o yaml 
kubectl get pod memory-demo -o yaml > memory-demo-format.yaml
```

描述pod详细信息，查看容器当前是否起来

```
[root@master ~]# kubectl describe pod memory-demo
```

由于压力测试进行了时长 --timeout 约束，我们在执行指定时间后，容器进程终止，为 Completed。

但是由于restartPolicy 参数默认是 Always，所以，在短暂的完成后，容器又会重新拉起。

![[06fa58dedf.png]]

## Pod标签Label

删除pod

```
[root@master ~]# kubectl delete pod memory-demo
pod "memory-demo" deleted
```

重新建立带有Label标签的Pod

```
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo
  namespace: kube-system
  labels:
    version: "1.0" 
    env: "dev"
spec:
  containers:
  - name: demo
    # image: polinux/stress
    imagePullPolicy: IfNotPresent   # 优化拉取策略，本地没有再去拉取
    image: cf-workers-docker-io-38g.pages.dev/polinux/stress:1.0.4
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "150M", "--timeout", "100"]
```

![[d512d55140.png]]

## Pod资源限制

准备2个不同限制方式的创建pod的yaml文件

```
[root@master ~]# vim pod-150.yml
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
---
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo-1
  namespace: namespace1
spec:
  restartPolicy: Never
  containers:
  - name: memory-demo-ctr1
    image: polinux/stress:1.0.4
    imagePullPolicy: IfNotPresent
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    command: ["stress"]				    # 启动容器时执行的命令
    args: ["--vm", "1", "--vm-bytes", "150M", "--timeout", "30"]  # 产生1个进程分配150M内存30s后释放
```

```
[root@master ~]# vim pod-250.yml
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
---
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo-2
  namespace: namespace1
spec:
  restartPolicy: Never
  containers:
  - name: memory-demo-ctr2
    image: cf-workers-docker-io-38g.pages.dev/polinux/stress:1.0.4
    imagePullPolicy: IfNotPresent
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "250M", "--timeout", "30"]
```

```
[root@master ~]# kubectl apply -f pod-150.yml
namespace/namespace1 created
pod/memory-demo-1 created

[root@master ~]# kubectl apply -f pod-250.yml
namespace/namespace1 unchanged
pod/memory-demo-2 created
```

```
[root@master ~]# kubectl get namespace  |grep namespace1
namespace1        Active   2m28s

[root@master ~]# kubectl get pod -n namespace1
NAME            READY   STATUS      RESTARTS   AGE
memory-demo-1    1/1     Running     0          3m37s
memory-demo-2   0/1     OOMKilled   5          3m13s

查看会发现memory-demo-2这个pod状态变为OOMKilled，因为它是内存不足所以显示Container被杀死
```

说明: 一旦pod中的容器挂了，我们就把容器重启。策略包括如下：

- Always：表示容器挂了总是重启，这是默认策略
- OnFailures：表容器状态为错误时才重启，也就是容器正常终止时才重启
- Never：表示容器挂了不予重启
- 对于Always这种策略，容器只要挂了，就会立即重启，这样是很耗费资源的。所以Always重启策略是这么做的：第一次容器挂了立即重启，如果再挂了就要延时10s重启，第三次挂了就等20s重启（**线性回退算法**）...... 依次类推

如果想要添加重启策略，把上述 Yaml 文件中的 spec 字段下的 restartPolicy 注释放开即可

![[87c792a479.png]]

测试完后删除

```
kubectl delete ns namespace1

# 或者
kubectl delete -f pod-150.yaml
kubectl delete -f pod-250.yaml
```

![[1729ad5132.png]]

# 【掌握】Pod交互操作

## 一个Pod包含多个容器

1, 准备yml文件

```
[root@master ~]# vim pod-multi-ctr.yml
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo
  namespace: kube-system
spec:
  restartPolicy: Never
  containers:
  - name: memory-demo-ctr-1
    image: polinux/stress:1.0.4
    imagePullPolicy: IfNotPresent
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "150M", "--timeout", "300"]
    
  - name: memory-demo-ctr-2
    image: polinux/stress:1.0.4
    imagePullPolicy: IfNotPresent
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
    command: ["stress"]
    args: ["--vm", "1", "--vm-bytes", "150M", "--timeout", "300"]
```

2, 应用yml文件创建pod

```
[root@master ~]# kubectl apply -f pod-multi-ctr.yml
```

3, 查看pod在哪个节点

```
[root@master ~]# kubectl get pods -n kube-system -o wide

# 可以看到有2个容器,运行在node2节点
```

![[ec099033a6.png]]

等待 timeout 时间后，容器运行结束

![[600ef0faac.png]]

4,在node2上验证,确实产生了2个容器

```
# docker在这里作为了解，因为我们安装的 K8S 集群，大部分是默认使用 containerd 作为了容器运行时
[root@node2 ~]# docker ps -a |grep stress
7f2ba28dc7bb        68478b32266c                                         "stress --vm 1 --vm-…"   5 minutes ago       Up 5 minutes                                  k8s_memory-demo-ctr-2_memory-demo_default_86c31332-d8df-40ee-b332-f285ffe0a7df_0

9e45276b3e3a        68478b32266c                                         "stress --vm 1 --vm-…"   5 minutes ago       Up 5 minutes                                  k8s_memory-demo-ctr-1_memory-demo_default_86c31332-d8df-40ee-b332-f285ffe0a7df_0
```

## 对Pod里的容器进行操作

命令帮助

```
[root@master ~]# kubectl exec -h
```

### **不用交互直接执行命令**

```
格式为: kubectl exec pod名 -c 容器名 -- 命令
```

**注意:**

- -c 容器名为可选项,如果是1个pod中1个容器,则不用指定;【工作中90% 只有一个容器】
- 如果是1个pod中多个容器,不指定默认为第1个。

```
[root@master ~]# kubectl exec -n kube-system memory-demo -c memory-demo-ctr-1 -- touch /111
```

不指定容器名,则默认为pod里的第1个容器

```
[root@master ~]# kubectl exec -n kube-system   memory-demo  -- touch /222
```

### **和容器交互操作**(最常用)

# 进入指定容器

kubectl exec -it <Pod名> -c <容器名> -n <命名空间> -- /bin/bash

和docker exec几乎一样

```
[root@master ~]# kubectl exec -n kube-system  -it memory-demo -c memory-demo-ctr-1 -- /bin/bash
bash-4.3# touch /333
bash-4.3# ls
111    333    dev    home   media  proc   run    srv    tmp    var
222    bin    etc    lib    mnt    root   sbin   sys    usr
bash-4.3# exit
exit
```

![[1409e6a831.png]]

```
# 因此，推荐大家加上 --
kubectl exec -n kube-system  -it memory-demo -n dev -- /bin/bash
```

![[b95af8cba9.png]]

**删除pod**

```
[root@master ~]# kubectl delete pod memory-demo -n kube-system
pod "memory-demo" deleted
```

## 总结

1、Pod中文意思是_____；一个Pod可以有一个或多个_____;

**豆荚 Container (容器)**

2、有控制器管理的Pod，介绍了一个控制器 —— deployment；

3、Pod的Yaml文件格式查看 kubectl _______ pod --help

4、学习Pod的Yaml字段：

|   |   |   |
|---|---|---|
|**字段名**|**英文读法/含义**|**运维实战作用**|
|`**namespace**`|`/ˈneɪmˌspeɪs/`<br><br>命名空间|资源隔离，将开发(dev)与生产(prod)环境分开。|
|`**label**`|`/ˈleɪbl/`<br><br>标签|用于分类和被 `Selector`<br><br>筛选的键值对。|
|`**imagePullPolicy**`|镜像拉取策略|`Always`<br><br>, `Never`<br><br>, `IfNotPresent`<br><br>(本地有就不下)。|
|`**restartPolicy**`|重启策略|`Always`<br><br>(默认), `OnFailure`<br><br>, `Never`<br><br>。|
|`**resources**`|`/rɪˈsɔːrsɪz/`<br><br>资源限制|定义 `requests`<br><br>(需求) 和 `limits`<br><br>(限制) CPU/内存。|
|`**containers**`|`/kənˈteɪnərz/`<br><br>容器|Pod 内运行的具体业务进程列表。|

5、对Pod的容器进行操作

# 进入指定容器

kubectl exec -it <Pod名> -c <容器名> -n <命名空间> -- /bin/bash