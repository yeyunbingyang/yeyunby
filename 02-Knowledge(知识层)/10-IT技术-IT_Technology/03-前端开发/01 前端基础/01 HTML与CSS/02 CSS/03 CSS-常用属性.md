---
title: CSS 常用属性
domain: IT_Technology
tags:
  - CSS
  - 字体
  - 文本
  - 背景
  - 颜色
status: 稳定
created: 2026-06-26
updated: 2026-06-26
source: 尚硅谷禹神HTML+CSS前端基础
related:
  - "[[CSS-MOC]]"
  - "[[04 CSS-盒模型]]"
summary: CSS常用属性包括像素概念、颜色表示（颜色名/rgb/hex/hsl）、字体控制、文本控制（颜色/间距/修饰/缩进/对齐/行高）、列表、表格、背景、鼠标、垂直对齐等属性。
---

## 四、CSS常用属性

### 1. 像素的概念

概念：我们的电脑屏幕是，是由一个一个"小点"组成的，每个"小点"，就是一个像素（px）。

规律：像素点越小，呈现的内容就越清晰、越细腻。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732244728260-6593733f-1620-480c-893e-4b37f948fdc1.png)

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732288519566-db4e5236-8c8c-4a79-bd49-64bfcbe5e1ee.png)

注意点：如果电脑设置中开启了缩放，那么就会影响一些工具的测量结果，但这无所谓，因为我们工作中都是参考详细的设计稿，去给元素设置宽高。

### 2.颜色的表示

#### 2.1 表示方式一：颜色名

编写方式：直接使用颜色对应的英文单词，编写比较简单，例如：

1. **红色：** `red`

2. **绿色：** `green`

3. **蓝色：** `blue`

4. **紫色：** `purple`

5. **橙色：** `orange`

6. **灰色：** `gray`

......

1. 颜色名这种方式，表达的颜色比较单一，所以用的并不多。

2. 具体颜色名参考 MDN官方文档：

[https://developer.mozilla.org/en-US/docs/Web/CSS/named-color](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)

#### 2.2 表示方式二：rgb或 rgba

编写方式：使用 **红、黄、蓝** 这三种光的三原色进行组合。

- **r** 表示 **红色**
- **g** 表示 **绿色**
- **b**表示 **蓝色**
- **a** 表示 **透明度**

**举例**

```css
/* 使用 0~255 之间的数字表示一种颜色 */
color: rgb(255, 0, 0);       /* 红色 */
color: rgb(0, 255, 0);       /* 绿色 */
color: rgb(0, 0, 255);       /* 蓝色 */
color: rgb(0, 0, 0);         /* 黑色 */
color: rgb(255, 255, 255);   /* 白色 */

/* 混合出任意一种颜色 */
color: rgb(138, 43, 226);           /* 紫罗兰色 */
color: rgba(255, 0, 0, 0.5);       /* 半透明的红色 */

/* 也可以使用百分比表示一种颜色（用的少） */
color: rgb(100%, 0%, 0%);           /* 红色 */
color: rgba(100%, 0%, 0%, 50%);     /* 半透明的红色 */
```

小规律：

1. 若三种颜色值相同，呈现的是灰色，值越大，灰色越浅。

2. rgb(0,0,0)是黑色， rgb(255,255,255)是白色。

3. 对于 rbga来说，前三位的 rgb形式要保持一致，要么都是 0~255的数字，要么都是

百分比 。

#### 2.3 表示方式三：HEX或 HEXA

HEX 的原理同与rgb 一样，依然是通过：**红**、**绿**、**蓝**色进行组合，只不过要用 **6 位（分成 3 组）** 来表达，格式为：`#rrggbb`

每一位数字的取值范围是： 0 ~ f ，即：（ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f）

所以每一种光的最小值是： 00，最大值是： ff

```css
color: #ff0000;/* 红色 */
color: #00ff00;/* 绿色 */
color: #0000ff;/* 蓝色 */
color: #000000;/* 黑色 */
color: #ffffff;/* 白色 */

/* 如果每种颜色的两位都是相同的，就可以简写*/
color: #ff9988;/* 可简为：#f98 */

/* 但要注意前三位简写了，那么透明度就也要简写 */
color: #ff998866;/* 可简为：#f986 */
```

注意点： IE浏览器不支持 HEXA，但支持 HEX。

#### 2.4 表示方式四：HSL或 HSLA

- HSL是通过：色相、饱和度、亮度，来表示一个颜色的，格式为：hsl(色相,饱和度,亮度)

- 色相：取值范围是 0~360度，具体度数对应的颜色如下图：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732245734414-8c32795c-891d-43d5-930d-8a32fa00d89e.png)

