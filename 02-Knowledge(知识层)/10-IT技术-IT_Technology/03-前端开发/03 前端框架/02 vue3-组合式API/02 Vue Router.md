# Vue-Router

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618113-a4dd4940-4f1d-40d9-9545-8e1a483a7e88.png "null")

## 安装

```
npm install vue-router@4
```

## 创建 router

在router目录下进行配置

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737367115963-507ae45e-6238-472e-a2f6-7faa0fdf7df4.png)

index.ts 引入路由 createRouter创建路由器实例

routers 可以定义 路由与组件的对应关系数组

首先创建一个 /src/router/a5router.ts 文件，在其中定义路由

```
import {createRouter, createWebHashHistory} from 'vue-router'
import A51 from '../views/A51.vue'
import A52 from '../views/A52.vue'
// 路由 => 路径和组件之间的对应关系
const routes = [
  {
    path: '/a1',
    component: A51
  },
  {
    path: '/a2', 
    component: A52
  }
]

const router = createRouter({ 
  history: createWebHashHistory(), // 路径格式
  routes: routes // 路由数组
})

export default router
```

- createWebHashHistory 是用 # 符号作为【单页面】跳转技术，上面两个路由访问时路径格式为

- [http://localhost:7070/#/a1](http://localhost:7070/#/a1)

- [http://localhost:7070/#/a2](http://localhost:7070/#/a2)

- 每个路由都有两个必须属性

- path：路径

- component：组件

- createRouter 用来创建 router 对象，作为默认导出

需要在 main.ts 中导入 router 对象：

```
// ...
import A5 from './views/A5.vue'  // vue-router
import router from './router/a5router'
createApp(A5).use(antdv).use(router).mount('#app')
```

A5 是根组件，不必在 router 中定义，但需要在其中定义 router-view，用来控制路由跳转后，A51、A52 这些组件的显示位置，内容如下

```
<template>
  <div class="a5">
    <router-view></router-view>

  </div>

</template>
```

效果如下

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618180-4f09bd4a-2220-4ba6-b05c-242d616abfc7.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618249-56dd81e8-87fa-4f51-9762-f0b8103d3def.png "null")

## 动态导入

```
import {createRouter, createWebHashHistory} from 'vue-router'
import A51 from '../views/A51.vue'
import A52 from '../views/A52.vue'
const routes = [
  // ...
  {
    path: '/a3',
    component: () => import('../views/A53.vue')
  }
]
```

- **用 import 关键字导入，效果是打包时会将组件的 js 代码都打包成一个大的 js 文件，如果组件非常多，会影响页面加载速度**

- 而 import 函数导入（动态导入），则是按需加载，即

- 当路由跳转到 /a3 路径时，才会去加载 A53 组件对应的 js 代码

- vue-router 官方推荐采用动态导入

## 路由器工作模式

history 选项控制了路由和 URL 路径是如何双向映射的。

[https://router.vuejs.org/zh/guide/essentials/history-mode.html](https://router.vuejs.org/zh/guide/essentials/history-mode.html)

1. `history`模式【推荐】

优点：`URL`更加美观，不带有`#`，更接近传统的网站`URL`。

缺点：后期项目上线，需要服务端配合处理路径问题，否则刷新会有`404`错误。

```
const router = createRouter({
    history:createWebHistory(), //history模式
    /******/
})
```

问题：

当用户直接访问某个路由路径时（比如 `http://localhost:8080/profile`），浏览器会发起 HTTP 请求，而此时后端通常没有配置路径来处理这些前端路由请求。

后端通常只处理 API 请求（如 `/api/*`），并没有处理前端路由（如 `/profile`）。

**需要确保后端配置所有的非 API 路由，直接返回** `**index.html**`**，以便前端路由能够接管路径解析和页面渲染。**

**Spring Boot 配置**

即使是前后端分离，也需要配置 Spring Boot 来处理这些路径。你可以通过配置 `@Controller`，将所有的请求（除了 API 请求）都转发到 `index.html`。

```
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class FrontendController {

    // 所有前端路由都重定向到 index.html
    @RequestMapping(value = "/{path:[^\\.]*}")
    public String forwardToIndex() {
        return "forward:/index.html";
    }
}
```

2. `hash`模式

优点：兼容性更好，因为不需要服务器端处理路径。

缺点：`URL`带有`#`不太美观，且在`SEO`优化方面相对较差。

```
const router = createRouter({
    history:createWebHashHistory(), //hash模式
    /******/
})
```

**总结对比：**

|   |   |   |   |
|---|---|---|---|
|模式|特点|适用场景|示例 URL|
|**Hash 模式**|使用井号（#）来分隔路由，路径不会发送到服务器|不需要服务器配置支持，适用于简单应用|`http://example.com/#/home`|
|**Memory 模式**|内存中存储路由历史，不依赖 URL 地址|SSR 或隐藏 URL 路径的情况|无 URL，历史存储在内存中|
|**HTML5 模式****⭐**|使用 HTML5 History API，URL 清爽|需要控制服务器并支持前端路由的应用|`http://example.com/home`|

## 【to的两种写法】

```
<!-- 第一种：to的字符串写法 -->
<router-link active-class="active" to="/home">主页</router-link>

<!-- 第二种：to的对象写法 -->
<router-link active-class="active" :to="{path:'/home'}">Home</router-link>
```

## 【命名路由】

作用：可以简化路由跳转及传参（后面就讲）。

给路由规则命名：

```
routes:[
  {
    name:'zhuye',
    path:'/home',
    component:Home
  },
  {
    name:'xinwen',
    path:'/news',
    component:News,
  },
  {
    name:'guanyu',
    path:'/about',
    component:About
  }
]
```

跳转路由：

```
<!--简化前：需要写完整的路径（to的字符串写法） -->
<router-link to="/news/detail">跳转</router-link>

<!--简化后：直接通过名字跳转（to的对象写法配合name属性） -->
<router-link :to="{name:'guanyu'}">跳转</router-link>
```

## 嵌套路由

如果希望再嵌套更深层次的路由跳转，例如：希望在 A53 组件内再进行路由跳转

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618304-673130a5-cf85-49b2-b7e6-76185933d85b.png "null")

首先，修改 A53.vue

```
<template>
  <div class="a53">
    <router-view></router-view>

  </div>

</template>
```

其次，再修改 /src/router/a5router.ts 文件 内容

```
import {createRouter, createWebHashHistory} from 'vue-router'
import A51 from '../views/A51.vue'
import A52 from '../views/A52.vue'
const routes = [
  // ...
  {
    path: '/a3',
    component: () => import('../views/A53.vue'),
    children: [
      {
        path: 'student',
        component: () => import('../views/A531.vue')
      },
      {
        path: 'teacher',
        component: () => import('../views/A532.vue')
      }
    ]
  }
]

// ...
```

将来访问 /a3/student 时，效果为

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618351-024aebb7-56e1-4574-8ed9-871042e121cd.png "null")

