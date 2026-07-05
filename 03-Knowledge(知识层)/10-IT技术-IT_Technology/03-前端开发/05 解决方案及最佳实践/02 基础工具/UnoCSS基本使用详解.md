# UnoCSS 基本使用详解

> 原子化 CSS = **把样式拆成最小不可再分的"功能积木"**

---

## 目录

1. [安装与启动](#1-安装与启动)
2. [最基础的类名用法](#2-最基础的类名用法)
3. [布局类名](#3-布局类名)
4. [间距类名](#4-间距类名)
5. [文字样式类名](#5-文字样式类名)
6. [颜色与背景](#6-颜色与背景)
7. [边框与圆角](#7-边框与圆角)
8. [尺寸类名](#8-尺寸类名)
9. [响应式设计](#9-响应式设计)
10. [状态变体](#10-状态变体)
11. [完整实战 Demo](#11-完整实战-demo)

---

## 1. 安装与启动

### 1.1 创建 Vite 项目（推荐）

```bash
# 创建项目
npm create vite@latest my-unocss-app -- --template vanilla-ts
cd my-unocss-app

# 安装 UnoCSS
npm install -D unocss

# 安装预设（核心功能）
npm install -D @unocss/preset-uno @unocss/preset-attributify @unocss/preset-icons
```

### 1.2 配置文件

创建 `uno.config.ts`：

```ts
import { defineConfig } from 'unocss'
import presetUno from '@unocss/preset-uno'
import presetAttributify from '@unocss/preset-attributify'
import presetIcons from '@unocss/preset-icons'

export default defineConfig({
  presets: [
    presetUno(),           // 核心预设，提供所有基础类名
    presetAttributify(),   // 属性化写法（可选）
    presetIcons(),         // 图标支持（可选）
  ],
})
```

### 1.3 Vite 配置

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import UnoCSS from 'unocss/vite'

export default defineConfig({
  plugins: [
    UnoCSS(),
  ],
})
```

### 1.4 入口文件引入

```ts
// main.ts
import 'virtual:uno.css'

// 你的其他代码...
```

### 1.5 启动项目

```bash
npm run dev
```

---

## 2. 最基础的类名用法

### 2.1 类名 = "功能积木"

每个类名只做一件事，像搭积木一样拼起来：

```html
<!-- 一个普通的按钮 -->
<button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
  点击我
</button>
```

拆解一下这个按钮用了哪些"积木"：

| 类名 | 作用 | 生成的 CSS |
|------|------|-----------|
| `px-4` | 水平内边距 1rem（16px） | `padding-left: 1rem; padding-right: 1rem` |
| `py-2` | 垂直内边距 0.5rem（8px） | `padding-top: 0.5rem; padding-bottom: 0.5rem` |
| `bg-blue-500` | 背景色蓝色 | `background-color: #3b82f6` |
| `text-white` | 文字白色 | `color: #ffffff` |
| `rounded` | 圆角 | `border-radius: 0.25rem` |
| `hover:bg-blue-600` | 鼠标悬停时背景变深 | `:hover { background-color: #2563eb }` |

### 2.2 数字规律

大部分数字类名遵循 **除以 4 = rem** 的规律：

| 类名 | 实际值 | 像素值 |
|------|--------|--------|
| `p-1` | 0.25rem | 4px |
| `p-2` | 0.5rem | 8px |
| `p-3` | 0.75rem | 12px |
| `p-4` | 1rem | 16px |
| `p-6` | 1.5rem | 24px |
| `p-8` | 2rem | 32px |
| `p-10` | 2.5rem | 40px |
| `p-12` | 3rem | 48px |

> 记忆口诀：**数字 ÷ 4 = rem，rem × 16 = px**

---

## 3. 布局类名

### 3.1 Flex 布局

```html
<!-- 横向排列，居中对齐 -->
<div class="flex items-center justify-between">
  <div>左边</div>
  <div>右边</div>
</div>

<!-- 纵向排列 -->
<div class="flex flex-col gap-4">
  <div>第一项</div>
  <div>第二项</div>
  <div>第三项</div>
</div>

<!-- 换行布局 -->
<div class="flex flex-wrap gap-4">
  <div class="w-32">卡片1</div>
  <div class="w-32">卡片2</div>
  <div class="w-32">卡片3</div>
</div>
```

**常用 Flex 类名**：

| 类名 | 作用 |
|------|------|
| `flex` | 开启 flex 布局 |
| `flex-col` | 纵向排列（column） |
| `flex-row` | 横向排列（row，默认） |
| `flex-wrap` | 允许换行 |
| `flex-nowrap` | 不允许换行 |
| `items-start` | 垂直方向顶部对齐 |
| `items-center` | 垂直方向居中对齐 |
| `items-end` | 垂直方向底部对齐 |
| `justify-start` | 水平方向左对齐 |
| `justify-center` | 水平方向居中对齐 |
| `justify-end` | 水平方向右对齐 |
| `justify-between` | 两端对齐 |
| `justify-around` | 均匀分布 |
| `gap-4` | 子元素间距 1rem |

### 3.2 Grid 布局

```html
<!-- 3 列等宽网格 -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-red-100 p-4">1</div>
  <div class="bg-blue-100 p-4">2</div>
  <div class="bg-green-100 p-4">3</div>
</div>

<!-- 响应式网格：手机 1 列，平板 2 列，电脑 3 列 -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
  <div>卡片1</div>
  <div>卡片2</div>
  <div>卡片3</div>
</div>

<!-- 不等宽网格 -->
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-2 bg-blue-100">占 2 列</div>
  <div class="col-span-1 bg-red-100">占 1 列</div>
  <div class="col-span-1 bg-green-100">占 1 列</div>
</div>
```

**常用 Grid 类名**：

| 类名 | 作用 |
|------|------|
| `grid` | 开启 grid 布局 |
| `grid-cols-2` | 2 列 |
| `grid-cols-3` | 3 列 |
| `grid-cols-4` | 4 列 |
| `grid-cols-12` | 12 列（常用） |
| `col-span-2` | 跨 2 列 |
| `col-span-full` | 跨全部列 |
| `gap-4` | 网格间距 |
| `row-gap-4` | 行间距 |
| `col-gap-4` | 列间距 |

### 3.3 定位

```html
<!-- 相对定位 + 绝对定位 -->
<div class="relative w-64 h-64 bg-gray-200">
  <div class="absolute top-4 left-4 bg-red-500 text-white px-2 py-1">
    左上角
  </div>
  <div class="absolute bottom-4 right-4 bg-blue-500 text-white px-2 py-1">
    右下角
  </div>
  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-green-500 text-white px-2 py-1">
    正中间
  </div>
</div>

<!-- 固定定位（导航栏） -->
<nav class="fixed top-0 left-0 right-0 bg-white shadow z-50">
  固定在顶部的导航
</nav>
```

**常用定位类名**：

| 类名 | 作用 |
|------|------|
| `relative` | 相对定位 |
| `absolute` | 绝对定位 |
| `fixed` | 固定定位 |
| `sticky` | 粘性定位 |
| `top-0` | 距顶部 0 |
| `bottom-4` | 距底部 1rem |
| `left-1/2` | 距左边 50% |
| `right-0` | 距右边 0 |
| `z-10` | 层级 10 |
| `z-50` | 层级 50（最高） |

---

## 4. 间距类名

### 4.1 内边距（Padding）

```html
<!-- 四边内边距 -->
<div class="p-4">四周都是 16px</div>

<!-- 单边内边距 -->
<div class="pt-4">上边 16px</div>
<div class="pr-4">右边 16px</div>
<div class="pb-4">下边 16px</div>
<div class="pl-4">左边 16px</div>

<!-- 水平/垂直内边距 -->
<div class="px-4">左右 16px</div>
<div class="py-4">上下 16px</div>

<!-- 组合写法 -->
<div class="px-6 py-4">左右 24px，上下 16px</div>
```

**Padding 缩写规则**：

| 缩写 | 全称 | 方向 |
|------|------|------|
| `p` | padding | 四边 |
| `px` | padding-x | 左右 |
| `py` | padding-y | 上下 |
| `pt` | padding-top | 上 |
| `pr` | padding-right | 右 |
| `pb` | padding-bottom | 下 |
| `pl` | padding-left | 左 |

### 4.2 外边距（Margin）

```html
<!-- 四边外边距 -->
<div class="m-4">四周都是 16px</div>

<!-- 单边外边距 -->
<div class="mt-4">上边距 16px</div>
<div class="mr-4">右边距 16px</div>
<div class="mb-4">下边距 16px</div>
<div class="ml-4">左边距 16px</div>

<!-- 水平/垂直外边距 -->
<div class="mx-4">左右外边距 16px</div>
<div class="my-4">上下外边距 16px</div>

<!-- 自动居中 -->
<div class="mx-auto w-64">水平居中，宽度 256px</div>

<!-- 负外边距 -->
<div class="-mt-4">向上移动 16px</div>
```

**Margin 缩写规则**：

| 缩写 | 全称 | 方向 |
|------|------|------|
| `m` | margin | 四边 |
| `mx` | margin-x | 左右 |
| `my` | margin-y | 上下 |
| `mt` | margin-top | 上 |
| `mr` | margin-right | 右 |
| `mb` | margin-bottom | 下 |
| `ml` | margin-left | 左 |
| `mx-auto` | margin-x auto | 水平居中 |

---

## 5. 文字样式类名

### 5.1 字体大小

```html
<p class="text-xs">超小字 12px</p>
<p class="text-sm">小字 14px</p>
<p class="text-base">正常 16px</p>
<p class="text-lg">大字 18px</p>
<p class="text-xl">更大 20px</p>
<p class="text-2xl">2倍 24px</p>
<p class="text-3xl">3倍 30px</p>
<p class="text-4xl">4倍 36px</p>
<p class="text-5xl">5倍 48px</p>
```

### 5.2 字体粗细

```html
<p class="font-thin">极细 100</p>
<p class="font-light">细体 300</p>
<p class="font-normal">正常 400</p>
<p class="font-medium">中等 500</p>
<p class="font-semibold">半粗 600</p>
<p class="font-bold">粗体 700</p>
<p class="font-extrabold">特粗 800</p>
```

### 5.3 文字颜色

```html
<p class="text-gray-500">灰色</p>
<p class="text-red-500">红色</p>
<p class="text-blue-500">蓝色</p>
<p class="text-green-500">绿色</p>
<p class="text-yellow-500">黄色</p>
<p class="text-purple-500">紫色</p>
<p class="text-pink-500">粉色</p>
```

### 5.4 文字对齐

```html
<p class="text-left">左对齐</p>
<p class="text-center">居中</p>
<p class="text-right">右对齐</p>
<p class="text-justify">两端对齐</p>
```

### 5.5 文字装饰

```html
<p class="underline">下划线</p>
<p class="line-through">删除线</p>
<p class="no-underline">无装饰</p>
<p class="uppercase">全大写</p>
<p class="lowercase">全小写</p>
<p class="capitalize">首字母大写</p>
<p class="truncate">超出省略...</p>
<p class="break-words">自动换行</p>
```

### 5.6 行高与字间距

```html
<p class="leading-none">行高 1</p>
<p class="leading-tight">行高 1.25</p>
<p class="leading-normal">行高 1.5</p>
<p class="leading-relaxed">行高 1.625</p>
<p class="leading-loose">行高 2</p>

<p class="tracking-tight">字间距紧凑</p>
<p class="tracking-normal">字间距正常</p>
<p class="tracking-wide">字间距宽松</p>
```

---

## 6. 颜色与背景

### 6.1 颜色体系

UnoCSS 使用 Tailwind 的颜色体系，每种颜色有 11 个色阶（50-950）：

```html
<!-- 红色系 -->
<div class="bg-red-50">最浅红</div>
<div class="bg-red-100">很浅红</div>
<div class="bg-red-200">浅红</div>
<div class="bg-red-300">较浅红</div>
<div class="bg-red-400">浅红</div>
<div class="bg-red-500">标准红</div>
<div class="bg-red-600">深红</div>
<div class="bg-red-700">较深红</div>
<div class="bg-red-800">很深红</div>
<div class="bg-red-900">最深红</div>
<div class="bg-red-950">极深红</div>
```

**常用颜色**：

| 颜色名 | 用途 |
|--------|------|
| `slate` | 石板灰（偏蓝灰） |
| `gray` | 灰色 |
| `zinc` | 锌灰（偏暖灰） |
| `neutral` | 中性灰 |
| `stone` | 石色（偏黄灰） |
| `red` | 红色 |
| `orange` | 橙色 |
| `amber` | 琥珀色 |
| `yellow` | 黄色 |
| `lime` | 青柠色 |
| `green` | 绿色 |
| `emerald` | 翠绿色 |
| `teal` | 蓝绿色 |
| `cyan` | 青色 |
| `sky` | 天蓝色 |
| `blue` | 蓝色 |
| `indigo` | 靛蓝色 |
| `violet` | 紫罗兰色 |
| `purple` | 紫色 |
| `fuchsia` | 紫红色 |
| `pink` | 粉色 |
| `rose` | 玫瑰色 |

### 6.2 背景色

```html
<div class="bg-white">白色背景</div>
<div class="bg-black">黑色背景</div>
<div class="bg-transparent">透明背景</div>
<div class="bg-gray-100">浅灰背景</div>
<div class="bg-blue-500">蓝色背景</div>
<div class="bg-red-500/50">半透明红色背景（50% 透明度）</div>
```

### 6.3 背景渐变

```html
<!-- 线性渐变 -->
<div class="bg-gradient-to-r from-blue-500 to-purple-500">
  从左到右渐变
</div>

<div class="bg-gradient-to-br from-red-400 via-pink-500 to-purple-600">
  从左上到右下，中间经过粉色
</div>

<!-- 径向渐变 -->
<div class="bg-radial from-yellow-200 to-orange-400">
  径向渐变
</div>

<!-- 角度渐变 -->
<div class="bg-conic from-red-500 via-green-500 to-blue-500">
  圆锥渐变
</div>
```

**渐变方向**：

| 类名 | 方向 |
|------|------|
| `bg-gradient-to-t` | 下到上 |
| `bg-gradient-to-tr` | 左下到右上 |
| `bg-gradient-to-r` | 左到右 |
| `bg-gradient-to-br` | 左上到右下 |
| `bg-gradient-to-b` | 上到下 |
| `bg-gradient-to-bl` | 右上到左下 |
| `bg-gradient-to-l` | 右到左 |
| `bg-gradient-to-tl` | 右下到左上 |

---

## 7. 边框与圆角

### 7.1 边框

```html
<!-- 边框宽度 -->
<div class="border">1px 边框</div>
<div class="border-2">2px 边框</div>
<div class="border-4">4px 边框</div>
<div class="border-8">8px 边框</div>

<!-- 单边边框 -->
<div class="border-t">上边框</div>
<div class="border-r">右边框</div>
<div class="border-b">下边框</div>
<div class="border-l">左边框</div>

<!-- 边框颜色 -->
<div class="border border-red-500">红色边框</div>
<div class="border-2 border-blue-500">蓝色粗边框</div>

<!-- 边框样式 -->
<div class="border border-dashed">虚线边框</div>
<div class="border border-dotted">点线边框</div>
<div class="border border-double">双线边框</div>
```

### 7.2 圆角

```html
<div class="rounded">小圆角 4px</div>
<div class="rounded-md">中圆角 6px</div>
<div class="rounded-lg">大圆角 8px</div>
<div class="rounded-xl">超大圆角 12px</div>
<div class="rounded-2xl">2xl 圆角 16px</div>
<div class="rounded-3xl">3xl 圆角 24px</div>
<div class="rounded-full">完全圆形/椭圆</div>
<div class="rounded-none">无圆角</div>

<!-- 单边圆角 -->
<div class="rounded-t-lg">顶部圆角</div>
<div class="rounded-b-lg">底部圆角</div>
<div class="rounded-l-lg">左边圆角</div>
<div class="rounded-r-lg">右边圆角</div>
```

### 7.3 阴影

```html
<div class="shadow">小阴影</div>
<div class="shadow-sm">更小阴影</div>
<div class="shadow-md">中等阴影</div>
<div class="shadow-lg">大阴影</div>
<div class="shadow-xl">超大阴影</div>
<div class="shadow-2xl">2xl 阴影</div>
<div class="shadow-none">无阴影</div>
<div class="shadow-inner">内阴影</div>
```

---

## 8. 尺寸类名

### 8.1 宽度

```html
<!-- 固定宽度 -->
<div class="w-0">0</div>
<div class="w-px">1px</div>
<div class="w-1">0.25rem (4px)</div>
<div class="w-4">1rem (16px)</div>
<div class="w-8">2rem (32px)</div>
<div class="w-12">3rem (48px)</div>
<div class="w-16">4rem (64px)</div>
<div class="w-24">6rem (96px)</div>
<div class="w-32">8rem (128px)</div>
<div class="w-48">12rem (192px)</div>
<div class="w-64">16rem (256px)</div>
<div class="w-96">24rem (384px)</div>

<!-- 百分比宽度 -->
<div class="w-1/2">50%</div>
<div class="w-1/3">33.33%</div>
<div class="w-2/3">66.66%</div>
<div class="w-1/4">25%</div>
<div class="w-3/4">75%</div>
<div class="w-full">100%</div>

<!-- 特殊宽度 -->
<div class="w-screen">屏幕宽度</div>
<div class="w-min">最小内容宽度</div>
<div class="w-max">最大内容宽度</div>
<div class="w-fit">适应内容宽度</div>
<div class="w-auto">自动宽度</div>
```

### 8.2 高度

```html
<!-- 固定高度 -->
<div class="h-4">1rem (16px)</div>
<div class="h-8">2rem (32px)</div>
<div class="h-12">3rem (48px)</div>
<div class="h-16">4rem (64px)</div>
<div class="h-24">6rem (96px)</div>
<div class="h-32">8rem (128px)</div>
<div class="h-48">12rem (192px)</div>
<div class="h-64">16rem (256px)</div>

<!-- 百分比高度 -->
<div class="h-1/2">50%</div>
<div class="h-full">100%</div>

<!-- 特殊高度 -->
<div class="h-screen">屏幕高度</div>
<div class="h-min">最小内容高度</div>
<div class="h-max">最大内容高度</div>
<div class="h-fit">适应内容高度</div>
<div class="h-auto">自动高度</div>
```

### 8.3 最大/最小尺寸

```html
<!-- 最大宽度 -->
<div class="max-w-xs">最大 320px</div>
<div class="max-w-sm">最大 384px</div>
<div class="max-w-md">最大 448px</div>
<div class="max-w-lg">最大 512px</div>
<div class="max-w-xl">最大 576px</div>
<div class="max-w-2xl">最大 672px</div>
<div class="max-w-3xl">最大 768px</div>
<div class="max-w-4xl">最大 896px</div>
<div class="max-w-5xl">最大 1024px</div>
<div class="max-w-6xl">最大 1152px</div>
<div class="max-w-7xl">最大 1280px</div>
<div class="max-w-full">最大 100%</div>
<div class="max-w-screen-sm">最大屏幕 sm 宽度</div>
<div class="max-w-screen-md">最大屏幕 md 宽度</div>
<div class="max-w-screen-lg">最大屏幕 lg 宽度</div>
<div class="max-w-screen-xl">最大屏幕 xl 宽度</div>

<!-- 最小高度 -->
<div class="min-h-0">最小 0</div>
<div class="min-h-full">最小 100%</div>
<div class="min-h-screen">最小屏幕高度</div>
```

---

## 9. 响应式设计

### 9.1 断点系统

```html
<!-- 默认：手机端 -->
<!-- sm: 640px 以上 -->
<!-- md: 768px 以上 -->
<!-- lg: 1024px 以上 -->
<!-- xl: 1280px 以上 -->
<!-- 2xl: 1536px 以上 -->

<div class="text-sm sm:text-base md:text-lg lg:text-xl">
  手机小字 → 平板正常 → 电脑大字
</div>

<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
  手机 1 列 → 平板 2 列 → 电脑 3 列 → 大屏 4 列
</div>
```

### 9.2 响应式隐藏/显示

```html
<!-- 只在手机上显示 -->
<div class="block sm:hidden">手机端内容</div>

<!-- 只在平板及以上显示 -->
<div class="hidden sm:block">平板及以上内容</div>

<!-- 只在电脑上显示 -->
<div class="hidden lg:block">电脑端内容</div>

<!-- 复杂条件 -->
<div class="hidden sm:block md:hidden">
  只在 sm 断点显示（640px-768px）
</div>
```

### 9.3 响应式布局实战

```html
<!-- 响应式卡片列表 -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
  <div class="bg-white rounded-lg shadow p-4">
    <h3 class="text-lg font-bold mb-2">卡片标题</h3>
    <p class="text-gray-600">卡片内容描述...</p>
  </div>
  <!-- 更多卡片... -->
</div>

<!-- 响应式导航 -->
<nav class="flex flex-col sm:flex-row items-center justify-between p-4 bg-white shadow">
  <div class="text-xl font-bold mb-4 sm:mb-0">Logo</div>
  <div class="flex flex-col sm:flex-row gap-4">
    <a href="#" class="text-gray-600 hover:text-blue-500">首页</a>
    <a href="#" class="text-gray-600 hover:text-blue-500">产品</a>
    <a href="#" class="text-gray-600 hover:text-blue-500">关于</a>
  </div>
</nav>
```

---

## 10. 状态变体

### 10.1 交互状态

```html
<!-- 悬停状态 -->
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
  鼠标放上来变深色
</button>

<!-- 焦点状态 -->
<input class="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">

<!-- 激活状态 -->
<button class="bg-blue-500 active:bg-blue-800 text-white px-4 py-2 rounded">
  点击时变最深色
</button>

<!-- 禁用状态 -->
<button class="bg-gray-300 text-gray-500 px-4 py-2 rounded disabled:opacity-50" disabled>
  禁用按钮
</button>
```

### 10.2 子元素状态

```html
<!-- 第一个子元素 -->
<ul class="divide-y divide-gray-200">
  <li class="first:pt-0 py-4">第一项（无上边框）</li>
  <li class="py-4">第二项</li>
  <li class="last:pb-0 py-4">最后一项（无下边框）</li>
</ul>

<!-- 奇偶行 -->
<table>
  <tr class="even:bg-gray-100 odd:bg-white">
    <td>奇数行白色</td>
  </tr>
  <tr class="even:bg-gray-100 odd:bg-white">
    <td>偶数行灰色</td>
  </tr>
</table>

<!-- 子元素悬停 -->
<div class="group">
  <div class="group-hover:bg-blue-100">
    鼠标放在父元素上，这个元素变色
  </div>
</div>
```

### 10.3 深色模式

```html
<!-- 自动跟随系统 -->
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  白天白底黑字，晚上黑底白字
</div>

<!-- 手动切换 -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900">
    <h1 class="text-gray-900 dark:text-white">标题</h1>
  </body>
</html>
```

### 10.4 组合变体

```html
<!-- 深色模式下悬停 -->
<div class="bg-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-700">
  深色模式下悬停效果不同
</div>

<!-- 响应式 + 悬停 -->
<div class="text-sm sm:text-base hover:text-lg">
  响应式大小，悬停变大
</div>

<!-- 复杂组合 -->
<button class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-700 dark:hover:bg-blue-800 sm:px-6 sm:py-3">
  响应式 + 深色模式 + 悬停
</button>
```

---

## 11. 完整实战 Demo

### 11.1 登录页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>登录 - UnoCSS Demo</title>
  <script src="/src/main.ts" type="module"></script>
</head>
<body class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">

  <!-- 登录卡片 -->
  <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">
    <!-- 标题 -->
    <div class="text-center mb-8">
      <h1 class="text-3xl font-bold text-gray-800 mb-2">欢迎回来</h1>
      <p class="text-gray-500">请登录您的账户</p>
    </div>

    <!-- 表单 -->
    <form class="space-y-6">
      <!-- 邮箱输入 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">邮箱地址</label>
        <input 
          type="email" 
          placeholder="your@email.com"
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
        >
      </div>

      <!-- 密码输入 -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">密码</label>
        <input 
          type="password" 
          placeholder="••••••••"
          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
        >
      </div>

      <!-- 记住我 + 忘记密码 -->
      <div class="flex items-center justify-between">
        <label class="flex items-center">
          <input type="checkbox" class="w-4 h-4 text-blue-500 rounded border-gray-300 focus:ring-blue-500">
          <span class="ml-2 text-sm text-gray-600">记住我</span>
        </label>
        <a href="#" class="text-sm text-blue-500 hover:text-blue-600">忘记密码？</a>
      </div>

      <!-- 登录按钮 -->
      <button type="submit" class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:shadow-lg transition duration-200">
        登录
      </button>
    </form>

    <!-- 分隔线 -->
    <div class="relative my-6">
      <div class="absolute inset-0 flex items-center">
        <div class="w-full border-t border-gray-200"></div>
      </div>
      <div class="relative flex justify-center text-sm">
        <span class="px-4 bg-white text-gray-500">或使用以下方式登录</span>
      </div>
    </div>

    <!-- 社交登录 -->
    <div class="grid grid-cols-2 gap-4">
      <button class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
        <span class="text-gray-600 font-medium">Google</span>
      </button>
      <button class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
        <span class="text-gray-600 font-medium">GitHub</span>
      </button>
    </div>

    <!-- 注册链接 -->
    <p class="text-center mt-6 text-sm text-gray-600">
      还没有账户？
      <a href="#" class="text-blue-500 hover:text-blue-600 font-medium">立即注册</a>
    </p>
  </div>

</body>
</html>
```

### 11.2 商品卡片列表

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>商品列表 - UnoCSS Demo</title>
  <script src="/src/main.ts" type="module"></script>
</head>
<body class="bg-gray-50 min-h-screen">

  <!-- 顶部导航 -->
  <nav class="bg-white shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="text-xl font-bold text-gray-800">商城</div>
        <div class="flex items-center gap-4">
          <button class="relative p-2 text-gray-600 hover:text-gray-800">
            <span class="absolute top-0 right-0 w-4 h-4 bg-red-500 text-white text-xs rounded-full flex items-center justify-center">3</span>
            购物车
          </button>
        </div>
      </div>
    </div>
  </nav>

  <!-- 主内容区 -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- 页面标题 -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">热门商品</h1>
      <p class="mt-2 text-gray-600">精选好物，品质保证</p>
    </div>

    <!-- 商品网格 -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">

      <!-- 商品卡片 1 -->
      <div class="bg-white rounded-xl shadow-sm hover:shadow-lg transition duration-300 overflow-hidden group">
        <!-- 图片区域 -->
        <div class="relative h-48 bg-gray-200">
          <div class="absolute inset-0 flex items-center justify-center text-gray-400">
            商品图片
          </div>
          <!-- 折扣标签 -->
          <span class="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
            -20%
          </span>
          <!-- 收藏按钮 -->
          <button class="absolute top-3 right-3 p-2 bg-white rounded-full shadow opacity-0 group-hover:opacity-100 transition">
            ❤️
          </button>
        </div>
        <!-- 内容区域 -->
        <div class="p-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-1">无线蓝牙耳机</h3>
          <p class="text-sm text-gray-500 mb-3">高清音质，超长续航</p>
          <div class="flex items-center justify-between">
            <div>
              <span class="text-xl font-bold text-red-500">¥199</span>
              <span class="text-sm text-gray-400 line-through ml-2">¥249</span>
            </div>
            <button class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium rounded-lg transition">
              加入购物车
            </button>
          </div>
        </div>
      </div>

      <!-- 商品卡片 2 -->
      <div class="bg-white rounded-xl shadow-sm hover:shadow-lg transition duration-300 overflow-hidden group">
        <div class="relative h-48 bg-gray-200">
          <div class="absolute inset-0 flex items-center justify-center text-gray-400">
            商品图片
          </div>
          <span class="absolute top-3 left-3 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded">
            新品
          </span>
          <button class="absolute top-3 right-3 p-2 bg-white rounded-full shadow opacity-0 group-hover:opacity-100 transition">
            ❤️
          </button>
        </div>
        <div class="p-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-1">智能手表</h3>
          <p class="text-sm text-gray-500 mb-3">健康监测，运动追踪</p>
          <div class="flex items-center justify-between">
            <div>
              <span class="text-xl font-bold text-gray-900">¥899</span>
            </div>
            <button class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium rounded-lg transition">
              加入购物车
            </button>
          </div>
        </div>
      </div>

      <!-- 商品卡片 3 -->
      <div class="bg-white rounded-xl shadow-sm hover:shadow-lg transition duration-300 overflow-hidden group">
        <div class="relative h-48 bg-gray-200">
          <div class="absolute inset-0 flex items-center justify-center text-gray-400">
            商品图片
          </div>
          <button class="absolute top-3 right-3 p-2 bg-white rounded-full shadow opacity-0 group-hover:opacity-100 transition">
            ❤️
          </button>
        </div>
        <div class="p-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-1">机械键盘</h3>
          <p class="text-sm text-gray-500 mb-3">RGB背光，青轴手感</p>
          <div class="flex items-center justify-between">
            <div>
              <span class="text-xl font-bold text-gray-900">¥399</span>
            </div>
            <button class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium rounded-lg transition">
              加入购物车
            </button>
          </div>
        </div>
      </div>

      <!-- 商品卡片 4 -->
      <div class="bg-white rounded-xl shadow-sm hover:shadow-lg transition duration-300 overflow-hidden group">
        <div class="relative h-48 bg-gray-200">
          <div class="absolute inset-0 flex items-center justify-center text-gray-400">
            商品图片
          </div>
          <span class="absolute top-3 left-3 bg-orange-500 text-white text-xs font-bold px-2 py-1 rounded">
            热卖
          </span>
          <button class="absolute top-3 right-3 p-2 bg-white rounded-full shadow opacity-0 group-hover:opacity-100 transition">
            ❤️
          </button>
        </div>
        <div class="p-4">
          <h3 class="text-lg font-semibold text-gray-900 mb-1">便携充电宝</h3>
          <p class="text-sm text-gray-500 mb-3">20000mAh，快充协议</p>
          <div class="flex items-center justify-between">
            <div>
              <span class="text-xl font-bold text-red-500">¥129</span>
              <span class="text-sm text-gray-400 line-through ml-2">¥169</span>
            </div>
            <button class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium rounded-lg transition">
              加入购物车
            </button>
          </div>
        </div>
      </div>

    </div>
  </main>

</body>
</html>
```

### 11.3 仪表盘布局

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>仪表盘 - UnoCSS Demo</title>
  <script src="/src/main.ts" type="module"></script>
</head>
<body class="bg-gray-100 min-h-screen">

  <div class="flex h-screen">

    <!-- 侧边栏 -->
    <aside class="w-64 bg-gray-900 text-white flex-shrink-0 hidden md:block">
      <div class="p-6">
        <h2 class="text-xl font-bold">管理后台</h2>
      </div>
      <nav class="mt-6">
        <a href="#" class="flex items-center px-6 py-3 bg-gray-800 border-l-4 border-blue-500">
          <span class="mr-3">📊</span>
          仪表盘
        </a>
        <a href="#" class="flex items-center px-6 py-3 hover:bg-gray-800 transition">
          <span class="mr-3">👥</span>
          用户管理
        </a>
        <a href="#" class="flex items-center px-6 py-3 hover:bg-gray-800 transition">
          <span class="mr-3">📦</span>
          商品管理
        </a>
        <a href="#" class="flex items-center px-6 py-3 hover:bg-gray-800 transition">
          <span class="mr-3">📋</span>
          订单管理
        </a>
        <a href="#" class="flex items-center px-6 py-3 hover:bg-gray-800 transition">
          <span class="mr-3">⚙️</span>
          系统设置
        </a>
      </nav>
    </aside>

    <!-- 主内容 -->
    <div class="flex-1 flex flex-col overflow-hidden">

      <!-- 顶部栏 -->
      <header class="bg-white shadow-sm px-6 py-4 flex items-center justify-between">
        <button class="md:hidden text-gray-600">
          ☰
        </button>
        <h1 class="text-xl font-semibold text-gray-800">仪表盘</h1>
        <div class="flex items-center gap-4">
          <span class="text-gray-600">👤 管理员</span>
          <button class="text-gray-600 hover:text-gray-800">退出</button>
        </div>
      </header>

      <!-- 内容区 -->
      <main class="flex-1 overflow-auto p-6">

        <!-- 统计卡片 -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-500 mb-1">总用户</p>
                <p class="text-2xl font-bold text-gray-900">12,345</p>
              </div>
              <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-500 text-xl">
                👥
              </div>
            </div>
            <p class="text-sm text-green-500 mt-4">↑ 12% 较上月</p>
          </div>

          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-500 mb-1">总订单</p>
                <p class="text-2xl font-bold text-gray-900">8,234</p>
              </div>
              <div class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center text-green-500 text-xl">
                📦
              </div>
            </div>
            <p class="text-sm text-green-500 mt-4">↑ 8% 较上月</p>
          </div>

          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-500 mb-1">销售额</p>
                <p class="text-2xl font-bold text-gray-900">¥128,430</p>
              </div>
              <div class="w-12 h-12 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-500 text-xl">
                💰
              </div>
            </div>
            <p class="text-sm text-red-500 mt-4">↓ 3% 较上月</p>
          </div>

          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-500 mb-1">转化率</p>
                <p class="text-2xl font-bold text-gray-900">3.24%</p>
              </div>
              <div class="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center text-purple-500 text-xl">
                📈
              </div>
            </div>
            <p class="text-sm text-green-500 mt-4">↑ 0.5% 较上月</p>
          </div>
        </div>

        <!-- 图表区域 -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          <div class="bg-white rounded-xl shadow-sm p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">销售趋势</h3>
            <div class="h-64 bg-gray-50 rounded-lg flex items-center justify-center text-gray-400">
              [图表区域]
            </div>
          </div>
          <div class="bg-white rounded-xl shadow-sm p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">用户增长</h3>
            <div class="h-64 bg-gray-50 rounded-lg flex items-center justify-center text-gray-400">
              [图表区域]
            </div>
          </div>
        </div>

        <!-- 最近订单表格 -->
        <div class="bg-white rounded-xl shadow-sm overflow-hidden">
          <div class="px-6 py-4 border-b border-gray-200">
            <h3 class="text-lg font-semibold text-gray-900">最近订单</h3>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">订单号</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">客户</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">商品</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">金额</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">状态</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200">
                <tr class="hover:bg-gray-50 transition">
                  <td class="px-6 py-4 text-sm text-gray-900">#ORD-001</td>
                  <td class="px-6 py-4 text-sm text-gray-600">张三</td>
                  <td class="px-6 py-4 text-sm text-gray-600">无线蓝牙耳机</td>
                  <td class="px-6 py-4 text-sm text-gray-900 font-medium">¥199</td>
                  <td class="px-6 py-4">
                    <span class="px-2 py-1 text-xs font-medium bg-green-100 text-green-800 rounded-full">已完成</span>
                  </td>
                </tr>
                <tr class="hover:bg-gray-50 transition">
                  <td class="px-6 py-4 text-sm text-gray-900">#ORD-002</td>
                  <td class="px-6 py-4 text-sm text-gray-600">李四</td>
                  <td class="px-6 py-4 text-sm text-gray-600">智能手表</td>
                  <td class="px-6 py-4 text-sm text-gray-900 font-medium">¥899</td>
                  <td class="px-6 py-4">
                    <span class="px-2 py-1 text-xs font-medium bg-yellow-100 text-yellow-800 rounded-full">配送中</span>
                  </td>
                </tr>
                <tr class="hover:bg-gray-50 transition">
                  <td class="px-6 py-4 text-sm text-gray-900">#ORD-003</td>
                  <td class="px-6 py-4 text-sm text-gray-600">王五</td>
                  <td class="px-6 py-4 text-sm text-gray-600">机械键盘</td>
                  <td class="px-6 py-4 text-sm text-gray-900 font-medium">¥399</td>
                  <td class="px-6 py-4">
                    <span class="px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded-full">待发货</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </main>
    </div>
  </div>

</body>
</html>
```

### 11.4 移动端适配页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>移动端页面 - UnoCSS Demo</title>
  <script src="/src/main.ts" type="module"></script>
</head>
<body class="bg-gray-100 min-h-screen pb-20">

  <!-- 顶部搜索栏 -->
  <header class="bg-white sticky top-0 z-50 shadow-sm px-4 py-3">
    <div class="flex items-center gap-3">
      <div class="flex-1 relative">
        <input 
          type="text" 
          placeholder="搜索商品..."
          class="w-full pl-10 pr-4 py-2.5 bg-gray-100 rounded-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
        <span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">🔍</span>
      </div>
      <button class="text-gray-600 text-sm">消息</button>
    </div>
  </header>

  <!-- 轮播图区域 -->
  <div class="px-4 mt-4">
    <div class="h-40 bg-gradient-to-r from-blue-400 to-purple-500 rounded-2xl flex items-center justify-center text-white text-xl font-bold shadow-lg">
      轮播图区域
    </div>
  </div>

  <!-- 分类图标 -->
  <div class="px-4 mt-6">
    <div class="grid grid-cols-5 gap-4">
      <div class="flex flex-col items-center gap-2">
        <div class="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center text-2xl">📱</div>
        <span class="text-xs text-gray-600">手机</span>
      </div>
      <div class="flex flex-col items-center gap-2">
        <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center text-2xl">💻</div>
        <span class="text-xs text-gray-600">电脑</span>
      </div>
      <div class="flex flex-col items-center gap-2">
        <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center text-2xl">🎧</div>
        <span class="text-xs text-gray-600">数码</span>
      </div>
      <div class="flex flex-col items-center gap-2">
        <div class="w-12 h-12 bg-yellow-100 rounded-xl flex items-center justify-center text-2xl">👕</div>
        <span class="text-xs text-gray-600">服饰</span>
      </div>
      <div class="flex flex-col items-center gap-2">
        <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center text-2xl">🏠</div>
        <span class="text-xs text-gray-600">家居</span>
      </div>
    </div>
  </div>

  <!-- 秒杀专区 -->
  <div class="px-4 mt-6">
    <div class="bg-white rounded-2xl p-4 shadow-sm">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-bold text-red-500">⚡ 限时秒杀</h2>
        <span class="text-xs text-gray-500">更多 ></span>
      </div>
      <div class="flex gap-3 overflow-x-auto pb-2">
        <div class="flex-shrink-0 w-28">
          <div class="h-28 bg-gray-200 rounded-xl flex items-center justify-center text-gray-400 text-xs">商品图</div>
          <p class="text-xs text-gray-800 mt-2 truncate">蓝牙耳机</p>
          <div class="flex items-baseline gap-1 mt-1">
            <span class="text-red-500 font-bold text-sm">¥99</span>
            <span class="text-gray-400 text-xs line-through">¥199</span>
          </div>
        </div>
        <div class="flex-shrink-0 w-28">
          <div class="h-28 bg-gray-200 rounded-xl flex items-center justify-center text-gray-400 text-xs">商品图</div>
          <p class="text-xs text-gray-800 mt-2 truncate">充电宝</p>
          <div class="flex items-baseline gap-1 mt-1">
            <span class="text-red-500 font-bold text-sm">¥59</span>
            <span class="text-gray-400 text-xs line-through">¥129</span>
          </div>
        </div>
        <div class="flex-shrink-0 w-28">
          <div class="h-28 bg-gray-200 rounded-xl flex items-center justify-center text-gray-400 text-xs">商品图</div>
          <p class="text-xs text-gray-800 mt-2 truncate">数据线</p>
          <div class="flex items-baseline gap-1 mt-1">
            <span class="text-red-500 font-bold text-sm">¥9.9</span>
            <span class="text-gray-400 text-xs line-through">¥29</span>
          </div>
        </div>
        <div class="flex-shrink-0 w-28">
          <div class="h-28 bg-gray-200 rounded-xl flex items-center justify-center text-gray-400 text-xs">商品图</div>
          <p class="text-xs text-gray-800 mt-2 truncate">手机壳</p>
          <div class="flex items-baseline gap-1 mt-1">
            <span class="text-red-500 font-bold text-sm">¥19</span>
            <span class="text-gray-400 text-xs line-through">¥49</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 推荐商品 -->
  <div class="px-4 mt-6">
    <h2 class="text-lg font-bold text-gray-800 mb-4">🔥 为你推荐</h2>
    <div class="grid grid-cols-2 gap-3">
      <div class="bg-white rounded-xl overflow-hidden shadow-sm">
        <div class="h-40 bg-gray-200 flex items-center justify-center text-gray-400 text-xs">商品图</div>
        <div class="p-3">
          <p class="text-sm text-gray-800 line-clamp-2">无线蓝牙耳机 高清音质 超长续航 降噪</p>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-red-500 font-bold">¥199</span>
            <span class="text-xs text-gray-400">已售 1.2万</span>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl overflow-hidden shadow-sm">
        <div class="h-40 bg-gray-200 flex items-center justify-center text-gray-400 text-xs">商品图</div>
        <div class="p-3">
          <p class="text-sm text-gray-800 line-clamp-2">智能手表 运动健康监测 心率血氧检测</p>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-red-500 font-bold">¥899</span>
            <span class="text-xs text-gray-400">已售 8千</span>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl overflow-hidden shadow-sm">
        <div class="h-40 bg-gray-200 flex items-center justify-center text-gray-400 text-xs">商品图</div>
        <div class="p-3">
          <p class="text-sm text-gray-800 line-clamp-2">机械键盘 RGB背光 青轴手感 游戏办公</p>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-red-500 font-bold">¥399</span>
            <span class="text-xs text-gray-400">已售 5千</span>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl overflow-hidden shadow-sm">
        <div class="h-40 bg-gray-200 flex items-center justify-center text-gray-400 text-xs">商品图</div>
        <div class="p-3">
          <p class="text-sm text-gray-800 line-clamp-2">便携充电宝 20000mAh 快充 轻薄便携</p>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-red-500 font-bold">¥129</span>
            <span class="text-xs text-gray-400">已售 2万</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 底部导航 -->
  <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 px-6 py-2">
    <div class="flex justify-around items-center">
      <a href="#" class="flex flex-col items-center text-blue-500">
        <span class="text-xl">🏠</span>
        <span class="text-xs mt-1">首页</span>
      </a>
      <a href="#" class="flex flex-col items-center text-gray-400">
        <span class="text-xl">📦</span>
        <span class="text-xs mt-1">分类</span>
      </a>
      <a href="#" class="flex flex-col items-center text-gray-400">
        <span class="text-xl">🛒</span>
        <span class="text-xs mt-1">购物车</span>
      </a>
      <a href="#" class="flex flex-col items-center text-gray-400">
        <span class="text-xl">👤</span>
        <span class="text-xs mt-1">我的</span>
      </a>
    </div>
  </nav>

</body>
</html>
```

---

## 常用类名速查表

### 布局

| 类名 | 作用 |
|------|------|
| `block` | 块级元素 |
| `inline-block` | 行内块级 |
| `hidden` | 隐藏 |
| `flex` | Flex 布局 |
| `grid` | Grid 布局 |
| `container` | 容器（自动居中） |
| `mx-auto` | 水平居中 |

### 间距

| 类名 | 作用 |
|------|------|
| `p-4` | 四边内边距 1rem |
| `px-4` | 左右内边距 |
| `py-4` | 上下内边距 |
| `m-4` | 四边外边距 |
| `mx-auto` | 水平居中 |
| `space-y-4` | 子元素垂直间距 |
| `gap-4` | 网格/弹性间距 |

### 尺寸

| 类名 | 作用 |
|------|------|
| `w-full` | 宽度 100% |
| `h-full` | 高度 100% |
| `w-screen` | 屏幕宽度 |
| `h-screen` | 屏幕高度 |
| `min-h-screen` | 最小屏幕高度 |
| `max-w-md` | 最大宽度 448px |

### 文字

| 类名 | 作用 |
|------|------|
| `text-sm` | 小字 14px |
| `text-base` | 正常 16px |
| `text-lg` | 大字 18px |
| `text-xl` | 更大 20px |
| `font-bold` | 粗体 |
| `text-center` | 居中 |
| `truncate` | 超出省略 |

### 颜色

| 类名 | 作用 |
|------|------|
| `bg-white` | 白色背景 |
| `bg-gray-100` | 浅灰背景 |
| `text-gray-800` | 深灰文字 |
| `text-red-500` | 红色文字 |
| `bg-blue-500` | 蓝色背景 |

### 边框

| 类名 | 作用 |
|------|------|
| `border` | 1px 边框 |
| `border-2` | 2px 边框 |
| `rounded` | 小圆角 |
| `rounded-lg` | 大圆角 |
| `rounded-full` | 完全圆形 |
| `shadow` | 阴影 |
| `shadow-lg` | 大阴影 |

### 交互

| 类名 | 作用 |
|------|------|
| `hover:bg-blue-600` | 悬停变色 |
| `focus:ring-2` | 焦点光环 |
| `active:bg-blue-800` | 点击变色 |
| `disabled:opacity-50` | 禁用透明度 |
| `transition` | 过渡动画 |
| `duration-200` | 动画时长 200ms |

### 响应式

| 类名 | 作用 |
|------|------|
| `sm:` | 640px 以上 |
| `md:` | 768px 以上 |
| `lg:` | 1024px 以上 |
| `xl:` | 1280px 以上 |
| `hidden sm:block` | 手机隐藏，平板显示 |

---

> 更多类名请参考官方文档：https://unocss.dev/
