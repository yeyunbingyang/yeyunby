# 页面无法访问

selinux关闭

端口开放 80

在 **GitLab** 中，如果你想把默认的 **HTTP/80 或 HTTPS/443 端口**改成其他端口，需要修改配置文件，然后重新配置 GitLab。下面是详细步骤。⚙️

---

# 更改应用端口

## 一、修改 GitLab 端口

编辑 GitLab 配置文件：

```
sudo vim /etc/gitlab/gitlab.rb
```

找到或添加以下配置（以改成 8081 为例）：

```
external_url 'http://服务器IP:8081'
```

注意：

- 如果是 HTTPS，改端口需要 `https://服务器IP:8443`
- GitLab 会自动修改内部 nginx 配置为对应端口

---

## 二、重新配置 GitLab

修改配置后必须执行：

```
sudo gitlab-ctl reconfigure
```

这会更新 nginx、puma 等服务的端口设置

---

## 三、检查端口监听

```
ss -lntp | grep 8081
```

你应该看到：

```
0.0.0.0:8081  users:(("nginx",pid=xxxx,fd=xx))
```

---

## 四、防火墙设置

确保新端口放行：

```
firewall-cmd --add-port=8081/tcp --permanent
firewall-cmd --reload
```

如果使用 Ubuntu：

```
ufw allow 8081/tcp
```

---

## 五、访问 GitLab

修改浏览器地址：

```
http://服务器IP:8081
```

如果原先是 HTTPS，还要指定 `https://服务器IP:8443`

---

## 六、注意事项

1. **external_url** 是核心配置，一定要和你访问的端口一致
2. 修改端口后，如果有 CI/CD 或 Webhook，需要同步修改 URL
3. SELinux 或防火墙规则也需要允许新端口

---

如果你需要，我可以帮你写一个 **完整示例：GitLab 改端口 + 防火墙放行 + 测试访问**，保证改完后直接可以在浏览器访问。

你希望我帮你写吗？

# 默认账号密码

## 一、默认账号

默认管理员账号：

```
用户名: root
```

---

## 二、默认密码查看位置（最重要）

GitLab 会把初始密码保存到：

```
/etc/gitlab/initial_root_password
```

查看命令：

```
cat /etc/gitlab/initial_root_password
```

会看到类似：

```
Password: 3Z9f4Yh7kLm2QpX
```

登录：

```
http://服务器IP
用户名: root
密码: 上面的密码
```

---

## 三、注意（重要）

这个文件 **24****小时****后****会****自动****删除**。

官方说明：

为安全原因，initial_root_password 文件会在第一次 reconfigure 后保留 24 小时。

如果文件没了，就只能 **重****置****密码**。

---

## 四、如果密码文件不存在（重置 root 密码）

执行：

```
gitlab-rake "gitlab:password:reset[root]"
```

然后输入新密码即可。

# docker安装

[https://docs.gitlab.com/install/docker/installation/](https://docs.gitlab.com/install/docker/installation/)