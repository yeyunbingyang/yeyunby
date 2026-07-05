# 是什么

相当于Java的Maven

NPM（Node Package Manager）是随同NodeJS一起安装的包管理工具，它能解决NodeJS代码部署上的很多问题。以下是NPM的一些常见使用场景：

1. **安装包**：你可以使用`npm install <package_name>`命令来安装指定的包。如果你想要将包保存为项目的依赖，可以使用`npm install --save <package_name>`命令。

2. **更新包**：你可以使用`npm update`命令来更新项目的全部依赖包。

3. **卸载包**：你可以使用`npm uninstall <package_name>`命令来卸载指定的包。

4. **查看已安装的包**：你可以使用`npm list`命令来查看项目的所有依赖包。如果你想要查看全局安装的包，可以使用`npm list -g`命令。

5. **全局安装**：有时你可能需要全局安装一些包，通常是一些命令行工具或脚本。你可以使用`npm install -g <package_name>`命令来全局安装指定的包。

6. **运行脚本**：在`package.json`的`scripts`部分，你可以定义多个脚本命令。然后，你可以使用`npm run <script_name>`命令来运行这些脚本。

7. **初始化项目**：你可以使用`npm init`命令来初始化一个新的项目。这个命令会创建一个`package.json`文件，用于存储项目的元信息和依赖信息。

# 配置 npm

npm 是 js 的包管理器，就类似于 java 界的 maven，要确保它使用的是国内镜像

检查镜像

```
npm get registry
```

如果返回的不是 `https://registry.npm.taobao.org/`，需要做如下设置

```
npm config set registry https://registry.npm.taobao.org/
```

# 命令

- npm init： 项目初始化；

- npm init -y：默认一路yes，不用挨个输入信息【生成package.js文件】

- npm install 包名：安装js包到项目中（仅当前项目有效）。指定 **包名**，或者 **包名@版本号**

- npm install -g： 全局安装，所有都能用![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371087-eae19eaf-9cd9-4c92-bbce-4365969b1c98.png "null")

- 可以去 [npm仓库](https://www.npmjs.com/) 搜索第三方库

- npm update 包名：升级包到最新版本

- npm uninstall 包名：卸载包

- npm run：项目运行

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371168-b323a361-3ae3-4e7a-8fd8-d6d88a2fd1a4.png "null")

- 可以运行scripts部分内容【使用npm run 脚本名 】

```
{
  "name": "demo02-npm",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo '哈哈哈'",
    "dev": "node main.js",
    "build": "echo '正在打包...'"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "jquery": "^3.7.1"
  }
}
```

- 可以直接使用命令【node 脚本程序】直接运行对应脚本![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371226-fa90b5d9-8c50-4f3a-9e87-368e28939da2.png "null")

# 使用流程

- 项目创建：node环境 ==》 环境初始化 ==》 安装依赖 ==》运行项目

- 项目迁移：node环境 ==》 下载依赖 ==》运行项目

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371283-603525fd-ea79-4a5f-9f68-f4acbac060a0.png "null")

- node环境分享项目文件夹时，不要node_modles【包含下载的依赖】

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371339-ef9259f6-a6bd-4dea-aea3-62f5f6d83ff5.png "null")

- 删除node_modles文件夹【在package-lock.json依赖已经声明】

- 第三方也需要有node.js环境，运行下载依赖命令

```
npm install 
```

- 运行项目，根据脚本声明进行启动

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737358371398-7dc55f1e-aeb4-4491-a74c-48f6eff260aa.png "null")