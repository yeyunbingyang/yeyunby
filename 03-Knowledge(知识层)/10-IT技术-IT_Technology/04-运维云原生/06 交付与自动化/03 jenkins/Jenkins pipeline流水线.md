# Jenkins pipeline流水线

# Pipeline介绍

## 什么是 Jenkins Pipeline?

- **Pipeline** 是 Jenkins 的“自动化流程脚本”，用代码描述整个软件交付生命周期，如拉取代码、编译、测试、部署、发布等流程，实现标准化、自动化、一键上线。Pipeline 的定义文件通常叫做 `Jenkinsfile`，可以和源码一起维护。

## Jenkins Pipeline优势

**一切皆代码**：流程、环境、步骤全部用代码描述，易回溯、可追溯、团队协作方便。

**可视化**：自动生成流程图，方便运维与开发查看流程。

**标准化与复用**：企业统一规范、减少人工失误。

# Jenkins Pipeline 基本语法

## 两种主要语法

- **声明式（Declarative）**：推荐，结构化、层级清晰，易读易维护。

- **脚本式（Scripted）**：自由度高，用Groovy语法，适合复杂逻辑或老项目。

[https://www.jenkins.io/zh/doc/book/pipeline/](https://www.jenkins.io/zh/doc/book/pipeline/)

## 声明式语法

就像写菜单、列流程表，**格式严谨、简单明了，结构像“包裹套娃”**。

```
pipeline {
    agent any   // 在任何Jenkins节点执行
    stages {
        stage('第一步：拉代码') {
            steps {
                echo '拉取代码'
            }
        }
        stage('第二步：编译') {
            steps {
                echo '编译代码'
            }
        }
        stage('第三步：部署') {
            steps {
                echo '部署到服务器'
            }
        }
    }
}
```

**重点记住：**

- `pipeline {}` 最外层

- 里面是 `stages {}`，一堆 `stage {}`，每个stage就是一个步骤

- 每个`stage`下都有`steps`，里面是要执行的命令

## 脚本式语法

更像写脚本、写程序，**格式自由，控制更灵活**。

```
node {
    stage('拉代码') {
        echo '拉取代码'
    }
    stage('编译') {
        echo '编译代码'
    }
    stage('部署') {
        echo '部署到服务器'
    }
}
```

**重点记住：**

- `node {}` 是最外层

- 里面直接写 `stage('步骤名')`，每个stage写一步要做的事

- 想加if判断、循环、try-catch等复杂逻辑都可以直接写

## 两种写法对比

|   |   |   |
|---|---|---|
|目的|声明式写法|脚本式写法|
|拉代码|`stage('拉代码'){...}`|`stage('拉代码'){...}`|
|编译|`stage('编译'){...}`|`stage('编译'){...}`|
|部署|`stage('部署'){...}`|`stage('部署'){...}`|
|外层包裹|`pipeline {}` + `stages {}`|`node {}`|
|格式|结构化、标准、易看懂|脚本风格、自由灵活|

建议：

只需要会声明式写法就可以做80%以上的项目。

只要记住有`pipeline`、`stages`、`stage`、`steps`这几个“套娃”结构就不容易出错。

# Jenkins Pipeline项目部署

技术栈：CentOS、Git、Gitee、Jenkins（Pipeline）、Docker、Docker Compose

## 源码准备

第一步：创建Gitee仓库

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340878844-d487c2d4-0142-440d-bdae-b03520734751.png "null")

第二步：上传代码到本地仓库

拉取Gitee仓库

```
git clone git@gitee.com:centos9/wordpress.git
```

切换到wordpress目录

```
cd wordpress
```

放置代码到wordpress目录，然后提交到本地仓库并发布到Gitee仓库中

```
git add .
git commit -m "提交wordpress代码"

git push origin master
```

## 安装Jenkins插件

Pipeline、Git plugin、SCM API Plugin、Credentials Plugin、Credentials Binding Plugin（流水线用环境变量传递密码时使用）、Publish Over SSH

系统安装sshpass工具

```
dnf install sshpass -y
```

## 配置生产环境

安装Docker

```
[root@sever ~]# yum install wget -y
[root@sever ~]# wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo
[root@sever ~]# yum install docker-ce -y

[root@sever ~]# systemctl start docker
[root@sever ~]# systemctl enable docker
[root@sever ~]# systemctl status docker
```

安装Docker Compose

```
[root@sever ~]# mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
[root@sever ~]# chmod +x /usr/local/bin/docker-compose
```

Web环境部署

