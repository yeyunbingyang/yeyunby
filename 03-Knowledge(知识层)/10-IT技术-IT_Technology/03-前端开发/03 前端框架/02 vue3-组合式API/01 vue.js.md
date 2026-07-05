# Vue3

技术选型

- Vue

- **选项式 API** 还是 **组合式 API**✔️

- **HTML** 还是 **单文件组件**✔️

- 语法

- **javascript** 还是 **typescript**✔️

- 构建工具

- **@vue/cli** 还是 **vite**✔️

- 路由

- **vue-router**✔️

- 共享存储

- **vuex** 还是 **pinia**✔️

- 视图组件

- **ElementUI** 还是 **Antdv**✔️

## 1) 环境准备

### 创建项目

采用 vite 作为前端项目的打包，构建工具

```
npm init vite@latest
```

按提示操作

```
cd 项目目录
npm install
npm run dev
```

### 编码 IDE

推荐采用微软的 VSCode 作为开发工具，到它的官网 [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/) 下载安装即可

code . 就可以在vscode 中打开

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615153-e7b926a1-5537-4966-8792-87cfac9004fa.png "null")

要对 *.vue 做语法支持，还要安装一个 Volar 插件

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615222-4a8f505f-b2b9-4d54-a400-75391a414828.png "null")

### 安装 devtools

- devtools 插件网址：[https://devtools.vuejs.org/guide/installation.html](https://devtools.vuejs.org/guide/installation.html)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615285-cd25caf9-3546-47f9-b91e-cd708d00a16d.png "null")

### 修改端口

打开项目根目录下 vite.config.ts

```
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 7070
  }
})
```

- 文档地址：[配置 Vite {#configuring-vite} | Vite中文网 (vitejs.cn)](https://vitejs.cn/config/#server-port)

- host: '0.0.0.0', 局域网其他人也可以访问

### 配置根路径

在 Vue 3 中，使用 `@` 符号来引用路径是很常见的需求。如果你在 Vite 项目中遇到了找不到模块“@/**”或其相应的类型声明的问题，可以按照以下步骤解决：

1. 首先，我们需要使用 `path` 包的 `resolve` 方法来引用路径。因此，第一步是执行以下命令安装 `@types/node`，以便使用 `path`：

```
npm i -D @types/node
```

2. 接下来，在 `vite.config.ts` 中配置路径别名。你可以像这样设置别名：

```
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';

export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': resolve(__dirname, './src'),
            '*': resolve('')
        }
    }
});
```

3. 在 `tsconfig.json` 中添加以下两项配置，以便让 TypeScript 知道如何处理路径别名：

```
"compilerOptions": {
    "baseUrl": ".",
    "paths": {
        "@/*": ["src/*"]
    }
}
```

### 配置代理

为了避免前后端服务器联调时， fetch、xhr 请求产生跨域问题，需要配置代理，同样是修改项目根目录下 vite.config.ts

```
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 7070,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
})
```

- 文档地址：[配置 Vite {#configuring-vite} | Vite中文网 (vitejs.cn)](https://vitejs.cn/config/#server-proxy)

### 项目结构

```
index.html
package.json
tsconfig.json
vite.config.ts
├─public
└─src
    ├─assets
    ├─components
    ├─model
    ├─router
    ├─store
    └─views
```

- index.html 为主页面

- package.json npm 配置文件

- tsconfig.json typescript 配置文件

- vite.config.ts vite 配置文件

- public 静态资源

- src/components 可重用组件

- src/model 模型定义【一些实体】

- src/router 路由

- src/store 共享存储

- src/views 视图组件

## 2) Vue 组件

### 组件化

组件系统是一个抽象的概念；

- 组件：小型、独立、可复用的单元

- 组合：通过组件之间的组合、包含关系构建出一个完整应用

几乎任意类型的应用界面都可以抽象为一个组件树；

![](https://cdn.nlark.com/yuque/0/2025/webp/40487410/1737444615345-2acf3cb6-e560-48f3-b4ca-3e434209ca5f.webp "null")

### SFC

Vue 的**单文件组件** (即 *.vue 文件，英文 Single-File Component，简称 **SFC**) 是一种特殊的文件格式，使我们能够将一个 Vue 组件的模板、逻辑与样式封装在单个文件中.

Vue 的组件文件以 .vue 结尾，每个组件由三部分组成

```
<script setup lang="ts">
//编写脚本
</script>

<template>
  //编写页面模板
</template>

<style scoped>
  //编写样式
</style>
```

- script 代码部分，控制模板的数据来源和行为

- template 模板部分，由它生成 html 代码

- style 样式部分，一般不咋关心【`scoped` 属性表示样式仅作用于当前组件。】

根组件是 src/App.vue，先来个 Hello,world 例子

```
<script setup lang="ts">
import { ref } from "vue";
let msg = ref("hello"); // 把数据变成响应式的

function change() {
  msg.value = "world";
  console.log(msg);
}
</script>

<template>
  <h1>{{ msg }}</h1>

  <input type="button" value="修改msg" @click="change" />
</template>
```

- {{msg}} 用来把一个变量绑定到页面上某个位置

- 绑定的变量必须用 ref 函数来封装

- ref 返回的是【响应式】数据，即数据一旦变化，页面展示也跟着变化

### 运行原理

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615399-b93dcc9c-bf85-4f63-82c4-8c9da2503538.png "null")

main.js文件解析

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615450-a55729e7-0949-44f9-ab77-e6915360975f.png "null")

**创建一个 Vue 应用**[](https://cn.vuejs.org/guide/essentials/application.html#creating-a-vue-application)

**应用实例**[](https://cn.vuejs.org/guide/essentials/application.html#the-application-instance)

每个 Vue 应用都是通过 `createApp` 函数创建一个新的 **应用实例**：

```
import { createApp } from 'vue'

const app = createApp({
  /* 根组件选项 */
})
```

**根组件**[](https://cn.vuejs.org/guide/essentials/application.html#the-root-component)

我们传入 `createApp` 的对象实际上是一个组件，每个应用都需要一个“根组件”，其他组件将作为其子组件。

如果你使用的是单文件组件，我们可以直接从另一个文件中导入根组件。

```
import { createApp } from 'vue'
// 从一个单文件组件中导入根组件
import App from './App.vue'

const app = createApp(App)
```

虽然本指南中的许多示例只需要一个组件，但大多数真实的应用都是由一棵嵌套的、可重用的组件树组成的。例如，一个待办事项 (Todos) 应用的组件树可能是这样的：

```
App (root component)
├─ TodoList
│  └─ TodoItem
│     ├─ TodoDeleteButton
│     └─ TodoEditButton
└─ TodoFooter
   ├─ TodoClearButton
   └─ TodoStatistics
```

我们会在指南的后续章节中讨论如何定义和组合多个组件。在那之前，我们得先关注一个组件内到底发生了什么。

**挂载应用**[](https://cn.vuejs.org/guide/essentials/application.html#mounting-the-app)

应用实例必须在调用了 `.mount()` 方法后才会渲染出来。该方法接收一个“容器”参数，可以是一个实际的 DOM 元素或是一个 CSS 选择器字符串：

【显示效果都在div里】

```
<div id="app"></div>
```

```
app.mount('#app')
```

应用根组件的内容将会被渲染在容器元素里面。容器元素自己将**不会**被视为应用的一部分。

`.mount()` 方法应该始终在整个应用配置和资源注册完成后被调用。同时请注意，不同于其他资源注册方法，它的返回值是根组件实例而非应用实例。

**DOM 中的根组件模板**[](https://cn.vuejs.org/guide/essentials/application.html#in-dom-root-component-template)

根组件的模板通常是组件本身的一部分，但也可以直接通过在挂载容器内编写模板来单独提供：

```
<div id="app">
  <button @click="count++">{{ count }}</button>

</div>
```

```
import { createApp } from 'vue'

const app = createApp({
  data() {
    return {
      count: 0
    }
  }
})

app.mount('#app')
```

当根组件没有设置 `template` 选项时，Vue 将自动使用容器的 `innerHTML` 作为模板。

DOM 内模板通常用于[无构建步骤](https://cn.vuejs.org/guide/quick-start.html#using-vue-from-cdn)的 Vue 应用程序。它们也可以与服务器端框架一起使用，其中根模板可能是由服务器动态生成的。

#### main.ts

```
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

createApp(App)
  .mount('#app')
```

- createApp（函数） 是创建一个 Vue 应用程序，它接收的参数 App 即之前我们看到的根组件

- mount 就是把根组件生成的 html 代码片段【挂载】到 index.html 中 id 为 app 的 html 元素上

可以修改自己的组件文件，挂载到主页面

新建 src/views/E0.vue，内容如下

```
<script setup lang="ts"> //setup lang="ts"必须加
import { ref } from 'vue' //引入响应式函数
let msg = ref('hello') //封装变量为响应式

function hello() {
  msg.value = 'world' //访问时要加value
  console.log(msg)
}
</script>

<template>
  <h1>{{ msg }}</h1>

  <input type="button" value="修改" @click="hello">
</template>

<style scoped>
</style>
```

修改 main.ts 将自己的组件文件挂载

```
import { createApp } from 'vue'
import './style.css'
// import App from './App.vue'
import E0 from './views/E0.vue'

createApp(E0).mount('#app')
```

- 以后我们用这样的方式演示课堂案例

打开浏览器控制台，进入 Vue 的开发工具，尝试做如下修改

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615505-f7306e99-f621-421b-bee5-48a09fbde1d4.png "null")

当把 msg 的值由 "Hello, World" 改为 "你好" 时，会发现页面展示同步发生了变化

### 生命周期

每个 Vue 组件实例在创建时都需要经历一系列的初始化步骤，比如设置好数据侦听，编译模板，挂载实例到 DOM，以及在数据改变时更新 DOM。在此过程中，它也会运行被称为生命周期钩子的函数，让开发者有机会在特定阶段运行自己的代码。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615565-36bb2f65-ba83-43b0-ba0a-66cdfac37ab3.png "null")

生命周期整体分为**四个阶段**，分别是：`创建、挂载、更新、销毁`，每个阶段都有两个钩子，一前一后。

**常用的钩子：**

- **onMounted(挂载完毕)**

- **onUpdated(更新完毕)**

- **onBeforeUnmount(卸载之前)**

- 概念：`Vue`组件实例在创建时要经历一系列的初始化步骤，在此过程中`Vue`会在合适的时机，调用特定的函数，从而让开发者有机会在特定阶段运行自己的代码，这些特定的函数统称为：生命周期钩子

- 规律：

生命周期整体分为四个阶段，分别是：**创建、挂载、更新、销毁**，每个阶段都有两个钩子，一前一后。

- `Vue2`的生命周期

创建阶段：`beforeCreate`、`created`

挂载阶段：`beforeMount`、`mounted`

更新阶段：`beforeUpdate`、`updated`

销毁阶段：`beforeDestroy`、`destroyed`

- `Vue3`的生命周期

创建阶段：`setup`

挂载阶段：`onBeforeMount`、`onMounted`

更新阶段：`onBeforeUpdate`、`onUpdated`

卸载阶段：`onBeforeUnmount`、`onUnmounted`

- 常用的钩子：`onMounted`(挂载完毕)、`onUpdated`(更新完毕)、`onBeforeUnmount`(卸载之前)

```
<script setup>

import {onBeforeMount, onBeforeUpdate, onMounted, onUpdated, ref} from "vue";

const count = ref(1);
function countAdd(){
  count.value ++;
}

//生命周期钩子函数

//挂载 去后台查询用户信息
onBeforeMount(()=>{
  //
  console.log("挂载前：count",count.value) //变量初始化完成
  console.log("挂载前：",document.getElementById("btn01")) //元素标签没有初始化完成
})

onMounted(()=>{
  //
  console.log("挂载完成：count",count.value)
  console.log("挂载完成：",document.getElementById("btn01"))

})

//更新前： 前内容未变，数据变了
onBeforeUpdate(()=>{
  console.log("更新前：count",count.value)
  console.log("更新前：btn内容",document.getElementById("btn01").innerHTML)
})
//更新完： 内容变
onUpdated(()=>{
  console.log("更新完：count",count.value)
  console.log("更新完：btn内容",document.getElementById("btn01").innerHTML)
})

</script>

<template>
<button id="btn01" @click="countAdd">点 {{count}}</button>

</template>

<style scoped>

</style>
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615627-52786411-71be-49e0-bf10-10046b6870ca.png "null")

