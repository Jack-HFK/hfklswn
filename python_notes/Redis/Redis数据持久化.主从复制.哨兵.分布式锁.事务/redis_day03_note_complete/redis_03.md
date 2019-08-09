# 故情回顾

### **五大数据类型及应用场景**

| 类型       | 特点                                                         | 使用场景                                                     |
| :--------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| string     | 简单key-value类型，value可为字符串和数字                     | ==常规计数==（微博数, 粉丝数等功能）                         |
| hash       | 是一个string类型的field和value的映射表，hash特别适合用于存储对象 | ==存储部分可能需要变更的数据==（比如用户信息）               |
| list       | 有序可重复列表                                               | ==关注列表，粉丝列表，消息队列等==                           |
| set        | 无序不可重复列表                                             | ==存储并计算关系==（如微博，关注人或粉丝存放在集合，可通过交集、并集、差集等操作实现如共同关注、共同喜好等功能） |
| sorted set | 每个元素带有分值的集合                                       | ==各种排行榜(首选有序集合sorted set)==                       |

### **位图操作（bitmap）**

```python
# 应用场景
1、可以实时的进行数据统计（网站用户的上线次数统计,活跃度的统计）
# 常用命令
1、setbit key offset value
2、BITCOUNT key
```

### **哈希（散列）类型**

```python
# 应用场景
1、很适合存储对象类型，比如说用户ID作为key，用户的所有属性及值作为key对应的value
（用户维度统计-各种数据统计-发帖数、粉丝数等）
# 常用命令
HSET key field value
HSETNX key field value
HMSET key field value field value

HGET key field
HMGET key field filed
HGETALL key
HKEYS key
HVALS key

HLEN key
HEXISTS key field

HINCRBY key filed increment
HINCRBYFLOAT key field increment

HDEL key field 
```

### **集合类型**

```python
# 应用场景
1、共同关注、共同好友
# 常用命令

SADD key member1 member2

SMEMBERS key
SCARD key

SREM key member1 member2
SRANDMEMBER key [count]

SISMEMBER key member

SDIFF key1 key2 
SDIFFSTORE destination key1 key2

SINTER key1 key2
SINTERSTORE destination key1 key2

SUNION key1 key2
SUNIONSTORE destination key1 key2
```

### **有序集合**

```python
# 应用场景
1、各种排行榜
   1、游戏：列出前100名高分选手
   2、列出某用户当前的全球排名
   3、各种日排行榜、周排行榜、月排行榜
# 常用命令
zadd key score member

ZRANGE key start stop [withscores]
ZREVRANGE key start stop [withscores]
ZRANGEBYSCORE key min max [withscores] [limit offset count]
ZSCORE key member
ZCOUNT key min max
ZCARD key

ZRANK key member
ZREVRANK key member

ZINCRBY key increment member

ZREM key member
ZREMRANGEBYSCORE key min max

zunionstore destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]
ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX
```

------

------

# 有序集合sortedset

**有序集合的交集与并集**

```python
# 交集（weights代表权重值，aggregate代表聚合方式 - 先计算权重值，然后再聚合）
ZINTERSTORE destination numkeys key1 key2 WEIGHTS weight AGGREGATE SUM|MIN|MAX
# 并集（weights代表权重值，aggregate代表聚合方式 - 先计算权重值，然后再聚合）
ZUNIONSTORE destination numkeys key [weights 权重值] [AGGREGATE SUM|MIN|MAX]
```

**案例1：网易音乐排行榜**

```python
1、每首歌的歌名作为元素
2、每首歌的播放次数作为分值
3、使用ZREVRANGE来获取播放次数最多的歌曲
```

**代码实现**

