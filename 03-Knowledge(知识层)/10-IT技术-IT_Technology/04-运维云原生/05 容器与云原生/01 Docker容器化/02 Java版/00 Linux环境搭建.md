# 1.准备Linux环境

首先，我们要准备一个Linux的系统，成本最低的方式就是在本地安装一台虚拟机。为了统一学习环境，不管是使用MacOS还是Windows系统的同学，都建议安装一台虚拟机。

windows采用VMware，Mac则采用Fusion

## 1.1.安装VMware

VMware是业界最好用的虚拟机软件之一。

windows版本的网站如下：

[https://www.vmware.com/cn/products/workstation-pro/workstation-pro-evaluation.html](https://www.vmware.com/cn/products/workstation-pro/workstation-pro-evaluation.html)

Mac下也有对应版本，叫做VMware Fusion：

[https://www.vmware.com/cn/products/fusion.html](https://www.vmware.com/cn/products/fusion.html)

特别注意，Windows10以上版本操作系统需要下载安装VMware Workstation Pro16及以上版本，安装方式此处略。

如果自己电脑上已经有了低版本的VMware，则需要先卸载，再重新安装。卸载过程比较麻烦。

### 1.1.1.卸载旧版VMware（可选）

首先，在控制面板找到程序和功能选项，找到VMware，进行卸载操作：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268374890-f1044df1-10d2-40b6-b41d-b50603f29722.png "null")

弹出确认框, 点击"下一步":

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268374963-cf010738-88fe-4a4f-be2d-63fcddb3a416.png "null")

下一步之后, 选择删除:

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375014-d8ba4ab4-fa4e-4b47-b720-b75f52130135.png "null")

接下来，按照提示完成卸载操作即可。

卸载完成后，还需要看看VMware的安装目录是否有旧数据，一并清理掉。

比如安装在**C盘的******Program Files**(**x86**)**：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375072-9ba0080e-e7d8-492a-aa70-a80ffe054f1d.png "null")

则需要直接删除整个VMware目录：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375154-8411d3fb-a9a1-4c24-b595-b175891abe57.png "null")

接下来要清理注册表：

首先，按住Windows + R , 在弹出框中输入 "regedit" 调出注册表：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375210-948d308b-acc0-4ce0-a3cb-b365b220258a.png "null")

进入注册表编辑器，如图：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375255-85db4e8c-c7c7-48ae-99e8-7fdc7f37c369.png "null")

打开**`HKEY_CURRENT_USER`**文件夹，找到**`Software`**文件夹并打开

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375310-21d026a1-03a2-4bae-96b1-fcc2d84fd471.png "null")

找到“VMware.Inc”，右键删除：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375367-089f01f2-8be5-48cb-9aba-d62b76ea366d.png "null")

### 1.1.2.安装VMware

安装步骤略。。

安装以后可以免费试用，大家可以去官网购买正版许可证，或者去网上看看有没有好心人赠送你一个许可证。启动后的界面如图所示：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375418-fbd79576-21b6-4178-b4a9-9888ff473db3.png "null")

### 1.1.3.常见错误

如果VMware虚拟机运行报错，例如：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375464-d818326a-57ff-413f-9317-91fd5361ee78.png "null")

这个是由于英特尔的虚拟化技术, 没有开启, 需要进入系统的BIOS界面 , 开启英特尔的虚拟化技术 ; 不同的电脑型号 , 进入BIOS界面的方式不同, 需要百度查询一下自己电脑的型号 , 如何进BIOS ;

windows10系统可以参考: [https://blog.csdn.net/biu_code/article/details/107504627](https://blog.csdn.net/biu_code/article/details/107504627)

以ThinkPad为例，如图：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375512-df83c85d-1793-4480-9139-4133710800ae.png "null")

## 1.2.创建虚拟机

Centos7是比较常用的一个Linux发行版本，在国内的使用比例还是比较高的。

大家首先要下载一个Centos7的iso文件，我在资料中给大家准备了一个mini的版本，体积不到1G，推荐大家使用：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375570-d2e836b6-3682-4b70-8420-c30adde8354c.png "null")

我们在VMware《主页》界面中点击《创建新的虚拟机》按钮：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375636-24094483-7f4e-4753-af18-9d9b73c38bc6.png "null")

然后会弹出一个窗口，我们直接点击下一步：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375693-252a1d74-f5f6-4ce5-9a1c-3c14124675b5.png "null")

然后页面中选择你准备好的ISO文件，继续点击下一步：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375747-08891f5b-2b94-4163-92a9-3eff58a4b9a6.png "null")

