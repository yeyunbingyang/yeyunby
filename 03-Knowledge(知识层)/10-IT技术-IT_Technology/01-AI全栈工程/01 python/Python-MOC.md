---
domain: IT_Technology
status: 稳定
summary: Python 知识体系导航，按语法核心/标准库/生态/代码库四域组织，17篇知识笔记通过 Dataview 自动聚合。
tags: [MOC, Python]
created: 2026-06-12
updated: 2026-06-12
---

# Python-MOC

> Python 知识地图，位于 `01-AI全栈工程` 子域下，笔记源自尚硅谷大模型技术之 Python V1.0。

## 目录结构

| 目录 | 定位 | 内容示例 |
|------|------|----------|
| [[01-语法核心]] | 语言基础 | 变量、运算符、流程控制、组合数据类型 |
| [[02 标准库]] | 官方标准库 | re、json、socket、threading、io |
| [[03 生态]] | 第三方包与框架 | 数据库驱动、FastAPI、爬虫、数据分析 |
| [[代码库]] | 实用代码与案例 | 综合案例-客户管理系统 |

## 知识笔记清单

### 01-语法核心（13 篇）

| 笔记 | 内容 |
|------|------|
| [[01 初始Python]] | 计算机组成、编程语言简史、Python 起源与特点 |
| [[快速入门]] | Python 安装、PyCharm 配置、第一个程序 |
| [[基础知识]] | 注释、变量、数据类型、进制转换、输入输出、运算符 |
| [[流程控制]] | 顺序、分支（if/elif/else）、循环（while/for） |
| [[容器数据类型]] | 字符串、列表、元组、字典、集合 |
| [[函数]] | 定义、参数、返回值、作用域、递归、匿名函数 |
| [[文件操作]] | 文件读写、目录操作、CSV/JSON |
| [[类和对象]] | 类定义、对象创建、构造方法、属性与方法 |
| [[三大特性]] | 封装、继承、多态 |
| [[案例-愤怒的小鸟]] | 面向对象综合案例 |
| [[错误和异常]] | 异常捕获、自定义异常、finally、with 上下文 |
| [[模块与包]] | 模块导入、包管理、pip、虚拟环境 |
| [[Python高级语法]] | 闭包、装饰器、迭代器、生成器、反射 |

### 02 标准库（3 篇）

| 笔记 | 内容 |
|------|------|
| [[进程与线程]] | 多进程、多线程、互斥锁、GIL、进程池线程池 |
| [[网络编程]] | TCP/UDP、Socket、HTTP 协议 |
| [[正则表达式]] | re 模块、元字符、匹配模式、实战案例 |

### 03 生态

> 待建设：爬虫、数据分析、Web 开发、自动化、数据库驱动

### 代码库

| 笔记 | 内容 |
|------|------|
| [[综合案例-客户管理系统]] | 客户 CRUD 管理系统完整实现 |

## 语法核心笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/01-语法核心"
SORT file.name ASC
```

## 标准库笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/02 标准库"
SORT file.name ASC
```

## 生态笔记

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/03 生态"
SORT file.name ASC
```

## 代码库

```dataview
TABLE summary, status
FROM "03-Knowledge(知识层)/10-IT技术-IT_Technology/01-AI全栈工程/01 python/代码库"
SORT file.name ASC
```

---

## 跨域关联

- [[运维云原生-MOC]] — 运维场景下 Python 实战笔记（位于 `01 运维云原生`）
- [[AI工程-MOC]] — 上级 MOC，AI 全栈工程总导航
- [[自动化-MOC]] — Python 自动化工具链