## 3) 基础使用

### 文本插值

最基本的数据绑定形式是文本插值，它使用的是“Mustache”语法 (即双大括号)

```
<span>Message: {{ msg }}</span>
```

双大括号标签会被替换为[相应组件实例中](https://cn.vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-reactive-state) `msg` 属性的值。同时每次 `msg` 属性更改时它也会同步更新。

#### 指令【v-xxx】

##### 事件绑定：v-on

使用 `v-on`指令，可以为元素绑定事件。可以简写为 `@`

```
<script setup lang="ts">
import { ref } from 'vue'
const count = ref(0)
function dec() {
  count.value--
}
function inc() {
  count.value++
}
</script>

<template>
  <input type="button" value="-" @click="dec">
  <h2>{{count}}</h2>

  <input type="button" value="+" @click="inc">
</template>
```

【@事件名】用来将标签属性与函数绑定，事件发生后执行函数内代码

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615678-597d1740-20e5-45c8-ad69-85206e5d6571.png "null")

Modifiers：修饰符详情

[https://cn.vuejs.org/guide/essentials/event-handling.html](https://cn.vuejs.org/guide/essentials/event-handling.html)

##### 条件判断：v-if

`v-if` 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回真值时才被渲染。

```
<h1 v-if="awesome">Vue is awesome!</h1>
```

##### 循环：v-for

[https://cn.vuejs.org/guide/essentials/list.html](https://cn.vuejs.org/guide/essentials/list.html)

我们可以使用 `v-for` 指令基于一个数组来渲染一个列表。

**基础使用**

`v-for` 指令的值需要使用 `item in items` 形式的特殊语法，其中 `items` 是源数据的数组，而 `item` 是迭代项的**别名**。

`v-for` 也支持使用可选的第二个参数表示当前项的位置索引。

```
const parentMessage = ref('Parent')
const items = ref([{ message: 'Foo' }, { message: 'Bar' }])

<li v-for="(item, index) in items">
  {{ parentMessage }} - {{ index }} - {{ item.message }}
</li>
```

```
Parent - 0 - Foo
Parent - 1 - Ba
```

**在** `v-for` **里使用范围值**

`v-for` 可以直接接受一个整数值。在这种用例中，会将该模板基于 `1...n` 的取值范围重复多次。

```
<span v-for="n in 10">{{ n }}</span>
```

注意此处 `n` 的初值是从 `1` 开始而非 `0`。

**v-for 与对象**

你也可以使用 v-for 来遍历一个对象的所有属性。遍历的顺序会基于对该对象调用 Object.keys() 的返回值来决定。

```
const myObject = reactive({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10'
})

<ul>
  <li v-for="value in myObject">
    {{ value }}
  </li>

  
  <li v-for="(value, key) in myObject">
  {{ key }}: {{ value }}
  </li>

  
  <li v-for="(value, key, index) in myObject">
  {{ index }}. {{ key }}: {{ value }}
  </li>

</ul>
```

第二个参数表示属性名 (例如 key)：

第三个参数表示位置索引：index

下面是一个综合示例，演示了 `v-for` 在 Vue 3 中的各种用法，包括基本循环、带索引、解构赋值、多层嵌套循环和对象遍历：

```
<script setup lang="ts">
import { ref, reactive } from 'vue'

// 基本数据
const count = ref(0)
const awesome = ref(true)

// 事件处理函数
function dec() {
count.value--
}

function inc() {
count.value++
}

function toggleAwesome() {
awesome.value = !awesome.value
}

// 循环数据
const items = ref([
{ message: 'Foo', id: 1, children: ['A', 'B'] },
{ message: 'Bar', id: 2, children: ['C', 'D'] }
])

// 对象数据
const myObject = reactive({
title: 'How to do lists in Vue',
author: 'Jane Doe',
publishedAt: '2016-04-10'
})

// 父作用域数据
const parentMessage = ref('Parent')
</script>
```

# 事件绑定：v-on

使用 v-on 指令，可以为元素绑定事件。可以简写为 @

<input type="button" value="-" @click="dec">

## {{ count }}

<input type="button" value="+" @click="inc">

# 条件判断：v-if

v-if 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回真值时才被渲染。

# 组件条件判断

<button @click="toggleAwesome">  
{{ awesome ? '隐藏' : '显示' }}  

# 循环：v-for（基本循环）

我们可以使用 v-for 指令基于一个数组来渲染一个列表。

- {{ item.message }}

# 循环：v-for（带索引）

- {{ parentMessage }} - {{ index }} - {{ item.message }}

# 循环：v-for（解构赋值）

- {{ message }}

- {{ message }} {{ index }}

# 循环：v-for（多层嵌套）

- {{ item.message }} {{ childItem }}

# 循环：v-for（对象遍历）

- {{ value }}

- {{ key }}: {{ value }}

- {{ index }}. {{ key }}: {{ value }}

##### `v-show`

另一个可以用来按条件显示一个元素的指令是 `v-show`。其用法基本一样：

```
<h1 v-show="ok">Hello!</h1>
```

**不同之处在于** `v-show` **会在 DOM 渲染中保留该元素**；`v-show` 仅切换了该元素上名为 `display` 的 CSS 属性。

`v-show` 不支持在 `<template>` 元素上使用，也不能和 `v-else` 搭配使用。

##### 更多指令

[https://cn.vuejs.org/api/built-in-directives.html；后期我们都会用到。](https://cn.vuejs.org/api/built-in-directives.html；后期我们都会用到。)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615732-07099d61-3c92-4d91-9b5d-df73c738d43d.png "null")

### ref 与 reactive【响应式】

数据的动态变化需要反馈到页面；

Vue通过`ref()`和`reactive()`包装数据，将会生成一个数据的代理对象。vue内部的 **基于依赖追踪的响应式系统** 就会**追踪**感知**数据变化**，并**触发页面**的重新**渲染**。

#### 响应式 - ref()【通用】

### **使用步骤：**

1. 使用 **ref()** 包装**原始类型、对象类型数据**，生成 **代理对象**

2. **任何方法、js代码中**，使用 `代理对象.value` 的形式读取和修改值

3. **页面组件中**，直接使用 `代理对象`

注意：推荐使用 const（常量） 声明代理对象。代表代理对象不可变，但是内部值变化会被追踪。*

```
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}
</script>
```

{{ count }}

### **深层响应性**

属性也是响应式

```


  import { ref } from 'vue'

  const obj = ref({
    nested: { count: 0 },
    arr: ['foo', 'bar']
  })

  function mutateDeeply() {
    // 以下都会按照期望工作
    obj.value.nested.count++
    obj.value.arr.push('baz')
  }
```

#### 响应式 - reactive()【对象类型】

## 使用步骤：

1. 使用 **reactive()** 包装**对象类型数据**，生成 **代理对象**

2. **任何方法、js代码中**，使用 `代理对象.属性`的形式读取和修改值

3. **页面组件中**，直接使用 `代理对象.属性`

```
import { reactive } from 'vue'

const state = reactive({ count: 0 })

<button @click="state.count++">
{{ state.count }}
</button>
```

#### 对比

```
<script setup lang="ts">
import { ref, reactive } from 'vue'
const msg = ref('Hello, World')
const user = reactive({ name: '张三' })
</script>

<template>
  <h2>{{msg}}</h2>

  <h2>{{user.name}}</h2>

</template>
```

- **ref 能将任意类型的数据变为【响应式】的**

- **reactive 只能将对象类型变为【响应式】，对基本类型无效（例如 string，number，boolean）**

- 注意：推荐使用 const（常量） 声明代理对象。代表代理对象不可变，但是内部值变化会被追踪。

还有一点不同

```
<script setup lang="ts">
import { ref, reactive } from 'vue'
const u1 = ref({ name: '张三' })
const u2 = reactive({ name: '张三' })

function test() {
  console.log(u1.value) //
  console.log(u2)       //
}

test()
</script>

  
<template>
  <h2>{{u1.name}}</h2>

  <h2>{{u2.name}}</h2>

</template>
```

- **在 template 模板中使用 ref 包装的数据，直接写【变量名】就可以了**

- **但在js代码中要使用 ref 包装的数据，必须用【变量名.value】才能访问到**

- reactive 包装的数据，在模板中和代码中都是一致的

#### 最佳实践：⭐

推荐使用ref、另外代理响应式对象 const声明

- ref

- 基础数据类型和对象都可以使用
- js中 .value调用
- 引用替换时可以保证响应式

- reactive

- 对象类型可用
- 直接使用
- 深层次响应式时使用
- 引用替换时不能持续响应式

|   |   |   |
|---|---|---|
|**特性**|`**ref**`|`**reactive**`|
|**支持类型**|基本类型和对象类型|仅对象类型（含数组、Map等）|
|**访问方式**|JS中需 `.value`<br><br>，模板自动解包|直接访问属性|
|**响应式保持**|替换引用仍保持响应式|替换引用会丢失响应式|
|**解构处理**|解构后仍为响应式（无需额外处理）|需用 `toRefs`<br><br>保持响应性|
|**性能**|基本类型开销较小|复杂对象时性能与 `ref`<br><br>包装对象相当|

1、我该用哪个函数？ 答：可以 ref() 一把梭、也可以 ref()包装基本数据、reactive()包装对象

2、使用 const 声明响应式常量【使用响应包装，不可以修改变量的引用】

3、响应式数据具有深层响应式特性（属性.属性.属性 也都是响应式的）

响应式：ref()、reactive()；

ref()：

1、把基本类型、对象类型数据使用 ref() 包装成响应式数据

2、使用 代理对象.value = ""【js修改才使用】

3、页面取值、属性绑定 直接 {{url}}

reactive():

1、把对象类型使用 reactive() 包装成响应式数据

2、使用 代理对象 = ""、

3、页面取值、属性绑定 直接 {{变量名}}

- 区别：

1. `ref`创建的变量必须使用`.value`（可以使用`volar`插件自动添加`.value`）。![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444616076-f28d609d-8c97-41b6-94cb-f9b0fff9a7f0.png)

2. `reactive`重新分配一个新对象，会**失去**响应式（可以使用`Object.assign`去整体替换）。ref可以进行赋值![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615778-01701e4b-f51c-4d5e-84f2-0eefb895e9d8.png "null")

- 使用原则：⭐

1. 若需要一个基本类型的响应式数据，必须使用`ref`。

2. 若需要一个响应式对象，层级不深，`ref`、`reactive`都可以。

3. 若需要一个响应式对象，且层级较深，推荐使用`reactive`。

#### 【toRefs 与 toRef】

- 作用：**将一个响应式对象中的每一个属性，转换为**`ref`**对象。**【解析的属性与对象同步】

- 备注：`toRefs`与`toRef`功能一致，但`toRefs`可以批量转换。

- 语法如下：

```
<template>
  <div class="person">
    <h2>姓名：{{person.name}}</h2>

    <h2>年龄：{{person.age}}</h2>

    <h2>性别：{{person.gender}}</h2>

    <button @click="changeName">修改名字</button>

    <button @click="changeAge">修改年龄</button>

    <button @click="changeGender">修改性别</button>

  </div>

</template>

<script lang="ts" setup name="Person">
  import {ref,reactive,toRefs,toRef} from 'vue'

  // 数据
  let person = reactive({name:'张三', age:18, gender:'男'})
    
  // 通过toRefs将person对象中的n个属性批量取出，且依然保持响应式的能力
  let {name,gender} =  toRefs(person)
    
  // 通过toRef将person对象中的gender属性取出，且依然保持响应式的能力
  let age = toRef(person,'age')

  // 方法
  function changeName(){
    name.value += '~'
  }
  function changeAge(){
    age.value += 1
  }
  function changeGender(){
    gender.value = '女'
  }
</script>
```

### 属性绑定-v-bind

v-bind 默认数据不具备响应式特性

响应式特性数据的变化可以更新到页面效果上

想要响应式地绑定一个 attribute，应该使用 `v-bind` [指令](https://cn.vuejs.org/api/built-in-directives.html#v-bind)：

`v-bind` 指令指示 Vue 将元素的 `id` attribute 与组件的 `dynamicId` 属性保持一致。如果绑定的值是 `null` 或者 `undefined`，那么该 attribute 将会从渲染的元素上移除。

- 使用 `v-bind:属性='xx'`语法，可以为标签的某个属性绑定值；

- 可以简写为 `:属性='xx'`

```
<script setup>
  //
  let url = "http://www.baidu.com"
</script>

<template>
  <a v-bind:href="url">go</a>

  <a :href="url">go</a>

</template>

<style scoped>

</style>
```

注意：此时如果我们想修改变量的值，属性值并不会跟着修改。可以测试下。因为还没有响应式特性

```
<script setup lang="ts">
import { ref } from 'vue'
const path = ref('/src/assets/vue.svg')

</script>

<template>
  <img :src="path" alt="">
</template>
```

- 【: 属性名】用来将标签属性与【响应式】变量绑定

- src和它之外的路径写法（public下直接调用，不用写路径），src要写完整路径

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615841-d165634d-ea3f-4f06-97ad-a7057995352c.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615895-283e66f1-67fe-4033-9b2c-6ca90e6c72b5.png "null")

### 表单绑定 v-model

页面上需要用户输入的信息需要双向绑定

页面上数据 与 js数据同步

```
<script setup lang="ts">
import { ref } from "vue";
const user = ref({
  name:'张三',
  age:18,
  sex:'男',
  fav:['游泳','打球']
})

function saveUser() {
  console.log(user.value)
}
</script>

<template>
  <div class="outer">
    <div>
      <label for="">请输入姓名</label>

      <input type="text" v-model="user.name"/>
    </div>

    <div>
      <label for="">请输入年龄</label>

      <input type="text" v-model="user.age"/>
    </div>

    <div>
      <label for="">请选择性别</label>

      男 <input type="radio" value="男" v-model="user.sex"/> 
      女 <input type="radio" value="女" v-model="user.sex"/>
    </div>

    <div>
      <label for="">请选择爱好</label>

      游泳 <input type="checkbox" value="游泳" v-model="user.fav"/> 
      打球 <input type="checkbox" value="打球" v-model="user.fav"/> 
      健身 <input type="checkbox" value="健身" v-model="user.fav"/>
    </div>

    <div>
      <input type="button" value="保存" @click="saveUser">
    </div>

  </div>

</template>

<style scoped>
  div {
    margin-bottom: 8px;
  }
  .outer {
    width: 100%;
    position: relative;
    padding-left: 80px;
  }
  label {
    text-align: left;
    width: 100px;
    display: inline-block;
    position: absolute;
    left :0;
  }
</style>
```

- **用 v-model 实现双向绑定**，即

- javascript 数据可以同步到表单标签

- 反过来用户在表单标签输入的新值也会同步到 javascript 这边

- 双向绑定只适用于表单这种带【输入】功能的标签，其它标签的数据绑定，单向就足够了

- 复选框这种标签，双向绑定的 javascript 数据类型一般用数组

### 计算属性-computed

计算属性：根据已有数据计算出新数据

有时在数据展示时要做简单的计算

```
<script setup lang="ts">
import { ref } from 'vue'
const firstName = ref('三')
const lastName = ref('张')

</script>

<template>
  <h2>{{lastName + firstName}}</h2>

  <h3>{{lastName + firstName}}</h3>

  <h4>{{lastName + firstName}}</h4>

</template>
```

看起来较为繁琐，可以用计算属性改进

```
<script setup lang="ts">
import { ref, computed } from 'vue'
const firstName = ref('三')
const lastName = ref('张')
const fullName = computed(() => {
  console.log('enter')
  return lastName.value + firstName.value
})
</script>

<template>
  <h2>{{fullName}}</h2>

  <h3>{{fullName}}</h3>

  <h4>{{fullName}}</h4>

</template>
```

- fullName 即为**计算属性，它具备缓存功能**，即 firstName 和 lastName 的值发生了变化，才会重新计算

- **如果用函数实现相同功能，则没有缓存功能**

```
<script setup lang="ts">
import { ref } from 'vue'
const firstName = ref('三')
const lastName = ref('张')
function fullName() {
  console.log('enter')
  return lastName.value + firstName.value
}
</script>

  
<template>
  <h2>{{fullName()}}</h2>

  <h3>{{fullName()}}</h3>

  <h4>{{fullName()}}</h4>

</template>
```

### 模板引用

`ref` 是一个特殊的 attribute，和 `v-for` 章节中提到的 `key` 类似。它允许我们在一个特定的 DOM 元素或子组件实例被挂载后，获得对它的直接引用

#### 【标签的 ref 属性】

作用：**用于注册模板引用。**

- 用在普通`DOM`标签上，获取的是`DOM`节点。

- 用在组件标签上，获取的是组件实例对象。

##### 用在普通`DOM`标签上：

1. `ref` **赋值**：  
    在 Vue3 中，`ref` 用于在模板中引用 DOM 元素，而不是在 `<script>` 中手动创建。需要在模板中将 `ref` 属性与变量关联起来。

2. `ref` **使用方式**：  
    你需要在 `<script>` 中使用 `ref` 变量来访问模板中的 DOM 元素，而不是 `document.getElementById`。`ref` 的值会被自动填充为对应的 DOM 元素。

以下是修正后的代码：

```
<template>
  <div class="person">
    <h1 ref="title1">学习</h1>

    <h2 ref="title2">前端</h2>

    <h3 ref="title3">Vue</h3>

    <input type="text" ref="inpt"> <br><br>
    <button @click="showLog">点我打印内容</button>

  </div>

</template>

<script lang="ts" setup>
import { ref } from 'vue'

// 用于存储ref标记的内容
const title1 = ref<HTMLElement | null>(null)
const title2 = ref<HTMLElement | null>(null)
const title3 = ref<HTMLElement | null>(null)

function showLog() {
  // 通过ref获取元素
  console.log(title1.value?.innerText)
  console.log(title2.value?.innerText)
  console.log(title3.value?.innerText)
}
</script>
```

**关键点**

1. **模板中的** `ref`：  
    在模板中，你的 `ref` 是在 `<h1>`、`<h2>` 和 `<h3>` 标签上声明的。Vue 会自动将这些元素赋值给 `ref` 变量 `title1`、`title2` 和 `title3`。

2. **访问** `ref` **的值**：  
    在 `<script>` 中，`ref` 变量的值是一个包含 DOM 元素的对象，你需要通过 `.value` 访问这个 DOM 元素。在 Vue 3 中，`ref` 返回的是一个响应式对象，所以你需要使用 `.value` 来访问实际的 DOM 元素。

3. `HTMLElement | null`：  
    使用 TypeScript 时，可以为 `ref` 添加类型注解，表示 `ref` 的值可能是 `HTMLElement` 或 `null`。这样可以帮助你避免访问 `null` 时出现错误。

##### **用在组件标签上：**

```
<!-- 父组件App.vue -->
<template>
  <Person ref="ren"/>
  <button @click="test">测试</button>

</template>

<script lang="ts" setup name="App">
  import Person from './components/Person.vue'
  import {ref} from 'vue'

  let ren = ref()

  function test(){
    console.log(ren.value.name)
    console.log(ren.value.age)
  }
</script>


<!-- 子组件Person.vue中要使用defineExpose暴露内容 -->

<script lang="ts" setup name="Person">
  import {ref,defineExpose} from 'vue'
    // 数据
  let name = ref('张三')
  let age = ref(18)
  /****************************/
  /****************************/
  // 使用defineExpose将组件中的数据交给外部
  defineExpose({name,age})
</script>
```

### 组件深入

#### 使用组件

要使用一个子组件，我们需要在父组件中导入它。假设我们把计数器组件放在了一个叫做 `ButtonCounter.vue` 的文件中，这个组件将会以默认导出的形式被暴露给外部。

```
<script setup>
import ButtonCounter from './ButtonCounter.vue'
</script>

<template>
  <h1>Here is a child component!</h1>

  <ButtonCounter />
</template>
```

通过 `<script setup>`，导入的组件都在模板中直接可用。

当然，你也可以全局地注册一个组件，使得它在当前应用中的任何组件上都可以使用，而不需要额外再导入。

#### 全局注册

我们可以使用 [Vue 应用实例](https://cn.vuejs.org/guide/essentials/application.html)的 `.component()` 方法，让组件在当前 Vue 应用中全局可用。

```
import { createApp } from 'vue'

const app = createApp({})

app.component(
  // 注册的名字
  'MyComponent',
  // 组件的实现
  {
    /* ... */
  }
)
```

如果使用单文件组件，你可以注册被导入的 `.vue` 文件：

```
import MyComponent from './App.vue'

app.component('MyComponent', MyComponent)
```

`.component()` 方法可以被链式调用：

```
app
  .component('ComponentA', ComponentA)
  .component('ComponentB', ComponentB)
  .component('ComponentC', ComponentC)
```

全局注册的组件可以在此应用的任意组件的模板中使用：

```
<!-- 这在当前应用的任意组件中都可用 -->
<ComponentA/>
<ComponentB/>
<ComponentC/>
```

### 组件传值

#### 父传子 - Props

父组件给子组件传递值；

**单向数据流**效果：

- 父组件修改值，子组件发生变化

- 子组件修改值，父组件不会感知到

```
//父组件给子组件传递数据：使用属性绑定
<Son :books="data.books" :money="data.money"/>
  
//子组件定义接受父组件的属性
let props = defineProps({
  money: {
    type: Number,
    required: true,
    default: 200
  },
  books: Array
});
```

- 声明数据

- 在子组件中绑定属性

- defineProps声明接收数据

`App.vue`中代码：

```
// 定义一个接口，限制每个Person对象的格式
export interface PersonInter {
id:string,
name:string,
age:number
}

// 定义一个自定义类型Persons
export type Persons = Array<PersonInter>
```

```
<template>
    <Person :list="persons"/>
</template>
```

```

<template>
  <div class="person">
    <ul>
      <li v-for="item in list" :key="item.id">
        {{item.name}}--{{item.age}}
      </li>
```

### 解释

1. `defineProps` **函数**：

- `defineProps` 是 Vue 3 的一个 Composition API 函数，用于定义一个组件的 `props`。它接受一个泛型参数，指定 `props` 的类型。
- 在这段代码中，`defineProps<{ list?: Persons }>()` 定义了一个 `list` 属性，它是可选的（`?` 表示可选），类型为 `Persons`。

2. `withDefaults` **函数**：

- `withDefaults` 是一个用于为 `defineProps` 中定义的 `props` 提供默认值的函数。
- 在这段代码中，`withDefaults` 函数接收两个参数：第一个是通过 `defineProps` 定义的 `props`，第二个是一个对象，用于定义默认值。

3. **默认值的设置**：

- `list` 属性的默认值是一个返回数组的函数（`list: () => [...]`）。这个数组包含一个对象，其中有 `id`、`name` 和 `age` 属性。
- 使用函数而不是直接赋值，是因为在 Vue 中，引用类型的 `props` 默认值应使用工厂函数（即返回值为对象或数组的函数），以避免所有组件实例共享相同的引用。

#### 子传父 - Emit

props 用来父传子，emit 用来子传父

```
//子组件定义发生的事件
let emits = defineEmits(['buy']);
function buy(){
  // props.money -= 5;
  emits('buy',-5);
}

//父组件感知事件和接受事件值
  <Son :books="data.books" :money="data.money"
       @buy="moneyMinis"/>
```

这段代码是一个 Vue 3 组件中的一部分，用于处理一个名为 `buy` 的事件。让我来详细解释一下：

1. 首先，您使用了 `defineEmits` 函数来定义了一个名为 `emits` 的变量。这个函数允许您**声明组件可以触发的事件**。

2. 然后，在 `buy` 函数中，您调用了 `emits` 函数，并传递了两个参数：

- 第一个参数是事件名称 `'buy'`，表示您要触发的事件是 `buy`。

- 第二个参数是 `-5`，表示您要传递给事件处理程序的数据。

3. 在注释中，您提到了 `props.money -= 5;`，但是在这段代码中并没有直接操作 `props`。如果您想要更新组件的 `money` 属性，您需要在组件的 `props` 中定义它，并在适当的地方进行更新。

总之，这段代码用于触发一个名为 `buy` 的事件，并传递了一个值为 `-5` 的参数。

在父组件中

```
function moneyMinis(arg){
  // alert("感知到儿子买了棒棒糖"+arg)
  data.money+=arg;
}
```

```
<Son :books="data.books" :money="data.money" @buy="moneyMinis"/>
```

思考：兄弟传值

- 利用父子传值即可 子1-》父-》子2

```
<script setup>

import Son from "./Son.vue";
import {reactive, ref} from "vue";

//1、 父传子：单向数据流
// const money = ref(100);
// const books = ref(["西游记","水浒传"])

const data = reactive({
  money: 100,
  books: ["西游记","水浒传"]
})

function moneyMinis(arg){
  // alert("感知到儿子买了棒棒糖"+arg)
  data.money+=arg;
}
</script>

<template>
<div style="background-color: #f9f9f9">
  <h2>Father</h2>

  <button @click="data.money+=10">充值</button>

<!--  <Son :books="data.books" :money="data.money"-->
<!--       @buy="moneyMinis"/>-->
  <Son v-bind="data">
    <template v-slot:title>
      哈哈SonSon
    </template>

    <template #btn>
      买飞机
    </template>

  </Son>

</div>

</template>

<style scoped>

</style>


```

```
<script setup>
//1、定义属性：只读
// let props = defineProps(['money','books']);

let props = defineProps({
  money: {
    type: Number,
    required: true,
    default: 200
  },
  books: Array
});



//2、使用emit: 定义事件
let emits = defineEmits(['buy']);
function buy(){
  // props.money -= 5;
  emits('buy',-5);
}
</script>

<template>
<div style="background-color: #646cff;color: white">
  <h3>
    <slot name="title">
      哈哈Son
    </slot>

  </h3>

  <div>账户：{{props.money}}</div>

  <div>图书：
    <li v-for="b in props.books">{{b}}</li>

  </div>

  <button @click="buy">
    <slot name="btn"/>
  </button>

</div>

</template>

<style scoped>

</style>
```

### 插槽 - Slots

子组件可以使用插槽接受模板内容。【HTML内容】

`<slot>` 元素是一个**插槽出口** (slot outlet)，标示了父元素提供的**插槽内容** (slot content) 将在哪里被渲染。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444615950-cb232805-35a3-4e22-9814-cde464803299.png "null")

#### 基本使用

```
<!-- 组件定义 -->
<button >
  <slot></slot> <!-- 插槽出口 -->
</button>

<!-- 组件使用 -->
<FancyButton>
  Click me! <!-- 插槽内容 -->
</FancyButton>
```

#### 默认内容

```
<button type="submit">
  <slot>
    Submit <!-- 默认内容 -->
  </slot>

</button>
```

#### 具名插槽

部分使用场景

定义

```
<div class="container">
  <header>
    <slot name="header"></slot>

  </header>

  <main>
    <slot></slot>

  </main>

  <footer>
    <slot name="footer"></slot>

  </footer>

</div>
```

使用： `v-slot`可以简写为 `#`

```
<BaseLayout>
  <template v-slot:header>
    <!-- header 插槽的内容放这里 -->
  </template>

</BaseLayout>
```

#### 作用域插槽

插槽留出数据接口 可以向父组件进行数据传递

```
<!-- <MyComponent> template -->
<div>
  <slot :message="hello"></slot>
  <slot name="footer" />
</div>
```

```
<!-- 该模板无法编译 -->
<MyComponent v-slot="{ message }">
  <p>{{ message }}</p>
  <template #footer>
    <!-- message 属于默认插槽，此处不可用 -->
    <p>{{ message }}</p>
  </template>
</MyComponent>
```

## 4) 进阶用法

### 前后端交互⭐

#### xhr

上传文件时可以监测进度

浏览器中有两套 API 可以和后端交互，发送请求、接收响应，fetch api 前面我们已经介绍过了，另一套 api 是 xhr，基本用法如下

```
const xhr = new XMLHttpRequest()
xhr.onload = function() { //响应返回后会触发事件onload事件 。在发送前定义接受，防止响应提前没有触发
    console.log(xhr.response) //接受响应
}
xhr.open('GET', 'http://localhost:8080/api/students') //准备工作
xhr.responseType = "json" //请求数据格式
xhr.send() //发送
```

但这套 api 虽然功能强大，但比较老，不直接支持 Promise，因此有必要对其进行改造【promise改造】

```
function get(url: string) {
  return new Promise((resolve, reject)=>{ //构造promise对象
    const xhr = new XMLHttpRequest()
    xhr.onload = function() {
      if(xhr.status === 200){
        resolve(xhr.response)  //resolve正确响应接受
      } else if(xhr.status === 404) {
        reject(xhr.response)   //reject错误接受
      } // 其它情况也需考虑，这里简化处理
    }
    xhr.open('GET', url)
    xhr.responseType = 'json'
    xhr.send()
  })
}
```

- Promise 对象适合用来封装异步操作，并可以配合 await 一齐使用

- Promise 在构造时，需要一个箭头函数，箭头函数有两个参数 resolve 和 reject

- resolve 是异步操作成功时被调用，把成功的结果传递给它，最后会作为 await 的结果返回

- reject 在异步操作失败时被调用，把失败的结果传递给它，最后在 catch 块被捉住

- **await 会一直等到 Promise 内调用了 resolve 或 reject 才会继续向下运行**

调用示例1：同步接收结果，不走代理

```
try {
  const resp = await get("http://localhost:8080/api/students")
  console.log(resp)
} catch (e) {
  console.error(e)
}
```

调用示例2：走代理

```
try {
  const resp = await get('/api/students')
  console.log(resp)  
} catch(e) {
  console.log(e)
}
```

- 走代理明显慢不少

#### axios⭐⭐⭐

##### 基本用法

axios 就是对 xhr api 的封装，手法与前面例子类似，简化封装

安装

```
npm install axios
```

一个简单的例子

```
<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

let count = ref(0);

async function getStudents() {
  try {
    const resp = await axios.get("/api/students");
    count.value = resp.data.data.length;
  } catch (e) {
    console.log(e);
  }
}

onMounted(() => {
  getStudents()
})
</script>

<template>
  <h2>学生人数为：{{ count }}</h2>

</template>
```

- **onMounted** 指 vue 组件生成的 html 代码片段，**挂载完毕后被执行**![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444616005-7b6116da-8f53-4cc6-b707-68fd0f74974a.png "null")

再来看一个 post 例子

```
<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

const student = ref({
  name: '',
  sex: '男',
  age: 18
})

async function addStudent() {
  console.log(student.value)
  const resp = await axios.post('/api/students', student.value)
  console.log(resp.data.data)
}
</script>

<template>
  <div>
    <div>
      <input type="text" placeholder="请输入姓名" v-model="student.name"/>
    </div>

    <div>
      <label for="">请选择性别</label>

      男 <input type="radio" value="男" v-model="student.sex"/> 
      女 <input type="radio" value="女" v-model="student.sex"/>
    </div>

    <div>
      <input type="number" placeholder="请输入年龄" v-model="student.age"/>
    </div>

    <div>
      <input type="button" value="添加" @click="addStudent"/>
    </div>

  </div>

</template>

<style scoped>
div {
  font-size: 14px;
}
</style>
```

##### 环境变量

- 开发环境下，联调的后端服务器地址是 `http://localhost:8080`，

- 上线改为生产环境后，后端服务器地址为 `http://itheima.com`

这就要求我们区分开发环境和生产环境，这件事交给构建工具 vite 来做

默认情况下，vite 支持上面两种环境，分别对应根目录下两个配置文件

- .env.development - 开发环境

- .env.production - 生产环境

针对以上需求，分别在两个文件中加入

```
VITE_BACKEND_API_BASE_URL = 'http://localhost:8080'
```

和

```
VITE_BACKEND_API_BASE_URL = 'http://itheima.com'
```

然后在代码中使用 vite 给我们提供的特殊对象 `import.meta.env`，就可以获取到 `VITE_BACKEND_API_BASE_URL` 在不同环境下的值

```
import.meta.env.VITE_BACKEND_API_BASE_URL
```

默认情况下，不能**智能提示自定义的环境变量**，做如下配置：新增文件 `src/env.d.ts` 并添加如下内容

```
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_BACKEND_API_BASE_URL: string
  // 更多环境变量...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

- 参考文档地址 [环境变量和模式 | Vite 官方中文文档 (vitejs.dev)](https://cn.vitejs.dev/guide/env-and-mode.html)

##### baseURL

可以自己创建一个 axios 对象，方便添加默认设置，新建文件 /src/api/request.ts

```
// 创建新的 axios 对象
import axios from 'axios'
const _axios = axios.create({ //新封装的axios对象
  baseURL: import.meta.env.VITE_BACKEND_API_BASE_URL
})

export default _axios
```

然后在其它组件中引用这个 ts 文件，例如 /src/views/E8.vue，就不用自己拼接路径前缀了

```
<script setup lang="ts">
import axios from '../api/request'
// ...
await axios.post('/api/students', ...)    
</script>
```

##### 拦截器

统一错误处理返回

简化数据返回【少调用一次then，直接返回resp.data】

```
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    return response;
  }, function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    return Promise.reject(error);
  });
