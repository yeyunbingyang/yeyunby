

**学习目标：**

- 掌握WXML获取节点信息的用法

- 知道如何修改 uni-ui 扩展组件的样式

- 掌握 uniForm 表单验证的使用方法

- 能够在 uni-app 中使用自定义字体图标

### 一、uni-app 基础知识

uni-app 是组合了 Vue 和微信小程序的相关技术知识，要求大家同时俱备 Vue 和原生小程序的开发基础。

#### 1.1 节点信息

在此再次强调一下原生小程序中并没有 DOM 操作相关的内容，也因此在 uni-app 中也是无法对 DOM 进行操作的，但在实际开发过程中是有获取节点信息，如宽高、位置等信息的需求的，这一节就来学习在 uni-app 中如何获取节点的宽高及位置等信息。

##### 1.1.1 创建查询器

在网页中可以直接使用 `document.querySelector` 来查找 DOM 节点，在 uni-app 或小程序中则没有这样一个方法，取而代之的是调用 API `uni.createSelectorQuery` 创建一个查询实例（查询器），进而调用该实例的方法来查询页面中的节点元素。

```
<!-- pages/wiki/index.vue -->
<script setup>
  import { onMounted } from 'vue'
    
  // 在生命周期中调用
  onMounted(() => {
    // 节点查询器（实例）
    const selectorQuery = uni.createSelectorQuery()
        console.log(selectorQuery)
  })
</script>

<template>
  <view class="container">
    <view class="box">获取这个盒子的宽高、位置等信息</view>

  </view>

</template>

<style lang="scss">
  page {
    padding: 30rpx;
  }

  .box {
    width: 300rpx;
    height: 300rpx;
    margin-top: 40rpx;
    background-color: pink;
  }
</style>
```

注意事项：

1. 需要在 `onMounted` 或 `onReady` 生命周期中调用

2. 选择自定义组件中的节点时，需要调用 `in` 方法并传入当前页面实例（后面会例子来演示）

##### 1.1.2 节点对象

在查询节点时分成 3 种情形，获取到的结果为节点信息对象（NodesRef）

- `select` 根据选择器的要求，只查找符合条件的第一个节点，结果是一个对象

- `selectAll` 根据选择器的要求，查找符合条件的全部节点，结果是一个对象数组

- `selectViewport` 特指获取视口，查找视口的尺寸、滚动位置等信息

```
<script setup>
  import { onMounted } from 'vue'

  onMounted(() => {
    // 1. 节点查询器（实例）
    const selectorQuery = uni.createSelectorQuery()
    
    // 2. 查找节点

    // 2.1 查找单个节点
    selectorQuery.select('.box').boundingClientRect((rect) => {
      // 获取宽高和位置
      console.log(rect)
    })

    // 2.2 查找全部节点
    selectorQuery.selectAll('.box').boundingClientRect((rects) => {
      // 获取宽高和位置
      console.log(rects)
    })

    // 2.3 查找视口信息
    selectorQuery.selectViewport().boundingClientRect((rect) => {
      console.log(rect)
    })

    // 3. 执行请求结果
    selectorQuery.exec()
  })
</script>

<template>
  <view class="container">
    <view class="box">获取这个盒子的宽高、位置等信息</view>

    <view class="box"> 类选择器名称一样的另一个盒子 </view>

  </view>

</template>

<style lang="scss"></style>
```

注意事项：

1. 不执行 `exec` 方法，将获取不到任何的节点信息

2. 有多个查询步骤时，在结尾只执行一次 `exec` 即可，避免重复查询

3. `exec` 方法代表执行结束，因此务必保证最后再调用

##### 1.1.3 节点信息

节点信息对象中包含了若干的信息，根据需要调用不同的方法进行获取：

1. `boundingClientRect` 节点的宽高及位置，**长度单位是** `px`

2. `scrollOffset` 节点滚动的位置，仅支持 `scroll-view` 组件或页面（ viewport）

