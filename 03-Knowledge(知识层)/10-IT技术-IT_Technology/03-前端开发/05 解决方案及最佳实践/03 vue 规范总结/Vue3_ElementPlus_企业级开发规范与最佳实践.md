# Vue3 + Element Plus 企业级开发规范与最佳实践

> 基于 Vue3 Composition API + Element Plus + Vite + Pinia 的企业级前端项目开发规范，涵盖项目结构、Axios 封装、权限控制、数据大屏适配等核心实践。参考 2026 年 Vue3 企业级开发最新趋势。citeweb_search:6#1web_search:6#2

---

## 一、项目目录结构规范

```
project/
├── .env                    # 环境变量（开发）
├── .env.production         # 环境变量（生产）
├── vite.config.ts          # Vite 构建配置
├── package.json            # 依赖管理
├── src/
│   ├── main.ts             # 入口文件（注册全局组件、插件）
│   ├── App.vue             # 根组件（仅 <router-view />）
│   ├── api/                # API 接口层
│   │   ├── system/
│   │   │   ├── user.ts     # 用户相关接口
│   │   │   └── type.ts     # 用户数据模型（TypeScript 类型）
│   │   └── login.ts        # 登录接口
│   ├── assets/             # 静态资源
│   │   ├── icons/          # SVG 图标
│   │   ├── images/         # 图片
│   │   └── styles/         # 全局样式
│   │       ├── index.scss    # 全局基础样式（在 main.ts 引入）
│   │       ├── reset.scss    # 清除默认样式
│   │       └── variable.scss # SCSS 全局变量（vite.config.ts 配置引入）
│   ├── components/         # 全局公共组件
│   ├── directive/          # 自定义指令（权限控制、防抖节流等）
│   ├── layout/             # 布局组件
│   │   ├── index.vue       # 布局主入口
│   │   ├── components/
│   │   │   ├── AppMain.vue     # 主内容区
│   │   │   ├── Navbar.vue      # 顶部导航栏
│   │   │   ├── Sidebar/        # 侧边栏
│   │   │   │   ├── index.vue
│   │   │   │   ├── SidebarItem.vue
│   │   │   │   └── SidebarLogo.vue
│   │   │   └── TagsView/       # 标签页
│   │   └── hooks/
│   │       └── useLayout.js    # 布局相关组合式函数
│   ├── router/             # 路由配置
│   │   ├── index.ts        # 路由实例创建 + 守卫
│   │   └── routes.ts       # 常量路由（基础路由）
│   ├── store/              # Pinia 状态管理
│   │   ├── index.ts        # 大仓库创建
│   │   ├── modules/        # 小仓库（user、app、permission 等）
│   │   └── types/
│   │       └── type.ts     # 仓库 state 类型定义
│   ├── utils/              # 工具函数
│   │   ├── request.ts      # Axios 二次封装
│   │   ├── auth.ts         # Token 存取（基于 js-cookie）
│   │   └── ruoyi.ts        # 通用方法（日期格式化、树构建等）
│   └── views/              # 页面组件
│       ├── login/          # 登录页
│       ├── home/           # 首页
│       ├── system/         # 系统管理
│       │   └── user/       # 用户管理
│       └── screen/         # 数据大屏
└── public/                 # 静态公共资源
```

> **军规 1**：按业务域组织代码，而非按技术类型。模块越独立，重构成本越低。citeweb_search:6#1

---

## 二、环境变量配置

### 2.1 .env.development

```env
# 页面标题
VITE_APP_TITLE = 若依管理系统

# 开发环境配置
VITE_APP_ENV = 'development'

# 接口基础路径（会被 Vite 代理转发）
VITE_APP_BASE_API = '/dev-api'
```

### 2.2 Vite 代理配置（vite.config.ts）