- 饱和度：取值范围是 0%~100%。（向色相中对应颜色中添加灰色， 0%全灰， 100%没有灰）
- 亮度：取值范围是 0%~100%。（0%亮度没了，所以就是黑色。 100%亮度太强，所以就是白色了）

- HSLA其实就是在HSL的基础上，添加了透明度。

### 3.CSS字体属性

#### 3.1 字体大小

属性名：font-size

作用：控制字体的大小。

语法：

```css
div {
  font-size: 40px;
}
```

注意点：

1. Chrome 浏览器支持的最小文字为 12px，默认的文字大小为 16px，并且 0px会自动消失。⭐

2. 不同浏览器默认的字体大小可能不一致，所以最好给一个明确的值，不要用默认大小。

3. 通常以给 body设置 font-size属性，这样 body中的其他元素就都可以继承了。

借助控制台看样式：

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732246247821-f0986ecf-78a6-40e3-8222-868099f292de.png)

#### 3.2 字体族

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747056608356-09f4499d-638e-4b15-8e29-33d5887cd034.png)

属性名：font-family

作用：控制字体类型。

语法：

```css
div {
  font-family: "STCaiyun","Microsoft YaHei",sans-serif
}
```

注意：

1. 使用字体的英文名字兼容性会更好，具体的英文名可以自行查询，或在电脑的设置里去寻找。

2. 如果字体名包含空格，必须使用引号包裹起来。

3. 可以设置多个字体，按照从左到右的顺序逐个查找，找到就用，没有找到就使用后面的，且通常在最后写上serif（衬线字体、顿笔字体）或sans-serif（非衬线字体）。

4. windows 系统中，默认的字体就是微软雅黑。

#### 3.3 字体风格

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747056435916-cae3b0c1-e708-4ae2-b250-716989d7ac33.png)

属性名：font-style

作用：控制字体是否为斜体。

常用值：

1. normal ：正常（默认值）
2. italic ：斜体（使用字体自带的斜体效果）
3. oblique ：斜体（强制倾斜产生的斜体效果）

实现斜体时，更推荐使用 italic。

语法：

```css
div {
  font-style: italic;
}
```

#### 3.4 字体粗细

属性名：font-weight

作用：控制字体的粗细。

常用值：

- 关键词 ：

1. lighter：细

2. normal： 正常

3. bold：粗

4.bolder：很粗 （多数字体不支持

- 数值：

1. 100~1000 且无单位，数值越大，字体越粗 （或一样粗，具体得看字体设计时的精确程度）。

2. 100~300等同于 lighter， 400~500等同于 normal， 600及以上等同于

bold。

语法：

```css
div {
  font-weight: bold;
}

div {
  font-weight: 600;
}
```

#### 3.5 字体复合写法

属性名： font，可以把上述字体样式合并成一个属性。

作用：将上述所有字体相关的属性复合在一起编写。

编写规则：

1.字体大小、字体族**必须**都写上。 否则 font 属性不生效

2. 字体族**必须**是最后一位、字体大小**必须**是倒数第二位。

3. 各个属性间用空格隔开。

实际开发中更推荐复合写法，但这也不是绝对的，比如只想设置字体大小，那就直接用font-size属性。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>05_字体复合属性</title>
    <style>
        .atguigu {
            font: bold italic 100px "STCaiyun","STHupo",sans-serif;
        }
    </style>
</head>
<body>
    <div class="atguigu">尚硅谷</div>