```python
import redis

r = redis.Redis(host='192.168.153.136',port=6379,db=0)

r.zadd('ranking',{'song1':1,'song2':1,'song3':1,'song4':1})
r.zadd('ranking',{'song5':1,'song6':1,'song7':1})
r.zadd('ranking',{'song8':1,'song9':1})

r.zincrby('ranking',50,'song3')
r.zincrby('ranking',60,'song5')
r.zincrby('ranking',80,'song7')
# 获取前3名
rlist = r.zrevrange('ranking',0,2,withscores=True)

i = 1
for r in rlist:
    print('第%d名:%s 播放次数: %s' % (i,r[0].decode(),int(r[1])))
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
问题：如何获取三款手机的销量排名？
ZUNIONSTORE mobile-001:003 mobile-001 mobile-002 mobile-003 # 可否？
# 正确
1、ZREVRANGE mobile-003 0 -1 withscores
2、ZUNIONSTORE mobile-001:003 3 mobile-001 mobile-002 mobile-003 AGGREGATE MAX
```

**python代码实现**

```python
import redis

r = redis.Redis(host='192.168.153.136',port=6379,db=0)

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
print(rlist)

i = 1
for r in rlist:
    print('第{}名：{}-{}'.format(i,r[0].decode(),int(r[1])))
    i += 1
```

# **==数据持久化==**

**持久化定义**

```python
1.将数据从掉电易失的内存放到永久存储的设备上。
2.Redis缓存性数据库，将在内存中的数据保存到可以永久保存的存储设备中。
3.主要应用是将内存中的对象存储在数据库中，或者存储在磁盘文件中、数据文件中、等等。
```

**为什么需要持久化**

```python
1.因为Redis所有的数据都在内存上，所以必须得做数据持久化。
2.因为数据都是缓存在内存中的，当你重启系统或者关闭系统，缓存在内存中的数据就会消失殆尽，再也找不回来。
  所以，为了数据长期保存，需要将Redis放在内存的数据做持久化存储。
```

## RDB 模 式

**定 义 :**    **纯备份数据**

​			**RDB模式 : 将存在的数据真实的存储备份保存，实现数据持久化**

​		    **RDB模式为系统默认模式，默认为开启状态。**	

​	**数据持久化分类之 - RDB模式（默认开启）**

```python
1、保存真实的数据
2、将服务器包含的所有数据库数据以二进制文件的形式保存到硬盘里面
3、默认文件名所在路径 ：/var/lib/redis/dump.rdb
```

#### **创建rdb文件的两种方式**

#### RDB手动保存方式

**方式一：**服务器执行客户端发送的 SAVE命令 或者 BGSAVE 命令

**原 理：**

​		客户端执行连接后手动执行SAVE命令 或者 BGSAVE 命令后，服务器将执行一次：把Redis数据库存储在内存		中的数据备份到数据库或者磁盘。

**手 动 数 据 备 份 语 法:**

```python
客户端连接Redis数据库后：
方法一：
	 SAVE       '此命令阻塞Redis服务器'
方法二：
	 BGSAVE		'服务器创建子进程执行此方法，不阻塞服务器'
```

**SAVE和BGSAVE方法详解：**

```python
'SAVE 方 法 :
127.0.0.1:6379> SAVE
OK
# 特点
1、执行SAVE命令过程中，redis服务器将被阻塞，Redis服务器无法处理客户端发送的命令请求，在SAVE命令执行完毕后，服务器才会重新开始处理客户端发送的命令请求
2、如果RDB文件已经存在，那么服务器将自动使用新的RDB文件代替旧的RDB文件
# 工作中定时持久化保存一个文件

'BGSAVE 方 法 :
127.0.0.1:6379> BGSAVE
Background saving started
# 执行过程如下
1、客户端 发送 BGSAVE 给服务器
2、服务器马上返回 Background saving started 给客户端
3、服务器 fork() 子进程做这件事情
4、服务器继续提供服务
5、子进程创建完RDB文件后再告知Redis服务器

# 配置文件相关操作  '防止配置文件出错更改前先备份:指令: cp redis.conf redis.conf.bak'
				'cat redis.conf > /home/tarena/a.txt'
/etc/redis/redis.conf
263行: dir /var/lib/redis # 表示rdb文件存放路径
253行: dbfilename dump.rdb  # 文件名
    	详细步骤如下:
    	1.tarena@tarena:~$ sudo -i   <-----主目录下输入
		2.[sudo] tarena 的密码： 		<-----输入密码
		3.root@tarena:~# cd /etc/redis/  <----进入目标目录下
		4.root@tarena:/etc/redis# cat redis.conf > /home/tarena/redis_conf.txt  <--备份文件
		5.root@tarena:cd /home/tarena/目录下
        6.root@tarena:vi redis_conf.txt  <---打开备份文件
        7.Shift键 + :键    <---进入文件编写模式
        8.set nu 			<----输入此指令表示显示行数
                
# 两个命令比较
SAVE比BGSAVE快，因为需要创建子进程，消耗额外的内存

# 补充：可以通过查看日志文件来查看redis都做了哪些操作

# 日志文件：配置文件中搜索 logfile
logfile位置 /var/log/redis/redis-server.log  
打开文件: 'vi /var/log/redis/redis-server.log' 
查看文件后二十行日志 tail -20 /var/log/redis/redis-server.log 
查看文件前二十行日志 tail 20 /var/log/redis/redis-server.log 
```

