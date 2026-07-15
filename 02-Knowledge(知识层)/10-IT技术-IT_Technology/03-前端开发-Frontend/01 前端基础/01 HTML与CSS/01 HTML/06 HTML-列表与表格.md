---
title: HTML 列表与表格
domain: IT_Technology
tags:
  - HTML
  - 列表
  - 表格
status: 草稿
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[HTML-MOC]]"
summary: HTML列表分为有序、无序和自定义三种，表格由table/caption/thead/tbody/tfoot构成，支持跨行跨列操作。
---

## 列表

### 有序列表

概念：有顺序或侧重顺序的列表。

```
<h2>要把大象放冰箱总共分几步</h2>
<ol>
  <li>把冰箱门打开</li>
  <li>把大象放进去</li>
  <li>把冰箱门关上</li>
</ol>
```

### 无序列表

概念：无顺序或不侧重顺序的列表。

```
<h2>我想去的几个城市</h2>
<ul>
  <li>成都</li>
  <li>上海</li>
  <li>西安</li>
  <li>武汉</li>
</ul>
```

### 列表嵌套

概念：列表中的某项内容，又包含一个列表（注意：嵌套时，请务必把解构写完整）。

```
<h2>我想去的几个城市</h2>
<ul>
  <li>成都</li>
  <li>
    <span>上海</span>
    <ul>
      <li>外滩</li>
      <li>杜莎夫人蜡像馆</li>
      <li>
        <a href="https://www.opg.cn/">东方明珠</a>
      </li>
      <li>迪士尼乐园</li>
    </ul>
  </li>
  <li>西安</li>
  <li>武汉</li>
</ul>
```

注意： li 标签最好写在 ul 或 ol 中，不要单独使用。

### 自定义列表

1. ![](media/image78.png "null")![](media/image78.png "null")![](media/image79.png "null")概念：所谓自定义列表，就是一个包含**术语名称**以及**术语描述**的列表。
2. 一个 dl 就是一个自定义列表，一个 dt 就是一个术语名称，一个 dd 就是术语描述（可以有多个）。

```
<h2>如何高效的学习？</h2>
<dl>
<dt>做好笔记</dt>
<dd>笔记是我们以后复习的一个抓手</dd>
<dd>笔记可以是电子版，也可以是纸质版</dd>
<dt>多加练习</dt>
<dd>只有敲出来的代码，才是自己的</dd>
<dt>别怕出错</dt>
<dd>错很正常，改正后并记住，就是经验</dd>
</dl>
```

## 表格

### 基本结构

1. 一个完整的表格由：**表格标题**、**表格头部**、**表格主体**、**表格脚注**，四部分组成。

![](media/image80.jpeg "null")![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732085716841-d741efed-88c3-4cdd-a5b8-bcaeec7696bd.png)

2. 表格涉及到的标签：

table ：表格

caption：表格标题

thead：表格头部

tbody ：表格主体

tfoot：表格注脚

![](media/image32.png "null")tr ：每一行

![](media/image81.png "null")![](media/image81.png "null")th 、 td ：每一个单元格（备注：表格头部中用 th ，表格主体、表格脚注中用： td ）

- `**tr**` **(table row)**：表示表格中的一行。
- `**td**` **(table data)**：表示表格中的一个单元格，通常用于存储数据。
- `**th**` **(table header)**：表示表格中的一个表头单元格。

![](media/image83.jpeg "null")![](media/image84.jpeg "null")![](media/image85.jpeg "null")![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732085846804-bc38918e-e747-46ad-b4db-fc1b5ec0c136.png)

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732085852748-e46703be-5452-4c9f-a112-37eef49cbf3f.png)

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732085859434-d9d40cce-f459-4cc1-ae13-27e4d34aa7d5.png)

3. 具体编码：

