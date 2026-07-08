---
title: Selenium 进阶 — 交互操作、翻页与无头模式
domain: IT_Technology
tags:
  - Python
  - 爬虫
  - Selenium
  - 自动化
status: 草稿
created: 2026-06-14
updated: 2026-06-14
source: 尚硅谷大模型技术之Python V1.0
related:
  - "[[01-概念、原理与基本使用]]"
  - "[[02-元素定位与数据提取]]"
  - "[[Python-MOC]]"
summary: Selenium 进阶技巧——click 点击、send_keys 输入、execute_script 滚动、翻页 while True 模式、无头模式、弹窗处理与 Cookie 管理，附完整翻页爬虫实战
---

# Selenium 进阶 — 交互操作、翻页与无头模式

## 一句话结论

> `click()` 点击、`send_keys()` 输入、`execute_script()` 执行 JS 是 Selenium 三大交互核心；配合 `while True` + 点击下一页 + `try/except` 判断终止，构成通用翻页爬虫模式；`headless` 无头模式提效 30%。

---

## 一、click() — 点击

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 定位搜索按钮并点击
search_btn = driver.find_element(By.ID, 'su')
search_btn.click()
```

### 点击失败的常见原因与解决方案

| 问题 | 原因 | 解决 |
|------|------|------|
| `ElementNotInteractableException` | 元素被遮挡或不可见 | 先滚动到元素位置 |
| `ElementClickInterceptedException` | 被另一个元素挡住（如弹窗）| 关闭遮挡元素，或 JS 直接点击 |
| 点击没反应 | 元素存在但点击事件未绑定 | 用 `execute_script` 强制触发 |

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 方案 1：滚动到元素再点击
el = driver.find_element(By.ID, 'btn')
driver.execute_script('arguments[0].scrollIntoView()', el)
el.click()

# 方案 2：ActionChains 模拟真实用户点击
ActionChains(driver).move_to_element(el).click().perform()

# 方案 3：JS 直接触发（绕过一切遮挡）
driver.execute_script('arguments[0].click()', el)
```

---

## 二、send_keys() — 输入

```python
input_box = driver.find_element(By.ID, 'kw')

# 输入文本
input_box.send_keys('Python 爬虫')

# 输入前先清空
input_box.clear()
input_box.send_keys('Selenium')

# 逐字输入（模拟真人）
import time
for char in 'Selenium':
    input_box.send_keys(char)
    time.sleep(0.1)

# 输入特殊键
from selenium.webdriver.common.keys import Keys
input_box.send_keys('hello')
input_box.send_keys(Keys.ENTER)        # 回车
input_box.send_keys(Keys.CONTROL, 'a') # Ctrl+A 全选
input_box.send_keys(Keys.BACKSPACE)    # 退格
```

---

## 三、execute_script() — 执行 JavaScript

这是 Selenium 最强大的方法——绕过前端限制直接操控页面：

```python
# ====== 滚动操作（爬虫最高频使用）======

# 滚动到底部（无限参数——一把拉到底）
driver.execute_script('window.scrollTo(0, 1000000)')

# 滚动到指定元素
el = driver.find_element(By.ID, 'target')
driver.execute_script('arguments[0].scrollIntoView()', el)

# 滚动到指定位置
driver.execute_script('window.scrollTo(0, 500)')   # 向下滚 500px

# 平滑滚动（触发懒加载）
driver.execute_script('window.scrollBy(0, 1000)')

# ====== 修改页面元素 ======

# 修改属性
driver.execute_script("document.querySelector('#input').value = 'DrissionPage'")

# 移除元素（如删除遮挡的广告弹窗）
driver.execute_script("document.querySelector('.ad-modal').remove()")

# 修改样式
driver.execute_script("document.querySelector('#box').style.display = 'block'")

# ====== 获取页面数据 ======

# 获取变量
title = driver.execute_script('return document.title')

# 获取元素位置信息
rect = driver.execute_script('return arguments[0].getBoundingClientRect()', el)
print(f'元素位置: {rect}')
```

### 为什么 execute_script 能解决 click 失败

材料中的经典案例：翻页按钮定位成功但 `click()` 无效：