然后填写`虚拟机的名称`以及虚拟机将来`保存的位置`：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375797-e1a395e8-107a-4784-96a9-158d5445229a.png "null")

再次下一步，填写虚拟机磁盘大小。这里建议给大一点，否则将来不够用调整起来麻烦。而且这里设置大小并不是立刻占用这么多，而是设置一个上限：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375856-c35d1a35-e330-44df-88d8-e80e52bee92c.png "null")

继续下一步，然后选择虚拟机硬件设置：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375904-5b1a5e8d-50e6-4685-a321-fcc4aa7597e6.png "null")

在弹出的窗口中设置虚拟机硬件，建议CPU给到4核，内存给到8G：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268375966-428cfed1-80ff-4155-ae37-4c3854492c69.png "null")

配置完成后，点击`关闭`，回到上一页面，继续点击`完成`：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376023-42898a6c-4614-449c-aff3-4cee7460d2fd.png "null")

虚拟机就创建完毕了：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376079-37c3f2c6-a05f-4490-a964-7bf44f7c7b8b.png "null")

## 1.3.安装Centos7

接下来，我们启动刚刚创建的虚拟机，开始安装Centos7系统：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376129-8f63dd35-4702-4229-b026-005a8fa61ab2.png "null")

启动后需要选择安装菜单，将鼠标移入黑窗口中后，将无法再使用鼠标，需要按上下键选择菜单。选中Install Centos 7 后按下回车：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376183-d0753983-1962-4148-b732-0efd6f6dcb33.png "null")

然后会提示我们按下enter键继续：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376233-6fcba739-6da8-4b40-b25c-52fd70e8af3d.png "null")

过一会儿后，会进入语言选择菜单，这里可以使用鼠标选择。选择中文-简体中文，然后继续：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376276-3ce96a58-ccad-4887-a5ba-b0d9f39bd585.png "null")

接下来，会进入安装配置页面：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376325-c2394e78-8282-4a2a-94a2-dff05e656aae.png "null")

鼠标向下滚动后，找到系统-安装位置配置，点击：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376372-b90034d9-a09c-48a3-8b8d-848cb809b0c8.png "null")

选择刚刚添加的磁盘，并点击完成：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376417-fffd543b-e438-46a0-b493-7fe840b04577.png "null")

然后回到配置页面，这次点击《网络和主机名》：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376471-b89932de-c76a-49ef-8433-eef6f275b31b.png "null")

在网络页面做下面的几件事情：

1. 修改主机名为自己喜欢的主机名，不要出现中文和特殊字符，建议用localhost

2. 点击应用

3. 将网络连接打开

4. 点击配置，设置详细网络信息

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376523-320d11cc-e358-4861-a563-0c4b18114da8.png "null")

最好用一个截图软件，记住上图中的网络详细信息，接下来的配置要参考：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376575-bcae9612-5819-48a7-96c6-cc357e80031b.png "null")

点击配置按钮后，我们需要把网卡地址改为静态IP，这样可以避免每次启动虚拟机IP都变化。所有配置照搬你自己截图的网络信息填写，不要照抄我的：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376627-f8cccfd1-928f-4702-a5f3-81ad58830da6.png "null")

上图中的四个信息参考之前的**以太网****(ens33)****网卡**的截图，不要照搬我的来写。

最后，点击完成按钮：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376679-1a3ae866-f81c-47e3-affe-b220f0f3cecd.png "null")

回到配置界面后，点击`开始安装`：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376736-6bdbec7e-4bcc-4a5d-89e5-a97f03ce7325.png "null")

接下来需要设置root密码：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376787-82d13bbc-2f66-4815-a6d9-151cad070fd8.png "null")

填写你要使用的root密码，然后点击完成：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376849-e8ecf051-0eb3-439f-8878-abafdee9b5ea.png "null")

接下来，耐心等待安装即可。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376899-87f2a153-b063-4d8c-abba-373e65057704.png "null")

等待安装完成后，点击**重启**：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268376946-26c1389e-ae2e-41b2-82c8-efb4611f939f.png "null")

耐心等待一段时间，不要做任何操作，虚拟机即可启动完毕：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377004-896039a8-c37f-460c-8253-dc809ecf9ead.png "null")

输入用户名root，然后点击回车，会要求你输入密码：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377055-246bb201-4499-4388-a57c-6591c1df518e.png "null")

