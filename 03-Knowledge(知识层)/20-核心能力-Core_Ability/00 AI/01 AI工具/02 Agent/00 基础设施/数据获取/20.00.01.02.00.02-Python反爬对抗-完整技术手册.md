# Python 反爬对抗 — 完整技术手册

> 从 TLS 指纹到浏览器指纹，从 CF 到 DataDome
> 更新时间：2026-06-19

---

## 0. 反爬检测的四个层次（一次性讲清楚）

```
你发送请求
    │
    ▼
┌─────────────────────────────────────────────────────┐
│ Layer 1: IP 信誉                                    │
│   ASN 归属、数据中心 vs 住宅、请求频率               │
│   被拦表现：直接 403 / 空响应 / 要求登录             │
│   解决：住宅代理、移动代理、请求间隔                 │
├─────────────────────────────────────────────────────┤
│ Layer 2: TLS / HTTP/2 指纹                         │
│   JA3/JA4、密码套件顺序、H2 SETTINGS、Header 顺序   │
│   被拦表现：Cloudflare 1020 / 403 无 Challenge      │
│   解决：curl_cffi、tls-client、真实浏览器            │
├─────────────────────────────────────────────────────┤
│ Layer 3: 浏览器 JS 指纹                             │
│   navigator.webdriver、Canvas、WebGL、Audio、字体    │
│   被拦表现：Turnstile/DataDome 弹出验证/滑块         │
│   解决：Camoufox、Patchright、undetected-chromedriver│
├─────────────────────────────────────────────────────┤
│ Layer 4: 行为分析                                   │
│   鼠标轨迹、滚动速度、点击精度、页面停留时间         │
│   被拦表现：验证完又弹、随机拦截、shadow ban         │
│   解决：humanize 延迟、Bezier 曲线、session 预热    │
└─────────────────────────────────────────────────────┘
```

**关键认知**：每一层独立评分。过了 Layer 1 不代表 Layer 2 不会被拦。四层全过才能稳定抓取。

---

## Layer 1: IP 信誉

### 1.1 IP 类型金字塔

```
            成功率
LTE/5G 移动代理    ████████████████████  95%+
   ↓
住宅代理 (Resi)    ██████████████████    85-95%
   ↓
ISP 静态代理       ██████████████        70-85%
   ↓
数据中心代理       ████████              40-60%
   ↓
云服务器 IP        ███                   10-30%  ← 你的本地/云服务器在这里
```

### 1.2 Python 代理写法

```python
# 基础写法
proxies = {
    'http': 'http://user:pass@residential-proxy.com:8080',
    'https': 'http://user:pass@residential-proxy.com:8080',
}
resp = requests.get(url, proxies=proxies, timeout=30)

# curl_cffi
from curl_cffi import requests as cffi_requests
session = cffi_requests.Session(impersonate='chrome124')
resp = session.get(url, proxies=proxies)

# Playwright
browser = p.chromium.launch(proxy={
    'server': 'http://residential-proxy.com:8080',
    'username': 'user',
    'password': 'pass',
})
```

### 1.3 请求频率控制

```python
import time
import random

# ❌ 机器式间隔 — 容易被检测
time.sleep(2)

# ✅ 拟人随机间隔
time.sleep(random.uniform(3, 8))                    # 页间间隔
time.sleep(random.uniform(0.5, 2.5))                # 元素间间隔

# ✅ 带抖动的批量请求
def human_delay(base=2.0):
    jitter = random.gauss(0, base * 0.3)             # 高斯分布抖动
    time.sleep(max(0.5, base + jitter))
```

---

## Layer 2: TLS / HTTP/2 指纹

### 2.1 为什么 `requests` 直接 403

```
标准 requests 库（OpenSSL）发送的 TLS ClientHello:
  → JA3 指纹明确标识 "Python/urllib3"
  → Cloudflare/DataDome 看到这个指纹 → 直接 403，不给任何 Challenge
这才是"为什么我用 requests 连页面都看不到"的根本原因。
```

### 2.2 curl_cffi — 最轻量解决方案（⭐ 首推）

```bash
pip install curl-cffi
```