```
[root@sever ~]# mkdir web
[root@sever ~]# cd web
[root@sever ~]# mkdir www php mysql
[root@sever ~]# touch php/php.ini
[root@sever ~]# vim docker-compose.yml
services:
  nginx:
    image: nginx:1.25
    container_name: nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./www:/var/www/html
    depends_on:
      - php

  php:
    build: ./php
    container_name: php
    restart: always
    volumes:
      - ./www:/var/www/html
      - ./php/php.ini:/usr/local/etc/php/php.ini
    depends_on:
      - mysql

  mysql:
    image: mysql:8.0
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: wordpress
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/data:/var/lib/mysql
      
[root@sever ~]# vim php/Dockerfile
FROM php:8.3-fpm

# 安装常用WordPress依赖扩展
RUN apt-get update \
    && apt-get install -y libjpeg-dev libpng-dev libfreetype6-dev libzip-dev libonig-dev libicu-dev libxml2-dev libcurl4-openssl-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd exif zip mysqli pdo_mysql intl mbstring opcache

# 可选，安装curl扩展
RUN docker-php-ext-install curl

# 可选，推荐开启opcache配置（可提升php性能）
COPY php.ini /usr/local/etc/php/php.ini
```

运行Docker Compose

```
 docker-compose up -d
```

停止Docker容器（了解，不需要执行）

```
docker-compose stop
```

删除Docker容器（了解，不需要执行）

```
docker-compose down
```

配置Nginx

```
echo '
server {
    listen 80;
    server_name _;

    root /var/www/html;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
' > nginx/conf.d/default.conf
```

## 创建pipeline流水线项目

创建web项目

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340878925-f6d33cb1-b043-4784-8ba6-036f88ffcb0c.png "null")

生成代码拉取流水线

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879056-3ba5562f-f3fa-4201-829e-67d127c159fe.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879265-a8bf8c71-4191-4fee-9892-c3095865438f.png "null")

地址信息：

```
checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'bbe429d6-a97d-495a-b1d2-edbcfc53be5e', url: 'https://gitee.com/centos9/wordpress.git']])
```

设置项目信息，并勾选丢弃旧的构建

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879347-678d8b8f-664e-4c8f-a557-9f4db4683130.png "null")

设置流水线

```
pipeline {
  agent any
  environment {
    DEPLOY_SERVER = '192.168.88.200'
    DEPLOY_USER = 'root'
    DEPLOY_PASSWORD = '123456'    // 这里要改成你的真实密码
    REMOTE_WEB_ROOT = '/root/web/www/'
  }
  stages {
    stage('拉取 WordPress 代码') {
      steps {
        checkout scmGit(
          branches: [[name: '*/master']],
          extensions: [],
          userRemoteConfigs: [[
            credentialsId: 'bbe429d6-a97d-495a-b1d2-edbcfc53be5e', // 改为你的 Gitee 凭据ID
            url: 'https://gitee.com/centos9/wordpress.git'
          ]]
        )
      }
    }

    stage('清空远端 Web 目录') {
      steps {
        sh """
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "rm -rf ${REMOTE_WEB_ROOT}/*"
        """
      }
    }

    stage('发布代码到 Web 容器') {
      steps {
        sh """
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "mkdir -p ${REMOTE_WEB_ROOT}"
          sshpass -p "${DEPLOY_PASSWORD}" scp -r ./* ${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_WEB_ROOT}/
        """
      }
    }

    stage('重载 Nginx 服务') {
      steps {
        sh """
          # 如果用docker compose可以reload nginx，以下路径需替换为实际的compose文件路径
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "docker exec nginx nginx -s reload || true"
        """
      }
    }
  }
  post {
    success {
      echo "部署成功！WordPress 已同步到 LNMP 容器。"
    }
    failure {
      echo "部署失败，请检查日志！"
    }
  }
}
```

构建pipeline流水线任务

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879416-3fd37a54-25c3-438b-98af-505eab2ff5b6.png "null")

查看控制台输出

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879493-41425aa3-611c-4a3e-b1c7-c08464e4d729.png "null")

访问[http://Web服务器IP地址/，完成wordpress安装，最终如下图所示](http://Web服务器IP地址/，完成wordpress安装，最终如下图所示)

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879557-482f9a39-8588-4a9a-8856-fff891de0319.png "null")

# Jenkins + Gitee Tag 自动化发布系统

版本回退

v1.0

v2.0（稳定版）

v3.0（最新版本），发现v3.0不及预期。

## 安装Jenkins 插件

Git Parameter Plug-In：用于获取Gitee版本仓库的Tag标签（文本域选择方式）=> 本次使用这个

Active Choices plugin：用于获取Gitee版本仓库的Tag标签（下拉选项方式）

## 添加v2版本代码

准备phpinfo.php文件

```
<?php
  phpinfo();
?>
```

上传Gitee仓库设置Tag标签

```
git add .
git commit -m "add phpinfo.php"
git push origin master

git tag -a v2.0 -m "v2.0版本"
git push origin master v2.0
```

## 重新配置Pipeline项目

