[TOC]

扩　展：

SPA ---------------Single Page Application--------------------------------建议简易页面使用

AJAX---------------------------Asynchronus javascript And XML 

JSON----------------JavaScript Object Notation----------------------XML(老旧版)被(JSON)逐渐替代-------(HTML必懂)

XHR-------------AJAX核心对象--------异步对象(XMLHttpRequest)

# AJAX

AJAX---------------------------Asynchronus javascript And XML --------------------------阿贾克斯

**AJAX简介：**

AJAX是一种用于创建快速动态网页的技术，通过在后台与服务器进行少量的数据交互，使网页实现异步更新。

意味着可以不重新加载整个页面的情况下，对页面的某部分进行更新。

Asynchronus (异步的)  javascript (JS) And  XML。

**AJAX的核心对象---------XMLHttpRequest(异步对象)**

# XHR

AJAX的核心对象--------------------------XHR---------------------------- XMLHttpRequest(异步对象)

**XHR简介:**

​		在XHR诞生前，网页获取客户端和服务器的任何状态更新，都需要刷新一次页面。

​		在XHR诞生后，完全可以通过JS代码异步实现这一次刷新过程，省略了每次整个页面刷新的弊端。

 **作 用**：

​	简称"xhr"

​	称为"**异步对象**"，代替浏览器向服务器异步的发送请求并接受请求。

#  创建异步对象(xhr)

​	xhr的创建是由**JS**来提供的。

​	主流的异步对象是XMLHttpRequest类型的，并且主流浏览器都支持。

​	主流浏览器：IE7+ , Chrom , Firefox , Safari , Opera ...

 **语 法**

​	**支持XMLHttpRequest:**

​			通过 : new XMLHttpRequest()　　　　　　　		  <---------高级版本，使用群体普遍

​	**不支持XMLHttpRequest:**

​			 通过 : new ActiveXObject("Microsoft.XMLhttp") 	 <----------低版本，使用群体少

####  判断浏览器的支持性 :

```javascript
if(window.XMLHttpRequest){	
		则说明浏览器支持：XMLHttpRequest()
}else{
		则说明浏览器支持: ActiveXObject("Microsoft.XMLHTTP")
}
```

```js
// 实例，封装判断浏览器的支持性函数
function createXhr(){
   //根据不同的浏览器创建不同的异步对象
   if(window.XMLHttpRequest){
       var xhr = new XMLHttpRequest();     <---------创建支持XHR的异步对象
   }else{
           var xhr = new ActiveXObject("Microsoft.XMLHTTP");　　<-----------创建支持AxO的异步对象
    }
    return xhr;
}
```

- ###  XHR的成员

####  open() ----方法

​	1 . 方 法

```
open()
```

​	2 .  **作 用** : **创建请求并发送请求**

​	3 . **语 法** ：

```javascript
xhr.open(method,url,async);
```

| 参　 数 | 作　用                     | 取　值                                            |
| ------- | -------------------------- | ------------------------------------------------- |
| method  | 请求方式                   | "get"  或  "post"                                 |
| url     | 请求地址                   | 字符串                                            |
| async   | 是否采用异步的方式发送请求 | true : 异步的发送请求　或　false : 同步的发送请求 |

注：async : 当代码中需要执行多次 : 向服务端发送请求时，如果后一次请求需要用前一次请求的结果，需要取值	   为false，请求发送设置为同步，以免造成前一次请求先结束，后一次请求没有得到前一次请求的结果。

```js
//使用get方式向02-server的地址发送异步请求
xhr.open("get","/02-server",ture)
```

#### readyState ----属性

1 . **作　用**：表示请求状态，通过不同的**请求状态值**来表示xhr与服务器的交互情况。

2 . 请求状态值 : 由0-4共5个值表示5个不同的状态，readyState的值只能取值，不能赋值。

| 请求状态值 | 由0-4共5个值表示5个不同的状态 |
| ---------- | ----------------------------- |
| 0          | 请求尚未初始化                |
| 1          | 已经与服务器建立联系          |
| 2          | 服务器端已经接受请求信息      |
| 3          | 服务器端处理中                |
| 4          | 服务端响应完成                |

