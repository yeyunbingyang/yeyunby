---
title: CSS 盒模型
domain: IT_Technology
tags:
  - CSS
  - 盒模型
  - margin
  - padding
  - border
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[03 CSS-常用属性]]"
  - "[[05 CSS-处理细节]]"
summary: CSS盒模型由content、padding、border、margin四层构成，核心包括显示模式（块/行内/行内块）、各部分属性、margin塌陷与合并、圆角与阴影。
---

## 五、CSS盒子模型

### 1.CSS长度单位

1. px：像素。

2. em：相对元素 font-size的倍数。

3. rem：相对根字体大小，html标签就是根。

4. % ：相对父元素计算。

注意： CSS中设置长度，必须加单位，否则样式无效！

### 2.元素的显示模式

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747065098847-f119639e-20e3-44f9-ba47-581759a31886.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747065121956-813d7cb6-60a2-4055-9264-44083b6fe1b8.png)

**块元素（block）**

又称：块级元素

特点：

1. 在页面中**独占一行**，不会与任何元素共用一行，是从上到下排列的。

2. 默认宽度：撑满**父元素**。

3. 默认高度：由**内容**撑开。

4. **可以**通过 CSS设置宽高。

**行内元素（inline）**

又称：内联元素

特点:

1. 在页面中**不独占一行**，一行中不能容纳下的行内元素，会在下一行继续从左到右排列。

2. 默认宽度：由**内容**撑开。

3. 默认高度：由**内容**撑开。

4. **无法**通过 CSS设置宽高。

**行内块元素（inline-block）**

又称：内联块元素

特点：

1. 在页面中**不独占一行**，一行中不能容纳下的行内元素，会在下一行继续从左到右排列。

2. 默认宽度：由**内容**撑开。

3. 默认高度：由**内容**撑开。

4. **可以**通过 CSS设置宽高。

**注意：**元素早期只分为：**行内元素**、**块级元素**，区分条件也只有一条："是否独占一行"，如果按照这种分类方式，行内块元素应该算作行内元素。

### 3.总结各元素的显示模式

**块元素（block）**

1. 主体结构标签： `<html>`、 `<body>`

2. 排版标签： `<h1>` ~ `<h6>`、 `<hr>`、 `<p>`、 `<pre>`、 `<div>`

3. 列表标签： `<ul>`、 `<ol>`、 `<li>`、 `<dl>`、 `<dt>`、 `<dd>`

4. 表格相关标签： `<table>`、 `<tbody>`、 `<thead>`、 `<tfoot>`、 `<tr>`、`<caption>`

5. `<form>` 与 `<option>`

**行内元素（inline）**

1. 文本标签： `<br>`⭐、 `<em>`、 `<strong>`、 `<sup>`、 `<sub>`、 `<del>`、 `<ins>`

2. `<a>` 与 `<label>`

**行内块元素（inline-block）**

1. 图片： `<img>`

2. 单元格： `<td>`、 `<th>`

3. 表单控件： `<input>`、 `<textarea>`、 `<select>`、 `<button>`

4. 框架标签： `<iframe>`


### 4.修改元素的显示模式

通过CSS中的 display属性可以修改元素的默认显示模式，常用值如下：

|   |   |
|---|---|
|**值**|**描述**|
|none|元素会被**隐藏**。|
|block|元素将作为**块级元素**显示。|
|inline|元素将作为**内联元素**显示。|
|inline-block|元素将作为**行内块元素**显示。|

### 5.盒子模型的组成

CSS会把所有的HTML 元素都看成一个**盒子**，所有的样式也都是基于这个盒子。

1. **margin（外边距）**：盒子与外界的距离。

2. **border（边框）**：盒子的边框。

3. **padding（内边距）**：紧贴内容的补白区域。

4. **content（内容）：**元素中的文本或后代元素都是它的内容。

盒子是边框及以内。

外m 盒子外 【元素之间】

内p 盒子内 【元素内容】

图示如下

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732252286288-23592fd1-42ce-4f9f-a628-94fbf79b198f.png)

盒子的大小 = content + 左右 padding + 左右 border 。

注意：外边距 margin不会影响盒子的大小，但会影响盒子的位置。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747143245345-1ccb435a-dac0-4e1b-8538-149a4df6f9c5.png)

### 6.盒子内容区（content）

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|width|设置内容区域宽度|长度|
|max-width|设置内容区域的最大宽度|长度|
|min-width|设置内容区域的最小宽度|长度|
|height|设置内容区域的高度|长度|
|max-height|设置内容区域的最大高度|长度|
|min-height|设置内容区域的最小高度|长度|