#### RDB自动保存方式

**方式二：设置配置文件条件满足时自动保存（使用最多）**

**RDB自动保存方式为Redis数据库默认方式，配置文件中默认为开启状态**

```python
# 命令行示例
redis>save 300 10
  　　	表示如果距离上一次创建RDB文件已经过去了300秒，并且服务器的所有数据库总共已经发生了不少于10次修			　改，那么自动执行BGSAVE命令，两个条件都满足自动执行bgsave自动备份数据
redis>save 60 10000
  		　表示如果距离上一次创建rdb文件已经过去60秒，并且服务器所有数据库总共已经发生了不少于10000次			　修改，那么执行bgsave命令 ，两个条件都满足自动执行bgsave自动备份数据

# redis配置文件默认（属于完全备份）
218行: save 900 1
219行: save 300 10
220行: save 60 10000
  1、只要三个条件中的任意一个被满足时，服务器就会自动执行BGSAVE命令,自动备份数据
  2、每次创建RDB文件之后，服务器为实现自动持久化而设置的时间计数器和次数计数器就会被清零，并重新开始计数，所以多个保存条件的效果不会叠加
```

## AOF 模 式

**数据持久化分类之 - AOF（AppendOnlyFile，默认未开启）**

**特点** 			**存储Redis的指令**

```python
1、存储的是命令，而不是真实数据
2、默认不开启
# 开启方式（修改配置文件）
1、/etc/redis/redis.conf
  672行: appendonly yes # 把 no 改为 yes
  676行: appendfilename "appendonly.aof"
2、重启服务
  sudo /etc/init.d/redis-server restart
```

**RDB缺点**

```python
1、创建RDB文件需要将服务器所有的数据库的数据都保存起来，这是一个非常消耗资源和时间的操作，所以服务器需要隔一段时间才创建一个新的RDB文件，也就是说，创建RDB文件不能执行的过于频繁，否则会严重影响服务器的性能
2、可能丢失数据(丢失可能性大)
```

#### **AOF持久化原理及优点**

```python
# 原理
   1、每当有修改数据库的命令被执行时，服务器就会将执行的命令写入到AOF文件的末尾
   2、因为AOF文件里面存储了服务器执行过的所有数据库修改的命令，所以给定一个AOF文件，服务器只要重新执行一遍AOF文件里面包含的所有命令，就可以达到还原数据库的目的

# 优点
  用户可以根据自己的需要对AOF持久化进行调整，让Redis在遭遇意外停机时不丢失任何数据，或者只丢失一秒钟的数据，这比RDB持久化丢失的数据要少的多
```

**安全性问题考虑**

```python
# 因为
  虽然服务器执行一个修改数据库的命令，就会把执行的命令写入到AOF文件，但这并不意味着AOF文件持久化不会丢失任何数据，在目前常见的操作系统中，执行系统调用write函数，将一些内容写入到某个文件里面时，为了提高效率，系统通常不会直接将内容写入硬盘里面，而是将内容放入一个内存缓存区（buffer）里面，等到缓冲区被填满时才将存储在缓冲区里面的内容真正写入到硬盘里

# 所以
  1、AOF持久化：当一条命令真正的被写入到硬盘里面时，这条命令才不会因为停机而意外丢失
  2、AOF持久化在遭遇停机时丢失命令的数量，取决于命令被写入到硬盘的时间
  3、越早将命令写入到硬盘，发生意外停机时丢失的数据就越少，反之亦然
```

