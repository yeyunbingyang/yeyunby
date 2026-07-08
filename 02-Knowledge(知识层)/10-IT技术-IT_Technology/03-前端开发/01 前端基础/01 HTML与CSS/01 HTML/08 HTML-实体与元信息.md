---
title: HTML 实体与元信息
domain: IT_Technology
tags:
  - HTML
  - iframe
  - meta
  - 实体
status: 草稿
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[HTML-MOC]]"
summary: iframe框架在网页中嵌入其他页面，HTML实体用于显示特殊符号，meta元信息配置字符编码、SEO、视口等参数，常用全局属性包括id、class、style等。
---

## 框架标签

|   |   |   |   |
|---|---|---|---|
|**标签名**|**功能和语义**|**属性**|**单** **/** **双标****签**|
|iframe|框架（在网页中嵌入其他文件）|name：框架名字，可以与 target属性配合。<br><br>width： 框架的宽。<br><br>height： 框架的高度。 frameborder：是否显示边框，值：0或者1。|双|

iframe标签的实际应用：

1. 在网页中嵌入广告。

2. 与超链接或表单的 target配合，展示不同的内容。

## HTML实体

在 HTML中我们可以用一种**特殊的形式**的内容，来表示某个**符号**，这种特殊形式的内容，就是 HTML实体。比如小于号`<` 用于定义HTML标签的开始。如果我们希望浏览器正确地显示这些字符，我们必须在 HTML源码中插入字符实体。

**字符实体**由三部分组成：一个 &和 一个实体名称（或者一个 # 和 一个实体编号），最后加上一个分号 ; 。

常见字符实体总结：

|   |   |   |   |
|---|---|---|---|
||**描述**|**实体名称**|**实体编号**|
||**空格**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087781986-63631ab4-6847-4696-a483-a84076efedfa.png)|**&#160;**|
|**<**|**小于号**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087781956-8c7c9d43-8f7b-4622-8e67-ab014a9873ff.png)|**&#60;**|
|**>**|**大于号**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782103-f4194409-8b2b-4d09-985a-152891e21c22.png)|**&#62;**|
|**&**|**和号**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782118-22727a02-1773-4cef-a553-0ebd6f11cc01.png)|**&#38;**|
|"|引号|&quot;|&#34;|
|´|反引号|&acute;|&#180;|
|￠|分（cent）|&cent;|&#162;|
|£|镑（pound）|&pound;|&#163;|
|**¥**|**元****（****yen****）**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782127-e516d6b5-5e0d-4cb8-b57d-41e8401e1d00.png)|**&#165;**|
|€|欧元（euro）|&euro;|&#8364;|
|**©**|**版权****（****copyright****）**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782451-1a7440c6-7d65-487e-9f70-da1b8e3dcce2.png)|**&#169;**|
|®|注册商标|&reg;|&#174;|
|™|商标|&trade;|&#8482;|
|**×**|**乘号**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782604-0b905019-75e8-472b-85c2-a20620919817.png)|**&#215;**|
|**÷**|**除号**|![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732087782695-0efc2905-c894-4cdb-92d3-231b9a03dd1e.png)|**&#247;**|

完整实体列表，请参考： [**HTML Standard (whatwg.org)**](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references)

## HTML全局属性

常用的全局属性：

|   |   |
|---|---|
|**属性名**|**含义**|
|id|给标签指定唯一标识，注意： id是不能重复的。<br><br>作用：可以让 label标签与表单控件相关联；也可以与 CSS、 JavaScript配合使用，。|
|class|给标签指定类名，随后通过 CSS就可以给标签设置样式。|
|style|给标签设置 CSS样式。|
|dir|内容的方向，值: ltr、 rtl|
|title|给标签设置一个文字提示，一般超链接和图片用得比较多。|
|lang|给标签指定语言，具体规范和可选值请参考【10. HTML设置语言】。|

完整的全局属性，请参考： [**全局属性 - HTML（超文本标记语言） | MDN (mozilla.org)**](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes)

## ![](media/image121.png "null")meta 元信息

1. 配置字符编码

```
<meta charset="utf-8">
```

2. 针对 IE 浏览器的兼容性配置。

```
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

3. 针对移动端的配置（移动端课程中会详细讲解）

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

4. 配置网页关键字

```
<meta name="keywords" content="8-12个以英文逗号隔开的单词/词语">
```

5. 配置网页描述信息

```
<meta name="description" content="80字以内的一段话，与网站内容相关">
```

6. 针对搜索引擎爬虫配置：

```
<meta name="robots" content="此处可选值见下表">
```

|   |   |
|---|---|
|**值**|**描述**|
|index|允许搜索爬虫索引此页面。|
|noindex|要求搜索爬虫不索引此页面。|
|follow|允许搜索爬虫跟随此页面上的链接。|
|nofollow|要求搜索爬虫不跟随此页面上的链接。|
|all|与 index,follow等价|
|none|与 noindex,nofollow等价|
|noarchive|要求搜索引擎不缓存页面内容。|
|nocache|noarchive 的替代名称。|

7. 配置网页作者：

```
<meta name="author" content="tony">
```

8. 配置网页生成工具

```
<meta name="generator" content="Visual Studio Code">
```

9. 配置定义网页版权信息：

```
<meta name="copyright" content="2023-2027©版权所有">
```

10. 配置网页自动刷新

```
<meta http-equiv="refresh" content="10;url=http://www.baidu.com">
```

完整的网页元信息，请参考： [**文档级元数据元素** **|** **MDN**](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta)
