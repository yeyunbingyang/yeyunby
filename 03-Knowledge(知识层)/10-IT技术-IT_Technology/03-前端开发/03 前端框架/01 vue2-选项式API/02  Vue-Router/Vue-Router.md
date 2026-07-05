# 路由入门

## 单页应用程序介绍

### 1.概念

单页应用程序：SPA【Single Page Application】是指所有的功能都在**一个html页面**上实现

### 2.具体示例

单页应用网站： 网易云音乐 [https://music.163.com/](https://music.163.com/)

多页应用网站：京东 [https://jd.com/](https://jd.com/)

### 3.单页应用 VS 多页面应用

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128459-7ececbbc-a75b-4c6e-aecd-f908132cfd63.png "null")

单页应用类网站：系统类网站 / 内部网站 / 文档类网站 / 移动端站点

多页应用类网站：公司官网 / 电商类网站

### 4.总结

1.什么是单页面应用程序?

2.单页面应用优缺点?

3.单页应用场景？

## 路由介绍

### 1.思考

单页面应用程序，之所以开发效率高，性能好，用户体验好

最大的原因就是：**页面按需更新**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128528-a2656cd7-5c95-4c38-8083-3cfc7ad575ba.png "null")

比如当点击【发现音乐】和【关注】时，**只是更新下面部分内容**，对于头部是不更新的

要按需更新，首先就需要明确：**访问路径**和 **组件**的对应关系！

访问路径 和 组件的对应关系如何确定呢？ **路由**

### 2.路由的介绍

生活中的路由：设备和ip的映射关系

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128597-650c5eab-dbc0-427d-956f-f97d63682b1a.png "null")

Vue中的路由：**路径和组件**的**映射**关系

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128750-801fd126-540f-432e-83b3-0bc483fac50d.png "null")

### 3.总结

- 什么是路由
- Vue中的路由是什么

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128827-f98030f5-bc2c-4bc4-9ff4-9649cd3ce75c.png "null")

## 路由的基本使用

### 1.目标

认识插件 VueRouter，掌握 VueRouter 的基本使用步骤

### 2.作用

**修改**地址栏路径时，**切换显示**匹配的**组件**

### 3.说明

Vue 官方的一个路由插件，是一个第三方包

### 4.官网

[https://v3.router.vuejs.org/zh/](https://v3.router.vuejs.org/zh/)

### 5.VueRouter的使用（5+2）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128916-80e666b1-77e7-48c7-82ed-5df138c7bd94.png "null")

固定5个固定的步骤（不用死背，熟能生巧）

1. 下载 VueRouter 模块到当前工程，版本3.6.5
2. ![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944128986-edd8ccb2-2335-4b87-a341-dfebaf1b6dfc.png "null")

```
yarn add vue-router@3.6.5
```

3. main.js中引入VueRouter

```
import VueRouter from 'vue-router'
```

4. 安装注册

```
Vue.use(VueRouter)
```

5. 创建路由对象

```
const router = new VueRouter()
```

6. 注入，将路由对象注入到new Vue实例中，建立关联

```
new Vue({
  render: h => h(App),
  router:router
}).$mount('#app')
```

当我们配置完以上5步之后 就可以看到浏览器地址栏中的路由 变成了 /#/的形式。表示项目的路由已经被Vue-Router管理了

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944129060-a72a61c4-a65b-4562-906d-5cdc8629bb40.png "null")

### 6.代码示例

main.js

```
// 路由的使用步骤 5 + 2
// 5个基础步骤
// 1. 下载 v3.6.5
// yarn add vue-router@3.6.5
// 2. 引入
// 3. 安装注册 Vue.use(Vue插件)
// 4. 创建路由对象
// 5. 注入到new Vue中，建立关联


import VueRouter from 'vue-router'
Vue.use(VueRouter) // VueRouter插件初始化

const router = new VueRouter()

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
```

### 7.两个核心步骤

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944129126-30a55fbc-f5e6-4511-b14f-8ab6f71cd44a.png "null")

