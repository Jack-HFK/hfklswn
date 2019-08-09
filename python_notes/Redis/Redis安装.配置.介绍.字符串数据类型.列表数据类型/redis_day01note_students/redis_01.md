[TOC]

# **Redis数据库介绍**

- 特点及优点

```python
1、开源的，使用C编写，基于内存且支持持久化
2、高性能的Key-Value的NoSQL数据库
3、支持数据类型丰富，字符串strings，散列hashes，列表lists，集合sets，有序集合sorted sets 等
4、支持多种编程语言（C C++ Python Java PHP ... ）
5. '缓存性数据库':前端读取数据起到缓存的作用，防止缓存穿透 
6. 非常适合高并发读取数据的处理。
```

- 注 意

  ```python
  1.Redis**基于内存的数据库---------**MySQL**基于磁盘的数据库
  1.由于Redis基于内存,计算机重新启动内存东西丢失,重新启动后内存中的Redis重新加载存在磁盘的Redis备份。
  ```

- 与其他数据库对比

```python
1、MySQL : 关系型数据库，表格，基于磁盘，慢
2、MongoDB：键值对文档型数据库，值为JSON文档，基于磁盘，慢，存储数据类型单一
3、Redis的诞生是为了解决什么问题？？
   # 解决硬盘IO带来的性能瓶颈
```

- 应用场景

```python
1、使用Redis来缓存一些经常被用到、或者需要耗费大量资源的内容，通过这些内容放到redis里面，程序可以快速读取这些内容
2、一个网站，如果某个页面经常会被访问到，或者创建页面时消耗的资源比较多，比如需要多次访问数据库、生成时间比较长等，我们可以使用redis将这个页面缓存起来，减轻网站负担，降低网站的延迟，比如说网站首页等
３．需要实时性更新数据的场景。
```

- redis版本

```python
1、最新版本：5.0
2、常用版本：2.4、2.6、'2.8'、'3.0'、3.2、3.4、4.0、5.0
3、图形界面管理工具(写的一般)
	RedisDesktopManager
```

- 诞生历程

```python
# 1、历史
LLOOGG.com 公司帮助别的网站统计用户信息，各个网站发送的浏览记录都会存储到存储队列，5-10000条记录，多余5条需要收费

# 2、原理
FIFO机制，先进先出，满了进一条就出一条，网站越多，队列越多，推入和弹出操作越多

# 3、技术及问题
开始使用MySQL进行硬盘读写，速度很慢，导致无法实时显示，所以自己写了一个列表结构的内存数据库，程序性能不会受到硬盘IO的限制，加了持久化的功能

# 4、redis数据库戛然而生
# 为了解决负载问题，所以发明了redis
```

- Redis附加功能

```python
1、持久化
  将内存中数据保存到磁盘中，保证数据安全，方便进行数据备份和恢复
2、过期键功能
   为键设置一个过期时间，让它在指定时间内自动删除
   <节省内存空间>
   # 音乐播放器，日播放排名，过期自动删除等，都会缓存在Redis数据库中，MySQL数据库也会有备份。
3、事务功能
   原子的执行多个操作
4、主从复制
5、Sentinel哨兵
```

# **Redis安装**

### **Ubuntu版本安装及使用**

### Ubuntu版本启动与连接

```python
# 安装
sudo apt-get install redis-server
# 服务端启动Redis数据库，此命令启动的服务端终端关闭后依旧可以连接
sudo /etc/init.d/redis-server status | start | stop | restart
						'status: 查看状态　start:启动 stop:停止 restart:重启'

#　启动服务端，此命令启动不可以关闭终端
redis-server --port　端口号
						
# 客户端连接　　　'客户端连接后即可以使用Redis数据库了'
redis-cli -h IP地址 -p 端口  '默认端口6379 MySQL默认端口3306
redis-cli # 默认连接本机的6379端口　　　　

127.0.0.1:6379>ping　　'输入ping如果返回PONG表示连接畅通'
PONG
```

**Redis安装失败产生Ubuntu18.04无本地网卡问题解决方案**	