```

```
// 创建新的 axios 对象
import axios from 'axios'
const _axios = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_API_BASE_URL
})

// 请求拦截器
_axios.interceptors.request.use(
  (config)=>{ // 统一添加请求头
    config.headers = {
      Authorization: 'aaa.bbb.ccc'
    }
    return config
  },
  (error)=>{ // 请求出错时的处理
    return Promise.reject(error)
  }
)

// 响应拦截器
_axios.interceptors.response.use(
  (response)=>{ // 状态码  2xx
    // 这里的code是自定义的错误码【后端的code】响应但不正确
    if(response.data.code === 200) {
      return response
    }     
    else if(response.data.code === 401) {       
      // 情况1
      return Promise.resolve({})
    }
    // ... 
  },
  (error)=>{ // 状态码 > 2xx, 400,401,403,404,500
    console.error(error) // 处理了异常
    if(error.response.status === 400) {
      // 情况1
    } else if(error.response.status === 401) {
      // 情况2
    } 
    // ...
    return Promise.resolve({}) //继续执行，返回空对象
  }
)

export default _axios
```

处理响应时，又分成两种情况

1. 后端返回的是标准响应状态码，这时会走响应拦截器第二个箭头函数，用 error.response.status 做分支判断

2. 后端返回的响应状态码总是200，用自定义错误码表示出错，这时会走响应拦截器第一个箭头函数，用 response.data.code 做分支判断

另外

- Promise.reject(error) 类似于将异常继续向上抛出，异常由调用者（Vue组件）来配合 try ... catch 来处理

- Promise.resolve({}) 表示错误已解决，返回一个空对象，调用者中接到这个空对象时，需要配合 ?. 来避免访问不存在的属性

### 条件与列表

首先，新增**模型数据** src/model/Model8080.ts

```
export interface Student {
  id: number;
  name: string;
  sex: string;
  age: number;
}