```python
from curl_cffi import requests

# ========== 基础用法 ==========
# 一行搞定 — 伪装成 Chrome 136 的 TLS 指纹
resp = requests.get(
    'https://target.com',
    impersonate='chrome136',           # 核心：模仿浏览器 TLS 指纹
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    },
    timeout=30,
)
print(resp.status_code)               # 200 而不是 403


# ========== Session 保持 ==========
session = requests.Session(impersonate='chrome136')
session.get('https://target.com/login')
session.post('https://target.com/login', data={'user': '...'})
# 后续请求自动带 Cookie


# ========== 进阶配置（高防站）==========
from curl_cffi import CurlOpt

session = requests.Session(
    impersonate='chrome136',
    default_headers=True,              # 自动生成浏览器级 Headers
    timeout=30,
    extra_fp={
        'tls_permute_extensions': True,   # 随机化 TLS Extension 顺序
        'tls_grease': True,               # GREASE — 注入假扩展迷惑检测
        'tls_cert_compression': 'brotli',  # Brotli 证书压缩
        'tls_signature_algorithms': [     # 签名算法顺序（和真实 Chrome 一致）
            'ecdsa_secp256r1_sha256',
            'rsa_pss_rsae_sha256',
            'rsa_pkcs1_sha256',
            'ecdsa_secp384r1_sha384',
            'rsa_pss_rsae_sha384',
            'rsa_pkcs1_sha384',
        ],
    },
    curl_options={
        CurlOpt.TCP_KEEPALIVE: 1,
        CurlOpt.TCP_KEEPIDLE: 60,
        CurlOpt.TCP_KEEPINTVL: 30,
    },
)

resp = session.get('https://target.com')
```

### 2.3 curl_cffi async（并发提速）

```python
from curl_cffi.requests import AsyncSession
import asyncio

async def fetch_all(urls):
    async with AsyncSession(impersonate='chrome136') as s:
        tasks = [s.get(url) for url in urls]
        return await asyncio.gather(*tasks)

results = asyncio.run(fetch_all([
    'https://target.com/page=1',
    'https://target.com/page=2',
    'https://target.com/page=3',
]))
```

### 2.4 可用 impersonate 版本

```python
# 2026 年仍有效的 Chrome 指纹
'chrome136'  # 最新
'chrome131'  # 稳定
'chrome124'  # 广泛兼容
'chrome120'  # 最低保守选择

# 其他浏览器
'firefox133'
'edge131'
'safari18_0'
```

### 2.5 TLS-Chameleon（需要更多控制时）

```bash
pip install tls-chameleon
```

```python
from tls_chameleon import TLSChameleon

tc = TLSChameleon(profile='chrome_136')

# 自动检测目标站的反爬类型并选择剖面
resp = tc.get('https://target.com')
# WAF Shield 功能：自动识别 CF/Akamai/DataDome 并匹配最佳指纹

# AI Domain Memory：学习每个域名的最佳剖面
resp = tc.get('https://target.com', use_memory=True)
```

### 2.6 HTTP Header 顺序

Cloudflare 和 DataDome 都会检查 Header 顺序。`curl_cffi` 的 `default_headers=True` 已自动处理，但如果手动设置要注意：

```python
# ❌ Python dict 无序（3.6 之前）/ 或顺序不对
headers = {
    'Cookie': '...',
    'User-Agent': '...',
    'Accept': '...',
}

# ✅ 使用 Session.headers 保持正确顺序
session = requests.Session()
session.headers.update({
    'sec-ch-ua': '"Chromium";v="136"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 ...',
    'accept': 'text/html,...',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
})
```

---

## Layer 3: 浏览器 JS 指纹

### 3.1 检测对象 — 浏览器指纹全景

```
检测信号                         公开属性
──────────────────────────────────────────
navigator.webdriver              ← 一键暴露（自动化标记）
navigator.plugins.length         ← 真实浏览器有插件，headless 为 0
navigator.hardwareConcurrency    ← 太整数的值可疑
screen.colorDepth / resolution   ← 与 UA 不匹配会扣分
Canvas 指纹 (toDataURL)          ← 相同 GPU/OS 产生相同哈希
WebGL 指纹 (RENDERER)            ← 暴露 GPU 型号和驱动
AudioContext 指纹                ← 音频硬件特征
字体列表                         ← 缺失常见字体触发检测
window.chrome                    ← headless 下不存在的对象
Permissions API                  ← headless 下状态异常
```