1. 创建需要的组件 (views目录)，配置路由规则![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944129205-1f1e5f41-2f2a-46fa-a574-e7637cb393f4.png "null")
2. 配置导航，配置路由出口(路径匹配的组件显示的位置)

App.vue

```
<div class="footer_wrap">
  <a href="#/find">发现音乐</a>

  <a href="#/my">我的音乐</a>

  <a href="#/friend">朋友</a>

</div>

<div class="top">
  <router-view></router-view>

</div>
```

### 8.总结

1. 如何实现 路径改变，对应组件 切换,应该使用哪个插件?
2. Vue-Router的使用步骤是什么(5+2)?

## 组件的存放目录问题

注意： **.vue文件** 本质无区别

### 1.组件分类

.vue文件分为2类，都是 **.vue文件（本质无区别）**

- 页面组件 （配置路由规则时使用的组件）
- 复用组件（多个组件中都使用到的组件）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944129279-6da1e48d-891f-455f-8ab2-c32fb27e5a46.png "null")

### 2.存放目录

分类开来的目的就是为了 **更易维护**

1. src/views文件夹页面组件 - 页面展示 - 配合路由用
2. src/components文件夹复用组件 - 展示数据 - 常用于复用

### 3.总结

- 组件分类有哪两类？分类的目的？
- 不同分类的组件应该放在什么文件夹？作用分别是什么？

## 路由的封装抽离

问题：所有的路由配置都在main.js中合适吗？

目标：将路由模块抽离出来。 好处：**拆分模块，利于维护**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944129364-3b2d3ec3-8987-4261-9157-41b1f45fed98.png "null")

路径简写：

**脚手架环境下** @指代src目录，可以用于快速引入组件

总结：

- 路由模块的封装抽离的好处是什么？
- 以后如何快速引入组件？

# 路由跳转-声明式导航

<router-link to="/c1/p1">P1</router-link>

## 导航链接

### 1.需求

实现导航高亮效果

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131031-11c2029e-84ed-4799-895d-5bc3404a52b7.png "null")

如果使用a标签进行跳转的话，需要给当前跳转的导航加样式，同时要移除上一个a标签的样式，太麻烦！！！

### 2.解决方案

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131146-feee795a-3c2d-4d17-9487-d252d216c137.png "null")

vue-router 提供了一个全局组件 router-link (取代 a 标签)

- **能跳转**，配置 to 属性指定路径(**必须**) 。本质还是 a 标签 ，**to 无需 #**
- **能高亮**，默认就会提供**高亮类名**，可以直接设置高亮样式

语法： 发现音乐

```
  <div>
    <div class="footer_wrap">
      <router-link to="/find">发现音乐</router-link>

      <router-link to="/my">我的音乐</router-link>

      <router-link to="/friend">朋友</router-link>

    </div>

    <div class="top">
      <!-- 路由出口 → 匹配的组件所展示的位置 -->
      <router-view></router-view>

    </div>

  </div>
```

### 3.通过router-link自带的两个样式进行高亮

使用router-link跳转后，我们发现。当前点击的链接默认加了两个class的值 `router-link-exact-active`和`router-link-active`

我们可以给任意一个class属性添加高亮样式即可实现功能

### 4.总结

- router-link是什么？
- router-link怎么用？
- router-link的好处是什么？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131232-7515ac20-2198-449c-b70e-e9e16ae0a344.png "null")

## 两个类名

精确匹配和模糊匹配

当我们使用跳转时，自动给当前导航加了**两个类名**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131306-78d00660-8605-4c95-9a81-44630d192463.png "null")

### 1.router-link-active

**模糊匹配（用的多）**

to="/my" 可以匹配 /my /my/a /my/b ....

只要是以/my开头的路径 都可以和 to="/my"匹配到

### 2.router-link-exact-active

**精确匹配**

to="/my" 仅可以匹配 /my

### 3.在地址栏中输入二级路由查看类名的添加

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131376-9fb68e2c-07cb-4908-8338-f175590d6162.png "null")

### 4.总结

- router-link 会自动给当前导航添加两个类名，有什么区别呢？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131477-bc6f1776-6b03-491a-9602-1bb489318f59.png "null")

## 自定义类名（了解）

