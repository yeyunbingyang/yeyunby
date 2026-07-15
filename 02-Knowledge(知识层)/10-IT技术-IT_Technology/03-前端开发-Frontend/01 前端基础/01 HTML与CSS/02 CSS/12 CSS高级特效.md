---
title: CSS 高级特效
domain: IT_Technology
tags:
  - CSS
  - 变换
  - 动画
  - 渐变
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
summary: CSS高级特效包括平面转换（位移/旋转/缩放/倾斜）、渐变（线性/径向）、空间转换（3D）、关键帧动画及综合案例应用。
---

## 目标：

使用位移、缩放、旋转、渐变效果丰富网页元素的呈现方式。

## 01-平面转换

### 简介

作用：为元素添加**动态效果**，一般与过渡配合使用

概念：改变盒子在**平面**内的**形态**（位移、旋转、缩放、倾斜）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403500931-616e9b26-e3a9-49a6-8008-ad8660bebf25.png)

平面转换也叫 2D 转换，属性是 **transform**

### 平移

transform: translate(X轴移动距离, Y轴移动距离);

- 取值

- 像素单位数值
- 百分比（参照**盒子自身尺寸**计算结果）
- **正负**均可

- 技巧

- translate() **只写一个值**，表示沿着 **X** 轴移动
- 单独设置 X 或 Y 轴移动距离：translateX() 或 translateY()

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747406330833-e34570ae-9ecc-4ac4-8d3f-7872d836ed20.png)

### 定位居中

- 方法一：margin

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403540328-f49ddc4e-808b-4b1a-a855-fb0ba34904cf.png)

- 方法二：平移 → 百分比参照盒子自身尺寸计算结果

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403551217-9e7081d8-89fb-4c38-b5b0-d407a35ed303.png)

### 案例-双开门

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403566036-65e31fb9-0725-450f-ab88-cd8534b03c9e.png)

- HTML 结构

```html
<div class="father">
     <div class="left"></div>
     <div class="right"></div>
 </div>
```

- CSS 样式

```css
* {
     margin: 0;
     padding: 0;
 }

 /* 1. 布局：父子结构，父级是大图，子级是左右小图 */
 .father {
     display: flex;
     margin: 0 auto;
     width: 1366px;
     height: 600px;
     background-image: url(./images/bg.jpg);

     overflow: hidden;
 }

 .father .left,
 .father .right {
     width: 50%;
     height: 600px;
     background-image: url(./images/fm.jpg);

     transition: all .5s;
 }

 .father .right {
     /* right 表示的取到精灵图右面的图片 */
     background-position: right 0;
 }

 /* 2. 鼠标悬停的效果：左右移动 */
 .father:hover .left {
     transform: translate(-100%);
 }

 .father:hover .right {
     transform: translateX(100%);
 }
```

### 旋转

transform: rotate(旋转角度);

- 取值：角度单位是 **deg**
- 技巧

- 取值正负均可
- 取值为正，顺时针旋转
- 取值为负，逆时针旋转

### 转换原点

默认情况下，转换原点是盒子中心点

transform-origin: 水平原点位置 垂直原点位置;

取值：

- **方位名词**（left、top、right、bottom、center）
- 像素单位数值
- 百分比

### 案例-时钟

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403579156-cb818563-f9c6-46ca-a2cf-d725c37d9a2a.png)

```css
.hour {
   width: 6px;
   height: 50px;
   background-color: #333;
   margin-left: -3px;
   transform: rotate(15deg);
   transform-origin: center bottom;
 }

 .minute {
   width: 5px;
   height: 65px;
   background-color: #333;
   margin-left: -3px;
   transform: rotate(90deg);
   transform-origin: center bottom;
 }

 .second {
   width: 4px;
   height: 80px;
   background-color: red;
   margin-left: -2px;
   transform: rotate(240deg);
   transform-origin: center bottom;
 }
```

### 多重转换

多重转换技巧：先平移再旋转

transform: translate() rotate();

- 多重转换原理：以第一种转换方式坐标轴为准转换形态

- 旋转会改变网页元素的坐标轴向
- 先写旋转，则后面的转换效果的轴向以旋转后的轴向为准，会影响转换结果

- 旋转会改变坐标轴

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747412186958-b78d9265-b220-477b-b734-6340a61d1032.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747412236595-e69021af-e9b6-421d-bd03-2da86356a3e4.png)

### 缩放

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747412342350-7aa2c666-9137-4423-92d3-f0720be47b0c.png)

