# 前后端分离

#### 1 . 什么是前后端分离

​	前端： 即客户端，负责渲染用户显示界面【如web的js动态渲染页面, 安卓， IOS，pc客户端等】

​	后端：即服务器端，负责接收http请求，处理数据

# API(应用程序编程接口)

**定 义 :**  Application Programming Interface

​		一些预先定义的函数。或指软件系统不同组成部分衔接的约定。两个系统间(前后端之间)通信的一个接口

**目 的 :**

​		提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力，而无需访问源码，或理解内部工作机		制的细节。

​		通俗易懂：比如定义好一个类，使用者只需要知道类其中的方法和属性，每个方法和每个属性能干什么事，						　别人直接拿来就用，不需要看你是怎么实现的功能，而你提供给用户的每个方法和每个属性的说						　明就是: 《API文档》

**前后端分离 完整请求过程**

​    		1，前端通过http请求后端API

​			2，后端以json形式返回前端数据

​			3，前端生成用户显示界面【如html , ios , android】

​	**判断前后端分离得核心标准： 谁生成显示页面**

​    1，后端生成【前后端未分离】  ex: flask->render_template  django -> HttpResponse(html)

​	2,   前端生成【前后端分离】

| 协议默认端口   | 端口号 |
| -------------- | ------ |
| https 默认端口 | 443    |
| http 默认端口  | 80     |

#### 2 . 优 点

​	1，各司其职

​		前端：视觉层面，兼容性，前端性能优化

​		后端：并发，可用性，性能

​	2，解耦，前端和后端均易于扩展

​	3，后端灵活搭配各类前端 - 如安卓等

​	4，提高用户体验

​	5，前端+后端可完全并行开发，加快开发效率



#### 3 . 分离常见问题

| 问题                                                         | 答案                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 如何解决http无状态？                                         | 采用token(详情见下方章节)                                    |
| 如果前端为JS，如何解决跨域问题？                             | 采用CORS(详情见下方章节)                                     |
| 如何解决csrf问题                                             | 采用token                                                    |
| Single Page web Application 是否会影响Search Engine Optimization效果 | 会，前后端分离后，往往页面不存在静态文字【例如新闻的详细内容】 |
| ”老板，这个逻辑到底是让前端做还是后端做啊?“                  | 底线原则: 数据校验需要前后端都做                             |
| ”老板，前端工作压力太大了啊“                                 | 团队协作不能只是嘴上说说                                     |
| 动静分离和前后端分离是一个意思么？                           | 动静分离指的是 css/js/img这类静态资源跟服务器拆开部署，典型方案-静态资源交由CDN厂商处理 |



#### 4 . 实现方式

1，Django/Flask 后端只返回json

2,	前端 ->  ex: js向服务器发出ajax请求，获取数据，拿到数据后动态生成html

3,	前端服务和后端服务 分开部署



# token - 令牌

#### base64 

​			　一种编码方式， '防君子不防小人' 

| 方法              | 作用                                                  | 参数                                               | 返回值                                                    |
| ----------------- | ----------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------- |
| b64encode         | 将输入的参数转化为base64规则的串                      | 预加密的明文，类型bytes字节串。　例：b‘guoxiaonao’ | base64对应编码的密文，类型为bytes；例:b'Z3VveGlhb25hbw==' |
| b64decode         | 将base64串 解密回 明文                                | base64密文,类型为bytes。　例：b'Z3VveGlhb25hbw=='  | 参数对应的明文，类型为bytes；例：b'guoxiaonao'            |
| urlsafe_b64encode | 作用同b64encode,但是会将 '+'替换成 '-',将'/'替换成'_' | 同b64encode                                        | 同b64encode                                               |
| urlsafe_b64decode | 作用同b64decode                                       | 同b64decode                                        | 同b64decode                                               |

代码演示:

