# json-server 本地 Mock 接口搭建指南

> json-server 是一个基于 Node.js 的轻量级工具，可在 30 秒内搭建一套完整的 RESTful API，非常适合前端开发阶段模拟后端接口。

---

## 一、安装 json-server

### 1.1 全局安装

```bash
npm install -g json-server
```

### 1.2 验证安装

```bash
json-server -v
```

> 正常输出版本号（如 `0.17.4`）即表示安装成功。

---

## 二、准备数据文件

### 2.1 创建项目目录

在电脑任意位置创建文件夹（**不含中文**），例如：

```
service/
└── db.json
```

### 2.2 编写 db.json

```json
{
  "address": [
    {
      "id": 101,
      "receiver": "李白姓白",
      "mobile": "13800000101",
      "province": "浙江省",
      "city": "杭州市",
      "area": "西湖区",
      "location": "西湖大道101号",
      "state": 1
    },
    {
      "id": 102,
      "receiver": "苏轼",
      "mobile": "13800000102",
      "province": "北京市",
      "city": "北京市",
      "area": "昌平区",
      "location": "西湖大道102号",
      "state": 0
    },
    {
      "id": 103,
      "receiver": "韩愈",
      "mobile": "13800000103",
      "province": "浙江省",
      "city": "杭州市",
      "area": "西湖区",
      "location": "西湖大道103号",
      "state": 1
    }
  ]
}
```

> 每个顶级键（如 `address`）会自动生成对应的 RESTful 路由。

---

## 三、启动服务

### 3.1 方式一：本机访问（默认）

```bash
cd service
json-server --watch db.json
```

| 配置项 | 默认值 |
|--------|--------|
| 主机 | `localhost` |
| 端口 | `3000` |
| 访问地址 | `http://localhost:3000/address` |

> 仅本机可访问，适合个人开发调试。

### 3.2 方式二：局域网共享

```bash
json-server --host 192.168.28.95 db.json --port 5000
```

| 参数 | 说明 |
|------|------|
| `--host` | 本机局域网 IP（`ipconfig` / `ifconfig` 查看） |
| `--port` | 自定义端口号 |
| 访问地址 | `http://192.168.28.95:5000/address` |

> 同一局域网内的其他设备（手机、同事电脑）均可访问。

---

## 四、常用 RESTful API 操作

启动后自动支持以下接口：

| 方法       | 请求地址           | 说明                |
| -------- | -------------- | ----------------- |
| `GET`    | `/address`     | 获取全部地址列表          |
| `GET`    | `/address/101` | 获取 id=101 的地址     |
| `POST`   | `/address`     | 新增地址（Body 传 JSON） |
| `PUT`    | `/address/101` | 全量更新 id=101 的地址   |
| `PATCH`  | `/address/101` | 局部更新 id=101 的地址   |
| `DELETE` | `/address/101` | 删除 id=101 的地址     |

### 查询示例

```bash
# 按条件筛选
curl "http://localhost:3000/address?province=浙江省"

# 分页（_page 页码，_limit 每页条数）
curl "http://localhost:3000/address?_page=1&_limit=2"

# 排序（_sort 字段，_order 顺序）
curl "http://localhost:3000/address?_sort=id&_order=desc"
```

---

## 五、进阶配置（可选）

### 5.1 自定义路由

创建 `routes.json`：

```json
{
  "/api/address": "/address"
}
```

启动时加载：

```bash
json-server --watch db.json --routes routes.json
```

### 5.2 指定中间件（如跨域）

```bash
json-server --watch db.json --middlewares ./cors.js
```

### 5.3 静默启动（不打开浏览器）

```bash
json-server --watch db.json --no-open
```

---

## 六、常见问题

| 问题 | 解决 |
|------|------|
| 端口被占用 | 换端口：`--port 5001` |
| 找不到 `json-server` 命令 | 检查全局安装路径，或使用 `npx json-server` |
| 中文路径报错 | 文件夹/文件路径中不要出现中文 |
| 局域网其他设备无法访问 | 关闭防火墙，或确认 `--host` 为本机局域网 IP |

---

## 七、快速启动脚本（推荐）

在 `package.json` 中添加：

```json
{
  "scripts": {
    "mock": "json-server --watch db.json --port 3000"
  }
}
```

之后直接运行：

```bash
npm run mock
```