### 3.2 Camoufox — C++ 级指纹伪造（⭐ 浏览器层首推）

```bash
pip install camoufox playwright
playwright install chromium    # Camoufox 需要 Playwright 作为基础
```

```python
from camoufox import Camoufox
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 一键创建防检测浏览器
    browser = Camoufox(
        p,
        # headless=False,             # 有头模式
        headless=True,                # 也支持无头（比 Playwright 原生 headless 更安全）
        geoip=True,                   # 自动匹配时区/语言到代理 IP 位置
        humanize=True,                # 随机化鼠标移动、滚动、打字速度
        screen={
            'width': 1920,            # 和代理 IP 所在的常见分辨率一致
            'height': 1080,
        },
    )
    page = browser.new_page()
    page.goto('https://target.com')
    
    # 验证隐蔽性
    leaks = page.evaluate("""() => {
        return {
            webdriver: navigator.webdriver,
            plugins: navigator.plugins.length,
            chrome: !!window.chrome,
        };
    }""")
    print(leaks)  # {webdriver: false, plugins: 5, chrome: true}
```

**Camoufox 本质**：基于 Firefox 定制编译（Firefox 市场占有率 ~3%，反爬系统对它的检测投入远小于 Chromium），C++ 级别修补了 `navigator.webdriver`、Canvas、WebGL、AudioContext 等检测点，**在 JS 执行之前就已完成指纹伪装**。

### 3.3 Patchright — Playwright 原生 API 的防检测补丁

```bash
pip install patchright
patchright install chromium
```

```python
# API 和 Playwright 几乎一样！
from patchright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://target.com')
    # 之后所有操作和 Playwright 一模一样
```

**优势**：如果你已经会用 Playwright，代码零改动，只换 import。
**定位**：修补 CDP 协议层痕迹（`Runtime.enable` 时序、执行上下文泄漏等）。

### 3.4 undetected-chromedriver（传统选择，Selenium 用户）

```bash
pip install undetected-chromedriver
```

```python
import undetected_chromedriver as uc

driver = uc.Chrome(headless=False)    # 自动下载匹配的 Chrome 并打补丁
driver.get('https://target.com')
```

**适用**：已有 Selenium 脚本，需要快速加防检测。
**劣势**：2026 年维护频率下降，新版 Chrome 可能滞后。

### 3.5 浏览器层如何选

| 场景 | 推荐 | 理由 |
|------|------|------|
| 已有 Playwright 代码 | **Patchright** | 零改动，只换 import |
| 新建项目 | **Camoufox** | C++ 级隐蔽，Firefox 基数低 |
| 已有 Selenium 代码 | **undetected-chromedriver** | 最快迁移 |
| 极致隐蔽需求 | **Camoufox + Patchright** 组合 | 协议层 + C++ 层双保险 |

---

## Layer 4: 行为分析

### 4.1 检测信号

```
行为信号                        被检测到的表现
────────────────────────────────────────────
页面加载后立即操作              机器人典型：没有"阅读时间"
恒定速度滚动                    鼠标滚轮事件间隔完全一致
直线鼠标移动                    人类不可能画出完美直线
始终精确点击同一位置            点击坐标标准差为零
从不误触/miss click             正常用户误触率 5-15%
标签页始终活跃                  visibilitychange 事件从不触发
固定间隔翻页                    精确 2.000s 翻页 = 机器人
```

### 4.2 行为拟人化 — Camoufox 内置方案

```python
from camoufox import Camoufox

browser = Camoufox(
    p,
    humanize=True,              # 核心开关
    # 内部自动：
    #   - 鼠标移动用 Bezier 曲线
    #   - 打字速度随机分布（120-300ms/字符）
    #   - 滚动间隔高斯扰动
    #   - 页面停留观察（先扫再操作）
)
```

### 4.3 行为拟人化 — 手动精细控制

