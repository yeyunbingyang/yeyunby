基于 `opencli-browser` 的文档，对**任意网站**进行数据抓取的标准流程如下。核心原则是：**先观察（`state`/`find`），再定位（`ref`/`selector`），后提取（`get`/`extract`/`network`），每步验证（`match_level`/`get value`）。

---

## 一、标准抓取流程（以静态列表页为例）

### Step 1: 打开页面并获取结构快照

```bash
# 创建 session（这里叫 demo）
opencli browser demo open "https://example.com/items"

# 等待关键元素出现（SPA 或懒加载必须）
opencli browser demo wait selector ".item-list" --timeout 10000

# 获取 DOM 快照，拿到 [N] 数字引用
opencli browser demo state
```

**`state` 输出示例**：
```
[1] <div class="item-list">
  [2] <div class="item">
    [3] <h2>商品 A</h2>
    [4] <span class="price">¥100</span>
  [5] <div class="item">
    [6] <h2>商品 B</h2>
    [7] <span class="price">¥200</span>
```

### Step 2: 用 `find` 精确锁定目标元素

```bash
# 获取所有商品标题
opencli browser demo find --css ".item h2"

# 获取所有价格
opencli browser demo find --css ".item .price"
```

`find` 会返回带 `ref` 的匹配项，你可以直接用这个 `ref` 做后续操作。

### Step 3: 提取数据

**方式 A：逐个 `get text`（适合少量精确字段）**
```bash
opencli browser demo get text 3   # 商品 A 标题
opencli browser demo get text 4   # 商品 A 价格
```

**方式 B：`extract` 长文提取（适合文章、详情页）**
```bash
# 自动识别 <main>/<article>/<body>，分块返回 Markdown
opencli browser demo extract --selector ".item-list" --chunk-size 4000
# 返回 { content, next_start_char }，循环直到 next_start_char 为 null
```

**方式 C：`eval` 定向提取（适合结构化 JSON 数据）**
```bash
opencli browser demo eval "(() => {
  const items = [...document.querySelectorAll('.item')];
  return items.map(el => ({
    title: el.querySelector('h2')?.innerText,
    price: el.querySelector('.price')?.innerText
  }));
})()"
```

---

## 二、高级场景：动态页面 / 需要交互

### 场景：点击"加载更多"翻页抓取

```bash
opencli browser demo open "https://example.com/items"
opencli browser demo state

# 循环执行：抓取当前页 → 点击加载更多 → 等待新内容 → 重新 state
# 第 1 轮
opencli browser demo extract --selector ".item-list"

# 点击"加载更多"按钮（假设 ref 为 20）
opencli browser demo click 20

# 必须等待新内容渲染！
opencli browser demo wait selector ".item-list .item:nth-child(11)" --timeout 10000

# 重新 state，旧 ref 已失效！
opencli browser demo state

# 第 2 轮：重新 find + extract
opencli browser demo extract --selector ".item-list"
```

**关键规则**：导航、点击、表单提交、SPA 路由变化都会使旧 `ref` 失效。必须 **`state` → action → `state`**。

### 场景：填写表单后抓取搜索结果

```bash
opencli browser demo open "https://example.com/search"

# 1. 观察表单
opencli browser demo state
# 假设 [3] 是搜索框，[5] 是提交按钮

# 2. 输入关键词（fill 直接设值，type 模拟键盘）
opencli browser demo fill 3 "OpenCLI"
# 或：opencli browser demo type 3 "OpenCLI"

# 3. 验证输入
opencli browser demo get value 3

# 4. 提交（优先 click 按钮，不要 eval submit）
opencli browser demo click 5

# 5. 等待结果列表
opencli browser demo wait selector ".result-item" --timeout 15000

# 6. 重新 state 获取新 ref
opencli browser demo state

# 7. 提取
opencli browser demo extract --selector ".results"
```

---

## 三、最佳实践：优先用 `network` 而非 DOM 抓取

