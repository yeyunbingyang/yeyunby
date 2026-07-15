# Pinia

## 核心

**Pinia** 是 Vue 的**存储库**，它允许您**跨组件/页面共享状态**。

Pinia 三个核心概念：

- State：表示 Pinia Store 内部保存的数据（data）

- Getter：可以认为是 Store 里面数据的计算属性（computed）

- Actions：是暴露修改数据的几种方式。

**_虽然外部也可以直接读写Pinia Store 中保存的data，但是我们建议使用Actions暴露的方法操作数据更加安全_**。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444620076-bc0c547a-9910-4ecc-b4e5-523ff865063a.png "null")

需求：在组件 p1 里更新了数据，主页组件也同步更新显示

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444620150-82428661-4d0a-468c-9360-1fc17b7f1873.png "null")

- storage 虽然可以实现多个组件的数据共享，但是需要【主动访问】才能获取更新后的数据

- 本例中由于没有涉及主页组件的 mounted 操作，因此并不会【主动】获取 storage 的数据

## 安装

```
npm install pinia
```

在 main.ts 中引入

```
import { createPinia } from 'pinia'

// ...
createApp(A6).use(antdv).use(router).use(createPinia()).mount('#app')
```

此时开发者工具中已经有了`pinia`选项

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737444620258-1c699e38-a391-4470-bd5d-3f42a5fabc7d.png)

## 定义Store

再新建 store 目录来管理共享数据，下面是 /src/store/UserInfo.ts

```
import axios from '../api/request'
import { defineStore } from "pinia"
import { UserInfoDto } from '../model/Model8080'

export const useUserInfo = defineStore('userInfo', {
  state: () => {
    return { username: '', name: '', sex: '' }
  },
  actions: {
    async get(username: string) {
      const resp = await axios.get(`/api/info/${username}`)
      Object.assign(this, resp.data.data)
    },
    async update(dto: UserInfoDto) {
      await axios.post('/api/info', dto)
      Object.assign(this, dto)
    }
  }
})
```

- 定义了 useUserInfo 函数，用来获取共享数据，它可能用于多个组件

- 命名习惯上，函数变量以 use 打头

- state 定义数据格式

- actions 定义操作数据的方法

- get 方法用来获取用户信息

- update 方法用来修改用户信息

- **由于 useRequest 必须放在 setup 函数内**，这里简化起见，直接使用了 axios

获取用户信息

```
<template>
  <div class="a6main">
    <a-layout>
      <a-layout-header>
        <span>{{serverUsername}} 【{{userInfo.name}} - {{userInfo.sex}}】</span>

      </a-layout-header>

      <a-layout>
        <!-- ... -->
      </a-layout>

    </a-layout>

  </div>

</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import AIcon from '../components/AIcon3' // jsx icon 组件
import { serverMenus, serverUsername } from '../router/a6router'
    
import { useUserInfo } from '../store/UserInfo'
const userInfo = useUserInfo()

onMounted(()=>{
  userInfo.get(serverUsername.value)
})
</script>
```

修改用户信息

```
<template>
  <div class="a6p1">
    <h3>修改用户信息</h3>

    <hr>
    <a-form>
      <a-form-item label="用户名">
        <a-input readonly v-model:value="dto.username"></a-input>

      </a-form-item>

      <a-form-item label="姓名" v-bind="validateInfos.name">
        <a-input v-model:value="dto.name"></a-input>

      </a-form-item>

      <a-form-item label="性别">
        <a-radio-group v-model:value="dto.sex">
          <a-radio-button value="男">男</a-radio-button>

          <a-radio-button value="女">女</a-radio-button>

        </a-radio-group>

      </a-form-item>

    </a-form>

    <a-button type="primary" @click="onClick">确定</a-button>

  </div>

</template>

<script setup lang="ts">
import { Form } from 'ant-design-vue'
import { onMounted, ref } from 'vue'
import { UserInfoDto } from '../model/Model8080'
import { useUserInfo } from '../store/UserInfo';
const dto = ref<UserInfoDto>({ username: '', name: '', sex: '' })
const userInfo = useUserInfo()
onMounted(()=>{
  Object.assign(dto.value, userInfo)
})
const rules = ref({
  name: [
    {required: true, message:'姓名必填'}
  ]
})
const { validateInfos, validate } = Form.useForm(dto, rules)
async function onClick() {
  try {
    await validate()
    await userInfo.update(dto.value)
  } catch (e) {
    console.error(e)
  }
}
</script>
```

- **不能直接把 userInfo 绑定到表单，需要 dto 中转一下【不然就直接修改了共享数据】**

- userInfo.update 和 useInfo.get 返回的都是 Promise 对象，可以配合 await 一起用

## 【存储+读取数据】

1. `Store`是一个保存：**状态**、**业务逻辑** 的实体，每个组件都可以**读取**、**写入**它。

2. 它有三个概念：`state`、`getter`、`action`，相当于组件中的： `data`、 `computed` 和 `methods`。

3. 具体编码：`src/store/count.ts`