- #### 注　意：先 readyState属性 后 status属性

  服务器响应请求时先响应readyState ----属性,再响应status ----属性。

  所以同时判断属性readyState和status响应时 : 先判断readyState属性再判断status 属性,先后顺序不能改变。

#### status ----属性

1 . **作　用**：　表示服务器端的响应状态码


| 服务器响应状态码 | 例如：                           |
| ---------------- | -------------------------------- |
| 404              | Not Found                        |
| 200              | 响应成功并返回正确的请求处理信息 |

```js
例如：
if(xhr.readyState4 && xhr.status==200){
	//满足条件，允许接受服务器端的响应信息
}
```

#### responseText ----属性

1 . **作　用**：　表示服务器端的响应回来的数据信息

```js
例如：
if(xhr.readyState4 && xhr.status==200){
	//满足条件，允许接受服务器端响应回来的信息
    console.log(xhr.responseText);
}
```

#### onreadystatechange -事件

1 . 作　用：每当**readyState**值发生改变时要触发的操作。

​	readyState：表示请求状态，通过不同的**请求状态值**来表示xhr与服务器的交互情况。

​	onreadystatechange -事件: 表示xhr与服务器的交互情况发生变化时要出发的事件。

​	onreadystatechange----------回调函数

2 . 操作 ---- 回调函数

3 . 每当服务器响应请求readyState值发生改变时,onreadystatechange回调函数返回重新调用

```js
示　例：
xhr.onreadystatechange = function(){
	if(xhr.readyState4 && xhr.status==200){
	//满足条件，允许接受服务器端的响应信息
    console.log(xhr.responseText);
	}
}
```

#### send() ----方法

1 . 作　用：通知xhr向服务器端开始发送请求。

2 . **语　法：**

```js
xhr.send(body)
```

**body参数**

| body     | 请求主体           | 示例:                |
| -------- | ------------------ | -------------------- |
| get请求  | body的值为null     | xhr.send(null)       |
| post请求 | body的值为请求数据 | xhr.send("请求数据") |

# AJAX的操作步骤

#### GET请求

​	1 . 创建 xhr 。

​	2 . 创建请求 - open() 

​	3 . 设置回调函数　-  onreadystatechange

​			(1) . 判断状态

​			(2) . 接收响应

​			(3) . 业务处理

​	4 . 发送请求 - send()

```js
function createXhr(){
   //根据不同的浏览器创建不同的异步对象
   if(window.XMLHttpRequest){
       var xhr = new XMLHttpRequest();
   }else{
       var xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xhr;
}
```

```html
	{# 引用js文件判断浏览器支持类型 #}
    <script src="/static/common.js"></script>
    <script>
        function btnShow(){
          //1 . 创建 xhr
            	//调用以上js文件的createXhr()方法，根据不同的浏览器创建不同的异步对象
                var xhr = createXhr();
          //2 . 创建请求 - open()　
                xhr.open("get","/ajax/server-02/",true);
          //3 . 设置回调函数　-  onreadystatechange
                xhr.onreadystatechange = function(){
                    if(xhr.readyState==4 && xhr.status==200){
                    //接受服务器端响应的数据
                    var res = xhr.responseText;
                    document.getElementById("show").innerHTML = res;
                    }
                }
          //4 . 发送请求 - send()
                xhr.send(null);
        }
    </script>
</head>
<body>
     <!--onclick 实现点击按钮时在控制台执行并输出-->
    <button onclick="btnShow()">异步显示</button>
    <a href="/ajax/server-02">同步显示</a>
    <div id="show"></div>
</body>
```

#### AJAX发送POST请求

１ . 创建xhr

２ . 创建请求

​	(1) . 请求方式改为POST

​	(2) . 有**请求参数**的话不能拼在地址后面,而是通过发送请求一同发送给服务器。

  3 . 设置回调函数

  4 . 设置请求消息头 ----Content - Type	

```javascript
xhr.setRequestHeader(
	"Content - Type",
	"application/x-www-form-urlencoded"
);
```

​	5 . 发送请求

```javascript
xhr.send("name=hfk&age=25&gender=男");
```

**示　例**：

