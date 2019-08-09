# Django添加跨域支持		   

**目的：**让Django支持跨域。

django-cors-headers官网 https://pypi.org/project/django-cors-headers/

**注 意**　：**不要直接pip 将把django升级到2.0以上，强烈建议用离线安装方式**，建议安装Django1.11.8

让Django支持跨域，需要安装django-cors-headers-3.0.2第三方包，安装过程如下：。

​		1 . FTP获取源码包 

​		2 . 将源码包粘贴到虚拟机

​		3 . 执行文件 tar -zxvf django-cors-headers-3.0.2.tar.gz解压

​		4 . cd 到 解压后的目录 cd django-core-headers-3.0.2

​		5 . sudo python3 setup.py install 执行安装

​		6 . pip3 freeze|grep"cors" 检查是否安装成功；

​	   若屏幕执行Finished processing dependencies for django-cors-headers==3.0.2 则安装成功

# **Django配置流程**

**配置位置：**settings.py文件中添加以下配置

```python
							# setting.py文件中添加
    
    	1  INSTALLED_APPS 中添加 corsheaders
		2  MIDDLEWARE 中添加 corsheaders.middleware.CorsMiddleware
		   位置尽量靠前，官方建议在 ‘django.middleware.common.CommonMiddleware’ 上方
		3  CORS_ORIGIN_ALLOW_ALL=True 布尔值,如果为True 白名单不启用(所有域都能来,都能访问。上线不能设置为True)
		4  CORS_ORIGIN_WHITELIST =[   <-----------控制或限定可以接受那些域可以访问，公司上线使用，
			"https://example.com"  <-CORS_ORIGIN_ALLOW_ALL设置为True此限制不起作用,与其相排斥。
		    ]                     <--------参数可以累加，限定的域可以累加。
        5  CORS_ALLOW_METHODS = (        # 允许的接收的请求：
                'DELETE',  	  # 删除请求
                'GET', 		  # 获取请求
                'OPTIONS',    # 协商请求
                'PATCH',      # 局部更新
                'POST',       # 获取请求
                'PUT',        # 全部更新
                )
		6  CORS_ALLOW_HEADERS = (   # 当前支持的所有的header(头)
				'accept-encoding',
				'authorization',
				'content-type',
				'dnt',      # 请求加了"dnt"，不要给此推荐任何不相关的请求(广告等)(没啥用!不受约束)
				'origin',
				'user-agent',
				'x-csrftoken',      # 自由组织自己定义的header头，以 x- 开头
				'x-requested-with',
			)
		7  CORS_PREFLIGHT_MAX_AGE  默认自带 86400s
		8  CORS_EXPOSE_HEADERS  []   # 前端想取后端自定义header头的内容,设置在其中
		9  CORS_ALLOW_CREDENTIALS  布尔值， 默认False # 跨域后是否设置使用cookie
```

# 时间设置

```python
TIME_ZONE = "Asia/Shanghai"   <------------东八区时间，默认加八小时 
# USE_TZ = True               <-------------设置为True默认使用东八时区时间
USE_TZ = False                <---------------设置为False默认使用现在系统时间
```



# 数据库的配置

- sqlite 数据库配置

```python
# file: settings.py
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- **mysql 数据库配置**

```python
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mywebdb',  # 数据库名称,需要自己定义
        'USER': 'root',
        'PASSWORD': '123456',  # 管理员密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

**关于数据为的SETTING设置**

1. ENGINE

   - 指定数据库的后端引擎

   ```python
   'django.db.backends.mysql'
   'django.db.backends.sqlite3'
   'django.db.backends.oracle'
   'django.db.backends.postgresql'
   ```

   - mysql引擎如下:
     - 'django.db.backends.mysql'

2. NAME

   - 指定要连接的数据库的名称
   - `'NAME': 'mywebdb'`

3. USER

   - 指定登录到数据库的用户名
   - `'USER':'root'`

4. PASSWORD

   - 接数据库时使用的密码。
   - `'PASSWORD':'123456'`

5. HOST

   - 连接数据库时使用哪个主机。
   - `'HOST':'127.0.0.1'`

6. PORT

   - 连接数据库时使用的端口。
   - `'PORT':'3306'`

# 添加 mysql 支持

- 安装pymysql 模块

  - `$ sudo pip install pymysql`

