- 官方文档：[https://docs.wxpython.org/](https://docs.wxpython.org/)
- 示例代码库：`wxPython/demo`（安装后自带）
- 书籍：《wxPython in Action》

---

### 一、wxPython 简介

wxPython 是基于 C++ 的 wxWidgets GUI 库的 Python 封装，支持跨平台开发（Windows/macOS/Linux）。

#### 特点：

- 原生外观控件
- 丰富的组件库
- 灵活的布局管理（Sizers）
- 支持事件驱动编程

---

### 二、环境安装

```python
pip install wxPython
```

---

### 三、基础框架结构

#### 核心组件：

- `wx.App`: 应用程序对象（必须且只能有一个）
- `wx.Frame`: 主窗口容器
- `MainLoop()`: 启动事件循环

#### 最简单的窗口

面向 对象方式维护界面

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        # 调用父类构造函数，创建窗口
        # parent=None 表示这是顶级窗口
        # title 设置窗口标题
        super().__init__(parent=None, title="Hello wxPython")
        # 创建面板
        pl = wx.Panel(self)
        # 创建静态文本
        staticText = wx.StaticText(pl,label='欢迎学习python')
        # 创建按钮
        btn = wx.Button(pl,label='开始学习',pos=(300,400))

if __name__ == "__main__": # python程序主入口
    # 创建应用程序对象（每个 wxPython 程序必须有且只有一个 App 实例）
    app = wx.App()
    
    # 创建窗口实例
    frame = MyFrame()

    # 显示窗口
    frame.show()
    
    # 启动主事件循环（监听用户操作和系统事件）保持窗口显示
    app.MainLoop()
```

---

### 四、常用控件

组件创建第一个参数都是指父组件

#### 常用控件列表：

- wx.Panel：面板
- `wx.Button`: 按钮
- `wx.StaticText`: 静态文本
- `wx.TextCtrl`: 单行/多行文本框
- `wx.CheckBox`: 复选框
- `wx.RadioButton`: 单选按钮
- `wx.ListBox`: 列表框
- `wx.ComboBox`: 下拉框

#### 基础控件示例

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="控件示例")
        
        # 创建面板：建议将所有控件放在 Panel 上
        # 可避免 Windows 系统下的背景色问题
        panel = wx.Panel(self)  

        # 创建静态文本控件
        # pos 参数指定位置 (x,y)
        self.label = wx.StaticText(panel, label="Hello World!", pos=(20, 20))
        
        # 创建按钮控件
        # 绑定点击事件到 on_click 方法
        self.btn = wx.Button(panel, label="点击我", pos=(20, 50))
        self.btn.Bind(wx.EVT_BUTTON, self.on_click)
        
        # 创建单行文本框
        # size=(200, -1) 表示宽度200，高度默认
        self.text = wx.TextCtrl(panel, pos=(20, 80), size=(200, -1))

    def on_click(self, event):
        """按钮点击事件处理函数"""
        # 获取文本框内容
        input_text = self.text.GetValue()
        
        # 更新标签文本
        self.label.SetLabel(f"你输入了：{input_text}")

# ... 运行代码与基础框架相同 ...
```

---

### 五、布局管理（Sizers）

#### Sizer 参数说明：

- `proportion`: 控件在剩余空间中的占比（0=固定大小）
- `flag`: 布局标志（如 `wx.EXPAND` 填满空间，`wx.ALL` 四周边距）
- `border`: 边距大小（单位：像素）

#### 常用 Sizers：

- `wx.BoxSizer`: 线性布局（水平/垂直）
- `wx.GridSizer`: 网格布局
- `wx.FlexGridSizer`: 灵活网格布局
- `wx.GridBagSizer`: 复杂网格布局

#### BoxSizer 示例

```python
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="布局示例")
        panel = wx.Panel(self)
        
        # 创建垂直方向的 BoxSizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # 创建可扩展的文本框（占满剩余空间）
        self.text = wx.TextCtrl(panel)
        
        # 创建两个按钮
        btn_ok = wx.Button(panel, label="确定")
        btn_cancel = wx.Button(panel, label="取消")

        # 添加控件到 sizer：
        # - text 控件占 1 份剩余空间（proportion=1）
        # - 四周保留 5 像素边距（border=5）
        # - wx.EXPAND 表示控件填满分配空间
        sizer.Add(self.text, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        
        # 按钮只占用固定高度（proportion=0）
        # 左右边距 5 像素（不包含上下边距）
        sizer.Add(btn_ok, proportion=0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        
        # 第二个按钮四周保留 5 像素边距
        sizer.Add(btn_cancel, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        
        # 将 sizer 应用到面板
        panel.SetSizer(sizer)
```

---

### 六、事件处理

#### 绑定事件示例

```python
class MyFrame(wx.Frame):
    def __init__(self):
        # ... 初始化控件代码 ...
        
        # 绑定按钮点击事件到处理方法
        # wx.EVT_BUTTON 是按钮点击事件类型
        self.btn.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        # 绑定窗口关闭事件
        # 当用户点击关闭按钮时触发
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_button_click(self, event):
        """按钮点击事件处理"""
        # 显示信息对话框
        # wx.OK 显示确定按钮
        # wx.ICON_INFORMATION 显示信息图标
        wx.MessageBox("按钮被点击了！", "提示", wx.OK|wx.ICON_INFORMATION)

    def on_close(self, event):
        """窗口关闭事件处理"""
        # 创建确认对话框
        dlg = wx.MessageDialog(
            None, 
            "确定要退出吗？", 
            "确认", 
            wx.YES_NO  # 显示是/否按钮
        )
        
        # 显示模态对话框（阻塞其他窗口操作）
        if dlg.ShowModal() == wx.ID_YES:
            # 销毁窗口（退出程序）
            self.Destroy()
        dlg.Destroy()  # 必须手动销毁对话框
```

#### 常见事件类型：

- `wx.EVT_BUTTON`: 按钮点击
- `wx.EVT_TEXT`: 文本内容改变
- `wx.EVT_CHECKBOX`: 复选框状态改变
- `wx.EVT_CLOSE`: 窗口关闭
- `wx.EVT_MENU`: 菜单项选择

---

### 七、高级功能

#### 1. 菜单栏

```python
class MyFrame(wx.Frame):
    def __init__(self):
        # ... 其他初始化代码 ...
        
        # 创建菜单栏
        menubar = wx.MenuBar()
        
        # 创建文件菜单
        file_menu = wx.Menu()
        
        # 添加菜单项：
        # - wx.ID_OPEN 是预定义的标准ID（会自动处理图标和快捷键）
        # - "打开" 是显示的文本
        # - "打开文件" 是状态栏提示
        item_open = file_menu.Append(wx.ID_OPEN, "打开", "打开文件")
        
        # 添加分隔线
        file_menu.AppendSeparator()
        
        # 退出项
        item_exit = file_menu.Append(wx.ID_EXIT, "退出", "退出程序")
        
        # 将菜单添加到菜单栏
        menubar.Append(file_menu, "文件")
        
        # 设置窗口菜单栏
        self.SetMenuBar(menubar)
        
        # 绑定退出菜单项事件
        self.Bind(wx.EVT_MENU, self.on_exit, item_exit)
```

#### 2. 对话框

```python
# 创建文件选择对话框
dlg = wx.FileDialog(
    None, 
    "选择文件",         # 对话框标题
    wildcard="All files (*.*)|*.*",  # 文件过滤器
    style=wx.FD_OPEN   # 对话框样式（打开文件）
)

# 显示模态对话框
if dlg.ShowModal() == wx.ID_OK:
    # 获取用户选择的文件路径
    selected_path = dlg.GetPath()
    print("选择的文件：", selected_path)

# 必须销毁对话框（释放资源）
dlg.Destroy()
```

---
