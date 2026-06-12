---
title: mysqlclient
domain: IT_Technology
tags: [Python, MySQL, 数据库, mysqlclient, MySQLdb]
status: 稳定
created: 2026-06-10
updated: 2026-06-10
source: ""
related: [[PyMySQL]], [[mysql-connector-python对比]]
summary: "mysqlclient 是 Python 连接 MySQL 的 C 扩展驱动（MySQLdb 的活跃 fork），性能约为 PyMySQL 的 2-3 倍，安装需编译环境，API 与 PyMySQL 几乎一致，是高并发生产环境的推荐选择"
---

# mysqlclient

## 一句话结论

> mysqlclient 是 MySQLdb 的现代化 fork，基于 C 扩展实现，性能碾压纯 Python 驱动（PyMySQL），但安装需要 C 编译器和 MySQL 开发库；如果你追求性能且能搞定编译环境，它应该是首选。

## 核心内容

### 1. 背景与定位

mysqlclient 是 Python 生态中**历史最悠久**的 MySQL 驱动。它 fork 自早已停更的 `MySQL-python`（即 `MySQLdb`），由社区持续维护至今。线程安全、兼容 Django 等主流框架，是许多生产环境的事实标准。

| 特性 | mysqlclient | PyMySQL |
|------|-------------|---------|
| 实现方式 | C 扩展（libmysqlclient） | 纯 Python |
| 性能 | 高（接近原生） | 中（约为 mysqlclient 的 1/3~1/2） |
| 安装难度 | 需 C 编译器 + MySQL 开发库 | `pip install` 即用 |
| 线程安全 | 是 | 否（需每个线程独立连接） |
| Django 默认 | 推荐 | 备选 |
| Python 版本支持 | 3.8+ | 3.7+ |

### 2. 安装

#### Windows

从 [ Christoph Gohlke 的非官方 wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) 下载预编译 `.whl` 再安装，或使用 conda：

```powershell
conda install mysqlclient
```

直接用 pip 在 Windows 上大概率失败（缺少 Visual C++ 编译环境）。

#### macOS

```bash
brew install mysql-client pkg-config
pip install mysqlclient
```

#### Linux（Debian/Ubuntu）

```bash
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install mysqlclient
```

#### Linux（CentOS/RHEL）

```bash
sudo yum install python3-devel mysql-devel gcc pkg-config
pip install mysqlclient
```

### 3. 使用方式

mysqlclient 遵循 Python DB-API 2.0 规范，API 与 PyMySQL **几乎完全相同**。如果已有 PyMySQL 代码，基本上改一行 import 即可切换：

```python
# PyMySQL
import pymysql

# mysqlclient（两种导入方式等价）
import MySQLdb
# 或
import mysqlclient  # 新版推荐
```

> ⚠️ 注意：传统上使用 `import MySQLdb`，但新版 mysqlclient 推荐 `import mysqlclient`。`%s` 占位符规则与 PyMySQL 一致。

#### 3.1 查询操作（SELECT）

```python
import MySQLdb

# 创建连接（参数名与 PyMySQL 略有不同）
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',      # mysqlclient 用 passwd，不是 password
    db='school',           # mysqlclient 用 db，不是 database
    charset='utf8mb4'
)

try:
    cursor = conn.cursor()

    sql = "SELECT id, name, age, gender, score FROM students WHERE class_id = %s"
    cursor.execute(sql, (3,))

    # 取单条
    row = cursor.fetchone()
    print(row)  # (1, '赵云', 22, '男', 98.0)

    # 取所有
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print(f"查询失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

#### 3.2 增加操作（INSERT）

```python
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, user='root',
    passwd='123456', db='school', charset='utf8mb4'
)

try:
    cursor = conn.cursor()

    sql = "INSERT INTO students (name, age, gender, score, class_id) VALUES (%s, %s, %s, %s, %s)"
    row_count = cursor.execute(sql, ('赵云', 22, '男', 98.0, 3))
    print(f"受影响行数: {row_count}")

    conn.commit()
    print("插入成功")

except Exception as e:
    print(f"插入失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

#### 3.3 修改操作（UPDATE）

```python
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, user='root',
    passwd='123456', db='school', charset='utf8mb4'
)

try:
    cursor = conn.cursor()

    sql = "UPDATE students SET score = %s WHERE name = %s"
    row_count = cursor.execute(sql, (95.0, '赵云'))
    print(f"更新行数: {row_count}")

    conn.commit()
    print("更新成功")

except Exception as e:
    print(f"更新失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

#### 3.4 删除操作（DELETE）

```python
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, user='root',
    passwd='123456', db='school', charset='utf8mb4'
)

try:
    cursor = conn.cursor()

    sql = "DELETE FROM students WHERE name = %s"
    row_count = cursor.execute(sql, ('赵云',))
    print(f"删除行数: {row_count}")

    conn.commit()
    print("删除成功")

