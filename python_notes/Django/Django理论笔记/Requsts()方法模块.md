`requests`库是一个常用的用于`http`请求的模块，它使用`python`语言编写，可以方便的对网页进行爬取，是学习`python`爬虫的较好的http请求模块。

## 一、 requests模块的安装

首先我们要继续requests模块的安装。

### 1、 pip命令安装

- windows系统下只需要在命令行输入命令 pip install requests 即可安装
- 在 linux 系统下，只需要输入命令 sudo pip install requests ，即可安装。

### 2、下载安装包安装

由于`pip`命令可能安装失败所以有时我们要通过下载第三方库文件来进行安装。
在`github`上的地址为：<https://github.com/requests/requests> 
下载文件到本地之后，解压到`python`安装目录。 
之后打开解压文件，在此处运行命令行并输入：`python setup.py install` 即可。
之后我们测试`requests`模块是否安装正确，在交互式环境中输入 `import requests` 如果没有任何报错，说明`requests`模块我们已经安装成功了

## 二、requests模块的使用方法

### 1、requests库的七个主要方法

| 方法               | 解释                           |
| :----------------- | :----------------------------- |
| requests.request() | 构造一个请求，支持以下各种方法 |
| requests.get()     | 获取html的主要方法             |
| requests.head()    | 获取html头部信息的主要方法     |
| requests.post()    | 向html网页提交post请求的方法   |
| requests.put()     | 向html网页提交put请求的方法    |
| requests.patch()   | 向html提交局部修改的请求       |
| requests.delete()  | 向html提交删除请求             |

**(1)requests.get()**

这个方法是我们平时最常用的方法之一，通过这个方法我们可以了解到其他的方法，所以我们详细介绍这个方法。 
具体参数是：

```
r=requests.get(url,params,**kwargs)
```

- url: 需要爬取的网站地址。
- params: 翻译过来就是参数， url中的额外参数，字典或者字节流格式，可选。
- **kwargs : 12个控制访问的参数

我们先来讲讲**kwargs:
**kwargs有以下的参数，对于requests.get,其第一个参数被提出来了。

- params：字典或字节序列， 作为参数增加到url中,使用这个参数可以把一些键值对以?key1=value1&key2=value2的模式增加到url中

   

  例如：kv = {'key1':' values', 'key2': 'values'} 
  r = requests.get('[http:www.python123.io/ws](http://www.python123.io/ws)', params=kw)

- data：字典，字节序或文件对象，重点作为向服务器提供或提交资源是提交，，作为request的内容，与params不同的是，data提交的数据并不放在url链接里， 而是放在url链接对应位置的地方作为数据来存储。，它也可以接受一个字符串对象。

- json：json格式的数据， json合适在相关的html，http相关的web开发中非常常见， 也是http最经常使用的数据格式， 他是作为内容部分可以向服务器提交。

   

  例如：kv = {'key1': 'value1'} 
  r = requests.post('<http://python123.io/ws>', json=kv)

- headers：字典是http的相关语，对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何我们想模拟的浏览器来对url发起访问。

   

  例子： hd = {'user-agent': 'Chrome/10'} 
  r = requests.post('<http://python123.io/ws>', headers=hd)

- cookies：字典或CookieJar，指的是从http中解析cookie

- auth：元组，用来支持http认证功能

- files：字典， 是用来向服务器传输文件时使用的字段。

   

  例子：fs = {'files': open('data.txt', 'rb')} 
  r = requests.post('<http://python123.io/ws>', files=fs)

- timeout: 用于设定超时时间， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一个timeout的异常。

- proxies：字典， 用来设置访问代理服务器。

- allow_redirects: 开关， 表示是否允许对url进行重定向， 默认为True。

- stream: 开关， 指是否对获取内容进行立即下载， 默认为True。

- verify：开关， 用于认证SSL证书， 默认为True。

- cert： 用于设置保存本地SSL证书路径

其中response对象有以下属性：

| 属性                | 说明                                             |
| :------------------ | :----------------------------------------------- |
| r.status_code       | http请求的返回状态，若为200则表示请求成功。      |
| r.text              | http响应内容的字符串形式，即返回的页面内容       |
| r.encoding          | 从http header 中猜测的相应内容编码方式           |
| r.apparent_encoding | 从内容中分析出的响应内容编码方式（备选编码方式） |
| r.content           | http响应内容的二进制形式                         |