```python
# 环境
Vmware Workstion Player 15
Ubuntu18.04
解决方案
1.将网卡设置为 ：仅主机模式
2.在Linux命令行输入如下命令：
	1 . sudo service network-manager stop
    2 . sudo rm /var/lib/NetworkManager/NetworkManager.state
    3 . sudo service network-manager start
3.再输入指令: ifconfig ,ping www.baidu.com 测试
4.可选项:设置网卡为 NAT 模式   --------注意查看防火墙的限制导致的问题。 
```

### **Windows版本安装及使用**

```python
1、下载安装包
   https://github.com/ServiceStack/redis-windows/blob/master/downloads/redis-64.3.0.503.zip
2、解压安装包
3、启动服务端
   双击解压后的 redis-server.exe文件 
4、客户端连接
   双击解压后的 redis-cli.exe文件   '客户端连接后即可以使用Redis数据库了'
    
# 问题：关闭终端后服务终止
# 解决：将Redis服务安装到本地服务，终端关闭后依旧可以执行服务
1、重命名 redis.windows.conf文件 为 redis.conf,作为redis服务的配置文件
2、cmd命令行，进入到redis-server.exe所在目录
3、执行：redis-server --service-install redis.conf --loglevel verbose
4、计算机-管理-服务-Redis-启动

# 卸载Redis服务安装到本地服务
到 redis-server.exe 所在路径执行：
1、redis-server --service-uninstall
2、sc delete Redis  '彻底清除本地服务的残留'
```

### **配置文件详解**

- **配置文件所在路径**

```python
1、Ubuntu配置文件所在位置
	/etc/redis/redis.conf  			
	'打开文件指令:sudo vi /etc/redis/redis.conf 打开此文件进行设置 	
2、windows 下载解压后的redis文件夹中
	redis.windows.conf 
	redis.conf文件   '打开此文件进入即可设置'
```

- **设置连接密码**

```python
1、requirepass 密码
2、重启服务
   sudo /etc/init.d/redis-server restart
3、客户端连接
   redis-cli -h 127.0.0.1 -p 6379 -a 123456
   127.0.0.1:6379>ping
```

- **允许远程连接**

```python
1、# 注释掉IP地址绑定   #号注释  文件所在69行:
   bind 127.0.0.1      <-------注释此行
2、# 关闭保护模式（默认开始，不允许外部网络访问）  文件所在88行:
   protected-mode no    <-----默认为 protected-mode yes 改为 protected-mode no 
3、# 想要新配置生效 重启redis服务  
   sudo /etc/init.d/redis-server restart
```

- **远程连接测试**

  **Windows连接Ubuntu的Redis服务**

```python
# cmd命令行
1、d:
2、cd Redis3.0
3、redis-cli -h x.x.x.x -a 123456    # x.x.x.x : IP地址 
4、x.x.x.x:6379>ping
```

# Redis常用命令

### **五大数据类型**

**使用方法：**每个数据类型的使用方法都有一套自己的方法

Redis五大数据类型

```
1、字符串数据类型（string）
2、列表数据类型（list）
3、哈希散列数据类型（hash）
4、集合数据类型（set）
5、有序集合类型（sorted set）
```

MySQL四大数据类型

# **字符串类型(string)**

**特点**

```python
1、字符串、数字，都会转为字符串来存储
2、以二进制的方式存储在内存中
```

**注 意 :	Redis操作指令不区分大小写,Redis存储的KEY(键)和Value(值)区分大小写**

#### **字符串常用命令-==必须掌握==**

```python
# 1. 设置一个key-value
set key value
# 2. 获取key的值
get key							'示 例:	127.0.0.1:6379> get hfk   提取值为: "hfklswn"
# 3. key不存在时再进行设置(nx)
set key value nx
# 4. 设置过期时间(ex)
set key value ex seconds(秒)	    '示 例: 127.0.0.1:6379> set swn hfklswn nx ex 10

# 5. 同时设置多个key-value        
mset key1 value1 key2 value2 key3 value3  
							   '示 例 :127.0.0.1:6379> mset swn1 hfk1 swn2 hfk2 hfk3 swn3
# 6. 同时获取多个key-value
mget key1 key2 key3       	   '示 例 : 127.0.0.1:6379> mget swn1 swn2 swn3
```

