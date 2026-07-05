# 面经PC

项目演示: 本地源代码《教学资料》

接口文档: [https://www.apifox.cn/apidoc/project-934563/api-19465917](https://www.apifox.cn/apidoc/project-934563/api-19465917)

**接口根路径**: [http://interview-api-t.itheima.net/](http://interview-api-t.itheima.net/)

本项目的技术栈 本项目技术栈基于 [ES2015+](http://es6.ruanyifeng.com/)、[vue2](https://cn.vuejs.org/index.html)、[vuex3](https://vuex.vuejs.org/zh-cn/)、[vue-router3](https://router.vuejs.org/zh-cn/) 、[vue-cli5](https://github.com/vuejs/vue-cli) 、[axios](https://github.com/axios/axios) 和 [element-ui](https://github.com/ElemeFE/element)

## 一、项目演示及项目收获

### 1.项目演示

根据课程资料中的内容进行项目查看![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146484-73d2d3e8-2355-418e-90e9-ae448d7d81df.png "null")

### 2.项目收获

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146572-900d1498-190a-4094-9d46-b99bfeb750d7.png "null")

## 二、创建项目

### 1.创建项目步骤

```
vue create hm-element-pc
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146633-f95fd0c1-b336-45aa-bc83-56aa24bbc225.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146708-9bb04f81-8d93-4a5c-ab76-5cf19478ca59.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146790-9d7da9dd-7145-440b-946b-68e2cee6c54d.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146852-d7467d00-7d8b-4ff0-a8f6-4161b629fa1a.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146922-29381234-5d0e-4b76-b8da-70e94798aca8.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944146985-a387cb09-9523-4cad-81ac-61b96677b20d.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147070-0e90da25-c0de-4e94-896a-309650c5d9d1.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147130-8c13bfee-a907-4dba-9928-9c6b7e460b9e.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147228-20013bc4-a0fa-4fec-9811-5ef2af4ac236.png "null")

### 2.sass/scss 语法说明

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147327-da4bf10e-32bc-4cf9-b46d-13e8dbd96f33.png "null")

```
less sass stylus 都是 css 预处理器，语法上稍有差异，作用一样
都是让 css，增强能力，具备变量，函数.. 的能力

sass的语法两种语法 .sass(旧) .scss(新)
1 .sass 和 .stylus 语法很像 (了解)
  要求省略 {} 和 分号， 缩进表示嵌套
  
2 .scss 和 .less   语法很像， 都支持嵌套, 变量...
  scss 声明变量：$变量名
  less 声明变量: @变量名
```

## 三、调整项目目录

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147403-691b4bb5-4ef2-40ac-a66b-19b17f0b0199.png "null")

默认生成的目录结构不满足我们的开发需求，所以这里需要做一些自定义改动。主要是两个工作：

- 删除初始化的默认文件

- 修改剩余代码内容

- 新增调整我们需要的目录结构

### 1.删除文件

- components/HelloWorld.vue

- views/HomeView.vue

- views/AboutView.vue

- assets/logo.png

### 2.修改内容

`src/router/index.js`

```
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: []
})

export default router
```

`src/App.vue`

```
<template>
  <div id="app">
    <router-view></router-view>

  </div>

</template>

<style lang="scss">

