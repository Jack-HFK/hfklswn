[TOC]

# 故情回顾

### **五大数据类型**

```python
1、字符串数据类型（string）
2、列表数据类型（list）
3、哈希散列数据类型（hash）
4、集合数据类型（set）
5、有序集合类型（sorted set）
```

### **字符串类型**指令

```python
# 设置key相关操作
1、set key value
2、setnx key value
3、mset k1 v1 k2 v2 k3 v3
4、set key value ex seconds
5、set key value
5、expire key 5
5、pexpire key 5
5、ttl key
5、persist key
# 获取key相关操作
6、get key
7、mget k1 k2 k3
8、strlen key 
# 数字相关操作
7、incrby key 步长
8、decrby key 步长
9、incr key
10、decr key
11、incrbyfloat key number
```

### **列表类型指令**

```python
# 插入元素相关操作
1、LPUSH key value1 value2 
2、RPUSH key value1 value2
3、RPOPLPUSH source destination
4、LINSERT key after|before value newvalue
# 查询相关操作
5、LRANGE key start stop
6、LLEN key
# 删除相关操作
7、LPOP key
8、RPOP key
9、BLPOP key timeout
10、BRPOP key timeout
11、LREM key count value
12、LTRIM key start stop
# 修改指定元素相关操作
13、LSET key index newvalue
```

**思考：**

**Redis列表如何当做共享队列来使用？？？**

```python
# 同学你好，你还记得小米应用商店爬取URL地址的案例吗？
1、生产者消费者模型
2、生产者进程在列表中 LPUSH | RPUSH 数据，消费者进程在列表中 RPOP | LPOP 数据
```

### **Python与redis交互注意**

```python
1、r.set('name','Tom',ex=5,nx=True)
2、r.mset({'user1:name':'Tom','user1:age':'25'})
# 有元素时返回弹出元素,否则返回None
3、r.brpop('mylist')
```

# **位图操作bitmap**

**定义**

```python
1、位图不是真正的数据类型，它是定义在字符串类型中
2、一个字符串类型的值最多能存储512M字节的内容，位上限：2^32
3、数据以二进制存储在数据库，位图就是操作其中的这些二进制。<把二进制的０改为１或１改为０>
# 1MB = 1024KB
# 1KB = 1024Byte(字节)
# 1Byte = 8bit(位)
```

**强势点**

```python
1.可以实时的进行统计，极其节省空间。
2.位图操作拥有极快的速度，消耗内存相当少，相当节约内存。
3.目前主用于日常的大量的用户统计
典型案例：
官方在模拟1亿2千8百万用户的模拟环境下，在一台MacBookPro上，典型的统计如“日用户数”的时间消耗小于50ms, 占用16MB内存
```

### **设置某一位上的值（setbit）**

```python
# 设置某一位上的值（offset是偏移量，从0开始）　【offset是偏移量：相当于索引的意思】
     # 【二进制中的某一位的值设置为０或者１】
setbit key offset value      '[设置成功返回0，设置失败返回1][每8bit(位)代表一个字节]'

# 获取某一位上的值【某一位的值是０或者是１】
GETBIT key offset

# 统计键所对应的值中有多少个 1 
BITCOUNT key
```

**示 例：设置某一位上的值**

setbit key offset value

```python
# 默认扩展位以0填充        
127.0.0.1:6379> set mykey ab			# 设置魔key对应的值为0或1，通过读取0或1，判断某些条件
OK
127.0.0.1:6379> get mykey
"ab"
127.0.0.1:6379> SETBIT mykey 0 1
(integer) 0
127.0.0.1:6379> get mykey
"\xe1b"
127.0.0.1:6379> 
```

**示 例：获取某一位上的值**

GETBIT key offset

```python
127.0.0.1:6379> GETBIT mykey 3
(integer) 0
127.0.0.1:6379> GETBIT mykey 0
(integer) 1
127.0.0.1:6379> 
```

****

**示 例：统计键所对应的值中有多少个1**  

BITCOUNT key