```javascript
 <script src="/static/common.js"></script>
    <script src="/static/jquery-1.11.3.js"></script>
    <script>
        $(function(){
            /*为 #btnPost 绑定click 事件 */
            $("#btnPost").click(function(){
                //1.创建xhr
                var xhr = createXhr();
                //2.创建请求
                xhr.open("post","/ajax/server-05/",true)
                //3.设置回调函数
                xhr.onreadystatechange = function(){
                    if(xhr.readyState==4 && xhr.status==200){
                       alert(xhr.responseText);
                  }
                }
                //4.设置请求消息头
                xhr.setRequestHeader(
                    "Content-Type",
                    "application/x-www-form-urlencoded"
                );
                //5.发送请求
                // 获取csrfmiddlewaretoken的值
                var csrf = $("[name='csrfmiddlewaretoken']").val();
                var uname = $("#uname").val();
                var upwd = $("#upwd").val();
                var params = "uname="+uname+"&upwd="+upwd+"&csrfmiddlewaretoken="+csrf;
                xhr.send(params);
            });
        });

    </script>
</head>
```

```html
<body>
    {% csrf_token %}
    <p>
        用户名称 <input type="text" id="uname">
    </p>
    <p>
        用户密码 <input type="password" id="upwd">
    </p>
    <p>
        <input type="button" id="btnPost" value="注册">
    </p>
</body>
</html>
```

#### 获取{% csrf_token %}验证

一 . **定 义:**

跨站请求伪造CSRF : 某些恶意网站上包含链接、表单按钮或者JavaScript,它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，所以会设置中间件防止伪造的链接。
1 . 通过添加{% csrf_token %}验证。

2 . HTML中会出现**属性name名**为**csrfmiddlewaretoken**的**input**标签。

3 . input标签的value值是通过**防止跨站请求伪造CSRF中间件**的密码。

4 . 可以通过HTTP POST请求体中添加 csrfmiddlewaretoken=<input/>标签 发送验证码给服务器通过验证。

```javascript
// 获取csrfmiddlewaretoken的值
var csrf = $("[name='csrfmiddlewaretoken']").val();

例如：
<http://127.0.0.1:8000/?csrfmiddlewaretoken=csrf>
```
**HTML 中添加：{% csrf_token %}后的HTML**　

```html
HTML 中添加：　{% csrf_token %}　
服务器响应给客户端的HTML源代码中会传递input标签，随机生成value值作为通过中间件的密码,每次密码都不一样.
<input type='hidden' name='csrfmiddlewaretoken' 						         value='zKUrHwWHAQFIaquYDLohyBys1U0FQZquuW3qY5rtXn9QCeqOcxPLbRH4bMsfreA4' />
```

each()

------

------

# JSON

简 介：

​		JSON---------------JavaScript Object Notation---------------(JS 对象 表现方式)-------数据交换语言。

作 用:	JSON以 **JavaScript(JS)对象** 的格式来约束前后端交互的字符串数据 , 易于计算机数据解析和生成。

JSON ---------- JS对象

```javascript
使用 JS 对象表示一个人的信息，包含如下属性：
	name："姓名"
	age:"年龄"
	height:"身高"
	weight:"体重"
var obj = {
	name:"姓名",
	age:30,
	height:180,
	weight:180  <------------------JS中最后一个元素不能加逗号，否则报错。
}
```

#### JSON规范

##### JS 对 象　

​	**定　义 : 使用JSON表示单个对象**

​	1 . 使用 **{}** 表示一个对象。

​	2 . 在 **{}** 中使用 **key:value** 来表示属性(数据)。

​	3 . **key** 必须使用 **""** 引起来。

​	4 . **value** 如果是字符串的话，也必须使用 **""** 引起来。

​	5 .多对 **key:value** 之间使用**逗号 ,** 分割。

```javascript
示　例　：
var obj = '{"name":"hfk","age":30}';
```

##### JS 数 组

   **定　义** ：使用JSON表示多个对象 , 数组在JS中是用**中 **括号 [ ] **括起来的内容。

​	1 . 使用 **[ ]** 来表示一组对象。