### 1.问题

router-link的**两个高亮类名 太长了**，我们希望能定制怎么办

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131573-dd088b8a-0353-44fd-a00a-3813e9846e82.png "null")

### 2.解决方案

我们可以在创建路由对象时，额外配置两个配置项即可。 `linkActiveClass`和`linkExactActiveClass`

```
const router = new VueRouter({
  routes: [...],
  linkActiveClass: "类名1",
  linkExactActiveClass: "类名2"
})
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131659-9c7a23f1-4691-4897-a436-2c741e278d98.png "null")

### 3.代码演示

```
// 创建了一个路由对象
const router = new VueRouter({
  routes: [
    ...
  ], 
  linkActiveClass: 'active', // 配置模糊匹配的类名
  linkExactActiveClass: 'exact-active' // 配置精确匹配的类名
})
```

### 4.总结

如何自定义router-link的两个**高亮类名**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131738-02ba0dd6-2e52-4667-b21b-7e68e7232882.png "null")

## 查询参数传参

### 1.目标

在跳转路由时，进行传参

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131807-a9c4772f-5acd-462a-8e50-e25e18ab4ef0.png "null")

比如：现在我们在搜索页点击了热门搜索链接，跳转到详情页，**需要把点击的内容带到详情页**，改怎么办呢？

### 2.跳转传参

我们可以通过两种方式，在跳转的时候把所需要的参数传到其他页面中

- 查询参数传参
- 动态路由传参

### 3.查询参数传参

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131882-a6f4e0fa-12ee-4e2e-8c81-406bc6ab9f15.png "null")

- 如何传参？
- 如何接受参数固定用法：$router.query.参数名

### 4.代码演示

App.vue

```
<template>
  <div id="app">
    <div class="link">
      <router-link to="/home">首页</router-link>

      <router-link to="/search">搜索页</router-link>

    </div>

    <router-view></router-view>

  </div>

</template>

<script>
export default {};
</script>

<style scoped>
.link {
  height: 50px;
  line-height: 50px;
  background-color: #495150;
  display: flex;
  margin: -8px -8px 0 -8px;
  margin-bottom: 50px;
}
.link a {
  display: block;
  text-decoration: none;
  background-color: #ad2a26;
  width: 100px;
  text-align: center;
  margin-right: 5px;
  color: #fff;
  border-radius: 5px;
}
</style>
```

Home.vue

```
<template>
  <div class="home">
    <div class="logo-box"></div>

    <div class="search-box">
      <input type="text">
      <button>搜索一下</button>

    </div>

    <div class="hot-link">
      热门搜索：
      <router-link to="/search?key=黑马程序员">黑马程序员</router-link>

      <router-link to="/search?key=前端培训">前端培训</router-link>

      <router-link to="/search?key=如何成为前端大牛">如何成为前端大牛</router-link>

    </div>

  </div>

</template>

<script>
export default {
  name: 'FindMusic'
}
</script>

<style>
.logo-box {
  height: 150px;
  background: url('@/assets/logo.jpeg') no-repeat center;
}
.search-box {
  display: flex;
  justify-content: center;
}
.search-box input {
  width: 400px;
  height: 30px;
  line-height: 30px;
  border: 2px solid #c4c7ce;
  border-radius: 4px 0 0 4px;
  outline: none;
}
.search-box input:focus {
  border: 2px solid #ad2a26;
}
.search-box button {
  width: 100px;
  height: 36px;
  border: none;
  background-color: #ad2a26;
  color: #fff;
  position: relative;
  left: -2px;
  border-radius: 0 4px 4px 0;
}
.hot-link {
  width: 508px;
  height: 60px;
  line-height: 60px;
  margin: 0 auto;
}
.hot-link a {
  margin: 0 5px;
}
</style>
```

Search.vue

```
<template>
  <div class="search">
    <p>搜索关键字: {{ $route.query.key }} </p>

    <p>搜索结果: </p>

    <ul>
      <li>.............</li>

      <li>.............</li>

      <li>.............</li>

      <li>.............</li>

    </ul>

  </div>

</template>

