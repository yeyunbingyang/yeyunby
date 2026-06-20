## **range对象**

![[Pasted image 20260613005515.png]]

### 特点：

- **生成等差数列**，节省内存
- **语法**：`range(start, end, step)`

```python
# 创建
r = range(5)        # 0,1,2,3,4
r = range(2, 10, 3) # 2,5,8

# 转换为列表
list(r)  # [2,5,8]
```
