---
domain: IT_Technology
tags: [Python, 打包, PyInstaller]
status: 稳定
created: 2026-06-12
summary: "PyInstaller 单文件打包（-F -w）是中小型 Python GUI 项目分发首选，配合 spec 文件可精细控制依赖与资源"
---
以下是使用 Python 打包工具将程序转换为独立 EXE 文件的详细指南：

---

### 一、常用打包工具对比

|                 |                        |                |
| --------------- | ---------------------- | -------------- |
| 工具名称            | 特点                     | 适用场景           |
| **PyInstaller** | 跨平台、支持单文件打包、易用性高       | 中小型项目首选        |
| **cx_Freeze**   | 官方推荐、支持多平台、需手动配置       | 需要精细控制依赖的项目    |
| **py2exe**      | 仅限 Windows、配置复杂        | 旧项目兼容性维护       |
| **Nuitka**      | 将 Python 编译为 C 代码、性能优化 | 需要保护源码或提升性能的项目 |

---

### 二、使用 PyInstaller (推荐)

#### 1. 安装 PyInstaller

```python
pip install pyinstaller
```

#### 2. 基础打包命令

```python
# 打包为单个 EXE 文件（包含所有依赖）
pyinstaller -F -w your_script.py

# 打包为文件夹（便于调试）
pyinstaller -D your_script.py
```

#### 常用参数说明：

- `-F` (`--onefile`)：生成单个 EXE 文件
- `-w` (`--windowed`)：隐藏控制台窗口（GUI 程序必选）
- `--icon=app.ico`：设置 EXE 图标
- `--add-data "src;dest"`：添加额外资源文件
- `--hidden-import module`：手动指定隐藏依赖

---

### 三、打包 wxPython 程序示例

#### 1. 示例代码 (`demo.py`)

```python
import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Hello World")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
```

#### 2. 打包命令

```python
# 生成单文件 + 隐藏控制台 + 自定义图标
pyinstaller -F -w --icon=app.ico demo.py
```

#### 3. 处理资源文件

如果程序包含图片、配置文件等资源：

```python
# 将 images 文件夹打包到 exe 同级目录
pyinstaller -F -w --add-data "images/*;images/" demo.py
```

代码中需添加资源路径处理：

```python
import sys
import os

# 获取临时解压路径（仅单文件模式需要）
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

image_path = os.path.join(base_path, "images/logo.png")
```

---

### 四、常见问题解决方案

#### 1. 文件体积过大

- **使用 UPX 压缩**：

```python
pyinstaller -F --upx-dir=/path/to/upx your_script.py
```

1. 下载 [UPX](https://upx.github.io/)
2. 打包时添加参数：

- **清理无用依赖**：  
    使用虚拟环境打包：

```python
# 创建干净环境
python -m venv venv
venv\Scripts\activate
pip install pyinstaller wxPython
```

#### 2. 缺失动态库

- 手动指定隐藏导入：

```python
pyinstaller --hidden-import=wx.sipp your_script.py
```

#### 3. 防病毒软件误报

- 使用代码签名证书（需购买）
- 提交到杀毒软件厂商白名单

---

### 五、进阶配置（`spec` 文件）

通过生成 spec 文件进行精细控制：

```python
pyi-makespec your_script.py
```

编辑生成的 `your_script.spec`：

```python
a = Analysis(
    ['your_script.py'],
    binaries=[],
    datas=[('images/*', 'images')],  # 添加资源文件
    hiddenimports=['wx.sipp'],       # 指定隐藏依赖
    ...
)
```

使用 spec 文件打包：

```python
pyinstaller your_script.spec
```

---

### 六、其他工具示例（cx_Freeze）

#### 1. 安装

```python
pip install cx_Freeze
```

#### 2. 创建 `setup.py`

```python
from cx_Freeze import setup, Executable

build_options = {
    "packages": ["wx"],
    "excludes": ["tkinter"],
    "include_files": ["images/"]
}

setup(
    name="MyApp",
    version="1.0",
    description="My wxPython App",
    options={"build_exe": build_options},
    executables=[Executable("demo.py", base="Win32GUI")]
)
```

#### 3. 执行打包

```python
python setup.py build
```

---

### 七、最佳实践建议

1. **分层测试**：先打包简单程序验证基础功能
2. **多平台验证**：在目标系统（如纯净版 Windows）测试
3. **版本管理**：记录所有依赖库版本（使用 `pip freeze > requirements.txt`）
4. **日志调试**：打包时保留控制台查看错误信息

---

通过以上步骤，您可以将 Python 程序高效地打包为可执行文件。PyInstaller 在大多数情况下能提供开箱即用的解决方案，而 cx_Freeze 则适合需要深度定制的场景。
