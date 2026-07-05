# SCSS（SASS）深度指南

> SCSS 是 SASS 的类 CSS 语法版本，是目前前端项目（Vue、React、Angular）中最主流的 CSS 预处理器。本指南以 SCSS 为核心，同时标注 LESS 的差异供参考。

---

## 一、为什么选 SCSS？

| 维度 | SCSS | LESS（对比参考） |
|------|------|-----------------|
| **语法** | 类 CSS（`{}` + `;`），零迁移成本 | 类 CSS，同样易上手 |
| **变量符号** | `$color: red;` | `@color: red;` |
| **社区生态** | ✅ Bootstrap、Vuetify、Element Plus 源码均用 SCSS | 早期流行，现新项目较少使用 |
| **框架支持** | ✅ Vue CLI / Vite / React 原生支持 | 需额外配置 |
| **功能丰富度** | ✅ 条件语句、循环、Map、模块化更完善 | 基础功能满足，高级特性缺失 |
| **维护状态** | ✅ Dart Sass 官方持续维护 | 社区活跃度下降 |

**结论：新项目无脑选 SCSS。**

---

## 二、SCSS 核心语法速查

### 2.1 变量（Variables）

```scss
$primary: #42b983;
$font-size-base: 16px;
$border-radius: 4px;

.btn {
  color: $primary;
  font-size: $font-size-base;
  border-radius: $border-radius;
}
```

> 作用域：先查找局部变量，再查找全局变量。

---

### 2.2 嵌套（Nesting）

```scss
.nav {
  padding: 10px;

  // 后代选择器
  ul {
    list-style: none;

    li {
      display: inline-block;

      // 父选择器引用 &
      &:hover {
        color: $primary;
      }
    }
  }

  // 生成 .nav.active
  &.active {
    background: #f0f0f0;
  }
}
```

> `&` 代表父选择器，可生成组合类名（如 `.nav.active`、`.btn-primary`）。

---

### 2.3 混合（Mixins）

```scss
// 定义
@mixin flex-center($direction: row) {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: $direction;
}

// 使用
.container {
  @include flex-center(column);
}
```

> Mixins 可带参数和默认值，适合封装重复样式逻辑。

---

### 2.4 继承（Extend）

```scss
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.message {
  @extend %message-shared;
}

.success {
  @extend %message-shared;
  border-color: green;
}
```

> `%` 为占位符选择器，不会单独输出 CSS。比 Mixin 更省代码体积（共用选择器）。

---

### 2.5 运算（Operations）

```scss
$base-width: 100px;

.col-2 {
  width: $base-width * 2;   // 200px
}

.col-half {
  width: $base-width / 2;   // 50px
}
```

---

### 2.6 内置函数（Built-in Functions）

```scss
$primary: #42b983;

.btn {
  background: $primary;
  color: white;

  &:hover {
    background: darken($primary, 10%);   // 加深 10%
  }

  &:disabled {
    background: lighten($primary, 20%);  // 变浅 20%
  }
}
```

| 常用函数 | 作用 |
|---------|------|
| `darken($color, $amount)` | 加深颜色 |
| `lighten($color, $amount)` | 变浅颜色 |
| `mix($color1, $color2, $weight)` | 混合两种颜色 |
| `rgba($color, $alpha)` | 设置透明度 |
| `str-length($string)` | 字符串长度 |

---

### 2.7 条件与循环（LESS 不支持）

```scss
// 条件语句
@mixin theme($mode) {
  @if $mode == dark {
    background: #000;
    color: #fff;
  } @else {
    background: #fff;
    color: #000;
  }
}

// for 循环
@for $i from 1 through 3 {
  .col-#{$i} {
    width: 100px * $i;
  }
}
// 输出: .col-1 { width: 100px; } .col-2 { width: 200px; } ...

// each 遍历 Map
$colors: (
  primary: #42b983,
  danger: #ff4d4f,
  warning: #faad14
);

@each $name, $color in $colors {
  .text-#{$name} {
    color: $color;
  }
}
```

---

### 2.8 模块化（@use / @forward）⭐ 推荐

```scss
// _variables.scss（下划线开头表示 partial，不单独编译）
$primary: #42b983;
$font-size: 16px;

@function rem($px) {
  @return $px / 16px * 1rem;
}

// styles.scss
@use 'variables' as v;

body {
  color: v.$primary;
  font-size: v.rem(32px);  // 调用命名空间下的变量和函数
}
```

> `@use` 替代旧的 `@import`，具备命名空间隔离，避免全局污染。

---

## 三、Vue 项目完整配置

### 3.1 安装依赖

```bash
npm install -D sass
```

> 只需安装 `sass`（Dart Sass），无需 `sass-loader`（Vite 已内置）。

### 3.2 组件中使用

lang="scss"

```vue
<template>
  <div class="card">
    <h1 class="title">Hello SCSS</h1>
  </div>
</template>

<style lang="scss" scoped>
$primary: #42b983;

.card {
  padding: 20px;
  background: lighten($primary, 45%);

  .title {
    color: $primary;
    font-weight: bold;
  }
}
</style>
```

### 3.3 Vite 全局变量配置

```js
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/styles/variables.scss" as *;`
      }
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
})
```

```scss
// src/styles/variables.scss
$primary: #42b983;
$danger: #ff4d4f;

@function rem($px) {
  @return $px / 16px * 1rem;
}
```

> `as *` 将命名空间导入全局，组件中可直接使用 `$primary` 而无需前缀。

---

## 四、SCSS vs LESS 语法速查对比

| 特性 | SCSS | LESS |
|------|------|------|
| 变量 | `$color: red;` | `@color: red;` |
| Mixin 定义 | `@mixin name {}` | `.name() {}` |
| Mixin 调用 | `@include name;` | `.name;` |
| 继承 | `@extend %placeholder;` | 不支持占位符 |
| 条件语句 | `@if / @else` | 有限支持（ guards ） |
| 循环 | `@for / @each / @while` | 有限支持（递归 Mixin） |
| 模块化 | `@use / @forward`（命名空间） | `@import`（全局污染） |
| Map | `$map: (key: value);` | 不支持 |
| 函数定义 | `@function name() {}` | 有限支持 |

---

## 五、最佳实践

1. **用 `@use` 替代 `@import`** — 避免全局命名冲突
2. **变量文件用 `_` 前缀** — 标记为 partial，不单独编译输出
3. **善用 `&` 父选择器** — 生成 BEM 类名如 `.btn { &--primary {} }` → `.btn--primary`
4. **Mixin vs Extend 选择** — 带参数用 Mixin，纯复用选 Extend（更省体积）
5. **函数封装常用计算** — 如 `rem()`、`vw()` 等响应式单位转换