```ts
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())
  const { VITE_APP_ENV } = env

  return {
    base: VITE_APP_ENV === 'production' ? '/' : '/',
    plugins: [vue()],
    resolve: {
      alias: {
        '~': path.resolve(__dirname, './'),
        '@': path.resolve(__dirname, './src')
      }
    },
    server: {
      port: 80,
      host: true,
      open: true,
      proxy: {
        '/dev-api': {
          target: 'http://localhost:8080',
          changeOrigin: true,
          rewrite: (p) => p.replace(/^\/dev-api/, '')
        }
      }
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `@use "@/styles/variable.scss" as *;`
        }
      }
    }
  }
})
```

> `proxy` 将前端 `/dev-api/**` 请求代理到后端 `http://localhost:8080`，并自动去掉 `/dev-api` 前缀。

---

## 三、Axios 二次封装（request.ts）

### 3.1 核心封装

```ts
import axios from 'axios'
import { ElNotification, ElMessageBox, ElMessage, ElLoading } from 'element-plus'
import { getToken } from '@/utils/auth'
import errorCode from '@/utils/errorCode'
import { tansParams, blobValidate } from '@/utils/ruoyi'
import cache from '@/plugins/cache'
import { saveAs } from 'file-saver'
import useUserStore from '@/store/modules/user'

// 创建 axios 实例
const service = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json;charset=utf-8' }
})

// ========== 请求拦截器 ==========
service.interceptors.request.use(config => {
  // 是否需要携带 token（默认需要）
  const isToken = (config.headers || {}).isToken === false
  // 是否需要防止重复提交（默认需要）
  const isRepeatSubmit = (config.headers || {}).repeatSubmit === false

  // 1. Token 注入
  if (getToken() && !isToken) {
    config.headers['Authorization'] = 'Bearer ' + getToken()
  }

  // 2. GET 请求 params 序列化
  if (config.method === 'get' && config.params) {
    let url = config.url + '?' + tansParams(config.params)
    url = url.slice(0, -1)
    config.params = {}
    config.url = url
  }

  // 3. 防重复提交（针对 POST/PUT）
  if (!isRepeatSubmit && (config.method === 'post' || config.method === 'put')) {
    const requestObj = {
      url: config.url,
      data: typeof config.data === 'object' ? JSON.stringify(config.data) : config.data,
      time: new Date().getTime()
    }
    const requestSize = Object.keys(JSON.stringify(requestObj)).length
    const limitSize = 5 * 1024 * 1024 // 5MB 限制

    if (requestSize >= limitSize) {
      console.warn(`[${config.url}]: 请求数据超出 5MB，跳过防重复提交验证`)
      return config
    }

    const sessionObj = cache.session.getJSON('sessionObj')
    if (!sessionObj) {
      cache.session.setJSON('sessionObj', requestObj)
    } else {
      const interval = 1000 // 1秒内视为重复提交
      if (sessionObj.data === requestObj.data &&
          requestObj.time - sessionObj.time < interval &&
          sessionObj.url === requestObj.url) {
        const message = '数据正在处理，请勿重复提交'
        console.warn(`[${config.url}]: ${message}`)
        return Promise.reject(new Error(message))
      } else {
        cache.session.setJSON('sessionObj', requestObj)
      }
    }
  }

  return config
}, error => {
  console.log(error)
  return Promise.reject(error)
})

// ========== 响应拦截器 ==========
service.interceptors.response.use(res => {
  const code = res.data.code || 200
  const msg = errorCode[code] || res.data.msg || errorCode['default']

  // 二进制数据直接返回（文件下载）
  if (res.request.responseType === 'blob' || res.request.responseType === 'arraybuffer') {
    return res.data
  }

  // 状态码处理
  if (code === 401) {
    // Token 过期，弹窗重新登录
    if (!isRelogin.show) {
      isRelogin.show = true
      ElMessageBox.confirm('登录状态已过期，请重新登录', '系统提示', {
        confirmButtonText: '重新登录',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        isRelogin.show = false
        useUserStore().logOut().then(() => {
          location.href = '/index'
        })
      }).catch(() => { isRelogin.show = false })
    }
    return Promise.reject('无效的会话，请重新登录')
  } else if (code === 500) {
    ElMessage({ message: msg, type: 'error' })
    return Promise.reject(new Error(msg))
  } else if (code === 601) {
    ElMessage({ message: msg, type: 'warning' })
    return Promise.reject(new Error(msg))
  } else if (code !== 200) {
    ElNotification.error({ title: msg })
    return Promise.reject('error')
  }

  return Promise.resolve(res.data)
}, error => {
  let { message } = error
  if (message === 'Network Error') {
    message = '后端接口连接异常'
  } else if (message.includes('timeout')) {
    message = '系统接口请求超时'
  } else if (message.includes('Request failed with status code')) {
    message = '系统接口' + message.substr(message.length - 3) + '异常'
  }
  ElMessage({ message, type: 'error', duration: 5000 })
  return Promise.reject(error)
})

// ========== 通用下载方法 ==========
let downloadLoadingInstance

export function download(url, params, filename, config) {
  downloadLoadingInstance = ElLoading.service({
    text: '正在下载数据，请稍候',
    background: 'rgba(0, 0, 0, 0.7)'
  })

  return service.post(url, params, {
    transformRequest: [(params) => tansParams(params)],
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    responseType: 'blob',
    ...config
  }).then(async (data) => {
    const isBlob = blobValidate(data)
    if (isBlob) {
      const blob = new Blob([data])
      saveAs(blob, filename)
    } else {
      const resText = await data.text()
      const rspObj = JSON.parse(resText)
      const errMsg = errorCode[rspObj.code] || rspObj.msg || errorCode['default']
      ElMessage.error(errMsg)
    }
    downloadLoadingInstance.close()
  }).catch((r) => {
    console.error(r)
    ElMessage.error('下载文件出现错误，请联系管理员！')
    downloadLoadingInstance.close()
  })
}

export default service
```

