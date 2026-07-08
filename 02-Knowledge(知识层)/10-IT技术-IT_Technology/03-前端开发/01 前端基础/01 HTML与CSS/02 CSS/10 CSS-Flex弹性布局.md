---
title: CSS Flex 弹性布局
domain: IT_Technology
tags:
  - CSS
  - Flex
  - 弹性布局
  - 居中
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[06 CSS-浮动]]"
  - "[[07 CSS-定位]]"
summary: Flex弹性布局通过伸缩容器和伸缩项目的属性控制元素分布、对齐和顺序。容器属性（flex-direction/wrap/justify-content/align-items）和项目属性（flex/grow/shrink/basis/order）配合实现灵活布局。
---

## 伸缩盒模型⭐

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747147548396-b11c778c-d3d6-4557-a5ad-3ecb67616691.png)

### 1. 伸缩盒模型简介

2009年，w3c提出了一种新的盒子模型 ——FlexibleBox （伸缩盒模型，又称：弹性盒子）。

它可以轻松的控制：元素分布方式、元素对齐方式、元素视觉顺序

.......截止目前，除了在部分 IE 浏览器不支持，其他浏览器均已全部支持。

伸缩盒模型的出现，逐渐演变出了一套新的布局方案 ——flex布局。

小贴士：

1. 传统布局是指：基于传统盒状模型，主要靠： display属性 + position属性 + float

属性。

2.flex布局目前在移动端应用比较广泛，因为传统布局不能很好的呈现在移动设备上。

### 2. 伸缩容器、伸缩项目

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747147917134-c785f0e5-c3ea-47cf-b830-5138897c6284.png)

**伸缩容器**： 开启了flex的元素，就是：伸缩容器。

1. 给元素设置： display:flex 或 display:inline-flex，该元素就变为了伸缩容器。

2. display:inline-flex 很少使用，因为可以给多个伸缩容器的父容器，也设置为伸缩容器。

3. 一个元素可以同时是：伸缩容器、伸缩项目。

**伸缩项目**：伸缩容器所有**子元素**自动成为了：伸缩项目。

1. 仅伸缩容器的**子元素**成为了伸缩项目，孙子元素、重孙子元素等后代，不是伸缩项目。

2. 无论原来是哪种元素（块、行内块、行内），一旦成为了伸缩项目，全都会"**块状化**"。

### 3. 主轴与侧轴

**主轴：** 伸缩项目沿着主轴排列，主轴默认是水平的，默认方向是：从左到右（左边是起点，右边是终点）。

**侧轴：** 与主轴垂直的就是侧轴，侧轴默认是垂直的，默认方向是：从上到下（上边是起点，下边是终点）。

### 4. 主轴方向

属性名：flex-direction

常用值如下

1.**row ：主轴方向水平从左到右 —— 默认值**

2. row-reverse：主轴方向水平从右到左。

3. column：主轴方向垂直从上到下。

4. column-reverse：主轴方向垂直从下到上。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259180940-5daceebe-0d1f-4a10-8e8d-ec86352ce9e5.png)

注意：改变了主轴的方向，侧轴方向也随之改变。

### 5. 主轴换行方式

属性名：flex-wrap

常用值如下：

1. nowrap：默认值，不换行。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259272670-497c19e3-76b6-431d-86da-c373a6284fad.png)

2. wrap：自动换行，伸缩容器不够自动换行。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259277535-9b491462-947f-49a3-b6a4-fa25eb1b22d2.png)

3. wrap-reverse：反向换行。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259282429-1769cb00-f744-4e32-b11c-6ace68e04b72.png)

### 6. flex-flow

flex-flow是一个复合属性，复合了flex-direction和flex-wrap两个属性。值没有顺序要求。

```css
flex-flow: row wrap;
```

### 7. 主轴对齐方式

属性名：justify-content

常用值如下：

1. flex-start：主轴起点对齐。—— 默认值

2. flex-end：主轴终点对齐。

3. center：居中对齐

4. space-between：均匀分布，两端对齐（最常用）。

5. space-around：均匀分布，两端距离是中间距离的一半。

6. space-evenly：均匀分布，两端距离与中间距离一致。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259450266-82688666-80ef-4787-8ee2-4857c74813fc.png)

### 8. 侧轴对齐方式

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747148241105-c0b104e0-4cea-43b7-b487-8cb66b79196b.png)

还有设置换行的情况

#### 一行的情况

所需属性：align-items

常用值如下：

1. flex-start：侧轴的起点对齐。

2. flex-end：侧轴的终点对齐。

3. center：侧轴的中点对齐。

4. baseline: 伸缩项目的第一行文字的基线对齐。

5. stretch：如果伸缩项目**未设置高度**，将占满整个容器的高度。—— **（默认值）**

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259532835-a5587964-8b86-46b9-a2e7-2d6da5129740.png)

#### 多行的情况

所需属性：align-content

