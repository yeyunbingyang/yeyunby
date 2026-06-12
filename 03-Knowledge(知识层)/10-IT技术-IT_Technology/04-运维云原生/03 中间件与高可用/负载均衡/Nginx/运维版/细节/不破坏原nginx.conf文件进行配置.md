为了实现**完全不破坏原有的** `**nginx.conf**`，且**不需要 WordPress**，我们将采用“配置分离”方案。

这个示例将创建一个独立的 HTML 首页，并通过一个独立的配置文件来管理它。

---

### 1. 准备静态页面文件

首先，我们在一个独立于 Nginx 安装目录的位置创建网页文件，这样即使你以后升级或重装 Nginx，网页数据也不会丢失。

Bash

```
# 创建网页存放目录
mkdir -p /var/www/mysite

# 编写首页文件
cat <<EOF > /var/www/mysite/index.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>欢迎来到我的服务器</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #eceff1; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #3498db; }
        h1 { color: #2c3e50; margin-bottom: 10px; }
        p { color: #7f8c8d; font-size: 1.1em; }
        .tag { background: #e8f4fd; color: #3498db; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚀 Nginx 服务已就绪</h1>
        <p>这是位于 <span class="tag">CentOS Stream 10</span> 上的独立站点</p>
        <p>配置已实现物理隔离，主文件未受污染。</p>
    </div>
</body>
</html>
EOF
```

---

### 2. 配置主文件（仅一次性引导）

我们需要在 `nginx.conf` 中加入一行“指令”，让它去读取外部配置。

编辑 `/usr/local/nginx/conf/nginx.conf`，在 `http { ... }` 块的最后一行（但在最后一个 `}` 之前）添加：

Nginx

```
http {
    # ... 原有的各种参数保持不动 ...

    # 关键行：包含所有子配置
    include /usr/local/nginx/conf/conf.d/*.conf;
}
```

---

### 3. 创建独立站点配置文件

现在，我们把所有的站点逻辑写在这个独立文件中：

Bash

```
# 创建配置文件夹
mkdir -p /usr/local/nginx/conf/conf.d

# 编写站点配置
cat <<EOF > /usr/local/nginx/conf/conf.d/mysite.conf
server {
    listen       80;
    server_name  localhost; # 如果有域名可以填入域名

    location / {
        root   /var/www/mysite;
        index  index.html;
    }

    # 专门处理错误页面
    error_page  404              /404.html;
    error_page  500 502 503 504  /50x.html;
}
EOF
```

---

### 4. 权限设置与生效

为了确保 Nginx 进程（你之前创建的 `www` 用户）能够读取这些文件：

Bash

```
# 修正目录所有权
chown -R www:www /var/www/mysite
chmod -R 755 /var/www/mysite

# 语法检查
/usr/local/nginx/sbin/nginx -t

# 热重启（不影响现有连接）
/usr/local/nginx/sbin/nginx -s reload
```

---

### 📝 最终检查清单

- **主文件**：只加了一行 `include`，结构依然清晰。

- 原文件locallhost 域名会覆盖

- **安全性**：页面文件放在 `/data` 目录下，权限归属 `www` 用户。
- **扩展性**：以后如果你想再加一个站点，只需在 `conf.d/` 下新建一个 `.conf` 文件并 `reload` 即可，完全不需要动 `nginx.conf`。