### 3.2 Token 管理（auth.ts）

```ts
import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}
```

### 3.3 API 接口封装规范

```ts
// api/login.ts
import request from '@/utils/request'

export function login(username, password, code, uuid) {
  return request({
    url: '/login',
    method: 'post',
    data: { username, password, code, uuid },
    headers: {
      isToken: false,        // 登录接口不需要 token
      repeatSubmit: false    // 登录接口不防重复提交
    }
  })
}

// api/system/user.ts
export function listUser(query) {
  return request({
    url: '/system/user/list',
    method: 'get',
    params: query  // GET 请求参数
  })
}

export function getUser(userId) {
  return request({
    url: '/system/user/' + userId,
    method: 'get'
  })
}

export function addUser(data) {
  return request({
    url: '/system/user',
    method: 'post',
    data  // POST 请求体
  })
}

export function updateUser(data) {
  return request({
    url: '/system/user',
    method: 'put',
    data
  })
}

export function delUser(userId) {
  return request({
    url: '/system/user/' + userId,
    method: 'delete'
  })
}

export function updateUserPwd(oldPassword, newPassword) {
  return request({
    url: '/system/user/profile/updatePwd',
    method: 'put',
    params: { oldPassword, newPassword }
  })
}
```

> **规范：** `params` 用于 GET 查询参数，`data` 用于 POST/PUT 请求体，`headers` 用于特殊配置（如免 token）。

---

## 四、Vue 原型扩展与全局方法

### 4.1 原理

`this.$xxx` 调用的是 Vue 实例原型上的属性或方法：

- **Vue 内置：** `$el`、`$refs`、`$emit`、`$nextTick`、`$router`、`$store`
- **自定义扩展：** 通过 `app.config.globalProperties` 挂载（Vue3）

### 4.2 Vue3 全局挂载示例

```ts
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

// 挂载全局方法
app.config.globalProperties.$modal = {
  confirm: ElMessageBox.confirm,
  msgSuccess: (msg) => ElMessage.success(msg)
}
app.config.globalProperties.$download = download

// 注册所有 Element Plus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.mount('#app')
```