</style>
```

store/index.js 和 main.js 不用动

### 3.新增需要目录

在 src 目录下中补充创建以下目录：

- /api ： 存储请求函数模块

- /styles: 样式文件模块

- /utils: 工具函数模块

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147494-d17796de-f0e6-40d4-93d2-376c904630db.png "null")

4. 将项目需要的图片资源放置 **assets 文件夹** 中

## 四、引入 element-ui 组件库

官方文档: [https://element.eleme.io/#/zh-CN](https://element.eleme.io/#/zh-CN)

### 1.全部引入

全部引入, 会导入所有的组件， 但是体积会变大

- 安装

```
yarn add element-ui
```

- 在`main.js`中

```
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
```

- 演示

```
<el-button type="primary">主要按钮</el-button>
```

### 2.按需导入 (推荐)

减轻将来打包后的包的体积

- 安装

```
yarn add element-ui
```

- 安装`babel-plugin-component`

```
yarn add babel-plugin-component -D
```

- 在 `babel.config.js` 中配置

```
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  // 新增plugins插件节点,修改完配置文件一定重启项目
  "plugins": [
    [
      "component",
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      }
    ]
  ]
}
```

- 使用插件`main.js`中

```
import { Button } from 'element-ui'
Vue.use(Button)
```

### 3.抽离element.js模块

- 由于组件的导入都书写到了`main.js`中,导致`main.js` 代码冗余将element-ui组件的导入和注册单独抽离到utils文件夹中

- 新建element.js

- **项目中 ** 完整按需导入如下：

```
import Vue from 'vue';
import {
  Popconfirm,
  Avatar,
  Breadcrumb,
  BreadcrumbItem,
  Pagination,
  Dialog,
  Menu,
  Input,
  Option,
  Button,
  Table,
  TableColumn,
  Form,
  FormItem,
  Icon,
  Row,
  Col,
  Card,
  Container,
  Header,
  Aside,
  Main,
  Footer,
  Link,
  Image,
  Loading,
  MessageBox,
  Message,
  Drawer,
  MenuItem
} from 'element-ui';

Vue.use(Breadcrumb);
Vue.use(BreadcrumbItem);
Vue.use(Drawer);
Vue.use(Popconfirm);
Vue.use(Avatar);
Vue.use(Pagination);
Vue.use(Dialog);
Vue.use(Menu);
Vue.use(MenuItem);
Vue.use(Input);
Vue.use(Option);
Vue.use(Button);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Icon);
Vue.use(Row);
Vue.use(Col);
Vue.use(Card);
Vue.use(Container);
Vue.use(Header);
Vue.use(Aside);
Vue.use(Main);
Vue.use(Footer);
Vue.use(Link);
Vue.use(Image);

Vue.use(Loading.directive);

Vue.prototype.$loading = Loading.service;
Vue.prototype.$msgbox = MessageBox;
Vue.prototype.$alert = MessageBox.alert;
Vue.prototype.$confirm = MessageBox.confirm;
Vue.prototype.$prompt = MessageBox.prompt;
Vue.prototype.$notify = Notification;
Vue.prototype.$message = Message;
```

|   |   |   |
|---|---|---|
|类型|示例|用途|
|组件注册|`Vue.use(Button)`|模板中 `<el-button>` 可用|
|指令注册|`Vue.use(Loading.directive)`|使用 `v-loading` 指令 特殊组件和服务|
|服务挂载|`Vue.prototype.$message`|JS 中调用提示/弹窗服务【原型挂载服务类组件、这些组件不能直接 `<el-message>` 用模板调用，而是以 JS 方式调用，需要挂载到 Vue 原型上：】|

```
this.$message.success('操作成功');
this.$confirm('确认删除？').then(...);
this.$loading({ fullscreen: true });
```

- 直接导入main.js中

```
// 直接导入vant-ui.js
import '@/utils/element.js'
```

### 4.主题色定制

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147560-f64f2adb-cee3-4acc-ad9d-78e47244873e.png "null")

[官网](https://element.eleme.cn/#/zh-CN/component/custom-theme)

新建 styles/index.scss

```
// 修改主题色
$--color-primary: rgba(114,124,245,1);
$--font-path: '~element-ui/lib/theme-chalk/fonts';
@import "~element-ui/packages/theme-chalk/src/index";

//初始化body样式
body {
  margin: 0;
  padding: 0;
  background: #fafbfe;
}
```

main.js 引入

```
import '@/styles/index.scss'
```

## 五、公共模块的封装

### 1.request模块 - axios封装

接口文档地址：[https://www.apifox.cn/apidoc/project-934563/api-19465917](https://www.apifox.cn/apidoc/project-934563/api-19465917)

我们会使用 axios 来请求后端接口, 一般都会对 axios 进行一些配置 (比如: 配置基础地址等)

一般项目开发中, 都会对 axios 进行基本的二次封装, 单独封装到一个模块中, 便于使用

1. 安装 axios

```
npm i axios
```

2. 新建 `utils/request.js` 封装 axios 模块利用 axios.create 创建一个自定义的 axios 来使用[http://www.axios-js.com/zh-cn/docs/#axios-create-config](http://www.axios-js.com/zh-cn/docs/#axios-create-config)

```
/* 封装axios用于发送请求 */
import axios from 'axios'