- 修改项目中__init__.py 加入如下内容来提供pymysql引擎的支持

  ```python
  __init__文件中添加以下代码：
  
  import pymysql
  pymysql.install_as_MySQLdb()
  
  让Django支持Mysql
  ```

#### 数据库的迁移

- 迁移是Django同步您对模型所做更改（添加字段，删除模型等） 到您的数据库模式的方式

1. **生成或更新迁移文件**
   - 将每个应用下的models.py文件生成一个中间文件,并保存在migrations文件夹中
   - `python3 manage.py makemigrations`
2. **执行迁移脚本程序**
   - 执行迁移程序实现迁移。将每个应用下的migrations目录中的中间文件同步回数据库
   - `python3 manage.py migrate`

# 应用-app安装配置

- 在 settings.py 中配置应用, 让此应用能和整个项目融为一体

  ```python
  # file : settings.py 
  INSTALLED_APPS = [
      ... ...,
      '自定义应用名称'
  ]
  
  ```

- 如:

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      "corsheaders",
      'user',  # 自定义APP模块
      'music',  # 自定义APP模块
       # ....
  ]
  
  ```

# setting.py基础设置

```python
#　setting.py文件
1.BASE_DIR
用于绑定当前项目的绝对路径 ( 动态计算出来的 ), 所有文件都可以依懒此路径
2. DEBUG
   用于配置 Django 项目的启用模式 , 取值 :
3. True 表示开发环境中使用 调试模式 ( 用于开发中 )
4. False 表示当前项目运行在生产环境中 ( 不启用调试 )
5. ALLOWED_HOSTS
   4 / 177/11/2019
   django教程day01.md
   设置允许访问到本项目的网络地址列表 , 取值 :
6. [] 空列表 , 表示只有 127.0.0.1, localhost, '[::1]' 能访问本项目
7. ['*'] ,表示任何网络地址都能访问到当前项目
8. ['*.tedu.cn', 'weimingze.com'] 表示只有当前两个主机能访问当前项目
   注意 :
   如果要在局域网其它主机也能访问此主机 , 启动方式应使用如下模式 :
   python3 manage.py runserver 0.0.0.0:5000 # 指定网络设备所有主
   机都可以通过 5000 端口访问 ( 需加 ALLOWED_HOSTS = ['*'])
9. INSTALLED_APPS
   指定当前项目中安装的应用列表
10. MIDDLEWARE
    用于注册中间件
11. TEMPLATES
    用于指定模板的配置信息
12. DATABASES
    用于指定数据库的配置信息
13. LANGUAGE_CODE
    用于指定语言配置
    取值 :
    英文 : "en-us"
    中文 : "zh-Hans"
14. TIME_ZONE
    用于指定当前服务器端时区
    取值 :
    世界标准时间 : "UTC"
    中国时区 : "Asia/Shanghai"
15. ROOT_URLCONF
    用于配置根级 url 配置 'mywebsite1.urls'
    如 :
    ROOT_URLCONF = 'mywebsite1.urls'
    协议
    注 : 此模块可以能过 from
    django.conf import settings
    HTTP
    在 TCP/IP 协议中位于应用层的协议
    HTTP 协议的请求和响应
    5 / 17
    导入和使用
```

# 配置安装PyJWT文件

**一 . 下载压缩包**

安装 pip3 install pyjwt　压缩包

```python
PyJWT压缩包复制到所用电脑文件夹中(文件夹位置不限)
```

**二 . 终端解压压缩包**

```python
1 . 终端找到文件所在位置

2 . 在文件所在的位置执行　　pip3 install　解压后文件的名字
	pip3 install PyJWT-1.4.0-py2.py3-none-any.whl
	
	解压成功：提示如下
	Processing ./PyJWT-1.4.0-py2.py3-none-any.whl
	Installing collected packages: PyJWT
	Successfully installed PyJWT-1.4.0
    
3 . pip3 freeze|grep "JWT" 查看文件安装及版本信息
	
    安装成功提示如下：
    PyJWT==1.4.0