#### **字符串常用命令==作为了解==**

```python
# 1.获取长度
strlen key
# 2.获取指定范围切片内容
getrange key start stop 	   'start 开始下标 结束下标'
# 3.从索引值开始，value替换原内容
setrange key index value      '示例: 127.0.0.1:6379> setrange hfks 4 love'
# 4.追加拼接value的值
append key value
```

#### **数值操作-==字符串类型数字(必须掌握)==**

```python
# 整数操作
INCRBY key 步长                '示 例 :127.0.0.1:6379> incrby number 8
DECRBY key 步长				 '示 例 :127.0.0.1:6379> DECRBY number 8
INCR key : +1操作
DECR key : -1操作
# 应用场景: 抖音上有人关注你了，是不是可以用INCR呢，如果取消关注了是不是可以用DECR

# 浮点数操作: 先转为数字类型，然后再进行相加减，不能使用append
incrbyfloat key step   
					'127.0.0.1:6379> incrbyfloat str 8.8  浮点数相加  
					'127.0.0.1:6379> incrbyfloat str -8.8  浮点数相减			 		
```

#### **键的命名规范**

​	mset  wang:email  wangweichao@tedu.cn

```python
127.0.0.1:6379> mset wang:email wangweichao@tedu.cn guo:email guods@tedu.cn
OK
127.0.0.1:6379> mget wang:email guo:email
1) "wangweichao@tedu.cn"
2) "guods@tedu.cn"
127.0.0.1:6379> 
```

#### **string命令汇总**

**注意 : 新旧版本string命令汇总，新版本支持旧版本命令**

```python
# 字符串操作
1、set key value
2、set key value nx
3、get key
3、mset
4、mget
5、set key value ex seconds
6、strlen key 
#　返回旧值并设置新值(如果键不存在，就创建并赋值)
7、getset key value
# 数字操作
8、incrby key 步长
9、decrby key 步长
10、incr key
11、decr key
12、incrbyfloat key number # (可以为整数或负数)
# 设置过期时间的两种方式
# 方式一
1、set key value ex 3
# 方式二 :之前版本指令，新版本也支持此命令
1、set key value
2、expire key 5 # 秒
3、pexpire key 5 # 毫秒
# 查看存活时间
ttl key
# 删除设置过期时间
persist key
```

# **通用命令 ==适用于所有数据类型==**

```python
# 切换库
select number    'number : 下标索引，从零开始索引。'
# 查看键
keys *           '示 例 : 127.0.0.1:6379> keys hfk 查看指定键的键(没啥用) '
# 键类型
TYPE key
# 键是否存在       '示 例: 127.0.0.1:6379> exists hfk [返回(integer) 1] '
exists key  存在：返回(integer) 1   不存在返回：(integer) 0      
# 删除键
del key
# 键重命名
rename key newkey
# 清除当前库中所有数据（慎用）
flushdb
# 清除所有库中所有数据（慎用）
flushall
```

**string数据类型注意**

```python
# key值取值原则
1、key值不宜过长，消耗内存，且在数据中查找这类键值的计算成本高
2、不宜过短，可读性较差
# 值
1、一个字符串类型的值最多能存储512M内容
```

**练习**

```python
1、查看 db0 库中所有的键
   select 0
   keys *
2、设置键 trill:username 对应的值为 user001，并查看
   set trill:username 'user001'
3、获取 trill:username 值的长度
   strlen trill:username
4、一次性设置 trill:password 、trill:gender、trill:fansnumber 并查看（值自定义）
   mset trill:password '123456' trill:gender 'm' trill:fansnumber 10
   mget trill:password trill:gender trill:fansnumber
5、查看键 trill:score 是否存在
   exists trill:score
6、增加10个粉丝
   incrby trill:fansnumber 10
7、增加2个粉丝（一个一个加）
   incr trill:fansnumber 
   incr trill:fansnumber
8、有3个粉丝取消关注你了
   decrby trill:fansnumber 3
9、又有1个粉丝取消关注你了
   decr trill:fansnumber
10、思考、思考、思考...,清除当前库
   flushdb
11、一万个思考之后，清除所有库
   flushall
```

