---
domain: IT_Technology
status: 稳定
summary: PyQt6 官方文档核心参考：安装、信号槽、核心控件、布局、对话框、Model/View、QSS 样式、打包发布
tags: [Python, PyQt6, GUI, Qt]
created: 2026-06-14
source: https://maicss.com/pyqt/v6/ (PyQt6 中文文档)
---

# PyQt6 核心参考

> 基于官方文档体系整理。在线文档：[PyQt6 中文文档](https://maicss.com/pyqt/v6/)

## 一、安装与第一个窗口

### 安装

```bash
pip install PyQt6
```

### 最小应用

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)    # 每个 PyQt 应用必须创建一个 QApplication

window = QWidget()
window.setWindowTitle("第一个窗口")
window.resize(400, 300)
window.show()

sys.exit(app.exec())            # 进入事件循环
```

> **关键**：`app.exec()` 启动事件循环，`sys.exit()` 确保程序正常退出。

## 二、信号与槽（Signals & Slots）

Qt 的核心通信机制。控件状态变化时发射**信号**，**槽**是响应信号的函数。

### 基本连接

```python
button = QPushButton("点击")
button.clicked.connect(on_clicked)       # 信号.connect(槽函数)

def on_clicked():
    print("按钮被点击")
```

### 带参数的信号

```python
slider = QSlider()
slider.valueChanged.connect(on_value_changed)   # 信号自带参数

def on_value_changed(value):
    print(f"当前值: {value}")
```

### 自定义信号

```python
from PyQt6.QtCore import pyqtSignal, QObject

class MyObject(QObject):
    my_signal = pyqtSignal(str)           # 定义带 str 参数的信号

obj = MyObject()
obj.my_signal.connect(lambda msg: print(msg))
obj.my_signal.emit("Hello")
```

### 常用控件信号速查

| 控件 | 常用信号 |
|------|---------|
| `QPushButton` | `clicked()`, `pressed()`, `released()` |
| `QLineEdit` | `textChanged(str)`, `returnPressed()` |
| `QCheckBox` | `stateChanged(int)` |
| `QComboBox` | `currentIndexChanged(int)`, `currentTextChanged(str)` |
| `QSlider` | `valueChanged(int)`, `sliderMoved(int)` |
| `QSpinBox` | `valueChanged(int)` |
| `QListWidget` | `currentRowChanged(int)`, `itemClicked(QListWidgetItem)` |

## 三、核心控件速查

### 按钮类

| 控件 | 说明 |
|------|------|
| `QPushButton` | 普通按钮 |
| `QRadioButton` | 单选按钮 |
| `QCheckBox` | 复选框 |
| `QToolButton` | 工具栏按钮 |

### 输入类

| 控件 | 说明 |
|------|------|
| `QLineEdit` | 单行文本框 |
| `QTextEdit` | 多行富文本编辑 |
| `QPlainTextEdit` | 多行纯文本编辑 |
| `QSpinBox` | 整数微调框 |
| `QDoubleSpinBox` | 浮点微调框 |
| `QComboBox` | 下拉组合框 |
| `QDateEdit` / `QTimeEdit` | 日期/时间选择 |

### 显示类

| 控件 | 说明 |
|------|------|
| `QLabel` | 标签（文本、图片、动图） |
| `QProgressBar` | 进度条 |
| `QLCDNumber` | LCD 数字显示 |

### 容器类

| 控件 | 说明 |
|------|------|
| `QGroupBox` | 带标题的分组框 |
| `QTabWidget` | 标签页容器 |
| `QStackedWidget` | 堆叠页面 |
| `QScrollArea` | 滚动区域 |
| `QSplitter` | 可拖拽分割面板 |

### 列表/树/表

| 控件 | 说明 |
|------|------|
| `QListWidget` | 列表控件 |
| `QTreeWidget` | 树形控件 |
| `QTableWidget` | 表格控件 |

## 四、布局管理

### 四种基本布局

```python
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

# 水平布局
hbox = QHBoxLayout()
hbox.addWidget(QPushButton("左"))
hbox.addWidget(QPushButton("右"))

# 垂直布局
vbox = QVBoxLayout()
vbox.addWidget(QLabel("上方"))
vbox.addWidget(QLabel("下方"))

# 网格布局
grid = QGridLayout()
grid.addWidget(QPushButton("(0,0)"), 0, 0)
grid.addWidget(QPushButton("(0,1)"), 0, 1)
grid.addWidget(QPushButton("(1,0)"), 1, 0, 1, 2)  # 跨 2 列

# 表单布局
form = QFormLayout()
form.addRow("姓名:", QLineEdit())
form.addRow("年龄:", QSpinBox())
```

### 布局嵌套

```python
main_layout = QVBoxLayout()
main_layout.addLayout(hbox)       # 嵌套另一个布局
main_layout.addWidget(button)     # 添加控件
window.setLayout(main_layout)
```

### 常用方法

| 方法 | 说明 |
|------|------|
| `addStretch(n)` | 添加弹性空间（n 为拉伸因子） |
| `addSpacing(px)` | 添加固定间距（像素） |
| `setSpacing(px)` | 设置控件间距 |
| `setContentsMargins(l,t,r,b)` | 设置边距 |

## 五、对话框

### 标准对话框

```python
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QColorDialog, QFontDialog, QInputDialog