```python
# ❌ click() 失败——元素被遮挡或不在可视区
next_btn = driver.find_element(By.XPATH, '//a[contains(text(), "下一页")]')
next_btn.click()   # 可能报错或无效

# ✅ 先滚动确保可见，再点击
driver.execute_script('window.scrollTo(0, 1000000)')    # 拉到底
next_btn = driver.find_element(By.XPATH, '//a[contains(text(), "下一页")]')
next_btn.click()                                         # 现在能点到了
```

---

## 四、通用翻页模式（while True + try/except）

这是材料中讲解的核心翻页逻辑——适用于绝大多数分页网站：

### 4.1 模式结构

```python
while True:
    # 1. 提取当前页数据
    items = driver.find_elements(By.CLASS_NAME, 'item')
    for item in items:
        data = item.find_element(By.TAG_NAME, 'h3').text
        all_data.append(data)

    # 2. 尝试点击下一页
    try:
        # 滚动到页面底部（确保按钮可见可点）
        driver.execute_script('window.scrollTo(0, 1000000)')

        # 定位下一页按钮
        next_btn = driver.find_element(By.XPATH, '//a[contains(text(), "下一页")]')
        next_btn.click()

        # 等待新页面加载
        import time
        time.sleep(2)

    except Exception:
        # 找不到或点不了下一页 → 终止循环
        print('已到最后一页')
        break
```

### 4.2 翻页模式关键点

| 环节 | 要点 |
|------|------|
| 数据提取 | 每页循环内提取 → 追加到总列表 |
| 翻页点击 | `try/except` 包裹——找不到"下一页"按钮时跳出 |
| 滚动 | **先滚后点**——避免按钮被遮挡或不在视口 |
| 等待 | `sleep(2)` 确保新页加载完成后再提取数据 |
| 终止条件 | `NoSuchElementException` → 最后一页 |

### 4.3 判断是否最后一页的三种方式

```python
# 方式一：找「下一页」按钮（材料推荐）
next_btn = driver.find_elements(By.XPATH, '//a[contains(text(), "下一页")]')
if not next_btn:
    break

# 方式二：检查「下一页」按钮是否有 disabled 属性
next_btn = driver.find_element(By.CLASS_NAME, 'next')
if 'disabled' in next_btn.get_attribute('class'):
    break

# 方式三：对比当前页码和总页码
current = int(driver.find_element(By.CLASS_NAME, 'current').text)
total = int(driver.find_element(By.CLASS_NAME, 'total').text)
if current >= total:
    break
```

---

## 五、完整翻页爬虫实战

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PageSpider:
    """通用翻页爬虫模板"""

    def __init__(self, url, headless=False):
        """初始化浏览器"""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.url = url
        self.data = []

    def parse_items(self):
        """提取当前页数据——子类按实际页面结构重写"""
        items = self.driver.find_elements(By.CLASS_NAME, 'item')
        page_data = []
        for item in items:
            title = item.find_element(By.TAG_NAME, 'h3').text
            page_data.append({'标题': title})
        return page_data

    def go_next_page(self):
        """翻到下一页——返回 True 成功，False 已到最后一页"""
        try:
            # 滚动确保按钮可见
            self.driver.execute_script('window.scrollTo(0, 1000000)')
            time.sleep(0.5)

            # 找下一页按钮
            next_btn = self.driver.find_element(
                By.XPATH, '//a[contains(text(), "下一页")]'
            )
            next_btn.click()
            time.sleep(2)   # 等新页加载
            return True
        except Exception:
            return False

    def run(self, max_pages=5):
        """主流程"""
        self.driver.get(self.url)
        page = 1

        while True:
            print(f'第 {page} 页')
            page_data = self.parse_items()
            self.data.extend(page_data)
            print(f'  本页 {len(page_data)} 条，累计 {len(self.data)} 条')

            if page >= max_pages:
                print(f'达到最大页数 {max_pages}，停止')
                break

            if not self.go_next_page():
                print('已到最后一页，停止')
                break

            page += 1

        self.driver.quit()
        return self.data


# 使用
spider = PageSpider('https://example.com/list', headless=True)
all_data = spider.run(max_pages=3)
print(f'\n共 {len(all_data)} 条数据')
for d in all_data[:5]:
    print(f"  {d['标题']}")