// 如果 spring 错误，返回的对象格式
export interface SpringError {
  timestamp: string,
  status: number,
  error: string,
  message: string,
  path: string
}

// 如果 spring 成功，返回 list 情况
export interface SpringList<T> {
  data: T[],
  message?: string,
  code: number
}

// 如果 spring 成功，返回 page 情况
export interface SpringPage<T> {
  data: { list: T[], total: number },
  message?: string,
  code: number
}

// 如果 spring 成功，返回 string 情况
export interface SpringString {
  data: string,
  message?: string,
  code: number
}

import { AxiosResponse } from 'axios'
export interface AxiosRespError extends AxiosResponse<SpringError> { } //
export interface AxiosRespList<T> extends AxiosResponse<SpringList<T>> { }
export interface AxiosRespPage<T> extends AxiosResponse<SpringPage<T>> { }
export interface AxiosRespString extends AxiosResponse<SpringString> { }
```

其中

- AxiosRespPage 代表分页时的响应类型

- AxiosRespList 代表返回集合时的响应类型

- AxiosRespString 代表返回字符串时的响应类型

- AxiosRespError 代表 Spring 出错时时的响应类型

```
<script lang="ts" setup>
import { ref, onMounted } from "vue";
import axios from "../api/request";
import { Student, SpringList } from "../model/Model8080";

