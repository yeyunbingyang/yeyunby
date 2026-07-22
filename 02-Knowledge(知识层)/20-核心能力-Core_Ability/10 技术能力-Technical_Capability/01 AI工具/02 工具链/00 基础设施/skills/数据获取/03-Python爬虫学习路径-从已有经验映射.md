---
title: Python爬虫学习路径
domain: Core_Ability
tags: [Python, 爬虫, 学习路径, 经验映射]
status: 稳定
created: 2026-06-19
updated: 2026-07-22
summary: "Python 爬虫学习路径——从PowerShell/JS/CLI经验映射到Python等价写法的完整指南"
---

# Python 爬虫学习路径

> 从 PowerShell/JS/CLI 经验映射到 Python 等价写法
> 更新时间：2026-06-19

---

## 0. 你的现有技能 → Python 映射

| 你已有的能力 | 技术 | Python 等价 |
|-------------|------|------------|
| `opencli eval "..."` | JS 在页面执行 | `page.evaluate("""...""")` — 完全一样 |
| `[regex]::Matches($yaml, $pattern)` | 正则提取 | `re.findall(pattern, text)` |
| `ConvertTo-Json -Depth 3` | JSON 输出 | `json.dumps(data, ensure_ascii=False, indent=2)` |
| `HashSet[string]` 去重 | 集合去重 | `set()` / `{item for item in ...}` |
| `Out-File -Encoding UTF8` | 写入文件 | `open(path, 'w', encoding='utf-8').write()` |
| `New-Item -Directory` | 创建目录 | `os.makedirs(name, exist_ok=True)` |
| `--headed` + `sleep 15` | CF 穿透 | `headless=False` + `page.wait_for_timeout(15000)` |
| `snapshot` → 正则 | 快照提取 | Playwright locator / BS4 / regex |

**你的核心思维已经到位**：
- IIFE 包裹避免变量污染 ✓
- CSS 选择器 > XPath ✓
- 有头模式等 CF 自动完成 ✓
- 翻页后重新获取引用 ✓

缺的只是 Python 语法和生态工具的熟练度。

---

## 第一层：HTTP 基础（requests + BeautifulSoup）

### 1.1 纯 HTTP 获取 + 解析

这是爬虫最基本的"请求→解析→提取"循环。**不启动浏览器**。

```python
import requests
from bs4 import BeautifulSoup
import json

# === 发请求 ===
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://target.com',
}
resp = requests.get('https://target.com/list?page=1', headers=headers, timeout=30)
resp.encoding = 'utf-8'

# === 解析 ===
soup = BeautifulSoup(resp.text, 'html.parser')

# === 提取 ===
data = []
for item in soup.select('.gallery-item'):        # CSS 选择器 — 和 querySelectorAll 一样
    a = item.select_one('a[href]')               # 和 el.querySelector('a[href]') 一样
    if not a:
        continue
    data.append({
        'title': a.get('title', '').strip() or a.get_text(strip=True),
        'url': a['href'],
    })

# === 输出 ===
print(json.dumps({'count': len(data), 'data': data}, ensure_ascii=False, indent=2))
```

**与你已有 JS 的对比**：
```js
// 你的 opencli eval 写法
const els = [...document.querySelectorAll('.gallery-item')];
return JSON.stringify({
    count: els.length,
    data: els.map((el, i) => {
        const a = el.querySelector('a[href]');
        return { title: a?.textContent.trim(), url: a?.href };
    })
});
```
```python
# Python 等价
items = soup.select('.gallery-item')
data = []
for el in items:
    a = el.select_one('a[href]')
    if a:
        data.append({'title': a.get_text(strip=True), 'url': a['href']})
```

### 1.2 翻页模式

```python
def fetch_page(page_num):
    resp = requests.get(f'https://target.com/list?page={page_num}', headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    return [extract_item(el) for el in soup.select('.item')]

all_data = []
for page in range(1, 28):          # 用 range 替代 PowerShell 的 for 循环
    print(f'Fetching page {page}...')
    all_data.extend(fetch_page(page))
    import time
    time.sleep(2)                   # 礼貌间隔
```