常用值如下：

1. flex-start：与侧轴的起点对齐。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259603860-7fa5ffd6-f766-4fec-905e-e80cb618f2ce.png)

2. flex-end：与侧轴的终点对齐。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259609616-eb915b7f-8dd8-4699-9d4f-3e92e4128349.png)

3. center：与侧轴的中点对齐。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259615529-bbf02194-0eb6-43dd-ad19-5b3eafb16a4b.png)

4. space-between：与侧轴两端对齐，中间平均分布。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1733105902176-3aaade63-708d-4de6-a0ab-1935ea6e9c43.png)

5. space-around：伸缩项目间的距离相等，比距边缘大一倍。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259622237-5e9f2ffd-1d6b-40a0-80bd-b7519887b9d3.png)

6. space-evenly: 在侧轴上完全平分。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259714248-31c6c049-dc60-454c-8a2b-64e5300ec422.png)

7. stretch：占满整个侧轴。—— 默认值

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732259706050-3fc6a16c-b796-492d-8f82-f08059402fb4.png)

### 9.flex实现水平垂直居中⭐

方法一：父容器开启 flex布局，随后使用 justify-content和 align-items实现水平垂直居中

```css
.outer {
width: 400px; height: 400px;
background-color: #888; display: flex;
justify-content: center; align-items: center;
}
.inner {
width: 100px; height: 100px;
background-color: orange;
}
```

方法二：父容器开启 flex布局，随后子元素margin:auto

```css
.outer {
width: 400px; height: 400px;
background-color: #888; display: flex;
}
.inner {
width: 100px; height: 100px;
background-color: orange; margin: auto;
}
```

### 10. 伸缩性

#### 1.1. flex-basis【初始长度】

概念： flex-basis设置的是主轴方向的**基准长度**，会让宽度或高度失效。

备注：主轴横向：宽度失效；主轴纵向：高度失效

作用：浏览器根据这个属性设置的值，计算主轴上是否有多余空间，默认值 auto，即：伸缩项目的宽或高。

`flex-basis` 的行为：

- `flex-basis: auto;`：默认值，项目的基准尺寸由它的内容决定。也就是元素的原始宽度（如果是块级元素则是宽度，如果是行内元素则是内容宽度）。
- `flex-basis: 0;`：使项目的基准尺寸为 0，此时项目的尺寸主要由 `flex-grow` 和 `flex-shrink` 控制。
- `flex-basis` 设置固定值：可以为 `flex-basis` 设置固定的像素值、百分比或其他单位，这时该值会作为项目的初始尺寸。

#### 1.2. flex-grow（伸）

概念：flex-grow定义伸缩项目的放大比例，**默认为** **0**，即：纵使主轴存在剩余空间，也不拉伸（放大）。

规则：【分剩余空间】

若所有伸缩项目的flex-grow值都为 **1** ，则：它们将**等分剩余空间**（如果有空间的话）。

若三个伸缩项目的 flex-grow 值分别为： 1 、 2 、 3 ，则：分别瓜分到：1/6、2/6、3/6的空间。

#### 1.3. flex-shrink（缩）

概念：flex-shrink定义了项目的压缩比例，默认为 1，即：如果空间不足，该项目将会缩小。

收缩项目的计算，略微复杂一点，我们拿一个场景举例：

例如：

三个收缩项目，宽度分别为： 200px、 300px、 200px，它们的 flex-shrink值分别为： 1 、 2 、 3

若想刚好容纳下三个项目，需要总宽度为 700px，但目前容器只有 400px，还差 300px

所以每个人都要收缩一下才可以放下，具体收缩的值，这样计算：

1. 计算分母： (200×1) + (300×2) + (200×3) = 1400

2. 计算比例：

项目一： (200×1) / 1400 = 比例值1

项目二： (300×2) / 1400 = 比例值2

项目三： (200×3) / 1400 = 比例值3

3. 计算最终收缩大小：

项目一需要收缩： 比例值1 × 300

项目二需要收缩： 比例值2 × 300

项目三需要收缩： 比例值3 × 300

### 11. flex复合属性

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747148360025-7401b068-37b1-4e6e-8e4e-ebb691649080.png)

flex 复合属性 ，复合了：flex-grow、flex-shrink、 flex-basis三个属性，默认值为 0 1 auto

如果写 flex:1 1 auto ，则可简写为： flex:auto

如果写 flex:1 1 0 ，则可简写为： flex:1

如果写 flex:0 0 auto ，则可简写为： flex:none

如果写 flex:0 1 auto，则可简写为： flex:0 auto—— 即flex 初始值

### 12. 项目排序

order属性定义项目的排列顺序。数值越小，排列越靠前，默认为 0。

### 13. 侧轴单独对齐

通过 align-self 属性，可以单独调整某个伸缩项目的【侧轴】对齐方式

默认值为auto，表示继承父元素的align-items 属性。