// 说明 students 数组类型为 Student[]
const students = ref<Student[]>([]);

async function getStudents() {
  // 说明 resp.data 类型是 SpringList<Student>
  const resp = await axios.get<SpringList<Student>>("/api/students");  
  console.log(resp.data.data);
  students.value = resp.data.data;
}

onMounted(() => getStudents());
</script>

<template>
  <div class="outer">
    <div class="title">学生列表</div>

    <div class="thead">
      <div class="row bold">
        <div class="col">编号</div>

        <div class="col">姓名</div>

        <div class="col">性别</div>

        <div class="col">年龄</div>

      </div>

    </div>

    <div class="tbody">
      <div v-if="students.length === 0">暂无数据</div>

      <template v-else>
        <div class="row" v-for="s of students" :key="s.id">
          <div class="col">{{ s.id }}</div>

          <div class="col">{{ s.name }}</div>

          <div class="col">{{ s.sex }}</div>

          <div class="col">{{ s.age }}</div>

        </div>

      </template>

    </div>

  </div>

</template>

<style scoped>
.outer {
  font-family: 华文行楷;
  font-size: 20px;
  width: 500px;
}

.title {
  margin-bottom: 10px;
  font-size: 30px;
  color: #333;
  text-align: center;
}

.row {
  background-color: #fff;
  display: flex;
  justify-content: center;
}