```python
import base64   # 调用模块　base64
#base64加密
s = b'guoxiaonao'
b_s = base64.b64encode(s)
#b_s打印结果为 b'Z3VveGlhb25hbw=='

#base64解密
ss = base64.b64decode(b_s)
#ss打印结果为 b'guoxiaonao'

```

#### SHA-256  

​	安全散列算法的一种（hash）

​	hash三大特点：

​	1）定长输出    2）不可逆    3） 雪崩

```python
import hashlib 			# 调用模块 hashlib
s = hashlib.sha256() 	#创建sha256对象
s.update(b'xxxx')  	    #添加欲hash的内容，类型为 bytes
s.digest()  		    #获取最终结果　　　　　　　(密码传递１６进制传递)
```

#### HMAC-SHA256 

HMAC-SHA256 是一种通过特别计算方式之后产生的消息认证码。

使用**散列算法**（以下选用SHA-256）同时结合一个**加密密钥**。它可以用来保证数据的完整性，同时可以用来作某个消息的身份验证。

```python
import hmac
#生成hmac对象
#第一个参数为加密的key，bytes类型，
#第二个参数为欲加密的串，bytes类型
#第三个参数为hmac的算法，指定为SHA256
h = hmac.new(key, str, digestmod='SHA256 ') 
h.digest() #获取最终结果
```

​	4，RSA256 非对称加密

​		1，加密： 公钥加密，私钥解密

​		2，签名： 私钥签名， 公钥验签

#  JWT -  json-web-token  

### JWT 三大组成

定 义 :

​		是为了在网络应用环境间传递声明而执行的一种基于JSON开放的标准。

特 点 : 

​		特别适用于分布式站点的单点登录（SSO）场景。JWT声明一般被用来身份提供者和服务提供者间传递和验证		被认证的用户信息，实现用户身份的验证。

#####  一 . header

​		  格式为字典-元数据

**header 格 式 : **

```python
{'alg':'HS256', 'typ':'JWT'}
#alg代表要使用的 算法
#typ表明该token的类别 - 此处必须为 大写的 JWT
```

**header 用 法 :** 

1 .  **{'alg':'HS256', 'typ':'JWT'}** 该部分数据需要转成**json串**

2 . 转成**json**串后运用**base64**进行加密

3 . 如果用http等协议需要发送给前端需要转换为**字节串**

```python
import json
import base64
header = {'alg': 'HS256', 'typ': 'Jwt'}
# sort_keys=True 从字典得到的字符串，将字符串序列化的进行排序   json.dumps()计算机字符串转换json串
header_json = json.dumps(header, separators=(",", ":"), sort_keys=True)
# json串用base64加密 生成base64 加密后encode()转换成字节串发送给前端
header_bs = base64.urlsafe_b64encode(header_json.encode())    <---json串转换为字节串后b64方法
```

**注 意 :**. 字典中的键值对base64加密前必须进行序列化排序,因为字典是无序的,无序的字符串进行base64加密,两次加密的结果是可能不同的,直接回造成雪崩,所有要保证从字典中得到字符串结果是字符串序列化排序过的

```python
import json
header = {'alg': 'HS256', 'typ': 'Jwt'}
# sort_keys=True 从字典得到的字符串，将字符串序列化的进行排序,按照字符串之间比较大小进行排序.   
# json.dumps()计算机字符串转换json串
header_json = json.dumps(header, separators=(",", ":"), sort_keys=True)
```

**注 意 :** 字典中的键值对base64加密前必须去掉空格再进行加密

```python
import json
s = {"hfk":1}
json.dumps(s)   # 得到　{"hfk": 1}   <-----value值会多出空格，加密运算必须去掉空格再进行加密
json.dumps(s,separators=(",", ":"))   # 得到去掉空格的value {"hfk":1}
# 参数separators=(",", ":")中 
   1. 第一个参数是字典 键值对 与 键值对 之间需要的符号链接 此处为逗号,逗号两旁严格按照没有空格输出
   2. 第二个参数为是字典 键 与 值 之间需要的符号链接 此处为冒号,冒号两旁严格按照没有空格输出
```