```css
transform: scale(缩放倍数);
 transform: scale(X轴缩放倍数, Y轴缩放倍数);
```

- 技巧

- 通常，只为 scale() 设置一个值，表示 X 轴和 Y 轴等比例缩放
- 取值大于1表示放大，取值小于1表示缩小

### 案例-播放特效

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403590623-3273e1d1-f92f-47c0-b3eb-9430e203f329.png)

- CSS 样式

注意css层叠问题

```css
/* 1. 摆放播放按钮：图片区域的中间 */
 .box li {
   overflow: hidden;
 }

 .pic {
   position: relative;
 }

 .pic::after {
   position: absolute;
   left: 50%;
   top: 50%;
   /* margin-left: -29px;
   margin-top: -29px; */
   /* transform: translate(-50%, -50%); */

   content: '';
   width: 58px;
   height: 58px;
   background-image: url(./images/play.png);
   transform: translate(-50%, -50%) scale(5);
   opacity: 0;

   transition: all .5s;
 }
 /* 2. hover效果：大按钮，看不见：透明是0 → 小按钮，看得见：透明度1 */
 .box li:hover .pic::after {
   transform: translate(-50%, -50%) scale(1);
   opacity: 1;
 }
```

### 倾斜

transform: skew();

取值：角度度数 deg

## 02-渐变

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747467564573-0c4c4f5b-b2bf-43dd-83f9-48445277f373.png)

渐变是多个颜色逐渐变化的效果，一般用于设置盒子背景

悬浮在元素上可以变暗后、使文字更加清晰

分类：

- 线性渐变

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403603458-81f5f64c-218b-4723-b5a6-92c3916537d4.png)

- 径向渐变

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403611628-01c4fbf3-aa5c-4c1a-a5af-0fb75b85ef95.png)

### 线性渐变

```css
background-image: linear-gradient(
   渐变方向,
   颜色1 终点位置,
   颜色2 终点位置,
   ......
 );
```

取值：

- 渐变方向：可选【默认从上到下】

- to 方位名词
- 角度度数

- 终点位置：可选

- 百分比

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747468223475-0390d58f-d9ea-4933-8280-dde186a419ac.png)

### 案例-产品展示

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403629613-41b20299-4a2c-4443-8eb0-035163c59928.png)

- HTML 结构

```html
<div class="box">
   <img src="./images/product.jpeg" alt="" />
   <div class="title">OceanStor Pacific 海量存储斩获2021 Interop金奖</div>
   <div class="mask"></div>
 </div>
```

- CSS 样式

```css
.mask {
   position: absolute;
   left: 0;
   top: 0;
   width: 100%;
   height: 100%;
   background-image: linear-gradient(
       transparent,
       rgba(0,0,0,0.5)
   );
   opacity: 0;

   transition: all .5s;
 }

 .box:hover .mask {
   opacity: 1;
 }
```

### 径向渐变

光晕效果 / 鼠标悬停聚光灯

按钮高光（立体感按钮）

图标 / 卡片边缘发光背景

模仿太阳/能量球

```css
radial-gradient([形状 size] at 位置, 颜色1, 颜色2, ...)


background-image: radial-gradient(
   半径 at 圆心位置,
   颜色1 终点位置,
   颜色2 终点位置,
   ......
 );
```

#### 🔍 参数详解

##### 1. 形状与大小（半径）

- 形状【可忽略】

- `circle`：圆形（默认）
- `ellipse`：椭圆（默认如果容器宽高不同）

- 大小：【水平半径，垂直半径】

- 具体值：`100px 200px`（椭圆），或 `100px`（圆）

##### 2. 圆心位置

`at` 后面定义圆心位置，可用：

- **像素值**：`at 100px 100px`
- **百分比**：`at 50% 50%`（中心）
- **方位关键字**：如：

- `at center`（默认中心）
- `at top left`
- `at bottom right`
- `at 30% top`

##### 3. 颜色及停止位置

每个颜色后可跟一个"渐变终点位置"：

- 绝对单位：`red 50px`
- 百分比：`blue 70%`

![[Pasted image 20260630215030.png]]

#### 📘 示例代码

##### ✅ 示例 1：中心为圆形渐变

```css
background-image: radial-gradient(
circle at center, red, blue);
```

##### ✅ 示例 2：椭圆渐变，左上角开始

```css
background-image: radial-gradient(
ellipse at top left, red 0%, blue 100%);
```

##### ✅ 示例 3：指定半径为椭圆

```css
background-image: radial-gradient(
100px 150px at 50% 50%, orange, purple);
```