</body>
</html>
```

### 4.CSS文本属性

#### 4.1文本颜色

- 属性名：color
- 作用：控制文字的颜色。
- 可选值：

- 颜色名
- rgb 或 rgba
- hex 或 hexa （十六进制）
- hsl 或hsla

开发中常用的是： rgb/rgba或 HEX/HEXA（十六进制）。

举例：

```css
div {
color: rgb(112,45,78);
}
```

#### 4.2 文本间距

字母间距： letter-spacing

单词间距： word-spacing（通过空格识别词）

属性值为像素（px），正值让间距增大，负值让间距缩小。

#### 4.3 文本修饰

属性名：text-decoration

作用：控制文本的各种装饰线。

可选值：

1. **none**：无装饰线（常用）

2. **underline**：下划线（常用）

3. overline： 上划线

4. line-through： 删除线

可搭配如下值使用：

1. dotted：虚线

2. wavy：波浪线

3.也可以指定颜色

举例：

```css
a {
  text-decoration: none;
}
```

#### 4.4 文本缩进

属性名：text-indent。

作用：控制文本首字母的缩进。

属性值：CSS中的长度单位，例如：px

举例：

```css
div {
  text-indent:40px;
}
```

后面我们会学习 css中一些新的长度单位，目前我们只知道像素( px)。

#### 4.5文本对齐_水平

- 属性名： text-align。
- 作用：控制文本的水平对齐方式。
- 常用值：

1. left：左对齐（默认值）

2. right：右对齐

3.center：居中对齐

- 举例

```css
div {
  text-align: center;
}
```

#### 4.6 细说 font-size⭐

定义字体实际大小，即文字顶线（Top line）到底线（Bottom line）的垂直距离

1. 由于字体设计原因，文字最终呈现的大小，并不一定与 font-size的值一致，可能大，也可能小。

例如： font-size设为 40px，最终呈现的文字，可能比 40px大，也可能比 40px小。

2. 通常情况下，文字相对字体设计框，并不是垂直居中的，通常都靠下 一些。

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732536869389-5177d785-65ff-485f-af22-55815e74d774.png)

宽按比例变大

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732536964653-48b9e8cb-f659-4371-8def-cc82aae0fb8d.png)

![](https://cdn.nlark.com/yuque/0/2024/png/40487410/1732536986177-814ab16f-fc85-4cbf-9350-7608faea379f.png)

#### 4.7 行高⭐

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739430662584-12ee2b4d-1d4e-4b68-978d-3ddb4ec67421.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747056499745-4f84da6b-8916-45aa-b8f8-1b810b6ae427.png)

- 属性名：line-height
- 作用：控制一行文字的高度。控制行高，即两行文字基线间的距离。其计算方式为：**line-height = font-size + 行间距。单行是两个半行距。** 影响文本垂直间距和元素高度（未显式设置 `height` 时）
- 可选值：

1. normal：由浏览器根据文字大小决定的一个默认值。

2. 像素( px)。

3. 数字：参考自身 font-size的倍数（很常用）。⭐

4. 百分比：参考自身 font-size的百分比。

- 备注：由于字体设计原因，文字在一行中，并不是绝对垂直居中，若一行中都是文字，不会太影响观感。
- 举例

```css
div {
  line-height: 60px;
  line-height: 1.5;
  line-height: 150%;
}
```

- 行高注意事项⭐

1. line-height过小会怎样？line-height < font-size—— **文字产生重叠**，且最小值是 0，不能为负数。【行高中有字体大小】

2. line-height是可以继承的，且为了能更好的呈现文字，最好写数值。

3. line-height和 height是什么关系？【行高填充高度】

设置了 height，那么高度就是 height的值。

不设置 height的时候，会根据 line-height计算高度。

- 应用场景⭐

- 对于多行文字：控制行与行之间的距离
- 对于单行文字：让height等于line-height，可以实现文字垂直居中。

备注：由于字体设计原因，靠上述办法实现的居中，并不是绝对的垂直居中，但如果一行中都是文字，不会太影响观感。

- 关系及设置场景

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1746164487452-0b2e3af2-bb63-49db-ad80-5e9ee025e13b.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1746164647930-290d1fe8-211c-42ab-9f86-d2c8c9fb487a.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CSS 文本设置关系示例</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }

    h2 {
      margin-top: 40px;
      color: #333;
    }

    .example {
      margin: 10px 0;
      padding: 10px;
      color: #fff;
    }

    /* 背景色分类 */
    .bg-aqua { background-color: aqua; color: #000; }
    .bg-blue { background-color: rgb(43, 15, 201); }
    .bg-violet { background-color: blueviolet; }
    .bg-chartreuse { background-color: chartreuse; color: #000; }
    .bg-orange { background-color: darkorange; }

    /* 结构对比示例 */
    .h-50 { height: 50px; }
    .fs-20 { font-size: 20px; }
    .fs-50 { font-size: 50px; }
    .fs-60 { font-size: 60px; }
    .fs-90 { font-size: 90px; }

    .lh-20 { line-height: 20px; }
    .lh-50 { line-height: 50px; }
    .lh-60 { line-height: 60px; }
  </style>
</head>

<body>
  <h2>height 与 line-height 的关系</h2>
  <div class="example lh-20 bg-aqua">单行未设置</div>
  <div class="example lh-20 bg-blue">未设置<br>未设置<br>未设置</div>
  <div class="example h-50 lh-20 bg-violet">元素高度 &gt; 行高</div>
  <div class="example h-50 lh-50 bg-chartreuse">元素高度 = 行高</div>
  <div class="example h-50 lh-60 bg-orange">元素高度 &lt; 行高</div>

  <h2>height 与 font-size 的关系</h2>
  <div class="example h-50 fs-20 bg-violet">单行元素高度 &gt; 字体大小</div>
  <div class="example h-50 fs-20 bg-blue">多行元素高度 &gt; 字体大小<br>多行元素高度 &gt; 字体大小</div>
  <div class="example h-50 fs-50 bg-chartreuse">元素高度 = 字体大小</div>
  <div class="example h-50 fs-60 bg-orange">元素高度 &lt; 字体大小</div>

  <h2>line-height 与 font-size 的关系</h2>
  <div class="example lh-50 fs-20 bg-violet">单行行高 &gt; 字体大小</div>
  <div class="example lh-50 fs-20 bg-blue">多行行高 &gt; 字体大小<br>多行元素高度 &gt; 字体大小</div>
  <div class="example lh-50 fs-50 bg-chartreuse">行高 = 字体大小</div>
  <div class="example lh-50 fs-90 bg-orange">行高 &lt; 字体大小</div>
</body>

</html>
```