<script>
export default {
  name: 'MyFriend',
  created () {
    // 在created中，获取路由参数
    // this.$route.query.参数名 获取
    console.log(this.$route.query.key);
  }
}
</script>

<style>
.search {
  width: 400px;
  height: 240px;
  padding: 0 20px;
  margin: 0 auto;
  border: 2px solid #c4c7ce;
  border-radius: 5px;
}
</style>
```

router/index.js

```
import Home from '@/views/Home'
import Search from '@/views/Search'
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter) // VueRouter插件初始化

// 创建了一个路由对象
const router = new VueRouter({
  routes: [
    { path: '/home', component: Home },
    { path: '/search', component: Search }
  ]
})

export default router
```

main.js

```
...
import router from './router/index'
...
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
```

## 动态路由传参

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944131976-7edd3fbb-4037-4d5a-8e0d-ecd6d3711da9.png "null")

### 1.动态路由传参方式

- 配置动态路由

动态路由后面的参数可以随便起名，但要有语义

```
const router = new VueRouter({
  routes: [
    ...,
    { 
      path: '/search/:words', 
      component: Search 
    }
  ]
})
```

- 配置导航链接to="/path/参数值"
- 对应页面组件**接受参数**$route.**params**.参数名

params后面的参数名要和动态路由配置的参数保持一致

### 2.查询参数传参 VS 动态路由传参

1. 查询参数传参 (比较适合传**多个参数**)
2. 跳转：to="/path?参数名=值&参数名2=值"
3. 获取：$route.query.参数名
4. 动态路由传参 (**优雅简洁**，传单个参数比较方便)

注意：动态路由也可以传多个参数，但一般只传一个

1. 配置动态路由：path: "/path/:参数名"
2. 跳转：to="/path/参数值"
3. 获取：$route.params.参数名

### 3.总结

声明式导航跳转时, 有几种方式传值给路由页面？

- 查询参数传参（多个参数）
- 动态路由传参（一个参数，优雅简洁）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132132-0f70003d-3b2c-4c1f-8b2c-c18d7501bcbf.png "null")

## 动态路由参数的可选符(了解)

### 1.问题

配了路由 path:"/search/:words" 为什么按下面步骤操作，会未匹配到组件，显示空白？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132254-c2bf8d53-3aee-4a5e-ba9a-71e9fe5e5343.png "null")

### 2.原因

/search/:words 表示，**必须要传参数**。如果不传参数，也希望匹配，可以加个可选符"？"

```
const router = new VueRouter({
  routes: [
     ...
    { path: '/search/:words?', component: Search }
  ]
})
```

# 路由跳转-编程式导航

## 两种路由跳转方式

### 1.问题

点击按钮跳转如何实现？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132402-5f72c62e-98d4-44bf-94be-405ade503bb7.png "null")

### 2.方案

编程式导航：用JS代码来进行跳转

### 3.语法

两种语法：

- path 路径跳转 （简易方便）
- name 命名路由跳转 (适合 path 路径长的场景)

### 4.path路径跳转语法

特点：简易方便

```
//简单写法
this.$router.push('路由路径')

//完整写法
this.$router.push({
  path: '路由路径'
})
```

### 5.代码演示 path跳转方式

```
<template>
  <div class="home">
    <div class="logo-box"></div>

    <div class="search-box">
      <input type="text">
        <button @click="goSearch">搜索一下</button>

      </div>

    <div class="hot-link">
      热门搜索：
      <router-link to="/search/黑马程序员">黑马程序员</router-link>

      <router-link to="/search/前端培训">前端培训</router-link>

      <router-link to="/search/如何成为前端大牛">如何成为前端大牛</router-link>

    </div>

  </div>

</template>

<script>
  export default {
    name: 'FindMusic',
    methods: {
      goSearch () {
        // 1. 通过路径的方式跳转
        // (1) this.$router.push('路由路径') [简写]
        // this.$router.push('/search')

        // (2) this.$router.push({     [完整写法]
        //         path: '路由路径' 
        //     })
        // this.$router.push({
        //   path: '/search'
        // })

        // 2. 通过命名路由的方式跳转 (需要给路由起名字) 适合长路径
        //    this.$router.push({
        //        name: '路由名'
        //    })
        this.$router.push({
          name: 'search'
        })
      }
    }
  }
