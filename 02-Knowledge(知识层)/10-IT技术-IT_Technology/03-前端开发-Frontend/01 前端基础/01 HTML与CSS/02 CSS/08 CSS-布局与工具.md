---
title: CSS 布局与工具
domain: IT_Technology
tags:
  - CSS
  - 版心
  - 重置样式
  - 精灵图
  - 字体图标
  - Emmet
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[07 CSS-定位]]"
summary: CSS布局辅助概念包括版心设计、常用布局名词、重置默认样式（reset.css/normalize.css）、Emmet缩写语法、像素工具Pxcook、CSS精灵技术以及字体图标的使用。
---

## 八、布局

### 1. 版心

在 PC端网页中，一般都会有一个固定宽度且水平居中的盒子，来显示网页的主要内容，这是网页的**版心**。

版心的宽度一般是 960~1200像素之间。

版心可以是一个，也可以是多个。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732249120275-e11e94a2-34cf-448b-a26b-e042fe27f348.png)

### 2.常用布局名词

|   |   |
|---|---|
|**位置**|**说明**|
|顶部导航条|topbar|
|页头|header、 page-header|
|导航|nav、 navigator、 navbar|
|搜索框|search、 search-box|
|横幅、广告、宣传图|banner|
|主要内容|content、 main|
|侧边栏|aside、 sidebar|
|页脚|footer、 page-footer|

### 3. 重置默认样式

很多元素都有默认样式，比如：

1. p元素有默认的上下 margin。

2. h1~h6标题也有上下 margin，且字体加粗。

3. body元素有默认的 8px外边距。

4. 超链接有默认的文字颜色和下划线。

5. ul元素有默认的左 。

6. .......

在早期，元素默认样式，能够让我们快速的绘制网页，但如今网页的设计越来越复杂，内容越来越多，而且很精细，这些默认样式会给我们绘制页面带来麻烦；而且这些默认样式，在不同的浏览器上呈现出来的效果也不一样，所以我们需要重置这些默认样式。

#### 方案一：使用全局选择器

```css
* {
margin: 0;
padding: 0;
......
}
```

此种方法，在简单案例中可以用一下，但实际开发中不会使用，因为 *选择的是所有元素，而并不是所有的元素都有默认样式；而且我们重置时，有时候是需要做特定处理的，比如：想让a元素的文字是灰色，其他元素文字是蓝色。

#### 方案二：reset.css

选择到具有默认样式的元素，清空其默认的样式。

经过 reset后的网页，好似"一张白纸"，开发人员可根据设计稿，精细的去添加具体的样式。

#### 方案三：Normalize.css

Normalize.css是一种最新方案，它在清除默认样式的基础上，保留了一些有价值的默认样式。

官网地址： [http://necolas.github.io/normalize.css/](http://necolas.github.io/normalize.css/)

相对于reset.css，Normalize.css有如下优点：

1. 保护了有价值的默认样式，而不是完全去掉它们。
2. 为大部分HTML元素提供一般化的样式。
3. 新增对 HTML5 元素的设置。
4. 对并集选择器的使用比较谨慎，有效避免调试工具杂乱。

备注： Normalize.css的重置，和 reset.css相比，更加的温和，开发时可根据实际情况进行选择。

## Emmet 写法

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747066303059-14bf1a56-703d-46b2-be91-8074289e6ea4.png)

Emmet 是一种缩写语法，主要用于快速编写 HTML 和 CSS 代码。以下是一些常见的 Emmet 写法及其展开结果示例：

---

### 📄 HTML 示例

|   |   |   |
|---|---|---|
|Emmet 缩写|展开结果|中文说明|
|`div`|`<div></div>`|创建一个 div 元素|
|`.box`|`<div class="box"></div>`|创建一个 class 为 box 的 div|
|`#header`|`<div id="header"></div>`|创建一个 id 为 header 的 div|
|`ul>li*3`|`<ul><li></li><li></li><li></li></ul>`|创建一个包含 3 个 li 的 ul 列表|
|`div>h1+p`|`<div><h1></h1><p></p></div>`|div 中包含一个标题和一个段落|
|`nav>ul>li.item$*3`|`<nav><ul><li class="item1"></li>...</ul></nav>`|创建带编号类名的导航列表|
|`a[href="https://example.com"]`|`<a href="https://example.com"></a>`|创建带链接地址的超链接|
|`form:post>input:submit`|`<form method="post"><input type="submit"></form>`|创建一个 POST 表单，带提交按钮|
|`table>tr*2>td*3`|`<table><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>`|创建一个 2 行 3 列的表格结构|