##### ✅ 示例 4：以 80px 半径圆从鼠标点击处展开

```css
background-image: radial-gradient(
circle 80px at 200px 300px, yellow, green);
```

## 03-综合案例

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403459229-bee86a0a-de29-4e79-b61a-9eee6b0e48c1.png)

### 导航-频道

#### 箭头旋转

平面转换-选择

```css
.x-header-nav .nav-item:hover .icon-down {
   transform: rotate(-180deg);
 }
```

#### 频道列表

平面转换-平移

```css
.channel-layer {
   position: absolute;
   top: 60px;
   left: 50%;
   z-index: -2;
   width: 1080px;
   height: 120px;
   padding: 10px;
   margin-left: -540px;
   color: #72727b;
   background-color: #f5f5f5;
   border: 1px solid #e4e4e4;
   border-top: none;
   transition: all 0.5s;
   transform: translateY(-120px);
 }

 /* TODO 2. 弹窗频道 */
 .x-header-nav .nav-item:hover .channel-layer {
   transform: translateY(0);
 }
```

### 渐变按钮

#### 搜索按钮

左到右线性

```css
.x-header-search form .btn {
   position: absolute;
   top: 0;
   right: 0;
   width: 60px;
   height: 40px;
   line-height: 40px;
   text-align: center;
   background-color: #f86442;
   border-top-right-radius: 20px;
   border-bottom-right-radius: 20px;
   background-image: linear-gradient(
     to right,
     rgba(255, 255, 255, 0.3),
     #f86442
   );
 }
```

#### 登录按钮

左到右线性

```css
/* TODO 7. 渐变按钮 */
 .card .card-info .login {
   padding: 3px 34px;
   color: #fff;
   background-color: #ff7251;
   border-radius: 30px;
   box-shadow: 0 4px 8px 0 rgb(252 88 50 / 50%);
   background-image: linear-gradient(
     to right,
     rgba(255, 255, 255, 0.2),
     #ff7251
   );
 }
```

#### 客户端按钮

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747472282034-781fd3ad-42e2-4113-8eb0-e0266763392e.png)

高亮 透明 左部分白透明到透明

```css
/* TODO 8. 径向渐变 */
 .download .dl .dl-btn {
   width: 68px;
   height: 34px;
   line-height: 34px;
   color: #fff;
   text-align: center;
   border-radius: 4px;
   background-image: radial-gradient(
     50px at 10px 10px,
     rgba(255, 255, 255, 0.5),
     transparent
   );
 }
```

### 轮播图

平面转换+定位

```css
/* TODO 4. 摆放图片 */
 .banner .banner-list .banner-item.left {
   z-index: 0;
   transform: translate(-160px) scale(0.8);
   transform-origin: left center;
 }

 .banner .banner-list .banner-item.right {
   z-index: 0;
   transform: translate(160px) scale(0.8);
   transform-origin: right center;
 }
```

### 猜你喜欢

```css
/* TODO 5. 播放按钮和遮罩 */
 .album-item .album-item-box::after {
   position: absolute;
   left: 0;
   top: 0;
   content: '';
   width: 100%;
   height: 100%;
   background: rgba(0,0,0,.5) url(../assets/play.png) no-repeat center / 20px;
   opacity: 0;
   transition: all .5s;
 }

 .album-item .album-item-box:hover::after {
   opacity: 1;
   background-size: 50px;
 }


 /* TODO 6. 图片缩放 */
 .album-item .album-item-box:hover img {
   transform: scale(1.1);
 }
```



## 04-空间转换

### 空间转换简介

- 空间：是从坐标轴角度定义的 X 、Y 和 Z 三条坐标轴构成了一个立体空间，Z 轴位置与视线方向相同。
- 空间转换也叫 3D转换
- 属性：transform

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831428-1949d1e0-3edb-4bcd-b655-18fc46d8945b.png "null")

### 平移

translate3d 3个值都必须写

```css
transform: translate3d(x, y, z);
transform: translateX();
transform: translateY();
transform: translateZ();
```

取值与平面转换相同

默认情况下，Z 轴平移没有效果，原因：电脑屏幕默认是平面，无法显示 Z 轴平移效果

### 视距

作用：指定了观察者与 Z=0 平面的距离，为元素添加透视效果

透视效果：近大远小、近实远虚

属性：(添加给直接父级，取值范围 800-1200)

