# Bun 快速入门使用指南

> 版本：Bun 1.x | 更新时间：2026-06
> Bun 是一个快速、轻量级的 JavaScript 全功能工具链，用 Zig 语言编写，基于 JavaScriptCore 引擎。

---

## 目录

1. [什么是 Bun](#什么是-bun)
2. [安装 Bun](#安装-bun)
3. [快速创建项目](#快速创建项目)
4. [核心功能演示](#核心功能演示)
5. [实战 Demo](#实战-demo)
6. [常用命令速查](#常用命令速查)
7. [与 Node.js 对比](#与-nodejs-对比)
8. [注意事项](#注意事项)

---

## 什么是 Bun

Bun 是一个**全功能 JavaScript 工具链**，集以下能力于一身：

| 功能 | 替代工具 | 说明 |
|------|----------|------|
| **运行时** | Node.js | 执行 JS/TS 代码 |
| **包管理器** | npm / yarn / pnpm | 安装依赖，速度极快 |
| **打包器** | webpack / Vite / Rollup | 构建和打包项目 |
| **测试运行器** | Jest / Vitest | 运行单元测试 |
| **脚本执行器** | package.json scripts | 运行开发脚本 |

**核心优势：**
- 🚀 **极速**：启动时间和执行速度远超 Node.js
- 📦 **零配置**：原生支持 TypeScript、JSX，无需额外配置
- 🔧 **一体化**：一个工具替代多个，减少工具链复杂度
- 🧪 **兼容 Node.js**：大部分 npm 包可直接运行

---

## 安装 Bun

### macOS / Linux（推荐）

```bash
curl -fsSL https://bun.sh/install | bash
```

### Windows

```powershell
# PowerShell
powershell -c "irm bun.sh/install.ps1 | iex"

# 或 Scoop
scoop install bun
```

### 通过 npm 安装（需先装 Node.js）

```bash
npm install -g bun
```

### 验证安装

```bash
bun --version
# 输出类似：1.3.0
```

---

## 快速创建项目

### 1. 初始化空白项目

```bash
mkdir my-bun-app && cd my-bun-app
bun init
```

按提示操作（默认回车即可），会生成：

```
my-bun-app/
├── .gitignore
├── index.ts          # 入口文件
├── tsconfig.json     # TypeScript 配置
└── README.md
```

### 2. 安装依赖

```bash
# 安装生产依赖
bun add <package-name>

# 安装开发依赖
bun add -d <package-name>

# 安装所有依赖（根据 package.json）
bun install
```

安装速度通常是 npm 的 **10-30 倍**。

---

## 核心功能演示

### Demo 1：运行 TypeScript（无需配置）

Bun 原生支持 `.ts` 文件，无需 `ts-node` 或编译步骤。

**`hello.ts`**

```typescript
// 直接运行 TypeScript，无需编译
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const user: string = "Bun";
console.log(greet(user));
```

```bash
bun run hello.ts
# 输出：Hello, Bun!
```

---

### Demo 2：内置 HTTP 服务器（Bun.serve）

Bun 内置了高性能的 HTTP 服务器 API。

**`server.ts`**

```typescript
const server = Bun.serve({
  port: 3000,
  hostname: "0.0.0.0",
  fetch(req) {
    const url = new URL(req.url);

    // 路由处理
    if (url.pathname === "/") {
      return new Response("🚀 Bun Server is running!", {
        headers: { "Content-Type": "text/plain" },
      });
    }

    if (url.pathname === "/api/hello") {
      return Response.json({
        message: "Hello from Bun!",
        timestamp: new Date().toISOString(),
      });
    }

    if (url.pathname === "/api/users" && req.method === "GET") {
      const users = [
        { id: 1, name: "Alice" },
        { id: 2, name: "Bob" },
      ];
      return Response.json(users);
    }

    return new Response("Not Found", { status: 404 });
  },
});

console.log(`✅ Server running at http://localhost:${server.port}`);
```

```bash
# 开发模式（热重载）
bun --hot run server.ts

# 生产模式
bun run server.ts
```

**测试接口：**

```bash
curl http://localhost:3000/
# 输出：🚀 Bun Server is running!

curl http://localhost:3000/api/hello
# 输出：{"message":"Hello from Bun!","timestamp":"..."}
```

---

### Demo 3：内置文件操作 API

Bun 提供了高度优化的文件读写 API。

**`file-demo.ts`**

```typescript
import { file, write, $ } from "bun";

// 1. 读取文件（同步）
const text = await Bun.file("./data.txt").text();
console.log("文件内容:", text);

// 2. 读取 JSON 文件
const config = await Bun.file("./config.json").json();
console.log("配置:", config);

// 3. 写入文件
await Bun.write("./output.txt", "Hello from Bun!\n");

// 4. 检查文件是否存在
const exists = await Bun.file("./output.txt").exists();
console.log("文件存在:", exists);

// 5. 使用 Shell 命令（Bun.$）
const result = await $`echo "Current directory: $(pwd)"`;
console.log(result.stdout.toString());
```

---

### Demo 4：内置测试框架（替代 Jest）

Bun 内置了与 Jest 兼容的测试运行器。

**`math.ts`**（被测试的模块）

```typescript
export function add(a: number, b: number): number {
  return a + b;
}

export function divide(a: number, b: number): number {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
}
```

**`math.test.ts`**（测试文件）

```typescript
import { describe, it, expect } from "bun:test";
import { add, divide } from "./math";

describe("Math utilities", () => {
  it("should add two numbers", () => {
    expect(add(2, 3)).toBe(5);
    expect(add(-1, 1)).toBe(0);
  });

  it("should divide two numbers", () => {
    expect(divide(10, 2)).toBe(5);
    expect(divide(7, 2)).toBe(3.5);
  });

  it("should throw on divide by zero", () => {
    expect(() => divide(10, 0)).toThrow("Cannot divide by zero");
  });
});
```

```bash
# 运行测试
bun test

# 监视模式
bun test --watch

# 生成覆盖率报告
bun test --coverage
```

---

### Demo 5：打包构建（替代 webpack/Vite）

Bun 内置了打包器，支持零配置构建。

**`build-demo.ts`**

```typescript
// 构建入口文件
await Bun.build({
  entrypoints: ["./src/index.ts"],
  outdir: "./dist",
  target: "bun",        // 目标平台：bun / node / browser
  format: "esm",        // 输出格式：esm / cjs
  minify: true,         // 代码压缩
  splitting: true,      // 代码分割
  sourcemap: "external", // 生成 source map
});

console.log("✅ Build completed!");
```

```bash
bun run build-demo.ts
```

**打包为独立可执行文件：**

```bash
# 将项目打包为单个可执行文件（无需 Node.js/Bun 环境）
bun build ./src/cli.ts --compile --outfile ./my-app

# 运行
./my-app
```

---

### Demo 6：WebSocket 服务器

Bun 内置了 WebSocket 支持。

**`websocket-server.ts`**

```typescript
Bun.serve({
  port: 3000,
  fetch(req, server) {
    const url = new URL(req.url);
    if (url.pathname === "/ws") {
      const success = server.upgrade(req);
      if (success) return undefined;
    }
    return new Response("WebSocket server running");
  },
  websocket: {
    open(ws) {
      console.log("Client connected");
      ws.subscribe("broadcast");
    },
    message(ws, message) {
      console.log(`Received: ${message}`);
      ws.publish("broadcast", `Echo: ${message}`);
    },
    close(ws) {
      console.log("Client disconnected");
    },
  },
});

console.log("WebSocket server running on ws://localhost:3000/ws");
```

---

## 实战 Demo：完整 REST API 项目

### 项目结构

```
bun-api-demo/
├── src/
│   ├── index.ts          # 入口
│   ├── routes/
│   │   └── tasks.ts      # 任务路由
│   ├── db.ts             # 内存数据库
│   └── types.ts          # 类型定义
├── tests/
│   └── api.test.ts       # API 测试
├── package.json
└── tsconfig.json
```

### 1. 初始化项目

```bash
mkdir bun-api-demo && cd bun-api-demo
bun init
```

### 2. 安装 Elysia（Bun 生态最流行的 Web 框架）

```bash
bun add elysia
```

### 3. 类型定义（`src/types.ts`）

```typescript
export interface Task {
  id: number;
  title: string;
  completed: boolean;
  createdAt: string;
}

export interface CreateTaskDto {
  title: string;
}

export interface UpdateTaskDto {
  title?: string;
  completed?: boolean;
}
```

### 4. 内存数据库（`src/db.ts`）

```typescript
import type { Task } from "./types";

let tasks: Task[] = [
  { id: 1, title: "学习 Bun", completed: false, createdAt: new Date().toISOString() },
  { id: 2, title: "写文档", completed: true, createdAt: new Date().toISOString() },
];

let nextId = 3;

export const db = {
  getAll(): Task[] {
    return tasks;
  },
  getById(id: number): Task | undefined {
    return tasks.find((t) => t.id === id);
  },
  create(title: string): Task {
    const task: Task = {
      id: nextId++,
      title,
      completed: false,
      createdAt: new Date().toISOString(),
    };
    tasks.push(task);
    return task;
  },
  update(id: number, data: Partial<Task>): Task | null {
    const index = tasks.findIndex((t) => t.id === id);
    if (index === -1) return null;
    tasks[index] = { ...tasks[index], ...data };
    return tasks[index];
  },
  delete(id: number): boolean {
    const index = tasks.findIndex((t) => t.id === id);
    if (index === -1) return false;
    tasks.splice(index, 1);
    return true;
  },
};
```

### 5. 路由（`src/routes/tasks.ts`）

```typescript
import { Elysia, t } from "elysia";
import { db } from "../db";

export const tasksRouter = new Elysia({ prefix: "/tasks" })
  .get("/", () => {
    return { data: db.getAll(), count: db.getAll().length };
  })

  .get("/:id", ({ params, set }) => {
    const task = db.getById(Number(params.id));
    if (!task) {
      set.status = 404;
      return { error: "Task not found" };
    }
    return { data: task };
  })

  .post("/", ({ body, set }) => {
    const task = db.create(body.title);
    set.status = 201;
    return { data: task, message: "Task created" };
  }, {
    body: t.Object({
      title: t.String({ minLength: 1 }),
    }),
  })

  .patch("/:id", ({ params, body, set }) => {
    const task = db.update(Number(params.id), body);
    if (!task) {
      set.status = 404;
      return { error: "Task not found" };
    }
    return { data: task, message: "Task updated" };
  })

  .delete("/:id", ({ params, set }) => {
    const success = db.delete(Number(params.id));
    if (!success) {
      set.status = 404;
      return { error: "Task not found" };
    }
    set.status = 204;
    return { message: "Task deleted" };
  });
```

### 6. 入口文件（`src/index.ts`）

```typescript
import { Elysia } from "elysia";
import { tasksRouter } from "./routes/tasks";

const app = new Elysia()
  .get("/", () => ({
    message: "Bun API Demo",
    version: "1.0.0",
    endpoints: ["/tasks"],
  }))
  .use(tasksRouter)
  .onError(({ code, error, set }) => {
    console.error(`[Error ${code}]`, error);
    set.status = 500;
    return { error: "Internal server error" };
  })
  .listen(3000);

console.log(`🚀 Server running at http://localhost:${app.server?.port}`);
console.log(`📚 API Docs: http://localhost:${app.server?.port}/swagger`);

export type App = typeof app;
```

### 7. API 测试（`tests/api.test.ts`）

```typescript
import { describe, it, expect, beforeAll, afterAll } from "bun:test";

const BASE_URL = "http://localhost:3000";

describe("Tasks API", () => {
  it("GET / should return API info", async () => {
    const res = await fetch(`${BASE_URL}/`);
    const data = await res.json();
    expect(res.status).toBe(200);
    expect(data.message).toBe("Bun API Demo");
  });

  it("GET /tasks should return all tasks", async () => {
    const res = await fetch(`${BASE_URL}/tasks`);
    const data = await res.json();
    expect(res.status).toBe(200);
    expect(Array.isArray(data.data)).toBe(true);
    expect(data.count).toBeGreaterThan(0);
  });

  it("POST /tasks should create a task", async () => {
    const res = await fetch(`${BASE_URL}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: "Test task" }),
    });
    const data = await res.json();
    expect(res.status).toBe(201);
    expect(data.data.title).toBe("Test task");
    expect(data.data.completed).toBe(false);
  });

  it("GET /tasks/:id should return single task", async () => {
    const res = await fetch(`${BASE_URL}/tasks/1`);
    const data = await res.json();
    expect(res.status).toBe(200);
    expect(data.data.id).toBe(1);
  });

  it("GET /tasks/:id should return 404 for unknown id", async () => {
    const res = await fetch(`${BASE_URL}/tasks/9999`);
    expect(res.status).toBe(404);
  });

  it("PATCH /tasks/:id should update a task", async () => {
    const res = await fetch(`${BASE_URL}/tasks/1`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: true }),
    });
    const data = await res.json();
    expect(res.status).toBe(200);
    expect(data.data.completed).toBe(true);
  });

  it("DELETE /tasks/:id should delete a task", async () => {
    const res = await fetch(`${BASE_URL}/tasks/2`, { method: "DELETE" });
    expect(res.status).toBe(204);
  });
});
```

### 8. 运行项目

```bash
# 开发模式（热重载）
bun --hot run src/index.ts

# 运行测试（需要先启动服务器）
bun test

# 构建生产版本
bun build src/index.ts --outdir ./dist --target bun

# 运行生产版本
bun run dist/index.js
```

### 9. Dockerfile 部署

```dockerfile
# 构建阶段
FROM oven/bun:1 AS builder
WORKDIR /app
COPY package.json bun.lock ./
RUN bun install --frozen-lockfile
COPY . .
RUN bun build src/index.ts --outdir ./dist --target bun

# 运行阶段
FROM oven/bun:1-slim AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./
EXPOSE 3000
CMD ["bun", "run", "dist/index.js"]
```

---

## 常用命令速查

| 命令 | 说明 |
|------|------|
| `bun --version` | 查看版本 |
| `bun init` | 初始化项目 |
| `bun run <file>` | 运行文件 |
| `bun --hot run <file>` | 热重载模式 |
| `bun install` | 安装依赖 |
| `bun add <pkg>` | 添加依赖 |
| `bun add -d <pkg>` | 添加开发依赖 |
| `bun remove <pkg>` | 移除依赖 |
| `bun test` | 运行测试 |
| `bun test --watch` | 测试监视模式 |
| `bun test --coverage` | 生成覆盖率报告 |
| `bun build <entry>` | 打包构建 |
| `bun build --compile <entry>` | 打包为独立可执行文件 |
| `bunx <pkg>` | 执行 npx 等价命令 |
| `bun upgrade` | 升级 Bun |

---

## 与 Node.js 对比

| 特性 | Bun | Node.js |
|------|-----|---------|
| 语言 | Zig | C++ |
| JS 引擎 | JavaScriptCore | V8 |
| TypeScript 支持 | ✅ 原生 | ❌ 需 ts-node |
| JSX 支持 | ✅ 原生 | ❌ 需 Babel |
| 包管理器 | 内置 | npm（外部） |
| 测试框架 | 内置 | Jest/Vitest（外部） |
| 打包器 | 内置 | webpack/Vite（外部） |
| 安装速度 | 极快（10-30x） | 较慢 |
| 启动速度 | 快 | 较慢 |
| 内存占用 | 低 | 较高 |
| 生态成熟度 | 成长中 | 非常成熟 |
| Windows 支持 | 较新 | 完善 |

---

## 注意事项

1. **兼容性**：大部分 npm 包可直接使用，但部分复杂原生模块可能需额外适配
2. **版本更新**：Bun 迭代很快，建议定期运行 `bun upgrade`
3. **Windows**：Windows 支持相对较新，生产环境建议 Linux/macOS
4. **Bytecode 缓存**：生产构建可启用 `--bytecode` 加速启动，但需注意版本绑定
5. **锁文件**：Bun 使用 `bun.lock`（或 `bun.lockb`），与 `package-lock.json` 不兼容

---

## 参考资源

- [Bun 官方文档](https://bun.sh/docs)
- [Bun GitHub](https://github.com/oven-sh/bun)
- [Elysia 框架](https://elysiajs.com/)

---

*文档完成。祝你使用 Bun 开发愉快！🚀*