访问 /a3/teacher 时，效果为

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618403-feba1cc9-35f9-4112-bb80-83db5409b324.png "null")

## 重定向

首页默认跳转

用法1

```
import {createRouter, createWebHashHistory} from 'vue-router'
import A51 from '../views/A51.vue'
import A52 from '../views/A52.vue'
const routes = [
  // ...
  {
    path: '/a3',
    component: () => import('../views/A53.vue'),
      
    redirect: '/a3/student', // 重定向到另外路径
      
    children: [
      {
        path: 'student',
        component: () => import('../views/A531.vue')
      },
      {
        path: 'teacher',
        component: () => import('../views/A532.vue')
      }
    ]
  }
]
// ...
```

效果是，页面输入 /a3，紧接着会重定向跳转到 /a3/student

用法2

```
import {createRouter, createWebHashHistory} from 'vue-router'
import A51 from '../views/A51.vue'
import A52 from '../views/A52.vue'
const routes = [
  {
    path: '/a1',
    component: A51
  },
  {
    path: '/a2', 
    component: A52
  },
  // ...
  {
    path: '/:pathMatcher(.*)*', // 可以匹配剩余的路径
    redirect: '/a2'
  }
]
// ...
```

效果是，当页面输入一个不存在路径 /aaa 时，会被 `path: '/:pathMatcher(.*)*'` 匹配到，然后重定向跳转到 A52 组件去

## 编程式

### useRoute：路由数据

路由传参跳转到指定页面后，页面需要取到传递过来的值，可以使用 `useRoute`方法；

拿到当前页路由数据；可以做

1. 获取到当前路径

2. 获取到组件名

3. 获取到参数

4. 获取到查询字符串

```
import {useRoute} from 'vue-router'
const route = useRoute()
// 打印query参数
console.log(route.query)
// 打印params参数
console.log(route.params)
```