### 1.3 HTTP 层的局限

- **不执行 JS**：SPA 页面（React/Vue 渲染）拿不到数据
- **容易被拦**：Cloudflare/DataDome 会在 HTTP 层直接返回 403/Challenge 页面
- **Cookie 管理**：需要手动维护 session

**何时用**：后端渲染的传统页面（HTML 里直接有数据）、API 接口。

---

## 第二层：反爬对抗（httpx + 会话管理）

### 2.1 Session 保持

```python
import httpx

with httpx.Client(
    headers={'User-Agent': '...'},
    follow_redirects=True,
    timeout=30,
) as client:
    # Session 自动保持 Cookie
    client.get('https://target.com/login')
    client.post('https://target.com/login', data={'user': '...', 'pass': '...'})
    # 后续请求自动带登录态
    resp = client.get('https://target.com/members-only')
```

### 2.2 异步并发（提速核心）

```python
import httpx
import asyncio

async def fetch(client, page):
    resp = await client.get(f'https://target.com/list?page={page}')
    return resp.text

async def main():
    async with httpx.AsyncClient() as client:
        # 同时请求 10 页 — 等价于 PowerShell 的 Start-Job 并发
        tasks = [fetch(client, p) for p in range(1, 11)]
        pages = await asyncio.gather(*tasks)  # 10 个请求并发等待
    return pages

asyncio.run(main())
```

### 2.3 lxml — 比 BeautifulSoup 快 5-10 倍

```python
from lxml import html

tree = html.fromstring(resp.text)
titles = tree.xpath('//a[contains(@href, "/detail/")]/text()')  # XPath
urls = tree.xpath('//a[contains(@href, "/detail/")]/@href')
```

**选择决策**：
| 场景 | 推荐 |
|------|------|
| 小规模（<100页） | BeautifulSoup + requests |
| 中规模（100-1000页） | lxml + httpx async |
| 大规模（>1000页） | Scrapy 框架 |

---

## 第三层：浏览器自动化（Playwright Python API）

### 3.1 你的 opencli 工作流 → Playwright 直译

这是你最熟悉的模式，Python 写法几乎原样照搬。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)   # = --headed
    page = browser.new_page()
    
    # === 打开页面 ===
    # opencli: opencli browser sess open "https://target.com"
    page.goto('https://target.com/list?page=1')
    
    # === 等待 CF 验证完成 ===
    # PowerShell: sleep 15
    page.wait_for_timeout(15000)
    
    # === 你的核心技能：JS eval 一步提取 ===
    # opencli: opencli browser sess eval "(function(){...})()"
    data = page.evaluate("""() => {
        const els = [...document.querySelectorAll('.gallery-item')];
        return els.map((el, i) => ({
            id: i + 1,
            title: el.querySelector('a')?.getAttribute('title')?.trim() || '',
            url: el.querySelector('a')?.href || '',
        }));
    }""")
    # data 已经是 Python list[dict]
    
    print(len(data))  # 80
    
    # === 点击翻页 ===
    # opencli: opencli browser sess click <N>
    page.click('.pagination .next')                # 比 ref 索引更稳定
    page.wait_for_timeout(10000)                   # CF 可能重新验证
    
    # === 翻页后必须重新提取，ref 已过期 ===
    data2 = page.evaluate("""() => {
        return [...document.querySelectorAll('.gallery-item')].map(el => ({}));
    }""")
    
    browser.close()
```

### 3.2 不用 eval 也能提取（Playwright 原生定位器）

```python
# 方式1：Locator（推荐，自动等待）
items = page.locator('.gallery-item')
count = items.count()                    # = get count
for i in range(count):
    title = items.nth(i).locator('a').get_attribute('title')
    url = items.nth(i).locator('a').get_attribute('href')

# 方式2：evaluate_all（批量提取，最快）
data = page.locator('.gallery-item').evaluate_all("""
    els => els.map(el => {
        const a = el.querySelector('a[href]');
        return { title: a?.title?.trim() || '', url: a?.href || '' };
    })
""")