此时你要输入密码，不过需要注意的是密码是**隐藏**的，输入了也看不见。所以放心输入，完成后回车即可：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377113-dd1a5718-511f-49cb-b72c-d477cd16d4a3.png "null")

只要密码输入正确，就可以正常登录。此时可以用命令测试虚拟机网络是否畅通：

```
ping baidu.com
```

如果看到这样的结果代表网络畅通：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377193-c0e3efa1-ee1f-438f-8e9a-259a97ecd6dc.png "null")

默认ping命令会持续执行，按下`CTRL` + `C`后命令即可停止。

## 1.4.设置虚拟机快照

在虚拟机安装完成后，最好立刻设置一个快照，这样一旦将来虚拟机出现问题，可以快速恢复。

我们先停止虚拟机，点击VMware顶部菜单中的`暂停``下拉选框`，选择`关闭客户机`：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377245-1814f8a2-601f-4018-aa0a-19c3b6fa0829.png "null")

接着，点击VMware菜单中的🔧按钮:

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377300-52bb1c65-76eb-4360-b394-0039fa2cffa1.png "null")

然后在弹出的快照管理窗口中，点击**拍摄快照**，填写新的快照信息：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377355-10471f1f-34fc-4e8f-83bb-6352a1ff9a61.png "null")

快照拍摄完成了！而且我们可以在不同阶段拍摄多个不同快照作为备份，方便后期恢复数据。

假如以后虚拟机文件受损，需要恢复到初识状态的话，可以选中要恢复的快照，点击转到即可：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377404-abf06664-4867-4cef-9628-5ce4e2873d7e.png "null")

# 2.SSH客户端

在VMware界面中操作虚拟机非常不友好，所以一般推荐使用专门的SSH客户端。市面上常见的有：

- Xshell：个人免费，商业收费，之前爆出过有隐藏后门。不推荐

- Finshell：基础功能免费，高级功能收费，基于Java，内存占用较高（在1个G左右）。不推荐

- MobarXterm：基础功能免费、高级功能收费。开源、功能强大、内存占用低（只有10m左右），但是界面不太漂亮。推荐使用

## 2.1.安装MobarXterm

这里我们会选择内存占用较低的MobarXterm作为SSH客户端，其官网地址：

[https://mobaxterm.mobatek.net/](https://mobaxterm.mobatek.net/)

安装完成后界面如图所示：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377469-2a528738-572a-47f9-88b4-a1441555632f.png "null")

点击session按钮，进入会话管理：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377525-7db7c178-33da-4a31-8983-df36e95ee70e.png "null")

在弹出的session管理页面中，按照下图填写信息并保存：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377572-254694b9-f65e-4c81-a460-2cc3ab775153.png "null")

点击OK后会提示你是第一次连接，询问你是信任连接的服务：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377624-a637f790-6694-4975-b6c3-78da838fb784.png "null")

选择accept之后，会询问你是否要记住密码，选择yes：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377683-86add46e-e327-45d7-8581-2e5ef73e38fc.png "null")

紧接着需要你设置一个MobarXterm的全局密码用于做密码管理，建议设置一个与虚拟机密码不同的：

输入密码：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377730-fb86f007-65d5-4d24-a5c3-140d16d8011c.png "null")

输入成功后，就会连接成功，并进入操作界面了：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377782-411122f1-99c3-4e7a-84af-0e542c600c4e.png "null")

这里需要做一些基础的配置：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377844-3dd5436f-46c4-47c2-81e3-2e6bc90ede1d.png "null")

## 2.2.配置默认编辑器

首先建议设置一下默认编辑器，这样我们通过MobarXterm的FTP工具打开文件时会以指定的编辑器打开，方便修改。我这里配置的是vscode：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377899-8510ba65-2d97-4f25-a804-cb65cd244ded.png "null")

## 2.3.配置右键粘贴

复制粘贴是很常用的配置，MobarXterm默认左键选中即**复制**，但是需要配置右键点击为**粘贴：**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268377963-12793384-e629-4c3d-ba0d-30f159e2d341.png "null")

这样，复制和粘贴可以全部通过鼠标操作，无需按键。

## 2.4.SSH配置

接下来还有几个ssh配置：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268378014-4ce30041-f501-405d-ac2f-a1cc18fdf1cf.png "null")

分别是：

- 默认的登录用户

- ssh保持连接

- 取消连接成功后的欢迎banner

## 2.5.关闭X-Server服务

大多数情况下，我们没有x-server的需求，因此可以选择不要自启动：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737268378068-9e502e0b-95bd-4f4f-9cfc-b76b192ac996.png "null")