# CSS 预处理器

LESS 和 SASS 是两种主流的 **CSS 预处理器**，它们都扩展了原生 CSS 的功能（如变量、嵌套、函数、运算等），使样式代码更强大、更可维护，但它们之间有一些关键区别：

---

## 🆚 LESS vs SASS 对比表

|   |   |   |
|---|---|---|
|比较项|**LESS**|**SASS/SCSS**|
|**语法格式**|类似 CSS，易于上手|有两种语法：SASS（缩进）和 SCSS（类 CSS）|
|**文件扩展名**|`.less`|`.sass`<br><br>（缩进）或 `.scss`<br><br>（类 CSS）|
|**运行环境**|主要依赖 Node.js|主要依赖 Dart Sass 或 LibSass|
|**变量定义**|使用 `@`<br><br>（如：`@color: red;`<br><br>）|使用 `$`<br><br>（如：`$color: red;`<br><br>）|
|**社区支持**|较早期流行，现使用较少|使用更广泛，Vue、React 官方推荐|
|**特性丰富度**|功能较少，基本满足常用需求|特性更多（如条件语句、循环、模块化更好）|
|**兼容性**|易上手、兼容性好|更强大，但学习成本略高|
|**常用场景**|老项目、简单样式|新项目、复杂组件化开发|

---

## ✅ 语法差异示例

### 🔹 变量

**LESS：**

```
@mainColor: #42b983;

body {
  color: @mainColor;
}
```

**SCSS：**

```
$mainColor: #42b983;

body {
  color: $mainColor;
}
```

---

### 🔹 嵌套

**LESS 和 SCSS 都支持：**

```
.nav {
  ul {
    li {
      color: red;
    }
  }
}
```

```
.nav {
  ul {
    li {
      color: red;
    }
  }
}
```

---

### 🔹 混合（Mixin）

**LESS：**

```
.rounded(@radius) {
  border-radius: @radius;
}

.box {
  .rounded(5px);
}
```

**SCSS：**

```
@mixin rounded($radius) {
  border-radius: $radius;
}

.box {
  @include rounded(5px);
}
```

---

### 🔹 循环（SCSS 支持更多）

**SCSS：**

```
@for $i from 1 through 3 {
  .col-#{$i} {
    width: 100px * $i;
  }
}
```

LESS 不支持类似原生的 `@for` 循环。

---

## ✅ 总结推荐

|                 |            |
| --------------- | ---------- |
| 使用场景            | 推荐         |
| 简单项目、低学习成本      | ✅ LESS     |
| Vue/React、现代前端  | ✅ SCSS（推荐） |
| 需要强大功能（循环、模块化等） | ✅ SCSS     |

---

📌 **Vue 项目中推荐使用 SCSS**，因为：

- Vue CLI 支持非常好（无需额外插件）
- 社区资源丰富（如 Bootstrap、Vuetify、Element Plus 等都使用 SCSS）

如你使用的是 Vue 项目，可以通过配置 `lang="scss"` 来直接使用 SCSS。

是否需要我给你一个 Vue 中使用 SCSS 的实际示例？

# Vue 项目中使用 SCSS

好的！下面是一个 Vue 项目中使用 **SCSS** 的完整示例，包括组件代码、项目依赖配置以及开发注意点。

---

## ✅ 1. 安装 SCSS 依赖

在 Vue 项目根目录下运行（如果用的是 Vue CLI 创建的项目）：

```
npm install -D sass sass-loader
```

⚠️ 注意：`node-sass` 已过时，使用 `sass`（Dart Sass）才是官方推荐。

---

## ✅ 2. 在 Vue 组件中使用 `lang="scss"`

```
<!-- src/components/HelloWorld.vue -->
<template>
  <div class="card">
    <h1 class="title">Hello, SCSS!</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld'
}
</script>

<style lang="scss" scoped>
$mainColor: #42b983;
$titleSize: 24px;

.card {
  padding: 20px;
  background: lighten($mainColor, 40%);

  .title {
    color: $mainColor;
    font-size: $titleSize;
    font-weight: bold;
    border-bottom: 2px solid darken($mainColor, 10%);
  }
}
</style>
```

---

## ✅ 3. SCSS 全局变量文件（可选）

如果你有多个组件需要复用颜色、字体大小等变量，推荐使用 **全局 SCSS 变量文件**。

### 创建全局变量文件

```
// src/assets/styles/variables.scss
$primary: #42b983;
$fontSizeBase: 16px;
```

### 配置自动引入（Vue CLI）

打开 `vue.config.js`：

```
module.exports = {
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "@/assets/styles/variables.scss";`
      }
    }
  }
}
```

这样每个组件都自动注入变量，无需手动 `@import`。

---

## ✅ 4. 使用 SCSS 的好处

- 嵌套清晰，结构直观
- 变量、函数增强复用
- 模块化 + 全局变量结合更高效
- 社区广泛支持，兼容 Vue、React、Vite、Webpack