```python
127.0.0.1:6379> SETBIT user001 1 1
(integer) 0
127.0.0.1:6379> SETBIT user001 30 1
(integer) 0
127.0.0.1:6379> bitcount user001
(integer) 2
127.0.0.1:6379> 
```

**应用场景案例**

网站用户的上线次数统计（寻找活跃用户）

用户名为key，上线的天作为offset，上线设置为1

示例: 用户名为 user001 的用户，今年第1天上线，第30天上线

SETBIT user1:login 1 1 

SETBIT user1:login 30 1

BITCOUNT user1:login

**代码实现**

```python
import redis

r = redis.Redis(host="127.0.0.1",port=6379,db=0)

# user1 :　设置user1一年中的第5天和200天登录
r.setbit("user1",4,1)
r.setbit("user1",199,1)
# user2 :　设置user2一年中的第100天和300天登录
r.setbit("user2",99,1)
r.setbit("user2",299,1)
# user3 :　设置user3一年中登录了100天以上
for i in range(1,366,2):
    r.setbit("user3",i,1)
# user4 :　设置user4一年中登录了100天以上
for i in range(1,366,3):
    r.setbit("user4",i,1)

# 获取所有的键
user_list = r.keys("user*")
# 存放活跃用户
active_user = []
# 存放不活跃用户
no_active_user = []
for user in user_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_user.append((user,login_count))
    else:
        no_active_user.append((user,login_count))

for user in active_user:
    for i in user:
        print("活跃用户：%s,活跃次数：%s"%(user[0],user[1]))

for user in no_active_user:
        print("不活跃用户：%s,活跃次数：%s"%(user[0],user[1]))
```

# **Hash散列数据类型**

- **定义**

```python
1、由field和关联的value组成的键值对
2、field和value是字符串类型
3、一个hash中最多包含2^32-1个键值对
```

- **优点**

```python
1、节约内存空间
2、每创建一个键，它都会为这个键储存一些附加的管理信息（比如这个键的类型，这个键最后一次被访问的时间等）
3、键越多，redis数据库在储存附件管理信息方面耗费内存越多，花在管理数据库键上的CPU也会越多
```

- **缺点（不适合hash情况）**

```python
1、不能使用二进制位操作命令:SETBIT、GETBIT、BITCOUNT等，如果想使用这些操作，只能用字符串键
2、不能使用过期键ex功能：键过期功能只能对 键 进行过期操作，而不能对散列的 字段 进行过期操作
	设置过期功能后针对的只是键的过期时间。
```

**Hash散列示意图：**

![](/home/tarena/hfk_python/python_notes/Redis/Redis集合.有序集合.Hash散列数据类型.位图/redis_day02_note_complete/MYXJ_20190806200526_save.jpg)



### **Hash散列基本命令操作**

```python
# 1、设置单个字段
HSET key field value　　　　　# field : 字段　 value :　字段值
HSETNX key field value			
									'示 例 127.0.0.1:6379> hset key1 name1 value1  
# 2、设置多个字段 				# field : 字段　 value :　字段值
HMSET key field value field value   
							'示 例 127.0.0.1:6379> HMSET key2 name1 value1 name2 value2 '
# 3、返回字段个数
HLEN key  							'示 例 127.0.0.1:6379> hlen key2'

# 4、判断键的字段是否存在（不存在返回 0  存在返回 1 如果键不存在也返回 0 )
HEXISTS key field　　

# 5、返回字段值
HGET key field   					'示 例 127.0.0.1:6379> HGET key1 name1'

# 6、返回多个字段值
HMGET key field filed

# 7、返回所有的键值对(返回字典)--> 键(key)和对应的值(value) ... 依照 "键","值","键","值"...依次排开
HGETALL key

# 8、返回所有键的字段名
HKEYS key

# 9、返回键的字段对应所有的值
HVALS key

# 10、删除键指定的字段
HDEL key field 

# 11、在字段对应值上进行整数增量运算(如果没有对应的字段或值，创建该字段和值)
HINCRBY key filed increment

# 12、在字段对应值上进行浮点数增量运算
HINCRBYFLOAT key field increment
```