创建tag参数

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879644-fc13e17e-3cdf-4ab6-a4f0-a8060ecee74c.png "null")

重新配置pipeline流水线

```
pipeline {
  agent any
  environment {
    DEPLOY_SERVER = '192.168.88.200'
    DEPLOY_USER = 'root'
    DEPLOY_PASSWORD = '123456'
    REMOTE_WEB_ROOT = '/root/web/www/'
  }
  //parameters {
    //这个位置就是填写你要设置的tag参数
    //string(name: 'tag', defaultValue: '$tag', description: 'Git标签')
  //}
  stages {
    stage('拉取 WordPress 代码') {
      steps {
        // 拉取指定tag代码
        checkout([
          $class: 'GitSCM',
          branches: [[name: "refs/tags/${params.tag}"]],
          doGenerateSubmoduleConfigurations: false,
          extensions: [],
          userRemoteConfigs: [[
            credentialsId: 'bbe429d6-a97d-495a-b1d2-edbcfc53be5e',
            url: 'https://gitee.com/centos9/wordpress.git'
          ]]
        ])
      }
    }

    stage('清空远端 Web 目录') {
      steps {
        sh """
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "rm -rf ${REMOTE_WEB_ROOT}/*"
        """
      }
    }

    stage('发布代码到 Web 容器') {
      steps {
        sh """
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "mkdir -p ${REMOTE_WEB_ROOT}"
          sshpass -p "${DEPLOY_PASSWORD}" scp -r ./* ${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_WEB_ROOT}/
        """
      }
    }

    stage('重载 Nginx 服务') {
      steps {
        sh """
          sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "docker exec nginx nginx -s reload || true"
        """
      }
    }
  }
  post {
    success {
      echo "部署成功！WordPress 已同步到 LNMP 容器。"
    }
    failure {
      echo "部署失败，请检查日志！"
    }
  }
}

参数说明：
如果你是在可视化界面里已经加了“标签”类型参数，Jenkinsfile里可以不用重复写`parameters`那一块，但加了也没事。实际以你界面参数为准。
 
checkout拉取tag代码
branches: [[name: "refs/tags/${params.tag}"]], 这样就能拉取Git仓库中你选择的tag。
如果参数名是其他，比如`git_tag`，就改为`${params.git_tag}`。
```

## 选择Tag重新构建任务

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879716-4228c80b-855e-4573-8980-c07c3fa679e5.png "null")

查看运行结果

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879840-9827eb24-df84-4308-b027-eafda6e15463.png "null")

测试验证代码，输入[http://Web服务器IP/phpinfo.php](http://Web服务器IP/phpinfo.php)

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340879939-ca56ab23-ea9e-4f94-ac47-e1e9ecbe5eee.png "null")

# 集成SonarQube代码质量检查

静态代码分析是指无需运行被测代码，仅通过分析或检查源程序的语法、结构、过程、接口等来检查程序的正确性，找出代码隐藏的错误和缺陷，如：参数不匹配、有歧义的嵌套语句、错误的递归、非法计算、可能出现的空指针引用等等。

静态代码扫描是CI/CD中重要的一环，可以在代码提交到代码仓库之后，在CI/CD流程中加入代码扫描步骤，从而及时地对代码进行质量的检查。这可以有效地降低后期维护成本，优化产品质量，提高产品交付速度。同时，静态代码扫描还可以将代码问题自动通知给开发人员，使得问题得到及时发现和解决。

通俗地说，通过将静态代码分析融入到CI/CD流程中，可以进一步提高软件开发过程的效率和质量，帮助团队快速交付高质量的产品。

## 安装SonarQube工具

安装PostgreSQL数据库

mysql:3306

pgsql:5432

```
docker pull postgres:latest
mkdir -p /postgres/{postgresql,data}
docker run -itd --name postgres -p 5432:5432 -v /postgres/postgresql:/var/lib/postgresql -v /postgres/data:/var/lib/postgresql/data -v /etc/localtime:/etc/localtime:ro -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -e POSTGRES_DB=sonar -e TZ=Asia/Shanghai --restart always --privileged=true -u 0 postgres:latest

docker ps
docker logs -f postgres
```

拉取SonarQube工具

```
docker pull sonarqube:9.9-community
mkdir -p /sonarqube/{extensions,logs,data}
chmod -R 777 /sonarqube
docker run -itd --name sonarqube -p 9000:9000 --link postgres -v /sonarqube/conf:/opt/sonarqube/conf -v /sonarqube/extensions:/opt/sonarqube/extensions -v /sonarqube/logs:/opt/sonarqube/logs -v /sonarqube/data:/opt/sonarqube/data -e SONARQUBE_JDBC_URL=jdbc:postgresql://postgres:5432/sonar -e SONARQUBE_JDBC_USERNAME=sonar -e SONARQUBE_JDBC_PASSWORD=sonar --restart always --privileged=true sonarqube:9.9-community
```