---

### 🎨 CSS 示例

|   |   |   |
|---|---|---|
|Emmet 缩写|展开结果|中文说明|
|`m10`|`margin: 10px;`|设置外边距为 10px|
|`p20-10`|`padding: 20px 10px;`|设置上下 20px，左右 10px 内边距|
|`w100`|`width: 100px;`|设置宽度为 100px|
|`h50`|`height: 50px;`|设置高度为 50px|
|`bgc#ccc`|`background-color: #ccc;`|设置背景色为 #ccc|
|`pos:a`|`position: absolute;`|设置绝对定位|
|`d:f`|`display: flex;`|设置弹性布局|

---

### 🧱 完整页面结构示例

以下是一个典型的页面结构 Emmet 写法和展开结果，附带中文说明：

#### Emmet 写法

```css
html:5>header.header>h1{我的网站}^nav.nav>ul>li.nav-item$*3>a{导航 $}^^main.main>section.hero>h2{欢迎来到我的网站}+p{这里是介绍内容。}^^section.content>article*2>h3{文章标题 $}+p{这是第 $ 篇文章的内容。}^^footer.footer>p{版权所有 © 2025}
```

#### 展开后的 HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

  <!-- 页头区域 -->
  <header class="header">
    <h1>我的网站</h1>
  </header>

  <!-- 导航栏 -->
  <nav class="nav">
    <ul>
      <li class="nav-item1"><a href="#">导航 1</a></li>
      <li class="nav-item2"><a href="#">导航 2</a></li>
      <li class="nav-item3"><a href="#">导航 3</a></li>
    </ul>
  </nav>

  <!-- 主体内容 -->
  <main class="main">
    <!-- 顶部展示区域 -->
    <section class="hero">
      <h2>欢迎来到我的网站</h2>
      <p>这里是介绍内容。</p>
    </section>

    <!-- 内容区域：两篇文章 -->
    <section class="content">
      <article>
        <h3>文章标题 1</h3>
        <p>这是第 1 篇文章的内容。</p>
      </article>
      <article>
        <h3>文章标题 2</h3>
        <p>这是第 2 篇文章的内容。</p>
      </article>
    </section>
  </main>

  <!-- 页脚 -->
  <footer class="footer">
    <p>版权所有 © 2025</p>
  </footer>

</body>
</html>
```

---

你可以将这些 Emmet 缩写直接粘贴到 VS Code 中使用，输入后按 `Tab` 键快速展开结构。是否需要我再补充 JavaScript 中的 Emmet 写法支持？

## Pxcook

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747141215664-0568c926-9b82-4560-b3d3-ea35f714e321.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747141230756-644707fb-f780-4e58-acfc-1dc07581cd0d.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747141671129-a07ef3fd-ac81-430e-97d4-37c4a997227f.png)

## CSS精灵

移动的是整图、而不是子图

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747150501532-0a8730f2-17c0-4c59-880c-4225905149e8.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747150631596-8557d355-aebe-4722-8784-625ccf70cd49.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747150639654-d27084e3-d9e9-4353-a16e-bb280601ee00.png)

## 字体图标

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747151128781-2751089d-95a6-44b5-a4c1-6d65511e994c.png)

### 下载字体

[https://www.iconfont.cn/](https://www.iconfont.cn/)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747150653148-d45ffa12-f02d-4bca-b1b5-acc8ba260d50.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747151339479-86ee2bf2-25dc-41d8-ad13-47f05cff1892.png)

### 使用字体

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747150683584-60338fb6-4540-4e00-9b9f-8c9a51927efc.png)

### 上传矢量图

| 字体图标 | iconfont.cn 阿里巴巴矢量图标库 |
