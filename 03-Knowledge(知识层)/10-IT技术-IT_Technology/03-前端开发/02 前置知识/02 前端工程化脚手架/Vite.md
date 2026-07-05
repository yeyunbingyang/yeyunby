# Vite

相当于SpringBoot脚手架

兼容性注意

Vite 需要 [Node.js](https://nodejs.org/en/) 版本 18+ 或 20+。然而，有些模板需要依赖更高的 Node 版本才能正常运行，当你的包管理器发出警告时，请注意升级你的 Node 版本。

## 简介

官网：[https://cn.vitejs.dev](https://cn.vitejs.dev)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1737361251753-a755fadf-35cc-4d4e-a871-c671939322b1.png "null")

- 快速创建前端项目脚手架

- 统一的工程化规范：目录结构、代码规范、git提交规范 等

- 自动化构建和部署：前端脚手架可以自动进行代码打包、压缩、合并、编译等常见的构建工作，可以通过集成自动化部署脚本，自动将代码部署到测试、生产环境等；

## 实战

### 创建项目

```
npm create vite #根据向导选择技术栈
```

### 安装依赖

```
npm install #安装项目所有依赖

npm install axios #安装指定依赖到当前项目
npm install -g xxx # 全局安装
```

### 项目启动

```
npm run dev #启动项目
```

### 项目打包

```
npm run build #构建后 生成 dist 文件夹
```

### 项目部署

- 前后分离方式：需要把 dist 文件夹内容部署到如 nginx 之类的服务器上。

- 前后不分离方式：把 dist 文件夹内容复制到 SpringBoot 项目 `resources` 下面