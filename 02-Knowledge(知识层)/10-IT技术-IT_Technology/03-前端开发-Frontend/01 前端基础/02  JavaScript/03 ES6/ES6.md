---
title: ES6+ 新特性
domain: IT_Technology
tags:
  - JavaScript
  - ES6
  - Promise
  - Async
  - 模块化
status: 稳定
created: 2026-06-30
updated: 2026-06-30
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[JS-MOC]]"
  - "[[02 变量与数据类型]]"
  - "[[03 运算符与表达式]]"
summary: ES6+ 核心新特性包括 Promise 异步编程、Async/Await 语法糖、ES Module 模块化导入导出机制。let/const/解构/箭头函数等基础语法见 JS 基础篇。
---

# ES6+ 新特性

- ECMAScript（ES） 是规范、 JavaScript 是 ES 的实现
- ES6 的第一个版本在 2015 年 6 月发布，正式名称是《ECMAScript 2015 标准》（简称 ES2015）
- ES6 指是 5.1 版以后的 JavaScript 的下一代标准，涵盖了 ES2015、ES2016、ES2017 等等

## 1. let 与 const

`let` 和 `const` 的详细用法见 [[02 变量与数据类型]]，该篇涵盖了：
- `let` 块作用域、禁止重复声明、无变量提升
- `const` 声明常量、引用类型内容可变
- `var` 对比及作用域问题

## 2. 解构赋值

数组解构和对象解构的详细用法见 [[03 运算符与表达式]] 的「特殊运算符 > `[] {}`【接收赋值】」章节。

## 3. 链判断（?.）

可选链运算符 `?.` 的详细用法见 [[03 运算符与表达式]] 的「特殊运算符 > `??` 与 `?.`」章节。

## 4. 参数默认值

函数参数默认值的详细用法见 [[05 对象类型（上）函数]] 的「Function > 默认参数」章节。

## 5. 箭头函数

箭头函数的详细用法见 [[05 对象类型（上）函数]] 的「Function > 箭头函数」章节。

## 6. 模板字符串

模板字符串的详细用法见 [[02 变量与数据类型]] 的「基本类型 > string > 模板字符串」章节。

## 7. Promise

代表 `异步对象`，类似 Java 中的 `CompletableFuture`

**Promise** 是现代 JavaScript 中异步编程的基础，是一个**由异步函数返回**的可以向我们指示当前操作所处的状态的对象。在 Promise 返回给调用者的时候，操作往往还没有完成，但 **Promise 对象可以让我们操作最终完成时对其进行处理（无论成功还是失败）**

fetch 是浏览器支持从远程获取数据的一个函数，这个函数返回的就是 `Promise 对象`

```js
const fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json"
);

console.log(fetchPromise);

fetchPromise.then((response) => { //返回Response对象
  console.log(`已收到响应：${response.status}`);
});

console.log("已发送请求……");
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432862569-19f99c72-faff-4826-be77-58df21efef4d.png "null")

### 7.1. fetch api

fetch 是浏览器支持从远程获取数据的一个函数，这个函数返回的就是 `Promise 对象`

fetch() 是一个全局方法，用于在 JavaScript 中发起 HTTP 请求。它是 XMLHttpRequest 的更强大和灵活的替代方案

```js
const fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

console.log(fetchPromise);

fetchPromise.then((response) => {
  console.log(`已收到响应：${response.status}`);
});

console.log("已发送请求……");
// promise.then();   // 操作成功以后
// promise.catch();  // 操作失败以后
```

**通过 fetch() API 得到一个 Response 对象；**

- **response.status**： 读取响应状态码
- **response.json()**：读取响应体 json 数据；（**这也是个异步对象**）

```js
const fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

