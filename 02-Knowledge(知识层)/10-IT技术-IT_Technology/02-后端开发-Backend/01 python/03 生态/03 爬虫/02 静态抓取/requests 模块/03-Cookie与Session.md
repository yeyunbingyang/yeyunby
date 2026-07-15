---
title: requests Cookie与Session
domain: IT_Technology
tags:
  - Python
  - 爬虫
  - requests
status: 草稿
created: 2026-06-14
updated: 2026-06-14
source: 尚硅谷大模型技术之Python V1.0
related:
  - "[[01-核心请求与响应]]"
  - "[[02-POST-请求与数据来源]]"
  - "[[Python-MOC]]"
summary: 手动 Cookie 的三种携带方式 → Session 自动会话保持 → GitHub 模拟登录完整实战，覆盖爬虫状态管理的完整学习路径
---

# requests Cookie与Session

## 一句话结论

> 手动 Cookie 适合快速测试，Session 适合生产——创建 `session = requests.Session()` 后，登录一次即可自动保持所有后续请求的登录态，配合 GitHub 登录实战掌握从 Cookie 到 Session 的完整路径。

---

## 一、携带 Cookie 的三种方式

### 1.1 方式一：headers 携带（最直接）

从浏览器 DevTools 复制完整的 Cookie 字符串，直接粘贴进 headers：

```python
headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Cookie": "sessionid=abc123; csrftoken=xyz789; user_id=42"
}
response = requests.get(url, headers=headers)
```

**优点**：最快，一条龙复制粘贴。  
**缺点**：Cookie 过期需重新复制；字符串很长，代码混乱。

---

### 1.2 方式二：cookies 参数（推荐）

将 Cookie 字符串解析为字典，通过 `cookies=` 参数传入：

```python
# 手动构造 Cookie 字典
cookies = {
    "sessionid": "abc123",
    "csrftoken": "xyz789",
}

response = requests.get(url, headers=headers, cookies=cookies)
```

**Cookie 字符串 → 字典**：

```python
cookie_str = "sessionid=abc123; csrftoken=xyz789; user_id=42"

# 方法 1：字典推导式
cookies = {
    item.split("=")[0].strip(): item.split("=")[1].strip()
    for item in cookie_str.split(";") if "=" in item
}

# 方法 2：for 循环（更直观）
cookies = {}
for item in cookie_str.split(";"):
    if "=" in item:
        key, value = item.split("=", 1)
        cookies[key.strip()] = value.strip()
```

---

### 1.3 方式三：CookieJar 对象

`response.cookies` 返回的是 `CookieJar` 对象，不是普通 dict：

```python
response = requests.get(url)
resp_cookies = response.cookies        # CookieJar 对象
print(type(resp_cookies))              # <class 'requests.cookies.RequestsCookieJar'>
```

CookieJar 比 dict 多了域名、路径、过期时间等元信息，requests 内部用它管理 Cookie。

### 三种方式对比

| 方式 | 推荐度 | 适用场景 |
|------|--------|---------|
| `headers={"Cookie": "..."}` | ⭐ 测试用 | 快速验证，Cookie 固定不变 |
| `cookies={"key": "value"}` | ⭐⭐ 较清晰 | Cookie 需要解析/构造时 |
| Session 自动管理 | ⭐⭐⭐ 最省心 | 需要登录、多页面保持会话 |

---

## 二、Session 会话保持

### 2.1 为什么需要 Session

**手动 Cookie 的痛点**：

```python
# 每发一次请求都要手动设置 Cookie
response1 = requests.get(url1, headers={"Cookie": "..."})
response2 = requests.get(url2, headers={"Cookie": "..."})
response3 = requests.get(url3, headers={"Cookie": "..."})
```

- Cookie 可能过期，需重新获取
- 每次请求都要重复设置
- 字符串很长，代码混乱

**Session 自动管理模式**：

```python
session = requests.Session()
session.post(login_url, data=login_data)   # 登录 → Cookie 自动保存
session.get(page1_url)                      # 自动带上
session.get(page2_url)                      # 自动带上
# 整个过程不用写一行 Cookie 代码
```

> Session 内部维护了一个 CookieJar：每次收到 `Set-Cookie` 就存进去，每次发请求就自动带上。

