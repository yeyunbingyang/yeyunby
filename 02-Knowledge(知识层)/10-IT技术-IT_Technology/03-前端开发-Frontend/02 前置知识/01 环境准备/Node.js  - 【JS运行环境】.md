推荐使用：nvm管理NodeJS

# NodeJS是什么？

简单的说 Node.js 就是运行在服务端的 JavaScript。

**作用**

在开发中，安装Node.js有许多好处：

1. **运行JavaScript代码**：Node.js是一个JavaScript运行环境，它允许你在服务器端运行JavaScript代码。这意味着你可以使用同一种语言（JavaScript）来编写前端和后端代码，这可以提高开发效率。

2. **构建工具**：许多流行的JavaScript构建工具，如Webpack、Babel和Gulp，都需要Node.js来运行。这些工具可以帮助你自动化编译、打包、压缩和优化你的代码。

3. **NPM**：Node.js附带了Node Package Manager（NPM），这是世界上最大的软件包库。你可以使用NPM来安装、更新和管理你的项目所需的库和工具。

4. **开发服务器**：Node.js可以用来创建一个本地开发服务器，这样你就可以在本地环境中测试和调试你的网站或应用。

5. **全栈开发**：使用Node.js，你可以进行全栈开发，即同时处理前端和后端。这对于需要快速原型设计和开发的项目非常有用。

6. **实时应用**：Node.js非常适合开发需要实时双向通信的应用，如在线聊天、实时通知等。

7. **性能**：Node.js使用了V8 JavaScript引擎，这是一款高性能的JavaScript引擎，可以提供快速的运行速度。

因此，无论你是前端开发者，还是全栈开发者，安装Node.js都是一个很好的选择。

在前端开发中，许多流行的框架和库需要Node.js环境，主要包括：

Vue.js：Vue.js是一个用于构建用户界面的JavaScript框架。在Vue.js的开发过程中，需要Node.js来运行开发服务器，进行模块打包，以及管理项目依赖。  
React.js：React是一个用于构建用户界面的JavaScript库。创建React应用通常使用create-react-app这样的脚手架工具，这些工具需要Node.js环境来运行。

# NodeJS安装

## 1. 双击资料中提供的安装包

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369319-8baf5dd4-84d6-4026-93a9-280d95afab46.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369388-a72b9bb3-0646-453b-9935-734251f5812b.png "null")

## 2. 选择安装目录

选择安装到一个，没有中文，没有空格的目录下（新建一个文件夹NodeJS）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369452-b8a16d0a-6607-4eaa-9ffe-3595ed4d0357.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369509-2a639087-1833-4347-a824-17c4dcfe1b1a.png "null")

## 3. 验证NodeJS环境变量

NodeJS 安装完毕后，会自动配置好环境变量，我们验证一下是否安装成功，通过： node -v

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369572-f6a39f64-001b-4d64-9007-abc7691be930.png "null")

## 4. 配置npm的全局安装路径

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369691-b3421658-ae03-43fa-ab67-7c06c41393f5.png)

使用管理员身份运行命令行，在命令行中，执行如下指令：

```
npm config set prefix "D:\IT\software\NodeJS"
```

注意：E:\develop\NodeJS 这个目录是NodeJS的安装目录

## 5. 切换npm的淘宝镜像

使用管理员身份运行命令行，在命令行中，执行如下指令：

```
npm config set registry https://registry.npm.taobao.org
```

## 6. 安装Vue-cli

使用管理员身份运行命令行，在命令行中，执行如下指令：

```
npm install -g @vue/cli
```

这个过程中，会联网下载，可能会耗时几分钟，耐心等待。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358369633-2f259b2a-1199-4632-82ad-265ed3bd67d0.png "null")

# 相关资料

[https://www.runoob.com/nodejs/nodejs-tutorial.html](https://www.runoob.com/nodejs/nodejs-tutorial.html)