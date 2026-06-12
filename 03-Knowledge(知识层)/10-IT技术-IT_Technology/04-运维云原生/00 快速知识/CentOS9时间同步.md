在 CentOS Stream 9 中，默认的时间同步服务是 chrony，而不是传统的 ntpd。 因此，建议使用 chrony 来配置和管理时间同步。 以下是使用 chrony 配置 NTP 服务的步骤：

## 1、安装chrony

```
sudo dnf install -y chrony
```

## 2、启动并启用 chronyd 服务

安装完成后，启动 chronyd 服务，并设置为开机自启：

```
sudo systemctl enable --now chronyd
```

## 3、配置 NTP 服务器

编辑 /etc/chrony.conf 配置文件，添加或修改 NTP 服务器地址。 例如，使用阿里云的 NTP 服务器：

```
sudo vi /etc/chrony.conf
```

在文件中找到以下行：

```
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (https://www.pool.ntp.org/join.html).

pool 2.centos.pool.ntp.org iburst
```

将其替换为：

```
# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (https://www.pool.ntp.org/join.html).
# pool 2.centos.pool.ntp.org iburst

server ntp1.aliyun.com iburst
server ntp2.aliyun.com iburst
server ntp3.aliyun.com iburst
server ntp4.aliyun.com iburst
server ntp5.aliyun.com iburst
server ntp6.aliyun.com iburst
```

保存并退出编辑器。

## 4、重启 chronyd 服务

修改配置后，重启 chronyd 服务以使更改生效：

```
sudo systemctl restart chronyd
```

## 5、验证时间同步状态

使用以下命令检查时间同步状态：

```
chronyc tracking
date
```

此外，您还可以使用以下命令查看 NTP 服务器的同步状态：

```
chronyc sources
```

如果输出中有 `^*` 标记的服务器，表示该服务器正在被使用进行时间同步。

## 6、设置时区

如果需要设置时区，可以使用 timedatectl 命令：

```
sudo timedatectl set-timezone Asia/Shanghai
```

请根据您的实际时区进行调整。

## 7、时间格式显示不同

输入date命令，如下所示：
![[Pasted image 20260607012813.png]]


LC_TIME 或 LANG 环境变量可能在两台系统上不同。例如，一台可能使用中文区域（如 zh_CN.UTF-8），另一台可能使用默认英文区域（如 en_US.UTF-8），从而影响日期格式。

统一方案：

```
locale
# 设置时间区域
export LC_ALL=en_US.UTF-8
或
export LC_ALL=zh_CN.UTF-8
```

通过以上步骤，就可以在 CentOS 9 上成功配置 NTP 服务，确保系统时间的准确性。