.col {
  border: 1px solid #f0f0f0;
  width: 15%;
  height: 35px;
  text-align: center;
  line-height: 35px;
}

.bold .col {
  background-color: #f1f1f1;
}
</style>
```

- 加入泛型是为了更好的提示

- **v-if 与 v-else 不能和 v-for 处于同一标签**

- template 标签还有一个用途，就是用它少生成一层真正 html 代码

- 可以看到将结果封装为响应式数据还是比较繁琐的，后面会使用 useRequest 改进

### 监听器- watch/watchEffect

单个 精准监听

```
watch(num,(value, oldValue, onCleanup)=>{
  console.log("value",value)
  console.log("oldValue",oldValue)
  if(num.value > 3){
    alert("超出限购数量")
    num.value = 3;
  }
})
```

多个【使用更多】

```
watchEffect(() => {
  if (num.value > 3) {
    alert("超出限购数量")
    num.value = 3;
  }

  if (car.price > 11000) {
    alert("太贵了")
    car.price = 11000;
  }
})
```

利用监听器，可以在【响应式】的基础上添加一些副作用，把更多的东西变成【响应式的】

- 原本只是数据变化 => 页面更新

- watch 可以在数据变化时 => 其它更新

```
<template>
  <input type="text" v-model="name" />
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
function useStorage(name: string) {
  const data = ref(sessionStorage.getItem(name) ?? ""); //初始值为会话存储数据
  watch(data, (newValue) => {
    sessionStorage.setItem(name, newValue);
  });
  return data;
}
const name = useStorage("name");
</script>
```

- 名称为 useXXXX 的函数，作用是**返回带扩展功能的【响应式】数据**

- **localStorage 即使浏览器关闭，数据还在**

- **sessionStorage 数据工作在浏览器活动期间**

### API 工具库-vueuse

封装好的返回带扩展功能的【响应式】数据方法

安装

```
npm install @vueuse/core
```

一些函数的用法

```
<template>
  <h3>X: {{x}}</h3>

  <h3>Y: {{y}}</h3>

  <h3>{{count}}</h3>

  <input type="button" @click="inc()" value="+">
  <input type="button" @click="dec()" value="-">

  <input type="text" v-model="name">