// 创建一个新的axios实例
const request = axios.create({
  baseURL: 'http://interview-api-t.itheima.net/',
  timeout: 5000
})

// 添加请求拦截器
request.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

// 添加响应拦截器
request.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response.data
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error)
})

export default request
```

### 2.storage模块 - 本地存储

新建 utils/storage.js

```
// 以前 token 令牌，如果存到了本地，每一次都写这么长，太麻烦
// localStorage.setItem(键， 值)
// localStorage.getItem(键)
// localStorage.removeItem(键)

const KEY = 'my-token-element-pc'

// 直接用按需导出，可以导出多个
// 但是按需导出，导入时必须 import { getToken } from '模块名导入'

// 获取
export const getToken = () => {
  return localStorage.getItem(KEY)
}

// 设置
export const setToken = (newToken) => {
  localStorage.setItem(KEY, newToken)
}

// 删除
export const delToken = () => {
  localStorage.removeItem(KEY)
}
```

## 六、路由设计配置

但凡是: 单个页面，独立展示的，都是一级路由 (登录 注册 首页架子 文章详情 ...)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147615-b9a6880e-149c-4d80-b924-1becb00d0f9c.png "null")

路由设计：

- 登录页 （一级） login

- 首页架子（一级） layout

- 数据看板（二级）dashboard

- 文章管理（二级）article

### 1.新建目录

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147680-60b1be26-a8ce-4487-a61d-931fad07c754.png "null")

以上文件夹及文件 直接从【素材中】拷贝即可

### 2.配置路由

`router/index.js`

```
import VueRouter from 'vue-router'
import Vue from 'vue'

import Layout from '@/views/layout'
import Login from '@/views/login'
import Dashboard from '@/views/dashboard'
import Article from '@/views/article'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/login', component: Login },
    {
      path: '/',
      component: Layout,
      redirect: '/dashboard',
      children: [
        { path: 'dashboard', component: Dashboard },
        { path: 'article', component: Article }
      ]
    }
  ]
})

export default router
```

`layout/index` 配置二级路由出口

```
<template>
  <div>
    <div>头部</div>

    <div>侧边</div>

    <router-view></router-view>

  </div>

</template>

<script>
export default {
  name: 'LayoutIndex'
}
</script>

<style>

</style>
```

测试路径1： [http://localhost:8080/#/login](http://localhost:8080/#/login)

测试路径2： [http://localhost:8080/#/dashboard](http://localhost:8080/#/dashboard)

测试路径3： [http://localhost:8080/#/article](http://localhost:8080/#/article)

## 七、登录模块

### 1.说明：

我们先学习 element-ui 表单组件的基本结构使用

### 2.需求：

实现如图效果

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147753-1c9c66e5-fd7d-4d51-8bde-6ff98f3177a0.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147826-0e2df05e-25cb-4a70-9c85-ea2464cef29c.png "null")

### 3.样式控制

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147880-bbbb31bc-9f4a-4014-88c6-b7ad71d19f7b.png "null")

一般情况，这种第三方的组件，为了样式控制方便，会给组件的根元素，起一个和组件名同名的类名

控制组件的样式：

1. 直接通过组件名 同名的 类， 进行控制样式

2. 自己通过添加 class 类名，进行控制样式

默认，写在scoped中的样式，只会影响到当前组件模板中的元素内容

深度作用选择器：向下影响到子元素的样式。Vue 组件样式中用来**穿透 scoped 样式限制**的语法，适用于修改第三方组件（比如 Element UI）内部的样式。

::v-deep (scss)

/deep/ (less)

```
<template>
  <div class="login-page">
    <el-card class="el-card">
      <template #header>黑马面经运营后台</template>

      <el-form>
        <el-form-item label="用户名：">
          <el-input placeholder="请输入用户名" />
        </el-form-item>

        <el-form-item label="密码：">
          <el-input placeholder="请输入密码：" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary">登录</el-button>

          <el-button>重置</el-button>

        </el-form-item>

      </el-form>

    </el-card>

  </div>