except Exception as e:
    print(f"删除失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

#### 3.5 批量插入（executemany）

```python
import MySQLdb

conn = MySQLdb.connect(
    host='localhost', port=3306, user='root',
    passwd='123456', db='school', charset='utf8mb4'
)

students = [
    ('张飞', 23, '男', 85.0, 1),
    ('关羽', 24, '男', 92.0, 1),
    ('黄忠', 60, '男', 78.0, 2),
    ('马超', 21, '男', 88.0, 3),
]

try:
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, age, gender, score, class_id) VALUES (%s, %s, %s, %s, %s)"
    row_count = cursor.executemany(sql, students)
    print(f"批量插入行数: {row_count}")

    conn.commit()
    print("批量插入成功")

except Exception as e:
    print(f"批量插入失败: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

> mysqlclient 的 `executemany` 直接利用 C 扩展批量写入，比 PyMySQL 的纯 Python 循环快更多。

#### 3.6 上下文管理器

```python
import MySQLdb

config = {
    'host': 'localhost', 'port': 3306, 'user': 'root',
    'passwd': '123456', 'db': 'school', 'charset': 'utf8mb4'
}

try:
    with MySQLdb.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql = "SELECT name, score FROM students WHERE score > %s"
            cursor.execute(sql, (90,))
            for row in cursor.fetchall():
                print(f"姓名: {row[0]}, 成绩: {row[1]}")
except Exception as e:
    print(f"操作失败: {e}")
```

#### 3.7 返回字典（DictCursor）

```python
import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.connect(
    host='localhost', user='root', passwd='123456',
    db='school', charset='utf8mb4',
    cursorclass=MySQLdb.cursors.DictCursor
)

with conn.cursor() as cursor:
    cursor.execute("SELECT name, score FROM students LIMIT 1")
    row = cursor.fetchone()
    print(row['name'], row['score'])

conn.close()
```

### 4. 连接参数对比（mysqlclient vs PyMySQL）

| 含义 | mysqlclient | PyMySQL |
|------|-------------|---------|
| 主机 | `host` | `host` |
| 端口 | `port` | `port` |
| 用户 | `user` | `user` |
| 密码 | **`passwd`** | **`password`** |
| 数据库 | **`db`** | **`database`** |
| 字符集 | `charset` | `charset` |
| 自动提交 | `autocommit` | `autocommit` |
| 游标类型 | `cursorclass` | `cursorclass` |
| Unix Socket | `unix_socket` | `unix_socket` |
| 连接超时 | `connect_timeout` | `connect_timeout` |

> ⚠️ 最常见的坑：用 PyMySQL 的 `password=` / `database=` 参数名去连接 mysqlclient，直接报 `TypeError`。

### 5. 线程安全

mysqlclient 支持线程级别的安全访问，多线程环境下可以共享连接（但不推荐共享游标）：

```python
import MySQLdb
from threading import Thread

conn = MySQLdb.connect(
    host='localhost', user='root', passwd='123456', db='school', charset='utf8mb4'
)

def query_student(name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
    result = cursor.fetchone()
    cursor.close()
    print(f"{name}: {result}")

threads = [Thread(target=query_student, args=(name,)) for name in ['赵云', '关羽', '张飞']]
for t in threads:
    t.start()
for t in threads:
    t.join()

conn.close()
```

> PyMySQL 的同一个连接在多线程并发下可能出错，mysqlclient 则通过内部锁保证了连接级别的线程安全。

## 关键概念

- **C 扩展驱动**：底层调用 MySQL 官方的 `libmysqlclient` C 库，协议解析与数据传输在 C 层面完成
- **MySQLdb 兼容**：完全兼容旧版 MySQLdb 的 `import MySQLdb` 导入方式，老项目迁移零改动
- **连接参数差异**：`passwd`（非 `password`）、`db`（非 `database`），这是与 PyMySQL 最显著的区别
- **线程安全**：连接对象可跨线程共享（内部有 GIL 保护），游标不应跨线程共享

## 适用场景

- Django / Flask 生产环境（Django 官方默认推荐 mysqlclient）
- 高并发场景：API 服务、数据平台、实时计算
- 大量数据读写：ETL 管道、批量迁移、报表生成
- 已安装 MySQL 开发库的环境（Linux 服务器、Docker 镜像）

## 最佳实践

- **生产环境优先 mysqlclient**：性能优势明显，社区成熟度高
- **Docker 部署**：基础镜像选 `python:3.x-slim` + `apt install default-libmysqlclient-dev` 一行搞定编译依赖
- **参数名别写错**：`passwd` / `db` 而非 `password` / `database`
- **连接池必用**：搭配 DBUtils 或 SQLAlchemy 连接池，避免频繁建立/断开 TCP 连接
- **字符集始终 utf8mb4**：与 PyMySQL 一样，MySQL 的 `utf8` 是不完全 UTF-8

## 反例与边界

- **Windows 安装地狱**：pip install 大概率失败，优先用 conda 或预编译 wheel
- **from MySQLdb import ...**：旧式导入在 mysqlclient 2.x 中仍可用，但 3.x 可能移除，建议逐步迁移到 `import MySQLdb`
- **mysqlclient 不支持异步**：如需 `async/await` 操作 MySQL，用 `aiomysql`（底层也是 PyMySQL）
- **不要混用驱动**：同一项目中只用一个 MySQL 驱动，混用 mysqlclient 和 PyMySQL 的 `%s` 占位规则虽一致但连接对象不互通

## 可行动建议

- 新项目启动时先尝试 `pip install mysqlclient`——如果装上了，直接用不用犹豫
- 若编译失败，退回 PyMySQL：`pip install pymysql`，代码只需改 import 和参数名
- 将连接参数配置化（环境变量 / 配置文件），切换驱动时只改配置而非代码
- Django 项目：默认 `'ENGINE': 'django.db.backends.mysql'` 底层自动使用 mysqlclient

## 延伸与关联

- 相关笔记：[[PyMySQL]]、[[mysql-connector-python对比]]
- 可继续研究：Django 数据库配置、DBUtils 连接池、aiomysql（异步方案）、SQLAlchemy + mysqlclient dialect