```
<script setup>
  import { onMounted } from 'vue'

  onMounted(() => {
    // 1. 节点查询器（实例）
    const selectorQuery = uni.createSelectorQuery()
    
    // 2. 查找节点

      // 省略了部分代码

    // 2.3 查找视口信息
    selectorQuery.selectViewport().boundingClientRect((rect) => {
      console.log(rect)
    })
    
    selectorQuery.selectViewport().scrollOffset((offset) => {
      console.log(offset)
    })

    // 3. 执行请求结果
    selectorQuery.exec()
  })
</script>

<template>
  <view class="container">
    <view class="box">获取这个盒子的宽高、位置等信息</view>

    <view class="box"> 类选择器名称一样的另一个盒子 </view>

  </view>

</template>

<style lang="scss"></style>
```

注意事项：

1. 在获取元素的位置时是按已定位的祖先元素为参考，即大家平时理解的“子绝父相”方式

2. 元素未定位时参视口（viewport）为参考

#### 1.2 自定义组件

在 uni-app 中自定义组件的定义与 Vue 组件基本一致，不要参照原生小程序方式来定义组件。

##### 1.2.1 easycom组件规范

easycom 是 uni-app 自定义的加载组件的规范，按该规范定义的组件可以实现自动导入，其规范要求如下：

1. 安装在项目根目录的 `components` 目录下，并符合 `components/组件名称/组件名称.vue`

2. 安装在 uni_modules 目录下，路径为 `uni_modules/插件ID/components/组件名称/组件名称.vue`

大家回忆一下扩展组件 uni ui 是不是就是在没有引入的情况下自动导入的，其原因就是符合 easycom 组件规范。

##### 1.2.2 custom-tabs

标签页（tabs）的切换在开发中是经常会使用到的一种交互方式，【优医咨询】项目就用到这种交互方式，接下来我们自已封装一个标签页组件，按着 easycom 的规范创建组件目录及文件：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748933409916-1cc1de58-1a41-4f46-9911-9ba4bf78002a.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748933410021-70730bb2-1dc6-4b3c-b62a-df4eda4ceb27.png "null")

1. `custom-tabs` 组件布局

接下来将上次课中完成的 tabs 部分的布局代码迁移到当前组件中：

```
<view class="custom-tabs">
  <view class="custom-tabs-bar active">
    <text class="tabbar-text">关注</text>

  </view>

  <view class="custom-tabs-bar">
    <text class="tabbar-text">推荐</text>

  </view>

  <view class="custom-tabs-bar">
    <text class="tabbar-text">护肤</text>

  </view>

  <view class="custom-tabs-bar">
    <text class="tabbar-text">减脂</text>

  </view>

  <view class="custom-tabs-bar">
    <text class="tabbar-text">饮食</text>

  </view>

  <view class="custom-tabs-cursor"></view>

</view>
```

```
// 自定义tabbar
.custom-tabs {
  display: flex;
  position: relative;
  padding: 0 30rpx;
}

.custom-tabs-bar {
  height: 80rpx;
  line-height: 80rpx;
  color: #979797;
  padding-right: 30rpx;
  position: relative;

  &.active {
    color: #121826;
    font-weight: 500;
  }
}

.tabbar-text {
  font-size: 30rpx;
}

.custom-tabs-cursor {
  position: absolute;
  bottom: 3px;
  left: 20px;

  width: 20px;
  height: 2px;
  border-radius: 2px;
  background-color: #2cb5a5;
  transition: all 0.3s ease-out;
}
```

2. 引用 `custom-tabs` 组件，**由于符合 easycom 组件规范，可以省略组件的导入步骤**

```
<!-- pages/index/index.vue -->
<template>
  ...
  <!-- 信息流 -->
  <view class="doctor-feeds">
    <custom-tabs></custom-tabs>

  </view>

</template>
```

3. 自定义组件属性，允许以属性的方式向组件传入数据

- `list` 数据类型为对象数组，初始值为 `[]`

- `list` 数组中的对象单元结构为 `{label: '', rendered: false}`