✅ 一、`height` 与 `line-height` 的关系

|   |   |
|---|---|
|场景|说明|
|**未设置 height，仅设置 line-height**|元素高度由 `line-height` 决定，单行文本上下有 line-height 的垂直空间。|
|**多行文本，未设置 height**|多行文本高度 = 行数 × `line-height`。每一行有固定的行间距。|
| `height > line-height` |文本偏向元素顶部（下方留白）|
| `height = line-height` |文本在容器内垂直居中，视觉上平衡。若多行，则溢出。可用于单行文本垂直居中。|
| `height < line-height` |文本偏向元素底部（上方留白）|

---

✅ 二、`height` 与 `font-size` 的关系

|   |   |
|---|---|
|场景|说明|
| `height > font-size` |容器高于字体大小，文字垂直对齐依赖于 `line-height`，默认可能偏上。|
|**多行文本，容器高于字体**|多行展示正常，行距由默认或指定的 `line-height` 控制。|
| `height = font-size` |容器刚好等于字体大小，若无额外 `line-height`，文字顶部和底部可能紧贴容器边缘。|
| `height < font-size` |字体超过容器，可能被裁剪，视觉效果不佳，不推荐。|

---

✅ 三、`line-height` 与 `font-size` 的关系

|                               |                                                                         |
| ----------------------------- | ----------------------------------------------------------------------- |
| 场景                            | 说明                                                                      |
| `line-height > font-size` | 正常行间距，推荐设置为 1.2–1.5 倍 font-size 以提升阅读体验。单行文字垂直居中，多余空间增加视觉留白，适用于按钮等居中场景。 |
| **多行文本，行高大于字体** | 行间距宽松，阅读体验更佳，适合段落文本。 |
| `line-height = font-size` | 行间距为 0，文字紧密排列但可能影响可读性。每行正好容纳文字，顶部与底部无留白，适合紧凑展示。 |
| `line-height < font-size` | 多行文本会重叠（行间距为负数）。行高不足以容纳大字号，文字重叠或被遮挡，严重影响可读性。 |

---

#### 4.8 文本垂直

**顶部：**无需任何属性，在垂直方向上，默认就是顶部对齐。

**居中：**对于单行文字，让height =line-height即可

问题：多行文字**垂直居中**怎么办？—— 后面我们用定位去做。

**底部：**对于多行文字，目前一个临时的方式：

让`line-height = (height * 2) - font-size -x`