</template>

<script>
export default {
  name: 'login-page'
}
</script>

<style lang="scss" scoped>
.el-card {
  width: 420px;
  margin: 0 auto;
  // 深度作用选择器   ::v-deep   /deep/
  ::v-deep .el-card__header { // __组件的子元素
    background: rgba(114,124,245,1);
    text-align: center;
    color: white;
  }
}
</style>
```

## 八、登录模块-样式美化

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944147936-a01b02ee-25a2-4411-ba86-1f914fc66234.png "null")

```
<template>
  <div class="login-page">
    <el-card>
      <template #header>黑马面经运营后台</template>

      <el-form autocomplete="off">
        <el-form-item label="用户名">
          <el-input placeholder="输入用户名"></el-input>

        </el-form-item>

        <el-form-item label="密码">
          <el-input type="password" placeholder="输入用户密码"></el-input>

        </el-form-item>

        <el-form-item class="tc">
          <el-button type="primary">登 录</el-button>

          <el-button >重 置</el-button>

        </el-form-item>

      </el-form>

    </el-card>

  </div>

</template>

<script>
export default {
  name: 'login-page',
  data () {
    return {

    }
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
.login-page {
  min-height: 100vh;
  background: url(@/assets/login-bg.svg) no-repeat center / cover;
  display: flex;
  align-items: center;
  justify-content: space-around;
  .el-card {
    width: 420px;
    ::v-deep .el-card__header{
      height: 80px;
      background: rgba(114,124,245,1);
      text-align: center;
      line-height: 40px;
      color: #fff;
      font-size: 18px;
    }
  }
  .el-form {
    padding: 0 20px;
  }
  .tc {
    text-align: center;
  }
}
</style>
```

## 九、element-ui 基本校验

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148008-ca8c02e8-c945-4f57-84e7-937b245c4dd7.png "null")

说明：在向后端发请求，调用接口之前，我们需要对所要传递的参数进行验证，把用户的错误扼杀在摇篮之中。

讲解内容:

- element-ui的校验

- el-form: `model`属性, `rules`规则

- el-form-item: 绑定 `prop` 属性

- el-input: 绑定 `v-model`

Form 组件提供了表单验证的功能

1. form组件需要 `:model`绑定form对象（必须）， 需要通过 `rules` 属性传入约定的验证规则

```
<el-form :model="form" :rules="rules">
    
export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  }
}
```

2. 在 data 中准备 rules 规则

```
rules: {
  username: [
    { required: true, message: '请输入用户名', trigger: ['blur', 'change'] },
    { min: 5, max: 11, message: '长度在 5 到 11 个字符', trigger: ['blur', 'change'] }
  ]
}
```

3. 将 Form-Item 的 `prop` 属性设置为需校验的字段名

```
<el-form-item label="用户名：" prop="username">
  <el-input v-model="form.username" placeholder="请输入手机号" />
</el-form-item>
```

## 十、element-ui 正则校验

下面是常用内置的基本验证规则：其余校验规则参见 [async-validator](https://github.com/yiminghe/async-validator)

|   |   |
|---|---|
|规则|说明|
|required|必须的，例如校验内容是否非空|
|pattern|正则表达式，例如校验手机号码格式、校验邮箱格式|

```
rules: {
  username: [
    { required: true, message: '请输入用户名', trigger: ['blur', 'change'] },
    { min: 5, max: 11, message: '长度在 5 到 11 个字符', trigger: ['blur', 'change'] }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: ['blur', 'change'] },
    { pattern: /^\w{5,11}$/, message: '请输入 5 到 10 位的密码', trigger: ['blur', 'change'] }
  ]
}

