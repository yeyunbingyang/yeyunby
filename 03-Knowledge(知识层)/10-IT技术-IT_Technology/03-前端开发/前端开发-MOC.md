---
title: 前端开发 MOC
domain: IT_Technology
tags: [MOC, 前端, JavaScript, Vue, CSS, HTML]
status: 稳定
created: 2026-05-07
updated: 2026-07-05
summary: "前端开发子域地图(97篇)，覆盖HTML(10)/CSS(14)/JS(20+)/TypeScript/Vue2/Vue3/uni-app/工程化与最佳实践"
---

# 前端开发

浏览器端用户界面工程，从 HTML/CSS/JS 三件套到现代框架工程化体系。已建 **97 篇**笔记，是知识库最完整的技术子域之一。

## 子域导航

| 子域 | 笔数 | 关键内容 |
|------|------|----------|
| 01 前端基础 | 70+ | [[HTML-MOC\|HTML]](10篇)、[[CSS-MOC\|CSS]](14篇)、[[JS-MOC\|JavaScript]](20+篇)、TypeScript(2篇) |
| 02 前置知识 | 10+ | 环境准备(Node/npm/pnpm/Bun)、工程化脚手架(Vite)、HTTP请求、跨域、上线 |
| 03 前端框架 | 15+ | Vue2选项式API、Vue3组合式API、uni-app跨端 |
| 04 组件库 | 3 | Ant Design Vue、ECharts报表 |
| 05 解决方案 | 5+ | 若依脚手架、CSS预处理器(SCSS/UnoCSS)、Vue3企业级规范 |

## 学习路径

`HTML/CSS 基础` → `JavaScript 核心` → `TypeScript` → `框架（Vue2/Vue3）` → `工程化工具链` → `性能优化`

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
- [[HTML-MOC|HTML 知识地图]] — 10 篇笔记（基础语法 → 图片超链接 → 列表表格 → 表单 → H5新特性）
- [[CSS-MOC|CSS 知识地图]] — 14 篇笔记（基础语法 → 选择器 → 盒模型 → Flex弹性布局 → 响应式 → CSS3新增）
- [[CSS 预处理器]] / [[SCSS_SASS_深度指南]] — SCSS/SASS 深度使用
- [[UnoCSS基本使用详解]] — 原子化 CSS 方案

### JavaScript 核心
- [[JS-MOC|JS 知识地图]] — 20+ 篇（基础语法 → 变量类型 → 运算符 → 控制语句 → 对象/数组 → WebAPIs/DOM → ES6+）
- TypeScript 类型系统基础（2篇：快速上手 + 速查手册）

### 框架
- **Vue 2**（选项式API）：基础指令、计算属性、生命周期、组件通信、Vue-Router、Vuex、面经项目实战
- **Vue 3**（组合式API）：Composition API、Pinia、Vue Router、组件通信、存储机制
- **uni-app**：跨端开发，优医咨询项目实战（9篇）

### 工程化工具链
- Vite 构建与 HMR 原理
- npm / pnpm / nvm 依赖管理
- Bun 运行时
- json-server 本地 Mock 接口

### 性能优化
- Core Web Vitals（LCP/FID/CLS）
- 首屏加载优化（SSR/SSG/懒加载）
- 图片优化（WebP/懒加载/CDN）
- 浏览器缓存策略（Cache-Control）

---

## 本子域笔记

```dataview
TABLE summary, status, updated
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/03-前端开发"
WHERE file.name != "前端开发-MOC"
SORT updated DESC
```