**python基本方法**

```python
# 1、更新一条数据的属性，没有则新建
hset(name, key, value) 
# 2、读取这条数据的指定属性， 返回字符串类型
hget(name, key)
# 3、批量更新数据（没有则新建）属性,参数为字典
hmset(name, mapping)
# 4、批量读取数据（没有则新建）属性
hmget(name, keys)
# 5、获取这条数据的所有属性和对应的值，返回字典类型
hgetall(name)
# 6、获取这条数据的所有属性名，返回列表类型
hkeys(name)
# 7、删除这条数据的指定属性
hdel(name, *keys)
```

### **Python代码操作hash散列**

```python
import redis

r = redis.Redis(host="192.168.153.136", port=6379, db=0)
# 新建一条键名为"user1"的数据, 包含属性name
r.hset("user1", "name", 'zhanshen001')
# 更改键名为"userinfo"的数据, 更改属性username的值
r.hset("user1", "name", 'zhanshen002')

# 取出属性username的值
username = r.hget("user1", "name")

# 输出看一下
print('name',username)

# 属性集合
user_dict = {
    "password": "123456",
    "name": "Wang Success",
    "sex": "male",
    "height": '178',
    "Tel": '13838383888',
}
# 批量添加属性
r.hmset("user1", user_dict)

# 取出所有数据(返回值为字典)
all_data = r.hgetall("userinfo")
print('all_data:', all_data)

# 删除属性(可以批量删除)
r.hdel("user1", "Tel")

# 取出所有属性名 : 列表
h_keys = r.hkeys("user1")
print('all_key_name:',h_keys)

# 取出所有属性值 : 列表
h_values = r.hvals('user1')
print('all_values:',h_values)
```

**应用场景：微博好友关注**

```python
1、用户ID为key，Field为好友ID，Value为关注时间
	user:10000 user:606 20190520
	user:10000 user:605 20190521
2、用户维度统计
   统计数包括：关注数、粉丝数、喜欢商品数、发帖数
   用户为key，不同维度为field，value为统计数
   比如关注了5人
	HSET user:10000 fans 5
	HINCRBY user:10000 fans 1
```

**应用场景: redis+mysql+hash组合使用**

- 原理

  ```python
  用户想要查询个人信息
  1.步骤一 先到到redis缓存中查询个人信息
  2.步骤二 redis中查询不到，到mysql查询，返回数据到客户端并缓存到redis
  3.步骤三 在一定时间内，再次查询个人信息，直接到redis缓存中查询。
  ```

- 代码实现

  ```python
  import redis
  import pymysql
  
  # 1、到redis中查询个人信息
  # 2、redis中查询不到，到mysql查询，并缓存到redis
  # 3、再次查询个人信息
  
  
  r = redis.Redis(host='192.168.153.136',port=6379,db=0)
  
  username = input('请输入用户名:')
  # 如果redis中没有缓存，则返回空字典{}
  result = r.hgetall(username)
  print('redis中找到:',result)
  
  # mysql中表字段: username、password、gender、age
  if not result:
      db = pymysql.connect('192.168.153.136','tiger','123456','spider',charset='utf8')
      cursor = db.cursor()
      cursor.execute('select gender,age from user where username=%s',[username])
      # (('m',30),)
      userinfo = cursor.fetchall()
      if not userinfo:
          print('MySQL中用户信息不存在')
      else:
          dict = {
              'gender':userinfo[0][0],
              'age':userinfo[0][1]
          }
          # hmset第二个参数为字典
          r.hmset(username,dict)
          # 设置过期时间为5分钟
          r.expire(username,60*5)
          print('redis缓存成功')
  ```

  

**mysql数据库中数据更新信息后同步到redis缓存**

用户修改个人信息时，要将数据同步到redis缓存