# **列表数据类型（List）**

- 特点

```python
1、元素是字符串类型
2、列表头尾增删快，中间增删慢，增删元素是常态
3、元素可重复
4、最多可包含2^32 -1个元素    （2的32次方减1）
5、索引同python列表
6、列表数据类型只存在有数据的列表和没有列表，不存在空列表
```

#### **头尾压入元素（LPUSH | RPUSH）==必须掌握==**

​	1、**LPUSH key value**     列表左侧(头部)压入元素

​	2、**RPUSH key value**     列表右侧(尾部)压入元素

```python
127.0.0.1:6379> LPUSH mylist1 0 1 2 3 4
(integer) 5
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "4"
2) "3"
3) "2"
4) "1"
5) "0"
127.0.0.1:6379> RPUSH mylist2 0 1 2 3 4
(integer) 5
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "0"
2) "1"
3) "2"
4) "3"
5) "4"
127.0.0.1:6379> 
```

#### **查看|设置 列表元素  ==必须掌握=**

**查看（LRANGE)**  

**注意 : 索引查看结果包含列表的stop:结束值**

```python
LRANGE key start stop    # start:开始值  stop:结束值 
# 查看列表中所有元素        
LRANGE key 0 -1   		 # 查看值包含索引的结束下标所对应的值
```

**获取指定位置元素（LINDEX）**

```python
LINDEX key index		    'index:下标索引'
```

**设置指定位置元素的值（LSET）**

```python
LSET key index value  		'index:下标索引'
```

**获取列表长度（LLEN)**

```python
LLEN key
```

#### **头尾弹出元素（LPOP |  RPOP）==必须**

**注 意 : 弹出元素后，所在列表内的元素实质性弹出，列表中将不存在弹出的元素**

**LPOP key** : 从列表头部弹出一个元素

**RPOP key** : 从列表尾部弹出一个元素

**RPOPLPUSH** source destination : 从一个列表**尾部**弹出元素压入到另一个列表**头部**

**示 例 :**

```python
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "4"
2) "3"
3) "2"
4) "1"
5) "8"
127.0.0.1:6379> LPOP mylist1
"4"
127.0.0.1:6379> RPOP mylist1
"8"
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "3"
2) "2"
3) "1"
127.0.0.1:6379> RPOPLPUSH mylist1 mylist2
"1"
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "3"
2) "2"
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "1"
2) "0"
3) "1"
4) "2"
```

#### **移除指定元素（LREM）**

**LREM key count value**

```python
count>0：表示从头部开始向表尾搜索，移除与value相等的元素，数量为count  '表头向表尾搜索移除'
count<0：表示从尾部开始向表头搜索，移除与value相等的元素，数量为count  '表尾向表头搜索移除'
count=0：移除表中所有与value相等的值  	'全部移除'
value : 需要移除的对象(值)
key : 键
```

示 例:

```python
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "3"
2) "2"
127.0.0.1:6379> LPUSH mylist1 3 2
(integer) 4
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "2"
2) "3"
3) "3"
4) "2"
127.0.0.1:6379> LREM mylist1 1 2
(integer) 1
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "3"
2) "3"
3) "2"
127.0.0.1:6379> LREM mylist1 1 3
(integer) 1
127.0.0.1:6379> LRANGE mylist1 0 -1
1) "3"
2) "2"
127.0.0.1:6379> 
```

#### **去除指定范围外元素（LTRIM） ==必须掌握==**

**LTRIM key start stop**

```
 start : 指定范围起始值
 stop  : 指定范围结束值
 key : 键
```

**示 例 :**