```css
perspective: 视距;
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831501-4ca8aa2c-ac99-489b-bfdb-5a3a748fe421.png "null")

### 旋转

- Z 轴：rotateZ()

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831570-274ffb61-3ede-4523-b33f-5ac61f7d446f.png "null")

- X 轴：rotateX()

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831635-cdc7c56d-fea3-4d8f-ba31-38c11edb2f1f.png "null")

- Y 轴：rotateY()

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831691-370a72b5-929e-4941-afaf-bf2304d74e8f.png "null")

### 左手法则

作用：根据旋转方向确定取值正负

使用：左手握住旋转轴, 拇指指向正值方向, 其他四个手指弯曲方向为旋转正值方向

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831760-86b81776-d012-488c-b78a-4b1683fead32.png "null")

### rotate3d-了解

- rotate3d(x, y, z, 角度度数) ：用来设置自定义旋转轴的位置及旋转的角度
- x，y，z 取值为0-1之间的数字

### 立体呈现

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747478540246-d9e224bb-122e-4fb1-accd-3fa20c0a1080.png)

作用：设置元素的子元素是位于 3D 空间中还是平面中

属性名：transform-style

属性值：

- flat：子级处于平面中
- preserve-3d：子级处于 3D 空间

### 案例-3d导航

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831822-883218d1-dd16-4423-9a16-af4e05947451.png "null")

案例步骤：

1. 搭建立方体

2. 绿色是立方体的前面
3. 橙色是立方体的上面

4. 鼠标悬停，立方体旋转

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831895-bfefc437-54fa-4f98-89a2-e135c0df0425.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403831996-5f82d4f2-f352-4ab3-94dc-1a36e36c5f90.png "null")

```css
.nav li {
  position: relative;
  width: 100px;
  height: 40px;
  line-height: 40px;
  transition: all 0.5s;

  transform-style: preserve-3d;

  /* 为了看到橙色和绿色的移动过程，给立方体添加旋转 */
  /* transform: rotateX(-20deg) rotateY(30deg); */
}

.nav li a {
  position: absolute;
  left: 0;
  top: 0;
  display: block;
  width: 100%;
  height: 100%;
  text-align: center;
  text-decoration: none;
  color: #fff;
}

/* 立方体每个面都有独立的坐标轴，互不影响 */
.nav li a:first-child {
  background-color: green;
  transform: translateZ(20px);
}

.nav li a:last-child {
  background-color: orange;
  transform: rotateX(90deg) translateZ(20px);
}

.nav li:hover {
  transform: rotateX(-90deg);
}
```

### 缩放

```css
transform: scale3d(x, y, z);
transform: scaleX();
transform: scaleY();
transform: scaleZ();
```

## 05-动画

- 过渡：实现两个状态间的变化过程
- 动画：实现多个状态间的变化过程，动画过程可控（重复播放、最终画面、是否暂停）

### 动画实现步骤

1. 定义动画

```css
/* 方式一 2个状态*/
@keyframes 动画名称 {
  from {}
  to {}
}

/* 方式二 多个状态*/
@keyframes 动画名称 {
  0% {}
  10% {}
  ......
  100% {}
}
```

2. 使用动画

```css
animation: 动画名称 动画花费时长;
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747486583563-d299ee10-9eb4-4be2-9182-3c8a778cc903.png)

### animation复合属性

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403832053-f4783479-4885-4d68-a619-dd6499c86306.png "null")

提示：

- 动画名称和动画时长必须赋值
- 取值不分先后顺序
- 如果有两个时间值，第一个时间表示动画时长，第二个时间表示延迟时间

### animation拆分写法

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403832118-fb4e9fd7-e2db-451d-bc68-d158efeeb62b.png "null")

### 案例-走马灯

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403832176-0391af6b-bd7e-449d-82bf-732538415422.png "null")

- HTML 结构

```html
<li><img src="./images/1.jpg" alt="" /></li>

<li><img src="./images/2.jpg" alt="" /></li>

<li><img src="./images/3.jpg" alt="" /></li>

<li><img src="./images/4.jpg" alt="" /></li>

<li><img src="./images/5.jpg" alt="" /></li>

<li><img src="./images/6.jpg" alt="" /></li>

<li><img src="./images/7.jpg" alt="" /></li>

<!-- 替身：填补显示区域的露白 -->
<li><img src="./images/1.jpg" alt="" /></li>

<li><img src="./images/2.jpg" alt="" /></li>

<li><img src="./images/3.jpg" alt="" /></li>
```

- CSS 样式

