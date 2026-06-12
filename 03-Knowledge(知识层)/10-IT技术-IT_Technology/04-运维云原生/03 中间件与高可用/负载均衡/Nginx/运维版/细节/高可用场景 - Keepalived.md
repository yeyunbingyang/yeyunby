1. 为了避免一台机器宕机、需要使用多态、而前面负载到资源机【而负载机也有可能出现宕机】【死循环】
2. keekalived 多台资源机 主从 都使用虚拟ip地址 宕机后使用备用机![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300253235-5697cd9a-4767-4af3-9ce1-4b1aa61fac8a.png "null")

安装 **Keepalived** 主要有两种方式：**编译安装** 和 **YUM 安装**，你提供了两种安装方式的详细配置和步骤。下面是安装和配置 Keepalived 的完整步骤。

### 1. 编译安装 Keepalived

1. **下载 Keepalived 源码**： 下载链接：[Keepalived下载页面](https://www.keepalived.org/download.html#)
2. **解压并进入目录**：

```
tar -zxvf keepalived-x.x.x.tar.gz
cd keepalived-x.x.x
```

3. **编译和安装**： 在安装过程中，如果遇到 `OpenSSL` 相关的错误，说明系统缺少 OpenSSL 开发包，需要安装 `openssl-devel` 包。

```
./configure
make
sudo make install
```

4. **解决 OpenSSL 错误**： 如果在执行 `./configure` 时出现类似如下错误：

```
configure: error:  
!!! OpenSSL is not properly installed on your system. !!!
!!! Can not include OpenSSL headers files.
```

你需要先安装 OpenSSL 开发库：

```
sudo yum install openssl-devel
```

### 2. 使用 YUM 安装 Keepalived

如果你不想编译安装，可以直接使用 YUM 安装 `Keepalived`。只需要执行以下命令：

```
sudo yum install keepalived
```

### 3. 配置 Keepalived ⭐

安装完成后，配置文件通常位于 `/etc/keepalived/keepalived.conf`。下面是两台机器的最小配置示例：

#### 第一台机器（Master）

```
! Configuration File for keepalived

global_defs {
    router_id lb111  # 路由器 ID
}

vrrp_instance atguigu {
    state MASTER  # 设置为 MASTER
    interface ens33  # 使用的网络接口
    virtual_router_id 51  # 虚拟路由器 ID
    priority 100  # 优先级，MASTER 的优先级通常设置高一些
    advert_int 1  # 广告时间间隔
    authentication {
        auth_type PASS  # 认证类型
        auth_pass 1111  # 认证密码
    }
    virtual_ipaddress {
        192.168.44.200  # 配置虚拟 IP 地址
    }
}
```

#### 第二台机器（Backup）

```
! Configuration File for keepalived

global_defs {
    router_id lb110  # 路由器 ID
}

vrrp_instance atguigu {
    state BACKUP  # 设置为 BACKUP
    interface ens33  # 使用的网络接口
    virtual_router_id 51  # 虚拟路由器 ID
    priority 50  # 优先级，BACKUP 的优先级通常设置低一些
    advert_int 1  # 广告时间间隔
    authentication {
        auth_type PASS  # 认证类型
        auth_pass 1111  # 认证密码
    }
    virtual_ipaddress {
        192.168.44.200  # 配置虚拟 IP 地址
    }
}
```

### 4. 启动 Keepalived 服务

配置完成后，启动 `Keepalived` 服务。

```
sudo systemctl start keepalived
```

### 5. 查看 Keepalived 状态

可以通过以下命令检查 Keepalived 服务的状态：

```
sudo systemctl status keepalived
```

### 6. 设置开机自启

如果你希望 Keepalived 在系统启动时自动启动，可以执行以下命令：

```
sudo systemctl enable keepalived
```

### 总结

- 通过编译安装或使用 `yum` 安装 Keepalived。
- 配置文件 `/etc/keepalived/keepalived.conf` 中包含虚拟路由器 ID、优先级、认证信息和虚拟 IP 地址的配置。
- 启动服务并确保开机自启。