</script>

<style>
  .logo-box {
    height: 150px;
    background: url('@/assets/logo.jpeg') no-repeat center;
  }
  .search-box {
    display: flex;
    justify-content: center;
  }
  .search-box input {
    width: 400px;
    height: 30px;
    line-height: 30px;
    border: 2px solid #c4c7ce;
    border-radius: 4px 0 0 4px;
    outline: none;
  }
  .search-box input:focus {
    border: 2px solid #ad2a26;
  }
  .search-box button {
    width: 100px;
    height: 36px;
    border: none;
    background-color: #ad2a26;
    color: #fff;
    position: relative;
    left: -2px;
    border-radius: 0 4px 4px 0;
  }
  .hot-link {
    width: 508px;
    height: 60px;
    line-height: 60px;
    margin: 0 auto;
  }
  .hot-link a {
    margin: 0 5px;
  }
</style>
```

### 6.name命名路由跳转

特点：适合 path 路径长的场景

语法：

- 路由规则，必须配置name配置项

```
{ name: '路由名', path: '/path/xxx', component: XXX },
```

- 通过name来进行跳转

```
this.$router.push({
  name: '路由名'
})
```

### 7.代码演示通过name命名路由跳转

```
<template>
  <div class="home">
    <div class="logo-box"></div>

    <div class="search-box">
      <input type="text">
      <button @click="goSearch">搜索一下</button>

    </div>

    <div class="hot-link">
      热门搜索：
      <router-link to="/search/黑马程序员">黑马程序员</router-link>

      <router-link to="/search/前端培训">前端培训</router-link>

      <router-link to="/search/如何成为前端大牛">如何成为前端大牛</router-link>

    </div>

  </div>

</template>

<script>
export default {
  name: 'FindMusic',
  methods: {
    goSearch () {
      // 1. 通过路径的方式跳转
      // (1) this.$router.push('路由路径') [简写]
      // this.$router.push('/search')

      // (2) this.$router.push({     [完整写法]
      //         path: '路由路径' 
      //     })
      // this.$router.push({
      //   path: '/search'
      // })

      // 2. 通过命名路由的方式跳转 (需要给路由起名字) 适合长路径
      //    this.$router.push({
      //        name: '路由名'
      //    })
      this.$router.push({
        name: 'search'
      })
    }
  }
}
</script>

<style>
.logo-box {
  height: 150px;
  background: url('@/assets/logo.jpeg') no-repeat center;
}
.search-box {
  display: flex;
  justify-content: center;
}
.search-box input {
  width: 400px;
  height: 30px;
  line-height: 30px;
  border: 2px solid #c4c7ce;
  border-radius: 4px 0 0 4px;
  outline: none;
}
.search-box input:focus {
  border: 2px solid #ad2a26;
}
.search-box button {
  width: 100px;
  height: 36px;
  border: none;
  background-color: #ad2a26;
  color: #fff;
  position: relative;
  left: -2px;
  border-radius: 0 4px 4px 0;
}
.hot-link {
  width: 508px;
  height: 60px;
  line-height: 60px;
  margin: 0 auto;
}
.hot-link a {
  margin: 0 5px;
}
</style>
```

### 8.总结

编程式导航有几种跳转方式？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132469-d8cdb423-5cd3-4aa8-a71c-38dedd892f59.png "null")

## path路径跳转传参【路由传参】

### 1.问题

点击搜索按钮，跳转需要把文本框中输入的内容传到下一个页面如何实现？

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132541-cf3c9639-d504-4131-9c16-5ad026c65eea.png "null")

### 2.两种传参方式

1.查询参数

2.动态路由传参

### 3.传参

两种跳转方式，对于两种传参方式都支持：

① path 路径跳转传参

② name 命名路由跳转传参

### 4.path路径跳转传参（query传参）

```
//简单写法
this.$router.push('/路径?参数名1=参数值1&参数2=参数值2')