------

##### 二 . payload

​		格式为字典-此部分分为**公有声明**和**私有声明**

**公共声明**：JWT提供了内置关键字用于描述常见的问题

**可选项 : **，用户根据自己需求 ，按需添加key，常见公共声明如下：

```python
{'exp':xxx, # Expiration Time 此token的过期时间的时间戳
 'iss':xxx，# (Issuer) Claim 指明此token的签发者
 'iat':xxx, # (Issued At) Claim 指明此创建时间的时间戳
 'aud':xxx, # (Audience) Claim	指明此token签发面向群体
}
```

**私有声明**：用户可根据自己业务需求，添加自定义的key，例如如下：

```python
{'username': 'guoxiaonao'}
```

**使用方法：**

​				1 . **公共声明**和**私有声明**均在同一个字典中．

​				2 . 转成json串再用base64加密

```python
@staticmethod
    def encode(payload, key, exp=300):
    	# 参数中的payload = {"username":"aaa"}
        payload = copy.deepcopy(payload)  # 深拷贝
        # 添加公有声明 -exp 且值为未来时间戳
        payload["exp"] = int(time.time()) + exp
        payload_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        payload_bs = base64.urlsafe_b64encode(payload_json.encode())
        <---------------------------------------------json串转换为字节串后b64方法
        # sort_keys=True 从字典得到的字符串，将字符串序列化的进行排序
        # separators=(",", ":")  value值会多出空格，加密运算必须去掉空格再进行加密
```

------

##### 三 . signature 签名

**签名语法规则:**

根据header中的alg确定 具体算法，以下用 HS256为例

**方 法 :** 　HMAC-SHA256 = HS２５６

```python
HS256(自定义的key , base64方法后的header + '.' + base64方法后的payload)
```

**注　释 :**　HMAC-SHA256 是 hmac算法

​			用自定义的key, 对base64方法后的header + '.' + base64方法后的payload进行hmac计算

```python
@staticmethod
    def encode(payload, key, exp=300):
 		# 签名
        # isinstance判断传入的key类型
        if isinstance(key, str):
            key = key.encode()   <-----字符串转换为字节穿后b64方法
        hm = hmac.new(key, header_bs + b"." + payload_bs, digestmod="SHA256")
        hm_bs = base64.urlsafe_b64encode(hm.digest())
        return header_bs + b"." + payload_bs + b"." + hm_bs

```

------

### JWT结果格式

```python
base64(header) + '.' + base64(payload) + '.' +  base64(sign)
```

**JWT最终得到的结果如下：** 

```python
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1b3hpYW9uYW8iLCJpc3MiOiJnZ2cifQ.Zzg1u55DCBqPRGf9z3-NAn4kbA-MJN83SxyLFfc5mmM'
```

### 校验jwt规则

​		1，解析header, 确认alg

​		2，签名校验 - 根据传过来的header和payload按 alg指明的算法进行签名，将签名结果和传过来的sign进行对比，若对比一致，则校验通过

​		3，获取payload自定义内容

### 安装并使用pyjwt 

​	1，安装 pip3 install pyjwt  <----------安装过程详情查看　Django项目配置md文件

