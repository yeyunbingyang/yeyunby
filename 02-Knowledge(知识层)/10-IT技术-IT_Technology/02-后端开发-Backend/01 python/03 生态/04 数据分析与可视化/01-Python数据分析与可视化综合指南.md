---
title: Python数据分析与可视化（尚硅谷课程全笔记）
domain: IT_Technology
tags: [Python, 数据分析, NumPy, Pandas, Matplotlib, Seaborn, 尚硅谷, 课程笔记]
status: 稳定
created: 2026-06-20
updated: 2026-06-20
source: "尚硅谷数据分析课程：docx讲义 + pptx课件(70页) + 7个Jupyter Notebook + 9个数据集"
related: []
summary: "尚硅谷Python数据分析课程系统整理：涵盖理论框架、工具链、NumPy/Pandas/Matplotlib/Seaborn完整API对照、缺失值处理、时间序列、项目实战"
---

# Python 数据分析与可视化

> 尚硅谷「从数据分析基础到实战应用」课程配套笔记。
> 整合 **docx 讲义**（理论框架与详细说明）、**pptx 课件**（70页图表对比）和 **7个Jupyter Notebook**（227个可执行代码单元）。

## 知识体系总览

```
1. 数据分析概述
   1.1 为什么要学数据分析
   1.3 数据分析完整流程（收集→清洗→分析→可视化）
   1.4 工具链：NumPy（发动机）+ Pandas（手术刀）+ Matplotlib（翻译官）
   1.2 Anaconda 安装与环境配置

2. NumPy 数值计算基础
   2.2 ndarray 属性 / 创建 / 运算 / 索引
   2.3 统计函数（18 种统计量完整对照）
   2.4 广播机制与矩阵运算

3. Pandas 表格数据处理
   3.1 Series（一维带标签数组）
   3.2 DataFrame（二维表格）
   3.3 缺失值处理（dropna / fillna / interpolate）
   3.4 数据类型转换与内存优化
   3.5 排序、分组、合并

4. 数据分析与挖掘
   4.1 GroupBy 分组聚合（split→apply→combine）
   4.2 数据合并（concat / merge / join）
   4.3 透视表与交叉表
   4.4 时间序列分析

5. 数据可视化
   5.1 Matplotlib 基础图表
   5.2 Seaborn 统计可视化
   5.3 综合项目：房地产市场分析
```

## 源文件对照

