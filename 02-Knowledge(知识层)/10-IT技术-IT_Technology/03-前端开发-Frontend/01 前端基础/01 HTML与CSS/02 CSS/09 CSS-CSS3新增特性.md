---
title: CSS3 新增特性
domain: IT_Technology
tags:
  - CSS
  - CSS3
  - box-sizing
  - 背景属性
  - 边框
  - 渐变
  - 文本
  - 3D
  - web字体
  - 媒体查询
status: 稳定
created: 2026-06-26
updated: 2026-06-30
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[04 CSS-盒模型]]"
  - "[[10 CSS-Flex弹性布局]]"
  - "[[11 CSS-多列布局与BFC]]"
  - "[[12 CSS高级特效]]"
  - "[[14 响应式]]"
summary: CSS3 在 CSS2 基础上新增了私有前缀、新长度单位、增强盒模型/背景/边框/文本属性、渐变、Web字体、2D/3D变换、过渡/动画升级、媒体查询等特性。Flex布局见[[10 CSS-Flex弹性布局]]，多列布局与BFC见[[11 CSS-多列布局与BFC]]，实战案例见[[12 CSS高级特效]]。
---

# CSS3 新增特性

> 参考 PDF：[CSS3笔记.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/40487410/1733034542304-4277568f-86dd-4e3b-86f2-0da8d93ff1f3.pdf)

---

## 一、CSS3 简介

### 1.1 CSS3 概述

CSS3 是 CSS2 的升级版本，它在 CSS2 的基础上，新增了很多强大的新功能，从而解决一些实际面临的问题。

