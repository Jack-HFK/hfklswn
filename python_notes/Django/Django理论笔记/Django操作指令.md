# 终端执行项目命令

**Django框架**终端执行命令

```终端
python3 manage.py runserver
```

**Flask框架**终端执行命令

```终端
python3 flask_client.py
```

#### MySql数据库创建指令

```mysql
create database 数据库名 default charset utf8 collate utf8_general_ci;
```

#### 创建项目的指令

```终端
django-admin startproject 项目名称
```

#### 运行项目的指令

```shell
项目文件夹下：
$ cd mywebsite1
$ python3 manage.py runserver
$ python3 manage.py runserver 5000　＃　指定只能本机使用 127.0.0.1 的 5000 端口访问本机
```

#### 应用-app创建指令

```终端
python3 manage.py startapp 应用名称(必须是标识符命令规则)
```

#### 数据库的迁移指令

```python
一. 生成或更新迁移文件
	python3 manage.py makemigrations

二. 执行迁移脚本程序
	python3 manage.py migrate
```



#### 创建后台数据库管理帐号

```python
python3 manage.py createsuperuser 
```