### useRouter：路由器

拿到路由器；可以控制跳转、回退等。

```
import {useRoute, useRouter} from "vue-router";

const router = useRouter();

// 字符串路径
router.push('/users/eduardo')

// 带有路径的对象
router.push({ path: '/users/eduardo' })

// 命名的路由，并加上参数，让路由建立 url
router.push({ name: 'user', params: { username: 'eduardo' } })

// 带查询参数，结果是 /register?plan=private
router.push({ path: '/register', query: { plan: 'private' } })

// 带 hash，结果是 /about#team
router.push({ path: '/about', hash: '#team' })

//注意： `params` 不能与 `path` 一起使用
router.push({ path: '/user', params: { username } }) //错误用法 -> /user
```

## 路由传参⭐

### query参数

1. 传递参数

```
<!-- 跳转并携带query参数（to的字符串写法） -->
<router-link to="/news/detail?a=1&b=2&content=欢迎你">
    跳转
</router-link>

                
<!-- 跳转并携带query参数（to的对象写法） -->
<RouterLink 
  :to="{
    //name:'xiang', //用name也可以跳转
    path:'/news/detail',
    query:{
      id:news.id,
      title:news.title,
      content:news.content
    }
  }"
>
  {{news.title}}
</RouterLink>
```

2. 接收参数：

```
import {useRoute} from 'vue-router'
const route = useRoute()
// 打印query参数
console.log(route.query)
```

### params参数

1. 传递参数

```
<!-- 跳转并携带params参数（to的字符串写法） -->
<RouterLink :to="`/news/detail/001/新闻001/内容001`">{{news.title}}</RouterLink>

                
<!-- 跳转并携带params参数（to的对象写法） -->
<RouterLink 
  :to="{
    name:'xiang', //用name跳转
    params:{
      id:news.id,
      title:news.title,
      content:news.title
    }
  }"
>
  {{news.title}}
</RouterLink>
```

2. 接收参数：

```
import {useRoute} from 'vue-router'
const route = useRoute()
// 打印params参数
console.log(route.params)
```

备注1：传递`params`参数时，若使用`to`的对象写法，必须使用`name`配置项，不能用`path`。

备注2：传递`params`参数时，需要提前在规则中占位。

## 【 replace属性】

1. 作用：控制路由跳转时操作浏览器历史记录的模式。

2. 浏览器的历史记录有两种写入方式：分别为` ``push`` `和` ``replace`` `：

- ` ``push`` `是追加历史记录（默认值）。

- `replace`是替换当前记录。

3. 开启`replace`模式：

```
<RouterLink replace .......>News</RouterLink>
```

## 导航守卫

我们只演示全局前置守卫。后置钩子等内容参照官方文档

常用场景，没有登录跳转到登录页，控制跳转逻辑

```
import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/AboutView.vue')
        },
        {
            path: '/user/:name',
            name: 'User',
            component: () => import('@/views/user/UserInfo.vue'),
            children: [
                {
                    path: 'profile',
                    component: () => import('@/views/user/Profile.vue')
                },
                {
                    path: 'posts',
                    component: () => import('@/views/user/Posts.vue')
                }
            ]
        }
    ]
})


//导航守卫 每次跳转时
router.beforeEach(async (to, from) => {
    console.log("守卫：to：", to)
    console.log("守卫：from：", from)
    if (to.fullPath === '/about') {
       return "/"
    }
})

export default router
```

## 主页布局

借助 antdv 的 layout 组件，可以实现主页【上】【左】【右】布局

```
<template>
  <div class="a53">
    <a-layout>
      <a-layout-header></a-layout-header>

      <a-layout>
        <a-layout-sider></a-layout-sider>

        <a-layout-content>
          <router-view></router-view>

        </a-layout-content>

      </a-layout>

    </a-layout>

  </div>

</template>

<style scoped>
.a53 {
  height: 100%;
  background-color: rgb(220, 225, 255);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='35' y='10' font-size='14' font-family='system-ui, sans-serif' text-anchor='middle' dominant-baseline='middle'%3EA53(主页)%3C/text%3E%3C/svg%3E");
  padding: 20px;
  box-sizing: border-box;
}
.ant-layout-header {
  height: 50px;
  background-color:darkseagreen;
}

.ant-layout-sider {
  background-color:lightsalmon;
}

.ant-layout-content {
  background-color: aliceblue;
}

.ant-layout-footer {
  background-color:darkslateblue;
  height: 30px;
}

.ant-layout {
  height: 100%;
}

.ant-layout-has-sider {
  height: calc(100% - 50px);
}
</style>
```