```python
import redis
import pymysql

# 当用户修改个人信息时，要同步更新到redis缓存中

def update_mysql(username,new_age):
    #  连接MySQL
    db = pymysql.connect('192.168.153.136','tiger','123456','spider',charset='utf8')
    cursor = db.cursor()
    cursor.execute('update user set age=%s where username=%s',[new_age,username])
    db.commit()
    cursor.close()
    db.close()

def update_redis(username,new_age):
    #  连接redis
    r = redis.Redis(host='192.168.153.136', port=6379, db=0)
    # 同步更新redis缓存
    r.hset(username,'age',new_age)
    print('已同步到redis缓存')
    # 设置过期时间为5分钟
    r.expire(username,60*5)
    # 从redis中打印查看
    print(r.hget(username,'age'))

if __name__ == '__main__':
    username = input('请输入用户名:')
    new_age = input('请输入新年龄:')
	update_mysql(username,new_age):
	update_redis(username,new_age)

"""
示 例： 更改mysql数据库数据，同步到redis数据库
"""
import redis
import pymysql

# 创建mysql连接
msdb = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456",
                       charset="utf8",
                       database="redis")

# 创建redis连接
rdb = redis.Redis(host="localhost", port=6379, db=0)

# 更新MySQL数据库
def update_mysql(age,username):
    # 创建mysql游标对象
    cursor = msdb.cursor()
    upd = "update user set age=%s where username=%s"
    try:
        # code 1 或 0
        code = cursor.execute(upd,[age,username])
        print(code)
        # 提交到数据库
        msdb.commit()
        if code == 1:
            return True
    except Exception as e:
        print("error:",e)
        msdb.rollback()  # 回滚
    # 关闭游标对象
    cursor.close()
    # 关闭数据库连接
    msdb.close()

# 更新Redis数据库
def update_redis(age):
    rdb.hset("user","age",age)
    print("已经同步到Redis")
    # 设置过期时间
    rdb.expire("suer",3)

if __name__ == "__main__":
    username = input("请输入用户名")
    age = input("请输入更改后的年龄")
    if update_mysql(age,username):
        update_redis(age)
    else:
        print("用户名有误")
```

# **集合数据类型(set)**

- 特点

```python
1、无序、去重      -----> 存放数据顺序无序,不存放重复的数据，去调重复数据再存放。
2、元素是字符串类型
3、最多包含2^32-1个元素
```

### **集合数据类型基本命令**

```python
# 1、增加一个或者多个元素,自动去重  <----键(key)存在 : 增加  键(key)不存在 : 创建
SADD key value1 value2         <----- '添加失败返回添加0，添加成功返回添加个数1

# 2、查看集合中所有元素
SMEMBERS key

# 3、删除一个或者多个元素，元素不存在自动忽略
SREM key value1 value2

# 4、元素是否存在 [返回 0 不存在][返回 1 存在]
SISMEMBER key value

# 5、随机返回集合中指定个数的元素，默认为1个 [count : 指定随机返回的个数]
SRANDMEMBER key [count]

# 6、随机弹出成员 默认随机弹出 1 个value(值)  [count : 指定随机弹出的个数]
SPOP key [count] 

# 7、返回集合中元素的个数，不会遍历整个集合，只是存储在键当中了
SCARD key

# 8、把元素从原集合移动到目标集合 [source : 原集合][destination : 目标集合]
SMOVE source destination value

# 9、差集
SDIFF key1 key2  '[键(key1) 相对键 (key2) 键(key2)中没有的value]'
SDIFF key2 key1  '[键(key2) 相对键 (key1) 键(key1)中没有的value]'

# 10、差集保存到指定的集合中  [destination : 指定集合]
		'[键(key1) 相对键 (key2) 键(key2)中没有的value(值) 保存到destination指定集合中]'
		SDIFFSTORE destination key1 key2 
		'[键(key2) 相对键 (key1) 键(key1)中没有的value(值) 保存到destination指定集合中]'
		SDIFFSTORE destination key2 key1 	#	[如果destination指定的集合存在值将会被覆盖]
					
# 11、交集 (两个集合都有的)
SINTER key1 key2
SINTERSTORE destination key1 key2

# 12、并集 (两个集合并，得到结果去掉重复的)
SUNION key1 key2
SUNIONSTORE destination key1 key2
```