```javascript
示　例　：
var objs = '[{"name":"hfk","age":30},{"name":"swn","age":28}, ... ...]';
```

# JSON后端发送前端接收

#### 前端中将JSON串转换为JS对象--parse()

**作　用**：前端接收后端数据，前端中将JSON字符串转换为JS对象。

一 . 将得到的**JSON**串转换成**JS对象/JS数组**

**语 法 :**

```javascript
var JS对象 = JOSN.parse(JSON字符串)
```

**对象**：在JS中表示为　**{}**　括起来的内容，{"key":"value"} 中 ：key为对象的属性，value为对应属性值。

**数组**：数组在JS中是用**中括号 [ ]**　括起来的内容。

```javascript
$("#btnJSON").click(function(){
                //1.模拟一个服务器端发送过来的JSON字符串
                var flight = '{"flighNO":"NH980","from":"PEK","to":"KIX","time":"14:20"}';
                //2.通过JSON.parse()将JSON字符串转换成JS对象
                var obj = JSON.parse(flight);
                //3.解析对象
                console.log("航班号:"+obj.flighNO);
                console.log("出发:"+obj.from);
                console.log("到达:"+obj.to);
                console.log("时间:"+obj.time);
            });
```

#### 服务器端将数据对象转换为JSON字符串

**作　用**：在python中的处理，服务器端将数据对象转换为JSON字符串发送给前端。

**规    范:**

​	1 . 允许将 元组　列表　字典　转化为JSON字符串发送给前端。

​	2 . 元组　列表　字典　中的内容必须是字符串，数字，元组，列表，字典。

##### JsonResponse 模块

功 能: 

​		使用 Django下的 JsonResponse 模块，直接转换 字典/列表 为 JSON串并发送给客户端。

​		相当于 HttpResponse模块 ，但是 JsonResponse省略了转换 JSON串的步骤。

```python
from django.http import JsonResponse
from django.http import HttpResponse
import json 

def jsonserver_views(request):
    #1. 使用字典来表示JSON数据
    dic = {
        "course":"Ajax","duration":3,"place":"BJ",
    }
    # 将dic通过Json.dumps转换为JSON格式的字符串,返回值为json字符串
    #jsonStr = json.dumps(dic)  # 只能传递给dumps一个参数
    # 使用列表表示多个JSON数据(列表封装字典)
    lis = [dic,{"a":1,"b":2,"c":"pig"},]
    #return HttpResponse(lis)
	return JsonResponse(lis)
```



##### **Python方法dumps()**

**作 用：**Python中提供了 **json** 模块，**json** 模块中提供了 **dumps** 方法实现 **json**字符串的转换

**语 法 :**

```python
import json
object = json.dumps(参数)
```

```python
import json 
def jsonserver_views(request):
    #1. 使用字典来表示JSON数据
    dic = {
        "course":"Ajax","duration":3,"place":"BJ",
    }
    # 将dic通过Json.dumps转换为JSON格式的字符串,返回值为json字符串
    jsonStr = json.dumps(dic)  # 只能传递给dumps一个参数
    # 使用列表表示多个JSON数据(列表封装字典)
    lis = [dic,{"a":1,"b":2,"c":"pig"},]
    return HttpResponse(lis)

#显示结果：{'course': 'Ajax', 'duration': 3, 'place': 'BJ'}{'a': 1, 'b': 2, 'c': 'pig'}
```

**dumps(参数)** : dumps方法的参数只能传递一个参数。

separators参数：

​						指定序列化后的JSON字符串格式，第一个参数指每个键值对之间的连接符号，第二个参数指的是每						一个键和键之间的连接符号

------

##### Django方法

**作 用：**使用**Django**中提供的序列化模块来完成**数据**到 JSON 字符串的转换

​			使用**Django**中提供的序列化模块来完成**QuerySet**到 JSON 字符串的转换

```python
from django.core import serializers

	jsonStr = serializers.serialize("json",QuerySet)
```