| 源文件 | 对应章节 | 单元数 | 内容说明 |
|--------|----------|--------|----------|
| `1.numpy学习.ipynb` | [[#NumPy 数值计算基础]] | 63 | ndarray 属性/创建/运算/索引/广播/统计 |
| `2.series学习.ipynb` | [[#Pandas Series]] | 43 | 序列创建/索引/切片/运算/缺失值 |
| `3.DataFrame学习.ipynb` | [[#Pandas DataFrame]] | 39 | 创建/列操作/筛选/清洗/排序/分组 |
| `4.数据分析.ipynb` | [[#数据分析与挖掘]] | 41 | GroupBy/merge/concat/透视表/时间序列 |
| `5.matplotlib学习.ipynb` | [[#数据可视化]] | 12 | 折线/柱状/散点/直方图/饼图/子图 |
| `6.seaborn学习.ipynb` | [[#Seaborn 统计可视化]] | 13 | 分布图/分类图/热力图/pairplot |
| `7.房地产市场分析.ipynb` | [[#综合项目：房地产市场分析]] | 16 | 数据加载→清洗→特征→建模→评估 |
| `尚硅谷数据分析.docx` | 全部 | — | 课程大纲、概念详解、API对照表 |
| `尚硅谷数据分析.pptx` | 全部 | 70页 | 课堂演示、架构图、安装指引 |
| `代码/data/*.csv` | Pandas/项目 | 9个数据集 | 天气/销售/企鹅/房价等真实数据 |

---

## 数据分析概述

### 数据分析完整流程

> 摘自 docx 讲义第 1.1.3 节

数据分析的完整流程分为四个阶段：

**① 数据收集** — 数据从哪里来
公司数据库（SQL/NoSQL）、公开数据集（政府统计/科研数据）、手动爬取（网页内容采集）

**② 数据清洗** — 最耗时环节（约占总时间 70-80%）
- **缺失值**：Excel 里的空单元格。Pandas 用 `dropna()` 删除、`fillna()` 填充、`interpolate()` 插值
- **错误数据**：年龄填成 200 岁、工资填负数。用 IQR（四分位距法）检测异常值
- **格式混乱**：日期写成 "2023年1月1日" 和 "01/01/2023" 混用。用 `pd.to_datetime()` 统一格式

**③ 数据分析**
统计描述（均值、中位数、标准差） / 分组对比（男 vs 女用户消费差异） / 相关性分析

**④ 数据可视化**
一图胜千言：折线图看趋势变化 / 柱状图看类别对比 / 散点图看变量关联

### 传统方法 vs Python 数据分析

> 摘自 docx §1.1.1 — Excel vs Pandas 功能对照

| 场景 | 传统方法（Excel） | Python 数据分析 |
|------|-------------------|-----------------|
| 数据处理量 | 约 104 万行 | 内存允许即可 |
| 1000 名学生成绩排名 | 手动操作约 2 小时 | `df.sort_values("score")` 3 分钟 |
| 自动化程度 | 手动拖拽操作，难以复现 | 代码一键运行，完全可重复 |
| 列操作 | 手动复制粘贴 | `df["col"]` 代码化操作 |
| 缺失值处理 | 逐个单元格手动处理 | `dropna()`/`fillna()` 批量处理 |
| 分组聚合 | 手动建数据透视表 | `groupby().agg()` 一行代码 |
| 学习难度 | 简单（无需编程） | 需要基础 Python 知识 |

### 数据分析工具链

> 摘自 docx 讲义 §1.1.4

**核心三件套**

| 工具 | 作用 | 课程类比 |
|------|------|----------|
| **NumPy** | 高性能数值计算（矩阵/向量/随机数/统计） | 数据的「发动机」|
| **Pandas** | 表格数据处理（类似高级 Excel） | 数据的「手术刀」|
| **Matplotlib** | 数据可视化（底层绘图库） | 数据的「翻译官」|

> 典型工作流：**NumPy 处理数字 → Pandas 整理表格 → Matplotlib 画图展示**

**辅助工具**

- **Jupyter Notebook** — 交互式编程环境，实时显示代码和结果，图文混合笔记
- **Anaconda** — Python + 包管理器（Conda）+ 200+ 预装库 = 一键搭建环境
- **Git** — 代码版本控制，避免脚本丢失，支持多人协作

### Anaconda vs 原生 Python

> 摘自 docx 讲义 §1.2

| 对比维度 | Anaconda 方案 | 原生 Python + pip |
|----------|--------------|-------------------|
| 安装难度 | ⭐️ 一键安装所有工具 | ⭐️⭐️⭐️ 需手动装每个库 |
| 依赖管理 | Conda 自动解决依赖冲突 | pip 可能遇版本兼容问题 |
| 磁盘占用 | 较大（3GB+ 基础包） | 可按需安装（最小仅几十MB） |
| 适用场景 | 初学者/快速开始 | 开发者/精确控制环境 |
| 典型场景 | 学校教学/个人学习 | 生产服务器部署 |

> "如果你希望像用手机 APP 一样简单，选 Anaconda；如果像专业厨师需要定制厨房，选原生 Python。"

---

## NumPy 数值计算基础

> **源文件**：`1.numpy学习.ipynb`（63单元） | **docx**：第 2 章

### 2.1 ndarray 核心概念

NumPy（Numerical Python）是 Python 科学计算的基础库。核心数据结构 **ndarray**（N-dimensional array）具备三个关键设计理念：

1. **多维性**：可表达任意维度数组。Python List 需层层嵌套，ndarray 用 stride 实现高性能多维访问
2. **同质性**：所有元素同一类型。利用 C 语言底层实现和 SIMD 向量化指令，速度远超 Python 循环
3. **广播**：不同 shape 数组自动对齐运算。规则：从尾端比较维度，相等或其一为 1 允许广播

### 2.2 ndarray 属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `ndim` | 维度数（几维） | `arr.ndim → 2` |
| `shape` | 各维度大小 | `arr.shape → (3, 4)` |
| `size` | 元素总数 | `arr.size → 12` |
| `dtype` | 数据类型 | `arr.dtype → dtype('int64')` |

### 2.3 ndarray 创建

```python
import numpy as np

arr = np.array(5)  # 创建0维的ndarray数组
print(arr)
print('arr的维度：', arr.ndim)   # 数组的维度number of dimensions

arr = np.array([1, 2, 3])  # 创建1维的ndarray数组
print(arr)
print('arr的维度：', arr.ndim)   # 数组的维度number of dimensions

arr = np.array([ [1, 2, 3], [4, 5, 6]])  # 创建2维的ndarray数组
print(arr)
print('arr的维度：', arr.ndim)   # 数组的维度number of dimensions

arr = np.array([1, 'hello'])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)

arr = np.array([1, 2.5])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)

arr = np.array(1)
print(arr)
print('数组的形状：', arr.shape)
print('数组的维度：', arr.ndim)
print('元素的个数：', arr.size)
print('元素的数据类型：', arr.dtype)
print('元素的转置', arr.T)

arr = np.array([1, 2.5, 3])
print(arr)
print('数组的形状：', arr.shape)
print('数组的维度：', arr.ndim)
print('元素的个数：', arr.size)
print('元素的数据类型：', arr.dtype)
print('元素的转置', arr.T)
```

### 2.4 数组运算

与 Python List 不同，ndarray 的 `*` 是**逐元素乘法**。矩阵乘法用 `@` 或 `np.dot()`。
内置数学函数：`np.sqrt()` `np.exp()` `np.log()` `np.sin()` `np.cos()` `np.abs()` `np.round()`

```python
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('数组的形状：', arr.shape)
print('数组的维度：', arr.ndim)
print('元素的个数：', arr.size)
print('元素的转置', arr.T)

# 基础的创建方法
list1 = [4, 5, 6]
arr = np.array(list1,dtype=np.float64)
print(arr.ndim)  # 属性
print(arr)

# copy
arr1 = np.copy(arr)  # 元素跟原始的数组相同，但是不是一个数组了
print(arr1)
arr1[0] = 8
print(arr1)
print(arr)

# 预定义形状
# 全0  全1  未初始化  固定值
# 全0
arr = np.zeros((2,3),dtype=int)
print(arr)
print(arr.dtype)

arr = np.zeros((200,),dtype=int)
print(arr)

# 全1
arr = np.ones((5,8),dtype=int)
print(arr)

# 未初始化
arr = np.empty((2,3))
print(arr)

arr = np.empty((4, 2))
print(arr)

arr = np.full((3,4),2025)
print(arr)

arr1 = np.zeros_like(arr)
print(arr1)
arr1 = np.empty_like(arr)
print(arr1)
arr1 = np.ones_like(arr)
print(arr1)
arr1 = np.full_like(arr,2026)
print(arr1)
```

### 2.5 索引与切片

```python
# 等差数列 2 4 6 8 10
arr = np.arange(1, 51, 1) # start,end,step(步长）
print(arr)

# 等间隔数列
arr = np.linspace(0,100,5)
print(arr)

arr = np.linspace(0,100,5,dtype=int)
print(arr)
arr = np.arange(0,101, 25)
print(arr)

# 对数间隔数列
arr = np.logspace(0,4,3,base=2)
print(arr)

arr = np.linspace(0,4,3)
print(arr)

arr = np.logspace(0,4,3)
print(arr)

# 特殊矩阵
# 单位矩阵：主对角线上的数字为1，其他的数字为0
arr = np.eye(3,4,dtype=int)
print(arr)


# 对角矩阵：主对角线上非零的0，其他的数字为0
arr = np.diag([5,1,2,3])
print(arr)
```

### 2.6 形状操作与广播

```python
# 随机数组的生成
# 生成0到1之间的随机浮点数（均匀分布）
arr = np.random.rand(2,3)
print(arr)

# 生成指定范围区间的随机浮点数
arr = np.random.uniform(3, 6,(2,3))
print(arr)

# 生成指定范围区间的随机整数
arr = np.random.randint(3, 30,(2,3))
print(arr)

# 生成随机数列（正态分布）（-3到3之间）
# 两边小，中间大
arr = np.random.randn(2,3)
print(arr)

# 设置随机种子
np.random.seed(20)
arr = np.random.randint(1,10,(2,5))
print(arr)

arr = np.array([1,2,3],dtype='i8')
print(arr)

arr = np.array([1,0,127,0],dtype= np.int8)
print(arr)

# 一维数组的索引与切片
arr = np.random.randint(1,100,20)
print(arr)

print(arr[10])
print(arr[:]) # 获取全部的数据
print(arr[2:5])  # start:end+1 左包右不包
print(arr[slice(2,15,3)])  #start,end,step
print(arr[ (arr>10)  & (arr<70) ]) # 布尔索引
```

### 2.7 统计运算

> 摘自 docx 讲义 §2.3.3 — NumPy 18 种统计量完整对照

| 统计量 | NumPy 方法 | 常见用途 |
|--------|-----------|---------|
| 总和 | `np.sum()` | 总支出 / 总收入 |
| 计数 | `np.size` / `np.count_nonzero()` | 数据规模 / 非零元素 |
| 平均数 | `np.mean()` | 成绩均值 / 产品均价 |
| 中位数 | `np.median()` | 房价中位数 / 收入中位数 |
| 标准差 | `np.std()` | 正常范围分析 |
| 方差 | `np.var()` | 波动性 / 风险评估 |
| 最大值 / 最小值 | `np.max()` / `np.min()` | 最高温度 / 最低价格 |
| 分位数 | `np.quantile()` | 工资等级 / 分数线 |
| 百分位数 | `np.percentile()` | 分布边界标记 |
| 累积和 | `np.cumsum()` | 累计收益 / 增长曲线 |
| 累积积 | `np.cumprod()` | 复利计算 |
| 协方差 | `np.cov()` | 多元统计分析 |
| 相关系数 | `np.corrcoef()` | 特征选择 / 热度图 |
| 直方图 | `np.histogram()` | 分布分析 |
| 唯一值 | `np.unique()` | 类别统计 / 去重 |

> **axis 参数**：`axis=0` 按列统计，`axis=1` 按行统计。默认 `None` 对全体计算。

```python
# 二维数组的索引与切片
arr = np.random.randint(1,100,(4,8))
print(arr)

print(arr[1,3])  # 索引
print(arr[ 1,2:5])
print(arr[2][  arr[2] > 50 ])
print( arr[:,3] )

# 算术运算
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)

c = [1, 2, 3]
d = [4, 5, 6]
for i in range(len(c)):
    d[i] = d[i]+c[i]
print(d)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[4,5,6],[7,8,9],[1,2,3]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)

# 数组与标量之间的算术运算
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a + 3)
print(a * 3)

# 广播机制: 1.获取形状 2.是否可广播
# 同一维度：相同、1
a = np.array([1,2,3]) #1*3
b = np.array([[4],[5],[6]])  #3*1
print(b - a )
'''a
 1 2 3
 1 2 3
 1 2 3
 b
 4 4 4
 5 5 5
 6 6 6
'''

a = np.array([1,2,3]) #1*3
b = np.array([4,5])  #1*2
print(b - a )

# 矩阵运算
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[4,5,6],[7,8,9],[1,2,3]])
print(a @ b)

'''a
1 2 3
4 5 6
7 8 9
b
4 5 6
7 8 9

1 2 3'''


# 计算平方根
print(np.sqrt(9))
print(np.sqrt([1,4,9]))
arr = np.array([1,25,81])
print(np.sqrt(arr))

# 计算指数  e^x  = y
print(np.exp(1))

# 计算自然对数  ln y = x
print(np.log(2.71))

# 计算正弦值、余弦值
print(np.sin(np.pi/2))
print(np.cos(np.pi))

# 计算绝对值
arr = np.array([-1, 1, 2, -3])
print(np.abs(arr))
```

```python
# 计算a的b次幂
print(np.power(arr,3))

# 四舍五入
print(np.round([3.2, 4.5, 8.1, 9.6]))

# 向上取整，向下取整
arr = np.array([1.6, 25.1, 81.7])
print(np.ceil(arr))
print(np.floor(arr))

# 检测缺失值NaN
np.isnan([1, 2, np.nan, 3])

arr = np.random.randint(1,200,8)
print(arr)

# 求和
print(np.sum([1,2,3]))

# 计算平均值
print(np.mean(arr))

# 计算中位数
# 奇数：排序后中间的数值
# 偶数：中间的两个数的平均值
print(np.median([4,1,2]))
print(np.median([1,1,1,1,1,1,1,1,1,100]))

# 计算标准差、方差
# 1,2,3 的平均值 2
# ((1-2)^2 + (2-2)^2 + (3-2)^2 )/ 3 = 0.666
arr1 = np.array([1,2,1,2,1,1,1,2])
arr2 = np.array([1,0,3,0,0,0,4,3])
print(np.mean(arr1))
print(np.mean(arr2))
print(np.var(arr1))
print(np.var(arr2))

# 计算最大值、最小值
print(arr)
print(np.max(arr), np.argmax(arr))
print(np.min(arr), np.argmin(arr))

# 分位数
# 中位数
# __________________
# 1     2    3     4
# 1       2        3
print(np.median([1,2,3]))
print(np.median([1,2,3,4]))
np.random.seed(0)
arr = np.random.randint(0,100,4)
print(arr)
# __________________
# 44   47   64   67
# (47+64)/2
print(np.median(arr))
print(np.percentile(arr,80))
# 0.25*3=0.75
# (47-44)*0.75=2.25 + 44 = 46.25
# 3*0.8 = 2.4
# (67-64)*0.4 = 1.2 + 64 = 65.2

# 累积和、累积积
arr = np.array([1,2,3])
print(np.sum(arr))
print(np.cumsum(arr))
print(np.cumprod(arr))

# 创建嵌套JSON结构的数据
import numpy as np
products = {
    "products": [
        {
            "id": f"P{i}",
            "name": f"Product {i}",
            "category": np.random.choice(["Electronics", "Clothing", "Home", "Food"]),
            "price": round(np.random.uniform(5, 200), 2),
            "in_stock": np.random.choice([True, False]),
            "specs": {
                "weight": round(np.random.uniform(0.1, 5), 2),
                "dimensions": {
                    "length": np.random.randint(5, 50),
                    "width": np.random.randint(5, 30),
                    "height": np.random.randint(5, 20)
                }
            }
        } for i in range(1, 21)
    ]
}

# 保存为JSON
import json
with open('data/products.json', 'w') as f:
    json.dump(products, f, indent=2)
```

---

## Pandas Series

> **源文件**：`2.series学习.ipynb`（43单元） | **docx**：第 3 章

Series 是带标签的一维数组——NumPy 数组 + Index 标签列。每个值都关联一个可访问的 index 标签。
与 Python dict 的区别：Series 的 index 可以**重复**（dict 的 key 唯一），Series 支持向量化运算。

```python
import pandas as pd
```

### 3.1 创建

```python
# series的创建
import pandas as pd
s = pd.Series([10,2,3,4,5])
# 自定义索引
s = pd.Series([10,2,3,4,5], index=['A', 'B', 'C', 'D', 'E'])
# s = pd.Series([10,2,3,4,5], index=[1,2,3,4,5])
# 定义name
s = pd.Series([10,2,3,4,5], index=['A', 'B', 'C', 'D', 'E'], name = '月份')
print(s)

# 通过字典来创建
s = pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
# print(s)
s2 = pd.Series([10,2,3,4,5], index=['A', 'B', 'C', 'D', 'E'], name = '月份')
s1 = pd.Series(s2,index=["A","C"])
print(s1)

# series的属性
'''
index:Series的索引对象
values:Series的值
dtype或dtypes"Series的元素类型
shape:Series的形状
ndim:Series的维度
size:Series的元素个数
name:Series的名称
loc[]  显式索引，按标签索引或切片
iloc[]  隐式索引，按位置索引或切片
at[]  使用标签访问单个元素
iat[]  使用位置访问单个元素
'''
# print(s.index)
# print(s.values)
# print(s.shape,s.ndim,s.size)
# s.name = 'test'
# print(s.dtype,s.name)
print(s.loc['a']) #显式索引
print(s.iloc[0])  #隐式索引
print(s.at['a'])
print(s.iat[0])

# 访问数据
# print(s[1])
# print(s['c'])
# print(s)
# print(s[s<3])
s['f']=6
print(s.head(2))
print(s.tail(1))

# 常见函数
s = pd.Series([10,2,np.nan,None,3,4,5], index=['A', 'B', 'C', 'D', 'E','F','G'], name= 'data')
print(s)

s.head(3)  # 默认取前5行的数据
s.tail(2)   #默认取后5行的数据

# 查看所有的描述性信息
s.describe()

# 获取元素个数(忽略缺失值）
print(s.count())

# 获取索引
print(s.keys())   # 方法
print(s.index)   # 属性

print(s.isna())  #检查Series里的每一个元素是否为缺失值
s.isna()
```

### 3.2 索引、切片与运算

```python
s.isin([4,5,6])  # 检查每个元素是否在参数集合中

s.describe()

print(s.mean())  #平均值
print(s.sum())   #总和
print(s.std())   #标准差
print(s.var())   #方差
print(s.min()) #最小值
print(s.max())  #最大值
print(s.median())  #中位数

print(s)

# print(s.sort_values())
print(s.quantile(0.8)) #分位数
#————————————————
#2  3   4  5   10
#位置 4*0.8=3.2
#值的计算  5 + （10-5）*0.2 = 6

#众数
s['H']=4
print(s.mode())

print(s.value_counts())  # 每个元素的计数

s.drop_duplicates()  #去重
s.unique()
print(s.nunique()) #去重后的元素个数

# 排序  值、索引
s.sort_index()  # 按索引排序
s.sort_values()  #按值排序

'''创建一个包含10名学生数学成绩的Series，成绩范围在50-100之间。
计算平均分、最高分、最低分，并找出高于平均分的学生人数。'''

import pandas as pd
import numpy as np
np.random.seed(42)
values = np.random.randint(50,101,10)
indexes = []
for i in range(1,11):
    indexes.append('学生'+str(i))
scores = pd.Series(values,indexes)
# print(scores)
print('平均分：',scores.mean())
print('最高分：',scores.max())
print('最低分：',scores.min())
# 高于平均分的学生人数
mean = scores.mean()
print('高于平均分的学生人数:',len(scores[scores>mean]))
print('高于平均分的学生人数:',scores[scores>mean].count())
```

### 3.3 缺失值与高级操作

```python
'''温度数据统计
给定某城市一周每天的最高温度Series，完成以下任务：
找出温度超过30度的天数
计算平均温度
将温度从高到低排序
找出温度变化最大的两天
'''
import pandas as pd
import numpy as np
temperatures = pd.Series([28, 31, 29, 32, 30, 27, 33],
                         index=['周一', '周二', '周三', '周四', '周五', '周六', '周日'])

# 找出温度超过30度的天数
n = temperatures[temperatures>30].count()
print('超过30度的天数：',n)

# 计算平均温度
print('平均温度：',temperatures.mean())

# 将温度从高到低排序
t2 = temperatures.sort_values(ascending=False)
print('从高到低排序：',t2)

# 找出温度变化最大的两天
# 28 31 29 32 30 27 33
# none 3 -2 3 -2 -3 6
t3 = temperatures.diff().abs()   #计算series的变化值

print('温度变化最大的两天',*(t3.sort_values(ascending=False).keys()[:2].tolist()))

'''
股票价格分析
给定某股票连续10个交易日的收盘价Series：
计算每日收益率（当日收盘价/前日收盘价 - 1）
找出收益率最高和最低的日期
计算波动率（收益率的标准差）


prices = pd.Series([102.3, 103.5, 105.1, 104.8, 106.2, 107.0, 106.5, 108.1, 109.3, 110.2], index=pd.date_range('2023-01-01', periods=10))
'''

import pandas as pd
import numpy as np
# 日期序列
date = pd.date_range('2000-06-1',periods=60)
print(list(date))

prices = pd.Series([102.3, 103.5, 105.1, 104.8, 106.2, 107.0, 106.5, 108.1, 109.3, 110.2], index=pd.date_range('2023-01-01', periods=10))

prices

'''计算每日收益率（当日收盘价/前日收盘价 - 1）
找出收益率最高和最低的日期
计算波动率（收益率的标准差）'''
# 计算每日收益率
a = prices.pct_change()  #percent  103.5/102.3 - 1

# 收益率最高的日期
print(a.idxmax())
# 收益率最低的日期
print(a.idxmin())

# 波动率
print(a.std())

'''销售数据分析
某产品过去12个月的销售量Series：
计算季度平均销量（每3个月为一个季度）
找出销量最高的月份
计算月环比增长率
找出连续增长超过2个月的月份

sales = pd.Series([120, 135, 145, 160, 155, 170, 180, 175, 190, 200, 210, 220],index=pd.date_range('2022-01-01', periods=12, freq='MS'))'''

a = pd.date_range('2022-01-01', periods=12, freq='MS')

sales = pd.Series([120, 135, 145, 160, 155, 170, 180, 175, 190, 200, 210, 220],index=pd.date_range('2022-01-01', periods=12, freq='MS'))
```

```python
sales

# 季度的平均销量
# (120+135+145)/3 = 400/3
sales.resample('QS').mean()  #重新采样

print('销量最高的月份',sales.idxmax())

print('月环比的增长率')
sales.pct_change()

# 找出连续增长超过2个月的月份
sales

a = sales.pct_change()
b=a>0
b[b.rolling(3).sum()==3].keys().tolist()

'''每小时销售数据分析
某商店每小时销售额Series：
按天重采样计算每日总销售额
计算每天营业时间（8:00-22:00）和非营业时间的销售额比例
找出销售额最高的3个小时'''

import pandas as pd
import numpy as np
np.random.seed(42)
h = pd.Series(np.random.randint(0,100,24),
          index=pd.date_range('2025-01-01',periods=24,freq='h'))
# 按天重采样计算每日总销售额
day_sales = h.resample('D').sum()
# hours_sales.sum()
# 计算每天营业时间（8:00-22:00）和非营业时间的销售额比例
mask =(h.index.hour>=8) & ((h.index.hour<=22))
b = h[mask]
n_b = h[~mask]
print(b.sum()/n_b.sum())
# 找出销售额最高的3个小时
print(h.nlargest(3).keys())
```

---

## Pandas DataFrame

> **源文件**：`3.DataFrame学习.ipynb`（39单元） | **docx**：第 3 章

DataFrame 是 Pandas 最核心的结构——带行列标签的二维表格，类比 Excel 表 / SQL 表。
每列是一个 Series，多列组合成 DataFrame。用 `df["列名"]` 提取列，`df.loc[行, 列]` 按标签访问，`df.iloc[行号, 列号]` 按位置访问。

### 3.4 创建与列操作

```python
# dataframe的创建方式
import pandas as pd
import numpy as np
# 通过series来创建
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([6,7,8,9,10])
df = pd.DataFrame({"第1列":s1,"第2列":s2})
# 通过字典来创建
df = pd.DataFrame(
    {
        "name":["tom",'jack','alice','bob','allen'],
        "age":[15,17,20,26,30],
        "score":[60.5,80,30.6,70,83.5]
    },index=[1,2,3,4,5],columns=["name","score","age"]
)
df

# dataframe的属性
print('行索引：')
print(df.index)
print('列标签：')
print(df.columns)
print('值')
print(df.values)

print('维度：',df.ndim)
print('形状:', df.shape)
print('元素个数：', df.size)
print('数据类型：')
print(df.dtypes)

# 行列转置
print(df.T)

# 获取元素 loc  iloc  at  iat
# 某行
print(df.loc[4])
print(df.iloc[3])

# 某列
print(df.loc[:,'name'])
print(df.iloc[:,0])

# 单个元素
print(df.at[3,'score'])
print(df.iat[2,1])
print(df.loc[3,'score'])
print(df.iloc[2,1])

# 获取单列数据
print(df['name'])
print(type(df['name']))
print(df.name)
print(type(df.name))
print(df[['name']])
print(type(df[['name']]))
df[['name']]
```

### 3.5 数据查看与筛选

`df.head(n)`/`tail(n)` 看头尾 / `df.info()` 看结构 / `df.describe()` 统计摘要 / `df.shape` 行列数 / `df.columns` 列名

```python
print(df[['name','score']]) # 多列数据的获取

# 查看部分数据
print(df.head(2))

print(df.tail(3))

# 使用布尔索引筛选数据
df[df.score>70]
df[ (df['score']>70) & (df.age<20)]

# 随机抽样
df.sample(3)

df = pd.DataFrame(
    {
        "name":["tom",'jack','alice','bob','allen'],
        "age":[15,17,20,26,30],
        "score":[60.5,80,30.6,70,83.5]
    },index=[1,2,3,4,5],columns=["name","score","age"]
)

print(df.head()) #查看前n行数据，默认是5行
print(df.tail(1))  #查看后n行数据，默认是5行

print(df.isin(['jack',20]))  #查看元素是否包含在参数集合中
```

### 3.6 缺失值处理

| 方法 | 说明 | 适合场景 |
|------|------|---------|
| `df.dropna()` | 删除含缺失的行/列 | 缺失率低 / 数据充足 |
| `df.fillna(val)` | 用指定值填充 | 已知合理默认值 |
| `df.fillna(method="ffill")` | 向前填充 | 时序数据 |
| `df.fillna(method="bfill")` | 向后填充 | 时序数据 |
| `df.interpolate()` | 线性插值 | 数值型时序 |

```python
print(df.isna()) # 查看元素是否是缺失值

print(df['score'].sum())  #某一列的总和
print(df.score.max())  #最大值
print(df.age.min())  #最小值
print(df.score.mean())  #平均数
print(df.score.median())  #中位数
print(df.age.mode())  #众数

df = pd.DataFrame(
    {
        "name":["tom","tom",'jack','alice','bob','allen'],
        "age":[15,15,15,20,26,30],
        "score":[60.5,60.5,80,30.6,70,83.5]
    },index=[1,2,3,4,5,6],columns=["name","score","age"]
)

print(df.score.std())  #标准差
print(df.score.var()) #方差
print(df.score.quantile(0.25))  #分位数

print(df.describe())

print(df.count())  #每一列非缺失值的个数

print(df.value_counts()) #出现的次数

print(df.drop_duplicates())
```

### 3.7 数据类型转换

| 操作 | 语法 | 说明 |
|------|------|------|
| 查看类型 | `df.dtypes` | 每列数据类型 |
| 强制转换 | `df["col"].astype("int32")` | 转为 int32 节省内存 |
| 转日期 | `pd.to_datetime(df["col"])` | 字符串 → datetime |
| 转分类 | `df["col"].astype("category")` | 低基数列优化（性别/省份） |
| 保留小数 | `df["col"].round(2)` | 数值格式化 |
| 容错转换 | `pd.to_numeric(col, errors="coerce")` | 无效值 → NaN |

```python
print(df.duplicated(subset=['age']))  #查看是否重复

df.sample(2) #随机抽样

print(df.replace(15,30))

df.cumsum()
df.cummin(axis=0)

print(df.sort_index(ascending=False))

print(df.sort_values(by='score'))

df = pd.DataFrame(
    {
        "name":["tom","tom",'jack','alice','bob','allen'],
        "age":[15,15,15,20,26,30],
        "score":[60.5,60.5,80,30.6,70,80]
    },index=[1,2,3,4,5,6],columns=["name","score","age"]
)

print(df.sort_values(by=['score','age'],ascending=[True,False]))
```

### 3.8 分组与透视

```python
df.nlargest(2,columns=['score','age'])
df.nsmallest(2,columns=['score','age'])

'''
案例1：学生成绩分析
场景：某班级的学生成绩数据如下，请完成以下任务：
1. 计算每位学生的总分和平均分。
2. 找出数学成绩高于90分或英语成绩高于85分的学生。
3. 按总分从高到低排序，并输出前3名学生。
'''
import pandas as pd
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '数学': [85, 92, 78, 88, 95],
    '英语': [90, 88, 85, 92, 80],
    '物理': [75, 80, 88, 85, 90]
}
scores = pd.DataFrame(data)

#1. 计算每位学生的总分和平均分。
scores['总分'] = scores[['数学','英语','物理']].sum(axis=1)
scores['平均分'] = scores['总分'] / 3
scores['平均分2'] = scores[['数学','英语','物理']].mean(axis=1)
#2. 找出数学成绩高于90分或英语成绩高于85分的学生。
scores[ (scores['数学']>90 ) | (scores['英语']>85 )  ]
#3. 按总分从高到低排序，并输出前3名学生。
r1 = scores.sort_values('总分',ascending=False).head(3)
r2 =scores.nlargest(3,columns=['总分'])
print(r1)
print(r2)

'''
案例2：销售数据分析
场景：某公司销售数据如下，请完成以下任务：
1. 计算每种产品的总销售额（销售额 = 单价 × 销量）。
2. 找出销售额最高的产品。
3. 按销售额从高到低排序，并输出所有产品信息。
'''
import pandas as pd

data = {
    '产品名称': ['A', 'B', 'C', 'D'],
    '单价': [100, 150, 200, 120],
    '销量': [50, 30, 20, 40]
}
df = pd.DataFrame(data)
df['总销售额'] = df['单价']*df['销量']
df.nlargest(1,columns=['总销售额'])
df.sort_values('总销售额',ascending=False)

'''案例3：电商用户行为分析
场景：某电商平台的用户行为数据如下，请完成以下任务：
1. 计算每位用户的总消费金额（消费金额 = 商品单价 × 购买数量）
2. 找出消费金额最高的用户，并输出其所有信息
3. 计算所有用户的平均消费金额（保留2位小数）
4. 统计电子产品的总购买数量
'''
import pandas as pd

data = {
    '用户ID': [101, 102, 103, 104, 105],
    '用户名': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    '商品类别': ['电子产品', '服饰', '电子产品', '家居', '服饰'],
    '商品单价': [1200, 300, 800, 150, 200],
    '购买数量': [1, 3, 2, 5, 4]
}
df = pd.DataFrame(data)
df['总消费金额'] = df['商品单价']*df['购买数量']
df.nlargest(1,columns=['总消费金额'])
df['总消费金额'].mean()
df[df['商品类别']=='电子产品']['购买数量'].sum()

#数据变形
import pandas as pd
data = {
    'ID': [1, 2],
    'name':['张三','李四'],
    'Math': [90, 85],
    'English': [88, 92],
    'Science': [95, 89]
}
df = pd.DataFrame(data)
df
df.T
#宽表转长表
df2= pd.melt(df, id_vars=['ID','name'], var_name='科目', value_name='分数')
df2.sort_values(by=['name','科目'])
#长表转宽表
df3=pd.pivot(df2,index=['ID','name'],columns=['科目'],values='分数')
#分列
data = {
    'ID': [1, 2],
    'name':['alice smith','bob jack'],
    'Math': [90, 85],
    'English': [88, 92],
    'Science': [95, 89]
}
df = pd.DataFrame(data)
df[['first name','last name']] = df['name'].str.split(' ')
# 加载数据
df = pd.read_csv("data/sleep.csv")

df=df[['person_id','blood_pressure']]
df[['high','low']]=df['blood_pressure'].str.split('/',expand=True)
df

# 加载数据
df_employees = pd.read_csv("data/employees.csv")
df_employees


# 加载数据
df_employees = pd.read_csv("data/employees.csv")
df_employees
# 1. 将first_name首字母大写，其余小写
df_employees['first_name'] = df_employees['first_name'].str.capitalize()

# 2. 提取邮箱域名（@后部分）
df_employees['email_domain'] = df_employees['email'].str.extract(r'@(.+)')

print(df_employees[['first_name', 'email', 'email_domain']].head())
```

---

## 数据分析与挖掘

> **源文件**：`4.数据分析.ipynb`（41单元） | **docx**：第 4 章 | **pptx**：GroupBy 三步法

### 4.1 GroupBy 分组聚合

Pandas 的 `groupby()` 模拟 SQL `GROUP BY`，遵循 **split → apply → combine** 三步模式：
1. **Split**：按分组键把数据分割为多个子组
2. **Apply**：对每个子组执行聚合函数（sum/mean/count）
3. **Combine**：将结果合并为一个结果表

```python
df.groupby("分组字段")["聚合字段"].聚合函数()
# 多键分组
df.groupby(["部门", "岗位"])["薪资"].mean()
```

```python
# 数据的导入
import pandas as pd
df = pd.read_csv('data/employees.csv')
print(type(df))
print(df.tail())
print(df.salary.mean())
# 数据的导出
df = df.tail()
df.to_csv('data/new.csv')

# json
df = pd.read_json('data/data1.json')
print(type(df))

import json
with open('data/test.json') as f:
    data = json.load(f)
# print(data['users'])
print(type(data))
df = pd.DataFrame(data['users'])
print(type(df))
df

# 缺失值的处理
# nan:not a number
import pandas as pd
import numpy as np
s = pd.Series([12,25,np.nan, None, pd.NA])
df = pd.DataFrame([[1,pd.NA,2],[2,3,5],[None,4,6]],columns=['第1列','第2列','第3列'])
print(s)
# 查看是否是缺失值
print(s.isna())
print(s.isnull())
print(df.isna())
print(df.isnull())
print(df.isna().sum(axis=1))
print(s.isna().sum()) #查看缺失值的个数

# 剔除缺失值
print(s.dropna())
print('-'*30)
print(df)
print(df.dropna()) #剔除一整条的记录
print(df.dropna(how='all')) #如果所有的值都是缺失值，删除这一行
print(df.dropna(thresh=1)) #如果至少有n个值不是缺失值，就保留
print(df.dropna(axis=1)) #剔除一整列的记录
print(df.dropna(subset=['第1列'])) #如果某列有缺失值，则删除这一行

# 填充缺失值
df = pd.read_csv('data/weather_withna.csv')
df.tail()
df.isna().sum(axis=0)
df.head()
print(df.fillna({'temp_max':20,'wind':2.5}).tail()) #使用字典来填充
print(df.fillna(df[['temp_max','wind']].mean()).tail()) #使用统计值来填充
print(df.ffill().tail())#用前面的相邻值填充
print(df.bfill().tail())#用后面的相邻值填充

# 时间数据的处理
import pandas as pd
d = pd.Timestamp('2015-02-28 10:22')
d1 = pd.Timestamp('2015-02-28 13:22')
print(d)
print(type(d))
print("年：",d.year)
print("月：",d.month)
print("日：",d.day)
print(d.hour, d.minute, d.second)
print("季度：",d.quarter)
print("是否是月底：",d.is_month_end)
# 方法
print("星期几：",d.day_name())
print("转换为天：",d.to_period("D"))
print("转换为季度：",d1.to_period("Q"))
print("转换为年度：",d1.to_period("Y"))
print("转换为月度：",d1.to_period("M"))
print("转换为周维度：",d1.to_period("W"))

# 字符串转换为日期类型
a = pd.to_datetime('20150228')
print(a)
print(type(a))
print(a.day_name())

# dataFrame 日期转换
df = pd.DataFrame({
    'sales':[100,200,300],
    'date':['20250601','20250602','20250603']
})
df['datetime'] = pd.to_datetime(df['date'])
df
print(df.info())
print(type(df['datetime']))
df['week']=df['datetime'].dt.day_name()
df['datetime'].dt.year



# csv 日期转换
df = pd.read_csv('data/weather.csv',parse_dates=['date'])
df.info()
df['date'].dt.day_name()

# 日期数据作为索引
# df.set_index('date' , inplace=True)#设置原来的df的索引
print(df.loc["2013-01":"2013-02"])

# 时间间隔
d1 = pd.Timestamp('2013-01-15')
d2 = pd.Timestamp('2023-02-23')
d3 = d2-d1
print(type(d3))
print(d3)

df = pd.read_csv('data/weather.csv',parse_dates=['date'])
df.info()
df['delta'] = df['date'] - df['date'][0]
df.set_index('delta',inplace=True)

df
print(df.loc['10 days':'20 days'])

days = pd.date_range("2025-07-03","2026-02-09",freq="W")
days = pd.date_range("2025-07-03",periods=10,freq="QE")
print(days)

df = pd.read_csv('data/weather.csv',parse_dates=['date'])
# 重新采样
df.set_index('date',inplace=True)
```

### 4.2 数据合并

| 函数 | 类比 SQL | 说明 |
|------|----------|------|
| `pd.concat([a,b])` | UNION ALL | 行/列拼接 |
| `df.merge(other, on="key")` | JOIN | 按 key 横向合并 |
| `df.join(other)` | 索引 JOIN | 按 index 合并 |

```python
df[ ["temp_max","temp_min"]].resample("MS").mean()

df[ ["temp_max","temp_min"]].resample("YE").mean()

import pandas as pd
data = {
    "name":['alice','alice','bob','alice','jack','bob'],
    "age":[26,25,30,25,35,30],
    'city':['NY','NY','LA','NY','SF','LA']
}
df = pd.DataFrame(data)

df.duplicated() #一整条记录都是一样的，标记为重复，返回True
df.drop_duplicates(subset=['name']) #根据指定列去重
df.drop_duplicates(subset=['name'],keep='last') #保留最后一次出现的行

# 数据类型的转换
df = pd.read_csv('data/sleep.csv')
df.dtypes

df['age'] = df['age'].astype('int16')

df['gender'] = df['gender'].astype('category')

df.gender

df['is_male'] = df['gender'].map({'Female':True,'Male':False})

df.is_male
```

### 4.3 透视表与时间序列

透视表：`pd.pivot_table(df, values="值", index="行", columns="列", aggfunc="mean")` — 类似 Excel 数据透视表
时间序列：`pd.to_datetime()` / `df.set_index("date")` / `df.resample("M")` 按月度重采样 / `df.shift()` 环比计算

```python
#数据变形
import pandas as pd
data = {
    'ID': [1, 2],
    'name':['alice','bob'],
    'Math': [90, 85],
    'English': [88, 92],
    'Science': [95, 89]
}
df = pd.DataFrame(data)
print(df)
df.T   #行列转置
# 宽表转换成长表
df2 = pd.melt(df,id_vars=['ID','name'],var_name='科目',value_name='分数')
df2.sort_values('name')
print(df2)
# 长表转宽表
pd.pivot(df2,index=['ID','name'],columns='科目',values='分数')

data = {
    'ID': [1, 2],
    'name':['alice smith','bob smith'],
    'Math': [90, 85],
    'English': [88, 92],
    'Science': [95, 89]
}
df = pd.DataFrame(data)
# 分列
df[['first','last']]  = df['name'].str.split(" ",expand=True)
df = pd.read_csv('data/sleep.csv')
df = df[['person_id','blood_pressure']]
df[['high','low']] = df['blood_pressure'].str.split('/',expand=True)
df['high']=df['high'].astype('int64')
df['low']=df['low'].astype('int64')
df.info()
df.high.mean()
df.low.mean()

# 数据分箱 pd.cut(x,bins,labels)
import pandas as pd
df = pd.read_csv('data/employees.csv')
df.head(10)

df1 = df.head(10)[['employee_id','salary']]
df1

pd.cut(df1['salary'],bins=3) #bins=n，分成n段区间，起始值、结束值是所有数据的最小值、最大值
#4180~14100~24000
pd.cut(df1['salary'],bins=3).value_counts()
pd.cut(df1['salary'],bins=[0,10000,20000,30000])#bins=list，分成n段区间
pd.cut(df1['salary'],bins=[0,10000,20000,30000]).value_counts()
df1['收入范围'] =pd.cut(df1['salary'],bins=[0,10000,20000,30000],labels=['低','中','高'])#bins=list，分成n段区间
pd.qcut(df1['salary'],3).value_counts()

# 睡眠数据
df = pd.read_csv('data/sleep.csv')
df1 = df.head(10)[['person_id','sleep_quality']]
df1
df['睡眠质量'] = pd.cut(df['sleep_quality'],bins=3,labels=
                         ['差','中','优'])
df['睡眠质量'].value_counts()
df.head(10)
df['gender']=df['gender'].astype('category')
df['gender'].value_counts()
# 字符串-->类别-->统计
# 数值-->分箱-->统计
print(df['gender'].dtype)
print(df['睡眠质量'].dtype)

# df.rename()   df.set_index()  df.reset_index()
df = pd.DataFrame({
    'name':['jack','alice','tom','bob'],
    'age':[20,30,40,50],
    'gender':['female','male','female','male']
})
df.set_index("name",inplace=True)
df.reset_index(inplace=True)
df.rename(columns={"age":"年龄"},index={0:4})

df.index=[1,2,3,4]
df.columns=["姓名",'年龄',"性别"]
df

# 分组聚合
# df.groupby('分组的字段')['聚合的字段'].聚合函数()
import pandas as pd
df = pd.read_csv('data/employees.csv')
df = df.dropna(subset=['department_id'])
df['department_id'] = df['department_id'].astype('int64')
# 计算不同部门的平均薪资
df.groupby('department_id').groups #查看分组
df.groupby('department_id').get_group(20) #查看具体的某个分组数据
df2 = df.groupby('department_id')[['salary']].mean()
df2['salary'] = df2['salary'].round(2)
df2=df2.reset_index()
df2.sort_values('salary',ascending=False)

# 计算不同部门不同岗位的人的平均薪资
df2=df.groupby(['department_id','job_id'])[['salary']].mean()
df2=df2.reset_index()
df2['salary'] = df2['salary'].round(1)
df2.sort_values('salary',ascending=False)
```

```python
# 企鹅数据分析
# 1. 导入必要的库
import pandas as pd
import numpy as np
# 2. 导入数据 喙
df = pd.read_csv('data/penguins.csv')
df.head(5)
df.info()


# 3. 数据清洗
# 缺失值的检查
print(df.isna().sum())
df.dropna(inplace=True)

# 4. 数据特征的构造
df['sex'] = df['sex'].astype('category')
df['bill_ratio'] = df['bill_length_mm']/df['bill_depth_mm']
df.head()

# 5. 数据分析
# 数据分箱-把体重分为三个等级
labels = ['低','中','高']
df['mass_level'] = pd.cut(df['body_mass_g'],bins=3,labels=labels)
print(df['mass_level'].value_counts())
# 按岛屿、性别分组分析
df.groupby(['sex','island']).agg({
    'body_mass_g':['mean','count'],
})

# 睡眠质量分析
# 1.导入库
import pandas as pd
import numpy as np
# 2.导入数据
df = pd.read_csv('data/sleep.csv')
df.head()
df.info()
df.describe()

# 3.数据清洗
df.isna().sum()
df.drop(columns='sleep_disorder',inplace=True)

# 4. 数据特征的构造
df['gender'] = df['gender'].astype('category')
df['occupation'] = df['occupation'].astype('category')
df['bmi_category'] = df['bmi_category'].astype('category')
df[['high','low']]=df['blood_pressure'].str.split('/',expand=True)

# 睡眠质量的分箱
labels = ['差','中','优']
df['quality_level'] = pd.cut(df['sleep_quality'],bins=3,labels=labels)
age_labels=['青少年','中年','老年']
df['age_level'] = pd.cut(df['age'],bins=3,labels=age_labels)
df.head()

# 5.数据的统计、分析
print(df['bmi_category'].value_counts())

# 根据不同的bmi分组，睡眠质量
df.groupby(['age_level','bmi_category']).agg({
    'sleep_duration':'mean',
    'sleep_quality':'mean',
    'stress_level':'mean'
})
```

---

## 数据可视化

> **源文件**：`5.matplotlib学习.ipynb`（12单元） + `6.seaborn学习.ipynb`（13单元） | **docx/pptx**：第 5 章

### 5.1 Matplotlib 核心架构

> pptx 架构图：`Figure(画布) → Axes(坐标系) → 图形要素(标题, 坐标轴, 图形要素, 图例, 数据标签)`

Matplotlib 是 Python 底层绘图库，Seaborn 基于它构建。主要组件：
- **Figure**：顶层画布，可包含多张子图
- **Axes**：实际绘图区（坐标系），承载图形
- **图形要素**：标题(`plt.title`)、轴标签(`xlabel/ylabel`)、图例(`legend`)、数据标签、网格线、刻度

| 图表 | 函数 | 场景 |
|------|------|------|
| 折线图 | `plt.plot()` | 趋势 |
| 柱状图 | `plt.bar()` / `barh()` | 对比 |
| 散点图 | `plt.scatter()` | 关联 |
| 直方图 | `plt.hist()` | 分布 |
| 饼图/圆环 | `plt.pie()` | 占比 |
| 箱线图 | `plt.boxplot()` | 离散 |

```python
'''
折线图  plot
条形图  bar
饼图 pie
散点图  scatter
箱线图  boxplot
多个图表
组合图
'''

# 绘制折线图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
month = ['1月','2月','3月','4月']
sales = [100,150,80,130]
# 绘制折线图
plt.plot(month,sales,
         label='产品A',
         color='orange',
         linewidth=2,
         linestyle='--',
         marker='o',)

# 添加标题
plt.title('2025年销售趋势', color='red',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('月份',fontsize=10)
plt.ylabel('销售额（万元）',fontsize=10)
# 添加图例
plt.legend(loc='upper left')
# 添加网格线
plt.grid(True,alpha=0.1,color='blue',linestyle='--')
# plt.grid(axis='x')
# 设置刻度字体大小
plt.xticks(rotation=0,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
# 设置y轴的范围
plt.ylim(0,160)
# 在每个数据点上显示数值
for x,y in zip(month,sales):
    plt.text(x,y+1,str(y),ha='center',va='bottom',fontsize=10)
# 显示图表
plt.show()

# 绘制柱状图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
subjects = ['语文','数学','英语','科学']
scores = [85, 92, 78, 88]

# 绘制柱状图
plt.bar(subjects,scores,
        label='小红',
        color='orange',
        width=0.6,)
#
# 添加标题
plt.title('2025年成绩分布', color='red',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('科目',fontsize=10)
plt.ylabel('分数',fontsize=10)
# 添加图例
plt.legend(loc='upper right')
# 添加网格线
plt.grid(axis='y',alpha=0.1,color='blue',linestyle='--')
# plt.grid(axis='x')
# 设置刻度字体大小
plt.xticks(rotation=0,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
# 设置y轴的范围
plt.ylim(0,100)
# 在每个数据点上显示数值
for x,y in zip(subjects,scores):
    plt.text(x,y+1,str(y),ha='center',va='bottom',fontsize=10)
# 自动优化排版
plt.tight_layout()
# 显示图表
plt.show()

# 绘制条形图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
countries = ['United States','China','Japan','Germany','India']
gdp = [ 92,78, 43, 22,8]
#
# 绘制条形图
plt.barh(countries,gdp,color='orange',)

# 添加标题
plt.title('2025年GDP排名', color='red',fontsize=20)
# 添加坐标轴的标签
plt.xlabel('GDP',fontsize=10)
plt.ylabel('国家',fontsize=10)
# 自动优化排版
plt.tight_layout()
# 显示图表
plt.show()

# 绘制饼图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))
# 要绘图的数据
things = ['学习','娱乐','运动','睡觉','其他']
times = [6,4,1,8,5]
colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']  #配色
# 绘制饼图
plt.pie(times,labels=things,
        autopct='%.1f%%',  # 显示百分比
        startangle=90, #调整初始画图的角度
        colors = colors,
        )
# 添加标题
plt.title('一天的时间分布', color='red',fontsize=20)
# 自动优化排版
plt.tight_layout()
# 显示图表
plt.show()

# 绘制环形图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))
# 要绘图的数据
things = ['学习','娱乐','运动','睡觉','其他']
times = [6,4,1,8,5]
colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']  #配色
# 绘制饼图
plt.pie(times,labels=things,
        autopct='%.1f%%',  # 显示百分比
        startangle=90, #调整初始画图的角度
        colors = colors,# 设置饼图的配色
        wedgeprops={'width':0.6},#设置圆环的宽度
        pctdistance=0.6, #设置百分比的位置
        )
# 添加标题
plt.title('一天的时间分布', color='red',fontsize=20)
plt.text(0,0,'总计：\n100%',ha='center',va='bottom',fontsize=10)
# 自动优化排版
plt.tight_layout()
# 显示图表
plt.show()
```

```python
# 绘制爆炸式饼图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))
# 要绘图的数据
things = ['学习','娱乐','运动','睡觉','其他']
times = [6,4,1,8,5]
colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']  #配色
explode = [0.1,0,0,0,0]#设置突出块的位置
# 绘制饼图
plt.pie(times,labels=things,
        autopct='%.1f%%',  # 显示百分比
        startangle=0, #调整初始画图的角度
        colors = colors,
        explode = explode,#设置突出块
        shadow=True,
        )
# 添加标题
plt.title('一天的时间分布', color='red',fontsize=20)
# 自动优化排版
plt.tight_layout()
# 显示图表
plt.show()

# 绘制散点图
import matplotlib.pyplot as plt
from matplotlib import rcParams # 字体
# rcParams['font.family'] = 'STHeiti' #mac  win:SimHei
rcParams['font.sans-serif'] = 'STHeiti'
# 创建图表，设置大小
plt.figure(figsize=(10,5))

# 要绘图的数据
scores=[50,55,60,65,70,75,80]
hours=[1,2,3,4,5,6,7]

# 绘制散点图
plt.scatter(hours,scores)

# 显示图表
plt.show()

# 箱线图
import matplotlib.pyplot as plt

# 模拟 3 门课的成绩
data = {
    '语文': [82, 85, 88, 70, 90, 76, 84, 83, 95],
    '数学': [75, 80, 79, 93, 88, 82, 87, 89, 92],
    '英语': [70, 72, 68, 65, 78, 80, 85, 90, 95]
}
plt.figure(figsize=(8, 6))
plt.boxplot(data.values(), tick_labels=data.keys())

plt.title("各科成绩分布（箱线图）")
plt.ylabel("分数")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()

'''
折线图：趋势随时间变化
条形图/柱状图：类别之间对比
饼图：整体组成比例
散点图：两变量相关性
箱线图：数据分布、异常
'''

# 多个图的绘制方法
import matplotlib.pyplot as plt
# 要绘图的数据
month = ['1','2','3','4']
sales = [100,150,80,130]

# 动态图表的生成
# f1 = plt.subplot(2,2,1) #生成一个子图 行 列 索引
f1 = plt.subplot(221) #生成一个子图 行 列 索引
f1.plot(month,sales)
f2 = plt.subplot(2,2,2)
f2.bar(month,sales)
f3 = plt.subplot(2,2,3)
f3.scatter(month,sales)
f4 = plt.subplot(224)
f4.barh(month,sales)

# 分析案例：温度分析
# 1. 导入库
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = 'STHeiti'

# 2. 导入数据
df = pd.read_csv('data/weather.csv')
df.head()
# 绘制气温的趋势变化图
df['date'] = pd.to_datetime(df['date'])
df=df[df['date'].dt.year==2015]
plt.figure(figsize=(15,10))
plt.plot(df['date'],df['temp_max'],label='最高气温')
plt.plot(df['date'],df['temp_min'],label='最低气温')
plt.title('2015年气温趋势变化图')
plt.xlabel('日期')
plt.ylabel('气温')
plt.legend()

# 绘制降水量的直方图
df['temp_mean'] = (df['temp_max'] + df['temp_min'])/2
plt.figure(figsize=(15,10))
plt.plot(df['date'],df['temp_mean'],label='平均气温')
plt.title('2015年气温趋势变化图')
plt.xlabel('日期')
plt.ylabel('气温')
plt.legend()
# 绘制降水量的直方图
plt.hist(df['precipitation'],bins=5)
```

### 5.2 可视化工具对比

> pptx 第 66 页表格

| 工具 | 说明 | 优点 | 缺点 |
|------|------|------|------|
| matplotlib | Python 底层绘图库 | 精细控制 | API 复杂 |
| seaborn | 基于 matplotlib | 美观、统计友好 | 定制性弱 |
| plotly | 交互式图形 | 可缩放悬停 | 学习曲线陡 |
| Excel 图表 | 内置工具 | 简单直观 | 数据量受限 |

### 5.3 Seaborn 统计可视化

Seaborn 提供更高级统计接口：更美主题、更简 API、内置分布分析、分类调色板。

| 函数 | 用途 |
|------|------|
| `sns.histplot()` | 直方图+KDE |
| `sns.boxplot()` | 分类箱线 |
| `sns.scatterplot()` | 散点（hue分组）|
| `sns.heatmap()` | 相关性热力 |
| `sns.pairplot()` | 多变量矩阵 |
| `sns.violinplot()` | 小提琴图 |
| `sns.barplot()` | 分类柱状 |

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["STHeiti"]
penguins = pd.read_csv("data/penguins.csv")
penguins.dropna(inplace=True)
penguins.info()
penguins.head()

# 直方图
sns.histplot(data=penguins, x="species")

#核密度估计图
'''核密度估计图（KDE，Kernel Density Estimate Plot）是一种用于显示数据分布的统计图表，它通过平滑直方图的方法来估计数据的概率密度函数，使得分布图看起来更加连续和平滑。核密度估计是一种非参数方法，用于估计随机变量的概率密度函数。其基本思想是，将每个数据点视为一个“核”（通常是高斯分布），然后将这些核的贡献相加以形成平滑的密度曲线。'''
#绘制喙长度的核密度估计图
sns.kdeplot(data=penguins, x="bill_length_mm")

sns.histplot(data=penguins, x="bill_length_mm", kde=True)

'''计数图
计数图用于绘制分类变量的计数分布图，显示每个类别在数据集中出现的次数，是分析分类数据非常直观的工具，可以快速了解类别的分布情况。'''
#绘制不同岛屿企鹅数量的计数图
sns.countplot(data=penguins, x="island")

#散点图
#绘制横轴为体重，纵轴为脚蹼长度的散点图。可通过hue参数设置不同组别进行对比
sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="sex")

#蜂窝图
#通过jointplot()函数，设置kind="hex"来绘制蜂窝图。
sns.jointplot(data=penguins, x="body_mass_g", y="flipper_length_mm", kind="hex")
```

```python
#二维核密度估计图
#通过kdeplot()函数，同时设置x参数和y参数来绘制二维核密度估计图。
sns.kdeplot(data=penguins, x="body_mass_g", y="flipper_length_mm")

#通过fill=True设置为填充，通过cbar=True设置显示颜色示意条。
sns.kdeplot(data=penguins, x="body_mass_g", y="flipper_length_mm", fill=True, cbar=True)

#条形图
sns.barplot(data=penguins, x="species", y="bill_length_mm", estimator="mean", errorbar=None)

#箱线图
sns.boxplot(data=penguins, x="species", y="bill_length_mm")

#小提琴图
'''小提琴图（Violin Plot） 是一种结合了箱线图和核密度估计图（KDE）的可视化图表，用于展示数据的分布情况、集中趋势、散布情况以及异常值。小提琴图不仅可以显示数据的基本统计量（如中位数和四分位数），还可以展示数据的概率密度，提供比箱线图更丰富的信息。'''
sns.violinplot(data=penguins, x="species", y="bill_length_mm")

#成对关系图
'''成对关系图是一种用于显示多个变量之间关系的可视化工具。它可以展示各个变量之间的成对关系，并且通过不同的图表形式帮助我们理解数据中各个变量之间的相互作用。
对角线上的图通常显示每个变量的分布（如直方图或核密度估计图），帮助观察每个变量的单变量特性。其他位置展示所有变量的两两关系，用散点图表示。'''
sns.pairplot(data=penguins, hue="species")
```

---

## 综合项目：房地产市场分析

> **源文件**：`7.房地产市场分析.ipynb`（16单元） | **数据**：`data/house_sales.csv`（约20MB）

完整端到端分析——原始数据 → 清洗 → 特征工程 → 可视化 → 建模

```python
# 1. 导入库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei'] #win
rcParams['font.sans-serif'] = ['STHeiti'] #mac

# 2. 导入数据
df = pd.read_csv('data/house_sales.csv')

# 3. 数据概览
print('总记录数：', len(df))
print('字段数量：', len(df.columns))
df.head(5)
df.info()

# 4. 数据清洗
# 删除无用的数据列
df.drop(columns='origin_url',inplace=True)
```

### 数据清洗

删除无用列 / `isnull().sum()` 检查缺失 / `dropna()` 删除 / `duplicated().sum()` 查重 / 数据类型转换 / IQR 法去异常

```python
# 检查是否有缺失值
df.isna().sum()
# 删除缺失值
df.dropna(inplace=True)

# 检查是否有重复值
df.duplicated().sum()
# 删除重复数据
df.drop_duplicates(inplace=True)
# print(len(df))
# 面积的数据类型转换
df['area'] = df['area'].str.replace('㎡','').astype(float)
# 售价的数据类型转换
df['price'] = df['price'].str.replace('万','').astype(float)
# 朝向的数据类型转换
df['toward'] = df['toward'].astype('category')
# 单价的数据类型转换
df['unit'] = df['unit'].str.replace('元/㎡','').astype(float)
# 建造年份的数据类型转换
df['year'] = df['year'].str.replace('年建','').astype(int)

# 异常值的处理
# 房屋面积的异常处理
df = df[ (df['area']<600) & (df['area']>20)]

# 房屋售价的异常处理  IQR
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
low_price = Q1 - 1.5*IQR
high_price = Q3 + 1.5*IQR
df = df[ (df['price']<high_price) & (df['price']>low_price) ]
```

### 特征工程

提取地区(从地址) / 判断楼层类型 / 提取卧室数(从户型"3室2厅"解析) / 计算楼龄 / 价格分箱(低/中/高)

```python
# 5. 新数据特征构造
# 地区district
df['district'] = df['address'].str.split('-').str[0]
# 楼层的类型floor_type
df['floor_type'] = df['floor'].str.split('（').str[0].astype('category')
def fun1(str1):
    if pd.isna(str1):
        return '未知'
    elif '低' in str1:
        return '低楼层'
    elif '中' in str1:
        return '中楼层'
    elif '高' in str1:
        return '高楼层'
    else:
        return '未知'
df['floor_type2'] = df['floor'].apply(fun1).astype('category')
# 是否是直辖市zxs
df['zxs'] = df['city'].apply(lambda x: 1 if x in ['北京','上海','天津','重庆'] else 0)
# 卧室的数量bedrooms
df['bedrooms'] = df['rooms'].str.split('室').str[0].astype(int)
# 客厅的数量livingrooms
# df['rooms'].str.split('室').str[1].str.split('厅').str[0].astype(int)
df['livingrooms'] = df['rooms'].str.extract(r'(\d+)厅').astype('int')
# 楼龄building_age
df['building_age'] = 2025 - df['year']
# 价格的分段price_labels
df['price_labels'] = pd.cut(df['price'],bins=4,labels=['低价','中价','高价','豪华'])

# 6. 问题分析及可视化

'''
问题编号: A1
问题: 哪些变量最影响房价？面积、楼层、房间数哪个影响更大？
分析主题: 特征相关性
分析目标: 了解房屋各特征对房价的线性影响
分组字段: 无
指标/方法: 皮尔逊相关系数
'''
# 选择数值型特征
a = df[['price','area','unit','building_age']].corr()#相关系数
# 对房价的影响最大的几个因素的排序
a['price'].sort_values(ascending=False)[1:]
# 相关性的热力图
plt.figure(figsize = (5,5))
sns.heatmap(a,cmap='coolwarm')
plt.title('房屋特征相关性热力图')
plt.tight_layout()
# df.head()

'''
问题编号: A2
问题: 全国房价总体分布是怎样的？是否存在极端值？
分析主题: 描述性统计
分析目标: 概览数值型字段的分布特征
分组字段: 无
指标/方法: 平均数/中位数/四分位数/标准差
'''
df.describe()
# 房价分布直方图
plt.subplot(111)
plt.hist(df['price'],bins=10)
df.head()
sns.histplot(data=df,x='price',bins=10,kde=True)
```

### 分析与可视化

`df.corr()` 相关性 + `sns.heatmap()` 热力图 / 房价分布直方图 / `groupby("city")` 各城市均价 / 户型均价 / 分箱分析

```python
'''
问题编号: A3
问题: 哪些城市房价最高？直辖市与非直辖市差异如何？
分析主题: 城市对比
分析目标: 比较不同城市房价水平
分组字段: city
指标/方法: 均价/单价中位数/箱线图
'''
# 按城市统计
city_stats = df.groupby('city').agg({
    'price': ['mean', 'median', 'count'],
    'unit': ['mean', 'median']
})
print("\n各城市房价统计:")
display(city_stats.sort_values(('unit', 'mean'), ascending=False).head(10))

# 可视化前10城市
top_cities = city_stats.sort_values(('unit', 'mean'), ascending=False).head(10).index
df_top = df[df['city'].isin(top_cities)]

plt.figure(figsize=(12, 6))
sns.boxplot(x='city', y='price', data=df_top, order=top_cities)
plt.title('TOP10城市房价分布对比', fontsize=14)
plt.xlabel('城市')
plt.ylabel('价格(元)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''
问题编号: A4
问题: 高价房在面积、楼层等方面有什么特征？
分析主题: 价格分层
分析目标: 识别不同价位房屋特征差异
分组字段: 价格分段(低中高)
指标/方法: 列联表/卡方检验
'''
"""A4 价格分层特征差异分析"""
print("\n=== A4 价格分层特征差异 ===")

# 按价格分段分析特征
price_group = df.groupby('price_labels').agg({
    'area': ['mean', 'median'],
    'building_age': 'mean',
    'unit': 'median',
    'zxs': 'mean'  # 直辖市占比
})

print("\n各价格层级特征对比:")
display(price_group)

# 可视化
plt.figure(figsize=(14, 5))

plt.subplot(131)
sns.barplot(x='price_labels', y='area', data=df, estimator=np.median)
plt.title('不同价格层级面积对比')
plt.ylabel('面积(㎡)')

plt.subplot(132)
sns.boxplot(x='price_labels', y='building_age', data=df)
plt.title('不同价格层级楼龄分布')
plt.ylabel('楼龄(年)')


plt.tight_layout()
plt.show()

'''
问题编号: A5
问题: 哪种户型最受欢迎？三室比两室贵多少？
分析主题: 户型分析
分析目标: 分析不同户型的市场表现
分组字段: rooms
指标/方法: 占比/平均单价/溢价率
'''
"""A5 户型市场表现分析"""
print("\n=== A5 户型分析 ===")

# 提取房间数（示例："3室2厅" -> 3）
df['room_count'] = df['rooms'].str.extract('(\d+)室').astype(float)

# 按户型统计
room_stats = df.groupby('room_count').agg({
    'price': ['mean', 'median'],
    'unit': 'median',
    'area': 'median',
    'city': 'nunique'
}).sort_values(('price', 'mean'))

print("\n各户型市场表现:")
display(room_stats)

# 可视化
plt.figure(figsize=(14, 5))

plt.subplot(131)
sns.boxplot(x='room_count', y='price', data=df)
plt.title('不同户型总价分布')
plt.xlabel('房间数')

plt.subplot(132)
sns.scatterplot(x='area', y='price', hue='room_count', data=df, palette='viridis')
plt.title('面积-价格-户型关系')

plt.subplot(133)
sns.barplot(x='room_count', y='unit', data=df, estimator=np.median)
plt.title('不同户型单价对比')
plt.xlabel('房间数')

plt.tight_layout()
plt.show()

'''
问题编号: A6
问题: 南北向是否真比单一朝向贵？贵多少？
分析主题: 朝向溢价
分析目标: 评估不同朝向的价格差异
分组字段: toward
指标/方法: 方差分析/多重比较
'''
df['toward'].value_counts()
df.groupby('toward').agg({
    'price':['mean','median'],
    'unit':'median',
    'building_age':'mean',
})
# 数据可视化
plt.figure(figsize=(14, 5))
sns.boxplot(x='toward', y='price', data=df)
plt.tight_layout()
```

---

## 数据集清单

| 文件 | 用途 |
|------|------|
| `data/weather.csv` (~50KB) | DataFrame 基础操作 |
| `data/weather_withna.csv` (~43KB) | 缺失值处理专项 |
| `data/sleep.csv` (~28KB) | GroupBy 分组聚合 |
| `data/penguins.csv` (~15KB) | Seaborn 可视化 |
| `data/employees.csv` (~7KB) | merge/concat 合并 |
| `data/house_sales.csv` (~20MB) | 综合项目 |
| `data/products.json` / `test.json` | JSON 解析 |

---

## 常用 API 速查

### NumPy
| 操作 | API |
|------|-----|
| 创建 | `np.array()` `np.zeros()` `np.ones()` `np.arange()` `np.linspace()` `np.random.randn()` |
| 属性 | `.shape` `.ndim` `.size` `.dtype` |
| 变形 | `.reshape()` `.flatten()` `.T` |
| 统计 | `.sum()` `.mean()` `.std()` `.min()` `.max()` `.median()` `.quantile()` |
| 运算 | `+ - * /` `@` `np.dot()` `np.sqrt()` `np.exp()` |
| 索引 | `arr[i]` `arr[i:j]` `arr[i,j]` `arr[bool_mask]` |

### Pandas
| 操作 | API |
|------|-----|
| 读取 | `pd.read_csv()` `pd.read_json()` |
| 写入 | `.to_csv()` `.to_json()` |
| 查看 | `.head()` `.info()` `.describe()` `.dtypes` `.shape` |
| 筛选 | `df["col"]` `.loc[]` `.iloc[]` `.query()` |
| 清洗 | `.dropna()` `.fillna()` `.drop_duplicates()` `.astype()` |
| 分组 | `.groupby()` `.agg()` `.transform()` |
| 合并 | `pd.concat()` `.merge()` `.join()` |
| 排序 | `.sort_values()` `.sort_index()` |
| 转换 | `pd.to_datetime()` `.astype("category")` `.round()` |

### Matplotlib
| 图表 | `plt.plot()` `plt.bar()` `plt.scatter()` `plt.hist()` `plt.pie()` |
| 修饰 | `plt.title()` `plt.xlabel()` `plt.ylabel()` `plt.legend()` `plt.grid()` |
| 显示 | `plt.show()` `plt.tight_layout()` |

## 学习建议

| 阶段        | 任务                                       | 时间    |
| --------- | ---------------------------------------- | ----- |
| 1. 理论     | 阅读本笔记第 1 章，建立全貌认知                        | 30min |
| 2. NumPy  | 逐行执行 `1.numpy学习.ipynb` 全部 63 单元          | 2-3h  |
| 3. Pandas | 依次执行 Series → DataFrame → 分析 三个 notebook | 3-4h  |
| 4. 可视化    | 执行 Matplotlib + Seaborn 两个 notebook      | 1-2h  |
| 5. 实战     | 独立完成 `7.房地产市场分析.ipynb`                   | 2-3h  |
| 6. 扩展     | 用 `data/` 下其他数据集自行设计分析任务                 | 不限    |
