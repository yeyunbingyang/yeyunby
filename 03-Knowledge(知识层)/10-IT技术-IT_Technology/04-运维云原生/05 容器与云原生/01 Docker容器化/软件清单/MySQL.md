# MySQL 关键目录（重点）

|   |   |
|---|---|
|目录|作用|
|/var/lib/mysql|数据库数据|
|/docker-entrypoint-initdb.d|初始化SQL|
|/etc/mysql/conf.d|MySQL配置|

# MySQL 容器启动流程（理解很重要）

MySQL Docker 启动流程：

```
容器启动
     ↓
docker-entrypoint.sh
     ↓
检查 /var/lib/mysql
     ↓
为空 → 初始化数据库
     ↓
执行 initdb.d 目录 SQL
     ↓
启动 mysqld
```

所以：

⭐ 初始化 SQL **只会执行一次**

# 带初始化 SQL 的 MySQL Dockerfile（常用）

很多时候需要 **自动****创建****表****或****导入****数据**。

项目结构：

```
mysql/
 ├─ Dockerfile
 └─ init.sql
```

### Dockerfile

```
FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=123456
ENV MYSQL_DATABASE=test

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
```

---

### init.sql

```
CREATE TABLE user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50)
);

INSERT INTO user(name) VALUES('admin');
```

---

启动容器时 MySQL 会自动执行：

```
/docker-entrypoint-initdb.d/*.sql
```

这是 **MySQL 官方镜像提供的初始化机制**。