如果页面通过 XHR/Fetch 从 API 获取数据，**直接拦截 API 响应**比解析 DOM 更可靠、更省 token。

```bash
# 1. 打开页面
opencli browser demo open "https://example.com/items"

# 2. 触发数据加载（滚动、点击等）
opencli browser demo scroll down --amount 800

# 3. 查看网络请求形状
opencli browser demo network --filter "title,price"
# 返回类似：
# { key: "items-api-a1b2", method: "GET", url: "/api/items", shape: { data: [{title, price}] } }

# 4. 提取具体 API 响应体
opencli browser demo network --detail items-api-a1b2
# 返回完整 JSON body
```

**优势**：API 返回的是结构化 JSON，无 DOM 漂移问题，不受前端重渲染影响。

---

## 四、处理复杂表单控件（Compound）

如果 `state` 显示 `compounds (N):`，说明有 date/select/file 等特殊控件：

```bash
# 查看 compound 信息
opencli browser demo state
# compounds (1): [12] select: { options: [...], options_total: 137, current: "" }

# 直接按 label 选择（CLI 匹配 live DOM，不受 50 条截断限制）
opencli browser demo select 12 "United States"

# 验证
opencli browser demo get value 12
```

---

## 五、在 Claude Code 中自动化（自然语言驱动）

安装 skill 后，你**不需要手动敲命令**。Claude Code 会自动执行上述流程：

> **你输入**：*"抓取 https://example.com/items 上的所有商品名称和价格"*  
> **Claude Code 内部执行**：
> 1. `browser demo open <url>`
> 2. `browser demo state` → 识别列表结构
> 3. `browser demo find --css ".item h2"` / `.price`
> 4. `browser demo get text <ref>` 循环提取
> 5. 整理成表格/JSON 返回给你

> **你输入**：*"这个页面是懒加载的，帮我滚动到底部把所有数据抓下来"*  
> **Claude Code 内部执行**：
> 6. 循环：`scroll down` → `wait` → `state` → `extract`，直到检测到"没有更多数据"

---

## 六、关键注意事项（避免踩坑）

| 注意点 | 说明 |
|--------|------|
| **🔴 Ref 会失效** | 页面任何变化（导航、点击、SPA 路由）后必须重新 `state`，旧 `[N]` 可能指向错误元素 |
| **🔴 优先 `network` 而非 DOM** | 如果数据来自 API，拦截网络请求比 scraping DOM 稳定 10 倍 |
| **🔴 检查 `match_level`** | `reidentified` 表示 CLI 猜测了新元素，务必 `get text/value` 验证后再继续 |
| **🔴 `type` 后验证** | React 受控输入、自动补全、mask 字段会静默吞字符，`type` 后必须 `get value` |
| **🔴 不用 `eval` 做写入** | `eval` 是只读的！提交表单、点击按钮必须用 `click`/`type`/`keys` |
| **🔴 等待是必须的** | SPA、懒加载、登录跳转后必须 `wait selector/text` 再 `state`，否则拿到的是旧 DOM |
| **🔴 用 `&&` 链式执行** | 同一 shell 内 `state && click 3 && get text 3`，分开的 shell 可能因页面变化导致 ref 竞争 |
| **🔴 截图是最后手段** | `screenshot` burn token 且 Agent 难以直接理解，优先 `state` + `find` |

---

## 七、快速诊断指令

抓取失败时，按此顺序排查：

```bash
# 1. 环境检查
opencli doctor

# 2. 查看当前页面结构（确认元素是否存在）
opencli browser demo state

# 3. 元素是否存在？
opencli browser demo find --css "你的选择器"

# 4. 是否跨域 iframe？
opencli browser demo frames

# 5. 数据是否来自 API？
opencli browser demo network --all

# 6. 查看详细执行日志
opencli browser demo state -v
```

如果你有**具体的网站**想抓，可以把 URL 和要抓的字段告诉我，我可以帮你写出精确的 `opencli browser` 命令序列。