</template>

<script setup lang="ts">
import { useMouse, useCounter, useStorage } from '@vueuse/core'

const {x, y} = useMouse()

const {count, inc, dec} = useCounter()

const name = useStorage("name", "") //不写默认本地
</script>
```

### 响应式的 axios 封装-useRequest

**响应式的 axios 封装**，官网地址 [一个 Vue 请求库 | VueRequest (attojs.org)](https://next.cn.attojs.org/)

首先安装 vue-request

```
npm install vue-request@next
```

组件

```
<template>
  <h3 v-if="students.length === 0">暂无数据</h3>

  <ul v-else>
    <li v-for="s of students" :key="s.id">
      <span>{{s.name}}</span>

      <span>{{s.sex}}</span>

      <span>{{s.age}}</span>

    </li>

  </ul>

</template>

<script setup lang="ts">
import axios from "../api/request"
import { useRequest } from 'vue-request'
import { computed } from 'vue'
import { AxiosRespList, Student } from '../model/Model8080'

// data 代表就是 axios 的响应对象
const { data } = useRequest<AxiosRespList<Student>>(() => axios.get('/api/students'))

const students = computed(()=>{
  return data?.value?.data.data || []
})
</script>

<style scoped>
ul li {
  list-style: none;
  font-family: "华文行楷";
}