//完整写法
this.$router.push({
  path: '/路径',
  query: {
    参数名1: '参数值1',
    参数名2: '参数值2'
  }
})
```

接受参数的方式依然是：$route.query.参数名

### 5.path路径跳转传参（动态路由传参）

```
//简单写法
this.$router.push('/路径/参数值')

//完整写法
this.$router.push({
  path: '/路径/参数值'
})

this.$router.push({
  path: `/search/${this.inpValue}`
})
```

接受参数的方式依然是：$route.params.参数值

**注意：**path不能配合params使用

## name命名路由传参

### 1.name 命名路由跳转传参 (query传参)

```
this.$router.push({
  name: '路由名字',
  query: {
    参数名1: '参数值1',
    参数名2: '参数值2'
  }
})
```

### 2.name 命名路由跳转传参 (动态路由传参)

```
this.$router.push({
  name: '路由名字',
  params: {
    参数名: '参数值',
  }
})
```

### 3.总结

编程式导航，如何跳转传参？

1.path路径跳转

- query传参

```
this.$router.push('/路径?参数名1=参数值1&参数2=参数值2')
this.$router.push({
  path: '/路径',
  query: {
    参数名1: '参数值1',
    参数名2: '参数值2'
  }
})
```

- 动态路由传参

```
this.$router.push('/路径/参数值')
this.$router.push({
  path: '/路径/参数值'
})
```

2.name命名路由跳转

- query传参

```
this.$router.push({
  name: '路由名字',
  query: {
    参数名1: '参数值1',
    参数名2: '参数值2'
  }
})
```

- 动态路由传参 (需要配动态路由)

```
this.$router.push({
  name: '路由名字',
  params: {
    参数名: '参数值',
  }
})
```

# 路由跳转 - 导航菜单

```
<el-menu router background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
    <el-submenu index="/c1">
        <span slot="title">
            <i class="el-icon-platform-eleme"></i>

            菜单1
        </span>

        <el-menu-item index="/c1/p1">子项1</el-menu-item>

        <el-menu-item index="/c1/p2">子项2</el-menu-item>

        <el-menu-item index="/c1/p3">子项3</el-menu-item>

    </el-submenu>

    <el-menu-item index="/c2">
        <span slot="title">
            <i class="el-icon-phone"></i>

            菜单2
        </span>

    </el-menu-item>

    <el-menu-item index="/c3">
        <span slot="title">
            <i class="el-icon-star-on"></i>

            菜单3
        </span>

    </el-menu-item>

</el-menu>
```

- 图标和菜单项文字建议用 `<span slot='title'></span>` 包裹起来
- i为图标标签，利用class属性选定图标
- `el-menu` 标签上加上 `router` 属性，表示结合导航菜单与路由对象，此时，就可以利用菜单项的 `index` 属性来路由跳转

# 动态路由与菜单⭐

将菜单、路由信息（仅主页的）存入数据库中（没有视图组件的不进行添加）

```
insert into menu(id, name, pid, path, component, icon) values
    (101, '菜单1', 0,   '/m1',    null,         'el-icon-platform-eleme'),
    (102, '菜单2', 0,   '/m2',    null,         'el-icon-delete-solid'),
    (103, '菜单3', 0,   '/m3',    null,         'el-icon-s-tools'),
    (104, '菜单4', 0,   '/m4',    'M4View.vue', 'el-icon-user-solid'),
    (105, '子项1', 101, '/m1/c1', 'C1View.vue', 'el-icon-s-goods'),
    (106, '子项2', 101, '/m1/c2', 'C2View.vue', 'el-icon-menu'),
    (107, '子项3', 102, '/m2/c3', 'C3View.vue', 'el-icon-s-marketing'),
    (108, '子项4', 102, '/m2/c4', 'C4View.vue', 'el-icon-s-platform'),
    (109, '子项5', 102, '/m2/c5', 'C5View.vue', 'el-icon-picture'),
    (110, '子项6', 103, '/m3/c6', 'C6View.vue', 'el-icon-upload'),
    (111, '子项7', 103, '/m3/c7', 'C7View.vue', 'el-icon-s-promotion');