#### Redis相关文件存放路径

```
/etc/下 存放配置文件
/etc/init.d/下 存放服务启动文件
```

| Redis数据库文件所在位置 | 文件地址                        |
| ----------------------- | ------------------------------- |
| 配置文件                | /etc/redis/redis.conf           |
| 备份文件                | /var/lib/redis/*.rdb\|*.aof     |
| 日志文件                | /var/log/redis/redis-server.log |
| 启动文件                | /etc/init.d/redis-server        |

#### **策略 - 配置文件**

```python
# 打开配置文件:vi /etc/redis/redis.conf，找到相关策略如下
1、701行: appendfsync always # [alwarys]
   服务器每写入一条命令，就将缓冲区里面的命令写入到硬盘里面，服务器就算意外停机，也不会丢失任何已经成功执行的命令数据
2、702行: appendfsync everysec # [everysec（默认）]
   服务器每一秒将缓冲区里面的命令写入到硬盘里面，这种模式下，服务器即使遭遇意外停机，最多只丢失1秒的数据
3、703行: appendfsync no # [no]
   服务器不主动将命令写入硬盘,由操作系统决定何时将缓冲区里面的命令写入到硬盘里面，丢失命令数量不确定

# 运行速度比较
always：速度慢
everysec和no都很快，默认值为everysec
```

#### AOF冗余命令处理

**AOF文件中是否会产生很多的冗余命令？**

```python
为了让AOF文件的大小控制在合理范围，避免胡乱增长，Redis提供了AOF重写功能，通过这个功能，服务器可以产生一个新的AOF文件
  -- 新的AOF文件记录的数据库数据和原由的AOF文件记录的数据库数据完全一样
  -- 新的AOF文件会使用尽可能少的命令来记录数据库数据，因此新的AOF文件的体积通常会小很多
  -- AOF重写期间，服务器不会被阻塞，可以正常处理客户端发送的命令请求
```

示例

| 原有AOF文件                | 重写后的AOF文件                         |
| -------------------------- | --------------------------------------- |
| select 0                   | SELECT 0                                |
| sadd myset peiqi           | SADD myset peiqi qiaozhi danni lingyang |
| sadd myset qiaozhi         | SET msg 'hello tarena'                  |
| sadd myset danni           | RPUSH mylist 2 3 5                      |
| sadd myset lingyang        |                                         |
| INCR number                |                                         |
| INCR number                |                                         |
| DEL number                 |                                         |
| SET message 'hello world'  |                                         |
| SET message 'hello tarena' |                                         |
| RPUSH mylist 1 2 3         |                                         |
| RPUSH mylist 5             |                                         |
| LPOP mylist                |                                         |

#### **AOF文件重写方法触发**

```python
1、客户端向服务器发送BGREWRITEAOF命令
   127.0.0.1:6379> BGREWRITEAOF
   Background append only file rewriting started

2、修改配置文件让服务器自动执行BGREWRITEAOF命令
 '默认如下：
  auto-aof-rewrite-percentage 100
  auto-aof-rewrite-min-size 64mb <--文件达到64M时执行一次重写,下次执行重写,文件量是上一次的一倍128M
  # 解释
    1、只有当AOF文件的增量大于100%时才进行重写，也就是大一倍的时候才触发
        # 第一次重写新增：64M
        # 第二次重写新增：128M
        # 第三次重写新增：256M（新增128M）
```



#### **RDB和AOF持久化对比**

| RDB持久化                                                    | AOF持久化                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 全量备份，一次保存整个数据库                                 | 增量备份，一次保存一个修改数据库的命令                       |
| 保存的间隔较长                                               | 保存的间隔默认为一秒钟                                       |
| 数据还原速度快                                               | 数据还原速度一般，冗余命令多，还原速度慢                     |
| 执行SAVE命令时会阻塞服务器，但手动或者自动触发的BGSAVE不会阻塞服务器 | 无论是平时还是进行AOF重写时，都不会阻塞服务器                |
| 更适合数据备份                                               | 更适合用来保存数据，通常意义上的数据持久化，在appendfsync always模式下运行 |

```python
# 用redis用来存储真正数据，每一条都不能丢失，都要用always，有的做缓存，有的保存真数据，我可以开多个redis服务，不同业务使用不同的持久化。
'新浪每个服务器上有4个redis服务，整个业务中有上千个redis服务，分不同的业务，每个持久化的级别都是不一样的。
```

**数据恢复(无需手动操作)**

```python
1.既有dump.rdb,又有appendonly.aof。
2.恢复数据时先找appendonly.aof
```

#### **配置文件常用配置总结**

```python
# 设置密码
1、requirepass password

# 开启远程连接
1.注释掉 bind 127.0.0.1 ::1
2.protected-mode yes|no  yes改为no允许远程连接

# rdb持久化-默认配置
1、dir /var/lib/redis
2、dbfilename dump.rdb

# rdb持久化-自动触发
save 900 1
save 300 10
save 60 10000

# aof持久化开启-默认配置
appendonly yes
appendfilename "appendonly.aof"

# aof持久化策略
appendfsync alwarys
appendfsync everysec # 默认配置
appendfsync no

# aof重写触发
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
```

# **==Redis主从复制==**

**定 义**

```python
master:主服务器	 					slaves:从服务器
1、一个Redis服务可以有多个该服务的复制品，这个Redis服务成为master，其他复制品成为slaves
2、master会一直将自己的数据更新同步给slaves，保持主从同步
3、只有master可以执行写命令，slave只能执行读命令
```

**作 用**

```python
slave从服务器 分担了读的压力（高并发）
```

**原 理**

```python
从服务器执行客户端发送的读命令，比如GET、LRANGE、SMEMMBERS、HGET、ZRANGE等等，客户端可以连接slaves执行读请求，来降低master的读压力
```

**两种实现方式**

### Linux终端设置主从服务器

**方式一**（Linux终端命令行实现主从复制）

**语 法 :**

```python
步骤一 ： 
	# 终端命令设置此服务器为从服务，并指定主服务
	redis-server --port 从端口号 --slaveof 127.0.0.1 主端口号
步骤二 :
    # 客户端连接从服务器的端口号
    redis-cli -h IP地址 -p 从端口  或者 redis-cli -p 从端口号
```

**示 例：**

```python
# 从服务端------->6300为从服务器 ----6300是6379的从服务器-----> 6379为主服务器
redis-server --port 6300 --slaveof 127.0.0.1 6379   
# 从客户端---->主从同步：此从客户端连接 端口号为6300的从服务器
redis-cli -p 6300     

'测 试 ：
# 执行 127.0.0.1:6300> keys * 测试是否数据同步
# 测试结果 发现是复制了原6379端口的redis中数据
127.0.0.1:6380> set mykey 123
(error) READONLY You can't write against a read only slave.
127.0.0.1:6380> 
# 从服务器只能读数据，不能写数据
```

### **Redis命令行中设置主从服务器**

​	**方式一**（Redis命令行实现2）

**语 法：**

```python
步骤一:
	# Redis命令行中切换为从服务器
	slaveof IP地址 从post端口号 
步骤二:
    # Redis命令行中切换为主服务器
    slaveof no one
```

```python
# 服务端启动
redis-server --port 6301
# 客户端连接
tarena@tedu:~$ redis-cli -p 6301
127.0.0.1:6301> keys *
1) "myset"
2) "mylist"
127.0.0.1:6301> set mykey 123
OK
# 切换为从
127.0.0.1:6301> slaveof 127.0.0.1 6379
OK
127.0.0.1:6301> set newkey 456
(error) READONLY You can't write against a read only slave.
127.0.0.1:6301> keys *
1) "myset"
2) "mylist"
# 再切换为主
127.0.0.1:6301> slaveof no one
OK
127.0.0.1:6301> set name hello
OK
```

### **本机服务器修改配置文件设置为主从服务器**

**方式二**(修改配置文件)

**语 法 ：**

```python
#每个redis服务器都有一个和他对应的配置文件 

# 需要本服务器为从服务器时：需要修改配置文件
1.创建配置文件 vi redis_6300.conf
2.文件中添加   slaveof 127.0.0.1 6379 	表示此服务器为从服务器，是主服务器为6379的从服务器。
3.文件中添加   port 6300    			 	表示此从服务器的端口
4.此配置文件只添加以上两句代码。

# 启动redis从服务器
redis-server redis_6300.conf   使用用创建的redis_6300.conf文件启动此从服务器

# 客户端连接从服务器测试
redis-cli -p 6300
127.0.0.1:6300> hset user:1 username guods
(error) READONLY You can't write against a read only slave.
```

# **==切换Master主服务器==**

### **手动切换服务器为Master主服务器**

```python
1、一个Master可以有多个Slaves
2、Slave下线，只是读请求的处理性能下降
3、Master下线，写请求无法执行
4、其中一台Slave使用SLAVEOF no one命令成为Master，其他Slaves执行SLAVEOF命令指向这个新的Master，从它这里同步数据
# 以上过程是手动的，能够实现自动，这就需要Sentine哨兵，实现故障转移Failover操作
```

**手动实现方法：**

```python
1、启动端口6400redis，设置为6379的slave
   redis-server --port 6400
   redis-cli -p 6400
   redis>slaveof 127.0.0.1 6379
2、启动端口6401redis，设置为6379的slave
   redis-server --port 6401
   redis-cli -p 6401
   redis>slaveof 127.0.0.1 6379
3、关闭6379redis
   sudo /etc/init.d/redis-server stop
4、把6400redis设置为master
   redis-cli -p 6401
   redis>slaveof no one
5、把6401的redis设置为6400redis的salve
   redis-cli -p 6401
   redis>slaveof 127.0.0.1 6400
# 这是手动操作，效率低，而且需要时间，有没有自动的？？？
```

### **==官方高可用方案哨兵Sentinel==**

**Redis之哨兵 - sentinel**

```python
1、Sentinel会不断检查Master和Slaves是否正常
2、每一个Sentinel可以监控任意多个Master和该Master下的Slaves
```

**案例演示**

**环境搭建**

```python
# 共3台redis的服务器，如果是不同机器端口号可以是一样的
1、启动6379的redis服务器
   	sudo /etc/init.d/redis-server start
2、启动6380的redis服务器，设置为6379的从
    redis-server --port 6380
    tarena@tedu:~$ redis-cli -p 6380
    127.0.0.1:6380> slaveof 127.0.0.1 6379
    OK
3、启动6381的redis服务器，设置为6379的从
   	redis-server --port 6381
   	tarena@tedu:~$ redis-cli -p 6381
   	127.0.0.1:6381> slaveof 127.0.0.1 6379
```

#### 安装并搭建sentinel哨兵

```python
步骤一：
	# 1、安装redis-sentinel
	sudo apt install redis-sentinel
		'安装验证：sudo /etc/init.d/redis-sentinel start(启动)|stop(停止)
 
步骤二：
	# 2、新建配置文件sentinel.conf		
	文件中添加　	port 26379			# 投票机制：票数：监控主服务器的哨兵数量，设置为奇数 
	文件中添加　  Sentinel monitor tedu IP地址 监控端口号 投票票数
									'示例：Sentinel monitor tedu 127.0.0.1 8888 1
步骤三：
	# 3、启动sentinel
	方式一: redis-sentinel sentinel.conf
	方式二: redis-server sentinel.conf --sentinel

'测 试 :
	  # 将主服务器master的redis服务终止，查看从是否会提升为主
	1.sudo /etc/init.d/redis-server stop
	  # 发现提升　从服务器端口号　为master主服务器，其他从服务器依旧为从
      # 在新的主服务器上设置新值，在主从服务器中测试查看　步骤如下：
							　　'新的主服务器： 127.0.0.1:主端口号> set name 测试码
							　　	　　　　　　 'OK
								   '从服务器： 127.0.0.1:从端口号> get name 
                    						 '测试码
# 启动旧的主服务器6379，观察日志，发现变为了新的主服务器的从
主从+哨兵基本就够用了
```

**sentinel.conf解释**

```python
# sentinel监听端口，默认是26379，可以修改
port 26379
# 告诉sentinel去监听地址为ip:port的一个master，这里的master-name可以自定义，quorum是一个数字，指明当有多少个sentinel认为一个master失效时，master才算真正失效
sentinel monitor <master-name> <ip> <redis-port> <quorum>
```

#### 公司生产环境中设置哨兵sentinel

```python
步骤一：
	# 1.安装哨兵sentinel
    sudo apt-get install redis-sentinel
步骤二：
	# 2.创建配置文件：sentinel.conf
    文件中添加：　port 26379
    文件中添加：　Sentinel monitor 名字 IP地址 Port端口号 投票票数
    							'示例：Sentinel monitor tedu 127.0.0.1 8888 1
步骤三:
   	# 3.启动sentinel服务
	方式一: redis-sentinel sentinel.conf
	方式二: redis-server sentinel.conf --sentinel
```

# **==分布式锁==**

**高并发产生的问题？**

```python
1、购票: 多个用户抢到同一张票？
2、购物: 库存只剩1个,被多个用户成功买到？
... ...
```

**怎么办？**

```python
在不同进程需要互斥地访问共享资源时，分布式锁是一种非常有用的技术手段
```

**原理**

```python
1、多个客户端先到redis数据库中获取一把锁,得到锁的用户才可以操作数据库
2、此用户操作完成后释放锁，下一个成功获取锁的用户再继续操作数据库
```

#### 分布式锁实现原理

**语 法:**

```python
set key value nx ex 3
```

**注 意:**

```python
'从redis2.8版本开始，set命令集成了两个参数，nx和ex，先拿nx来争抢锁，抢到之后，再用ex参数给锁加一个过期时间防止锁忘记了释放，造成死锁
```

**思考**

```python
# MySQL中不是有写锁吗？当执行update命令时会自动加写锁,为什么还会出现多个进程去执行+1操作时造成结果的不确定性？
```

![](/home/tarena/hfk_python/python_notes/Redis/辅助图片/╖╓▓╝╩╜╦°.png)

## **博客项目解决高并发问题**

1、在数据库中创建库 blog，指定字符编码utf8

```mysql
mysql -uroot -p123456
mysql>create database blog charset utf8;
```

2、同步数据库，并在user_profile中插入表记录

```python
# 同步数据库
1、python3 manage.py makemigrations
2、python3 manage.py migrate
# 插入一条表数据
3、insert into user_profile values ('guoxiaonao','guoxiaonao','guoxiaonao@tedu.cn','123456','aaaaaaaa','bbbbbbbb','cccccccc');
```

3、启动django项目，并找到django路由测试 test函数

```python
1、python3 manage.py runserver
2、查看项目的 urls.py 路由，打开firefox浏览器输入地址：http://127.0.0.1:8000/test
# 返回结果：	HI HI HI 
```

4、在数据库表中创建测试字段score

```python
1、user/models.py添加:
   score = models.IntegerField(verbose_name=u'分数',null=True,default=0)
2、同步到数据库
   python3 manage.py makemigrations user
   python3 manage.py migrate user
3、到数据库中确认查看
```

3、在blog/views.py中补充 test函数，对数据库中score字段进行 +1 操作

```python
from user.models import UserProfile
def test(request):
    # return JsonResponse('HI HI HI')

    u = UserProfile.objects.get(username='guoxiaonao')
    u.score += 1
    u.save()

    return JsonResponse({'msg': 'test is ok'})
```

4、启多个服务端，模拟30个并发请求

(1)多台服务器启动项目

```python
python3 manage.py runserver 127.0.0.1:8000
python3 manage.py runserver 127.0.0.1:8001
```

(2)在tools中新建py文件 test_api.py，模拟30个并发请求

```python
import threading
import requests
import random


def getRequest():
    url='http://127.0.0.1:8000/test'
    url2='http://127.0.0.1:8001/test'
    get_url = random.choice([url, url2])
    requests.get(get_url)

ts = []
for i in range(30):

    t=threading.Thread(target=getRequest,args=())
    ts.append(t)

if __name__ == '__main__':

    for t in ts:
        t.start()

    for t in ts:
        t.join()
```

  (3) python3 test_api.py

 (4) 在数据库中查看 score 字段的值

```python
并没有+30，而且没有规律，每次加的次数都不同，如何解决？？？
```

**解决方案：redis分布式锁**

```python
def test(request):
	# 解决方法二:redis分布式锁
    import redis
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    while True:
        try:
            with r.lock('guoxiaonao', blocking_timeout=3) as lock:
                u = UserProfile.objects.get(username='guoxiaonao')
                u.score += 1
                u.save()
            break
        except Exception as e:
            print('lock is failed')
    
    return HttpResponse('HI HI HI')
```

# **==Redis事务==**

**定义：**

​		Redis事务可以一次执行多个命令，本质上是一组命令的集合，Redis事务提供了一种“将多个命令打包， 然后一次性、按顺序地执行”的机制， 并且事务在执行的期间不会主动中断--->等到服务器在执行完事务中的所有命令之后， 才会继续处理其他客户端的其他命令。

**特点**

```python
Redis 事务可以一次执行多个命令,并且带有以下三个重要的保证：
1.批量操作在发送 EXEC 命令前被放入队列缓存

2. 单独的隔离操作：事务中的所有命令会被序列化、按顺序执行，在执行的过程中：
　　不会被其他客户端发送来的命令打断，其他客户端提交的命令请求不会插入到事务执行命令序列中。

3. 不保证原子性：redis中的一个事务中如果存在命令执行失败，那么其他命令依然会被执行，没有回滚机制
```

#### **事 务 命 令 语 法**

```python
1、MULTI  # 开启事务
2、命令1  # 执行命令
3、命令2 ... ...
4、EXEC  # 提交到数据库执行
4、DISCARD # 取消事务
```

**一个事务从开始到执行会经历以下三个阶段：**

- 开始事务。
- 命令入队。
- 执行事务。

**使用步骤**

```python
# 开启事务
127.0.0.1:6379> MULTI
OK
# 命令1入队列
127.0.0.1:6379> INCR n1
QUEUED
# 命令2入队列
127.0.0.1:6379> INCR n2
QUEUED
# 提交到数据库执行
127.0.0.1:6379> EXEC
1) (integer) 1
2) (integer) 1
```

**事务中命令错误处理**

```python
# 1、命令语法错误，命令入队失败，直接自动discard退出这个事务
  这个在命令在执行调用之前会发生错误。例如，这个命令可能有语法错误（错误的参数数量，错误的命令名）

  处理方案：客户端发生了第一个错误情况，在exec执行之前发生的。通过检查队列命令返回值:如果这个命令回答这个队列的命令是正确的，否则redis会返回一个错误。如果那里发生了一个队列命令错误，大部分客户端将会退出并丢弃这个事务。

# 2、命令语法没错，但类型操作有误，则事务执行调用之后失败，无法进行事务回滚
   从我们施行了一个由于错误的value的key操作（例如对着String类型的value施行了List命令操作）
   
	处理方案：发生在EXEC之后的是没有特殊方式去处理的：即使某些命令在事务中失败，所有的其他命令都将会被执行。
    
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379> set num 10
QUEUED
127.0.0.1:6379> LPOP num
QUEUED
127.0.0.1:6379> exec
1) OK
2) (error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> get num
"10"
127.0.0.1:6379> 
```

**为什么redis不支持事务回滚**

- 观点

```python
1、Redis的内部极其简单和快速，来源于它不需要回滚功能
2、在生产环境中，通常回滚并不能解决来自编程的错误。举个例子，你本来想+1，却+2了，又或者+在错误的类型上,回滚并不能解决。由于无法提供一个避免程序员自己的错误，而这种错误在产品中并不会出现，所以选择一个简单和快速的方法去支持事务
```

# **pipeline补充**

#### **python使用pipeline()与execute()批量进行批量操作**

示例

```python
import redis

# 创建连接池并连接到redis
pool = redis.ConnectionPool(host = '192.168.153.130',db=0,port=6379)
r = redis.Redis(connection_pool=pool)

# 第一组
pipe = r.pipeline()
pipe.set('fans',50)
pipe.incr('fans')
pipe.incrby('fans',100)
pipe.execute()

# 第二组
pipe.get('fans')
pipe.get('pwd')
# [b'151', b'123']
result = pipe.execute()
print(result)
```

# 

