```python
def jsonusers_views(request):
    users = Users.objects.all()
    # user =json.dumps(users)
    # return HttpResponse(user)
    jsonUser = serializers.serialize("json",users)
    return HttpResponse(jsonUser)

# 显示结果为:
[
	{"model": "ajax.users",
	 "pk": 1,
	 "fields": {"uname": "wang",
	 			"upwd": "123456", 
	 			"uemail": "wang@qq.com", 
	 			"nickname": "wangwc"}
		}
	]
```

# JSON前端发送后端接收

#### 前端中将JS对象转换为JSON字符串--stringify()

**作 用：**前端中将JS对象转换为JSON字符串发送给服务器端。

**方 法：**

```javascript
JSON.stringify()
```

```javascript
 <script>
        $(function(){
            $("#zhuce").click(function(){
                var xhr = createXhr();
                var params = {
                    username:$("#username").val(),
                    userpassword:$("#userpassword").val(),
                    useremail:$("#useremail").val(),
                    usernickname:$("#usernickname").val(),
                }
                // 将params转换为JSON字符串
                var str = JSON.stringify(params)
                xhr.open("get","/ajax/user-login-B/?params="+str,true);
                xhr.onreadystatechange = function(){
                    if(xhr.readyState==4 && xhr.status==200){
                        alert(xhr.responseText);
                    }
                }
                xhr.send(null);
            });
        });
    </script>
```



#### 服务器端将JSON字符串转换为字典/列表loads()

**作 用：**服务器端将JSON字符串转换为字典/列表格式字符串loads()

**方 法 ：**

```python
import json
josn.loads(jsonStr)
```

```python
def user_loginB(request):
    params = request.GET["params"]
    # 将params转换成Python字典
    dic = json.loads(params)
    try:
       Users.objects.create(uname=dic["username"],upwd=dic["userpassword"],                      					  uemail=dic["useremail"],nickname=dic["usernickname"])
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册失败")
```

# JQuery对AJAX的支持

简 介：JQuery对AJAX的支持提供了多种方法

#### $.each()

作 用 :　全局JQuery.$.each()函数也既是$.each()函数，它可以用来遍历任何一个集合，不管是JavaScript对象			   或者是一个JavaScript数组，或者是一个JSon对象。

语 法 : 

```
$.each(collection,callback(indexinArray,valueOFElement))
```

参 数 用 法 :

**collection** :	需要遍历的JS对象或JS数组。

**callback** :  回调函数，用于遍历collection所对应的JS对象或JS数组，

​				1 . indexinArray 遍历对象的下标索引

​				2 . valueOFElement遍历对象的下标索引所对应的值

```javascript
<script>
        $(function(){
            $("#btnShow").click(function(){
                var xhr = createXhr();
                xhr.open("get","/ajax/json-display-08B/",true);
                xhr.onreadystatechange = function(){
                    if(xhr.readyState==4 && xhr.status==200){
                        //接收响应数据并转换为JS数组
                        var suers = JSON.parse(xhr.responseText)
                        var html = "";
                        $(suers).each(function(i,obj){
                            html += "<tr>";
                                html += "<td>"+obj.pk+"</td>"
                                html += "<td>"+obj.fields.uname+"</td>"
                                html += "<td>"+obj.fields.upwd+"</td>"
                                html += "<td>"+obj.fields.uemail+"</td>"
                                html += "<td>"+obj.fields.nickname+"</td>"
                                html += "</tr>"
                        });
                        $("#content").html(html);
                        }
                    }
                xhr.send(null);
            });
        });
</script>
```

​				

#### $obj.load()

**作 用 :** 加载远程指定地址的页面内容到**$obj**中

​			适合用于把远程的页面加载到本页面中显示。

**参 数 用 法 :**		

**url** : 请求地址

**data** : 请求参数(可以省略)，如果没有参数则使用GET请求方式

1 . 通过字符串传参

```
"key1=value1&key2=value2"   注: 此种方法会使用GET请求方式发送请求。
```

2 . 通过JS对象传参

```
{key1:"value",key2:"value"}   	注:此种方法会使用POST请求方法发送请。
```

**callback** : 响应成功后的回调(可选)

```javascript
function(responseText){
    responseText:表示响应回来的数据    <-----创建变量responseText接收响应回来的数据
}
```

**语 法 :**