```

不同的用户查询的的菜单、路由信息是不一样的（根据角色信息返回菜单）

例如：访问 `/api/menu/admin` 返回所有的数据

```
[
    {
        "id": 102,
        "name": "菜单2",
        "icon": "el-icon-delete-solid",
        "path": "/m2",
        "pid": 0,
        "component": null
    },
    {
        "id": 107,
        "name": "子项3",
        "icon": "el-icon-s-marketing",
        "path": "/m2/c3",
        "pid": 102,
        "component": "C3View.vue"
    },
    {
        "id": 108,
        "name": "子项4",
        "icon": "el-icon-s-platform",
        "path": "/m2/c4",
        "pid": 102,
        "component": "C4View.vue"
    },
    {
        "id": 109,
        "name": "子项5",
        "icon": "el-icon-picture",
        "path": "/m2/c5",
        "pid": 102,
        "component": "C5View.vue"
    }
]
```

访问 `/api/menu/wang` 返回

```
[
    {
        "id": 103,
        "name": "菜单3",
        "icon": "el-icon-s-tools",
        "path": "/m3",
        "pid": 0,
        "component": null
    },
    {
        "id": 110,
        "name": "子项6",
        "icon": "el-icon-upload",
        "path": "/m3/c6",
        "pid": 103,
        "component": "C6View.vue"
    },
    {
        "id": 111,
        "name": "子项7",
        "icon": "el-icon-s-promotion",
        "path": "/m3/c7",
        "pid": 103,
        "component": "C7View.vue"
    }
]
```

前端根据他们身份不同，动态添加路由和显示菜单

**路由元信息（meta）**：在路由配置中使用 `meta` 字段存储权限信息，动态过滤路由时根据用户权限决定是否显示。

```
const routes = [
  {
    path: '/admin',
    component: Admin,
    meta: { requiresAuth: true, roles: ['admin'] } // 需要登录且角色为 admin
  },
  {
    path: '/user',
    component: User,
    meta: { requiresAuth: true, roles: ['user', 'admin'] } // 需要登录且角色为 user 或 admin
  }
];
```

## 动态路由

将查询出来的路由信息动态地添加到容器路由

```
export function addServerRoutes(array) {
  for (const { id, path, component } of array) {
    if (component !== null) {
      // 动态添加路由
      // 参数1：父路由名称
      // 参数2：路由信息对象
      router.addRoute('c', {
        path: path,
        name: id,
        component: () => import(`@/views/example15/container/${component}`)
      });
    }
  }
}
```

- js 这边只保留几个固定路由，如主页、404 和 login
- 以上方法执行时，将服务器返回的路由信息加入到名为 c 的父路由中去
- 这里要注意组件路径，前面 @/views 是必须在 js 这边完成拼接的，否则 import 函数会失效

## 重置路由

在用户注销时应当重置路由（恢复到初始路由）

vue2的路由版本中没有删除路由的方法

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739441076226-abe6d11f-1148-48c1-9223-9f4f7e696af2.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739441076281-2924a278-7573-4e0e-b53e-21c26950bda1.png "null")

```
const router = new VueRouter({
  routes
})

export function resetRouter() {
  router.matcher = new VueRouter({ routes }).matcher
}
```

初始路由表赋值给初始路由表

## 页面刷新

页面刷新后，会导致动态添加的路由失效，解决方法是将路由数据存入 sessionStorage

```
<script>
import axios from '@/util/myaxios'
import {resetRouter, addServerRoutes} from '@/router/example15'
const options = {
    data() {
        return {
            username: 'admin'
        }
    },
    methods: {
        async login() {       
            resetRouter(); // 重置路由     
            const resp = await axios.get(`/api/menu/${this.username}`)
            const array = resp.data.data;
            // localStorage     即使浏览器关闭，存储的数据仍在
            // sessionStorage   以标签页为单位，关闭标签页时，数据被清除
            sessionStorage.setItem('serverRoutes', JSON.stringify(array))
            addServerRoutes(array); // 动态添加路由
            this.$router.push('/');
        }
    }
}
export default options;
</script>
```

页面刷新，重新创建路由对象时，从 sessionStorage 里恢复路由数据

```
const router = new VueRouter({
  routes
})