# 方式3：page.evaluate（你最熟悉的方式）
data = page.evaluate("""() => {
    return [...document.querySelectorAll('.gallery-item')].map(el => ({
        title: el.querySelector('a')?.title?.trim(),
        url: el.querySelector('a')?.href,
    }));
}""")
```

### 3.3 CF 穿透的 Python 写法

```python
def bypass_cf_and_fetch(page, url):
    """你已经掌握的 CF 穿透逻辑，Python 化"""
    page.goto(url, wait_until='domcontentloaded')
    
    # 等待 CF JS Challenge 完成
    # 信号：页面标题不再是 "Just a moment..."
    try:
        page.wait_for_function(
            "document.title !== 'Just a moment...'",
            timeout=30000
        )
    except:
        # 如果 30s 还没过，检查是否需要手动处理
        print('CF challenge taking long...')
        page.wait_for_timeout(20000)
    
    # 确认真正内容出现
    page.wait_for_selector('.gallery-item', timeout=15000)
    
    # 然后提取
    return page.evaluate("""() => {
        return [...document.querySelectorAll('.gallery-item')].map(el => ({
            title: el.querySelector('a')?.title?.trim(),
            url: el.querySelector('a')?.href,
        }));
    }""")
```

### 3.4 翻页完整示例

```python
all_data = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    for page_num in range(1, 4):    # 翻 3 页
        url = f'https://target.com/list?page={page_num}'
        print(f'Page {page_num}...')
        
        page.goto(url, wait_until='domcontentloaded')
        page.wait_for_timeout(15000)
        
        items = page.evaluate("""() => {
            return [...document.querySelectorAll('.item')].map(el => ({
                page: %d,
                title: el.querySelector('a')?.textContent?.trim() || '',
                url: el.querySelector('a')?.href || '',
            }));
        }""" % page_num)
        
        all_data.extend(items)
    
    browser.close()

print(f'Total: {len(all_data)} items')
```

---

## 第四层：数据后处理 — PowerShell → Python

### 4.1 正则提取

```powershell
# PowerShell
$pattern = '(?s)- link "([^"]+)" [ref=e\d+\] [cursor=pointer\]:\s+- /url: /target/\d+'
$matches = [regex]::Matches($content, $pattern)
```

```python
# Python
import re
pattern = r'- link "([^"]+)" \[ref=e\d+\] \[cursor=pointer\]:\s+- /url: /target/\d+'
matches = re.findall(pattern, content)      # 返回 list[str]
# 或带位置信息
for m in re.finditer(pattern, content):
    title = m.group(1)
    url = m.group(0)
```

### 4.2 JSON 读写

```powershell
# PowerShell
$items | ConvertTo-Json -Depth 3 | Out-File -FilePath $path -Encoding UTF8
$data = Get-Content $path -Raw | ConvertFrom-Json
```

```python
# Python
import json

# 写入（ensure_ascii=False 保留中文）
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

# 读取
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### 4.3 去重对比

```powershell
# PowerShell
$set = [System.Collections.Generic.HashSet[string]]::new()
foreach ($item in $sourceData) {
    $mainTitle = ($item.title -split '/')[0].Trim() -replace '[\\/:*?"<>|\[\]]', '' -replace '\s+', ''
    $set.Add($mainTitle.ToLower())
}
$newOnes = $otherData | Where-Object {
    $t = ($_.title -split '/')[0].Trim() -replace '[\\/:*?"<>|\[\]]', '' -replace '\s+', ''
    -not $set.Contains($t.ToLower())
}
```

```python
# Python
import re

def normalize(title):
    """标题标准化"""
    main = title.split('/')[0].strip()
    main = re.sub(r'[\\/:*?"<>|[\]\]]', '', main)
    main = re.sub(r'\s+', '', main)
    return main.lower()

# 构建集合
titles = {normalize(item['title']) for item in source_data}

# 差集
new_items = [
    item for item in other_data
    if normalize(item['title']) not in titles
]
```

### 4.4 批量创建文件夹