CSS3 在未来会按照**模块化**的方式去发展：[https://www.w3.org/Style/CSS/current-work.html](https://www.w3.org/Style/CSS/current-work.html)

CSS3 的新特性如下：

- 新增了**更加实用的选择器**，例如：动态伪类选择器、目标伪类选择器、伪元素选择器等等。
- 新增了**更好的视觉效果**，例如：圆角、阴影、渐变等。
- 新增了**丰富的背景效果**，例如：支持多个背景图片，同时新增了若干个背景相关的属性。
- 新增了**全新的布局方案** —— 弹性盒子。
- 新增了 **Web 字体**，可以显示用户电脑上没有安装的字体。
- 增强了**颜色**，例如：HSL、HSLA、RGBA 几种新的颜色模式，新增 `opacity` 属性来控制透明度。
- 增加了 **2D 和 3D 变换**，例如：旋转、扭曲、缩放、位移等。
- 增加**动画与过渡效果**，让效果的变换更具流线性、平滑性。

### 1.2 CSS3 私有前缀

#### 什么是私有前缀

如下代码中的 `-webkit-` 就是私有前缀：

```css
div {
    width: 400px;
    height: 400px;
    -webkit-border-radius: 20px;
}
```

#### 为什么要有私有前缀

W3C 标准所提出的某个 CSS 特性，在被浏览器正式支持之前，浏览器厂商会根据浏览器的内核，使用私有前缀来测试该 CSS 特性，在浏览器正式支持该 CSS 特性后，就不需要私有前缀了。

查询 CSS3 兼容性的网站：[https://caniuse.com/](https://caniuse.com/)

#### 常见浏览器私有前缀

| 浏览器 | 私有前缀 |
|--------|----------|
| Chrome | `-webkit-` |
| Safari | `-webkit-` |
| Firefox | `-moz-` |
| Edge | `-webkit-` |
| 旧 Opera | `-o-` |
| 旧 IE | `-ms-` |

完整的多前缀写法示例：

```css
-webkit-border-radius: 20px;
-moz-border-radius: 20px;
-ms-border-radius: 20px;
-o-border-radius: 20px;
border-radius: 20px;
```

> **注意**：编码时不用过于关注浏览器私有前缀。常用 CSS3 新特性主流浏览器都是支持的，即便是为了老浏览器而加前缀，我们也可以借助现代的构建工具（如 Autoprefixer）去帮我们添加私有前缀。

---

## 二、CSS3 基本语法

### 2.1 新增长度单位

| 单位 | 含义 |
|------|------|
| `rem` | 根元素字体大小的倍数，只与根元素字体大小有关 |
| `vw` | 视口宽度的百分之多少，`10vw` 就是视口宽度的 10% |
| `vh` | 视口高度的百分之多少，`10vh` 就是视口高度的 10% |
| `vmax` | 视口宽高中大的那个的百分之多少（了解即可） |
| `vmin` | 视口宽高中小的那个的百分之多少（了解即可） |

### 2.2 新增颜色设置方式

CSS3 新增了三种颜色设置方式：`rgba`、`hsl`、`hsla`，在 [[03 CSS-常用属性]] 中已详细讲解，此处略过。

### 2.3 新增选择器

CSS3 新增的选择器有：动态伪类、目标伪类、语言伪类、UI 伪类、结构伪类、否定伪类、伪元素；这些在 [[02 CSS-选择器]] 中已详细讲解，此处略过。

---

## 三、CSS3 新增盒模型相关属性

### 3.1 `box-sizing` 怪异盒模型

使用 `box-sizing` 属性可以设置盒模型的两种类型：

| 可选值 | 含义 |
|--------|------|
| `content-box` | `width` 和 `height` 设置的是盒子内容区的大小（默认值） |
| `border-box` | `width` 和 `height` 设置的是盒子总大小（怪异盒模型） |

### 3.2 `resize` 调整盒子大小

使用 `resize` 属性可以控制是否允许用户调节元素尺寸。

| 值 | 含义 |
|----|------|
| `none` | 不允许用户调整元素大小（默认） |
| `both` | 用户可以调节元素的宽度和高度 |
| `horizontal` | 用户可以调节元素的宽度 |
| `vertical` | 用户可以调节元素的高度 |

### 3.3 `box-shadow` 盒子阴影

使用 `box-shadow` 属性为盒子添加阴影。

**语法**：

```css
box-shadow: h-shadow v-shadow blur spread color inset;
```

**各个值的含义**：

| 值 | 含义 |
|----|------|
| `h-shadow` | 水平阴影的位置，必须填写，可以为负值 |
| `v-shadow` | 垂直阴影的位置，必须填写，可以为负值 |
| `blur` | 可选，模糊距离 |
| `spread` | 可选，阴影的外延值 |
| `color` | 可选，阴影的颜色 |
| `inset` | 可选，将外部阴影改为内部阴影 |

默认值：`box-shadow: none` 表示没有阴影。

**示例**：

```css
/* 写两个值，含义：水平位置、垂直位置 */
box-shadow: 10px 10px;

/* 写三个值，含义：水平位置、垂直位置、颜色 */
box-shadow: 10px 10px red;

/* 写三个值，含义：水平位置、垂直位置、模糊值 */
box-shadow: 10px 10px 10px;

/* 写四个值，含义：水平位置、垂直位置、模糊值、颜色 */
box-shadow: 10px 10px 10px red;

/* 写五个值，含义：水平位置、垂直位置、模糊值、外延值、颜色 */
box-shadow: 10px 10px 10px 10px blue;

/* 写六个值，含义：水平位置、垂直位置、模糊值、外延值、颜色、内阴影 */
box-shadow: 10px 10px 20px 3px blue inset;
```

### 3.4 `opacity` 不透明度

`opacity` 属性能为整个元素添加透明效果，值是 0 到 1 之间的小数，0 是完全透明，1 表示完全不透明。

**`opacity` 与 `rgba` 的区别**：

- `opacity` 是一个属性，设置的是整个元素（包括元素里的内容）的不透明度。
- `rgba` 是颜色的设置方式，用于设置颜色，它的透明度仅仅是调整颜色的透明度。

---

## 四、CSS3 新增背景属性

### 4.1 `background-origin`

作用：设置背景图的原点。

| 值 | 含义 |
|----|------|
| `padding-box` | 从 padding 区域开始显示背景图像（默认值） |
| `border-box` | 从 border 区域开始显示背景图像 |
| `content-box` | 从 content 区域开始显示背景图像 |

### 4.2 `background-clip`

作用：设置背景图的向外裁剪的区域。

| 值 | 含义 |
|----|------|
| `border-box` | 从 border 区域开始向外裁剪背景（默认值） |
| `padding-box` | 从 padding 区域开始向外裁剪背景 |
| `content-box` | 从 content 区域开始向外裁剪背景 |
| `text` | 背景图只呈现在文字上 |

> **注意**：若值为 `text`，那么 `background-clip` 要加上 `-webkit-` 前缀。

### 4.3 `background-size`

作用：设置背景图的尺寸。

| 值 | 含义 |
|----|------|
| 长度值 | 用长度值指定背景图片大小，不允许负值。如 `background-size: 300px 200px;` |
| 百分比 | 用百分比指定背景图片大小，不允许负值。如 `background-size: 100% 100%;` |
| `auto` | 背景图片的真实大小（默认值） |
| `contain` | 将背景图片等比缩放，使背景图片的宽或高与容器相等，完整包含在容器内（可能造成部分区域无背景） |
| `cover` | 将背景图片等比缩放直到完全覆盖容器（背景图片有可能显示不完整）—— 相对比较好的选择 |

```css
background-size: 300px 200px;
background-size: 100% 100%;
background-size: contain;
background-size: cover;
```

### 4.4 `background` 复合属性

```css
background: color url repeat position / size origin clip
```

注意：
1. `origin` 和 `clip` 的值如果一样，只写一个值则两者都设置；如果设置了两个值，前面的是 `origin`，后面的是 `clip`。
2. `size` 的值必须写在 `position` 值的后面，并且用 `/` 分开。

### 4.5 多背景图

CSS3 允许元素设置多个背景图片，用逗号分隔：

```css
/* 添加多个背景图 */
background: url(../images/bg-lt.png) no-repeat,
            url(../images/bg-rt.png) no-repeat right top,
            url(../images/bg-lb.png) no-repeat left bottom,
            url(../images/bg-rb.png) no-repeat right bottom;
```

---

## 五、CSS3 新增边框属性

### 5.1 边框圆角

在 CSS3 中，使用 `border-radius` 属性可以将盒子变为圆角。

#### 分开设置每个角

| 属性名 | 作用 |
|--------|------|
| `border-top-left-radius` | 设置左上角：一个值是正圆半径，两个值分别是椭圆的 x 半径、y 半径 |
| `border-top-right-radius` | 设置右上角：同上 |
| `border-bottom-right-radius` | 设置右下角：同上 |
| `border-bottom-left-radius` | 设置左下角：同上 |

#### 复合写法

```css
border-radius: 10px;

/* 椭圆角复合写法（几乎不用） */
border-radius: 左上角x 右上角x 右下角x 左下角x / 左上y 右上y 右下y 左下y;
```

### 5.2 边框外轮廓（了解）

- **`outline-width`**：外轮廓的宽度。
- **`outline-color`**：外轮廓的颜色。
- **`outline-style`**：外轮廓的风格。

| 值 | 效果 |
|----|------|
| `none` | 无轮廓 |
| `dotted` | 点状轮廓 |
| `dashed` | 虚线轮廓 |
| `solid` | 实线轮廓 |
| `double` | 双线轮廓 |

- **`outline-offset`**：设置外轮廓与边框的距离，正负值都可以设置。

> **注意**：`outline-offset` 不是 `outline` 的子属性，是一个独立的属性。

**`outline` 复合属性**：

```css
outline: 50px solid blue;
```

---

## 六、CSS3 新增文本属性

### 6.1 文本阴影

在 CSS3 中，我们可以使用 `text-shadow` 属性给文本添加阴影。

**语法**：

```css
text-shadow: h-shadow v-shadow blur color;
```

**各个值的含义**：

| 值 | 描述 |
|----|------|
| `h-shadow` | 必需写，水平阴影的位置，允许负值 |
| `v-shadow` | 必需写，垂直阴影的位置，允许负值 |
| `blur` | 可选，模糊的距离 |
| `color` | 可选，阴影的颜色 |

默认值：`text-shadow: none` 表示没有阴影。

### 6.2 文本换行

在 CSS3 中，我们可以使用 `white-space` 属性设置文本换行方式。

| 值 | 含义 |
|----|------|
| `normal` | 文本超出边界自动换行，文本中的换行被浏览器识别为一个空格（默认值） |
| `pre` | 原样输出，与 `<pre>` 标签的效果相同 |
| `pre-wrap` | 在 `pre` 效果的基础上，超出元素边界自动换行 |
| `pre-line` | 在 `pre` 效果的基础上，超出元素边界自动换行，且只识别文本中的换行，空格会忽略 |
| `nowrap` | 强制不换行 |

### 6.3 文本溢出

在 CSS3 中，我们可以使用 `text-overflow` 属性设置文本内容溢出时的呈现模式。

| 值 | 含义 |
|----|------|
| `clip` | 当内联内容溢出时，将溢出部分裁切掉（默认值） |
| `ellipsis` | 当内联内容溢出块容器时，将溢出部分替换为 `...` |

> **注意**：要使得 `text-overflow` 属性生效，块容器必须显式定义 `overflow` 为非 `visible` 值，`white-space` 为 `nowrap` 值。

### 6.4 文本修饰升级

CSS3 升级了 `text-decoration` 属性，让其变成了复合属性。

**子属性及其含义**：

- **`text-decoration-line`**：设置文本装饰线的位置

| 值 | 含义 |
|----|------|
| `none` | 指定文字无装饰（默认值） |
| `underline` | 指定文字的装饰是下划线 |
| `overline` | 指定文字的装饰是上划线 |
| `line-through` | 指定文字的装饰是贯穿线 |

- **`text-decoration-style`**：文本装饰线条的形状

| 值 | 含义 |
|----|------|
| `solid` | 实线（默认） |
| `double` | 双线 |
| `dotted` | 点状线条 |
| `dashed` | 虚线 |
| `wavy` | 波浪线 |

- **`text-decoration-color`**：文本装饰线条的颜色

**复合写法**：

```css
text-decoration: text-decoration-line || text-decoration-style || text-decoration-color;
```

### 6.5 文本描边

> **注意**：文字描边功能仅 webkit 内核浏览器支持。

- **`-webkit-text-stroke-width`**：设置文字描边的宽度，写长度值。
- **`-webkit-text-stroke-color`**：设置文字描边的颜色，写颜色值。
- **`-webkit-text-stroke`**：复合属性，设置文字描边宽度和颜色。

---

## 七、CSS3 新增渐变

渐变是多个颜色之间的逐渐变化效果，一般用于设置盒子背景。实战用法见 [[12 CSS高级特效]]。

### 7.1 线性渐变

多个颜色之间的渐变，默认从上到下渐变。

**使用关键词设置方向**：

```css
background-image: linear-gradient(red, yellow, green);
background-image: linear-gradient(to top, red, yellow, green);
background-image: linear-gradient(to right top, red, yellow, green);
```

**使用角度设置方向**：

```css
background-image: linear-gradient(30deg, red, yellow, green);
```

**调整开始渐变的位置**：

```css
background-image: linear-gradient(red 50px, yellow 100px, green 150px);
```

### 7.2 径向渐变

多个颜色之间的渐变，默认从圆心四散（注意：不一定是正圆，要看容器本身宽高比）。

**基础用法**：

```css
background-image: radial-gradient(red, yellow, green);
```

**使用关键词调整圆心**：

```css
background-image: radial-gradient(at right top, red, yellow, green);
```

**使用像素值调整圆心**：

```css
background-image: radial-gradient(at 100px 50px, red, yellow, green);
```

**调整形状为正圆**：

```css
background-image: radial-gradient(circle, red, yellow, green);
```

**调整形状的半径**：

```css
background-image: radial-gradient(100px, red, yellow, green);
background-image: radial-gradient(50px 100px, red, yellow, green);
```

**调整颜色停止位置**：

```css
background-image: radial-gradient(red 50px, yellow 100px, green 150px);
```

### 7.3 重复渐变

无论线性渐变还是径向渐变，在没有发生渐变的位置继续进行渐变，就为重复渐变。

- **`repeating-linear-gradient`**：重复线性渐变，参数同 `linear-gradient`。
- **`repeating-radial-gradient`**：重复径向渐变，参数同 `radial-gradient`。

> 可以利用渐变做出很多有意思的效果：例如横格纸、立体球等等。

---

## 八、Web 字体

### 8.1 基本用法

可以通过 `@font-face` 指定字体的具体地址，浏览器会自动下载该字体，这样就不依赖用户电脑上的字体了。

**简写方式**：

```css
@font-face {
    font-family: "情书字体";
    src: url('./方正手迹.ttf');
}
```

**高兼容性写法**：

```css
@font-face {
    font-family: "atguigu";
    font-display: swap;
    src: url('webfont.eot'); /* IE9 */
    src: url('webfont.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
        url('webfont.woff2') format('woff2'),
        url('webfont.woff') format('woff'), /* chrome、firefox */
        url('webfont.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android */
        url('webfont.svg#webfont') format('svg'); /* iOS 4.1- */
}
```

### 8.2 定制字体

中文的字体文件很大，使用完整的字体文件不现实，通常针对某几个文字进行单独定制。

可使用阿里 Web 字体定制工具：[https://www.iconfont.cn/webfont](https://www.iconfont.cn/webfont)

### 8.3 字体图标

- 相比图片更加清晰。
- 灵活性高，更方便改变大小、颜色、风格等。
- 兼容性好，IE 也能支持。

字体图标的具体使用方式，每个平台不尽相同，最好参考平台使用指南。最常用的是阿里图标库：[https://www.iconfont.cn/](https://www.iconfont.cn/)

---

## 九、2D 变换

> 实战案例（如双开门、时钟、播放特效、轮播图）见 [[12 CSS高级特效]]。本节侧重 API 参考。

### 9.1 2D 位移

| 值 | 含义 |
|----|------|
| `translateX` | 设置水平方向位移，需指定长度值；百分比参考自身宽度 |
| `translateY` | 设置垂直方向位移，需指定长度值；百分比参考自身高度 |
| `translate` | 一个值代表水平方向，两个值代表水平和垂直方向 |

**注意点**：
1. 位移与相对定位很相似，都不脱离文档流，不会影响到其它元素。
2. 与相对定位的区别：相对定位的百分比值参考其父元素；位移的百分比值参考其自身。
3. 浏览器针对位移有优化，与定位相比，浏览器处理位移的效率更高。
4. `transform` 可以链式编写，例如：`transform: translateX(30px) translateY(40px);`
5. 位移对行内元素无效。
6. 位移配合定位，可实现元素水平垂直居中：

```css
.box {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
```

### 9.2 2D 缩放

| 值 | 含义 |
|----|------|
| `scaleX` | 设置水平方向的缩放比例，1 表示不缩放，大于 1 放大，小于 1 缩小 |
| `scaleY` | 设置垂直方向的缩放比例，同上 |
| `scale` | 同时设置水平和垂直缩放，一个值代表同时设置，两个值分别代表水平、垂直缩放 |

**注意点**：
1. `scale` 的值支持写负数，但几乎不用，容易让人产生误解。
2. 借助缩放，可实现小于 12px 的文字。

### 9.3 2D 旋转

| 值 | 含义 |
|----|------|
| `rotate` | 设置旋转角度，需指定角度值（`deg`），正值顺时针，负值逆时针 |

> **注意**：`rotateZ(20deg)` 相当于 `rotate(20deg)`，到了 3D 变换时还能写 `rotate(x, x, x)`。

### 9.4 2D 扭曲（了解）

2D 扭曲是指让元素在二维平面内被"拉扯"进而"走形"，实际开发几乎不用，了解即可。

| 值 | 含义 |
|----|------|
| `skewX` | 设置元素在水平方向扭曲，值为角度值，会将元素的左上角、右下角拉扯 |
| `skewY` | 设置元素在垂直方向扭曲，值为角度值，会将元素的左上角、右下角拉扯 |
| `skew` | 一个值代表 `skewX`，两个值分别代表 `skewX`、`skewY` |

### 9.5 多重变换

多个变换可以同时使用一个 `transform` 来编写。

```css
transform: translate(-50%, -50%) rotate(45deg);
```

> **注意**：多重变换时，建议最后旋转。因为旋转会改变坐标轴，影响后续变换的轴向。

### 9.6 变换原点

元素变换时，默认的原点是元素的中心，使用 `transform-origin` 可以设置变换的原点。

修改变换原点对位移没有影响，对旋转和缩放会产生影响。

| 写法 | 含义 |
|------|------|
| `transform-origin: 50% 50%` | 变换原点在元素中心位置，百分比相对于自身（默认值） |
| `transform-origin: left top` | 变换原点在元素左上角 |
| `transform-origin: 50px 50px` | 变换原点距离元素左上角 50px 50px |
| `transform-origin: 0` | 只写一个值时，第二个值默认为 50% |

---

## 十、3D 变换

### 10.1 开启 3D 空间

> **重要原则**：元素进行 3D 变换的首要操作：父元素必须开启 3D 空间！

使用 `transform-style` 开启 3D 空间：

| 值 | 含义 |
|----|------|
| `flat` | 让子元素位于此元素的二维平面内（2D 空间）—— 默认值 |
| `preserve-3d` | 让子元素位于此元素的三维空间内（3D 空间） |

### 10.2 设置景深

**何为景深？**—— 指定观察者与 z=0 平面的距离，能让发生 3D 变换的元素产生透视效果，看起来更加立体。

使用 `perspective` 设置景深：

| 值 | 含义 |
|----|------|
| `none` | 不指定透视（默认值） |
| 长度值 | 指定观察者距离 z=0 平面的距离，不允许负值 |

> **注意**：`perspective` 设置给发生 3D 变换元素的父元素！

### 10.3 透视点位置

所谓透视点位置，就是观察者位置；默认的透视点在元素的中心。

使用 `perspective-origin` 设置观察者位置（透视点的位置）：

```css
/* 相对坐标轴往右偏移 400px，往下偏移 300px
   （相当于人蹲下 300 像素，然后向右移动 400 像素看元素） */
perspective-origin: 400px 300px;
```

> **注意**：通常情况下，我们不需要调整透视点位置。

### 10.4 3D 位移

3D 位移是在 2D 位移的基础上，可以让元素沿 z 轴位移。

| 值 | 含义 |
|----|------|
| `translateZ` | 设置 z 轴位移，需指定长度值，正值向屏幕外，负值向屏幕里，不能写百分比 |
| `translate3d` | 第 1 个参数对应 x 轴，第 2 个对应 y 轴，第 3 个对应 z 轴，均不能省略 |

### 10.5 3D 旋转

3D 旋转是在 2D 旋转的基础上，可以让元素沿 x 轴和 y 轴旋转。

| 值 | 含义 |
|----|------|
| `rotateX` | 设置 x 轴旋转角度，面对 x 轴正方向：正值顺时针，负值逆时针 |
| `rotateY` | 设置 y 轴旋转角度，面对 y 轴正方向：正值顺时针，负值逆时针 |
| `rotate3d` | 前 3 个参数分别表示 x, y, z 坐标轴，第 4 个参数表示旋转角度。如 `rotate3d(1,1,1,30deg)` 表示 x、y、z 分别旋转 30 度 |

### 10.6 3D 缩放

3D 缩放是在 2D 缩放的基础上，可以让元素沿 z 轴缩放。

| 值 | 含义 |
|----|------|
| `scaleZ` | 设置 z 轴方向的缩放比例，1 表示不缩放，大于 1 放大，小于 1 缩小 |
| `scale3d` | 第 1 个参数对应 x 轴，第 2 个对应 y 轴，第 3 个对应 z 轴，参数不允许省略 |

### 10.7 多重变换

多个变换可以同时使用一个 `transform` 来编写。

```css
transform: translateZ(100px) scaleZ(3) rotateY(40deg);
```

> **注意**：多重变换时，建议最后旋转。

### 10.8 背部可见性

使用 `backface-visibility` 指定元素背面在面向用户时是否可见。

| 值 | 含义 |
|----|------|
| `visible` | 指定元素背面可见，允许显示正面的镜像（默认值） |
| `hidden` | 指定元素背面不可见 |

> **注意**：`backface-visibility` 需要加在发生 3D 变换元素的自身上。

---

## 十一、过渡（升级）

过渡可以在不使用 Flash 动画、不使用 JavaScript 的情况下，让元素从一种样式平滑过渡为另一种样式。

> 实战用法与注意事项见 [[12 CSS高级特效]]。本节侧重全部子属性详表。

### 11.1 `transition-property`

作用：定义哪个属性需要过渡，只有在该属性中定义的属性才会以有过渡效果。

| 常用值 | 含义 |
|--------|------|
| `none` | 不过渡任何属性 |
| `all` | 过渡所有能过渡的属性 |
| 具体属性名 | 如 `width`、`height`，多个以逗号分隔 |

> 不是所有的属性都能过渡。值为数字或能转为数字的属性才支持过渡。常见支持过渡的属性：颜色、长度值、百分比、`z-index`、`opacity`、2D/3D 变换属性、阴影。

### 11.2 `transition-duration`

作用：设置过渡的持续时间，即一个状态过渡到另一个状态耗时多久。

| 常用值 | 含义 |
|--------|------|
| `0` | 没有任何过渡时间（默认值） |
| `s` 或 `ms` | 秒或毫秒 |
| 列表 | 一个值则所有属性统一时间，多个值对应不同属性 |

### 11.3 `transition-delay`

作用：指定开始过渡的延迟时间，单位：`s` 或 `ms`。

### 11.4 `transition-timing-function`

作用：设置过渡的类型。

| 值 | 效果 |
|----|------|
| `ease` | 平滑过渡（默认值） |
| `linear` | 线性过渡 |
| `ease-in` | 慢 → 快 |
| `ease-out` | 快 → 慢 |
| `ease-in-out` | 慢 → 快 → 慢 |
| `step-start` | 等同于 `steps(1, start)` |
| `step-end` | 等同于 `steps(1, end)` |
| `steps(integer, start|end)` | 步进函数，第一个参数为正整数指定步数，第二个参数指定变化时间点（默认 `end`） |
| `cubic-bezier(n,n,n,n)` | 特定的贝塞尔曲线类型 |

在线制作贝塞尔曲线：[https://cubic-bezier.com](https://cubic-bezier.com)

### 11.5 `transition` 复合属性

```css
transition: 1s 1s linear all;
```

> 如果设置了一个时间，表示 `duration`；如果设置了两个时间，第一个是 `duration`，第二个是 `delay`；其他值没有顺序要求。

---

## 十二、动画（升级）

> 实战用法（如走马灯、精灵动画、多组动画）见 [[12 CSS高级特效]]。本节侧重全部子属性详表。

### 12.1 什么是帧与关键帧

- **帧**：一段动画就是一段时间内连续播放 n 个画面。每一张画面叫"帧"。同样时间内播放的帧数越多，画面越流畅。
- **关键帧**：在构成一段动画的若干帧中，起到决定性作用的 2-3 帧。

### 12.2 动画的基本使用

**第一步：定义关键帧（定义动画）**

```css
/* 简单方式（两种状态） */
@keyframes 动画名 {
    from {
        /* property: value */
    }
    to {
        /* property: value */
    }
}

/* 完整方式（多状态） */
@keyframes 动画名 {
    0%   { /* property: value */ }
    20%  { /* property: value */ }
    40%  { /* property: value */ }
    60%  { /* property: value */ }
    80%  { /* property: value */ }
    100% { /* property: value */ }
}
```

**第二步：给元素应用动画**

```css
.box {
    animation-name: testKey;       /* 指定动画 */
    animation-duration: 5s;        /* 设置动画所需时间 */
    animation-delay: 0.5s;         /* 设置动画延迟 */
}
```

### 12.3 `animation-timing-function`

设置动画的类型，常用值如下：

| 值 | 效果 |
|----|------|
| `ease` | 平滑动画（默认值） |
| `linear` | 线性过渡 |
| `ease-in` | 慢 → 快 |
| `ease-out` | 快 → 慢 |
| `ease-in-out` | 慢 → 快 → 慢 |
| `step-start` | 等同于 `steps(1, start)` |
| `step-end` | 等同于 `steps(1, end)` |
| `steps(integer, start|end)` | 步进函数 |
| `cubic-bezier(n,n,n,n)` | 贝塞尔曲线类型 |

### 12.4 `animation-iteration-count`

指定动画的播放次数：

| 值 | 含义 |
|----|------|
| `number` | 动画循环次数 |
| `infinite` | 无限循环 |

### 12.5 `animation-direction`

指定动画方向：

| 值 | 含义 |
|----|------|
| `normal` | 正常方向（默认） |
| `reverse` | 反方向运行 |
| `alternate` | 动画先正常运行再反方向运行，并持续交替运行 |
| `alternate-reverse` | 动画先反运行再正方向运行，并持续交替运行 |

### 12.6 `animation-fill-mode`

设置动画之外的状态：

| 值 | 含义 |
|----|------|
| `forwards` | 设置对象状态为动画结束时的状态 |
| `backwards` | 设置对象状态为动画开始时的状态 |

### 12.7 `animation-play-state`

设置动画的播放状态：

| 值 | 含义 |
|----|------|
| `running` | 运动（默认） |
| `paused` | 暂停 |

### 12.8 `animation` 复合属性

```css
.inner {
    animation: atguigu 3s 0.5s linear 2 alternate-reverse forwards;
}
```

> 只设置一个时间表示 `duration`，设置两个时间分别是 `duration` 和 `delay`，其他属性没有数量和顺序要求。`animation-play-state` 一般单独使用。

---

## 十三、伸缩盒模型（Flex 布局）

CSS3 新增了全新的布局方案 —— 弹性盒子（Flexible Box）。

> **详见**：[[10 CSS-Flex弹性布局]]

---

## 十四、多列布局

作用：专门用于实现类似于报纸的布局。

> **详见**：[[11 CSS-多列布局与BFC]]

---

## 十五、响应式布局 / 媒体查询

> 实战用法（如 Bootstrap 框架、常用阈值实践）见 [[14 响应式]]。本节侧重媒体查询规范参考。

### 15.1 媒体类型

| 值 | 含义 |
|----|------|
| `all` | 检测所有设备 |
| `screen` | 检测电子屏幕，包括电脑屏幕、平板屏幕、手机屏幕等 |
| `print` | 检测打印机 |

> 以下已废弃：`aural`、`braille`、`embossed`、`handheld`、`projection`、`tty`、`tv`

### 15.2 媒体特性

| 值 | 含义 |
|----|------|
| `width` | 检测视口宽度 |
| `max-width` | 检测视口最大宽度 |
| `min-width` | 检测视口最小宽度 |
| `height` | 检测视口高度 |
| `max-height` | 检测视口最大高度 |
| `min-height` | 检测视口最小高度 |
| `device-width` | 检测设备屏幕的宽度 |
| `max-device-width` | 检测设备屏幕的最大宽度 |
| `min-device-width` | 检测设备屏幕的最小宽度 |
| `orientation` | 检测视口的旋转方向：`portrait`（纵向）、`landscape`（横向） |

完整列表请参考：[MDN @media](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@media)

### 15.3 运算符

| 运算符 | 含义 |
|--------|------|
| `and` | 并且 |
| `,` 或 `or` | 或 |
| `not` | 否定 |
| `only` | 肯定 |

### 15.4 常用阈值

在实际开发中，会将屏幕划分成几个区间：

```css
/* 超小屏幕（手机） */
@media screen and (max-width: 768px) {
    /* CSS-Code */
}

/* 中等屏幕（平板） */
@media screen and (min-width: 768px) and (max-width: 1200px) {
    /* CSS-Code */
}
```

### 15.5 结合外部样式的用法

**用法一**：在 `<link>` 标签中指定媒体查询：

```html
<link rel="stylesheet" media="具体的媒体查询" href="mystylesheet.css">
```

**用法二**：在 CSS 文件中使用 `@media` 规则（更常用）：

```css
@media screen and (max-width: 768px) {
    /* CSS-Code */
}
```

---

## 十六、BFC

> **详见**：[[11 CSS-多列布局与BFC]]