### 4.3 在组件中使用

```vue
<script setup>
import { getCurrentInstance } from 'vue'
const { proxy } = getCurrentInstance()

// 调用全局方法
proxy.$modal.confirm('确认删除？').then(() => {
  proxy.$modal.msgSuccess('删除成功')
})
</script>
```

---

## 五、Element Plus 页面模板规范

### 5.1 标准 CRUD 页面结构

一个完整的后台管理页面通常包含以下区域：

```
┌─────────────────────────────────────────────┐
│  搜索表单区 (Search Form)                    │
├─────────────────────────────────────────────┤
│  功能按钮区 (Action Buttons)                 │
├─────────────────────────────────────────────┤
│  数据表格区 (Data Table)                     │
├─────────────────────────────────────────────┤
│  分页栏 (Pagination)                         │
├─────────────────────────────────────────────┤
│  新增/修改对话框 (Dialog)                     │
└─────────────────────────────────────────────┘
```

### 5.2 搜索表单

```vue
<template>
  <el-form :model="queryParams" ref="queryRef" :inline="true" v-show="showSearch" label-width="68px">
    <el-form-item label="用户名称" prop="userName">
      <el-input
        v-model="queryParams.userName"
        placeholder="请输入用户名称"
        clearable
        style="width: 240px"
        @keyup.enter="handleQuery"
      />
    </el-form-item>

    <el-form-item label="状态" prop="status">
      <el-select v-model="queryParams.status" placeholder="用户状态" clearable style="width: 240px">
        <el-option
          v-for="dict in sys_normal_disable"
          :key="dict.value"
          :label="dict.label"
          :value="dict.value"
        />
      </el-select>
    </el-form-item>

    <el-form-item label="创建时间" style="width: 308px">
      <el-date-picker
        v-model="dateRange"
        value-format="YYYY-MM-DD"
        type="daterange"
        range-separator="-"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
      />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" icon="Search" @click="handleQuery">搜索</el-button>
      <el-button icon="Refresh" @click="resetQuery">重置</el-button>
    </el-form-item>
  </el-form>
</template>
```

**el-form 常用属性速查：**

| 属性 | 说明 | 示例 |
|------|------|------|
| `:model` | 表单数据对象 | `:model="queryParams"` |
| `:rules` | 校验规则 | `:rules="rules"` |
| `ref` | 表单引用 | `ref="queryRef"` |
| `:inline` | 行内表单模式 | `:inline="true"` |
| `label-width` | 标签统一宽度 | `label-width="80px"` |

**常用方法（通过 ref 调用）：**

```ts
proxy.$refs.queryRef.validate((valid) => { /* 校验 */ })
proxy.$refs.queryRef.resetFields()   // 重置表单
proxy.$refs.queryRef.clearValidate() // 清除校验
```

### 5.3 功能按钮区

```vue
<el-row :gutter="10" class="mb8">
  <el-col :span="1.5">
    <el-button type="primary" plain icon="Plus" @click="handleAdd"
      v-hasPermi="['system:user:add']">新增</el-button>
  </el-col>
  <el-col :span="1.5">
    <el-button type="success" plain icon="Edit" :disabled="single" @click="handleUpdate"
      v-hasPermi="['system:user:edit']">修改</el-button>
  </el-col>
  <el-col :span="1.5">
    <el-button type="danger" plain icon="Delete" :disabled="multiple" @click="handleDelete"
      v-hasPermi="['system:user:remove']">删除</el-button>
  </el-col>
  <el-col :span="1.5">
    <el-button type="warning" plain icon="Download" @click="handleExport"
      v-hasPermi="['system:user:export']">导出</el-button>
  </el-col>
  <right-toolbar v-model:showSearch="showSearch" @queryTable="getList" :columns="columns" />
</el-row>
```

