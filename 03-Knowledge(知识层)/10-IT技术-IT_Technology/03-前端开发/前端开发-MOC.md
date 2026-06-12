---
title: 前端开发 MOC
domain: IT_Technology
tags: [MOC, 前端, JavaScript, Vue, React]
status: 稳定
created: 2026-05-07
updated: 2026-05-07
summary: "前端开发子域地图，覆盖 HTML/CSS/JS 基础、主流框架、工程化与性能优化"
---

# 前端开发

浏览器端用户界面工程，从 HTML/CSS/JS 三件套到现代框架工程化体系，关注用户体验与渲染性能。

## 学习路径

`HTML/CSS 基础` → `JavaScript 核心` → `框架（Vue/React）` → `工程化工具链` → `性能优化`

## 核心概念

| 概念 | 一句话定义 |
|------|-----------|
| DOM | 文档对象模型，JS 操作页面结构的接口层 |
| 事件循环 | JS 单线程的异步执行机制（宏/微任务队列） |
| 虚拟 DOM | 框架在内存中维护的 DOM 副本，diff 后再批量更新真实 DOM |
| 响应式 | 数据变化自动驱动视图更新的机制（Vue proxy / React setState） |
| 代码分割 | 按需加载 JS bundle，减少首屏体积（lazy load / dynamic import） |

## 关键知识点

### HTML / CSS
- 语义化标签与 SEO
- Flexbox / Grid 布局模型
- CSS 变量与 BEM 命名规范
- 响应式设计（媒体查询/容器查询）

### JavaScript 核心
- 原型链与继承（prototype / class）
- 闭包、作用域与 this 绑定
- Promise / async-await / 事件循环
- ES6+ 特性（解构/扩展/模块化/可选链）
- TypeScript 类型系统基础

### 框架
- **Vue 3**：Composition API、响应式原理（reactive/ref）、Pinia 状态管理
- **React**：Hooks（useState/useEffect/useMemo）、Fiber 架构、Redux/Zustand
- 路由（Vue Router / React Router）

![[Pasted image 20260524185308.png]]

### 工程化工具链
- Vite 构建与 HMR 原理
- ESLint / Prettier 代码规范
- 单元测试（Vitest/Jest）
- npm / pnpm 依赖管理

### 性能优化
- Core Web Vitals（LCP/FID/CLS）
- 首屏加载优化（SSR/SSG/懒加载）
- 图片优化（WebP/懒加载/CDN）
- 浏览器缓存策略（Cache-Control）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/03-前端开发"
WHERE file.name != "前端开发-MOC"
SORT updated DESC
```
