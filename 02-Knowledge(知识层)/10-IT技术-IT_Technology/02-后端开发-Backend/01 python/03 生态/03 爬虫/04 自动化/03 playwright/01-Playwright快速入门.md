---
title: Playwright 快速入门
domain: IT_Technology
tags:
  - Python
  - Playwright
  - 浏览器自动化
  - 爬虫
status: 稳定
created: 2026-08-10
updated: 2026-08-10
verified: 2026-08-10
review_after: 2026-11-10
source: "https://playwright.dev/python/docs/library"
related:
  - "[[Python-MOC]]"
summary: "Playwright 通过语义化 Locator、内置自动等待和浏览器上下文，为 Python 浏览器自动化提供稳定且可复现的页面操作能力"
---

# Playwright 快速入门

## 一句话结论

> Playwright 的稳定性主要来自“语义化定位 + 自动等待 + 明确断言”，常规操作应优先依赖 Locator 和 `expect`，不要用固定 `sleep()` 猜测页面何时就绪。

## 一、安装

建议先创建虚拟环境，再安装 Python 库和所需浏览器：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install playwright
python -m playwright install chromium
```

Linux 或 macOS 激活虚拟环境：

```bash
source .venv/bin/activate
```

> [!note]
> `pip install playwright` 安装 Python 包；`python -m playwright install chromium` 下载与当前 Playwright 版本匹配的 Chromium。需要 Firefox 或 WebKit 时，将 `chromium` 换成对应浏览器名，或省略浏览器名安装全部浏览器。

## 二、访问页面与关闭资源

同步 API 适合入门和简单脚本。用 `with sync_playwright()` 管理 Playwright 生命周期，并在结束时关闭浏览器：

```python
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    response = page.goto(
        "https://example.com",
        wait_until="domcontentloaded",
        timeout=30_000,
    )
    if response is not None and not response.ok:
        raise RuntimeError(
            f"页面访问失败：{response.status} {response.status_text}"
        )

    print(page.title())
    browser.close()
```

- `headless=True`：后台运行，适合脚本与 CI。
- 调试时可改为 `headless=False`，观察浏览器操作过程。
- `page.goto()` 默认会等待页面达到加载条件；`domcontentloaded` 通常比等待所有图片、广告资源更直接。

## 三、定位元素

Locator 会在每次操作前重新解析元素，并参与 Playwright 的自动等待。优先使用面向用户的稳定特征：

```python
# 按可访问角色与名称定位，通常是首选
heading = page.get_by_role("heading", name="Example Domain")

# 表单控件常用标签、占位符定位
username = page.get_by_label("用户名")
search_box = page.get_by_placeholder("搜索")

# 页面正文或测试契约
message = page.get_by_text("操作成功")
save_button = page.get_by_test_id("save-button")

# 必要时才退回 CSS
main_content = page.locator("main.content")
```

推荐顺序：

1. `get_by_role()`：模拟用户和辅助技术理解页面的方式。
2. `get_by_label()`、`get_by_placeholder()`、`get_by_text()`：表达业务含义。
3. `get_by_test_id()`：由应用提供稳定测试契约。
4. CSS 或 XPath：适合无语义标记的页面，但更容易受 DOM 重构影响。

> [!warning]
> Locator 默认严格匹配。单元素操作匹配到多个元素时会报错，应补充名称或过滤条件使定位唯一，不要习惯性使用 `.nth()` 掩盖歧义。

## 四、截图

```python
# 当前视口
page.screenshot(path="screenshots/page.png")

# 完整可滚动页面
page.screenshot(path="screenshots/full-page.png", full_page=True)

# 单个元素
page.get_by_role("heading").screenshot(path="screenshots/heading.png")
```

截图目录必须先存在；可用 `pathlib.Path.mkdir()` 创建。练习脚本已包含这一处理。

## 五、常见等待策略

### 5.1 首选：让动作自动等待

`click()`、`fill()` 等操作会等待目标满足可见、稳定、可接收事件、已启用等可操作条件：

```python
page.get_by_role("button", name="提交").click()
```

### 5.2 等待页面结果：使用可重试断言

```python
from playwright.sync_api import expect

result = page.get_by_text("提交成功")
expect(result).to_be_visible(timeout=10_000)
expect(result).to_contain_text("成功")
```

`expect` 会在超时前重试，比“先检查一次再判断”更适合动态页面。

### 5.3 等待导航：等待 URL

```python
page.get_by_role("link", name="订单详情").click()
page.wait_for_url("**/orders/*", timeout=10_000)
```

当点击会触发跳转且后续逻辑依赖目标地址时使用。URL 可使用精确字符串、通配符或正则表达式。

### 5.4 等待已知加载状态

```python
page.wait_for_load_state("domcontentloaded")
```

仅在代码确实需要一个明确的文档加载边界时使用。不要把 `networkidle` 当作通用“页面完成”判断：持续轮询、WebSocket 或统计请求可能让网络长期不空闲。

### 5.5 最后手段：等待明确条件

```python
loading = page.get_by_text("正在加载")
loading.wait_for(state="hidden", timeout=10_000)
```

等待业务可观察状态，而不是写 `page.wait_for_timeout(3000)`。固定时间等待会拖慢成功路径，也会在慢环境中偶发失败。

## 六、最小可运行练习

练习文件：[[01-Playwright最小练习.py|Playwright 最小练习]]

在本目录运行：

```powershell
python .\01-Playwright最小练习.py
```

成功时会打印页面标题，并在当前目录的 `screenshots/` 下生成 `example-domain.png`。练习覆盖：

- 启动和关闭 Chromium；
- 访问 `https://example.com`；
- 用角色与名称定位标题；
- 用 `expect` 等待并断言标题可见；
- 截取完整页面。

## 七、排错速查

| 现象 | 原因 | 处理 |
|------|------|------|
| 找不到浏览器可执行文件 | 只安装了 Python 包 | 执行 `python -m playwright install chromium` |
| 定位器严格模式报错 | 定位条件匹配多个元素 | 增加 `name`、`filter()` 或测试 ID，使其唯一 |
| 本机成功、CI 偶发失败 | 使用固定等待或一次性状态检查 | 改用 Locator 自动等待和 `expect` |
| 截图报目录不存在 | 父目录未创建 | 写入前执行 `Path(...).mkdir(parents=True, exist_ok=True)` |
| 页面一直等不到 `networkidle` | 页面存在长连接或持续请求 | 等待具体元素、URL 或业务状态 |

## 延伸与关联

- [[Python-MOC]] — Python 知识体系总导航
- [[01-概念、原理与基本使用|Selenium 概念、原理与基本使用]] — 对比传统 WebDriver 自动化方式
- [[02-Knowledge(知识层)/10-IT技术-IT_Technology/02-后端开发-Backend/01 python/03 生态/03 爬虫/04 自动化/01 DrissionPage/01-快速入门|DrissionPage 快速入门]] — 对比浏览器控制与 HTTP 请求融合方案