```
<!-- components/custom-tabs/custom-tabs.vue -->
<script setup>
  // 接收组件外部传入的数据
  const customTabsProps = defineProps({
    list: {
      type: Array,
      default: [],
    },
  })
</script>

<template>
  <view class="custom-tabs">
    <view
      v-for="tab in customTabsProps.list"
      :key="tab.label"
      class="custom-tabs-bar active"
    >
      <text class="tabbar-text">{{ tab.label }}</text>

    </view>

    <view class="custom-tabs-cursor"></view>

  </view>

</template>
```

首页面中引入组件时为 `custom-tabs` 组件传入数据

```
<!-- pages/index/index.vue -->
<script setup>
  import { ref } from 'vue'
  // 获取安全区域尺寸
  const { safeAreaInsets } = uni.getSystemInfoSync()

  // 定义tabs组件的数据
  const feedTabs = ref([
    { label: '关注', rendered: true },
    { label: '推荐', rendered: false },
    { label: '减脂', rendered: false },
    { label: '饮食', rendered: false },
  ])
</script>

<template>
  ...
  <!-- 信息流 -->
  <view class="doctor-feeds">
    <custom-tabs :list="feedTabs"></custom-tabs>

  </view>

</template>
```

4. 点击切换交互，此步骤要完成两个操作：一个是 tab 的高亮显示，另一个是指示游标位置的移动

先来看切换 tab 的高亮显示:

- 监听点击事件

- 根据点击元素的索引值来区分当前需要高亮的 tab 元素

- 高亮显示样式的类名为 `active`

```
<!-- components/custom-tabs/custom-tabs.vue -->
<script setup>
  import { ref } from 'vue'

  // 接收组件外部传入的数据
  const customTabsProps = defineProps({
    list: {
      type: Array,
      default: [],
    },
  })

  // 初始默认第一个 tab 高亮
  const tabIndex = ref(0)
  // 用户点击 tab
  function onTabChange(index, tab) {
    // 显示/隐藏组件
    tabIndex.value = index
  }
</script>

<template>
  <view class="custom-tabs">
    <view
      v-for="(tab, index) in customTabsProps.list"
      :key="tab.label"
      @click="onTabChange(index, tab)"
      :class="{ active: tabIndex === index }"
      class="custom-tabs-bar"
    >
      <text class="tabbar-text">{{ tab.label }}</text>

    </view>

    <view class="custom-tabs-cursor"></view>

  </view>

</template>
```

再来看指示游标的位置移动，实现此交互功能需要获取用户点击元素的位置和尺寸，动画效果是通过 css 的过渡（transition）实现的。

- 获取每个 tab 的宽度和位置，此处的难点是要计算每个 `tabbar-text` 相对于 `custom-tabs` 盒子的位置

- 计算游标的位置，根据布局结构看 `custom-tabs-cursor` 的定位是参照 `custom-tabs`

```
<!-- components/custom-tabs/custom-tabs.vue -->
<script setup>
  import { ref, onMounted, getCurrentInstance, computed } from 'vue'

  // 接收组件外部传入的数据
  const customTabsProps = defineProps({
    list: {
      type: Array,
      default: [],
    },
  })

  // 初始默认第一个 tab 高亮
  const tabIndex = ref(0)
  // 记录节点信息，宽度和位置
  const tabBarRect = ref([])

  // 生命周期
  onMounted(() => {
    // 在组件中应用，获取组件内部节点信息时需要调用 in 方法
    // 传入当页面实例，通过 getCurrentInstance 获取，相当于选项 API 中的 this
    const selectorQuery = uni.createSelectorQuery().in(getCurrentInstance())

    // 查找【所有节点】信息，用 selectAll 方法
    selectorQuery
      .selectAll('.custom-tabs, .tabbar-text')
      .boundingClientRect(([parent, ...data]) => {
        // 记录每个 tab 文字宽度和位置
        tabBarRect.value = data.map(({ width, left }) => {
          return { left: left - parent.left, width }
        })
      })

    // 执行节点查询
    selectorQuery.exec()
  })

  // 计算游标的位置
  const cursorPosition = computed(() => {
    if (tabBarRect.value.length === 0) return
    const { width, left } = tabBarRect.value[tabIndex.value]
    // 计算游标要居中显示
    return left + (width - 20) / 2
  })

  // 用户点击 tab
  function onTabChange(index, tab) {
    // 显示/隐藏组件
    tabIndex.value = index
  }
</script>

<template>
  <view class="custom-tabs">
    <view
      v-for="(tab, index) in customTabsProps.list"
      :key="tab.label"
      @click="onTabChange(index, tab)"
      :class="{ active: tabIndex === index }"
      class="custom-tabs-bar"
    >
      <text class="tabbar-text">{{ tab.label }}</text>

    </view>

    <view
      class="custom-tabs-cursor"
      :style="{ left: cursorPosition + 'px' }"
    ></view>

  </view>

</template>
```

