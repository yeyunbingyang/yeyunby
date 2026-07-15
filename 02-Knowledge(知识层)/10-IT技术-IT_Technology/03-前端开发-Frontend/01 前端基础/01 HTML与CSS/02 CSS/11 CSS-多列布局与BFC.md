---
title: CSS 多列布局与BFC
domain: IT_Technology
tags:
  - CSS
  - 多列布局
  - BFC
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[09 CSS-CSS3新增特性]]"
summary: 多列布局用于实现报纸式内容排版，BFC（块格式化上下文）是一种CSS渲染机制，可解决margin塌陷、浮动覆盖、高度塌陷等问题。
---

## 多列布局

作用：专门用于实现类似于报纸的布局。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732255807434-236763ae-a453-4a26-8b35-a0781517acba.png)

### 常用属性如下：

column-count：指定列数，值是数字。

column-width：指定列宽，值是长度。

columns：同时指定列宽和列数，复合属性；值没有数量和顺序要求。

column-gap：设置列边距，值是长度。

column-rule-style：设置列与列之间边框的风格，值与

column-rule-width：设置列与列之间边框的宽度，值是长度。

column-rule-color：设置列与列之间边框的颜色。

coumn-rule：设置列边框，复合属性。

## BFC

### 1. 什么是BFC

W3C上对 BFC的定义

原文：Floats, absolutely positioned elements, block containers (such as inline-blocks, table- cells, and table-captions) that are not block boxes, and block boxes with 'overflow' other than 'visible' (except when that value has been propagated to the viewport) establish new block formatting contexts for their contents.

译文：浮动、绝对定位元素、不是块盒子的块容器（如 inline-blocks 、 table-cells 和 table-captions），以及 overflow属性的值除 visible以外的块盒，将为其内容建立新的块格式化上下文。

MDN上对 BFC的描述：

**块格式化上下文（Block Formatting Context，BFC）** 是 Web页面的可视 CSS渲染的一部分，是块盒子的布局过程发生的区域，也是浮动元素与其他元素交互的区域。

更加通俗的描述：

1. BFC是 BlockFormattingContext（**块级格式上下文**），可以理解成元素的一个"特异功能"。

2. 该"特异功能"，在默认的情况下处于关闭状态；当元素满足了某些条件后，该"特异功能"被激活。

3.所谓激活"特异功能"，专业点说就是：该元素创建了 BFC（又称：开启了 BFC）。

### 2. 开启了BFC能解决什么问题

	1.元素开启后，其子元素不会再产生 margin塌陷问题。
	2. 元素开启后，自己不会被其他浮动元素所覆盖。
	3. 元素开启后，就算其子元素浮动，元素自身高度也不会塌陷。

### 3. 如何开启BFC

- 根元素
- 浮动元素
- 绝对定位、固定定位的元素
- 行内块元素
- 表格单元格： table、 thead、 tbody、tfoot、 th、 td、 tr、caption、overflow的值不为 visible 的块元素
- 伸缩项目
- 多列容器
- column-span为的 all 元素（即使该元素没有包裹在多列容器中）
- display的值，设置为flow-root