**案例: 新浪微博的共同关注**

需求: 当用户访问另一个用户的时候，会显示出两个用户共同关注过哪些相同的用户

设计: 将每个用户关注的用户放在集合中，求交集即可

实现:

user001 = {'peiqi','qiaozhi','danni'}

user002 = {'peiqi','qiaozhi','lingyang'}

user001和user002的共同关注为:

SINTER user001 user002 

结果为: {'peiqi','qiaozhi'}

### **python操作集合set**

```python
# 1、给name对应的集合中添加元素
sadd(name,values)		'r.sadd("set_name","tom")
						'r.sadd("set_name","tom","jim")

# 2、获取name对应的集合的所有成员: 返回值 : 集合
smembers(name)           'r.smembers(name)'

# 3、获取name对应的集合中的元素个数
scard(name)
r.scard("set_name")

# 4、检查value是否是name对应的集合内的元素:True|False
sismember(name, value)

# 5、随机删除并返回指定集合的一个元素
spop(name)

# 6、删除集合中的某个元素
srem(name, value)   'r.srem("set_name", "tom")'

# 7、获取多个name对应集合的交集
sinter(keys, *args)		'r.sinter("set_name","set_name1","set_name2") 输出为:｛b'b'｝''
						
# 8、给指定key(键)添加value(值)
r.sadd(key, value)  	'r.sadd("set_name","a","b")
						'r.sadd("set_name1","b","c")
						'r.sadd("set_name2","b","c","d")'

# 9、获取多个name对应的集合的并集
r.sunion(keys, *args)      'r.sunion("set_name","set_name1","set_name2")'

```

**python代码实现微博关注**

```python
import redis

r = redis.Redis(host='192.168.153.136',port=6379,db=0)

# 用户1关注的人
r.sadd('user_first','peiqi','qiaozhi','danni')
# 用户2关注的人
r.sadd('user_second','peiqi','qiaozhi','lingyang')

# user_first和user_second的共同关注的人为？？求差集
result = r.sinter('user_first','user_second')
# 把集合中的每个元素转为string数据类型
focus_on_set = set()
for r in result:
    focus_on_set.add(r.decode())

print(focus_on_set)
```



# **有序集合sortedset**

- 特点

```
1、有序、去重   
2、元素是字符串类型
3、每个元素都关联着一个浮点数分值(score)，并按照分值从小到大的顺序排列集合中的元素（分值可以相同）
4、最多包含2^32-1元素
```

- 示例

  **一个保存了水果价格的有序集合**

| 分值 | 2.0  | 4.0  | 6.0  | 8.0  | 10.0 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 元素 | 西瓜 | 葡萄 | 芒果 | 香蕉 | 苹果 |

​	**一个保存了员工薪水的有序集合**

| 分值 | 6000 | 8000 | 10000 | 12000 |      |
| ---- | ---- | ---- | ----- | ----- | ---- |
| 元素 | lucy | tom  | jim   | jack  |      |

​	**一个保存了正在阅读某些技术书的人数**

| 分值 | 300      | 400    | 555  | 666  | 777  |
| ---- | -------- | ------ | ---- | ---- | ---- |
| 元素 | 核心编程 | python | Java | c++  | c    |

### **有序集合基本命令**