| 方法                            | 参数说明                                                     | 返回值                                        |
| ------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| encode(payload, key, algorithm) | payload:  jwt三大组成中的payload,需要组成字典，按需添加公有声明和私有声明<br />例如:                                                {'username': 'guoxiaonao', 'exp': 1562475112}<br />参数类型： dict | token串<br />返回类型：bytes                  |
|                                 | key : 自定义的加密key<br />参数类型：str                     |                                               |
|                                 | algorithm:  需要使用的加密算法[HS256, RSA256等] <br />参数类型：str |                                               |
| decode(token,key,algorithm,)    | token:   token串<br />参数类型： bytes/str                   | payload明文<br />返回类型：dict               |
|                                 | key : 自定义的加密key ,需要跟encode中的key保持一致<br />参数类型：str |                                               |
|                                 | algorithm:  需要使用的加密算法[HS256, RSA256等] <br />参数类型：str |                                               |
|                                 | issuer:  发布者，若encode payload中添加 'iss' 字段，则可针对该字段校验<br />参数类型：str | 若iss校验失败，则抛出jwt.InvalidIssuerError   |
|                                 | audience：签发的受众群体，若encode payload中添加'aud'字段，则可针对该字段校验<br />参数类型：str | 若aud校验失败，则抛出jwt.InvalidAudienceError |

**PS**:  若encode得时候 payload中添加了exp字段; 则exp字段得值需为 当前时间戳+此token得有效期时间， 例如希望token 300秒后过期  {'exp': time.time() + 300};  在执行decode时，若检查到exp字段，且token过期，则抛出jwt.ExpiredSignatureError

```shell
终端JWT测试如下
In [1]: import jwt
In [2]: import time                                                             

In [3]: now = time.time()                                                      

In [4]: jwt.encode({"username":"111","exp":now+300},"hfk",algorithm="HS256")   
Out[4]: b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjExMSIsImV4cCI6MTU2NDgxNjIxMy44NjkxMTMyfQ.DMuXDJgfzB3Xj7Siq1At9ZXtjU79jvbEFp-1FOA2Xcg'


In [5]: token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjExMSIsImV4cCI6MTU2NDgxNjIxMy44NjkxMTMyfQ.DMuXDJgfzB3Xj7Siq1At9ZXtjU79jvbEFp-1FOA2Xcg'
                           
In [6]: jwt.decode(token,"hfk",algorithm="HS256")                               
Out[6]: {'username': '111'}
```



# CORS - Cross-origin resource sharing - 跨域资源共享

### 什么是CORS

​		允许浏览器向跨源(协议 + 域名 + 端口)服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制

### 特点

​		1，浏览器自动完成（在请求头中加入特殊头 或 发送特殊请求）

​		2，服务器需要支持（响应头中需要有特殊头）

------

**简单请求(Simple requests)和预检请求(Preflighted requests)**

------

# 简单请求(Simple requests)	

**满足以下全部条件**的请求为 **简单请求**（以下三点全满足的请求为简单请求）

​			1，请求方法只能如下：

​					GET  or HEAD or POST

​			2，请求头仅包含如下：

​					Accept

​					Accept-Language

​					Content-Language

​					Content-Type　（只会在POST请求中出现,表示此次POST请求提交过来的数据的类型　）

​			3，Content-Type 仅支持如下三种(三选一)：

​					application/x-www-form-urlencoded          <-----------简单的form请求

​					multipart/form-data   <----图片或文件上传时,表示当前数据以二进制传递,每一个数据存在消息边界的

​					text/plain															<--------------上传一个普通文本

​			**不满足以上任意一点的请求都是 预检请求**

### 简单请求发送流程

​		1，请求(request)

​				请求头中 携带 **Origin**，该字段表明自己来自哪个域

​		2，响应(response)

​				如果请求头中的**Origin**在服务器接受范围内， 则返回如下头响应

| 响应头                           | 作用                                                         | 备注 |
| -------------------------------- | ------------------------------------------------------------ | ---- |
| Access-Control-Allow-Origin      | 服务器可以接受得域      <--------------响应中携带这种响应头，一定是跨域请求。 | 必选 |
| Access-Control-Allow-Credentials | 是否接受Cookie          <-----------响应中携带这种响应头，表示允许使用Cookie | 可选 |
| Access-Control-Expose-Headers    | 默认情况下，xhr只能拿到如下响应头：Cache-Control，Content-Language，Content-Type，Expires，Last-Modified；如果有需要获取其他头，需在此指定 | 可选 |

