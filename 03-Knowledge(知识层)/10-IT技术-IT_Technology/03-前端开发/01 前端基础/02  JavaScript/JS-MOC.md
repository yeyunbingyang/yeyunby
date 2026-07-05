---
title: JavaScript 知识地图
domain: IT_Technology
tags:
  - JavaScript
  - 前端基础
  - MOC
status: 稳定
created: 2026-06-30
updated: 2026-06-30
source: ""
related:
  - "[[CSS-MOC]]"
summary: JavaScript 是前端交互的核心语言。以下笔记按学习路径组织，从基础语法到 WebAPI、ES6+ 新特性，涵盖变量/函数/对象/DOM/BOM/异步/模块化等内容。
---

# JavaScript 知识地图

## 学习路径

```mermaid
flowchart LR
  基础语法 --> 变量与数据类型
  变量与数据类型 --> 运算符
  运算符 --> 控制语句
  控制语句 --> 函数
  函数 --> 数组与对象
  数组与对象 --> DOM基础
  DOM基础 --> 定时器
  定时器 --> 事件监听
  事件监听 --> 事件流
  事件流 --> DOM节点操作
  DOM节点操作 --> BOM与存储
  BOM与存储 --> 正则
  正则 --> 综合实战
  综合实战 --> ES6
```

## 笔记列表

### 第一部分：JS 基础

| # | 笔记 | 内容 | 状态 |
|---|------|------|------|
| 1 | [[01 JS基础/01 介绍与基础语法]] | JS 简介、引入方式（内部/外部）、书写语法、3 种输出语句、动态类型 | 稳定 |
| 2 | [[01 JS基础/02 变量与数据类型]] | let/const/var、7 种基本类型（undefined/null/string/number/bigint/boolean/symbol）、truthy/falsy | 稳定 |
| 3 | [[01 JS基础/03 运算符与表达式]] | 一般运算符、=== / \|\| / ?? / ?. / ... / 解构赋值 | 稳定 |
| 4 | [[01 JS基础/04 控制语句]] | if-else/switch/for/while + for...in / for...of / try...catch | 稳定 |
| 5 | [[01 JS基础/05 对象类型（上）函数]] | Function 定义/调用/匿名/箭头/作用域/闭包/let-var 作用域差异 | 稳定 |
| 6 | [[01 JS基础/06 对象类型（下）数组与对象]] | Array（API/map-filter-forEach）+ Object（语法/this/原型继承/JSON） | 稳定 |

### 第二部分：Web APIs

| # | 笔记 | 内容 | 状态 |
|---|------|------|------|
| 7 | [[02 WebAPIS/01 DOM基础与元素操作]] | DOM 简介、获取元素（querySelector）、操作内容/样式/表单/自定义属性 | 稳定 |
| 8 | [[02 WebAPIS/02 定时器]] | setInterval/clearInterval + 轮播图案例 | 稳定 |
| 9 | [[02 WebAPIS/03 事件监听]] | 事件监听/事件类型（鼠标/焦点/键盘/input）/事件对象/this/排他思想 | 稳定 |
| 10 | [[02 WebAPIS/04 事件流和事件委托]] | 捕获/冒泡/阻止冒泡/事件委托/阻止默认行为/其他事件/元素尺寸位置 | 稳定 |
| 11 | [[02 WebAPIS/05 日期对象]] | Date 实例化/格式化方法（getFullYear等）/toLocaleString/时间戳 | 稳定 |
| 12 | [[02 WebAPIS/06 DOM节点操作]] | 父子兄弟节点查找/增删节点/M端事件（touch）/JS插件 | 稳定 |
| 13 | [[02 WebAPIS/07 BOM与本地存储]] | window/location/navigator/history/localStorage/sessionStorage/JSON存储 | 稳定 |
| 14 | [[02 WebAPIS/08 正则表达式]] | 正则语法/元字符（边界/量词/范围/字符类）/替换replace/修饰符 | 稳定 |
| 15 | [[02 WebAPIS/09 综合实战]] | 放大镜效果/商品详情页tab切换/返回顶部等实战 | 稳定 |

### 第三部分：ES6+

| # | 笔记 | 内容 | 状态 |
|---|------|------|------|
| 16 | [[03 ES6/ES6]] | let/const 块作用域、解构赋值、链判断 ?.、箭头函数、模板字符串、Promise、Async/Await、模块化 | 稳定 |

## 核心原则

- **动态类型**：JS 是弱类型语言，变量无类型、值有类型
- **函数一等公民**：函数可作为参数、返回值、赋值给变量
- **原型继承**：JS 的继承发生在对象之间，通过原型链实现
- **异步优先**：事件监听、定时器、Fetch/Promise 都是异步模式

## 相关资源

- [MDN JavaScript 文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
- [MDN Web APIs](https://developer.mozilla.org/zh-CN/docs/Web/API)
- [ES6 入门教程 - 阮一峰](https://es6.ruanyifeng.com/)

```dataview
TABLE summary, status, updated
FROM "KnowledgeBase/03-Knowledge/10-IT技术-IT_Technology/03-前端开发/01 前端基础/02  JavaScript"
WHERE contains(tags, "JavaScript") AND file.name != "JS-MOC"
SORT file.name ASC
```