# 消息框
QMessageBox.information(window, "标题", "信息内容")
reply = QMessageBox.question(window, "确认", "确定删除？", 
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

# 文件对话框
file_path, _ = QFileDialog.getOpenFileName(window, "选择文件", "", 
    "图片 (*.png *.jpg);;所有文件 (*)")

# 保存文件
save_path, _ = QFileDialog.getSaveFileName(window, "保存", "untitled.txt", 
    "文本 (*.txt)")

# 颜色选择
color = QColorDialog.getColor()

# 输入对话框
text, ok = QInputDialog.getText(window, "输入", "请输入姓名:")
num, ok = QInputDialog.getInt(window, "输入", "请输入年龄:", 25, 0, 150)
```

### QMessageBox 图标类型

| 方法 | 用途 |
|------|------|
| `information()` | 信息提示 |
| `warning()` | 警告 |
| `critical()` | 严重错误 |
| `question()` | 询问确认 |

## 六、菜单栏、工具栏、状态栏

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件(&F)")
        
        open_action = QAction("打开", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.on_open)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 工具栏
        toolbar = self.addToolBar("主工具栏")
        toolbar.addAction(open_action)

        # 状态栏
        self.statusBar().showMessage("就绪")
```

## 七、Model/View 编程

### 核心概念

| 组件 | 说明 |
|------|------|
| **Model** | 数据层，管理数据，通知 View 数据变化 |
| **View** | 显示层，从 Model 获取数据显示 |
| **Delegate** | 委托，控制数据的编辑和渲染 |

### 预定义 Model

```python
from PyQt6.QtCore import QStringListModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem

# 字符串列表模型
model = QStringListModel()
model.setStringList(["张三", "李四", "王五"])

# 标准项模型
model = QStandardItemModel()
model.setHorizontalHeaderLabels(["姓名", "年龄"])
model.appendRow([QStandardItem("张三"), QStandardItem("25")])

# View 绑定
list_view = QListView()
list_view.setModel(model)

tree_view = QTreeView()
tree_view.setModel(model)

table_view = QTableView()
table_view.setModel(model)
```

### 自定义 Model（继承 QAbstractTableModel）

```python
from PyQt6.QtCore import QAbstractTableModel, Qt

class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
```

## 八、QSS 样式表

用 CSS 语法美化界面：

```python
window.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3d8b40;
    }
    QLineEdit {
        border: 2px solid #ccc;
        border-radius: 4px;
        padding: 6px;
    }
    QLineEdit:focus {
        border-color: #4CAF50;
    }
""")
```

### QSS 常用选择器

| 选择器 | 示例 | 说明 |
|--------|------|------|
| 类型选择器 | `QPushButton` | 匹配所有该类型控件 |
| 类选择器 | `.myClass` | 匹配设置了该属性的控件 |
| ID 选择器 | `QPushButton#okBtn` | 匹配指定 objectName |
| 后代选择器 | `QWidget QPushButton` | 匹配容器内的子控件 |
| 伪状态 | `:hover`, `:pressed`, `:checked`, `:focus` | 匹配特定状态 |

## 九、多线程

GUI 操作必须在主线程；耗时任务应放入工作线程。

### QThread 方式

```python
from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def run(self):
        for i in range(101):
            self.progress.emit(i)
            self.msleep(50)        # 模拟耗时操作
        self.finished.emit("完成")

# 使用
self.worker = Worker()
self.worker.progress.connect(self.progress_bar.setValue)
self.worker.finished.connect(lambda msg: QMessageBox.information(self, "提示", msg))
self.worker.start()                 # 启动线程
```

### QThreadPool + QRunnable

```python
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSlot

class Task(QRunnable):
    def __init__(self, data):
        super().__init__()
        self.data = data

    @pyqtSlot()
    def run(self):
        # 耗时操作
        result = process(self.data)
        # 注意：不能在 QRunnable 中直接操作 UI
        # 需要通过信号或其他方式回传结果
```

## 十、常用模式与最佳实践

### 1. 面向对象组织窗口

```python
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("应用")
        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        # 集中创建控件
        pass
    
    def setup_connections(self):
        # 集中连接信号槽
        pass
```

### 2. 资源文件 (.qrc)

```xml
<!-- resources.qrc -->
<RCC>
    <qresource prefix="/icons">
        <file>icon.png</file>
    </qresource>
</RCC>
```

编译：`pyrcc6 resources.qrc -o resources_rc.py`

### 3. 打包发布

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=app.ico main.py
```

| 参数 | 说明 |
|------|------|
| `--onefile` | 打包为单个 exe |
| `--windowed` | 不显示控制台窗口 |
| `--icon=app.ico` | 指定图标 |
| `--add-data "src;dst"` | 包含额外文件 |

## 速查：常用类导入

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog,
    QPushButton, QLabel, QLineEdit, QTextEdit, QPlainTextEdit,
    QCheckBox, QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QListWidget, QTreeWidget, QTableWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QGroupBox, QTabWidget, QStackedWidget, QScrollArea,
    QMenuBar, QToolBar, QStatusBar,
    QMessageBox, QFileDialog, QColorDialog, QFontDialog, QInputDialog,
    QListView, QTreeView, QTableView,
)
from PyQt6.QtCore import (
    Qt, QThread, pyqtSignal, QTimer, QSize, QRect, QPoint,
    QAbstractTableModel, QAbstractListModel,
)
from PyQt6.QtGui import (
    QIcon, QPixmap, QFont, QColor, QAction, QKeySequence,
    QStandardItemModel, QStandardItem,
)
```

## 学习路径建议

1. **第 1 天**：安装 + 最小窗口 + 信号槽 + QPushButton/QLabel/QLineEdit
2. **第 2 天**：四种布局 + QMainWindow 框架（菜单/工具栏/状态栏）
3. **第 3 天**：对话框 + 其他输入控件（ComboBox/SpinBox/CheckBox）
4. **第 4 天**：列表/树/表格控件 + Model/View
5. **第 5 天**：QSS 样式 + 多线程 + 打包发布
