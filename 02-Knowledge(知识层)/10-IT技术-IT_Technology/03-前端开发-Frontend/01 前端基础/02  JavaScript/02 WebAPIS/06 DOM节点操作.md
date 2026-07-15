---
title: JS DOM 节点操作
domain: IT_Technology
tags:
  - JavaScript
  - WebAPIS
  - DOM
  - 节点操作
  - M端事件
status: 稳定
created: 2026-06-30
updated: 2026-06-30
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[JS-MOC]]"
  - "[[02 WebAPIS/01 DOM基础与元素操作]]"
  - "[[04 事件流和事件委托]]"
summary: DOM 节点操作包括父子兄弟节点的查找（parentNode/children/previousElementSibling）、创建插入（createElement/append/prepend）、删除（remove）、M端触屏事件（touchstart/touchmove/touchend）及 JS 插件使用。
---

# DOM 节点操作

## DOM 树

**DOM树：** DOM 将 HTML文档以树状结构直观的表现出来，我们称之为 DOM 树 或者 节点树

**节点（Node）** 是 DOM 树(节点树)中的单个点。包括文档本身、元素、文本以及注释都属于是节点。

- `元素节点`（重点）
  - 所有的标签 比如 body、 div
  - html 是根节点
- 属性节点
  - 所有的属性 比如 href
- 文本节点
  - 所有的文本

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747577410592-b34e034d-294a-4abe-92bc-5a731411d2f8.png)

## 查找节点

利用节点关系查找节点，返回的都是对象

- 父节点
- 子节点
- 兄弟节点

有了查找节点可以使我们选择元素更加方便

### 父节点

语法：

```js
元素.parentNode
```

```html
<body>
  <div class="pop">
    <a href="javascript:;" class="close"></a>
  </div>
  <script>
    // 点击关闭按钮可以关闭父盒子
    const closeBtn = document.querySelector('.close')
    // 利用孩子选取父节点,返回的也是一个元素对象
    console.log(closeBtn.parentNode)
    closeBtn.addEventListener('click', function () {
      this.parentNode.style.display = 'none'
    })
  </script>
</body>
```

### 子节点

**语法:**

```js
父元素.children
```

```html
<body>
  <ul>
    <li>我是第1个孩子</li>
    <li>我是第2个孩子</li>
    <li>我是第3个孩子</li>
    <li>我是第4个孩子</li>
  </ul>
  <script>
    // 1. 查询子节点
    const ul = document.querySelector('ul')
    console.log(ul.children)
  </script>
</body>
```

### 兄弟节点

```html
<body>
  <ul>
    <li>我是第1个孩子</li>
    <li>我是第2个孩子</li>
    <li>我是第3个孩子</li>
    <li>我是第4个孩子</li>
  </ul>
  <script>
    // 2. 查询兄弟节点
    const li2 = document.querySelector('ul li:nth-child(2)')
    console.log(li2.previousElementSibling) // 上一个兄弟
    console.log(li2.nextElementSibling)  // 下一个兄弟
    console.log(ul.children[0]) // 第一个孩子
    console.log(ul.children[2]) // 第三个孩子
  </script>
</body>
```

## 增加节点

很多情况下，我们需要在页面中增加元素

- 比如，点击发布按钮，可以新增一条信息

一般情况下，我们新增节点，按照如下操作：

- 创建一个新的节点
- 把创建的新的节点放入到指定的元素内部

1. 父元素最后一个子节点之后，插入节点元素

```js
element.append()
```

2. 父元素第一个子元素的之前，插入节点元素

```js
element.prepend()
```

如下代码演示：

```html
<body>
  <ul>
    <li>我是小li</li>
  </ul>
  <script>
    // 1. 创建节点
    const li = document.createElement('li')
    li.innerHTML = '我是放到后面的'
    console.log(li)

    // 2. 追加给父元素
    const ul = document.querySelector('ul')
    // 2.1 append 放到ul 的最后面 类似css的 after伪元素
    ul.append(li)
    // 2.2 prepend放到 ul 的最前面 类似css的 before伪元素
    const firstli = document.createElement('li')
    firstli.innerHTML = '我是放到前面的'
    ul.prepend(firstli)
  </script>
</body>
```

