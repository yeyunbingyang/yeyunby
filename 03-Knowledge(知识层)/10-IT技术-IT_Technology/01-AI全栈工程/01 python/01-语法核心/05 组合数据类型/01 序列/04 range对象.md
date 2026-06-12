## **range对象**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1741255267067-d16d8ca6-28bb-4d8f-b8b0-9e15aadb2e3b.png)

### 特点：

- **生成****等差数列**，节省内存
- **语法**：`range(start, end, step)`

```
# 创建
r = range(5)        # 0,1,2,3,4
r = range(2, 10, 3) # 2,5,8

# 转换为列表
list(r)  # [2,5,8]
```