| 按钮类型 | 颜色 | 用途 |
|---------|------|------|
| `primary` | 蓝色 | 新增 |
| `success` | 绿色 | 修改 |
| `danger` | 红色 | 删除 |
| `warning` | 黄色 | 导出 |
| `info` | 灰色 | 导入 |

### 5.4 数据表格

```vue
<el-table v-loading="loading" :data="userList" @selection-change="handleSelectionChange">
  <!-- 多选列 -->
  <el-table-column type="selection" width="50" align="center" />

  <!-- 数据列（支持显示/隐藏控制） -->
  <el-table-column label="用户编号" align="center" prop="userId" v-if="columns[0].visible" />
  <el-table-column label="用户名称" align="center" prop="userName" v-if="columns[1].visible" :show-overflow-tooltip="true" />

  <!-- 状态列（可编辑） -->
  <el-table-column label="状态" align="center" key="status" v-if="columns[5].visible">
    <template #default="scope">
      <el-switch
        v-model="scope.row.status"
        active-value="0"
        inactive-value="1"
        @change="handleStatusChange(scope.row)"
      />
    </template>
  </el-table-column>

  <!-- 操作列 -->
  <el-table-column label="操作" align="center" width="150" class-name="small-padding fixed-width">
    <template #default="scope">
      <el-tooltip content="修改" placement="top">
        <el-button link type="primary" icon="Edit" @click="handleUpdate(scope.row)"
          v-hasPermi="['system:user:edit']" />
      </el-tooltip>
      <el-tooltip content="删除" placement="top">
        <el-button link type="primary" icon="Delete" @click="handleDelete(scope.row)"
          v-hasPermi="['system:user:remove']" />
      </el-tooltip>
    </template>
  </el-table-column>
</el-table>
```

### 5.5 分页组件

```vue
<pagination
  v-show="total > 0"
  :total="total"
  v-model:page="queryParams.pageNum"
  v-model:limit="queryParams.pageSize"
  @pagination="getList"
/>
```

### 5.6 新增/修改对话框

```vue
<el-dialog :title="title" v-model="open" width="600px" append-to-body>
  <el-form :model="form" :rules="rules" ref="userRef" label-width="80px">
    <el-row>
      <el-col :span="12">
        <el-form-item label="用户昵称" prop="nickName">
          <el-input v-model="form.nickName" placeholder="请输入用户昵称" maxlength="30" />
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <el-form-item label="归属部门" prop="deptId">
          <el-tree-select
            v-model="form.deptId"
            :data="deptOptions"
            :props="{ value: 'id', label: 'label', children: 'children' }"
            value-key="id"
            placeholder="请选择归属部门"
            check-strictly
          />
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>

  <template #footer>
    <div class="dialog-footer">
      <el-button type="primary" @click="submitForm">确 定</el-button>
      <el-button @click="cancel">取 消</el-button>
    </div>
  </template>
</el-dialog>
```

### 5.7 完整 JS 逻辑（Composition API）