​		如果服务器不接受此域，则响应头中不包含 Access-Control-Allow-Origin

# 预检请求(Preflighted requests)

### 预检请求发送流程

​	1，OPTION 请求发起，携带如下请求头

| 请求头                         | 作用                 | 备注 |
| ------------------------------ | -------------------- | ---- |
| Origin                         | 表明此请求来自哪个域 | 必选 |
| Access-Control-Request-Method  | 此次请求使用方法     | 必选 |
| Access-Control-Request-Headers | 此次请求使用的头     | 必选 |

​	2，OPTION 接受响应阶段，携带如下响应头

| 响应头                           | 作用                                                         | 备注 |
| -------------------------------- | ------------------------------------------------------------ | ---- |
| Access-Control-Allow-Origin      | 服务器可以接受得域      :响应中携带这种响应头一定是跨域请求  | 必选 |
| Access-Control-Allow-Methods     | 告诉浏览器，服务器接受得所有的跨域请求方法                   | 必选 |
| Access-Control-Allow-Headers     | 返回所有支持的头部     : 当request前端请求携带‘Access-Control-Request-Headers’时,该响应头必然回复Access-Control-Allow-Headers | 必选 |
| Access-Control-Allow-Credentials | 是否接受Cookie          <-----------响应中携带这种响应头，表示允许使用Cookie | 可选 |
| Access-Control-Max-Age           | OPTION请求缓存时间，单位s                                    | 可选 |

​	3，主请求阶段 

| 请求头 | 作用                 | 备注 |
| ------ | -------------------- | ---- |
| Origin | 表明此请求来自哪个域 |      |

​	4，主请求响应阶段

| 响应头                      | 作用               | 备注 |
| --------------------------- | ------------------ | ---- |
| Access-Control-Allow-Origin | 当前服务器接受得域 |      |



### Django添加跨域支持		   

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

### **Django配置流程**

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

### setting.py文件配置

```python
								# setting.py文件中添加
    
    1  APPEND_SLASH = False  # URL路径 APPEND_SLASH默认True:自动添加/,设置为False:不自动添加/
  	2  2.(1  MEDIA_URL = "/media/"　# 建议图片视频存储在此文件内
       2.(2  MEDIA_ROOT = os.path.join(BASE_DIR,"media/") # 自动拼接计算存储视频图片的位置   
```

```python
       2 .(3		 # 设置MEDIA_URL= "/media/" 需要在 url.py主路由中 设置如下：
       from django.conf import settings
       from django.conf.urls.static import static
        # 此方法表示使用MEDIA下访问静态资源将通过以下路径寻找
       urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```

**例 如:**

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



# RESTful 

# ：Representational State Transfer

## 一 . 什么是RESTful

​	1，资源 **（Resources）**

​		**网络上的一个实体，或者说是网络上的一个具体信息**，并且每个资源都有一个独一无二得URI与之对应；获取资源-直接访问URI即可。

​	2，**表现层（Representation）**

​		如何去表现资源  - 即资源得表现形式；如HTML , xml  , JPG , json等

​	3，**状态转化（State Transfer）**

​		访问一个URI即发生了一次 客户端和服务端得交互；此次交互将会涉及到数据和状态得变化

​		客户端需要通过某些方式触发具体得变化  -  HTTP method 如 GET， POST，PUT，PATCH，DELETE 等

​	**定　义 :**

​				流行的一种软件架构互联网，是一组架构的约束条件和有原则的架构，是一种规范，一种规则。

​				RESTful架构具有结构清晰，符合标准，易于理解以及扩展方便的特点。

## 二 .  RESTful的特征

​	1，每一个URI代表一种资源

​	2，客户端和服务器端之前传递着资源的某种表现

​	3，客户端通过HTTP的几个动作 对 资源进行操作 - 发生‘状态转化’



