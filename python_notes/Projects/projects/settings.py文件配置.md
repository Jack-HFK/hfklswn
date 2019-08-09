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

**大众功能安装配置文件位置：都在 /etc/... .. 文件下**

```python
							# setting.py文件中添加
    
    	1  INSTALLED_APPS 中添加 corsheaders
		2  MIDDLEWARE 中添加 corsheaders.middleware.CorsMiddleware
		   位置尽量靠前，官方建议在 ‘django.middleware.common.CommonMiddleware’ 上方
		3  CORS_ORIGIN_ALLOW_ALL=True 布尔值,如果为True 白名单不启用(所有域都能来,上线不能设置为			   True)
		4  CORS_ORIGIN_WHITELIST =[
			"https://example.com"
		    ]
		5  CORS_ALLOW_METHODS = ( # 允许的接收的请求：
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
				'dnt',              # 请求加了"dnt"，不要给此推荐任何不相关的请求(没啥用!不受约束)
				'origin',
				'user-agent',
				'x-csrftoken',      # 自由组织自己定义的header头，以 x- 开头
				'x-requested-with',
			)
		7  CORS_PREFLIGHT_MAX_AGE  默认自带 86400s
		8  CORS_EXPOSE_HEADERS  []   # 前端想取后端自定义header头的内容
		9  CORS_ALLOW_CREDENTIALS  布尔值， 默认False 
```

# setting.py文件配置

#### 图片视频存储位置设置

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

#### 时间设置

```python
TIME_ZONE = "Asia/shanghai"   <------------东八区时间，默认加八小时 
# USE_TZ = True               <-------------设置为True默认使用东八时区时间
USE_TZ = False                <---------------设置为False默认使用现在系统时间
```