## 删除节点

若一个节点在页面中已不需要时，可以删除它

**语法：**

```js
element.remove()
```

1. 把对象从它所属的 DOM 树中删除
2. 删除节点和隐藏节点（display:none）有区别的：隐藏节点还是存在的，但是删除，则从 DOM 树中删除

```html
<body>
  <div class="remove">我要删除</div>
  <div class="none">我要隐藏</div>
  <script>
    // 1. 删除节点, remove 会从dom树中删除这个元素
    const remove = document.querySelector('.remove')
    remove.remove()

    // 2. display:none 隐藏元素，页面看不见，但是dom树中还存在这个标签
    const none = document.querySelector('.none')
    none.style.display = 'none'
  </script>
</body>
```

## M端事件

M端(移动端)有自己独特的地方。比如`触屏事件 touch`（也称触摸事件），Android 和 IOS都有。

touch 对象代表一个触摸点。触摸点可能是一根手指，也可能是一根触摸笔。触屏事件可响应用户手指（或触控笔）对屏幕或者触控板操作。

常见的触屏事件如下：

| 事件 | 说明 |
|------|------|
| `touchstart` | 手指触屏开始 |
| `touchmove` | 手指触屏滑动 |
| `touchend` | 手指触屏结束 |

```html
<body>
  <div class="box"></div>
  <script>
    // 触摸事件
    const box = document.querySelector('.box')
    // 1. 手指触屏开始事件 touchstart
    box.addEventListener('touchstart', function () {
      console.log('我开始摸了')
    })
    // 2. 手指触屏滑动事件 touchmove
    box.addEventListener('touchmove', function () {
      console.log('我一直摸')
    })
    // 3. 手指触屏结束事件  touchend
    box.addEventListener('touchend', function () {
      console.log('我摸完了')
    })
  </script>
</body>
```

## JS插件

插件: 就是别人写好的一些代码,我们只需要复制对应的代码,就可以直接实现对应的效果

学习插件的思路：

1. 看官网。了解这个插件可以完成什么需求 [https://www.swiper.com.cn/](https://www.swiper.com.cn/)
2. 查看基本使用流程 。 [https://www.swiper.com.cn/usage/index.html](https://www.swiper.com.cn/usage/index.html)
3. 写个小demo。看在线演示,找到符合自己需求的demo [https://www.swiper.com.cn/demo/index.html](https://www.swiper.com.cn/demo/index.html)
4. 应用的开发中。

### AlloyFinger

AlloyFinger 是腾讯 AlloyTeam 团队开源的超轻量级 Web 手势插件，为元素注册各种手势事件

github地址：[https://github.com/AlloyTeam/AlloyFinger](https://github.com/AlloyTeam/AlloyFinger)

使用步骤：

1. 下载js库：[http://alloyteam.github.io/AlloyFinger/alloy_finger.js](http://alloyteam.github.io/AlloyFinger/alloy_finger.js)
2. 将 AlloyFinger 库引入当前文件：`<script src="alloy_finger.js">`
3. 配置

```js
new AlloyFinger(element, {  // element 是给哪个元素做滑动事件
  swipe: function (e) {
    // 滑动的时候要做的事情 e.direction 可以判断上下左右滑动 Left  Right 等
  }
})
```

> **思想转变（相当重要）**：本次案例，我们尽量减少dom操作，采取`操作数据`的形式，为了后期Vue做铺垫。增加和删除都是针对于`数组的操作`，然后根据`数组数据渲染页面`（数据驱动视图）。事件委托的两个重要作用：1. 减少了注册次数 2. 给新增元素注册事件。