```python
import random
from playwright.sync_api import sync_playwright

# Bezier 曲线鼠标移动
def human_click(page, selector):
    """模拟人类点击：先移动视线、再移动鼠标、再点击"""
    el = page.locator(selector)
    box = el.bounding_box()
    if not box:
        return
    
    # 目标位置加随机偏移（人类不会点正中心）
    target_x = box['x'] + box['width'] * 0.5 + random.gauss(0, 3)
    target_y = box['y'] + box['height'] * 0.5 + random.gauss(0, 3)
    
    # 分两步：先大致移到附近（快），再微调（慢）——人的习惯
    page.mouse.move(
        box['x'] + box['width'] * 0.3,
        box['y'] + box['height'] * 0.3,
    )
    page.wait_for_timeout(random.randint(150, 400))
    page.mouse.move(target_x, target_y)
    page.wait_for_timeout(random.randint(50, 200))
    page.mouse.click(target_x, target_y)

# 拟人打字
def human_type(page, selector, text):
    el = page.locator(selector)
    el.click()
    for char in text:
        page.keyboard.type(char, delay=random.randint(80, 280))
        if random.random() < 0.05:          # 5% 概率打错并删除
            wrong = chr(ord(char) + 1)
            page.keyboard.type(wrong, delay=50)
            page.keyboard.press('Backspace')
            page.keyboard.type(char, delay=150)

# 拟人滚动
def human_scroll(page):
    for _ in range(random.randint(3, 8)):
        distance = random.randint(200, 600)
        steps = random.randint(5, 15)
        for i in range(steps):
            step = distance / steps + random.gauss(0, 5)
            page.mouse.wheel(0, step)
            page.wait_for_timeout(random.randint(10, 40))
        page.wait_for_timeout(random.randint(800, 3000))  # 假装在看内容

# 随机化的翻页间隔
def inter_page_delay():
    """模拟翻页之间的'人行为'"""
    # 高斯分布中心 5 秒，标准差 1.5 秒
    base = random.gauss(5, 1.5)
    # 10% 概率长间隔（去喝水/看别的）
    if random.random() < 0.1:
        base += random.randint(15, 45)
    time.sleep(max(2, base))
```

### 4.4 session 预热

```python
def warm_session(page):
    """让浏览器 session 看起来像真实用户"""
    page.goto('https://target.com')
    page.wait_for_timeout(random.randint(2000, 5000))
    
    # 随便滚动几下
    for _ in range(random.randint(2, 4)):
        page.mouse.wheel(0, random.randint(300, 800))
        page.wait_for_timeout(random.randint(500, 2000))
    
    # 随机悬停几个链接（表示在"浏览"）
    links = page.locator('a').all()
    for _ in range(random.randint(3, 7)):
        if links:
            random.choice(links).hover()
            page.wait_for_timeout(random.randint(300, 1500))
    
    # 然后再去目标列表页
    page.goto('https://target.com/list')
    page.wait_for_timeout(random.randint(1500, 3500))
```

---

## 实战：四层全开的完整抓取脚本