注意事项：通过 selectorQuery.selectAll 获取到的节点的位置和宽高时长度单位是 `px` ，不是 `rpx`

5. 自定义事件，定义事件的目的是通知组件外部，组件内部的 tab 发生了切换

- 定义事件名称

- 触发事件并传递数据

```
<!-- components/custom-tabs/custom-tabs.vue -->
<script setup>
  import { ref, onMounted, getCurrentInstance, computed } from 'vue'

    // 省略前面步骤的代码...

  // 自定义事件
  const customTabsEmit = defineEmits(['click'])

  // 省略前面步骤的代码...

  // 用户点击 tab
  function onTabChange(index, tab) {
    // 显示/隐藏组件
    tabIndex.value = index
    // 触发自定义事件
    customTabsEmit('click', { index, ...tab })
  }
</script>

<template>
...
</template>
```

首页面中引入组件时为 `custom-tabs` 组件时监听 `click` 事件

```
<!-- pages/index/index.vue -->
<script setup>
  import { ref } from 'vue'
  // 获取安全区域尺寸
  const { safeAreaInsets } = uni.getSystemInfoSync()

  // 定义tabs组件的数据
  const feedTabs = ref([
    { label: '关注', rendered: true },
    { label: '推荐', rendered: false },
    { label: '减脂', rendered: false },
    { label: '饮食', rendered: false },
  ])

  // 监听 custom-tabs 组件的变化
  function onFeedTabChange(ev) {
    console.log(ev)
  }
</script>

<template>
  ...
  <!-- 信息流 -->
  <view class="doctor-feeds">
    <custom-tabs :list="feedTabs" @click="onFeedTabChange"></custom-tabs>

  </view>

</template>
```

##### 1.2.3 custom-sticky

在页面滚动过程中常常要求实现某个节点能固定在距离页面顶部的某个位置，我们称这种效果为吸顶，为了方便以后重复使用吸顶的效果，我们来封装一个组件，核心实现思路为组件插槽 `slot` 和 `postion: sticky`。

1. 按 easycom 组件创建组件 `custom-sticky`

2. 搭建基本结构并定义插槽

```
<!-- components/custom-sticky/custom-sticky.vue -->
<script setup></script>

<template>
  <view class="custom-sticky">
    <slot></slot>

  </view>

</template>

<style lang="scss">
  .custom-sticky {
    position: sticky;
    z-index: 100;
    top: 0;
  }
</style>
```

3. 允许自定义距离顶部的距离和组件的背景颜色，通过自定义属性方式传入数据

```
<!-- components/custom-sticky/custom-sticky.vue -->
<script setup>
  import { computed } from 'vue'

  // 接收组件外部传入的数据
  const stickyProps = defineProps({
    offsetTop: {
      type: [String, Number],
      default: 0,
    },
    backgroundColor: {
      type: String,
      default: '#fff',
    },
  })

  // 自定义组件样式
  const stickStyle = computed(() => {
    return {
      paddingTop: stickyProps.offsetTop,
      backgroundColor: stickyProps.backgroundColor,
    }
  })
</script>

<template>
  <view :style="stickStyle" class="custom-sticky">
    <slot></slot>

  </view>

</template>

<style lang="scss">
  .custom-sticky {
    position: sticky;
    z-index: 100;
    top: 0;
  }
</style>
```