fetchPromise.then((response) => {//返回Response对象
  const jsonPromise = response.json();//获取读取响应体json数据
  jsonPromise.then((json) => { 
    console.log(json[0].name);
  });
});
```

### 7.2. Promise 状态

首先，Promise 有三种状态：

- **待定（pending）**：初始状态，既没有被兑现，也没有被拒绝。这是调用 fetch() 返回 Promise 时的状态，此时请求还在进行中。
- **已兑现（fulfilled）**：意味着操作成功完成。当 Promise 完成时，它的 then() 处理函数被调用。
- **已拒绝（rejected）**：意味着操作失败。当一个 Promise 失败时，它的 **catch()** 处理函数被调用。

### 7.3. 自定义 Promise 对象

```js
const promise = new Promise((resolve, reject) => {
  // 执行异步操作
  if (/* 异步操作成功 */) {
    resolve(value);// 调用 resolve，代表 Promise 将返回成功的结果
  } else {
    reject(error);// 调用 reject，代表 Promise 会返回失败结果
  }
});
```

改造老式 API 示例：

```js
let get = function (url, data) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: url,
            type: "GET",
            data: data,
            success(result) {
                resolve(result);
            },
            error(error) {
                reject(error);
            }
        });
    })
}
```

## 8. Async 函数

简化 promise 开发异步代码

**async function** 声明创建一个绑定到给定名称的新异步函数。函数体内允许使用 await 关键字，这使得我们可以**更简洁地编写基于 promise 的异步代码**，并且**避免了显式地配置 promise 链**的需要。

- `async 函数`是使用`async关键字声明的函数`。async 函数是 [AsyncFunction](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction) 构造函数的实例，并且其中允许使用 await 关键字。
- `async 和 await` 关键字让我们可以用一种更简洁的方式写出基于 [Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise) 的异步行为，而无需刻意地链式调用 promise。
- `async 函数` 返回的还是 `Promise对象`

**普通函数快速包装异步代码**

```js
async function func1() {
    //业务、计算
    let x = 101;
    if (x % 2 === 0) {
        return x; //正常返回
    } else {
        throw new Error("x不是偶数") //异常返回
    }
}

func1().then(data => console.log("then", data)).catch(err => console.log("err", err))
```

在异步函数中，你可以在调用一个返回 Promise 的函数之前使用 **await** 关键字。这使得代码在该点上等待，直到 Promise 被完成，这时 Promise 的响应被当作返回值，或者被拒绝的响应被作为错误抛出。

**转同步操作**

```js
async function fetchProducts() {
  try {
    // 在这一行之后，我们的函数将等待 `fetch()` 调用完成
    // 调用 `fetch()` 将返回一个"响应"或抛出一个错误
    const response = await fetch(
      "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
    );
    if (!response.ok) {
      throw new Error(`HTTP 请求错误：${response.status}`);
    }
    // 在这一行之后，我们的函数将等待 `response.json()` 的调用完成
    // `response.json()` 调用将返回 JSON 对象或抛出一个错误
    const json = await response.json();
    console.log(json[0].name);
  } catch (error) {
    console.error(`无法获取产品列表：${error}`);
  }
}

fetchProducts();
```

```js
let url = "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json";
async function fetchProducts() {
    let promise1 = await fetch(url);//返回Response对象
    let promise2 = await promise1.json();//获取读取响应体json数据
    console.log('promise1', promise1)
    console.log('promise2', promise2)
}
fetchProducts();
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432862717-ad8492fa-8ebf-4037-afd7-029b062a4d70.png "null")

## 9. 模块化

**将 JavaScript 程序拆分为可按需导入的单独模块**的机制。Node.js 已经提供这个能力很长时间了，还有很多的 JavaScript 库和框架已经开始了模块的使用（例如，[CommonJS](https://en.wikipedia.org/wiki/CommonJS) 和基于 [AMD](https://github.com/amdjs/amdjs-api/blob/master/AMD.md) 的其他模块系统 如 [RequireJS](https://requirejs.org/)，以及最新的 [Webpack](https://webpack.github.io/) 和 [Babel](https://babeljs.io/)）。

好消息是，最新的浏览器开始原生支持模块功能了。

### 9.1. 工程架构

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432862780-25786bbd-5af7-48b0-9fc1-bd571f950f48.png "null")

### 9.2. index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="main.js" type="module"/>
</head>

<body>
<h1>模块化测试</h1>

</body>

</html>
```

### 9.3. user.js

放在 `libs/user.js`

```js
const user = {
    username: "张三",
    age: 18
}

const isAdult = (age) => {
    if (age > 18) {
        console.log("成年人")
    } else {
        console.log("未成年")
    }
}

export {user, isAdult}

// Java 怎么模块化；
// 1、 druid.jar
// 2、import 导入类

// JS 模块化；
// 1、 xxx.js
// 2、 xxx.js 暴露功能；
// 3、import 导入 xxx.js 的功能
// xxx.js 暴露的功能，别人才能导入
```

### 9.4. main.js

```js
// 所有的功能不用写在一个JS中
import {user, isAdult} from './libs/user.js'

alert("当前用户：" + user.username)

isAdult(user.age);
```