```

---

## 六、无头模式（Headless）

无头模式 = 不显示浏览器窗口，在后台运行——省资源、速度快：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')            # 无头模式
options.add_argument('--disable-gpu')         # 禁用 GPU（Windows 下建议加）
options.add_argument('--window-size=1920,1080')  # 设置窗口大小（无头下必须设）
options.add_argument('--no-sandbox')          # 沙箱模式（Linux 下常用）

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')

# 正常操作——和普通模式完全一致
print(driver.title)
driver.quit()
```

| 模式 | 速度 | 可见性 | 适用场景 |
|------|------|--------|---------|
| 普通模式 | 基准 | 可见窗口 | 开发调试 |
| 无头模式 | 快 ~30% | 不可见 | 正式爬取 |

> 调试阶段用普通模式看效果，确认无误后切无头模式跑大批量。

---

## 七、弹窗处理

```python
# Alert 弹窗（JavaScript alert/confirm/prompt）
alert = driver.switch_to.alert
print(alert.text)               # 弹窗文本
alert.accept()                  # 点击确定
alert.dismiss()                 # 点击取消
alert.send_keys('输入内容')      # prompt 型弹窗输入

# 切换到 iframe
driver.switch_to.frame('iframe_id')      # 按 id/name
driver.switch_to.frame(0)                # 按 index（第一个 iframe）
driver.switch_to.default_content()       # 切回主页面

# 窗口切换
main_window = driver.current_window_handle
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])  # 切到新窗口
driver.close()                           # 关当前窗口
driver.switch_to.window(main_window)     # 回到主窗口
```

---

## 八、Cookie 操作

```python
# 获取所有 Cookie
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']} = {c['value']}")

# 获取单个 Cookie
token = driver.get_cookie('token')

# 添加 Cookie
driver.add_cookie({'name': 'token', 'value': 'abc123'})

# 删除 Cookie
driver.delete_cookie('token')
driver.delete_all_cookies()
```

> Cookie 操作通常在 `driver.get(url)` **之后**生效——打开目标域名再添加 Cookie。

---

## 常用操作速查

| 需求 | 代码 |
|------|------|
| 点击 | `el.click()` |
| 输入 | `el.send_keys('text')` |
| 清空 | `el.clear()` |
| 回车 | `el.send_keys(Keys.ENTER)` |
| 滚动到底 | `driver.execute_script('window.scrollTo(0, 1000000)')` |
| 滚动到元素 | `driver.execute_script('arguments[0].scrollIntoView()', el)` |
| JS 点击 | `driver.execute_script('arguments[0].click()', el)` |
| 无头模式 | `options.add_argument('--headless')` |
| 下一页 | `driver.find_element(By.XPATH, '//a[contains(text(), "下一页")]')` |
| 翻页终止 | `try/except` 捕获 `NoSuchElementException` |
| Cookie | `driver.get_cookie('name')` / `driver.add_cookie({...})` |

## 关键概念

- **click 失败三件套**：滚动 → ActionChains → JS 点击，逐级升级
- **翻页三要素**：while True + try/except + 滚动确保可见
- **execute_script**：Selenium 的后门——绕过一切前端限制直接操作 DOM
- **无头模式**：不显示浏览器窗口，开发用普通模式，生产切无头
- **翻页等待**：点击下一页后必须 `sleep()` 或显式等待，否则数据还在旧页面

## 可行动建议

- click 失败不要第一时间纠结——先试试滚动到元素 + 再 click
- send_keys 前要先 `clear()`，避免内容叠加
- 翻页必须先滚到底再点下一页——材料和实战都验证了这个套路
- 调试阶段用普通模式（能看到浏览器操作过程），确认无误再切 `headless`
- `execute_script` 是最终解决方案——click/send_keys 都无效时用它

## 延伸与关联

- [[02-元素定位与数据提取]] — 元素定位（8 种方式）+ 数据提取 + 等待机制
- [[01-概念、原理与基本使用]] — Selenium 基本概念、安装配置、选型定位
- [[DrissionPage 使用技巧]] — DrissionPage 的翻页、等待、iframe 处理——API 更简洁
- [[Python-MOC]] — Python 知识体系总导航
