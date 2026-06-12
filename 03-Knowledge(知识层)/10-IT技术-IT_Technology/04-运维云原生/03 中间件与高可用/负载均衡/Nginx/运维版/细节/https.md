![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300253292-3714b819-4fa8-4669-8f01-a9812f96f4ac.png "null")

非对称加密也不安全

可以伪造客户端

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300253353-c3f5b158-4acb-4733-bbc6-92c42fd12bb6.png "null")

CA机构保证不在网络传输的公钥安全【确定客户端和服务安全】【使用对称加密公钥 获取ca证书】

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737300253410-58bbcc99-b8ae-41c2-9fc4-fbdbe5b38082.png "null")

### HTTPS证书配置

HTTPS（HyperText Transfer Protocol Secure）是基于HTTP协议的安全协议，通过SSL/TLS协议加密HTTP请求和响应的内容，确保通信安全。配置HTTPS证书是让网站支持安全访问的关键步骤。下面将详细介绍如何配置HTTPS证书，包括自签名证书和CA签名证书的生成与配置。

### 1. 不安全的 HTTP 协议

默认情况下，HTTP 协议并不加密传输内容，所有信息以明文方式传输，容易受到中间人攻击（MITM）。为了提升安全性，HTTPS 通过使用 SSL/TLS 加密协议对数据进行加密。

### 2. OpenSSL 简介⭐

OpenSSL 是一个开源的实现了 SSL 和 TLS 协议的工具包，包含了 SSL 协议库、应用程序（如 `openssl` 命令行工具）以及密码算法库。OpenSSL 可以用来生成证书、管理证书、加密和解密数据。

#### OpenSSL包含的主要组件：

- **SSL协议库**：用于实现安全套接层（SSL）协议和传输层安全（TLS）协议。
- **应用程序**：包括 `openssl` 命令行工具，用于执行与证书管理、加密、解密相关的任务。
- **密码算法库**：包括常见的加密算法，如 RSA、AES、SHA 等。

### 3. 自签名证书【测试】

自签名证书是指由证书生成者自己签发的证书，通常用于测试或内部使用，不被公众信任的证书颁发机构（CA）签署。

#### 创建自签名证书的步骤：

1. **生成私钥**：

```
openssl genpkey -algorithm RSA -out server.key
```

2. **生成证书签署请求（CSR）**： 证书签署请求是用来向证书颁发机构（CA）申请证书的文件，但在自签名证书的情况下，CSR只是用于生成证书的请求文件。

```
openssl req -new -key server.key -out server.csr
```

3. **生成自签名证书**： 使用私钥和CSR生成自签名证书。

```
openssl x509 -req -in server.csr -signkey server.key -out server.crt
```

- `server.crt`：自签名证书。
- `server.key`：私钥。
- `server.csr`：证书签署请求。

4. **配置Web服务器（如 Nginx 或 Apache）**： 在Web服务器配置中，指定自签名证书和私钥文件的位置：Nginx 示例配置：

```
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/server.crt;
    ssl_certificate_key /path/to/server.key;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
```

### 4. 使用图形化工具 XCA

XCA（X Certificate and Key Management）是一个图形化工具，可以用来管理和生成 SSL 证书，私钥和证书签署请求。通过 XCA，用户可以轻松生成证书、私钥和CSR，而无需手动使用命令行。

#### 下载 XCA：

[下载地址](https://www.hohnstaedt.de/xca/index.php/download)

#### 使用 XCA 生成证书：

1. **下载并安装 XCA**。
2. **创建一个新数据库**： 打开 XCA，创建一个新的证书数据库（一个 `.xdb` 文件）。
3. **生成私钥和证书**：

- 在 XCA 中选择 "私钥" 标签，点击“新建”，然后选择生成新的私钥。
- 接着选择 "证书" 标签，点击 "新建证书"，在这里可以根据需要填写证书的相关信息，并选择“自签名”来生成自签名证书。

4. **导出证书和私钥**：

- 在生成证书后，可以导出证书文件和私钥文件，供 Web 服务器使用。

### 5. CA 签名证书

与自签名证书不同，CA签名证书是由受信任的证书颁发机构（CA）签发的证书，这些证书被广泛信任，适合生产环境中的应用。CA 签名证书需要申请并购买，常见的 CA 提供商包括 GlobalSign、Symantec、Comodo 等。

#### 获取 CA 签名证书的步骤：

1. **生成 CSR**（证书签署请求）： 使用 OpenSSL 或其他工具生成 CSR 文件，这个文件包含了关于你的服务器和公钥的信息，CA 会使用这个请求来生成一个证书。

```
openssl req -new -key server.key -out server.csr
```

2. **提交 CSR 给 CA**： 将生成的 CSR 提交给你选择的证书颁发机构（CA），CA 会进行验证并签署你的证书。
3. **安装 CA 签名证书**： CA 签发证书后，你会收到一个包含服务器证书和证书链的文件。你需要将这些文件安装到 Web 服务器中。Nginx 示例配置：

```
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/your_domain.crt;  # CA签名证书
    ssl_certificate_key /path/to/server.key;  # 私钥文件
    ssl_certificate_chain_file /path/to/ca_bundle.crt;  # CA证书链

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
```

### 总结

- **HTTPS证书配置** 提升网站安全，保护用户数据。
- **自签名证书** 通常用于测试或内部环境，不被公认的 CA 信任。
- **CA 签名证书** 是由受信任的证书颁发机构签发的，适用于生产环境。
- **XCA** 是一个方便的图形化工具，简化证书管理和生成过程。