```python
$obj.load(url,data,callback)

url : 请求地址
data : 请求参数    
callback : 响应成功后的回调
```

```javascript
<script src="/static/jquery-1.11.3.js"></script>
<script>
        $(function(){
            //加载URL路径为/ajax/head-13的页面到id为#top中
            $("#top").load("/ajax/head-13",function(resText){
                console.log(resText);
                window.setTimeout(function(){ //超时调用(一次性定时器)等待多久之后执行一次代码
                    $("#top").hide(5000); //hide(5000) 隐藏功能，参数为隐藏起来所需要的时间
                },5000);
            });
            //加载URL路径为/ajax/head-13的页面到id为#base中
            $("#base").load("/ajax/head-13");
        })
 </script>
```

#### $.get()

**作 用 :** 　通过GET方式异步的向远程地址发送请求

​	注 : 	只能使用GET请求方式和异步对象方式一起使用。

**参 数 方 法 :**

**url** :请求地址
**data** : 请求参数[可选]

​	1 . 通过字符串传参

```
"key1=value1&key2=value2"   注: 此种方法请求参数只能使用GET请求方式发送请求。
```

**callback** : 响应成功后的回调函数[可选]

```javascript
function(responseText){
    responseText:表示响应回来的数据
}
```

**type** : 响应回来的数据格式

```javascript
可 选 参 数：
1 . html :　响应回来的文本当成html文本处理

2 . text :　响应回来的文本当成普通文本处理

3 . script : 响应回来的文本当成JS脚本执行

4 . json : 响应回来的文本是JSON格式，会直接转换成JS对象/JS数组 
```

**语 法 :**

```
$get(url,data,callback,type)

url :请求地址
data : 请求参数[可选]
callback : 响应成功后的回调函数[可选]
type : 响应回来的数据格式[可选]
```

#### $.post()

**作 用 :** 　通过POST方式异步的向远程地址发送请求

​	注 : 	只能使用POST请求方式和异步对象方式一起使用。

**参 数 方 法 :**

**url** :请求地址
**data** : 请求参数[可选]

​		1 . 通过JS对象传参

```
{key1:"value",key2:"value"}   	注:此种方法请求参数只能使用POST请求方法发送请。
```

**callback** : 响应成功后的回调函数[可选]

```javascript
function(responseText){
    responseText:表示响应回来的数据
}
```

**type** : 响应回来的数据格式

```javascript
可 选 参 数：
1 . html :　响应回来的文本当成html文本处理

2 . text :　响应回来的文本当成普通文本处理

3 . script : 响应回来的文本当成JS脚本执行

4 . json : 响应回来的文本是JSON格式，会直接转换成JS对象/JS数组 
```

**语 法 :**

```
$.post(url,data,callback,type)

url :请求地址
data : 请求参数[可选]
callback : 响应成功后的回调函数[可选]
type : 响应回来的数据格式[可选]
```

#### $.ajax()

**作 用** : 自定义所有的自身ajax()方法的参数 

**语 法 :**

```javascript
$.ajax({AJAX的参数对象})            <-----------大括号不可省略
```

**参 数 方 法 :**

**url** :请求地址
**data** : 请求参数[可选]

​	1 . 通过字符串传参

```
"key1=value1&key2=value2"   注: 此种方法会使用GET请求方式发送请求。
```

​	2 . 通过JS对象传参

```
{key1:"value",key2:"value"}   	注:此种方法会使用POST请求方法发送请。
```

**type :** 

```
请求方式 ： "get"  或  "post"
```

**dataType** : 响应回来的数据格式。

```
可 选 参 数：
1 . html :　响应回来的文本当成html文本处理

2 . text :　响应回来的文本当成普通文本处理

3 . script : 响应回来的文本当成JS脚本执行

4 . json : 响应回来的文本是JSON格式，会直接转换成JS对象/JS数组 
```

**async** : 是否采用异步的方式发送请求

```
true : 异步(默认)
false : 同步
```

**success** : 响应成功后的回调函数

```
function(responseText){
	responseText:表示响应回来的数据
}
```

**error** : 请求或响应失败时的回调函数

```
function(){
	请求或响应失败时需要执行的函数
}
```

