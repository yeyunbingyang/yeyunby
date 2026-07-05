---
title: FastAPI入门
domain: IT_Technology
tags: [FastAPI, Web开发, Python, 后端]
status: 稳定
created: 2026-06-19
updated: 2026-06-19
source: "[[尚硅谷-FastAPI-基础到实战]]"
related: [[02-FastAPI进阶]]
summary: "FastAPI 是一个基于 Python 的高性能 Web 框架，通过装饰器定义路由、Pydantic 验证参数、自动生成交互式文档，支持同步和异步处理请求。"
---

# FastAPI 入门

> 基础程序、路由、请求与响应

## 一、FastAPI 简介

FastAPI 是一个基于 Python 的高性能 Web 框架，专门用于快速构建 API 接口服务。

### 核心特性

| 特性 | 说明 |
|------|------|
| 异步性能高 | 原生支持 `async/await`，并发处理能力强 |
| 开发效率高 | 类型提示 + Pydantic 验证，减少手动校验代码 |
| 自动生成文档 | 提供可交互式 Swagger/ReDoc 文档 |

### 同步与异步

```python
@app.get("/sync")
def func_sync():
    start = time.time()
    for i in range(10):
        time.sleep(1)      # 阻塞，逐个等待
    end = time.time()
    return {"time": f'{end-start:.2f}s'}

@app.get("/async")
async def func_async():
    start = time.time()
    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)  # 并发执行
    end = time.time()
    return {"time": f'{end-start:.2f}s'}
```

- **同步**：请求排队处理，每个 I/O 操作阻塞后续请求
- **异步**：I/O 等待期间可处理其他请求，吞吐量更高
![[Pasted image 20260619140558.png]]

![[Pasted image 20260619140420.png]]

### Pydantic 类型提示与验证

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    return user
```

---

## 二、第一个 FastAPI 程序

### 创建与运行

```bash
# 1. 创建项目（推荐使用虚拟环境）
# 2. 安装依赖
pip install fastapi uvicorn

# 3. 运行项目
uvicorn main:app --reload

# uvicorn[服务器] 文件名:实例名 --reload[修改代码自动重启]
```

- `--reload`：更改代码后自动重启服务器（开发模式）

### 访问项目

- 路由访问：`http://127.0.0.1:8000/`
- 交互式文档：`http://127.0.0.1:8000/docs`

### Hello World

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

> 访问 `http://127.0.0.1:8000/` 得到 `{"message":"Hello World"}`

### 虚拟环境的作用

隔离项目运行环境，避免依赖冲突，保持全局环境的干净和稳定。

---

## 三、路由

**路由**是 URL 地址和处理函数之间的映射关系，决定了当用户访问某个特定网址时，服务器应该执行哪段代码来返回结果。
![[Pasted image 20260619144235.png]]

FastAPI 的路由定义基于 Python 的装饰器模式：

```python
@app.get("/")
async def root():
    return {"message": "hello world"}
```

### 练习：自定义路由

需求：访问路径 `/user/hello`，响应结果是 `{"msg": "我正在学习 FastAPI ......"}`

```python
@app.get("/user/hello")
async def user_hello():
    return {"msg": "我正在学习 FastAPI ......"}
```

---

## 四、参数
![[Pasted image 20260619144425.png]]

参数是客户端发送请求时附带的额外信息和指令，让同一个接口能根据不同的输入返回不同的输出，实现动态交互。

### 参数分类
![[Pasted image 20260619144441.png]]

| 类型 | 位置 | 作用 | 方法 |
|------|------|------|------|
| 路径参数 | URL 路径的一部分 `/book/{id}` | 指向唯一特定资源 | GET |
| 查询参数 | URL? 之后 `k1=v1&k2=v2` | 过滤、排序、分页 | GET |
| 请求体参数 | HTTP Body 中 | 创建/更新资源，携带大量数据（JSON） | POST、PUT |

---

### 4.1 路径参数
![[Pasted image 20260619153349.png]]

```python
@app.get("/book/{id}")
async def get_book(id: int):
    return {"id": id, "title": f"这是第{id}本书"}
```

#### 路径参数 — 类型注解 `Path`

FastAPI 的 `Path` 函数允许为参数声明额外的信息和校验：

```python
from fastapi import Path

@app.get("/book/{id}")
async def get_book(id: int = Path()):
    return {"id": id, "title": f"这是第{id}本书"}
```

**Path 参数说明：**

| 参数 | 说明 |
|------|------|
| `...` | 必填 |
| `gt` / `ge` | 大于 / 大于等于 |
| `lt` / `le` | 小于 / 小于等于 |
| `description` | 描述信息 |
| `min_length` / `max_length` | 字符串长度限制 |

#### 练习：路径参数 + Path 注解

- 接口1：以新闻分类 id 为参数，id 范围 1~100
- 接口2：以新闻分类名称为参数，名称长度 2~10

```python
@app.get("/news/category/{category_id}")
async def get_category(category_id: int = Path(ge=1, le=100)):
    return {"category_id": category_id}

@app.get("/news/category_name/{name}")
async def get_category_name(name: str = Path(min_length=2, max_length=10)):
    return {"name": name}
```