## 侧边栏菜单

```
<template>
  <div class="a53">
    <a-layout>
      <a-layout-header></a-layout-header>

      <a-layout>
        <a-layout-sider>
          <a-menu theme="dark" mode="inline">
            <a-menu-item :key="1">
                
              <router-link to="/a3/student">菜单1</router-link>

                
            </a-menu-item>

            <a-menu-item :key="2">
              <router-link to="/a3/teacher">菜单2</router-link>

            </a-menu-item>

            <a-menu-item :key="3">菜单3</a-menu-item>

            <a-sub-menu :key="4" title="菜单4">
              <a-menu-item :key="41">菜单41</a-menu-item>

              <a-menu-item :key="42">菜单42</a-menu-item>

            </a-sub-menu>

          </a-menu>

        </a-layout-sider>

        <a-layout-content>
          <router-view></router-view>

        </a-layout-content>

      </a-layout>

    </a-layout>

  </div>

</template>
```

- a-menu-item 与 a-sub-menu 都必须为 key 属性唯一赋值，否则会产生混乱

- router-link 标签用来切换路由，to 是目标路由的路径

- theme 属性定义菜单的主题（默认亮色主题，dark 为暗色主题）

- mode 属性定义子菜单的展示模式（默认弹出，inline 显示在下方）

## 菜单图标

安装图标依赖

```
npm install @ant-design/icons-vue
```

菜单中使用图标

```
<template>
  <div class="a53">
    <a-layout>
      <a-layout-header></a-layout-header>

      <a-layout>
        <a-layout-sider>
          <a-menu theme="dark" mode="inline">
            <a-menu-item :key="1">
              <template #icon>
                <highlight-outlined />
              </template>

              <router-link to="/a3/student">菜单1</router-link>

            </a-menu-item>

            <a-menu-item :key="2">
              <template #icon>
                <align-center-outlined />
              </template>

              <router-link to="/a3/teacher">菜单2</router-link>

            </a-menu-item>

            <a-menu-item :key="3">
              <template #icon>
                <strikethrough-outlined />
              </template>

              菜单3</a-menu-item>

            <a-sub-menu :key="4" title="菜单4">
              <template #icon>
                <sort-descending-outlined />
              </template>

              <a-menu-item :key="41">菜单41</a-menu-item>

              <a-menu-item :key="42">菜单42</a-menu-item>

            </a-sub-menu>

          </a-menu>

        </a-layout-sider>

        <a-layout-content>
          <router-view></router-view>

        </a-layout-content>

      </a-layout>

    </a-layout>

  </div>

</template>

<script setup lang="ts">
import {HighlightOutlined, AlignCenterOutlined, StrikethroughOutlined, SortDescendingOutlined} from '@ant-design/icons-vue'
</script>
```

- 图标组件没有全局绑定，需要 import 之后才能使用

- 用 `<template #icon></template>` 插槽，才能确定图标展示的位置（菜单文字之前）

## 二次封装图标组件

最终希望用统一的图标组件去使用图标，图标名只是作为一个属性值传递进去，例如：

使用者

```
<template>
  <a-icon icon="highlight-outlined"></a-icon>

  <a-icon icon="align-center-outlined"></a-icon>

  <a-icon icon="strikethrough-outlined"></a-icon>

  <a-icon icon="sort-descending-outlined"></a-icon>

</template>

<script setup lang="ts">
import AIcon from '../components/AIcon1.vue'
</script>
```

### 方法1，使用 vue 组件

```
<script lang="ts" setup>
import {HighlightOutlined, AlignCenterOutlined, StrikethroughOutlined, SortDescendingOutlined} from '@ant-design/icons-vue'
const props = defineProps<{icon:string}>()
</script>

<template>
  <highlight-outlined v-if="icon==='highlight-outlined'"></highlight-outlined>

  <align-center-outlined v-else-if="icon==='align-center-outlined'"></align-center-outlined>

  <strikethrough-outlined v-else-if="icon==='strikethrough-outlined'"></strikethrough-outlined>

  <sort-descending-outlined v-else-if="icon==='sort-descending-outlined'"></sort-descending-outlined>

</template>
```

- 缺点：实现太笨