li span:nth-child(1) {
  font-size: 24px;
}
li span:nth-child(2) {
  font-size: 12px;
  color: crimson;
  vertical-align: bottom;
}
li span:nth-child(3) {
  font-size: 12px;
  color: darkblue;
  vertical-align: top;
}
</style>
```

- data.value 的取值一开始是 undefined，随着响应返回变成 axios 的响应对象

- 用 computed 进行适配

### 分页-usePagination⭐

在 src/model/Model8080.ts 中补充类型说明

```
export interface StudentQueryDto {
  name?: string,
  sex?: string,
  age?: string, // 18,20
  page: number,
  size: number
}
```

- js 中类似于 18,20 这样以逗号分隔字符串，会在 get 传参时转换为 java 中的整数数组

编写组件

```
<template>
  <input type="text" placeholder="请输入姓名" v-model="dto.name">
  <select v-model="dto.sex">
    <option value="" selected>请选择性别</option>

    <option value="男">男</option>

    <option value="女">女</option>

  </select>

  <input type="text" placeholder="请输入年龄范围" v-model="dto.age">
  <br>
  <input type="text" placeholder="请输入页码" v-model="dto.page">
  <input type="text" placeholder="请输入页大小" v-model="dto.size">
  <input type="button" value="搜索" @click="search">
  <hr>
  <h3 v-if="students.length === 0">暂无数据</h3>

  <ul v-else>
    <li v-for="s of students" :key="s.id">
      <span>{{s.name}}</span>

      <span>{{s.sex}}</span>

      <span>{{s.age}}</span>

    </li>

  </ul>

  <hr>
  总记录数{{total}} 总页数{{totalPage}}
</template>

<script setup lang="ts">
import axios from "../api/request"
import { usePagination } from 'vue-request'
import { computed, ref } from 'vue'
import { AxiosRespPage, Student, StudentQueryDto } from '../model/Model8080'

const dto = ref<StudentQueryDto>({name:'', sex:'', age:'', page:1, size:5})

// data 代表就是 axios 的响应对象
// 泛型参数1: 响应类型
// 泛型参数2: 请求类型
const { data, total, totalPage, run } = usePagination<AxiosRespPage<Student>, StudentQueryDto[]>(
  (d) => axios.get('/api/students/q', {params: d}), // 箭头函数
  {
    defaultParams: [ dto.value ], // 默认参数, 会作为参数传递给上面的箭头函数
    pagination: {
      currentKey: 'page', // 指明当前页属性
      pageSizeKey: 'size', // 指明页大小属性
      totalKey: 'data.data.total' // 指明总记录数属性
    } 
  } // 选项
)

const students = computed(()=>{
  return data?.value?.data.data.list || []
})

function search() {
  run(dto.value) // 会作为参数传递给usePagination的箭头函数
}
</script>

<style scoped>
ul li {
  list-style: none;
  font-family: "华文行楷";
}

li span:nth-child(1) {
  font-size: 24px;
}
li span:nth-child(2) {
  font-size: 12px;
  color: crimson;
  vertical-align: bottom;
}
li span:nth-child(3) {
  font-size: 12px;
  color: darkblue;
  vertical-align: top;
}
input,select {
  width: 100px;
}
</style>
```

- usePagination 只需要定义一次，后续还想用它内部的 axios 发请求，只需调用 run 函数

### 子组件

##### 例1

定义子组件 Child1

```
<template>
  <div class="container">
    <div class="card">
      <div>
        <p class="name">{{name}}</p>

        <p class="location">{{country}}</p>

      </div>

      <img :src="avatar || '/src/assets/vue.svg'"/>
    </div>

  </div>

</template>

<script setup lang="ts">
    
// 定义属性,  编译宏
defineProps<{name:string,country:string,avatar?:string}>()
    
</script>

<style scoped>
.container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  flex-direction: row-reverse;
}
.name {
  font-weight: bold;
}
.location {
  font-size: 0.8em;
  color: #6d597a;
}
.card {
  display: flex;
  justify-content: space-evenly;
  padding: 1em;
  margin: 1rem;
  border-radius: 5px;
  background: #fff;
  width: 200px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

.card:hover {
  transform: rotate(-5deg);
}

.card img {
  margin-left: 1em;
  border-radius: 50%;
  max-width: 55px;
  max-height: 55px;
}
</style>
```

父组件引用

```
<template>
  <Child1 name="张三" country="中国" avatar="/src/assets/vue.svg"></Child1>

  <Child1 name="李四" country="印度" avatar="/vite.svg"></Child1>

  <Child1 name="王五" country="韩国" ></Child1>

</template>

<script lang="ts" setup>
import Child1 from '../components/Child1.vue';
</script>
```

##### 例2

首先添加类型说明 model/ModelRandomUser.ts

```
import { AxiosResponse } from "axios";
export interface AxiosRespResults extends AxiosResponse<Results>{}

export interface Results {
  info: {
    page: number,
    results: number
  },
  results: Result[]
}

export interface Result {
  gender: 'male' | 'female',
  name: {
    first: string,
    last: string
  },
  location: {
    country: string
  },
  picture: {
    medium: string
  },
  login: {
    username: string
  }
}
```

子组件不变，父组件使用子组件

```
<!-- 父组件 -->
<template>
  <Child1 v-for="u of users" 
    :name="u.name.first" 
    :country="u.location.country" 
    :avatar="u.picture.medium"
    :key="u.login.username"></Child1>

</template>

<script setup lang="ts">
import axios from "axios";
import { useRequest } from "vue-request";
import { computed } from "vue";
import { AxiosRespResults } from '../model/ModelRandomUser'
import Child1 from "../components/Child1.vue";

const { data } = useRequest<AxiosRespResults>(
  ()=>axios.get('https://randomuser.me/api/?results=3')
)

const users = computed(()=>{
  return data.value?.data.results || []
})
</script>
```

如果觉得 Result 数据结构嵌套太复杂，还可以做一个类型映射

```
<!-- 父组件 -->
<template>
  <Child1 v-for="u of users" 
    :name="u.name" 
    :country="u.country" 
    :avatar="u.avatar"
    :key="u.username"></Child1>

</template>

<script setup lang="ts">
import axios from "axios";
import { useRequest } from "vue-request";
import { computed } from "vue";
import { AxiosRespResults, Result } from '../model/ModelRandomUser'
import Child1 from "../components/Child1.vue";

const { data } = useRequest<AxiosRespResults>(
  ()=>axios.get('https://randomuser.me/api/?results=3')
)

const users = computed(()=>{
  return data.value?.data.results.map(resultToUser) || []
})

interface User {
  name: string,
  country: string,
  avatar: string,
  username: string
}
function resultToUser(r:Result):User {
  return {
    name: r.name.first,
    country: r.location.country,
    avatar: r.picture.medium,
    username: r.login.username
  }
}
</script>
```

- resultToUser 将 Result 类型映射为 User 类型