举例说明：

```
>>> import requests



>>> r=requests.get("http://www.baidu.com")



>>> r.status_code



200



>>>  r.encoding



'ISO-8859-1'



>>> r.apparent_encoding



'utf-8'



>>> r.text



'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>ipt> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ\x9b´å¤\x9aäº§å\x93\x81</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a com/ class=cp-feedback>æ\x84\x8fè§\x81å\x8f\x8dé¦\x88</a>&nbsp;äº¬ICPè¯\x81030173å\x8f·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'



>>> r.encoding='utf-8'



>>> r.text



'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta chref=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css="h读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'
```

（以上r.text内容过长，自行删除了部分，看出编码效果即可）

requests库的异常

注意`requests`库有时会产生异常，比如网络连接错误、`http`错误异常、重定向异常、请求`url`超时异常等等。所以我们需要判断`r.status_codes`是否是200，在这里我们怎么样去捕捉异常呢？

这里我们可以利用`r.raise_for_status()` 语句去捕捉异常，该语句在方法内部判断`r.status_code`是否等于200，如果不等于，则抛出异常。

于是在这里我们有一个爬取网页的通用代码框架：

```
try:



    r=requests.get(url,timeout=30)#请求超时时间为30秒



    r.raise_for_status()#如果状态不是200，则引发异常



    r.encoding=r.apparent_encoding #配置编码



    return r.text



except:



    return "产生异常" 
```

**(2) request.head()**

看代码：

```
>>> r=requests.head("http://httpbin.org/get")



>>>r.headers



 {'Connection': 'keep-alive', 'Server': 'meinheld/0.6.1', 'Date': 'Mon, 20 Nov 2017 08:08:46 GMT', 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'X-Powered-By': 'Flask', 'X-Processed-Time': '0.000658988952637', 'Content-Length': '268', 'Via': '1.1 vegur'}
```

**(3)requests.post()**

1、向url post一个字典：

```
>>> payload={"key1":"value1","key2":"value2"}



>>> r=requests.post("http://httpbin.org/post",data=payload)



>>> print(r.text)



{



  "args": {}, 



  "data": "", 



  "files": {}, 



  "form": {



    "key1": "value1", 



    "key2": "value2"



  }, 



  "headers": {



    "Accept": "*/*", 



    "Accept-Encoding": "gzip, deflate", 



    "Connection": "close", 



    "Content-Length": "23", 



    "Content-Type": "application/x-www-form-urlencoded", 



    "Host": "httpbin.org", 



    "User-Agent": "python-requests/2.18.4"



  }, 



  "json": null, 



  "origin": "218.197.153.150", 



  "url": "http://httpbin.org/post"



}
```

2、向url post 一个字符串，自动编码为data

```python
>>>r=requests.post("http://httpbin.org/post",data='helloworld')
>>>print(r.text)
{
  "args": {}, 
  "data": "helloworld", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "10", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/post"
}
```

3.向url post一个文件

```python
>>> import requests
>>> files = {'files':open('F:\\python\\test\\test_case\\files.txt','rb')}
>>> r = requests.post('https://httpbin.org/post',files=files)
>>> print(r.text)
{
    "args":{
    },
    "data":"",
    "files":{
        "files":"hello worle!"
    },
    "form":{
    },
    "headers":{
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"close",
        "Content-Length":"158",
        "Content-Type":"multipart/form-data; boundary=d2fb307f28aeb57b932d867f80f2f600",
        "Host":"httpbin.org",
        "User-Agent":"python-requests/2.19.1"
    },
    "json":null,
    "origin":"113.65.2.187",
 	"url":"https://httpbin.org/post"
}
```

**(5)requests.put()**

看代码：

```
>>> payload={"key1":"value1","key2":"value2"}
>>> r=requests.put("http://httpbin.org/put",data=payload)
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/put"
```

**(6)requests.patch()**

`requests.patch`和`request.put`类似。 
两者不同的是： 
当我们用`patch`时仅需要提交需要修改的字段。 
而用`put`时，必须将20个字段一起提交到`url`，未提交字段将会被删除。 
`patch`的好处是：节省网络带宽。

**(7)requests.request()**

requests.request(）支持其他所有的方法。 
`requests.request(method，url,**kwargs)`

- method: “GET”、”HEAD”、”POST”、”PUT”、”PATCH”等等
- url: 请求的网址
- **kwargs: 控制访问的参数