### 方法2，使用函数式组件

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444618458-5fd02ca3-75c6-45b5-b253-80f9027266a7.png "null")

```
import { h } from "vue"
import * as Icons from '@ant-design/icons-vue'

interface Module {
  [p:string]: any
}

// 参数1: 组件属性
const AIcon = (props:{icon:string}) => {
  // console.log(props.icon)
  // console.log(Icons)
  // 参数1: 组件对象
  const im: Module = Icons
  return h(im[toCamelCase(props.icon)])
}

export default AIcon

// 将-分隔的单词转换为大驼峰命名的单词
function toCamelCase(str: string) { // highlight-outlined
  return str.split('-') // ['highlight', 'outlined']
    .map((e)=> e.charAt(0).toUpperCase() + e.slice(1) ) // ['Highlight', 'Outlined']
    .join('')
}
/*
Icons 的结构如下
{
  HighlightOutlined: HighlightOutlined组件对象,
  MonitorOutlined: MonitorOutlined组件对象,
  ...
}
*/
```

- 需要动态生成标签的时候，可以考虑使用函数式组件

### 方法3，使用 jsx 组件

首先，安装

```
npm install @vitejs/plugin-vue-jsx -D
```

配置 vite.config.ts

```
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx()]
})
```

编写一个 Hi.tsx 组件

```
export default {
  props: {
    msg: String
  },
  setup(props: { msg: string }) {
    return () => <h5>{props.msg}</h5>

  }
}
```

然后被其它组件使用

```
<script setup lang="ts">
import Hi from '../components/Hi'
</script>

<template>
  <Hi msg="Hello,World"></Hi>

</template>
```

用 jsx 实现图标组件

```
import * as Icons from '@ant-design/icons-vue'

interface Module {
  [p:string]: any
}

function toCamelCase(str: string) { // highlight-outlined
  return str
    .split("-") // ['highlight', 'outlined']
    .map((e) => e.charAt(0).toUpperCase() + e.slice(1)) // ['Highlight', 'Outlined']
    .join(""); // HighlightOutlined
}

export default {
  props: {
    icon: String
  },
  setup(props: {icon: string}) {
    const im: Module = Icons
    const tag = im[toCamelCase(props.icon)] // 图标组件
    // HighlightOutlined
    return ()=> <tag></tag> // 返回组件标签
  }
}
```

## 动态路由与菜单⭐

### 路由文件

a6router.js

```
import { createRouter, createWebHashHistory } from 'vue-router'
import { useStorage } from '@vueuse/core'
import { Route, Menu } from '../model/Model8080'
const clientRoutes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/A6Login.vue')
  },
  {
    path: '/404',
    name: '404',
    component: () => import('../views/A6NotFound.vue')
  },
  {
    path: '/',
    name: 'main',
    component: () => import('../views/A6Main.vue')
  },
  {
    path: '/:pathMatcher(.*)*',
    name: 'remaining',
    redirect: '/404'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes: clientRoutes
})

export const serverMenus = useStorage<Menu[]>('serverMenus', [])
const serverRoutes = useStorage<Route[]>('serverRoutes', [])
addServerRoutes(serverRoutes.value)

export function addServerRoutes(routeList: Route[]) {
  for (const r of routeList) {
    if (r.parentName) {
      router.addRoute(r.parentName, {
        path: r.path,
        component: () => import(r.component),
        name: r.name
      })
    }
  }
  serverRoutes.value = routeList
}

export function resetRoutes() {
  for (const r of clientRoutes) {
    router.addRoute(r)
  }
  serverRoutes.value = null
  serverMenus.value = null
}

export default router
```

本文件重要的函数及变量

- addServerRoutes 函数向路由表中添加由服务器提供的路由，路由分成两部分

- clientRoutes 这是客户端固定的路由

- serverRoutes 这是服务器变化的路由，存储于 localStorage

- resetRoutes 函数用来将路由重置为 clientRoutes

- vue-router@4 中的 addRoute 方法会【覆盖】同名路由，这是这种实现的关键

- 因此，服务器返回的路由最好是 main 的子路由，这样重置时就会比较简单，用之前的 main 一覆盖就完事了

- serverMenus 变量记录服务器变化的菜单，存储于 localStorage

### 登录组件

动态路由应当在登录时生成，A6Login.vue

