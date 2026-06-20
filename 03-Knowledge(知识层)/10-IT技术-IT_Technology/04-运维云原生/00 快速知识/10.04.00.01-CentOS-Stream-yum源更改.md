# 国内顶级镜像站（最常用）

国内大厂和高校维护的镜像站通常有非常清晰的 **“帮助文档 (Help)”**，点击对应的系统名称即可看到配置命令和地址。

|   |   |   |
|---|---|---|
|**镜像站名称**|**官网地址**|**特点**|
|**阿里云镜像**|[developer.aliyun.com/mirror/](https://developer.aliyun.com/mirror/)|运维首选，同步极快，带全套配置命令。|
|**清华大学 (TUNA)**|[mirrors.tuna.tsinghua.edu.cn](https://mirrors.tuna.tsinghua.edu.cn/help/centos-stream/)|包含详细的帮助文档（Help），学术和技术氛围浓厚。|
|**腾讯云镜像**|[mirrors.cloud.tencent.com](https://mirrors.cloud.tencent.com/)|适合腾讯云内网环境加速。|
|**华为云镜像**|[mirrors.huaweicloud.com](https://mirrors.huaweicloud.com/)|对鲲鹏等国产硬件支持非常好。|

# CentOS Stream 9

[https://www.cnblogs.com/hahaha111122222/p/18853560](https://www.cnblogs.com/hahaha111122222/p/18853560)

CentOS Stream 9 的主要源配置文件位于 `/etc/yum.repos.d/` 目录下，通常是 `centos.repo` 和 `centos-addons.repo`。建议先备份：

```
sudo cp -a /etc/yum.repos.d/centos.repo /etc/yum.repos.d/centos.repo.backup
sudo cp -a /etc/yum.repos.d/centos-addons.repo /etc/yum.repos.d/centos-addons.repo.backup
```

### 2. 替换为阿里云镜像源

有两种常用方法：

**方法一：直接下载或编写新的 repo 文件**  
你可以创建或编辑 `centos.repo` 文件，内容参考阿里云镜像站的配置。以下是一个示例配置（请根据实际情况调整仓库地址）：

```
[baseos]
name=CentOS Stream $releasever - BaseOS
baseurl=https://mirrors.aliyun.com/centos-stream/$releasever-stream/BaseOS/$basearch/os/
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/centos-stream/RPM-GPG-KEY-CentOS-Official
enabled=1

[appstream]
name=CentOS Stream $releasever - AppStream
baseurl=https://mirrors.aliyun.com/centos-stream/$releasever-stream/AppStream/$basearch/os/
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/centos-stream/RPM-GPG-KEY-CentOS-Official
enabled=1

[crb]
name=CentOS Stream $releasever - CRB
baseurl=https://mirrors.aliyun.com/centos-stream/$releasever-stream/CRB/$basearch/os/
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/centos-stream/RPM-GPG-KEY-CentOS-Official
enabled=1
```

类似地，根据需要配置 `centos-addons.repo` 中的其他仓库（如 extras、plus 等）。

**方法二：使用 sed 命令替换原有镜像地址**  
如果不想完全重写文件，可以用 sed 命令将官方地址批量替换为阿里云地址：

```
# 注释掉 metalink 行
sudo sed -i 's|^metalink|#metalink|' /etc/yum.repos.d/epel*.repo
# 将 baseurl 行取消注释并指向阿里云镜像
sudo sed -i 's|^#baseurl=https://download.example/pub|baseurl=https://mirrors.aliyun.com|' /etc/yum.repos.d/epel*.repo
```

注意：CentOS Stream 9 的默认 repo 文件可能使用 `metalink`，替换后需注释掉 `metalink` 行并启用 `baseurl`。

### 3. 清理并重建缓存

替换完成后，运行以下命令：

```
sudo dnf clean all    # 或 yum clean all
sudo dnf makecache    # 或 yum makecache
```

这会将旧的缓存清除，并从阿里云镜像重新生成软件包元数据缓存。

### 4. 测试更新

最后，可以执行一次系统更新测试是否正常工作：

```
sudo dnf update --refresh
```

如果更新过程顺利且速度明显提升，说明镜像源已成功切换。

### 注意事项

- **确保网络连通**：请确认服务器可以正常访问 `mirrors.aliyun.com`。
- **GPG 密钥**：阿里云镜像通常使用与官方相同的 GPG 密钥，因此 `gpgkey` 指向的地址可以保持不变或使用阿里云提供的副本。
- **仓库对应关系**：阿里云镜像中 CentOS Stream 9 的路径结构与官方类似，但需确认仓库（如 BaseOS、AppStream、CRB）的路径是否正确。
- **如果遇到问题**，可以检查 `/etc/yum.repos.d/` 下的文件格式是否正确，或暂时恢复备份文件。

通过以上步骤，你就可以将 CentOS Stream 9 的软件源替换为阿里云镜像，从而获得更快的下载速度和更稳定的更新体验。

# CentOS Stream 10

在 CentOS Stream 10 中，传统的 `yum` 已经被 `dnf` 完全取代（虽然 `yum` 命令仍作为软链接存在），且配置文件结构延续了 RHEL 10 的逻辑。

由于 CentOS Stream 10 是比较新的滚动发行版，替换源的操作主要涉及 `/etc/yum.repos.d/` 目录下的 `.repo` 文件。

---

### 1. 核心步骤：替换为国内镜像源（以阿里云为例）

目前国内主流镜像站（如阿里、网易、清华）对 Stream 10 的支持正在同步中。以下是通用替换逻辑：

#### 第一步：备份现有的源配置

在进行任何修改前，先归档旧配置：

```
mkdir /etc/yum.repos.d/bak
mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak/
```

#### 第二步：下载/创建新的源文件

你可以直接手动创建一个新的 `centos.repo` 文件，或者使用 `curl` 下载：

Bash

```
cat <<EOF > /etc/yum.repos.d/centos-stream.repo
[baseos]
name=CentOS Stream 10 - BaseOS
baseurl=https://mirrors.aliyun.com/centos-stream/10-stream/BaseOS/x86_64/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial

[appstream]
name=CentOS Stream 10 - AppStream
baseurl=https://mirrors.aliyun.com/centos-stream/10-stream/AppStream/x86_64/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
```

**注意：** 如果你的 CPU 架构是 ARM，请将路径中的 `x86_64` 替换为 `aarch64`。

#### 第三步：刷新缓存

```
dnf clean all
dnf makecache
```

---

### 2. 自动化替换工具：`sed` 技巧

如果你不想删除原文件，而是想直接修改官方文件中的 URL，可以使用你之前笔记中提到的 **“Shell 三剑客”**：

Bash

```
# 将官方镜像域名替换为阿里云域名
sed -i 's|mirror.stream.centos.org|mirrors.aliyun.com/centos-stream|g' /etc/yum.repos.d/centos*.repo

# 取消 baseurl 的注释（如果原文件使用的是金属连接/mirrorlist）
sed -i 's|^#baseurl|baseurl|g' /etc/yum.repos.d/centos*.repo
sed -i 's|^mirrorlist|#mirrorlist|g' /etc/yum.repos.d/centos*.repo
```

