---
title: OpenCLI 浏览器抓取操作参考
description: 基于 opencli-browser 的标准数据抓取流程——先观察（state/find）再定位（ref/selector）后提取（get/extract/network），每步验证
aliases:
  - opencli-browser
  - OpenCLI 浏览器自动化
tags:
  - OpenCLI
  - browser-automation
  - scraping
  - reference
created: 2026-07-23
updated: 2026-07-23
status: 稳定
domain: Core_Ability
related:
  - "01-OpenCLI"
summary: "opencli-browser 浏览器抓取的标准流程与关键注意事项——DOM 提取、API 拦截、动态翻页、表单填写、诊断排查。主文见 01-OpenCLI。"
---

# OpenCLI 浏览器抓取操作参考

> 基于 `opencli-browser` 的标准数据抓取流程。关于 OpenCLI 的整体介绍见 [[OpenCLI/01-OpenCLI]]。
>
> 核心原则：**先观察（`state`/`find`），再定位（`ref`/`selector`），后提取（`get`/`extract`/`network`），每步验证（`match_level`/`get value`）。**

---

## 标准流程

### Step 1 → 3：打开 → 观察 → 定位

```bash
opencli browser demo open "https://example.com/items"
opencli browser demo wait selector ".item-list" --timeout 10000
opencli browser demo state                             # 获取 DOM 快照（带 [N] 编号）
opencli browser demo find --css ".item h2"             # 定位元素
```

`state` 输出示例：
```
[1] <div class="item-list">
  [2] <div class="item">    [3] <h2>商品 A</h2>
```

### Step 4：提取数据

**方式 A：`get text`（少量字段）**
```bash
opencli browser demo get text 3    # 商品 A 标题
```

**方式 B：`extract`（文章/长内容）**
```bash
opencli browser demo extract --selector ".item-list" --chunk-size 4000
```

**方式 C：`eval`（结构化 JSON）**
```bash
opencli browser demo eval "(() => {
  return [...document.querySelectorAll('.item')].map(el => ({
    title: el.querySelector('h2')?.innerText,
    price: el.querySelector('.price')?.innerText
  }));
})()"
```

**推荐：`network`（API 拦截，最稳定）**
```bash
opencli browser demo network --filter "title,price"         # 查看 API 形状
opencli browser demo network --detail <key>                 # 获取完整 JSON
```

---

## 高级场景

### 动态翻页

```bash
# 循环：state → extract → click"加载更多" → wait → state（旧 ref 已失效！）
opencli browser demo state
opencli browser demo click 20
opencli browser demo wait selector ".item:nth-child(11)" --timeout 10000
opencli browser demo state    # 必须重新 state
```

### 表单填写

```bash
opencli browser demo fill 3 "OpenCLI"    # fill=设值, type=模拟键盘
opencli browser demo get value 3          # 必须验证（React 受控组件会吞字符）
opencli browser demo click 5              # 提交按钮
opencli browser demo wait selector ".result" --timeout 15000
opencli browser demo state
```

---

## 关键注意事项

| 注意点 | 说明 |
|--------|------|
| **Ref 会失效** | 页面任何变化后必须重新 `state` |
| **优先 `network`** | API 拦截比 DOM 抓取稳定 10 倍 |
| **检查 `match_level`** | `reidentified` 表示猜测了元素，先验证 |
| **`type` 后验证** | React 受控控件会吞字符，必须 `get value` |
| **`eval` 只读** | 不要用 `eval` 做写入操作，用 `click`/`fill` |
| **等待不可少** | SPA/懒加载后必须 `wait` 再 `state` |

---

## 快速诊断

```bash
opencli doctor                               # 1. 环境检查
opencli browser demo state                   # 2. 当前页面结构
opencli browser demo find --css "选择器"      # 3. 元素是否存在
opencli browser demo frames                  # 4. 是否 iframe
opencli browser demo network --all           # 5. 数据是否来自 API
```