在首页面的 `custom-tabs` 组件上应用吸顶的效果

```
<!-- pages/index/index.vue -->
<script setup>
  import { ref } from 'vue'
  // 获取安全区域尺寸
  const { safeAreaInsets } = uni.getSystemInfoSync()

  // 定义tabs组件的数据
  const feedTabs = ref([
    { label: '关注', rendered: true },
    { label: '推荐', rendered: false },
    { label: '减脂', rendered: false },
    { label: '饮食', rendered: false },
  ])

  // 监听 custom-tabs 组件的变化
  function onFeedTabChange(ev) {
    console.log(ev)
  }
</script>

<template>
  ...
  <!-- 信息流 -->
  <view class="doctor-feeds">
    <custom-sticky :offset-top="safeAreaInsets.top + 'px'">
      <custom-tabs :list="feedTabs" @click="onFeedTabChange"></custom-tabs>

    </custom-sticky>

  </view>

</template>
```

注意事项：

在设置吸顶距离时使用的是 `padding-top` 属性，而不是 `top` ，原因是这样可以避免刘海屏或灵动岛部分无法被覆盖的情况。

但上述设置会导致 `custom-sticky` 组件默认情况间距变大，为了解决这个问题我们采取这样一个技巧，通过 为`margin-top` 指定一个负值，将 `padding-top` 的间距抵消。

```
<template>
  ...
  <!-- 信息流 -->
  <view :style="{ marginTop: -safeAreaInsets.top + 'px' }" class="doctor-feeds">
    <custom-sticky :offset-top="safeAreaInsets.top + 'px'">
      <custom-tabs :list="feedTabs" @click="onFeedTabChange"></custom-tabs>

    </custom-sticky>

  </view>

</template>
```

这种处理方式虽不是很优雅，但相对算是比较高效的方式了，省去了监听滚动的事件，**更重要的是在自定义组件内部很难监听页面的滚动。**

##### 1.2.4 组件样式隔离