// \d 数字 0-9
// \w 字母数字下划线
// {m,n} 前面的字符，可以出现 m次 ~ n次
```

不要忘了配置prop

```
<el-form-item prop="password">
```

上述已经可以完成大部分需求，如果需要更复杂业务校验需求，可以自定义校验~ （项目课程：人力资源系统会进一步讲解）

## 十一、提交表单校验 和 重置

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148066-acb2e368-6550-4908-ab61-176c57766bea.png "null")

每次点击按钮, 进行ajax登录前, 应该先对整个表单内容校验, 不然还是会发送很多无效的请求!!!

要通过校验了, 才发送请求!!!

**作用:** `ref` **属性配合** `$refs` **可以获取 dom 元素 (或者 vue组件实例)**

1. 给组件或者元素, 添加 ref 属性

```
<hello ref="bb"></hello>
```

2. 通过 this.$refs 可以获取对应的引用, 并且调用方法

```
this.$refs.bb.sayHi()
```

**添加登录提交的校验**

```
<el-form ref="form" :model="form" :rules="rules" autocomplete="off">
...
<el-button @click="login" type="primary">登 录</el-button>

methods: {
  login () {
      this.$refs.form.validate(valid =>{
          if(!valid){
              return
          }
          console.log('可以发送请求了')
      })   
  }
}
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148124-7f1526bf-f0ed-4e83-b2af-7fb0828bb82c.png "null")

**添加重置功能**

```
<el-button @click="reset">重 置</el-button>

methods: {
  reset () {
    this.$refs.form.resetFields()
  }
}
```

## 十二、封装登录api登录请求

新建 `api/user.js` 提供api接口函数

```
import request from '@/utils/request'

export const login = ({ username, password }) => {
  return request.post('/auth/login', {
    username,
    password
  })
}
```

发送请求获取token

```
methods: {
   login () {
       this.$refs.form.validate(async valid =>{
        if(!valid){
            return
        }
          const res= await login(this.form)
        console.log(res)
      })    
  }
}
```

## 十三、vuex - user 模块 - 存token

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148211-ee1684c3-ac2b-455d-bd6f-6ea45b4066e0.png "null")

新建 `store/modules/user.js`

```
import { getToken, setToken } from '@/utils/storage'

export default {
  namespaced: true,
  state () {
    return {
      token: getToken()
    }
  },
  mutations: {
    setUserToken (state, payload) {
      state.token = payload
      setToken(payload)
    }
  },
  actions: { 
    async loginAction (context, obj) {
      // 发送登录请求
      const res = await login(obj)
      // commit mutation
      context.commit('setUserToken', res.data.token)
    }
  },
}
```

挂载模块

```
import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user
  }
})
```

登录时调用

```
async login () {
      // 登录时，需要先校验，校验通过才能发请求
      // 校验：通过 ref 和 $refs 拿到 el-form 组件，调用组件的校验方法
      // console.log(this.$refs.form)
      try {
        await this.$refs.form.validate()
        // 调用action(异步) async函数的调用会返回一个promise
        await this.$store.dispatch('user/loginAction', this.form)
        this.$message.success('恭喜登录成功')
        this.$router.push('/')
      } catch (e) {
        console.log(e)
      }
    },
        
        
 // 传统
this.$refs.form.validate((valid) => {
  if (valid) {
    // 提交登录请求
  } else {
    // 校验未通过
  }
})
```

## 十四、统一错误拦截

```
import { Message } from 'element-ui'


// 添加响应拦截器
request.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response.data
}, function (error) {
  // 所有的响应错误信息，统一处理
  if (error.response) { 
      Message.error(error.response.data.message) 
  }
  // 对响应错误做点什么
  return Promise.reject(error)
})
```

## 十五、登录访问拦截

`router/index.js`

没有token 且 访问的不是 登录页，就直接拦截到登录

```
// 白名单，定义成登录
const whiteList = ['/login']

// 路由导航守卫
router.beforeEach((to, from, next) => {
  // 1. 看有没有 token (vuex)，如果有，直接放行
  const token = store.state.user.token
  if (token) {
    next()
    return
  }

  // 2. 看是否在 白名单，如果在，直接放行
  if (whiteList.includes(to.path)) {
    next()
    return
  }

  // 3. 其他情况，拦截到登录
  next('/login')
})
```

## 十六、首页 layout 模块及请求拦截器统一处理

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148277-2d53a107-59ff-472e-af38-1dc0918d2e60.png "null")

### 1.layout 布局

`api/user.js` 准备api接口

```
export const getUser = () => {
  return request.get('/auth/currentUser')
}
```

`layout/index.vue`准备结构 （已准备）

