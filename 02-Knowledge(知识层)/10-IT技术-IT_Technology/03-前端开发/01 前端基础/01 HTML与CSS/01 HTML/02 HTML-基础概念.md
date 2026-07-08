---
title: HTML 基础概念
domain: IT_Technology
tags:
  - HTML
  - 前端基础
  - 浏览器
status: 草稿
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[HTML-MOC]]"
summary: 计算机由硬件和软件构成，B/S架构是前端开发的核心模式，浏览器通过各自内核对网页进行解析渲染，HTML是一种超文本标记语言。
---

# 参考

## 参考课程

《尚硅谷禹神HTML+CSS前端基础》

[HTML4笔记.pdf](https://www.yuque.com/attachments/yuque/0/2024/pdf/40487410/1732021706287-82515f0d-47b0-47bd-9fdf-195768848741.pdf)

# 基础知识

## 计算机

1. 计算机俗称电脑，是现代一种用于高速计算的电子计算机器，可以进行数值计算、逻辑计算，还
    具有存储记忆功能。
2. 计算机由 硬件 + 软件 成：
    硬件：看得见摸得着的物理部件。
    软件：可以指挥硬件工作的指令。
3. 软件的分类：

4. 系统软件：Windows、Linux、Android、Harmony 等。
5. 应用软件：微信、QQ、王者荣耀、PhotoShop 等。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732078932404-c06344b1-785a-494a-9f2d-b98d20a19a8e.png)

## C/S架构与B/S架构

1. 上面提到的应用软件，又分为两大类：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732023579440-8fdc9698-de9a-451f-9c42-74377a5f023a.png)
**C/S架构**，特点：需要安装、偶尔更新、不跨平台、开发更具针对性。
**B/S架构**，特点：无需安装、无需更新、可跨平台、开发更具通用性。

名词解释：C => client（客户端）、B => browser（浏览器）、S => server（服务器）。
服务器 ：为软件提供数据的设备（在背后默默的付出）。

2. 前端工程师，主要负责编写 B/S架构中的网页（呈现界面、实现交互）。

备注：大前端时代，我们可以用前端的技术栈，做出一个C/S架构的应用、甚至搭建一个服务器😎

## 浏览器相关知识

浏览器是网页运行的平台，常见的浏览器有： `**谷歌(Chrome) 、 Safari 、 IE 、 火狐(Firefox) 、 欧 朋(Opera)**` 等，以上这些是常用的五大浏览器。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732024024162-ad6ba0d3-df26-419d-b750-ace3d72c490b.png)

都有自己的内核、市场份额大

1.各大浏览器市场份额：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732078919073-5b5730f2-6c15-4dcb-bafc-a935be227009.png)

2.常见浏览器的内核：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732078945503-3412f751-313a-4642-a889-d25d1d2f6082.png)

## 网页相关概念

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732024704582-d77686f2-339d-44ae-ac9c-16f754ba13b3.png)

1. 网址：我们在浏览器中输入的地址。
2. 网页：浏览器所呈现的每一个页面。
3. 网站：多个网页构成了一个网站。
4. 网页标准

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732024360162-62716287-f9e2-4b2a-92b5-c92460c63301.png)

# HTML 简介

## 1. 什么是 HTML？

全称：HyperTextMarkupLanguage（超文本标记语言）。

超文本：暂且简单理解为 "超级的文本"，和普通文本比，内容更丰富。

标 记：文本要变成超文本，就需要用到各种标记符号。

语 言：每一个标记的写法、读音、使用规则，组成了一个标记语言。

## 2. 相关国际组织（了解）

**1. IETF**

全称：InternetEngineeringTaskForce（国际互联网工程任务组），成立于1985年底，是一个权威的互联网技术标准化组织，主要负责互联网相关技术规范的研发和制定，当前绝大多数国际互联网技术标准均出自IETF。官网：[**https://www.ietf.org**](https://www.ietf.org/)

**2. W3C**

全称：WorldWideWebConsortium（**万维网联盟**），创建于1994年，是目前Web技术领域，最具影响力的技术标准机构。共计发布了200多项技术标准和实施指南，对互联网技术的发展和应用起到了基础性和根本性的支撑作用，官网：[**https://www.w3.org**](https://www.w3.org/)

**3. WHATWF**

全称：WebHypertextApplicationTechnologyWorkingGroup（网页超文本应用技术工作小组）成立于2004年，是一个以推动网络HTML5标准为目的而成立的组织。由Opera、Mozilla基金会、苹果，等这些浏览器厂商组成。官网： [**https://whatwg.org/**](https://whatwg.org/)

## 3. HTML发展历史（了解）

从 HTML1.0开始发展，期间经历了很多版本，目前HTML的最新标准是：HMTL5，具体发展史如图（了解即可）。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732079838818-1e1c390d-b41e-41bb-ba58-0856a615484e.png)