在**原生小程序中**自定义组件中如果引用其它的自定义组件时，通过 `:deep` 也无法对组件内部样式进行修改，通过设置原生小程序的[样式隔离](https://zh.uniapp.dcloud.io/tutorial/vue-api.html#%E5%85%B6%E4%BB%96%E9%85%8D%E7%BD%AE)可以解决这个问题。

具体的设置方式如下代码所示：

```
<script setup>
    // 组件式 setup 语法糖
</script>

<script>
  // 选项式
  export default {
    options: {
      styleIsolation: 'shared',
    },
  }
</script>
```

可以同时在 vue 组件中使用选项式和组合式 setup 语法糖。

创建符合 easycom 组件规范的组件 `custom-form` ，以表单相关组件为例来进行演示：

```
<!-- components/custom-form/custom-form.vue -->
<template>
  <uni-forms label-width="0">
    <uni-forms-item>
      <uni-easyinput
        type="text"
        :clearable="false"
        placeholder="请输入手机号"
      />
    </uni-forms-item>

    <uni-forms-item>
      <uni-easyinput
        type="password"
        :clearable="false"
        placeholder="请输入密码"
      />
    </uni-forms-item>

    <uni-forms-item>
      <uni-easyinput type="textarea" :clearable="false" />
    </uni-forms-item>

    <uni-forms-item>
      <label style="display: flex; align-items: center" class="radio">
        <radio style="transform: scale(0.7)" value="" />
        <text>我已同意用户协议及隐私协议</text>

      </label>

    </uni-forms-item>

  </uni-forms>

  <button type="primary">提交</button>

</template>
```

在修改输入框 `uni-easyinput` 组件内部样式时就必须要指定 `styleIsolation: 'shared'` 否则在小程序中样式并不会生效。

```
<!-- components/custom-form/custom-form.vue -->
<script>
  export default {
    options: {
      styleIsolation: 'shared',
    },
  }
</script>

<style lang="scss">
  .uni-button {
    background-color: #2cb5a5;
  }

  :deep(.uni-easyinput__content-textarea) {
    padding: 5px 10px;
  }

  :deep(.uniui-eye-filled),
  :deep(.uniui-eye-slash-filled) {
    color: #c0c4cc !important;
  }
</style>
```

#### 1.3 uniForms 表单验证

表单数据的验证在开发中是最常处理的逻辑之一，然而原生小程序组件关于表单数据的获取的验证的能力非常弱，此时要么自行封装组件，要么使用第三方组件库，庆幸的是 uni-app 扩展组件 uni ui 提供了表单数据的获取的验证的能力，这节我们来学习 uniForms 的使用。

##### 1.3.1 表单数据

大家是否记得原生小程序组件中关于表单数据的获取只能支持[简易双向数据绑定](https://developers.weixin.qq.com/miniprogram/dev/framework/view/two-way-bindings.html)，由于这个局限性，在 uni-app 开发中经常使用 `uni-easyinput` 增强组件替代 `input` 和 `textarea` ，通过 `v-model` 来获取表单的数据：

```
<!-- components/custom-form/custom-form.vue -->
<script setup>
  import { ref } from 'vue'

  // 表单数据
  const formData = ref({
    mobile: '13212345678',
    password: 'abc12345',
    alt: '关于我的描述',
  })
</script>

<template>
  <uni-forms label-width="0">
    <uni-forms-item>
      <uni-easyinput
        type="text"
        :clearable="false"
        :input-border="false"
        v-model="formData.mobile"
        placeholder="请输入手机号"
      />
    </uni-forms-item>

    <uni-forms-item>
      <uni-easyinput
        type="password"
        :clearable="false"
        :input-border="false"
        v-model="formData.password"
        placeholder="请输入密码"
      />
    </uni-forms-item>

    <uni-forms-item>
      <uni-easyinput
        type="textarea"
        v-model="formData.alt"
        :clearable="false"
        :input-border="false"
      />
    </uni-forms-item>

    <uni-forms-item>
      <label style="display: flex; align-items: center" class="radio">
        <radio color="#2cb5a5" style="transform: scale(0.7)" value="" />
        <text>我已同意用户协议及隐私协议</text>

      </label>

    </uni-forms-item>

  </uni-forms>

  <button class="uni-button" type="primary">提交</button>

</template>
```

##### 1.3.2 验证规则

在对表单数据进行验证时不同的表单项，验证规则各不相同，在 uniForms 中通过 `rules` 属性来指定验证规则，语法格式如下：

```
<!-- components/custom-form/custom-form.vue -->
<script setup>
    import { ref } from 'vue'

  // 表单数据
  const formData = ref({
    mobile: '13212345678',
    password: 'abc12345',
    alt: '关于我的描述',
  })
  
  // 表单验证规则
  const formRules = {
    mobile: {
      rules: [
        { required: true, errorMessage: '请填写手机号码' },
        { pattern: '^1\\d{10}$', errorMessage: '手机号码格式不正确' },
      ],
    },
    password: {
      rules: [
        { required: true, errorMessage: '请输入密码' },
        { pattern: '^[a-zA-Z0-9]{8}$', errorMessage: '密码格式不正确' },
      ],
    },
  }
</script>
```

- `mobile`、`password` 表示要验证的数据名称，**该名称需要在组件中定义（后面步骤会介绍）**

- `rules` 表示具体验证数据的规则，规则可以有多条

- `required` 表示是否必填（不能为空）

- `pattern` 自定义正则表达式进行验证，正则中的 `\` 需要进行转义，即要写成 `\\`

- `errorMessage` 数据验证不合法时的提示文字

验证规则定义好之后，还有3件事需要处理：一是通过 `rules` 应用规则，二是为通过 `name` 为待验证数据命名，三是通过 `model` 指定验证的数据

```
<!-- components/custom-form/custom-form.vue -->
<template>
  <uni-forms label-width="0" :model="formData" :rules="formRules">
    <uni-forms-item name="mobile">
      <uni-easyinput
        type="text"
        :clearable="false"
        :input-border="false"
        v-model="formData.mobile"
        placeholder="请输入手机号"
      />
    </uni-forms-item>

    <uni-forms-item name="password">
      <uni-easyinput
        type="password"
        :clearable="false"
        :input-border="false"
        v-model="formData.password"
        placeholder="请输入密码"
      />
    </uni-forms-item>

    <uni-forms-item name="alt">
      <uni-easyinput
        type="textarea"
        v-model="formData.alt"
        :clearable="false"
        :input-border="false"
      />
    </uni-forms-item>

    <uni-forms-item>
      <label style="display: flex; align-items: center" class="radio">
        <radio color="#2cb5a5" style="transform: scale(0.7)" value="" />
        <text>我已同意用户协议及隐私协议</text>

      </label>

    </uni-forms-item>

  </uni-forms>

  <button class="uni-button" type="primary">提交</button>

</template>
```

##### 1.3.3 触发验证

在用户点击提交按钮时调用 uniForms 的方法来执行数据的验证：

1. 通过 ref 获取组件实例

2. 调用组件暴漏出来的方法

```
<!-- components/custom-form/custom-form.vue -->
<script setup>
  import { ref } from 'vue'

  // 组件 ref
  const formRef = ref()

     // 省略前面部分代码...

  // 表单提交
  async function onFormSubmit() {
    try {
      // 执行表单的验证
        await formRef.value.validate()
    } catch(error) {
      console.log(err)
    }
  }
</script>

<template>
  <uni-forms label-width="0" ref="formRef" :model="formData" :rules="formRules">
    ...
  </uni-forms>

  <button class="uni-button" @click="onFormSubmit" type="primary">提交</button>

</template>
```

#### 1.4 自定义字体图标

扩展组件中的 `uni-icons` 内置了许多的图标，在内置的图标不能满足要求时还可以使用自定义图标。

##### 1.4.1 单色图标

自定义单色图标的制作和使用与网页面几乎是一致的，首先在 [iconfont.cn](https://www.iconfont.cn/) 平台制作字体图标，其次下载字体文件及配套的样式文件。

```
// static/fonts/iconfont.scss
@font-face {
  font-family: 'iconfont';
  // 修改这里字体文件的引入路径，只保留 .ttf 格式字体文件即可（可以减少文件体积）
  src: url('/static/fonts/iconfont.ttf') format('truetype');
}

.iconfont {
  font-family: 'iconfont' !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

```
<!-- App.vue -->
<style lang="scss">
  // 将下载的字体文件及样式表放到 static/fonts 目录中
  // 将 iconfont.css 改成 iconfont.scss
  @import '@/static/fonts/iconfont.scss';
</style>
```

在 App.vue 中引入字体文件后可以在任何页面使用字体图标了，使用的方式也网页中是一样的：

```
<!-- pages/my/index.vue -->
  <view class="icons rows">
    <!-- 自定义字体图标 -->
    <text class="iconfont icon-done"></text>

    <text class="iconfont icon-box"></text>

  </view>
```

**上述用法是常规方式使用自定义图标，除此之个 uni-icons 也支持使用自定义图标：**

```
<!-- pages/my/index.vue -->
<view class="icons rows">
  <!-- 常规方式使用自定义字体图标 -->
  <text class="iconfont icon-done"></text>

  <text class="iconfont icon-box"></text>

  <!-- uni-icons 方式使用自定义字体图标 -->
  <uni-icons size="30" custom-prefix="iconfont" type="icon-done" />
  <uni-icons size="30" custom-prefix="iconfont" type="icon-box" />
</view>

<style lang="scss">
  page {
    padding: 30px;
    box-sizing: border-box;
  }

  .iconfont {
    font-size: 30px;
  }
</style>
```

- `custom-prefix` 指定自定义图标的公共类名

- `type` 指定自定义图标的名称

注意事项：原生小程序中是不支持引入本地字体图标文件，必须为网络地址或base64，在使用 uni-app 时引入的本地字体文件在打包后会处理成 base64，因此使用时可以引入本地字体文件。

##### 1.4.2 多色图标

多色图标目通过 svg 来支持的，然而微信小程序目前还不支持 svg 格式图片，所以在 uni-app 中多色图标只能用普通的图片来代替。

虽然多色图标是用普通图片来实现的，但是我们可以让其的使用方式变得方便一些，即从形式上看仍是以字体图标的方式来使用。

1. 安装 [iconfont-tools](https://github.com/HuaRongSAO/iconfont-tools) 工具来处理多色图标，将图标转找成 base64 格式的图片

```
npm install -g iconfont-tools
```

2. 通过命令行切换到**多色字体文件所在目录**，执行 `iconfont-tools`

```
iconfont-tools
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1748933410131-a9a95af1-d3b7-4a3a-abb8-92b4afd56651.png "null")

根据引导生成支持多色图标的文件，每个步骤中指定的名称自已可任意指定。

3. 把生成的字体文件 `color-fonts.css` 放到项目中，然后在 App.vue 文件中全局引入

```
<!-- App.vue -->
<style lang="scss">
  // 将下载的字体文件及样式表放到 static/fonts 目录中
  // 将 iconfont.css 改成 iconfont.scss
  @import '@/static/fonts/iconfont.scss';
  // 多色图标
  @import 'color-fonts.scss';
</style>
```

```
<!-- pages/my/index.vue -->
<view class="icons rows">
  <!-- 常规方式使用自定义字体图标 -->
  <text class="icon-symbol icon-symbol-tool-03"></text>

  <!-- uni-icons 方式使用自定义字体图标 -->
  <uni-icons custom-prefix="icon-symbol" type="icon-symbol-tool-03" />
</view>

<style lang="scss">
  page {
    padding: 30px;
    box-sizing: border-box;
  }

  .icon-symbol {
    width: 30px;
    height: 30px;
  }
</style>
```

注意事项：转换后的图片虽然使用方式上与字体图标相似，但是本质是是 base64 格式的图片，因此无法修改颜色，并且修改尺寸要修改其宽高来实现。

#### 1.5 生命周期

uni-app 中支持3种类型的生命周期函数，分别是小程序应用级生命周期、小程序页面级生命周期，Vue 生命周期。

##### 1.5.1 应用级

|   |   |   |   |
|---|---|---|---|
|名称|应用是否可用|页面是否可用|组件是否可用|
|onLaunch|是|否|否|
|onShow|是|否|否|
|onHide|是|否|否|

可以看出小程序应用级的生命周期只能用在应用级别，即只能在 App.vue 中应用。

##### 1.5.2 页面级

|   |   |   |   |
|---|---|---|---|
|名称|应用是否可用|页面是否可用|组件是否可用|
|onLoad|否|是|否|
|onShow|否|是|否|
|onReady|否|是|否|
|onHide|否|是|否|

可以看出小程序页面级的生命周期只能用在页面中，组件中是不支持的。

##### 1.5.3 组件级

|   |   |   |   |
|---|---|---|---|
|名称|应用是否可用|页面是否可用|组件是否可用|
|beforeCreate|是|是|是|
|created|是|是|是|
|beforeMount|是|是|是|
|mounted|是|是|是|
|beforeUpdate|是|是|是|
|updated|是|是|是|
|activated|仅H5|仅H5|仅H5|
|deactivated|仅H5|仅H5|仅H5|
|beforeDestoryed|是|是|是|
|destoryed|是|是|是|

当然上表是不需要大家死记硬背的，大家记这样一个原则即可：

- 应用生命周期和页面生命周期以**小程序**的生命期为准

- 自定义组件生命周期**以 Vue 的**生命周期为准

结合 Vue3 的 setup 语法使用【应用生命周期】和【页面生命周期】需要用到 `@dcloudio/uni-app` 包，**这个包不需要单独安装，HBuilder X 中内置已经包含，在项目代码中直接使用即可。**

```
<script setup>
  // Vue 组件生命周期
  import { onMounted } from 'vue'
  // 应用/页面生命周期（小程序生命周期）
  import { onLaunch, onLoad } from '@dcloudio/uni-app'
  
  // ...
</script>
```