```python
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "1"
2) "0"
3) "1"
4) "2"
5) "3"
6) "4"
127.0.0.1:6379> LTRIM mylist2 0 -2
OK
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "1"
2) "0"
3) "1"
4) "2"
5) "3"
127.0.0.1:6379> 
```

应用场景: 保存微博评论最后500条

```python
LTRIM user001::comments 0 499
```

#### **列表中插入值（LINSERT）**

**LINSERT key BEFORE|AFTER pivot value**

key和pivot不存在，不进行任何操作

```
BEFORE : 指定值的前边
AFTER ： 指定值的后边
pivot ：指定值
value : 插入的值
```

示例代码

```python
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "0"
2) "1"
3) "2"
4) "3"
5) "4"
127.0.0.1:6379> LINSERT mylist2 after 2 666
(integer) 6
127.0.0.1:6379> LINSERT mylist2 before 4 888
(integer) 7
127.0.0.1:6379> LRANGE mylist2 0 -1
1) "0"
2) "1"
3) "2"
4) "666"
5) "3"
6) "888"
7) "4"
127.0.0.1:6379> 
```

#### **阻塞弹出（BLPOP | BRPOP）==必须掌握==**

BLPOP key timeout

BRPOP key timeout

```python
1、如果弹出的列表不存在或者为空，就会阻塞
2、超时时间设置为0，就是永久阻塞，直到有数据可以弹出
3、如果多个客户端阻塞再同一个列表上，使用First In First Service原则，先到先服务
4、如果列表中的值为空，则返回值为None
key : 指定键
timeout : 指定需要阻塞的时间(需要阻塞多次时间)
阻塞弹出 : 指程序阻塞在此处等待列表中有值传来继续弹出，无值阻塞等待，程序不向下执行。
先到先服务　：　先阻塞程序的先执行列表传来的值然后弹出。
```

示例

```python
127.0.0.1:6379> BLPOP mylist2 0
1) "mylist2"
2) "3"
127.0.0.1:6379> BLPOP mylist2 0
1) "mylist2"
2) "2"
127.0.0.1:6379> BLPOP mylist2 0
1) "mylist2"
2) "1"
127.0.0.1:6379> BLPOP mylist2 0
# 阻塞了
```

```python
while True:
    #如果列表中为空时,返回None
    result = r.brpop("hfk",1)
    if result:
        print(result)
    else:
        break
```

#### **列表常用命令总结**

```python
# 增
1、LPUSH key value1 value2 
2、RPUSH key value1 value2
3、RPOPLPUSH source destination
4、LINSERT key after|before value newvalue
# 查
5、LRANGE key start stop
6、LLEN key   # 查询键(key)长度
# 删
7、LPOP key
8、RPOP key
9、BLPOP key timeout
10、BRPOP key timeout
11、LREM key count value  # 正数，负数，0
12、LTRIM key start stop  # 保留指定范围内的元素
# 改
13、LSET key index newvalue
```

**练习**

```python
1、查看所有的键
   keys *
2、向列表 spider::urls 中以RPUSH放入如下几个元素：01_baidu.com、02_taobao.com、03_sina.com、04_jd.com、05_xxx.com
   RPUSH spider::urls 01_baidu.com 02_taobao.com 03_sina.com 04_jd.com 05_xxx.com
3、查看列表中所有元素
   LRANGE spider::urls 0 -1
4、查看列表长度
   LLEN spider::urls
5、将列表中01_baidu.com 改为 01_tmall.com
   LSET spider::urls 0 01_tmall.com
6、在列表中04_jd.com之后再加1个元素 02_taobao.com
   LINSERT spider::urls after 04_jd.com 02_taobao.com
7、弹出列表中的最后一个元素
   RPOP spider::urls
8、删除列表中所有的 02_taobao.com
   LREM spider::urls 0 02_taobao.com
9、剔除列表中的其他元素，只剩前3条
   LTRIM spider::urls 0 2
```

# **python交互使用Redis**

**注 意 :**  

​		1 . **Python**中使用**Redis**时，得到的数据结果都是**字节串(bytes)**类型。

​		2 . **Python***中使用**Redis**时，获取key键对应的都是字节串列表。