```ts
<script setup name="User">
import { ref, reactive, watch, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { getToken } from '@/utils/auth'
import { listUser, getUser, addUser, updateUser, delUser, deptTreeSelect } from '@/api/system/user'

const router = useRouter()
const { proxy } = getCurrentInstance()
const { sys_normal_disable, sys_user_sex } = proxy.useDict('sys_normal_disable', 'sys_user_sex')

// ========== 响应式数据 ==========
const userList = ref([])
const loading = ref(true)
const showSearch = ref(true)
const open = ref(false)
const title = ref('')
const total = ref(0)
const ids = ref([])
const single = ref(true)
const multiple = ref(true)
const dateRange = ref([])
const deptName = ref('')
const deptOptions = ref(undefined)

// 列显示控制
const columns = ref([
  { key: 0, label: '用户编号', visible: true },
  { key: 1, label: '用户名称', visible: true },
  { key: 2, label: '用户昵称', visible: true },
  { key: 3, label: '部门', visible: true },
  { key: 4, label: '手机号码', visible: true },
  { key: 5, label: '状态', visible: true },
  { key: 6, label: '创建时间', visible: true }
])

// 表单数据
const data = reactive({
  form: {},
  queryParams: {
    pageNum: 1,
    pageSize: 10,
    userName: undefined,
    phonenumber: undefined,
    status: undefined,
    deptId: undefined
  },
  rules: {
    userName: [
      { required: true, message: '用户名称不能为空', trigger: 'blur' },
      { min: 2, max: 20, message: '长度必须介于 2 和 20 之间', trigger: 'blur' }
    ],
    nickName: [{ required: true, message: '用户昵称不能为空', trigger: 'blur' }],
    password: [
      { required: true, message: '用户密码不能为空', trigger: 'blur' },
      { min: 5, max: 20, message: '长度必须介于 5 和 20 之间', trigger: 'blur' },
      { pattern: /^[^<>"'|\\]+$/, message: '不能包含非法字符', trigger: 'blur' }
    ],
    email: [{ type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }],
    phonenumber: [
      { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号码', trigger: 'blur' }
    ]
  }
})

const { queryParams, form, rules } = toRefs(data)

// ========== 方法 ==========

/** 查询用户列表 */
function getList() {
  loading.value = true
  listUser(proxy.addDateRange(queryParams.value, dateRange.value)).then(res => {
    loading.value = false
    userList.value = res.rows
    total.value = res.total
  })
}

/** 搜索 */
function handleQuery() {
  queryParams.value.pageNum = 1
  getList()
}

/** 重置 */
function resetQuery() {
  dateRange.value = []
  proxy.resetForm('queryRef')
  queryParams.value.deptId = undefined
  proxy.$refs.deptTreeRef.setCurrentKey(null)
  handleQuery()
}

/** 新增 */
function handleAdd() {
  reset()
  getUser().then(response => {
    postOptions.value = response.posts
    roleOptions.value = response.roles
    open.value = true
    title.value = '添加用户'
  })
}

/** 修改 */
function handleUpdate(row) {
  reset()
  const userId = row.userId || ids.value
  getUser(userId).then(response => {
    form.value = response.data
    postOptions.value = response.posts
    roleOptions.value = response.roles
    form.value.postIds = response.postIds
    form.value.roleIds = response.roleIds
    open.value = true
    title.value = '修改用户'
  })
}

/** 提交 */
function submitForm() {
  proxy.$refs.userRef.validate(valid => {
    if (valid) {
      if (form.value.userId != undefined) {
        updateUser(form.value).then(() => {
          proxy.$modal.msgSuccess('修改成功')
          open.value = false
          getList()
        })
      } else {
        addUser(form.value).then(() => {
          proxy.$modal.msgSuccess('新增成功')
          open.value = false
          getList()
        })
      }
    }
  })
}

/** 删除 */
function handleDelete(row) {
  const userIds = row.userId || ids.value
  proxy.$modal.confirm(`是否确认删除用户编号为"${userIds}"的数据项？`).then(() => {
    return delUser(userIds)
  }).then(() => {
    getList()
    proxy.$modal.msgSuccess('删除成功')
  })
}

/** 状态变更 */
function handleStatusChange(row) {
  const text = row.status === '0' ? '启用' : '停用'
  proxy.$modal.confirm(`确认要"${text}""${row.userName}"用户吗?`).then(() => {
    return changeUserStatus(row.userId, row.status)
  }).then(() => {
    proxy.$modal.msgSuccess(text + '成功')
  }).catch(() => {
    row.status = row.status === '0' ? '1' : '0'
  })
}

/** 表格选择变化 */
function handleSelectionChange(selection) {
  ids.value = selection.map(item => item.userId)
  single.value = selection.length !== 1
  multiple.value = !selection.length
}

/** 重置表单 */
function reset() {
  form.value = {
    userId: undefined,
    deptId: undefined,
    userName: undefined,
    nickName: undefined,
    password: undefined,
    phonenumber: undefined,
    email: undefined,
    sex: undefined,
    status: '0',
    remark: undefined,
    postIds: [],
    roleIds: []
  }
  proxy.resetForm('userRef')
}

/** 取消 */
function cancel() {
  open.value = false
  reset()
}

// 初始化
getList()
</script>
```