```powershell
# PowerShell
$num = 0
foreach ($item in $items) {
    $num++
    $name = ($item.title -split '/')[0].Trim() -replace '[\:*?"<>|]', '_'
    $folderName = "$($num.ToString('000')).$name"
    if ($folderName.Length -gt 240) { $folderName = $folderName.Substring(0, 240) }
    New-Item -ItemType Directory -Path "$targetDir\$folderName" -Force | Out-Null
}
```

```python
# Python
import os
import re

target_dir = r'F:\output'

for num, item in enumerate(items, 1):
    name = item['title'].split('/')[0].strip()
    name = re.sub(r'[\\:*?"<>|]', '_', name)      # 安全命名
    folder = f'{target_dir}/{num:03d}.{name}'      # :03d = 3位补零
    folder = folder[:240] if len(folder) > 240 else folder
    os.makedirs(folder, exist_ok=True)
```

---

## 第五层：规模化（Scrapy / Crawl4AI）

### 5.1 何时从 Playwright → Scrapy

| 信号 | 说明 |
|------|------|
| 页面数 > 50 | 单线程太慢 |
| 需要增量抓取 | 去重+续抓 |
| 需要多种输出 | JSON/CSV/数据库 |
| 需要错误重试 | 自动重试+日志 |

### 5.2 Scrapy 最小示例

```python
# items.py
import scrapy

class ComicItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()

# spiders/list_spider.py
class ListSpider(scrapy.Spider):
    name = 'list'
    start_urls = ['https://target.com/list?page=1']
    
    def parse(self, response):
        for item in response.css('.gallery-item'):
            yield ComicItem(
                title=item.css('a::attr(title)').get('').strip(),
                url=item.css('a::attr(href)').get(''),
            )
        
        # 自动翻页
        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

# 运行
# scrapy runspider list_spider.py -o output.json
```

### 5.3 Crawl4AI — 适合你风格的选择

```python
# 你的 eval 思维 + Crawl4AI 的异步能力
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
import json

async def main():
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            # 用你熟悉的 JS 提取逻辑
            js_code="""
                return [...document.querySelectorAll('.gallery-item')].map(el => ({
                    title: el.querySelector('a')?.title?.trim(),
                    url: el.querySelector('a')?.href,
                }));
            """,
            # 等待 JS 渲染完成
            wait_for="js:() => document.querySelectorAll('.gallery-item').length > 0",
        )
        
        result = await crawler.arun(
            url='https://target.com/list',
            config=config,
        )
        
        # result.extracted_content 就是你的 JS 返回值
        data = json.loads(result.extracted_content)
        print(f'Found {len(data)} items')

asyncio.run(main())
```

---

## 学习节奏建议

```
Week 1-2: requests + BeautifulSoup
  → 搞定静态页面，能写出完整的"请求→解析→存文件"脚本

Week 3: Playwright Python API  
  → 把你现有的 opencli eval 技能平移过来，感受差异

Week 4: 数据后处理
  → JSON 读写、正则、去重、文件命名，把 PowerShell 脚本翻译成 Python

Week 5: asyncio + httpx
  → 理解异步，把同步爬虫提速 5-10x

Week 6+: Scrapy 或 Crawl4AI
  → 按兴趣选一个深入
```

---

## 环境一键搭建

```bash
# 基础
pip install requests beautifulsoup4 lxml httpx

# 浏览器自动化
pip install playwright
playwright install chromium

# 数据
pip install parsel       # Scrapy 提取库，可独立使用
pip install jmespath     # JSON 查询语言

# 规模化
pip install scrapy       # 框架
pip install crawl4ai     # AI 爬虫

# 开发工具
pip install ipython      # 交互式调试
pip install rich         # 终端美化输出
```

---

## 与现有技能笔记的关系

- 本文是 [浏览器自动化抓取-技能笔记](浏览器自动化抓取-技能笔记.md) 的 **Python 语言实现补充**
- 5 种可复用爬虫模式全部有 Python 等价写法
- 工具链对比表中的 CLI 命令 → Python API 调用