```python
# 在有序集合中添加一个成员      [score : 分值][value : 值]
zadd key score value		
	'示 例 : 127.0.0.1:6379> zadd swn score(分值) value(元素) score(分值) value(元素) ... '

# 查看指定区间元素（升序)  	[withscores : 分值---查看指定区间是否也查看分值]
zrange key start stop [withscores]  '示例:127.0.0.1:6379> zrange suer 0 -1  withscores'
									'返回结果显示格式 : (value,分值,value,分值...)'
# 查看指定区间元素（降序） 		[withscores : 分值---查看指定区间是否也查看分值]
ZREVRANGE key start stop [withscores]  

# 查看指定元素的分值
ZSCORE key value

# 返回指定区间元素			 <----类似MySQL数据库的分页
		# [withscores：返回指定区间元素对应的分值]  
    	# [min :指定区间最小的值 max : 指定区间最大的值]
    	# [limit : 不可更改，隶属指令 limit  类似MySQL数据库的分页]
    	# [offset : 跳过元素的个数] [count : 获取元素的个数]
		# [小括号 : 开区间  zrangebyscore fruits (2.0 8.0]
zrangebyscore key min max [withscores] [limit offset count]
		'示 例 : 127.0.0.1:6379> ZRANGEBYSCORE key8 100 200 withscores limit 8 88 '
		'示 例 ：127.0.0.1:6379> zrangebyscore key8 200 400 limit 8 88 withscores'
# 删除成员
zrem key value

# 增加或者减少分值  [increment:指定值的分值增加或减少的数量] [value : 对应的值]
zincrby key increment value  '示例 :127.0.0.1:6379> zincrby key 8888 value'

# 返回元素排名 [value:对应的值]　
zrank key value

# 返回元素逆序(倒序)排名　[value:对应的值]　
zrevrank key value

# 删除指定区间内的元素　　[指定区间被删除的值　包括 min max]
zremrangebyscore key min max　　

# 返回集合中元素个数
zcard key

# 返回指定范围中元素的个数　[包括 min max]
zcount key min max

# 并集 
	# [destination　: 需要并集到指定的集合]
	# [numkeys : 指定并集 有序集合的数量]
    # [key : 有序集合---> 有序的集合数量　必须满足　numkeys指定的数量]
    # [weights 权重值(默认值为1) :依次给每个key一个权重值，权重值：需要key对应value(值)与权重值相乘]
    # 【先计算权重值再并集】
    # [AGGREGATE SUM|MIN|MAX　SUM:获取交集后求和　MIN:获取交集后最小的　MAX:获取交集后最大的]
zunionstore destination numkeys key [weights 权重值(默认为１)] [AGGREGATE SUM|MIN|MAX]
	"示例:zunionstore key3 2 key1 key2 weights 1 0.5 aggregate sum"
    "并集给key3,指定并集集合的数量2,指定数量为2的集合key1,key2,
    "weigets给key指定权重,key1给１：key乘以1,key给0.5:key乘以0.5
    "aggregate sun　求权重后的key1 和 key2 的和，放入key3中"

# 交集：和并集类似，只取相同的元素
	# [destination　: 需要并集到指定的集合]
	# [numkeys : 指定交集 有序集合的数量]
    # [key : 有序集合---> 有序的集合数量　必须满足　numkeys指定的数量]
    # [weights 权重值(默认值为1) :依次给每个key一个权重值，权重值：需要key对应value(值)与权重值相乘]
    # 【先计算权重值再交集】
    # [AGGREGATE SUM|MIN|MAX　SUM:获取交集后的求和　MIN:获取交集后最小的　MAX:获取交集后最大的]
ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX
```

#### **代码实现示例**

**示 例：查看: 指定索引区间元素（升序）zrange key start stop [withscores]**

```python
127.0.0.1:6379> ZRANGE salary 0 -1
1) "lucy"
2) "tom"
3) "jim"
4) "jack"
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "lucy"
2) "6000"
3) "tom"
4) "8000"
5) "jim"
6) "10000"
7) "jack"
8) "12000"
127.0.0.1:6379> 
```

**示　例：查看: 指定索引区间元素（降序）**

ZREVRANGE key start stop [withscores]

**示　例：显示指定元素的分值**

ZSCORE key member

```python
127.0.0.1:6379> zscore salary jack
"14000"
127.0.0.1:6379> 
```

**示　例：返回指定区间元素**

zrangebyscore key min max [withscores] [limit offset count]

offset : 跳过多少个元素

count : 返回几个