访问SonarQube，[http://Web服务器IP:9000/](http://Web服务器IP:9000/)

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880077-120989d3-6b4e-4f41-b8ce-6b3b8085ad47.png "null")

默认账号密码都是admin/admin

修改SonarQube密码

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880144-b355f09b-a3d5-47e3-8296-0a5f5bef815a.png "null")

配置中文界面

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880231-1cc02967-ed8b-402b-9d19-643da26fd504.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880321-c50ce1ee-4f86-4ef6-bd3b-87612e3198df.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880415-e9f82bf5-b719-4f80-861c-b70986b5d1bb.png "null")

## 创建项目

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880488-6fca75cc-0a43-4f5a-ab77-7f11e9c1971a.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880555-e4f05846-3bb3-4401-9bfb-c77ae033fef1.png "null")

## 获取Token令牌

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880624-f3f36e5d-d60b-4818-8135-404be1c4498d.png "null")

获取令牌

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880686-ebb0f3f4-fa23-4e6c-9c2e-f6359e40f176.png "null")

复制令牌：sqp_8f3a93910ddc418420925bc6a26114711de871ef

安装Jenkins SonarQube插件

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880766-e0382237-54e7-419b-ba16-8b7de09a2418.png "null")

配置SonarQube

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880828-8dc71926-3438-42c7-8cb2-99279d89c56b.png "null")

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880897-b43d27e1-74bf-4142-94f5-4d855f7b4a03.png "null")

## 安装 sonar-scanner

注意：以下sonar-scanner命令行工具，需要在Jenkins服务器安装。

```
cd /opt
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
unzip sonar-scanner-cli-5.0.1.3006-linux.zip
ln -s /opt/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner
```

配置环境变量

```
vim /etc/profile
export PATH=$PATH:/opt/sonar-scanner-5.0.1.3006-linux/bin

source /etc/profile
```

Jenkins全局工具配置

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340880968-e6ca6524-c35b-4635-8b60-c227c973ccf6.png "null")

安装node工具（SonarQube依赖）

```
curl -sL https://rpm.nodesource.com/setup_18.x | bash -
dnf install -y nodejs
```

## 重新设置pipeline流水线代码

```
pipeline {
    agent any
    environment {
        DEPLOY_SERVER = '192.168.88.200'
        DEPLOY_USER = 'root'
        DEPLOY_PASSWORD = '123456'
        REMOTE_WEB_ROOT = '/root/web/www/'
        SONAR_HOST_URL = 'http://192.168.88.200:9000'
        SONAR_TOKEN = 'sqp_73b6338c17d5e71859cc6b444e54809a126ca230'
    }
    stages {
        stage('拉取 WordPress 代码') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "refs/tags/${params.tag}"]],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'bbe429d6-a97d-495a-b1d2-edbcfc53be5e',
                        url: 'https://gitee.com/centos9/wordpress.git'
                    ]]
                ])
            }
        }

        stage('SonarQube 代码扫描') {
            steps {
                script {
                    withSonarQubeEnv('sonarqube') {
                        sh "which sonar-scanner"
                        sh """
                            sonar-scanner \\
                              -Dsonar.projectKey=wordpress \\
                              -Dsonar.projectName=WordPress \\
                              -Dsonar.projectVersion=${params.tag} \\
                              -Dsonar.sources=. \\
                              -Dsonar.host.url=${SONAR_HOST_URL} \\
                              -Dsonar.login=${SONAR_TOKEN}
                        """
                    }
                }
            }
        }

        stage('清空远端 Web 目录') {
            steps {
                sh """
                  sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "rm -rf ${REMOTE_WEB_ROOT}/*"
                """
            }
        }

        stage('发布代码到 Web 容器') {
            steps {
                sh """
                  sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "mkdir -p ${REMOTE_WEB_ROOT}"
                  sshpass -p "${DEPLOY_PASSWORD}" scp -r ./* ${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_WEB_ROOT}
                """
            }
        }

        stage('重载 Nginx 服务') {
            steps {
                sh """
                  sshpass -p "${DEPLOY_PASSWORD}" ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} "docker exec nginx nginx -s reload || true"
                """
            }
        }
    }
    post {
        success {
            echo "部署成功！WordPress 已同步到 LNMP 容器。"
        }
        failure {
            echo "部署失败，请检查日志！"
        }
    }
}
```

构建Pipeline

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340881039-4d70da0b-da25-4c2f-8b69-16c300af7015.png "null")

时间会比较久，最终运行结果：

![](https://cdn.nlark.com/yuque/0/2026/png/40487410/1774340881179-a7d74e85-5e6e-4a29-a2af-6cd24af64d44.png "null")