---

### 4.2 查询参数
![[Pasted image 20260619153153.png]]

声明的参数不是路径参数时，FastAPI 自动将其解释为查询参数：

```python
@app.get("/news/news_list")
async def get_news_list(skip: int, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

#### 查询参数 — 类型注解 `Query`

```python
from fastapi import Query

@app.get("/user")
async def get_book(user_id: int = Query()):
    return {"user_id": user_id}
```

**Query 参数说明：** 同 Path 参数（`...`, `gt/ge`, `lt/le`, `description`, `min_length/max_length`）

#### 练习：查询参数

需求：查询图书接口，携带两个查询参数：
- 图书分类：默认值"Python开发"，长度限制 5~255
- 价格：限制范围 50~100

```python
@app.get("/book/search")
async def search_book(
    category: str = Query(default="Python开发", min_length=5, max_length=255),
    price: float = Query(ge=50, le=100)
):
    return {"category": category, "price": price}
```

---

### 4.3 请求体参数
![[Pasted image 20260619153218.png]]

HTTP 请求由三部分组成：
1. **请求行**：方法、URL、协议版本
2. **请求头**：元数据信息（Content-Type、Authorization 等）
3. **请求体**：实际要发送的数据内容

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    return user
```

#### 请求体参数 — 类型注解 `Field`

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
```

**Field 参数说明：**

| 参数 | 说明 |
|------|------|
| `...` | 必填 |
| `gt` / `ge` | 大于 / 大于等于 |
| `lt` / `le` | 小于 / 小于等于 |
| `default` | 默认值 |
| `description` | 描述信息 |
| `min_length` / `max_length` | 长度限制 |

#### 练习：请求体参数 + Field 注解

需求：新增图书接口，包含书名、作者、出版社、售价：
- 书名：不能为空，长度 2~20
- 作者：长度 2~10
- 出版社：默认值"黑马出版社"
- 售价：不能为空，价格大于 0 元

```python
class BookCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=20, description="书名")
    author: str = Field(min_length=2, max_length=10, description="作者")
    publisher: str = Field(default="黑马出版社", description="出版社")
    price: float = Field(..., gt=0, description="售价")

@app.post("/book/add")
async def add_book(book: BookCreate):
    return book
```

---

## 五、响应类型


FastAPI 默认将路径操作函数返回的 **Python 对象**（字典、列表、Pydantic 模型等），经由 `jsonable_encoder` 转换为 **JSON** 兼容格式，包装为 `JSONResponse` 返回。

如需返回非 JSON 数据（HTML、文件流等），FastAPI 提供丰富的响应类型：

| 响应类型                | 用途              | 示例                                  |
| ------------------- | --------------- | ----------------------------------- |
| **`JSONResponse`**  | 默认响应，返回 JSON 数据 | `return {"key": "value"}`           |
| **`HTMLResponse`**  | 返回 HTML 内容      | `return HTMLResponse(html_content)` |
| `PlainTextResponse` | 返回纯文本           | `return PlainTextResponse("text")`  |
| **`FileResponse`**  | 返回文件下载          | `return FileResponse(path)`         |
| `StreamingResponse` | 流式响应            | 生成器函数返回数据                           |
| `RedirectResponse`  | 重定向             | `return RedirectResponse(url)`      |


### 两种设置方式

**方式一：装饰器中指定响应类**（固定返回类型）

```python
from fastapi.responses import HTMLResponse

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是标题</h1>"
```

**方式二：返回响应对象**（文件下载、流式响应等）

```python
from fastapi.responses import FileResponse

@app.get("/file")
async def get_file():
    file_path = "./files/1.jpeg"
    return FileResponse(file_path)
```

### HTML 响应

```python
from fastapi.responses import HTMLResponse

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>Hello World</h1>"
```

### 文件下载响应

`FileResponse` 智能处理文件路径、媒体类型推断、范围请求和缓存头部：

```python
from fastapi.responses import FileResponse

@app.get("/file")
async def get_file():
    file_path = "./files/1.jpeg"
    return FileResponse(file_path)
```

---

## 六、自定义响应数据格式 — `response_model`

`response_model` 通过 Pydantic 模型来严格定义和约束 API 端点的输出格式，在提供自动数据验证和序列化的同时，更是保障数据安全性的第一道防线。【数据类型为json】

```python
from pydantic import BaseModel

class News(BaseModel):
    id: int
    title: str
    content: str

@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    return {
        "id": id,
        "title": f"这是第{id}本书",
        "content": "这是一本好书"
    }
```

---

## 七、异常处理 — HTTPException

对于客户端引发的错误（4xx），应使用 `fastapi.HTTPException` 来中断正常处理流程，并返回标准错误响应。

```python
from fastapi import FastAPI, HTTPException

@app.get('/news/{id}')
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="当前id不存在")
    return {"id": id}
```

---

## 关联笔记

- [[02-FastAPI进阶]] — 中间件、依赖注入、ORM
- [[03-ORM模板代码]] — SQLAlchemy ORM 配置与模型类
- [[code01_FastAPI入门.py]] — PyLab 配套练习代码
- [[Python-MOC]] — Python 知识总导航