## 三 .  如何设计符合RESTful 特征的API接口

#### 	1 . 协议  - http/https

#### 	2 . 域名：

​		域名中体现出api字样，如

​		https://api.example.com

​		or

​		https://example.org/api/

#### 	3 .  版本:

​		解决开发中，不同组完成顺序的不一致，留给未开发完毕的小组旧版本号 例如：/v1/版本留给小组/v2/上线

​		https://api.example.com/v1/　　<----版本１

​		https://api.example.com/v2/　　<----版本2



#### 	4 . 路径 -　　

​		**路径名字重点仔细起名**

​		路径中避免使用**动词**，资源用名词表示，案例如下

```python
https://api.example.com/v1/users　　<------/v1访问路径后避免使用动词
https://api.example.com/v1/animals	<-----/v1访问路径后避免使用动词
```

#### 	5 . HTTP动词语义

| HTTP动词语义     | 语义不可变,必须严格按照以下的要求使用                      |
| ---------------- | ---------------------------------------------------------- |
| GET（SELECT）    | 从服务器取出资源（一项或多项）                             |
| POST（CREATE）   | 在服务器新建一个资源                                       |
| PUT（UPDATE）    | 在服务器更新资源（客户端提供改变后的完整资源）（全部更新） |
| PATCH（UPDATE）  | 在服务器更新资源（客户端提供改变的属性）（局部更新）       |
| DELETE（DELETE） | 从服务器删除资源                                           |

**注 意** ：Django文件上传中不支持PUT请求/PATCH请求,只支持小部分字符串上传，所以建议使用POST请求。

具体案例如下：

```python
GET /zoos：列出所有动物园
POST /zoos：新建一个动物园
GET /zoos/ID：获取某个指定动物园的信息
PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
DELETE /zoos/ID：删除某个动物园
GET /zoos/ID/animals：列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
```

#### 6 . 巧用查询字符串

```python
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?type_id=1：指定筛选条件
```

#### 7 . 状态码

​		1，用HTTP响应码表达 此次请求结果。

```python
200 OK - [GET]：服务器成功返回用户请求的数据
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误
```

​		2, 自定义内部code 进行响应　　　　**注** : code名自定义不限制名字为code

​		如 返回结构如下  {'code':200,  'data': {}, 'error': xxx}

#### 8 . 返回结果

​	根据HTTP 动作的不同，返回结果的结构也有所不同

```python
GET /users：返回资源对象的列表（数组）
GET /users/guoxiaonao：返回单个资源对象  建议{}
POST /users：返回新生成的资源对象
PUT /users/guoxiaonao：返回完整的资源对象
PATCH /users/guoxiaonao：返回完整的资源对象
DELETE /users/guoxiaonao：返回一个空文档
```

# python 字典 dict

![1564143035837](/home/tarena/.config/Typora/typora-user-images/1564143035837.png)



#### 字典 dict:键值对　字典键存储位置的计算

1 . 新创建的键值对，会根据字典键key计算一个Hash(哈希值)。

2 . 根据计算的Hash(哈希值)计算出一个为空的位置，存放新创建的键值对。

3 . 如果Hash(哈希值)计算的结果对应的位置已经有键值对存放，在Python中会执行**开放地址法**

4 . **开放地址法** :利用历经有键值对存放的位置，再次运行Hash(哈希值)计算，依次类推直到找到计算为空的位置。

5 . 如果字典中的键值对存储量已经占有字典的2/3,字典存储位置不足1/3,字典会自动进行扩容，所有位置会自动　	进行重新的Hash(哈希值)位置运算，大容量的字典扩容相对可怕，运行量相当大。

6 . 如果删除字典中某个键值对，会影响到利用该位置进行二次计算过Hash(哈希值)的键值对的位置。



# 		静态资源公司解决方法

#### 一 . CDN

​	购买CDN，交给CDN厂商处理

