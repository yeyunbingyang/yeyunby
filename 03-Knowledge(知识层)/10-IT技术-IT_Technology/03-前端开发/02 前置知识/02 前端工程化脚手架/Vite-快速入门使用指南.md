# Vite 快速入门使用指南

> 版本：Vite 6.x | 更新时间：2026-06
> Vite 是下一代前端构建工具，提供极速的冷启动和热更新体验，相当于前端领域的 "Spring Boot 脚手架"。
![[Pasted image 20260630161411.png]]
---

## 目录

1. [简介](#简介)
2. [环境要求](#环境要求)
3. [快速创建项目](#快速创建项目)
4. [项目结构解析](#项目结构解析)
5. [核心功能演示](#核心功能演示)
6. [实战 Demo](#实战-demo)
7. [项目打包与部署](#项目打包与部署)
8. [常用命令速查](#常用命令速查)
9. [与 Webpack 对比](#与-webpack-对比)
10. [注意事项](#注意事项)

---

## 简介

官网：[https://cn.vitejs.dev](https://cn.vitejs.dev)

Vite 是 Vue 作者尤雨溪开发的**下一代前端构建工具**，核心理念：

- **极速冷启动**：基于原生 ESM，无需打包即可启动开发服务器
- **即时热更新**：利用浏览器原生 ESM，实现毫秒级 HMR
- **高效构建**：使用 Rollup 进行生产构建，输出高度优化的静态资源
- **开箱即用**：内置 TypeScript、JSX、CSS 等支持，零配置即可开始

**Vite 的定位：**

| 能力 | 说明 | 类比 |
|------|------|------|
| 项目脚手架 | 快速创建标准化前端项目 | Spring Boot Initializr |
| 开发服务器 | 极速启动，即时热更新 | Spring Boot DevTools |
| 构建工具 | 生产环境代码打包优化 | Maven/Gradle 打包 |
| 工程化规范 | 统一目录结构、代码规范 | Spring Boot 约定优于配置 |

---

## 环境要求

| 环境 | 要求 |
|------|------|
| Node.js | **18+** 或 **20+**（推荐） |
| 包管理器 | npm / yarn / pnpm / bun |

> ⚠️ **兼容性注意**：部分模板需要更高 Node 版本，当包管理器发出警告时，请升级 Node 版本。

```bash
# 检查 Node 版本
node -v

# 检查 npm 版本
npm -v
```

---

## 快速创建项目

### 方式一：交互式创建（推荐）

```bash
npm create vite
```

按向导选择：
1. **项目名称**：输入项目目录名
2. **框架**：选择技术栈（Vue / React / Svelte / Vanilla 等）
3. **变体**：选择语言（TypeScript / JavaScript）

```bash
# 示例输出
✔ Project name: my-vite-app
✔ Select a framework: Vue
✔ Select a variant: TypeScript

Scaffolding project in /path/to/my-vite-app...
Done. Now run:

  cd my-vite-app
  npm install
  npm run dev
```

### 方式二：命令行直接创建

```bash
# Vue + TypeScript
npm create vite@latest my-vue-app -- --template vue-ts

# React + TypeScript
npm create vite@latest my-react-app -- --template react-ts

# 纯 JavaScript
npm create vite@latest my-app -- --template vanilla
```

### 方式三：使用其他包管理器

```bash
# Yarn
yarn create vite

# pnpm
pnpm create vite

# Bun
bun create vite
```

---

## 项目结构解析

以 Vue + TypeScript 模板为例：

```
my-vite-app/
├── public/                 # 静态资源（直接复制到 dist）
│   └── vite.svg
├── src/
│   ├── assets/             # 项目资源（会被构建工具处理）
│   │   └── vue.svg
│   ├── components/         # 组件目录
│   │   └── HelloWorld.vue
│   ├── App.vue             # 根组件
│   ├── main.ts             # 入口文件
│   └── style.css           # 全局样式
├── index.html              # HTML 入口模板
├── vite.config.ts          # Vite 配置文件
├── tsconfig.json           # TypeScript 配置
├── tsconfig.node.json      # Node 环境 TS 配置
├── package.json            # 项目依赖与脚本
└── README.md
```

**关键文件说明：**

| 文件 | 作用 |
|------|------|
| `index.html` | 应用入口 HTML，Vite 会注入打包后的 JS/CSS |
| `vite.config.ts` | Vite 核心配置，插件、路径别名、代理等 |
| `src/main.ts` | JS 入口，创建 Vue/React 应用实例 |
| `public/` | 不参与构建的静态文件，直接复制到输出目录 |
| `src/assets/` | 参与构建的资源，会被压缩、hash 处理 |

---

## 核心功能演示

### Demo 1：安装依赖

```bash
# 进入项目目录
cd my-vite-app

# 安装项目所有依赖
npm install

# 安装指定依赖到当前项目
npm install axios

# 安装开发依赖
npm install -D @types/node

# 全局安装（通常用于 CLI 工具）
npm install -g vite
```

---

### Demo 2：启动开发服务器

```bash
# 启动开发服务器（默认端口 5173）
npm run dev

# 输出：
#   VITE v6.x  ready in xxx ms
#   ➜  Local:   http://localhost:5173/
#   ➜  Network: use --host to expose
#   ➜  press h + enter to show help
```

**开发服务器特性：**
- 极速冷启动（毫秒级）
- 即时热更新（HMR），修改代码浏览器自动刷新
- 按需编译，只编译当前页面需要的模块
- 支持 Source Map，方便调试

---

### Demo 3：配置路径别名

**`vite.config.ts`**

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),      // @ 指向 src 目录
      '@components': resolve(__dirname, 'src/components'),
      '@assets': resolve(__dirname, 'src/assets'),
    },
  },
})
```

**`tsconfig.json`**（TypeScript 需要同步配置）

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

**使用方式：**

```typescript
// 之前
import HelloWorld from '../../../components/HelloWorld.vue'

// 之后
import HelloWorld from '@components/HelloWorld.vue'
import { useUserStore } from '@/stores/user'
```

---

### Demo 4：配置代理（解决跨域）

**`vite.config.ts`**

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,           // 开发服务器端口
    open: true,           // 自动打开浏览器
    proxy: {
      '/api': {
        target: 'http://localhost:8080',  // 后端 API 地址
        changeOrigin: true,             // 改变请求源
        rewrite: (path) => path.replace(/^\/api/, ''), // 重写路径
      },
      '/upload': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})
```

**使用方式：**

```typescript
// 前端代码中直接请求 /api，会被代理到后端
fetch('/api/users')
  .then(res => res.json())
  .then(data => console.log(data))

// 实际请求的是 http://localhost:8080/users
```

---

### Demo 5：环境变量配置

Vite 使用 `.env` 文件管理环境变量，以 `VITE_` 开头的变量会暴露到客户端。

**`.env.development`**（开发环境）

```bash
VITE_APP_TITLE=My App (Dev)
VITE_API_BASE_URL=/api
VITE_APP_VERSION=1.0.0
```

**`.env.production`**（生产环境）

```bash
VITE_APP_TITLE=My App
VITE_API_BASE_URL=https://api.example.com
VITE_APP_VERSION=1.0.0
```

**代码中使用：**

```typescript
// 访问环境变量
console.log(import.meta.env.VITE_APP_TITLE)
console.log(import.meta.env.VITE_API_BASE_URL)

// 判断当前环境
if (import.meta.env.DEV) {
  console.log('开发环境')
}
if (import.meta.env.PROD) {
  console.log('生产环境')
}
```

---

### Demo 6：CSS 预处理器支持

Vite 内置支持 Sass、Less、Stylus，无需额外配置（需安装对应依赖）。

```bash
# 安装 Sass
npm install -D sass

# 安装 Less
npm install -D less

# 安装 Stylus
npm install -D stylus
```

**使用 Sass：**

```vue
<style scoped lang="scss">
$primary-color: #42b883;

.container {
  padding: 20px;

  .title {
    color: $primary-color;
    font-size: 24px;
  }

  &:hover {
    background: lighten($primary-color, 40%);
  }
}
</style>
```

---

### Demo 7：静态资源导入

```typescript
// 导入图片（URL 会被处理）
import logoUrl from './assets/logo.png'

// 导入 CSS
import './styles/main.css'

// 导入 JSON（自动解析为对象）
import data from './data.json'

// 导入 SVG 作为 Vue 组件（需安装 vite-plugin-svgr）
import Icon from './assets/icon.svg?component'

// 导入 Worker
import Worker from './worker.ts?worker'
const worker = new Worker()

// 导入 WASM
import initWasm from './calc.wasm?init'
```

---

## 实战 Demo

### 完整 Vue3 + TypeScript + Axios 项目

#### 1. 创建项目

```bash
npm create vite@latest vite-demo -- --template vue-ts
cd vite-demo
npm install
```

#### 2. 安装额外依赖

```bash
npm install axios vue-router@4 pinia
npm install -D sass @types/node
```

#### 3. 配置 Vite（`vite.config.ts`）

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  server: {
    port: 5173,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router', 'pinia'], // 第三方库单独打包
        },
      },
    },
  },
})
```

#### 4. 配置路由（`src/router/index.ts`）

```typescript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue'), // 懒加载
  },
  {
    path: '/users',
    name: 'Users',
    component: () => import('@/views/Users.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
```

#### 5. 配置 Axios 封装（`src/utils/request.ts`）

```typescript
import axios from 'axios'

const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    if (error.response?.status === 401) {
      // 未授权，跳转登录
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default request
```

#### 6. Pinia Store（`src/stores/user.ts`）

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // State
  const userInfo = ref<{ name: string; email: string } | null>(null)
  const isLoggedIn = ref(false)

  // Getters
  const userName = computed(() => userInfo.value?.name || '访客')

  // Actions
  function setUser(user: { name: string; email: string }) {
    userInfo.value = user
    isLoggedIn.value = true
  }

  function logout() {
    userInfo.value = null
    isLoggedIn.value = false
    localStorage.removeItem('token')
  }

  return { userInfo, isLoggedIn, userName, setUser, logout }
})
```

#### 7. 用户列表页面（`src/views/Users.vue`）

```vue
<template>
  <div class="users-page">
    <h1>用户列表</h1>
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="user-list">
      <div v-for="user in users" :key="user.id" class="user-card">
        <h3>{{ user.name }}</h3>
        <p>{{ user.email }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import request from '@/utils/request'

interface User {
  id: number
  name: string
  email: string
}

const users = ref<User[]>([])
const loading = ref(false)
const error = ref('')

async function fetchUsers() {
  loading.value = true
  error.value = ''
  try {
    const data = await request.get('/users')
    users.value = data
  } catch (err) {
    error.value = '获取用户列表失败'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchUsers()
})
</script>

<style scoped lang="scss">
.users-page {
  padding: 20px;

  h1 {
    color: #333;
    margin-bottom: 20px;
  }

  .user-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 16px;
  }

  .user-card {
    padding: 16px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    transition: box-shadow 0.2s;

    &:hover {
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    h3 {
      margin: 0 0 8px 0;
      color: #42b883;
    }

    p {
      margin: 0;
      color: #666;
    }
  }
}
</style>
```

#### 8. 入口文件（`src/main.ts`）

```typescript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './style.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')
```

#### 9. 根组件（`src/App.vue`）

```vue
<template>
  <div id="app">
    <nav class="navbar">
      <router-link to="/">首页</router-link>
      <router-link to="/about">关于</router-link>
      <router-link to="/users">用户列表</router-link>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.navbar {
  padding: 16px 24px;
  background: #333;
  display: flex;
  gap: 20px;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.navbar a.router-link-active {
  color: #42b883;
}

main {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
```

---

## 项目打包与部署

### 1. 项目打包

```bash
# 构建生产版本
npm run build

# 输出：
#   dist/                     # 构建输出目录
#   ├── assets/               # 静态资源（JS/CSS/图片，带 hash）
#   │   ├── index-xxx.js
#   │   ├── index-xxx.css
#   │   └── logo-xxx.png
#   ├── index.html            # 入口 HTML
#   └── vite.svg              # public 目录下的静态文件
```

### 2. 部署方式

#### 方式一：前后端分离（推荐）

将 `dist` 文件夹内容部署到 Nginx、Apache 等静态服务器。

**Nginx 配置示例：**

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/html/dist;
    index index.html;

    # 处理前端路由（SPA）
    location / {
        try_files $uri $uri/ /index.html;
    }

    # 静态资源缓存
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # 反向代理到后端 API
    location /api/ {
        proxy_pass http://localhost:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 方式二：前后端不分离（Spring Boot）

将 `dist` 文件夹内容复制到 Spring Boot 项目的 `src/main/resources/static/` 目录下。

```bash
# 前端构建后复制到 Spring Boot 项目
npm run build
cp -r dist/* ../springboot-project/src/main/resources/static/

# 然后正常打包 Spring Boot 项目
# mvn clean package
```

**Spring Boot 配置：**

```java
// 确保 Spring Boot 能处理前端路由
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        // 所有非 API 请求都返回 index.html
        registry.addViewController("/{path:[^\.]*}").setViewName("forward:/index.html");
    }
}
```

#### 方式三：Docker 部署

```dockerfile
# 构建阶段
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 运行阶段
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```bash
# 构建并运行
docker build -t my-vite-app .
docker run -d -p 80:80 my-vite-app
```

#### 方式四：Vercel / Netlify（云部署）

```bash
# 安装 Vercel CLI
npm install -g vercel

# 部署
vercel --prod
```

---

## 常用命令速查

| 命令 | 说明 |
|------|------|
| `npm create vite` | 创建新项目（交互式） |
| `npm create vite@latest my-app -- --template vue-ts` | 直接创建指定模板 |
| `npm install` | 安装所有依赖 |
| `npm install <pkg>` | 安装指定依赖 |
| `npm install -D <pkg>` | 安装开发依赖 |
| `npm run dev` | 启动开发服务器（默认 5173） |
| `npm run build` | 构建生产版本（输出 dist） |
| `npm run preview` | 预览生产构建 |
| `npm run lint` | 运行代码检查（需配置 ESLint） |
| `npx vite` | 直接运行 Vite（无需安装到项目） |

---

## 与 Webpack 对比

| 特性 | Vite | Webpack |
|------|------|---------|
| 冷启动速度 | ⚡ 极快（毫秒级） | 🐢 慢（秒级~分钟级） |
| 热更新速度 | ⚡ 毫秒级 | 🐢 秒级 |
| 配置复杂度 | 低（开箱即用） | 高（需大量配置） |
| 构建速度 | 快（Rollup） | 中等 |
| 生态插件 | 丰富（兼容 Rollup） | 非常丰富 |
| 适用场景 | 现代项目、快速开发 | 复杂项目、需要精细控制 |
| 学习曲线 | 平缓 | 陡峭 |

---

## 注意事项

1. **Node 版本**：确保 Node.js >= 18，否则部分功能可能异常
2. **环境变量**：只有以 `VITE_` 开头的变量会暴露到客户端代码
3. **路径别名**：修改 `vite.config.ts` 后，TypeScript 项目需同步更新 `tsconfig.json`
4. **public 目录**：`public/` 下的文件不会被构建处理，直接复制到 dist，引用时使用绝对路径 `/xxx`
5. **动态导入**：Vite 支持 `import()` 动态导入，可实现代码分割和懒加载
6. **SSR 支持**：Vite 支持服务端渲染，需额外配置
7. **库模式**：使用 `build.lib` 配置可将项目打包为 JS 库供他人使用

---

## 参考资源

- [Vite 官方中文文档](https://cn.vitejs.dev)
- [Vite GitHub](https://github.com/vitejs/vite)
- [Vue 3 文档](https://cn.vuejs.org/)
- [Pinia 文档](https://pinia.vuejs.org/)

---

*文档完成。祝你使用 Vite 开发愉快！⚡*