---

## 六、权限控制体系

### 6.1 按钮权限（自定义指令）

```ts
// directive/permission/hasPermi.ts
import useUserStore from '@/store/modules/user'

export default {
  mounted(el, binding) {
    const { value } = binding
    const all_permission = '*:*:*'
    const permissions = useUserStore().permissions

    if (value && value instanceof Array && value.length > 0) {
      const permissionFlag = value
      const hasPermissions = permissions.some(permission => {
        return all_permission === permission || permissionFlag.includes(permission)
      })
      if (!hasPermissions) {
        el.parentNode && el.parentNode.removeChild(el)
      }
    } else {
      throw new Error(`请设置操作权限标签值`)
    }
  }
}
```

**使用方式：**

```vue
<el-button v-hasPermi="['system:user:add']">新增</el-button>
<el-button v-hasPermi="['system:user:edit']">修改</el-button>
<el-button v-hasPermi="['system:user:remove']">删除</el-button>
```

### 6.2 路由守卫（鉴权）

```ts
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import { getToken } from '@/utils/auth'
import useUserStore from '@/store/modules/user'

const router = createRouter({
  history: createWebHistory(),
  routes: constantRoutes
})

// 白名单
const whiteList = ['/login', '/register']

router.beforeEach((to, from, next) => {
  const hasToken = getToken()

  if (hasToken) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      const userStore = useUserStore()
      if (userStore.roles.length === 0) {
        // 首次加载，获取用户信息和权限
        userStore.getInfo().then(() => {
          next({ ...to, replace: true })
        })
      } else {
        next()
      }
    }
  } else {
    if (whiteList.includes(to.path)) {
      next()
    } else {
      next(`/login?redirect=${to.path}`)
    }
  }
})
```

---

## 七、数据大屏适配方案

### 7.1 Scale 缩放方案（推荐）

```vue
<template>
  <div class="container">
    <div class="screen" ref="screen">
      <div class="top"><Top /></div>
      <div class="bottom">
        <div class="left"><Tourist /><Sex /><Age /></div>
        <div class="center"><Map /><Line /></div>
        <div class="right"><Rank /><Year /><Counter /></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const screen = ref()

function getScale(w = 1920, h = 1080) {
  const ww = window.innerWidth / w
  const wh = window.innerHeight / h
  return ww < wh ? ww : wh  // 取较小值，保证完整显示
}

onMounted(() => {
  screen.value.style.transform = `scale(${getScale()}) translate(-50%, -50%)`
})

window.onresize = () => {
  screen.value.style.transform = `scale(${getScale()}) translate(-50%, -50%)`
}
</script>

<style scoped lang="scss">
.container {
  width: 100vw;
  height: 100vh;
  background: url(./images/bg.png) no-repeat;
  background-size: cover;
}

.screen {
  position: fixed;
  width: 1920px;
  height: 1080px;
  left: 50%;
  top: 50%;
  transform-origin: left top;
}

.bottom {
  display: flex;
  .left, .right { flex: 1; display: flex; flex-direction: column; }
  .center { flex: 1.5; display: flex; flex-direction: column; }
}
</style>
```

### 7.2 适配方案对比

| 方案 | 原理 | 优点 | 缺点 |
|------|------|------|------|
| **vw/vh** | 视口单位 | 简单直接 | 文字不支持自动缩放，需手动计算 |
| **scale** ⭐ | CSS transform 缩放 | 等比例缩放，组件完美适配 | 边缘可能留白 |

---

## 八、通用工具函数

### 8.1 日期格式化