```
// 引入defineStore用于创建store
import {defineStore} from 'pinia'

// 定义并暴露一个store
export const useCountStore = defineStore('count',{
  // 动作
  actions:{},
  // 状态
  state(){
    return {
      sum:6
    }
  },
  // 计算
  getters:{}
})
```

4. 具体编码：`src/store/talk.ts`

```
// 引入defineStore用于创建store
import {defineStore} from 'pinia'

// 定义并暴露一个store
export const useTalkStore = defineStore('talk',{
  // 动作
  actions:{},
  // 状态
  state(){
    return {
      talkList:[
        {id:'yuysada01',content:'你今天有点怪，哪里怪？怪好看的！'},
             {id:'yuysada02',content:'草莓、蓝莓、蔓越莓，你想我了没？'},
        {id:'yuysada03',content:'心里给你留了一块地，我的死心塌地'}
      ]
    }
  },
  // 计算
  getters:{}
})
```

5. 组件中使用`state`中的数据

```
<template>
  <h2>当前求和为：{{ sumStore.sum }}</h2>

</template>


<script setup lang="ts" name="Count">
  // 引入对应的useXxxxxStore	
  import {useSumStore} from '@/store/sum'
  
  // 调用useXxxxxStore得到对应的store
  const sumStore = useSumStore()
</script>
```

```
<template>
    <ul>
    <li v-for="talk in talkStore.talkList" :key="talk.id">
      {{ talk.content }}
    </li>

  </ul>

</template>


<script setup lang="ts" name="Count">
  import axios from 'axios'
  import {useTalkStore} from '@/store/talk'

  const talkStore = useTalkStore()
</script>
```

## [修改数据]三种方式

1. 第一种修改方式，直接修改

```
countStore.sum = 666
```

2. 第二种修改方式：批量修改

```
countStore.$patch({
  sum:999,
  school:'atguigu'
})
```

3. 第三种修改方式：借助`action`修改（`action`中可以编写一些业务逻辑）【复用·】

```
import { defineStore } from 'pinia'

export const useCountStore = defineStore('count', {
  /*************/
  actions: {
    //加
    increment(value:number) {
      if (this.sum < 10) {
        //操作countStore中的sum
        this.sum += value
      }
    },
    //减
    decrement(value:number){
      if(this.sum > 1){
        this.sum -= value
      }
    }
  },
  /*************/
})
```

4. 组件中调用`action`即可

```
// 使用countStore
const countStore = useCountStore()

// 调用对应action
countStore.incrementOdd(n.value)
```

## 【storeToRefs】

- 借助`storeToRefs`将`store`中的数据转为`ref`对象，方便在模板中使用。

- **注意：**`pinia`**提供的**`storeToRefs`**只会将数据做转换，而**`Vue`**的**`toRefs`**会转换**`store`**中数据。**

```
<template>
    <div class="count">
        <h2>当前求和为：{{sum}}</h2>

    </div>

</template>

<script setup lang="ts" name="Count">
  import { useCountStore } from '@/store/count'
  /* 引入storeToRefs */
  import { storeToRefs } from 'pinia'

    /* 得到countStore */
  const countStore = useCountStore()
  /* 使用storeToRefs转换countStore，随后解构 */
  const {sum} = storeToRefs(countStore)
</script>
```

## 【getters】

1. 概念：当`state`中的数据，需要经过处理后再使用时，可以使用`getters`配置。

2. 追加` ``getters`` `配置。

```
// 引入defineStore用于创建store
import {defineStore} from 'pinia'

// 定义并暴露一个store
export const useCountStore = defineStore('count',{
  // 动作
  actions:{
    /************/
  },
  // 状态
  state(){
    return {
      sum:1,
      school:'atguigu'
    }
  },
  // 计算
  getters:{
    bigSum:(state):number => state.sum *10,
    upperSchool():string{
      return this. school.toUpperCase()
    }
  }
})
```

3. 组件中读取数据：

```
const {increment,decrement} = countStore
let {sum,school,bigSum,upperSchool} = storeToRefs(countStore)
```

## 【$subscribe】

订阅

通过 store 的 `$subscribe()` 方法侦听 `state` 及其变化

mutate【修改信息】,state【本次修改数据】

```
talkStore.$subscribe((mutate,state)=>{
  console.log('LoveTalk',mutate,state)
  localStorage.setItem('talk',JSON.stringify(talkList.value))
})
```

## 【store组合式setup写法】推荐

```
import {defineStore} from 'pinia'
import axios from 'axios'
import {nanoid} from 'nanoid'
import {reactive} from 'vue'

export const useTalkStore = defineStore('talk',()=>{
  // talkList就是state
  const talkList = reactive(
    JSON.parse(localStorage.getItem('talkList') as string) || []
  )

  // getATalk函数相当于action
  async function getATalk(){
    // 发请求，下面这行的写法是：连续解构赋值+重命名
    let {data:{content:title}} = await axios.get('https://api.uomg.com/api/rand.qinghua?format=json')
    // 把请求回来的字符串，包装成一个对象
    let obj = {id:nanoid(),title}
    // 放到数组中
    talkList.unshift(obj)
  }
     //重要：返回可用对象
  return {talkList,getATalk}
})
```