### 2.2 基本用法

```python
import requests

# 1. 创建 Session
session = requests.Session()

# 2. 发送请求——和 requests.get() / requests.post() 完全一致
response = session.get("https://www.example.com", headers=headers)
response = session.post("https://www.example.com/login", data=data)

# 3. 查看当前保存的 Cookie
print(session.cookies)
# <RequestsCookieJar[<Cookie sessionid=abc123 for .example.com/>]>
```

### 2.3 headers 的两种设置方式

```python
# 方式一：每次请求都传（精确控制）
session.get(url1, headers=headers)
session.post(url2, headers=headers)

# 方式二：全局设置（推荐——所有请求共享）
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."
})
session.get(url1)   # 自动带上 UA
session.get(url2)   # 自动带上 UA
```

### 2.4 使用场景判断

| 场景 | 是否用 Session |
|------|---------------|
| 只发一次请求 | ❌ 不需要 |
| 先登录再爬取个人页面 | ✅ **必须用** |
| 多页面间需要保持状态（如购物车）| ✅ **推荐用** |
| 每次请求独立、不需要状态 | ❌ 不需要 |

### 2.5 常见问题

**Q: Session 和手动 Cookie 冲突吗？**  
如果同时在 Session 请求中传入 `cookies` 参数，两者**合并**，传入的优先级更高。

**Q: Session 的 Cookie 会持久化吗？**  
不会。只在内存中，程序结束即丢失。需持久化时手动保存到文件。

**Q: 多个 Session 之间独立吗？**  
是。每个 `Session()` 实例有独立的 CookieJar，互不干扰。

```python
session_a = requests.Session()   # 账号 A
session_b = requests.Session()   # 账号 B
# 两者完全独立
```

---

## 三、实战：GitHub 模拟登录

### 3.1 为什么 GitHub 适合练手

| 难度因素 | GitHub | 电商/社交网站 |
|---------|--------|-------------|
| 密码加密 | ❌ 明文提交 | ✅ JS 加密后再提交 |
| 验证码 | ❌ 无 | ✅ 图像验证码/滑块 |
| 动态 sign | ❌ 无 | ✅ 需逆向 JS 算法 |
| 动态 token | ✅ 有（`authenticity_token`）| ✅ 有（且数量更多）|
| 表单字段数 | 6 个 | 10-30+ 个 |

> GitHub 只比"直接复制 Cookie 粘贴"多了一步：从 HTML 中提取 `authenticity_token`。

### 3.2 第一步：分析登录表单

用无痕窗口打开 `https://github.com/login` → F12 → Elements → 定位 `<form>`：

```html
<form action="/session" accept-charset="UTF-8" method="post">
    <input type="hidden" name="authenticity_token" value="abc123...xyz">
    <input type="hidden" name="timestamp" value="1234567890">
    <input type="text" name="login">
    <input type="password" name="password">
    <input type="hidden" name="webauthn-support" value="supported">
    <input type="submit" name="commit" value="Sign in">
</form>
```

| 要素 | 值 | 说明 |
|------|-----|------|
| `method` | `post` | POST 提交 |
| `action` | `/session` | 完整 URL：`https://github.com/session` |
| `authenticity_token` | 动态 | 每次刷新变化，需提取 |
| `login` | 用户输入 | 账号 |
| `password` | 用户输入 | 密码 |
| `webauthn-support` | `"supported"` | 固定值 |
| `commit` | `"Sign in"` | 固定值 |
| `timestamp` | 时间戳 | 可省略 |

### 3.3 第二步：抓包验证

1. F12 → Network → 勾选 **Preserve log**
2. 填入账号密码 → 点击 Sign in
3. 找到 document 类型的 POST 请求（`/session`）
4. 查看 Payload → 确认提交的字段名和格式

> 登录成功返回 **302 重定向**。返回 200 且页面仍是登录页 → 认证失败。

### 3.4 第三步：代码实现

#### 基本版本