// 从 sessionStorage 中恢复路由数据
const serverRoutes = sessionStorage.getItem('serverRoutes');
if(serverRoutes) {
  const array = JSON.parse(serverRoutes);
  addServerRoutes(array) // 动态添加路由
}
```

## 动态菜单

代码部分

map集合配合俩次循环

```
<script>
const options = {
    mounted() {
        const serverRoutes = sessionStorage.getItem('serverRoutes');
        const array = JSON.parse(serverRoutes);
        const map = new Map(); // 解析存储所有信息
        for(const obj of array) {
            map.set(obj.id, obj);
        }
        const top = []; // 顶层菜单
        for(const obj of array) {
            const parent = map.get(obj.pid);
            if(parent) {
                parent.children ??= [];
                parent.children.push(obj);
            } else { // 没有父级直接为一级
                top.push(obj);
            }
        }
        this.top = top;
    },
    data() {
        return {
            top: []
        }
    }
}
export default options;
</script>
```

菜单部分

```
<el-menu router background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" :unique-opened="true">
    <template v-for="m1 of top">
<el-submenu v-if="m1.children" :key="m1.id" :index="m1.path">
    <span slot="title">
        <i :class="m1.icon"></i> {{m1.name}}
        </span>

    <el-menu-item v-for="m2 of m1.children" :key="m2.id" :index="m2.path">
        <span slot="title">
            <i :class="m2.icon"></i> {{m2.name}}
        </span>

        </el-menu-item>

        </el-submenu>

<el-menu-item v-else :key="m1.id" :index="m1.path">
    <span slot="title">
        <i :class="m1.icon"></i> {{m1.name}}
        </span>

        </el-menu-item>

    </template>

</el-menu>
```

- 没有考虑递归菜单问题，认为菜单只有两级
- :unique-opened="true" （1个菜单展开，其他菜单不展开的效果）同一时刻只能打开一个菜单
- 将submenu也进行跳转绑定，虽然没有跳转，不绑定可能会出现控制台打印错误信息的状态

# 重定向 - redirect

## 1.问题

网页打开时， url 默认是 / 路径，未匹配到组件时，会出现空白

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944132327-51fe82e7-1fbe-4394-b849-137e3e56b315.png "null")

## 2.解决方案

**重定向** → 匹配 / 后, 强制跳转 /home 路径

## 3.语法

```
{ path: 匹配路径, redirect: 重定向到的路径 },
比如：
{ path:'/' ,redirect:'/home' }
```

## 4.代码演示

```
const router = new VueRouter({
  routes: [
    { path: '/', redirect: '/home'},
 	 ...
  ]
})
```

# 404 - path: "*"

## 1.作用

当路径找不到匹配时，给个提示页面

## 2.位置

404的路由，虽然配置在任何一个位置都可以，但一般都**配置在其他路由规则的最后面**

## 3.语法

path: "*" (任意路径) – 前面不匹配就命中最后这个

```
import NotFind from '@/views/NotFind'

const router = new VueRouter({
  routes: [
    ...
    { path: '*', component: NotFind } //最后一个
  ]
})
```

## 4.代码示例

NotFound.vue

```
<template>
  <div>
    <h1>404 Not Found</h1>

  </div>

</template>

<script>
export default {

}
</script>

<style>

</style>
```

router/index.js

```
...
import NotFound from '@/views/NotFound'
...

// 创建了一个路由对象
const router = new VueRouter({
  routes: [
     ...
    { path: '*', component: NotFound }
  ]
})

export default router
```

# 路由模式设置

## 1.问题

路由的路径看起来不自然, 有#，能否切成真正路径形式?

- hash路由(默认) 例如: [http://localhost:8080/#/home](http://localhost:8080/#/home)
- history路由(常用) 例如: [http://localhost:8080/home](http://localhost:8080/home) (以后上线需要服务器端支持，开发环境webpack给规避掉了history模式的问题)

## 2.语法

```
const router = new VueRouter({
    mode:'histroy', //默认是hash
    routes:[]
})
```