```

# 静态文件配置

**什么是静态文件**

​	**不能与服务器端做动态交互的文件都是静态文件**

​	如:图片,css,js,音频,视频,html文件(部分)

**静态文件配置**

​			在 **settings.py** 中配置一下两项内容:

**步骤一：配置静态文件的访问路径**

- 通过哪个url地址找静态文件
- STATIC_URL = '/static/'
- 说明:
  - 指定访问静态文件时是需要通过 /static/xxx或 127.0.0.1:8000/static/xxx
  - xxx 表示具体的静态资源位置

**步骤二：配置静态文件的存储路径**

- 静态文件名字必须是**static**,不能更换

- 静态文件在服务器端的保存位置

- STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

  ```python
  例如:
  	STATICFILES_DIRS=(元组)
  	在setings文件下的STATIC_URL = '/static/'下添加：静态文件的存储路径：
      
      # static：静态文件  访问路由的起始位置
  	STATIC_URL = '/static/'　　<----------静态文件名字必须是static,建议一般存放JSS/CSS文件
  	
      # 给'/static/'配置静态文件的存储路径  
  	STATICFILES_DIRS = (
  	    os.path.join(BASE_DIR,"static"),
  	)
  
  ```

3. 示例:

   ```py
   # file: setting.py
   STATICFILES_DIRS = (
       os.path.join(BASE_DIR, "static")
   )
   ```

#### 访问静态文件

1. 使用静态文件的访问路径进行访问

   - **访问路径: STATIC_URL=/static/**

   - 示例:

     ```html
     <img src="/static/images/lena.jpg">
     <img src="http://127.0.0.1:8000/static/images/lena.jpg">
     ```

2. **通过 {% static %}标签访问静态文件**

   **作用：**

   ​		防止页面中访问路径stasic改变，使用模板变量封装变化，代替原方法，

   ​		更改settings.py静态资源访问路径后，模板中静态资源访问路径无需改变。

   **《模板中如何访问静态文件路径》**

   ```
   {% static %}表示的就是静态文件访问路径
   ```

   **步骤一：加载 static**
   				**语法：**{% load static %}

   **步骤二：使用静态资源时**
   			　**语法:**　{% static '静态资源路径' %}

   ```html
   <!doctype html>
   <html lang="en">
   <head...>
   <body>
       <div>模板：动态的html网页</div>
       <div>通过 loader 获取模板 , 通过 HttpResponse 进行响应</div>
       <div>变量1:{{变量1}}</div>
       <div>
           {% load static %}
           静态文件：图片<img src="/static/meinv.png" alt="加载失败">
           <!--防止页面中访问路径stasic改变，使用模板变量代替防止变化-->
           静态文件：图片<img src="{% static 'lena.jpg' %}" alt="加载失败">
   
       </div>
   </body>
   </html>
   ```

   

- 示例:

- 路由配置文件

  ```python
  # file: url.py
  from . import views
  
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^show_image', views.show_image)
  ]
  - 视图函数文件
  # file: views.py
  from django.shortcuts import render
  
  def show_image(request):
      return render(request, "show_image.html")
  ```

  - 模板文件

  ```html
  <html>
  <head></head>
  <body>
  <h1>this is lena!</h1>
  <img src="/static/images/lena.jpg">
  <h1>this is templates lena!</h1>
  {% load static %}
  <img src="{% static 'images/lena.jpg' %}">
  </body>
  </html>
  ```

# 图片视频存储位置设置

```python
								# setting.py文件中添加
    
    1  APPEND_SLASH = False  # URL路径 APPEND_SLASH默认True:自动添加/,设置为False:不自动添加/
  	2  2.(1 MEDIA_URL = "/media/"　# 建议图片视频存储在此文件内，文件名不固定
       2.(2 MEDIA_ROOT = os.path.join(BASE_DIR,"media/") # 自动拼接计算存储视频图片的位置

```

```python
       2 .(3		 # 设置MEDIA_URL= "/media/" 需要在 url.py主路由中 设置如下：
       from django.conf import settings
       from django.conf.urls.static import static
        # 此方法表示使用MEDIA下访问静态资源将通过以下路径寻找
       urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```

例 如 :

```python
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)
```

```python
例如:
	STATICFILES_DIRS=(元组)
	在setings文件下的STATIC_URL = '/static/'下添加：静态文件的存储路径：
    
    # static：静态文件  访问路由的起始位置
	STATIC_URL = '/static/'　　<----------静态文件名字必须是static,建议一般存放JSS/CSS文件
	MEDIA_URL = "/media/"　    <----------建议一般存放图片视频存储在此文件内，文件名不固定
    # 给'/static/'配置静态文件的存储路径  
	STATICFILES_DIRS = (
	    os.path.join(BASE_DIR,"static"),
	)

```



