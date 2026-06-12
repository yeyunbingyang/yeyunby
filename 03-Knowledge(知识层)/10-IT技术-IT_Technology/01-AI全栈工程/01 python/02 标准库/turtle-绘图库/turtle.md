`turtle` 是 Python 自带的一个非常有趣、易上手的**绘图库**，主要用于教学、图形化编程和理解编程逻辑。它可以让“小乌龟”在窗口中移动、画线、填色、绘制图形。

下面我帮你分层讲解，适合初学者系统学习使用：

---

## 🧩 一、基本介绍

- 模块名：`turtle`（标准库，无需安装）
- 功能：控制一只“小乌龟”在画布上移动、旋转、画图。
- 运行方式：只要你的 Python 安装完整，在任何编辑器或 IDLE 中运行如下即可：

```
import turtle
turtle.forward(100)
turtle.done()
```

✅ 程序运行后，会弹出一个窗口，有一只小乌龟向前走并画出一条线。

---

## ✏️ 二、常用命令（动作控制）

动作指令

含义

示例

`turtle.forward(x)`

向前移动 x 像素

`turtle.forward(100)`

`turtle.backward(x)`

向后移动 x 像素

`turtle.backward(50)`

`turtle.right(angle)`

右转 angle 度

`turtle.right(90)`

`turtle.left(angle)`

左转 angle 度

`turtle.left(45)`

`turtle.goto(x, y)`

移动到坐标 (x, y)

`turtle.goto(50, -50)`

`turtle.setheading(angle)`

朝向某角度（0 向右，90 向上）

`turtle.setheading(180)`

`turtle.penup()`

抬笔（移动时不画线）

`turtle.pendown()`

落笔（移动时画线）

---

## 🎨 三、画笔样式与颜色

指令

说明

示例

`turtle.pensize(width)`

画笔粗细

`turtle.pensize(3)`

`turtle.pencolor("red")`

画笔颜色

`turtle.pencolor("blue")`

`turtle.fillcolor("yellow")`

填充颜色

`turtle.fillcolor("green")`

`turtle.speed(n)`

移动速度 (1~10 或 "fastest")

`turtle.speed(5)`

### 🟡 填充形状

```
import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()      # 开始填充
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()        # 结束填充
turtle.done()
```

---

## 🌀 四、常见图形示例

### 1. 画正方形

```
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()
```

### 2. 画多边形

```
import turtle

n = 6   # 边数
for i in range(n):
    turtle.forward(100)
    turtle.right(360 / n)

turtle.done()
```

### 3. 画圆与弧线

```
import turtle

turtle.circle(50)     # 半径50的圆
turtle.circle(80, 180)  # 半圆（画圆弧）

turtle.done()
```

---

## 🧠 五、控制窗口与坐标

指令

功能

`turtle.setup(width, height)`

设置窗口大小

`turtle.setworldcoordinates(llx, lly, urx, ury)`

设置坐标系范围

`turtle.hideturtle()`

隐藏乌龟

`turtle.showturtle()`

显示乌龟

`turtle.clear()`

清空画布但不关闭

`turtle.reset()`

复位画布与乌龟位置

`turtle.done()`

程序结束时保持窗口打开

示例：

```
import turtle

turtle.setup(600, 400)
turtle.hideturtle()
turtle.goto(-100, 0)
turtle.pencolor("red")
turtle.write("Hello Turtle!", font=("Arial", 18, "bold"))

turtle.done()
```

---

## 💫 六、综合小例子：绘制五角星

```
import turtle

turtle.color("orange")
turtle.begin_fill()

for i in range(5):
    turtle.forward(150)
    turtle.right(144)   # 五角星的关键角度

turtle.end_fill()
turtle.done()
```

---

## 🧩 七、事件交互（进阶）

`turtle` 还可以处理键盘、鼠标事件，比如：

```
import turtle

def move_up():
    turtle.setheading(90)
    turtle.forward(50)

turtle.listen()
turtle.onkey(move_up, "Up")

turtle.done()
```

↑ 键即可让乌龟前进，类似小游戏逻辑。

---

## ✅ 八、总结速记表

类别

常用函数

作用

移动

`forward()`, `backward()`, `goto()`

控制位置

转向

`right()`, `left()`, `setheading()`

控制方向

状态

`penup()`, `pendown()`, `hideturtle()`

控制画笔状态

样式

`pencolor()`, `pensize()`, `fillcolor()`

控制样式

画图

`circle()`, `dot()`, `begin_fill()/end_fill()`

绘制形状

系统

`clear()`, `reset()`, `done()`

控制窗口与状态

交互

`onkey()`, `listen()`, `onclick()`

事件绑定