```css
.box {
  width: 600px;
  height: 112px;
  border: 5px solid #000;
  margin: 100px auto;
  overflow: hidden;
}

.box ul {
  display: flex;
  animation: move 6s infinite linear;
}

/* 定义位移动画；ul使用动画；鼠标悬停暂停动画 */
@keyframes move {
  0% {
    transform: translate(0);
  }
  100% {
    transform: translate(-1400px);
  }
}

.box:hover ul {
  animation-play-state: paused;
}
```

无缝动画原理：复制开头图片到结尾位置（图片累加宽度 = 区域宽度）

### 精灵动画

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747488347414-610cc2bd-81c7-49e5-b1c1-b1652073e958.png)

- 核心

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403832230-77089097-a97c-4ade-9c96-5509eddca740.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747488451308-8d016f9a-115f-4fa1-aad5-28b1f98c5e6d.png)

- 制作步骤

- 1.准备显示区域盒子尺寸与一张精灵小图尺寸相同
- 2.定义动画移动背景图（移动距离 = 精灵图宽度）
- 3.使用动画steps(N)，N 与精灵小图个数相同

```css
div {
  width: 140px;
  height: 140px;
  border: 1px solid #000;
  background-image: url(./images/bg.png);
  animation: run 1s steps(12) infinite;
}

@keyframes run {
  from {
    background-position: 0 0;
  }
  to {
    background-position: -1680px 0;
  }
}
```

### 多组动画

```css
animation:
  动画一,
  动画二,
  ... ...
;
```

## 06-综合案例-全名出游

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747403832281-9d5c0848-0b41-4a7c-b7af-980f82416ba3.png "null")

### 背景

```css
/* 大背景 */
/* 默认状态HTML和body的高度是0，所以导致cover缩放背景图不成功 */
html {
  height: 100%;
}
body {
  height: 100%;
  background: url(../images/f1_1.jpg) no-repeat center 0 / cover;
  /* background-size: cover; */
}
```

### 云彩位置和动画

- HTML 结构

```html
<!-- 云 -->
<div class="cloud">
  <img src="./images/yun1.png" alt="">
  <img src="./images/yun2.png" alt="">
  <img src="./images/yun3.png" alt="">
</div>
```

- CSS 样式

```css
/* 云 */
.cloud img {
  position: absolute;
  left: 50%;
}

.cloud img:nth-child(1) {
  margin-left: -250px;
  top: 20px;
  animation: cloud 1s infinite alternate linear;
}
.cloud img:nth-child(2) {
  margin-left: 400px;
  top: 100px;
  animation: cloud 1s infinite alternate linear 0.4s;
}
.cloud img:nth-child(3) {
  margin-left: -550px;
  top: 200px;
  animation: cloud 1s infinite alternate linear 0.6s;
}

@keyframes cloud {
  100% {
    transform: translate(20px);
  }
}
```

### 文字动画

- HTML 结构

```html
<!-- 文字 -->
<div class="text">
  <img src="./images/font1.png" alt="">
</div>
```

- CSS 样式

```css
/* 文字 */
.text img {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  animation: text 1s;
}

/* 默认 → 小 → 大 → 小 → 默认 */
@keyframes text {
  0% {
    transform: translate(-50%, -50%) scale(1);
  }
  20% {
    transform: translate(-50%, -50%) scale(0.1);
  }
  40% {
    transform: translate(-50%, -50%) scale(1.4);
  }
  70% {
    transform: translate(-50%, -50%) scale(0.8);
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
  }
}
```

---

## 过渡 transition

作用：在元素**状态改变**时（如 hover），让属性值变化**平滑过渡**，而非瞬间切换。

### 语法

```css
transition: property duration timing-function delay;
```

| 参数 | 含义 | 示例 |
|------|------|------|
| property | 要过渡的 CSS 属性 | `all`（全部）、`transform`、`opacity` |
| duration | 过渡持续时间 | `0.5s`、`300ms`、`1s` |
| timing-function | 速度曲线 | `ease`（默认）、`linear`、`ease-in`、`ease-out`、`cubic-bezier()` |
| delay | 延迟开始时间 | `0s`（默认）、`0.5s` |

### 示例

```css
.box {
  width: 100px;
  height: 100px;
  background: blue;
  transition: all 0.5s ease 0s;
}

.box:hover {
  width: 200px;
  background: red;
}
```

### 注意事项

- 不是所有属性都能过渡。可过渡的通常是**数值型**或**颜色**属性（width/height/color/transform/opacity 等）。
- `display: none → block` 不能过渡，可用 `opacity + visibility` 替代。
- 若只有少数属性需要过渡，应指定具体属性而非 `all`，以提升性能。