```
<template>
  <el-container class="layout-page">
    <el-aside width="200px">
      <div class="logo">黑马面经</div>

      <el-menu
        router
        :default-active="$route.path"
        background-color="#313a46"
        text-color="#8391a2"
        active-text-color="#FFF"
      >
        <el-menu-item index="/dashboard">
          <i class="el-icon-pie-chart"></i>

          <span>数据看板</span>

        </el-menu-item>

        <el-menu-item index="/article">
          <i class="el-icon-notebook-1"></i>

          <span>面经管理</span>

        </el-menu-item>

      </el-menu>

    </el-aside>

    <el-container>
      <el-header>
        <div class="user">
          <el-avatar
            :size="36"
            :src="avatar"
          ></el-avatar>

          <el-link :underline="false">{{name}}</el-link>

        </div>

        <div class="logout">
          <el-popconfirm title="您确认退出黑马面运营后台吗？" @confirm="handleConfirm">
            <i slot="reference" title="logout" class="el-icon-switch-button"></i>

          </el-popconfirm>

        </div>

      </el-header>

      <el-main>
        <router-view></router-view>

      </el-main>

    </el-container>

  </el-container>

</template>

<script>
import { getUser } from '@/api/user'
export default {
  name: 'layout-page',
  data () {
    return {
      avatar: '',
      name: ''
    }
  },
  created () {
    this.initData()
  },
  methods: {
    async initData () {
      const { data } = await getUser()
      this.avatar = data.avatar
      this.name = data.name
    },
    handleConfirm () {
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped>
.layout-page {
  height: 100vh;
  .el-aside {
    background: #313a46;
    .logo {
      color: #fff;
      font-size: 20px;
      height: 60px;
      line-height: 60px;
      text-align: center;
    }
    .el-menu {
      border-right: none;
      margin-top: 20px;
      &-item {
        background-color: transparent !important;
        > span, i {
          padding-left: 5px;
        }
      }
    }
  }
  .el-header {
    box-shadow: 0px 0px 35px 0px rgba(154, 161, 171, 0.15);
    background: #fff;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    z-index: 999;
    .user {
      display: flex;
      align-items: center;
      background: #fafbfd;
      height: 60px;
      border: 1px solid #f1f3fa;
      padding: 0 15px;
      .el-avatar {
        margin-right: 15px;
      }
    }
    .logout {
      font-size: 20px;
      color: #999;
      cursor: pointer;
      padding: 0 15px;
    }
  }
  .el-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #aaa;
    border-top: 1px solid rgba(152, 166, 173, 0.2);
    font-size: 14px;
  }
}
</style>
```

遇到 401 错误

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148353-8b92963f-c032-4986-aa92-5f7dd2981ccf.png "null")

### 2.请求拦截器携带token

`utils/request.js`

```
// 添加请求拦截器
request.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  const { token } = store.state.user
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})
```

## 十七、退出功能

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148403-09cab779-d670-4895-bc31-29d8f464817e.png "null")

退出操作

```
handleConfirm () {
  // this.$router.push('/login')
  this.$store.commit('user/logout')
  this.$router.push('/login')
}
```

提供mutation

```
import { delToken, getToken, setToken } from '@/utils/storage'

export default {
  namespaced: true,
  state () {
    return {
      token: getToken()||''
    }
  },
  mutations: {
    ...,
    logout (state) {
      state.token = ''
      delToken()
    }
  }
}
```

## 十八、处理token过期

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148459-a8701d32-eec9-449a-aaf4-8a7cae39f4e9.png "null")

响应拦截器，处理token过期

```
import router from '../router'

// 添加响应拦截器
request.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response.data
}, function (error) {
  // 对响应错误做点什么  普通错误 + 401情况
  // console.dir(error)
  if (error.response) {
    if (error.response.status === 401) {
      // 给提示，清除无效token(vuex+本地)，拦到登录
      Message.error('尊敬的用户，当前登录状态已过期！')

      // 提交清除token的mutation
      store.commit('user/logout')

      // 跳转到登录
      router.push('/login')
    } else {
      // 给提示
      Message.error(error.response.data.message)
    }
  }
  return Promise.reject(error)
})
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748944148517-6cb3d7f4-8ec3-4e71-b1d1-aa018555b32a.png "null")