**注意：**

max-width、 min-width一般不与 width一起使用。

max-height、 min-height一般不与 height一起使用。

### 7.关于默认宽度

所谓的默认宽度，就是**不设置**width**属性时**，元素所呈现出来的宽度。

**总宽度** = 父的 content— 自身的左右 margin。

**内容区的宽度** = 父的 content— 自身的左右 margin— 自身的左右 border— 自身的左右padding。

### 8.盒子内边距（padding）

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|padding-top|上内边距|长度|
|padding-right|右内边距|长度|
|padding-bottom|下内边距|长度|
|padding-left|左内边距|长度|
|padding|复合属性|长度，可以设置 1~4个值|

padding复合属性的使用规则

1. padding:10px; 四个方向内边距都是 10px。

2. padding: 10px20px; 上 10px，左右 20px。（上下、左右）

3. padding:10px20px30px; 上 10px，左右 20px，下 30px。（上、左右、下）

4. padding:10px 20px 30px 40px;上 10px，右 20px，下 30px，左 40px。（上、右、下、左）

**注意点：**

1. padding的值不能为负数。

2. **行内元素** 的 左右内边距是没问题的，上下内边距不能完美的设置。

3. **块级元素**、**行内块元素**，四个方向**内边距**都可以完美设置。

### 9.盒子边框（border）

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|border-style|边框线风格，复合了四个方向的边框风格|none：默认值；solid：实线；dashed：虚线；dotted：点线；double：双实线|
|border-width|边框线宽度，复合了四个方向的边框宽度|长度，默认 3px|
|border-color|边框线颜色，复合了四个方向的边框颜色|颜色，默认黑色|
|border|复合属性|值没有顺序和数量要求。|
|border-left / border-right / border-top / border-bottom|分别设置各个方向的边框，每个方向有 style/width/color 三个子属性|同上|

边框相关属性共 20个。

border-style 、 border-width、 border-color其实也是复合属性。

### 10.盒子外边距（**margin**）

不会影响盒子大小、盒子与外界的距离

版心居中：设置左右magin相等、auto

盒子m 网页宽-盒子宽

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|margin-left|**左**外边距|CSS中的长度值|
|margin-right|**右**外边距|CSS中的长度值|
|margin-top|**上**外边距|CSS中的长度值|
|margin-bottom|**下**外边距|CSS中的长度值|
|margin|复合属性，可以写 1~4个值，规律同 padding（顺时针）|CSS中的长度值|

#### 10.1 margin注意事项⭐

1. 子元素的 margin，是参考父元素的 content计算的。（因为是父亲的 content中承装着子元素）

2. 上 margin、左 margin：影响自己的位置；下 margin、右 margin：影响后面兄弟元素的位置。

3. 块级元素、行内块元素，均可以完美地设置四个方向的 margin；但**行内元素，左右 margin 可以完美设置，上下 margin 设置无效。**

4. margin 的值也可以是 auto，如果给一个**块级元素**设置左右 margin都为 auto，该块级元素会在父元素中水平居中。

5. margin的值可以是负值。

#### 10.2 margin塌陷问题

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144305408-cd959ce7-256f-4cce-b71e-0c3af12182bb.png)

**什么是margin 塌陷？**

第一个子元素的**上**会作用在父元素上，最后一个子元素的**下**margin会作用在父元素上。

如何解决margin 塌陷？

- 方案一： 给父元素设置不为 0 的 padding。【推荐】
- 方案二： 给父元素设置宽度不为 0 的 border。
- 方案三：给父元素设置 css 样式 overflow:hidden 【推荐】

#### 10.3 margin合并问题

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144285878-89834c82-1ba7-4c89-9100-6e7e165ca685.png)

**什么是margin 合并？**

上面兄弟元素的**下外边距**和下面兄弟元素的**上外边距**会合并，取一个最大的值，而不是相加。

#### 如何解决 margin合并？

无需解决，布局的时候上下的兄弟元素，只给一个设置上下外边距就可以了。

#### 10.4 行内元素的 内外边距问题

行内元素相当于文本进行设置

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144524010-e8001cf6-6f47-47ce-a6f3-d926eea44cdb.png)

### 圆角

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144820122-a36652f8-21e1-4f1d-87fe-11d76302d0b8.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144836308-bdc8bf5b-10d7-4100-8495-5aca0bc4eb34.png)

### 阴影

平常都是直接在设计稿复制

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747144863410-1dcad426-5075-423b-9821-005f2d2d5a91.png)
