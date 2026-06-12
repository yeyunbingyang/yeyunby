针对使用 `pip` 下载速度慢的问题，可通过以下方法优化：

---

### 一、临时加速：指定国内镜像源

在 `pip install` 命令后添加 `-i` 参数直接使用国内镜像源，例如：

```
pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**常用镜像源**：

- 清华大学：`https://pypi.tuna.tsinghua.edu.cn/simple`
- 阿里云：`http://mirrors.aliyun.com/pypi/simple/`
- 中国科技大学：`https://pypi.mirrors.ustc.edu.cn/simple/`
- 豆瓣：`http://pypi.douban.com/simple/`

---

### 二、永久配置镜像源

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1761554249536-2d1e6263-631b-4d2b-95d9-54dbf7fa955f.png)

#### 1. **Windows 系统**

1. 在 `C:\Users\[用户名]\pip` 目录下新建 `pip.ini` 文件（若无 `pip` 文件夹需手动创建）。
2. 写入以下内容（以清华源为例）：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

其他镜像源需同步修改 `index-url` 和 `trusted-host` 参数。

#### 2. **Linux/Mac 系统**

1. 在用户根目录下创建 `.pip` 文件夹（若不存在）：

```
mkdir ~/.pip
```

2. 创建或修改 `~/.pip/pip.conf` 文件，内容同 Windows 配置。

---

### 三、其他优化方法

1. **使用** `.whl` **文件安装**  
    手动下载包的 `.whl` 文件后，通过本地路径安装：

```
pip install /path/to/package.whl
```

适用于大文件或网络不稳定场景。

2. **调整超时时间**  
    在配置文件中添加 `timeout` 参数，避免因网络波动导致下载中断：

```
[global]
timeout = 10000  # 单位：毫秒
```

---

### 四、注意事项

1. **镜像源信任设置**  
    `trusted-host` 必须与镜像源域名一致，否则会触发安全警告。
2. **文件编码与格式**  
    Windows 系统需确保 `pip.ini` 使用 ANSI 编码，避免因编码问题导致配置失效。

---

通过上述方法，可显著提升 `pip` 下载速度。如需完整镜像源列表或操作细节，可参考相关技术博客。