```python
import requests
import re

# 创建 Session
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
})

# 步骤 1：GET 登录页，提取 authenticity_token
login_page = session.get("https://github.com/login")
match = re.search(
    r'name="authenticity_token"\s+value="([^"]+)"',
    login_page.text
)
if not match:
    raise Exception("未找到 authenticity_token，页面结构可能已变化")
token = match.group(1)

# 步骤 2：构造登录数据并 POST
login_data = {
    "authenticity_token": token,
    "login": "你的GitHub账号",
    "password": "你的GitHub密码",
    "webauthn-support": "supported",
    "commit": "Sign in",
}

login_response = session.post("https://github.com/session", data=login_data)

# 判断结果
if "/session" in login_response.url:
    print("登录失败：仍在 /session 页面")
elif "login" in login_response.url:
    print("登录失败：被重定向回登录页")
else:
    print("登录成功！")

# 步骤 3：验证登录态
profile = session.get("https://github.com/settings/profile")
if "Sign in" not in profile.text[:500]:
    print("验证通过：已登录")
else:
    print("验证失败：未登录")
```

#### 封装版（推荐）

```python
import requests
import re

class GitHubLogin:
    """GitHub 模拟登录类"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        })

    def _get_token(self):
        resp = self.session.get("https://github.com/login")
        match = re.search(
            r'name="authenticity_token"\s+value="([^"]+)"',
            resp.text
        )
        if not match:
            raise Exception("未找到 authenticity_token")
        return match.group(1)

    def login(self):
        token = self._get_token()
        data = {
            "authenticity_token": token,
            "login": self.username,
            "password": self.password,
            "webauthn-support": "supported",
            "commit": "Sign in",
        }
        resp = self.session.post("https://github.com/session", data=data)
        return "/session" not in resp.url or "login" not in resp.url

    def is_logged_in(self):
        resp = self.session.get("https://github.com/settings/profile")
        return "Sign in" not in resp.text[:500]

# 使用
gh = GitHubLogin("你的账号", "你的密码")
if gh.login():
    print("登录成功！")
    if gh.is_logged_in():
        print("登录态验证通过")
        # 继续用 gh.session 访问任何需登录的页面
        stars = gh.session.get("https://github.com/你的账号?tab=stars")
```

### 3.5 常见问题排查

| 问题 | 原因 | 解决 |
|------|------|------|
| `authenticity_token` 提取为空 | 正则不匹配页面结构 | 打印 `login_page.text[:500]` 检查 |
| 登录后仍是未登录 | 没用 Session | 用 `session.post()` 而非 `requests.post()` |
| 422 状态码 | token 错误或过期 | 每次登录必须重新 GET 获取 token |
| 需手动处理重定向 | `allow_redirects=True` 默认跟随 | 设 `allow_redirects=False` 手动处理 |

```python
# 阻止自动跳转
resp = session.post(url, data=data, allow_redirects=False)
if resp.status_code == 302:
    print(f"重定向到: {resp.headers['Location']}")
```

## 关键概念

- **CookieJar**：requests 内部的 Cookie 封装对象，比 dict 多了域名、路径、过期时间等元信息
- **Session**：`requests.Session()` 返回的实例，内部维护 CookieJar 自动处理 Cookie 收发
- **session.headers.update()**：为 Session 设置全局默认请求头
- **authenticity_token**：Rails CSRF 防护 token，每次加载页面由服务端生成并嵌入 HTML，提交时必须回传
- **302 重定向**：登录成功后返回的状态码，requests 默认自动跟随
- **无痕窗口**：浏览器不携带任何 Cookie 的模式——用于测试未登录状态的页面效果

## 可行动建议

- 登录类爬虫第一件事：`session = requests.Session()`
- 用 `session.headers.update()` 设置全局 UA
- 登录成功后直接用 session 对象发后续请求，不再管 Cookie
- 调试时打印 `session.cookies` 确认 Cookie 是否正常保存
- 如果不确定是否登录成功，对比携带/不携带 Cookie 时页面的关键差异

## 延伸与关联

- [[01-核心请求与响应]] — GET/POST 请求基础、headers、timeout
- [[02-POST-请求与数据来源]] — POST data 字典五种来源（`authenticity_token` 属于来源三）
- [[Python-MOC]] — Python 知识体系总导航
- 下一步：挑战更复杂的登录——百度翻译（含 JS 逆向）或电商网站登录