小括号 : 开区间  zrangebyscore fruits (2.0 8.0

```python
127.0.0.1:6379> ZRANGEBYSCORE salary (8000 12000
1) "jim"
2) "jack"
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "lucy"
2) "6000"
3) "tom"
4) "8000"
5) "jim"
6) "10000"
7) "jack"
8) "12000"
```

**示　例：删除**

zrem key member

```python
127.0.0.1:6379> ZREM salary jim
(integer) 1
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "lucy"
2) "6000"
3) "tom"
4) "8000"
5) "jack"
6) "12000"
127.0.0.1:6379> 
```

**示　例：增加或者减少分值**

zincrby key increment member

```python
127.0.0.1:6379> ZINCRBY salary 2000 jack
"14000"
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "lucy"
2) "6000"
3) "tom"
4) "8000"
5) "jack"
6) "14000"
127.0.0.1:6379> 
```

**示　例：返回元素的排名（索引）**

zrank key member

```python
127.0.0.1:6379> zrank salary jack
(integer) 2
127.0.0.1:6379> 
```

**示　例：返回元素逆序排名**

zrevrank key member

```python
127.0.0.1:6379> ZREVRANK salary jack
(integer) 0
127.0.0.1:6379> ZREVRANK salary lucy
(integer) 2
127.0.0.1:6379> 
```

**示　例：删除指定区间内的元素**

zremrangebyscore key min max

```python
127.0.0.1:6379> ZREMRANGEBYSCORE salary 4000 6000
(integer) 1
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "tom"
2) "8000"
3) "jack"
4) "14000"
127.0.0.1:6379> 
```

**示　例：返回集合中元素个数**

zcard key

```python
127.0.0.1:6379> ZCARD salary
(integer) 2
127.0.0.1:6379>
```

**示　例：返回指定范围中元素的个数**

zcount key min max

zcount fruits 4 7 

zcount fruits (4 7

```python
127.0.0.1:6379> ZRANGE salary 0 -1 withscores
1) "tom"
2) "8000"
3) "jack"
4) "14000"
127.0.0.1:6379> zcount salary 8000 14000
(integer) 2
# 不包含8000，包含14000
127.0.0.1:6379> zcount salary (8000 14000
(integer) 1
127.0.0.1:6379> 
```

**示　例：并集**

zunionstore destination numkeys key [weights ] [AGGREGATE SUM|MIN|MAX]

```python
127.0.0.1:6379> zadd stu_score1 60 tom 70 jim
(integer) 2
127.0.0.1:6379> zadd stu_score2 80 tom 90 lucy
(integer) 2
# 默认为SUM
127.0.0.1:6379> ZUNIONSTORE stu_score3 2 stu_score1 stu_score2
(integer) 3
127.0.0.1:6379> ZRANGE stu_score3 0 -1 withscores
1) "jim"
2) "70"
3) "lucy"
4) "90"
5) "tom"
6) "140"
127.0.0.1:6379> 
# WEIGHTS 和 AGGREGATE 
127.0.0.1:6379> ZRANGE stu_score1 0 -1 withscores
1) "tom"
2) "60"
3) "jim"
4) "70"
127.0.0.1:6379> ZRANGE stu_score2 0 -1 withscores
1) "tom"
2) "80"
3) "lucy"
4) "90"
# 权重1给stu_score1，权重0.5给stu_score2，算完权重之后求和SUM
127.0.0.1:6379> ZUNIONSTORE stu_score8 2 stu_score1 stu_score2 weights 1 0.5 AGGREGATE SUM
(integer) 3
127.0.0.1:6379> ZRANGE stu_score8 0 -1 withscores
1) "lucy"
2) "45"
3) "jim"
4) "70"
5) "tom"
6) "100"
127.0.0.1:6379> 
```

**示　例：交集**

ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX

和并集类似，只取相同的元素

### **python操作sorted set**

```python
import redis

r = redis.Redis(host='192.168.43.49',port=6379,password='123456',db=0)
# 注意第二个参数为字典
r.zadd('salary',{'tom':6000,'jim':8000,'jack':12000})

# 结果为列表中存放元组[(),(),()]
print(r.zrange('salary',0,-1,withscores=True))
print(r.zrevrange('salary',0,-1,withscores=True))

# start:起始值,num:显示条数
print(r.zrangebyscore('salary',6000,12000,start=1,num=2,withscores=True))

# 删除
r.zrem('salary','tom')
print(r.zrange('salary',0,-1,withscores=True))

# 增加分值
r.zincrby('salary',5000,'jack')
print(r.zrange('salary',0,-1,withscores=True))

# 返回元素排名
print(r.zrank('salary','jack'))
print(r.zrevrank('salary','jack'))

# 删除指定区间内的元素
r.zremrangebyscore('salary',6000,8000)
print(r.zrange('salary',0,-1,withscores=True))

# 统计元素个数
print(r.zcard('salary'))

# 返回指定范围内元素个数
print(r.zcount('salary',6000,20000))

# 并集
r.zadd('salary2',{'jack':17000,'lucy':8000})
r.zunionstore('salary3',('salary','salary2'),aggregate='max')
print(r.zrange('salary3',0,-1,withscores=True))

# 交集
r.zinterstore('salary4',('salary','salary2'),aggregate='max')
print(r.zrange('salary4',0,-1,withscores=True))
```

**案例1：网易音乐排行榜**

```python
1、每首歌的歌名作为元素（先不考虑重复）
2、每首歌的播放次数作为分值
3、使用ZREVRANGE来获取播放次数最多的歌曲
```

#### **代码实现示例**

```python
import redis

r = redis.Redis(host='192.168.43.49',port=6379,password='123456',db=0)

r.zadd('ranking',{'song1':1,'song2':1,'song3':1,'song4':1})
r.zadd('ranking',{'song5':1,'song6':1,'song7':1})
r.zadd('ranking',{'song8':1,'song9':1})

r.zincrby('ranking',50,'song3')
r.zincrby('ranking',60,'song5')
r.zincrby('ranking',80,'song7')
# 获取前10名
rlist = r.zrevrange('ranking',0,2,withscores=True)

i = 1
for r in rlist:
    print('第%d名:%s' % (i,r[0].decode()))
    i += 1
```

**案例2: 京东商品畅销榜**

```python
# 第1天
ZADD mobile-001 5000 'huawei' 4000 'oppo' 3000 'iphone'
# 第2天
ZADD mobile-002 5200 'huawei' 4300 'oppo' 3230 'iphone'
# 第3天
ZADD mobile-003 5500 'huawei' 4660 'oppo' 3580 'iphone'
问题：如何获取三款收集的销量排名？
ZUNIONSTORE mobile-001:003 mobile-001 mobile-002 mobile-003 # 可否？
# 正确
1、ZADD mobile-003 5500 'huawei' 4660 'oppo' 3580 'iphone'
2、ZUNIONSTORE mobile-001:003 mobile-001 mobile-002 mobile-003 AGGREGATE MAX
```

**python代码实现**

```python
import redis

r = redis.Redis(host='192.168.43.49',port=6379,password='123456',db=0)

# 第1天
day01_dict = {
    'huawei' : 5000,
    'oppo'   : 4000,
    'iphone' : 3000
}
# 第2天
day02_dict = {
    'huawei' : 5200,
    'oppo'   : 4300,
    'iphone' : 3230
}
# 第3天
day03_dict = {
    'huawei' : 5500,
    'oppo'   : 4660,
    'iphone' : 3580
}
r.zadd('mobile-day01',day01_dict)
r.zadd('mobile-day02',day02_dict)
r.zadd('mobile-day03',day03_dict)

r.zunionstore('mobile-day01:03',('mobile-day01','mobile-day02','mobile-day03'),aggregate='max')
rlist = r.zrevrange('mobile-day01:03',0,-1,withscores=True)

i = 1
for r in rlist:
    print('第{}名：{}'.format(i,r[0].decode()) )
```



















