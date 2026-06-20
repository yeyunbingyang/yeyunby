# 1- 工单说明

基于阿里云ECS云服务器完成基于ChatGLM-6B语言模型快速搭建AI对话机器人。

```
开发给出的软件要求，可参考：
    操作系统: Ubuntu系统（必须安装显卡驱动，模型基于GPU运行）
    硬件要求: 最低 4核 + 8GB内存 + 8GB显存 

已给出相关部署文档可参考
```

背景说明：

ChatGLM-6B是一个开源的、支持中英双语对话的语言模型，它基于General Language Model（GLM）架构，具有62亿参数；并使用了和ChatGPT相似的技术，经过约1TB标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，能够生成符合人类偏好的回答。

最终界面效果：

![[附件/7fab0d7a95.png]]

# 2- 申领阿里云ECS服务器

![[附件/003a89b008.png]]

![[附件/d77a2ab770.png]]

![[附件/6e52268507.png]]

存储：

- 建议： 系统盘的大小，调整为60GB以上，以确保可以正常安装操作

![[附件/c150c51753.png]]

带宽与安全组：

![[附件/983d51cad6.png]]

管理设置：

![[附件/3723a80e76.png]]

下单购买：

![[附件/93b33d9fdd.png]]

购买成功后， 进入管理控制台

![[附件/31d042d470.png]]

# 3- 通过远程连接工具连接

![[附件/e7f8da0a3c.png]]

![[附件/1cbb3f2e0f.png]]

说明： 此处远程主机IP为云服务器的公网IP（此IP随着每次释放，可能都会有变化），无法使用私有IP访问。

![[附件/99ca58c0fe.png]]

默认下，仅阿里云内部访问下才可使用私网IP

![[附件/cd1a201802.png]]

![[附件/5dca757f7d.png]]

![[附件/f5de083ed0.png]]

# 4- 基础Python环境准备

由于本次基于chatglm-6b大模型部署的聊天机器人，采用的Python语言开发的，使用大量的Python核心库，顾首先需要再服务器中安装Python环境。

本次采用安装Anaconda来安装，Anaconda是一款开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项，同时Anaconda还提供虚拟环境，支持隔离不同的Python环境，从而减少互相影响。故一般部署Python项目主要安装以Anaconda版本为主

- 1- 下载Anaconda

```
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
```

![[附件/e861f5c1f9.png]]

- 2- 安装Anaconda

```
bash Anaconda3-2024.10-1-Linux-x86_64.sh
```

![[附件/80620169c2.png]]

![[附件/72d1cd5af5.png]]

![[附件/3a6ed1bfe0.png]]

![[附件/b42efaf270.png]]

等待一会，直到出现以下界面（请注意， 不要多次回车，以免后续部分 默认跳过，导致环境没有一次性初始化）

![[附件/b42a573817.png]]

![[附件/84ae61ef1d.png]]

注意：如果没有跳出询问初始化的界面， 该怎么办？

```
cd /root  # 如果你不是root用户，切换到自己的家目录下
vim .bashrc

滚到文件的最后面。输入 i  进入插入模式，添加以下内容：
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/root/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/root/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/root/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


添加后， 保存退出即可
```

![[附件/c40ccc0da8.png]]

- 3- 退出重新连接下服务器即可

![[附件/cdc9e287d9.png]]

如果以上都搞定后， 接下来，就可以构建虚拟环境，完成部署项目了

```
# 创建虚拟环境
conda create --name chatglm python=3.10

# 进入虚拟环境
conda activate chatglm


# 如果需要离开此虚拟环境，可执行以下命令： 离开当前虚拟环境
conda deactivate
```

![[附件/e4f5f5ab0a.png]]

# 5- 模型部署实操

- 下载chatglm-6b模型

```
# 创建目录： 创建一个用于放置大模型项目相关内容的目录
mkdir -p /export/data/glm
# 切换目录
cd /export/data/glm

# 安装 国内模型资源平台
pip install -U huggingface_hub
# 设置模型资源地址
export HF_ENDPOINT=https://hf-mirror.com

# 下载对应模型内容（以下为一行）
huggingface-cli download --resume-download THUDM/chatglm-6b-int4 --local-dir THUDM/chatglm-6b-int4
```

![[附件/75cc4c630f.png]]

![[附件/c5084b226d.png]]

- 2- 下载ChatGLM-6B代码

```
cd /export/data/glm
# 通过 git方式
git clone https://github.com/THUDM/ChatGLM-6B.git
```

![[附件/9ff4760bba.png]]

如果偶遇无法基于git连接GitHub克隆项目，可采用离线上传的方式： 资料中提供ChatGLM-6B.tar.gz，直接上传到/export/data/glm目录下并解压即可

- 3- 安装依赖

```
cd /export/data/glm/ChatGLM-6B

pip install -r requirements.txt -i https://mirror.sjtu.edu.cn/pypi/web/simple
```

![[附件/b6bad487af.png]]

- 4- 修改代码：

- 在项目中， 部分的依赖资源可能由于我们项目放置路径问题，导致部分资源存在加载不上的问题，一般会和开发小伙伴沟通，确认资源放置位置，从而进行修改调整

```
修改cli_demo.py文件中的模型位置：
# 增加一行内容
model_path = "/export/data/glm/THUDM/chatglm-6b-int4"
# 修改部分参数
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
model = model.eval()
```

- 5- 运行cli_demo.py

```
cd /export/data/glm/ChatGLM-6B
python cli_demo.py
```

![[附件/86601874fd.png]]

当然，也支持可视化的方式来运行：

```
第一步， 修改web端的代码， 重新设置模型位置
vim web_demo2.py

输入i 进入插入修改， 并修改以下内容：

# 增加一行内容
model_path = "/export/data/glm/THUDM/chatglm-6b-int4"
# 修改部分参数
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
model = model.eval()
```

![[附件/e77ac92fa5.png]]

```
第二步： 下载相关web运行依赖
#Streamlit库：允许你使用 Python 脚本编写交互式和可视化的 Web 应用，而无需具备前端开发经验
pip install streamlit streamlit_chat
```

![[附件/03d8a0866a.png]]

```
第三步： 启动
python -m streamlit run web_demo2.py --server.port 80 --server.address 0.0.0.0
```

![[附件/2573521321.png]]

![[附件/6407a51303.png]]

访问： http://公网IP:80

```
http://47.113.207.49/
```

![[附件/4fdeee4309.png]]