```python
"""
完整反爬栈：curl_cffi (Layer2) + Camoufox (Layer3) + 住宅代理 (Layer1) + 拟人行为 (Layer4)
按目标站防护级别选择组合：
  - 弱防护：只用 curl_cffi
  - 中等防护：curl_cffi + 住宅代理
  - 强防护：Camoufox/Patchright + 住宅代理 + 行为拟人
"""

import random
import time
import json
from camoufox import Camoufox
from playwright.sync_api import sync_playwright

PROXY = {
    'server': 'http://residential-proxy.example.com:8080',
    'username': 'your_user',
    'password': 'your_pass',
}

def slow_scroll(page):
    """随机慢速滚动，模拟浏览"""
    for _ in range(random.randint(3, 6)):
        page.mouse.wheel(0, random.randint(200, 500))
        time.sleep(random.uniform(0.5, 2.0))

with sync_playwright() as p:
    browser = Camoufox(
        p,
        headless=False,
        geoip=True,                     # 自动匹配代理 IP 的地理信息
        humanize=True,                  # 鼠标/键盘拟人化
        proxy=PROXY,
    )
    
    page = browser.new_page()
    all_data = []
    
    for page_num in range(1, 4):
        print(f'Fetching page {page_num}...')
        
        # 首次加载 + session 预热
        if page_num == 1:
            page.goto('https://target.com', wait_until='domcontentloaded')
            page.wait_for_timeout(random.randint(8000, 15000))  # 等 CF JS Challenge
        
        page.goto(
            f'https://target.com/list?page={page_num}',
            wait_until='domcontentloaded',
        )
        
        # 随机等待（模拟人看到新页面后的反应时间）
        page.wait_for_timeout(random.randint(3000, 8000))
        
        # 随机滚动
        slow_scroll(page)
        
        # 你的核心技能：JS eval 一步提取
        items = page.evaluate("""() => {
            const els = [...document.querySelectorAll('.gallery-item')];
            return els.map(el => {
                const a = el.querySelector('a[href]') || el.querySelector('a');
                return {
                    title: a?.getAttribute('title')?.trim() || a?.textContent?.trim() || '',
                    url: a?.href || '',
                };
            }).filter(x => x.url);
        }""")
        
        all_data.extend(items)
        print(f'  Page {page_num}: {len(items)} items')
    
    browser.close()

# 保存结果
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f'Done! Total: {len(all_data)} items')
```

---

## 各防护级别的对应策略速查

### Cloudflare

| 防护模式 | 表现 | 方案 |
|---------|------|------|
| 无防护（DNS only） | 正常访问 | `requests` 即可 |
| Free / 基本 JS Challenge | "Checking your browser..." 5秒跳转 | `curl_cffi` 足矣 |
| Pro / Managed Challenge | 每次页面都 Challenge | `curl_cffi` + 住宅代理 或 Camoufox |
| Business / Turnstile | 人机验证复选框 | Camoufox + 住宅代理 |
| Enterprise / Bot Fight Mode | 频繁 403/1020 无规律 | 住宅代理 + Camoufox + 行为拟人 + 低频 |

### DataDome

| 表现 | 方案 |
|------|------|
| 首次请求直接 403 | `curl_cffi` + 住宅代理 |
| 弹出 DataDome 拦截页 | Camoufox + 移动代理 |
| 滑块验证 | Camoufox + 2Captcha/CapSolver |
| 随机拦截+shadow ban | 移动代理 + Camoufox + 极端低频 |

### Akamai

| 表现 | 方案 |
|------|------|
| 无感拦截 | `tls-client`（Go SDK）+ 正确 Header 顺序 |
| sensor_data 数据收集 | `curl_cffi` + 住宅代理 |
| 行为分析拒绝 | Camoufox + 住宅代理 + session 预热 |

---

## 决策树

```
目标站返回什么？
    │
    ├─ 200 OK，数据在 HTML 里
    │   → requests + BeautifulSoup（不需要反爬）
    │
    ├─ 200 OK，但数据由 JS 渲染
    │   → Playwright / opencli（不需要反爬，需要 JS 渲染）
    │
    ├─ 403 / 1020 / 空白页，无任何 Challenge
    │   → curl_cffi（TLS 指纹问题）
    │   → 还不行 → + 住宅代理（IP 信誉问题）
    │
    ├─ "Checking your browser..." 或 Turnstile
    │   → Camoufox / Patchright（浏览器指纹问题）
    │   → 还不行 → + 住宅代理 + humanize
    │
    ├─ DataDome 拦截页 / 滑块
    │   → Camoufox + 移动代理 + 低频请求
    │   → 还不行 → 考虑使用专业 API 服务
    │
    └─ 反复被拦 / shadow ban（数据越来越空）
        → 降低频率、增加 session 预热、换 IP
        → 还不行 → 评估是否值得继续（有些站就是不想被爬）
```

---

## 与已有技能的对接

- 本文是 [Python爬虫学习路径](Python爬虫学习路径-从已有经验映射.md) 的 **Layer 2-4 深度展开**
- 最终提取代码仍然是你擅长的 `page.evaluate("""() => { ... }""")` — 只是外层加了防检测
- CF 穿透三板斧（[浏览器自动化抓取-技能笔记](浏览器自动化抓取-技能笔记.md) 模式三）的 Python 化实现
