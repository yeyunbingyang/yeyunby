# 1【掌握】Pod调度策略

## 1 Pod创建流程(重点)

![[附件/9875dce9e8.png]]

**step.1 用户提交Pod定义**

kubectl 向 k8s api server 发起一个create pod 请求(即我们使用Kubectl敲一个create pod命令)

**step.2 API Server 接收请求**

k8s api server接收到pod创建请求后，不会去直接创建pod；而是生成一个包含创建信息的yaml。

api server 将刚才的yaml信息写入etcd数据库。到此为止，仅仅是在etcd中添加了一条记录， 还没有任何的实质性进展。

**step.3 调度器选择节点**

scheduler 通过其 watcher 监测到 k8s api sever创建新pod对象请求 首先判断：pod.spec.nodeName == null? 若为null，表示这个Pod请求是新来的，需要创建；因此先进行调度计算，找到最“合适”的node。 然后将信息在etcd数据库中更新分配结果：pod.spec.Node = nodeA (设置一个具体的节点)

ps:同样上述操作的各种信息也要写到etcd数据库中。

![[附件/dc23c300f7.png]]

**step.4 节点上的 kubelet 创建 Pod**

kubelet 通过监测etcd数据库(即不停地看etcd中的记录)，发现 k8s api server 中有了个新的Pod创建请求； 如果这条记录中的Node与自己的编号相同(即这个pod由scheduler分配给自己了)，则调用node中的**运行时(Runtime)**，创建container。

## 2 调度约束方法

在默认情况下，一个Pod在哪个Node节点上运行，是由Scheduler组件采用相应的算法计算出来的，这个过程是不受人工控制的。

但是在实际使用中，这可能并不满足企业的需求，因为很多情况下，我们想控制某些Pod到达某些节点上，那么应该怎么做呢？这就要求了解kubernetes对Pod的调度规则，kubernetes提供了四大种调度方式：

- **自动调度：**运行在哪个节点上完全由Scheduler经过一系列的算法计算得出
- **定向调度(针对Pod)：**NodeName、NodeSelector
- **亲和性调度(针对Pod)：**NodeAffinity、PodAffinity、PodAntiAffinity
- **污点(针对Node) / 容忍(针对Pod)调度：**Node Taints、Pod Toleration

### ☆ 自动调度

Kubernetes 调度器（Scheduler）是集群控制平面的核心组件之一，负责将新创建的 Pod 分配到合适的 Node 上运行。其核心流程可分为两个关键阶段：**过滤（Filtering）和打分（Scoring）**。

#### **过滤（Filtering）**

Scheduler 会从集群所有节点中筛选出满足 Pod 运行要求的节点。

- 并行检查所有节点
- 任何不满足条件的节点会被立即排除
- 最终得到一个可行节点列表（Feasible Nodes）

**常见过滤条件**

暂时无法在飞书文档外展示此内容

#### **打分（Scoring）**

在可行节点中通过评分策略找到最优节点。

- 为每个可行节点计算分数（0-100）
- 不同评分策略有不同权重
- 调度器选择综合分数最高的节点

过滤，是为了解决**“能不能”**的问题

打分，是为了解决**“好不好”**的问题

#### 整体流程

![[附件/66b4c44ae3.png]]

### ☆ 定向调度

我们为了实现容器主机资源平衡使用, 可以使用约束把pod调度到指定的node节点。

应用场景举例 当应用对硬件有特定要求，如需要 GPU 支持的应用，可将节点标记为有 GPU 的标签，然后通过节点选择器将相关 Pod 调度到这些节点上。

- NodeName 用于将pod调度到指定的node名称上
- NodeSelector 用于将pod调度到**匹配Label**的一类node上

#### 案例1: NodeName

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

2, 应用YAML文件创建pod

暂时无法在飞书文档外展示此内容

3, 验证

暂时无法在飞书文档外展示此内容

![[附件/7328c5a254.png]]

4, 如果调度在一个不存在的节点，会一直创建不起来

比如，将节点改为 adm-node3

![[附件/1ab51b7491.png]]

#### **案例2**: NodeSelector

1, 为node2打标签

暂时无法在飞书文档外展示此内容

2, 编写YAML文件

暂时无法在飞书文档外展示此内容

3, 应用YAML文件创建pod

暂时无法在飞书文档外展示此内容

4, 验证

暂时无法在飞书文档外展示此内容

