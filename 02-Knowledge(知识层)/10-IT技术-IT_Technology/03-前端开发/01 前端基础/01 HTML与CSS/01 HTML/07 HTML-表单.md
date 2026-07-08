---
title: HTML 表单
domain: IT_Technology
tags:
  - HTML
  - 表单
  - form
status: 草稿
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[HTML-MOC]]"
summary: HTML表单通过form标签定义交互区域，包含文本输入框、密码框、单选/复选框、下拉框、文本域等控件，用于收集用户数据提交给服务器。
---

## 表单

概念：一个包含**交互的区域**，用于收集用户提供的数据。

### 基本结构

简单梳理：

|   |   |   |   |
|---|---|---|---|
|**标签名**|**标签****语义**|**常用属性**|**单** **/** **双****标签**|
|form|表单|action：用于指定表单的提交地址（需要与后端人员沟通后确定）。<br><br>target：用于控制表单提交后，如何打开页面，常用值如下：<br><br>_self：在本窗口打开。<br><br>_blank：在新窗口打开。<br><br>method：用于控制表单的提交方式，暂时只需了解，在后面<br><br>Ajax的课程中，会详细讲解。|双|
|input|输入框|type：设置输入框的类型，目前用到的值是 text，表示普通文本。<br><br>name：用于指定提交数据的名字，（需要与后端人员沟通后确定）。|单|
|button|按钮|本小节暂不涉及|双|

在本小节，我们先记住表单的整体形式，稍后会对表单控件进行详细讲解。

示例代码：

```
<form action="https://www.baidu.com/s" target="_blank" method="get">
  <input type="text" name="wd">
  <button>去百度搜索</button>
</form>
```

### 常用表单控件

**① 文本输入框**

```
<input type="text">
```

常用属性如下：

name属性：数据的名称。

value属性：输入框的默认输入值。

maxlength属性：输入框最大可输入长度。

**② 密码输入框**

```
<input type="password">
```

常用属性如下：

name属性：数据的名称。

value属性：输入框的默认输入值（一般不用，无意义）。

maxlength属性：输入框最大可输入长度。

**③ 单选框**

```
<input type="radio" name="sex" value="female">女
<input type="radio" name="sex" value="male">男
```

常用属性如下：

name属性：数据的名称，注意：想要单选效果，多个 radio的 name属性值要保持一致。

value属性：提交的数据值。

checked属性：让该单选按钮默认选中。

**④ 复选框**

```
<input type="checkbox" name="hobby" value="smoke">抽烟
<input type="checkbox" name="hobby" value="drink">喝酒
<input type="checkbox" name="hobby" value="perm">烫头
```

常用属性如下：：

name属性：数据的名称。

value属性：提交的数据值。

checked属性：让该复选框默认选中。

**⑤ 隐藏域**

```
<input type="hidden" name="tag" value="100">
```

用户不可见的一个输入区域，作用是： 提交表单的时候，携带一些固定的数据。

name属性：指定数据的名称。

value属性：指定的是真正提交的数据。

**⑥ 提交按钮**

```
<input type="submit" value="点我提交表单">
<button>点我提交表单</button>
```

注意：

1. button标签 type属性的默认值是 submit。

2. button不要指定 name属性

3. input标签编写的按钮，使用 value属性指定按钮文字。

**⑦ 重置按钮**

```
<input type="reset" value="点我重置">
<button type="reset">点我重置</button>
```

注意点：

1. button不要指定 name属性

2. input标签编写的按钮，使用 value属性指定按钮文字。

**⑧ 普通按钮**

```
<input type="button" value="普通按钮">
<button type="button">普通按钮</button>
```

注意点：普通按钮的 type值为 button，若不写 type值是 submit会引起表单的提交。

**⑨文本域**

```
<textarea name="msg" rows="22" cols="3">我是文本域</textarea>
```

常用属性如下：

1. rows属性：指定默认显示的行数，会影响文本域的高度。

2. cols属性：指定默认显示的列数，会影响文本域的宽度。

3. 不能编写 type属性，其他属性，与普通文本输入框一致。

**⑩ 下拉框**

```
<select name="from">
  <option value="黑">黑龙江</option>
  <option value="辽">辽宁</option>
  <option value="吉">吉林</option>
  <option value="粤" selected>广东</option>
</select>
```

常用属性及注意事项：

1. name属性：指定数据的名称。

2. option标签设置 value 属性， 如果没有 value属性，提交的数据是 option中间的文字；如果设置了 value属性，提交的数据就是 value 的值（建议设置 value 属性）

3. option标签设置了 selected属性，表示默认选中。

### 禁用表单控件

给表单控件的标签设置 disabled 既可禁用表单控件。

input、 textarea、 button、 select、 option都可以设置 disabled属性

### label 标签

label标签可与表单控件相关联，**关联之后点击文字**，与之对应的表单控件就会**获取焦点**。两种与 label关联方式如下：

1. 让 label标签的 for属性的值等于表单控件的 id。

2. 把表单控件套在 label标签的里面。

### fieldset 与 legend 的使用（了解）

fieldset可以为表单控件分组、 legend标签是分组的标题。

示例：

```
<fieldset>
  <legend>主要信息</legend>
  <label for="zhanghu">账户：</label>
  <input id="zhanghu" type="text" name="account" maxlength="10">
  <br>
  <label for="mima">密码：</label>
  <input id="mima" type="password" name="pwd" maxlength="6">
  <br>
  性别：
  <input type="radio" name="gender" value="male" id="nan">
  <label for="nan">男</label>
  <input type="radio" name="gender" value="female" id="nv">
  <label for="nv">女</label>
</fieldset>
```

### 表单总结

|   |   |   |   |   |
|---|---|---|---|---|
|**标签名**|   |**标签语义**|**常用属性**|   |
|form|   |表单|action属性： 表单要提交的地址。<br><br>target属性： 要跳转的新地址打开位置; 值: _self 、 _blank method 属性： 请求方式，值： get 、 post|   |
|input|   |多种形式的表单控件|type属性： 指定表单控件的类型。<br><br>值： text、 password、 radio、 checkbox、 hidden、 submit、 res button 等。<br><br>name属性： 指定数据名称<br><br>value属性：<br><br>对于输入框：指定默认输入的值；<br><br>对于单选和复选框：实际提交的数据；对于按钮：显示按钮文字。<br><br>disabled属性： 设置表单控件不可用。<br><br>maxlength属性： 用于输入框，设置最大可输入长度。<br><br>checked属性： 用于单选按钮和复选框，默认选中|   |
|textarea|   |文本域|name属性： 指定数据名称<br><br>rows 属性： 指定默认显示的行数，影响文本域的高度。<br><br>cols 属性： 指定默认显示的列数，影响文本域的宽度。<br><br>disabled 属性： 设置表单控件不可用。|   |
|select|   |下拉框|name属性： 指定数据名称<br><br>disabled属性： 设置整个下拉框不可用。|   |
|option|   |下拉框的选项|disabled属性： 设置拉下选项不可用。<br><br>value属性： 该选项事件提交的数据<br><br>（不指定value，会把标签中的内容作为提交数据）<br><br>selected属性： 默认选中。|   |
|button|   |按钮|disabled属性： 设置按钮不可用。<br><br>type属性： 设置按钮的类型，值： submit（默认）、 reset、 button|   |
|label|   |与表单控件做关联|for属性： 值与要关联的表单控件的ID值相同。|   |
|fieldset|   |表单边框||   |