备注： x是根据字体族，动态决定的一个值。

问题：垂直方向上的底部对齐，更好的解决办法是什么？——后面我们用定位去做。

#### 4.9 vertical-align⭐

【垂直对齐方式】

属性名： vertical-align。
作用：用于指定**同一行元素之间**，或 **表格单元格** 内文字的 **垂直对齐方式**。

常用值：

1. baseline（默认值）：使元素的基线与父元素的基线对齐。

2. top：使元素的**顶部**与其**所在行的顶部**对齐。

3. middle：使元素的**中部**与**父元素的基线**加上父元素**字母 X 的一半**对齐。

4.bottom：使元素的**底部**与其**所在行的底部**对齐。

特别注意： vertical-align不能控制块元素。【不能直接作用于文字】

### 5.CSS列表属性

列表相关的属性，可以作用在 ul、 ol、li元素上。

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|list-style-type|设置列表符号|常用值：none / square / disc / decimal / lower-roman / upper-roman / lower-alpha / upper-alpha|
|list-style-position|设置列表符号的位置|inside / outside|
|list-style-image|自定义列表符号|url(图片地址)|
|list-style|复合属性|没有数量、顺序的要求|

### 6.CSS表格属性

**1. 边框相关属性（其他元素也能用）：**

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|border-width|边框宽度|CSS中可用的长度值|
|border-color|边框颜色|CSS中可用的颜色值|
|border-style|边框风格|none / solid / dashed / dotted / double|
|border|边框复合属性|没有数量、顺序的要求|

注意：

1. 以上 4个边框相关的属性，其他元素也可以用，这是我们第一次遇见它们。

2. 在后面的盒子模型中，我们会详细讲解边框相关的知识。

**2. 表格独有属性（只有table 标签才能使用）：**

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|table-layout|设置列宽度|auto / fixed|
|border-spacing|单元格间距|CSS中可用的长度值。生效前提：单元格边框不能合并。|
|border-collapse|合并相邻单元格边框|collapse：合并 / separate：不合并|
|empty-cells|隐藏没有内容的单元格|show / hide。生效前提：单元格不能合并。|
|caption-side|设置表格标题位置|top / bottom|

以上 5个属性，只有表格才能使用，即： `<table>` 标签。

### 7.CSS背景属性⭐

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747064882962-367bbc9e-444c-46c1-a307-f1dd33bf8807.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747064847061-def3e9ae-3f71-4725-8714-2fb2ef7f3b71.png)

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|background-color|设置背景颜色|符合 CSS中颜色规范的值，默认 transparent。|
|background-image|设置背景图片|url(图片的地址)|
|background-repeat|设置背景重复方式|repeat / repeat-x / repeat-y / no-repeat|
|background-position|设置背景图位置|通过关键字（left/center/right + top/center/bottom）或坐标长度指定，只写一个值另一个方向默认 center|
|background|复合属性|没有数量和顺序要求|

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747064921731-9d9d3b16-da20-46e8-8a21-e27472c1f2cb.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747064940654-0f8d6766-c2d8-458a-a7f6-bd3b48de6695.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747064963056-934bd13c-26cd-431d-a04a-71aba0e36538.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747065030138-d3885718-727f-44a1-a6c7-f050782512b0.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747065049911-12b428ec-32b6-4f10-a954-e481c40e4126.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1747065064385-7fb132f5-c96f-4548-8379-3862c0446e6e.png)

### 8.CSS鼠标属性

|   |   |   |
|---|---|---|
|**CSS 属性名**|**功能**|**属性值**|
|cursor|设置鼠标光标的样式|pointer / move / text / crosshair / wait / help|

扩展：自定义鼠标图标

```css
/* 自定义鼠标光标 */
cursor: url("./arrow.png"),pointer;
```

### 9. 垂直对齐 vertical-align

| 属性值 | 含义 |
|--------|------|
| baseline | 默认值，元素基线与父元素基线对齐 |
| top | 元素顶端与行内最高元素顶端对齐 |
| middle | 元素中线与父元素基线 + x-height/2 对齐 |
| bottom | 元素底端与行内最低元素底端对齐 |

注意：vertical-align 只对 **行内元素**、**行内块元素**、**表格单元格**生效。

应用场景：
- 图片与文字垂直对齐（解决图片底部空白问题）
- 表格单元格内容垂直居中