```ts
export function parseTime(time, pattern = '{y}-{m}-{d} {h}:{i}:{s}') {
  if (!time) return null

  let date
  if (typeof time === 'object') {
    date = time
  } else {
    if (typeof time === 'string' && /^[0-9]+$/.test(time)) {
      time = parseInt(time)
    } else if (typeof time === 'string') {
      time = time.replace(/-/g, '/').replace('T', ' ').replace(/\.\d{3}/, '')
    }
    if (typeof time === 'number' && time.toString().length === 10) {
      time = time * 1000
    }
    date = new Date(time)
  }

  const formatObj = {
    y: date.getFullYear(),
    m: date.getMonth() + 1,
    d: date.getDate(),
    h: date.getHours(),
    i: date.getMinutes(),
    s: date.getSeconds(),
    a: date.getDay()
  }

  return pattern.replace(/{(y|m|d|h|i|s|a)+}/g, (result, key) => {
    let value = formatObj[key]
    if (key === 'a') return ['日', '一', '二', '三', '四', '五', '六'][value]
    if (result.length > 0 && value < 10) value = '0' + value
    return value || 0
  })
}
```

### 8.2 树形数据构建

```ts
export function handleTree(data, id = 'id', parentId = 'parentId', children = 'children') {
  const config = { id, parentId, childrenList: children }
  const childrenListMap = {}
  const nodeIds = {}
  const tree = []

  for (const d of data) {
    const pId = d[config.parentId]
    if (!childrenListMap[pId]) childrenListMap[pId] = []
    nodeIds[d[config.id]] = d
    childrenListMap[pId].push(d)
  }

  for (const d of data) {
    if (nodeIds[d[config.parentId]] == null) {
      tree.push(d)
    }
  }

  function adaptToChildrenList(o) {
    if (childrenListMap[o[config.id]]) {
      o[config.childrenList] = childrenListMap[o[config.id]]
    }
    if (o[config.childrenList]) {
      for (const c of o[config.childrenList]) {
        adaptToChildrenList(c)
      }
    }
  }

  for (const t of tree) adaptToChildrenList(t)
  return tree
}
```

### 8.3 日期范围参数拼接

```ts
export function addDateRange(params, dateRange, propName) {
  let search = params
  search.params = typeof search.params === 'object' && search.params !== null && !Array.isArray(search.params)
    ? search.params : {}
  dateRange = Array.isArray(dateRange) ? dateRange : []

  if (typeof propName === 'undefined') {
    search.params['beginTime'] = dateRange[0]
    search.params['endTime'] = dateRange[1]
  } else {
    search.params['begin' + propName] = dateRange[0]
    search.params['end' + propName] = dateRange[1]
  }
  return search
}
```

---

## 九、最佳实践总结

| 实践项 | 建议 |
|--------|------|
| **API 封装** | 按模块拆分 `api/` 目录，接口与类型定义同文件 |
| **请求参数** | GET 用 `params`，POST/PUT 用 `data`，特殊配置用 `headers` |
| **状态管理** | Pinia 替代 Vuex，按模块拆分小仓库。Store 只存状态和获取状态的方法，不存 UI 逻辑。citeweb_search:6#2 |
| **权限控制** | 路由守卫 + 自定义指令 `v-hasPermi` 双层控制 |
| **表单校验** | 统一在 `rules` 中定义，支持正则、长度、必填等 |
| **大屏适配** | 使用 `scale` 方案，基准尺寸 1920×1080 |
| **组件通信** | 简单场景用 `props/emit`，复杂场景用 Pinia |
| **代码规范** | 使用 `<script setup>` + Composition API，减少 `this` 依赖 |
| **性能优化** | 大数组/对象使用 `shallowRef`/`shallowReactive`，组件懒加载用 `defineAsyncComponent` citeweb_search:6#1 |
| **类型安全** | Props/Emits 必须使用泛型声明，禁用 `any` 使用 `unknown` citeweb_search:6#1 |