```
<template>
  <div class="login">
    <a-form :label-col="{ span: 6 }" autocomplete="off">
      <a-form-item label="用户名" v-bind="validateInfos.username">
        <a-input v-model:value="dto.username" />
      </a-form-item>

      <a-form-item label="密码" v-bind="validateInfos.password">
        <a-input-password v-model:value="dto.password" />
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 6, span: 16 }">
        <a-button type="primary" @click="onClick">Submit</a-button>

      </a-form-item>      
    </a-form>

  </div>

</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Form } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import axios from '../api/request'
import { useRequest } from 'vue-request'
import { AxiosRespToken, LoginDto, AxiosRespMenuAndRoute } from '../model/Model8080'
import { resetRoutes, addServerRoutes, serverMenus } from '../router/a6router'
const dto = ref({username:'', password:''})
const rules = ref({
  username: [
    {required: true, message:'用户名必填'}
  ],
  password:[
    {required: true, message:'密码必填'}
  ]
})
const { validateInfos, validate } = Form.useForm(dto, rules)
const router = useRouter()
const { runAsync:login } = useRequest<AxiosRespToken, LoginDto[]>((dto)=> axios.post('/api/loginJwt', dto), {manual:true})
const { runAsync:menu } = useRequest<AxiosRespMenuAndRoute, string[]>((username)=> axios.get(`/api/menu/${username}`), {manual:true})
async function onClick() {
  try {
    await validate()
    const loginResp = await login(dto.value
    if(loginResp.data.code === 200) { // 登录成功
      const token = loginResp.data.data.token
      const menuResp = await menu(dto.value.username)
      const routeList = menuResp.data.data.routeList
      addServerRoutes(routeList)
      serverMenus.value = menuResp.data.data.menuTree
      router.push('/')
    })
  } catch (e) {
    console.error(e)
  }
}
onMounted(()=>{
  resetRoutes()
})
</script>

<style scoped>
.login{
  margin: 200px auto;
  width: 25%;
  padding: 20px;
  height: 180px;
  background-color: antiquewhite;
}
</style>
```

- 登录成功后去请求 `/api/menu/{username}` 获取该用户的菜单和路由

- router.push 方法用来以编程方式跳转至主页路由

### 主页组件

A6Main.vue

```
<template>
  <div class="a6main">
    <a-layout>
      <a-layout-header>
      </a-layout-header>

      <a-layout>
        <a-layout-sider>
          <a-menu mode="inline" theme="dark">
            <template v-for="m1 of serverMenus">
              <a-sub-menu v-if="m1.children" :key="m1.id" :title="m1.title">
                <template #icon><a-icon :icon="m1.icon"></a-icon></template>

                <a-menu-item v-for="m2 of m1.children" :key="m2.id">
                  <template #icon><a-icon :icon="m2.icon"></a-icon></template>

                  <router-link v-if="m2.routePath" :to="m2.routePath">{{m2.title}}</router-link>

                  <span v-else>{{m2.title}}</span>

                </a-menu-item>

              </a-sub-menu>

              <a-menu-item v-else :key="m1.id">
                <template #icon><a-icon :icon="m1.icon"></a-icon></template>

                <router-link v-if="m1.routePath" :to="m1.routePath">{{m1.title}}</router-link>

                <span v-else>{{m1.title}}</span>

              </a-menu-item>

            </template>            
          </a-menu>

        </a-layout-sider>

        <a-layout-content>
          <router-view></router-view>

        </a-layout-content>

      </a-layout>

    </a-layout>

  </div>

</template>

<script setup lang="ts">
import AIcon from '../components/AIcon3' // jsx icon 组件
import { serverMenus } from '../router/a6router'
</script>

<style scoped>
.a6main {
  height: 100%;
  background-color: rgb(220, 225, 255);
  box-sizing: border-box;
}
.ant-layout-header {
  height: 50px;
  background-color:darkseagreen;
}

.ant-layout-sider {
  background-color:lightsalmon;
}

.ant-layout-content {
  background-color: aliceblue;
}

.ant-layout-footer {
  background-color:darkslateblue;
  height: 30px;
}

.ant-layout {
  height: 100%;
}

.ant-layout-has-sider {
  height: calc(100% - 50px);
}

</style>
```

## token 使用

1. 获取用户信息，例如服务器端可以把用户名、该用户的路由、菜单信息都统一从 token 返回

2. 前端路由跳转依据，例如跳转前检查 token，如果不存在，表示未登录，就避免跳转至某些路由

3. 后端 api 访问依据，例如每次发请求携带 token，后端需要身份校验的 api 需要用到