作业 有兴趣可以再删除后再创建（修改一下指定的节点或者标签值）,重复几次验证

![[附件/1d02b032b2.png]]

测验结果 没找到相应的节点或标签，定向调度就直接失败了。 总结 定向调度的缺点：如果人为误输入或者单词拼写错误，就无法正常启动了。

#### 问题总结

**问题1 查看 pod，发现一直是** **pending** **状态**

如果是调度到了不存在的节点，pending是正常的（要么是节点不存在，要么是节点没启动）

![[附件/dd3917872e.png]]

**问题2 查看node，发现一直是 not ready 状态**

好多小伙伴没把自己的集群起起来

![[附件/73d3ff8d08.png]]

### ☆ 亲和性调度

上一节，介绍了两种定向调度的方式，使用起来非常方便，但是也有一定的问题。

那就是如果没有满足条件的Node，那么Pod将不会被运行，即使在集群中还有可用Node列表也不行。

这就限制了它的使用场景。

基于上面的问题，kubernetes还提供了一种亲和性调度（Affinity）。它在NodeSelector的基础之上的进行了扩展，可以通过配置的形式，实现优先选择满足条件的Node进行调度，如果没有，也可以调度到不满足条件的节点上，使调度更加灵活。

Affinity主要分为三类：

- **nodeAffinity(node亲和性）**: 以node为目标，解决pod可以调度到哪些node的问题
- **podAffinity(pod亲和性)** : 以pod为目标，解决pod可以和哪些已存在的pod部署在同一个拓扑域中的问题
- **podAntiAffinity(pod反亲和性)** : 以pod为目标，解决pod不能和哪些已存在pod部署在同一个拓扑域中的问题

关于亲和性(反亲和性)使用场景的说明：

**亲和性**：如果两个应用频繁交互，那就有必要利用亲和性让两个应用的尽可能的靠近，这样可以减少因网络通信而带来的性能损耗。

**反亲和性**：当应用采用多副本部署时，有必要采用反亲和性让各个应用实例打散分布在各个node上，这样可以提高服务的高可用性。

#### **NodeAffinity**

首先来看一下NodeAffinity的可配置项：

暂时无法在飞书文档外展示此内容

补充说明 preferred 表明这是一个优先选择； DuringScheduling 说明该规则只在调度 Pod 到节点时考虑； IgnoredDuringExecution 意味着在 Pod 已经运行后，即使节点的状态或标签发生变化不再满足该规则，也不会影响 Pod 继续在该节点运行。

暂时无法在飞书文档外展示此内容

接下来首先演示一下requiredDuringSchedulingIgnoredDuringExecution ,

创建pod-nodeaffinity-required.yaml

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

![[附件/941c085a91.png]]

暂时无法在飞书文档外展示此内容

![[附件/807e2b8328.png]]

接下来再演示一下preferredDuringSchedulingIgnoredDuringExecution ,

创建pod-nodeaffinity-preferred.yaml

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

NodeAffinity注意事项： 1、如果同时定义了nodeSelector和nodeAffinity，那么必须两个条件都得到满足，Pod才能运行在指定的Node上 2、如果一个pod所在的Node在Pod运行期间其标签发生了改变，不再符合该Pod的节点亲和性需求，则系统将忽略此变化

#### **PodAffinity**

PodAffinity主要实现以运行的Pod为参照，实现让新创建的Pod跟参照Pod在一个区域的功能。

首先来看一下PodAffinity的可配置项：

暂时无法在飞书文档外展示此内容

PodAffinity 中，topologyKey 用于指定调度时作用域,例如: 1、如果指定为kubernetes.io/hostname，那就是以 Node 节点为区分范围 作用机制：调度器会尽量把新的 Pod 调度到特定 Pod 的同一个 Node 上； 示例场景：在微服务架构里，若两个微服务之间通信频繁，可以减少网络开销。 2、如果指定为beta.kubernetes.io/os,则以Node节点的操作系统类型来区分 作用机制：调度器会尽量把新 Pod 调度到和已有特定 Pod 操作系统类型相同的 Node 上； 示例场景：如果有一些应用只能在特定操作系统（如 Linux）上运行，可确保 Pod 都调度到相应 Node 上。

接下来，演示下requiredDuringSchedulingIgnoredDuringExecution,

1）首先创建一个参照Pod，pod-podaffinity-target.yaml：

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

2）创建pod-podaffinity-required.yaml，内容如下：

暂时无法在飞书文档外展示此内容

上面配置表达的意思是：新Pod必须要与拥有标签podenv=xxx或者podenv=yyy的pod在同一Node上，显然现在没有这样pod，接下来，运行测试一下。

暂时无法在飞书文档外展示此内容

关于PodAffinity的 preferredDuringSchedulingIgnoredDuringExecution，这里不再演示。

#### **PodAntiAffinity**

PodAntiAffinity主要实现以运行的Pod为参照，让新创建的Pod跟参照Pod不在一个区域中的功能。

它的配置方式和选项跟PodAffinty是一样的，这里不再做详细解释，直接做一个测试案例。

1）继续使用上个案例中目标pod

暂时无法在飞书文档外展示此内容

2）创建pod-podantiaffinity-required.yaml，内容如下：

暂时无法在飞书文档外展示此内容

上面配置表达的意思是：新Pod必须要与拥有标签podenv=pro的pod不在同一Node上，运行测试一下。

暂时无法在飞书文档外展示此内容

亲和性调度既有硬亲和性，也有软亲和性，相对弹性。 在实际工作中，单独搭建的云环境集群，往往操作系统和节点特性都是统一的，因为节点之前差异（标签）比较小。

#### 问题总结

**问题1 资源没找到**

![[附件/4e70e2e401.png]]

暂时无法在飞书文档外展示此内容

**问题2 标签查看不到值**

![[附件/3a382ed7fe.png]]

pod 中的标签，和 node 中的标签，是不一样的。

### ☆ 污点和容忍

#### **污点（Taints）**

前面的调度方式都是站在Pod的角度上，通过在Pod上添加属性，来确定Pod是否要调度到指定的Node上，其实我们也可以站在Node的角度上，通过在Node上添加**污点**属性，来决定是否允许Pod调度过来。

Node被设置上污点之后就和Pod之间存在了一种相斥的关系，进而拒绝Pod调度进来，甚至可以将已经存在的Pod驱逐出去。

污点的格式为：key=value:effect

key和value是污点的标签

effect描述污点的作用，支持如下三个选项：

- **PreferNoSchedule：**kubernetes将尽量避免把Pod调度到具有该污点的Node上，除非没有其他节点可调度
- **NoSchedule：**kubernetes将不会把Pod调度到具有该污点的Node上，但不会影响当前Node上已存在的Pod
- **NoExecute：**kubernetes将不会把Pod调度到具有该污点的Node上，同时也会将Node上已存在的Pod驱离

![[附件/8f2a49ca95.png]]

使用kubectl设置和去除污点的命令示例如下：

暂时无法在飞书文档外展示此内容

接下来，演示下污点的效果：

1. 准备节点node1（为了演示效果更加明显，暂时停止node2节点）
2. 为node1节点设置一个污点: tag=heima:PreferNoSchedule；然后创建pod1( pod1 可以 )
3. 修改为node1节点设置一个污点: tag=heima:NoSchedule；然后创建pod2( pod1 正常 pod2 失败 )
4. 修改为node1节点设置一个污点: tag=heima:NoExecute；然后创建pod3 ( 3个pod都失败 )

暂时无法在飞书文档外展示此内容

思考题：为什么我们在使用k8s集群时，所有创建的pod都自动分配给node1/node2节点，但是从来没有分配到master1和master2节点呢？ 小提示： 使用kubeadm/kubeasz搭建的集群，默认就会给master节点添加一个污点标记,所以pod就不会调度到master节点上. kubectl describe node master

![[附件/4a12bd9fb9.png]]

#### **容忍（Toleration）**

上面介绍了污点的作用，我们可以在node上添加污点用于拒绝pod调度上来，但是如果就是想将一个pod调度到一个有污点的node上去，这时候应该怎么做呢？这就要使用到**容忍**。

![[附件/62366f6392.png]]

污点就是拒绝，容忍就是忽略，Node通过污点拒绝pod调度上去，Pod通过容忍忽略拒绝

下面先通过一个案例看下效果：

1. 上一小节，已经在node1节点上打上了NoExecute的污点，此时pod是调度不上去的
2. 本小节，可以通过给pod添加容忍，然后将其调度上去

创建pod-toleration.yaml,内容如下

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

小提示 添加容忍，也就是修改pod，可以使用以下命令，在线修改 kubectl edit pod pod名字

下面看一下容忍的详细配置:

暂时无法在飞书文档外展示此内容

**为什么我们自己部署的Pod，都在 master node 上面，不在 work node 上面？**

就是因为 master 上面有污点

![[附件/1324845356.png]]

## 总结

1、**Pod创建流程（面试）** 1、用户向______发送请求；API Server 丰富Yaml文件，记录到____数据库； 2、Scheduler 负责查看 **NodeName节点** 字段是否为空，如果为空，按照指定的调度算法进行分配； 3、Kubelet 负责查看创建请求，并按照 Node 节点认领创建任务，下发给运行时Containerd，进行创建； 2、调度策略，除了**自动调度** 1、定向调度 - NodeName NodeSelector 2、亲和性调度 - NodeAffinity PodAffinity PodAntiAffinity 3、污点（Taints）和容忍（Toleration） 3、容忍是针对Pod的，污点是针对Node的；

# 2【熟悉】Pod的生命周期

常见pod运行场景：

- 有些pod(比如跑httpd服务),正常情况下会一直运行中,但如果手动删除它,此pod会终止
- 也有些pod(比如执行计算任务)，任务计算完后就会自动终止

上面两种场景中,pod从创建到终止的过程就是pod的生命周期。

## 1 Pod生命周期详解

![[附件/20907d1baf.png]]

### 容器启动

1. pod中的容器在创建前,有初始化容器(init container)来进行初始化环境
2. 初化完后,主容器(main container)开始启动
3. 主容器启动后,有一个**post start**的操作(启动后的触发型操作,或者叫启动后钩子)
4. post start后,就开始做健康检查

5. 第一个健康检查叫存活状态检查(liveness probe)，用来检查主容器存活状态的
6. 第二个健康检查叫准备就绪检查(readiness probe)，用来检查主容器是否启动就绪

### 容器终止

1. 可以在容器终止前设置**pre stop**操作(终止前的触发型操作,或者叫终止前钩子)
2. 当出现特殊情况不能正常销毁pod时,大概等待30秒会强制终止
3. 终止容器后还可能会重启容器(视容器重启策略而定)。

### 重启策略

- Always：表示容器挂了总是重启，这是默认策略
- OnFailures：表示容器异常退出（退出状态码非0）时才重启 O|1
- Never：表示容器挂了不予重启
- 对于Always这种策略，容器只要挂了，就会立即重启，这样是很耗费资源的。所以Always重启策略是这么做的：第一次容器挂了立即重启，如果再挂了就要延时10s重启，第三次挂了就等20s重启...... 依次类推

![[附件/eef8bd85d5.png]]

暂时无法在飞书文档外展示此内容

![[附件/6a87d238b2.png]]

## 2 HealthCheck健康检查(重点)

当Pod启动时，容器可能会因为某种错误(服务未启动或端口不正确)而无法访问等。

kubelet（1.16+）拥有三个检测器，它们分别对应不同的触发器(根据触发器的结构执行进一步的动作)

### 三种探针

暂时无法在飞书文档外展示此内容

应用场景

**startup Probe：**保护慢初始化应用（比如Java服务），直到其完成启动再启用其他探针； **livenessProbe：**适用于那些可能会因为各种原因（如程序死锁、资源耗尽等）而陷入非健康状态的容器，通过定期检测并重启容器来保证应用的可用性； **readinessProbe：**常用于需要一定时间进行初始化的容器，确保在容器完全准备好处理请求之前（比如数据库连接），不会将流量导向该容器，避免客户端请求失败；

### 三种探测方式

|   |   |
|---|---|
|**方式**|**说明**|
|**Exec**|**执行(Execute)命令**|
|HTTPGet|http请求某一个URL路径|
|TCP|tcp连接某一个端口|

### 五个探针参数（了解）

所有探针都支持以下参数：

暂时无法在飞书文档外展示此内容

**补充知识**

涉及到计算机网络中的七层模型/四层模型 1、HTTP 是属于**应用层协议**； 2、TCP 是属于**传输层协议**。

应用层

表示层 应用层（整合） HTTP、FTP、SNMP

会话层

**传输层 传输层 TCP**

**网络层 网络层 IP**

链路层 物理链路层（整合）

物理层

### 案例1: liveness-exec

1, 准备YAML文件

暂时无法在飞书文档外展示此内容

2, 应用YAML文件

暂时无法在飞书文档外展示此内容

3, 通过下面的命令观察

暂时无法在飞书文档外展示此内容

4, 过几分钟再观察

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

![[附件/b1885d9fa9.png]]

### 案例2: liveness-httpget

1, 编写YMAL文件

暂时无法在飞书文档外展示此内容

2, 应用YAML文件

暂时无法在飞书文档外展示此内容

3, 验证查看

暂时无法在飞书文档外展示此内容

4, 移动Nginx里的主页文件

暂时无法在飞书文档外展示此内容

5, 验证查看会发现

![[附件/ee6590afe2.png]]

暂时无法在飞书文档外展示此内容

![[附件/37bd1debb6.png]]

只restart过一次，如果你再移动一次 index.html，会再次出发重启，次数就 +1

### 案例3: liveness-tcp

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

2, 应用YAML文件创建pod

暂时无法在飞书文档外展示此内容

3, 查看验证

暂时无法在飞书文档外展示此内容

4, 交互关闭 Nginx

暂时无法在飞书文档外展示此内容

5, 再次验证查看

暂时无法在飞书文档外展示此内容

![[附件/8c7969f367.png]]

暂时无法在飞书文档外展示此内容

![[附件/d02fa218ef.png]]

**总结** 1、Liveness 探测失败后，会____； 2、重启后重新初始化了，容器里的数据会丢失；

### 案例4: readiness

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

2, 应用YAML文件

暂时无法在飞书文档外展示此内容

3, 验证查看

暂时无法在飞书文档外展示此内容

![[附件/b56f87889f.png]]

4, 交互移走Nginx主页

暂时无法在飞书文档外展示此内容

5, 再次验证

![[附件/df8e5fb736.png]]

暂时无法在飞书文档外展示此内容

![[附件/59a884d12d.png]]

6, 交互创建nginx主页文件再验证

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

不会触发重启，describe 展示的 Message 不会刷新

### 案例5: readiness+liveness综合

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

2, 应用YAML文件

暂时无法在飞书文档外展示此内容

3, 验证

暂时无法在飞书文档外展示此内容

![[附件/072359941f.png]]

## 3 钩子

### 启动后 post-start

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

2, 应用YMAL文件

暂时无法在飞书文档外展示此内容

3, 验证

暂时无法在飞书文档外展示此内容

暂时无法在飞书文档外展示此内容

![[附件/03ecbf8985.png]]

### 停止前 pre-stop

容器终止前执行的命令

1, 编写YAML文件

暂时无法在飞书文档外展示此内容

大驼峰写法：ReadinessProbeHttpGet 小驼峰写法：readinessProbeHttpGet

2, 应用YAML文件创建pod

暂时无法在飞书文档外展示此内容

3, 删除pod验证

暂时无法在飞书文档外展示此内容

**结论:** 当出现特殊情况不能正常销毁pod时，大概等待30秒会强制终止

![[附件/1934649d11.png]]

## 总结

1、initContainer 初始化容器【了解】 kubectl explain pod 查询Yaml参数 2、mainContainer 主容器 1、Post-Start 2、健康检查 Health Check | 探针 Probe【重点】 1、LivenessProbe 失败时，会重启 2、ReadinessProbe 失败时，会标记NotReady

3、StartupProbe 3、Pre-Stop 3、Probe的探测方式 1、Exec 运行 2、HTTP-Get 3、TCP

### pod故障排除

|   |   |
|---|---|
|状态|描述|
|Pending<br><br>待定、挂起|pod创建已经提交到Kubernetes。但是，因为某种原因而不能顺利创建。例如下载镜像慢，调度不成功。|
|Running<br><br>运行|pod已经绑定到一个节点，并且已经创建了所有容器。至少有一个容器正在运行中，或正在启动或重新启动。|
|Completed<br><br>完成|Pod中的所有容器都已成功终止。|
|Failed<br><br>失败|Pod的所有容器均已终止，且至少有一个容器已在故障中终止。也就是说，容器要么**以非零状态**退出，要么被系统终止。|
|Unknown<br><br>未知|由于某种原因apiserver无法获得Pod的状态，通常是由于Master与Pod所在主机kubelet通信时出错。|
|CrashLoopBackOff<br><br>循环重启挂断|多见于CMD语句错误或者找不到container入口语句导致了快速退出,可以用kubectl logs 查看日志进行排错|

在早期编程当中，采用二进制编程，同时为了节省内存，使用0/1作标记；

因此，在C语言编程中，使用 return 0; 表示函数正常退出。因此，非零状态，我们通常认为失败或产生异常了。

### 命令帮助

暂时无法在飞书文档外展示此内容