```
<table border="1">
  <!-- 表格标题 -->
  <caption>学生信息</caption>
  <!-- 表格头部 -->
  <thead>
    <tr>
      <th>姓名</th>
      <th>性别</th>
      <th>年龄</th>
      <th>民族</th>
      <th>政治面貌</th>
    </tr>
  </thead>
  <!-- 表格主体 -->
  <tbody>
    <tr>
      <td>张三</td>
      <td>男</td>
      <td>18</td>
      <td>汉族</td>
      <td>团员</td>
    </tr>
    <tr>
      <td>李四</td>
      <td>女</td>
      <td>20</td>
      <td>满族</td>
      <td>群众</td>
    </tr>
    <tr>
      <td>王五</td>
      <td>男</td>
      <td>20</td>
      <td>回族</td>
      <td>党员</td>
    </tr>
    <tr>
      <td>赵六</td>
      <td>女</td>
      <td>21</td>
      <td>壮族</td>
      <td>团员</td>
    </tr>
  </tbody>
  <!-- 表格脚注 -->
  <tfoot>
    <tr>
      <td colspan="4"></td>
      <td>共计：4人</td>
    </tr>
  </tfoot>
</table>
```

### 常用属性

|   |   |   |   |
|---|---|---|---|
|**标签名**|**标签语义**|**常用属性**|**单** _**/**_ **双 标****签**|
|table|表格|width：设置表格宽度。<br><br>height：设置表格**最小**高度，表格最终高度可能比设置的值大。【头和脚高度不会变化】<br><br>border：设置外表格边框宽度。<br><br>cellspacing： 设置单元格之间的间距。|双|
|thead|表格头部|height：设置表格头部高度。<br><br>align： 设置单元格的**水平**对齐方式，可选值如下：<br><br>1. left：左对齐<br><br>2. center：中间对齐<br><br>3. right：右对齐<br><br>valign：设置单元格的**垂直**对齐方式，可选值如下：<br><br>1. top：顶部对齐<br><br>2. middle：中间对齐<br><br>3. bottom：底部对齐|双|
|tbody|表格主体|常用属性与 thead相同。|双|
|tr|行|常用属性与 thead相同。|双|
|tfoot|表格脚注|常用属性与 thead相同。|双|
|td|普通单元格|width：设置单元格的宽度，同列所有单元格全都受影响。<br><br>heigth：设置单元格的高度，同行所有单元格全都受影响。<br><br>align：设置单元格的水平对齐方式。 valign：设置单元格的垂直对齐方式。 rowspan：指定要跨的行数。<br><br>colspan：指定要跨的列数。|双|
|th|表头单元格|常用属性与 td相同。|双|

注意点：

1. <table> 元素的 border 属性可以控制表格边框，但 border 值的大小，并不控制单元格边框的宽度，只能控制表格最外侧边框的宽度，这个问题如何解决？—— 后期靠 CSS 控制。
2. 默认情况下，每列的宽度，得看这一列单元格最长的那个文字。
3. 给某个 th 或 td 设置了宽度之后，他们所在的那一列的宽度就确定了。
4. 给某个 th 或 td 设置了高度之后，他们所在的那一行的高度就确定了。

### 跨行跨列

1. rowspan ：指定要跨的行数。
2. colspan ：指定要跨的列数。

课程表效果：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732086089626-0c563984-053e-4522-acb3-45f2798a825d.png)

编写思路：

![](media/image95.png "null")![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732086108612-9a0be730-1d31-4a39-b056-ea6e52a57ad9.png)

## 常用标签补充

|   |   |   |
|---|---|---|
|**标签名**|**标签含义**|**单** **/** **双 标签**|
|br|换行|单|
|hr|分隔|单|
|pre|按原文显示（一般用于在页面中嵌入大段代码）|双|

注意点：

1. 不要用 <br>来增加文本之间的行间隔，应使用 <p> 元素，或后面即将学到的 CSS margin 属性。

2.<hr>的语义是分隔，如果不想要语义，只是想画一条水平线，那么应当使用 CSS完成。