- 模块

**Ubuntu安装Redis模块**

```python
sudo pip3 install redis
```

**Windows安装Redis模块**

```python
方法一  :  python -m pip install redis
方法二  :  以管理员身份打开cdm命令行
		  pip3 install redis
```

#### 使用流程

```python
import redis
# 创建数据库连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
```

#### 通用命令代码示例

```python
import redis

# 创建数据库连接对象
r = redis.Redis(host='192.168.43.49',port=6379,db=0,password='123456')

# [b'key1',b'key2'] 
print(r.keys('*'))

# 键类型： [b'key3']   :字节串列表
print(type('key3'))

# 是否存在：1 或者 0    :1代表存在 0代表不存在
print(r.exists('key4'))

# 删除key：hfk   返回值 :1 或者 0   :1代表删除成功 0代表删除对象不存在
r.delete('hfk')
```

#### **字符串命令代码示例**

```python
import redis

r = redis.Redis(host='192.168.43.49',port=6379,db=0)

r.set('mystring','python')
# b'python'
print(r.get('mystring'))
# False
print(r.setnx('mystring','socket'))
# mset：参数为字典
r.mset({'mystring2':'mysql','mystring3':'mongodb'})
# mget：结果为一个列表
print(r.mget('mystring','mystring2','mystring3'))
# mystring长度：6
print(r.strlen('mystring'))
# 数字类型操作
r.set('number',10)
r.incrby('number',5)
r.decrby('number',5)
r.incr('number')
r.decr('number')
r.incrbyfloat('number',6.66)
r.incrbyfloat('number',-6.66)
# b'10'
print(r.get('number'))
```

#### **python操作list**

```python
import redis

r = redis.Redis(host='192.168.43.49',port=6379,db=0)
# ['mysql','redis']
r.lpush('pylist','redis','mysql')
# ['mysql','redis','django','spider']
r.rpush('pylist','django','spider')
# ['mysql','redis','django','spider','AI']
r.linsert('pylist','after','spider','AI')
# 5
print(r.llen('pylist'))
# ['redis','django','spider']
r.lpop('pylist')
r.rpop('pylist')
# ['redis','django','spider']
print(r.lrange('pylist',0,-1))
# ['redis','spider']
r.lrem('pylist',0,'django')
# 返回True，['redis']
r.ltrim('pylist',0,0)
# 返回True，['spiderman']
r.lset('pylist',0,'spiderman')

r.delete('pylist')
```

**list案例: 一个进程负责生产url，一个进程负责消费url**

进程1: 生产者

```python
import redis
import random
import time

urls_list = [
    '01_baidu.com',
    '02_sina.com',
    '03_taobao.com',
    '04_tmall.com',
    '05_jd.com'
]
r = redis.Redis(host='192.168.43.49',db=0,password='123456')
while True:
    url = random.choice(urls_list)
    r.lpush('spider::urls',url)
    time.sleep(random.randint(1,5))
```

进程2: 消费者

```python
import redis

r = redis.Redis(host='192.168.43.49',db=0,password='123456')

while True:
    # 结果为元组
    try:
        url = r.blpop('spider::urls',3)
        print(url[1])
        r.lrem('spider::urls',count=0,value=url[1])
    except:
        print('爬取结束')
        break
```

```python
import redis
import time
import random


# 创建连接对象
r = redis.Redis(host='localhost',port=6379,db=0)

# 生产者开始生产URL地址
for page in range(0,67):
    url = "http://app.mi.com/category/2#page=%s" % str(page)
    r.lpush("hfk:url",url)
    print(url)
    time.sleep(random.randint(1,3))  # 等待时间随机1到3秒，执行一次
```

```python
import redis
import time
import random

# 创建连接对象
r = redis.Redis(host='localhost',port=6379,db=0)

while True:
    url = r.brpop("hfk",5)
    if url:
        # print(url)  # (b'hfk', b'value')
        print("正在抓取：",url[1].decode())
    else:
        print("抓取结束")
        r.delete("hfk")
        break
```











