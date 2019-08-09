MySQL数据库
==========================

| Tedu Python 教学部 |
| --- |
| Author：吕泽|
| Days：2天|

-----------

[TOC]

------

------



## 数据库概述

### 数据存储阶段 

【1】 人工管理阶段

缺点 ：  数据无法共享,不能单独保持,数据存储量有限

【2】 文件管理阶段 （.txt  .doc  .xls）
    
优点 ： 数据可以长期保存,可以存储大量的数据,使用简单

缺点 ：  数据一致性差,数据查找修改不方便,数据冗余度可能比较大

【3】数据库管理阶段

优点 ： 数据组织结构化降低了冗余度,提高了增删改查的效率,容易扩展,方便程序调用，做自动化处理

缺点 ：需要使用sql 或者 其他特定的语句，相对比较复杂

### 数据库应用

>融机构、游戏网站、购物网站、论坛网站 ... ... 
>
>![1562566513172](/home/tarena/.config/Typora/typora-user-images/1562566513172.png)

![](img/数据库系统.png)

### 基础概念

>数据 ： 能够输入到计算机中并被识别处理的信息集合

>数据结构 ：研究一个数据集合中数据之间关系的

>数据库 ： 按照数据结构，存储管理数据的仓库。数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合。

>数据库管理系统 ：管理数据库的软件，用于建立和维护数据库

>数据库系统 ： 由数据库和数据库管理系统，开发工具等组成的集合 


### 数据库分类和常见数据库

* 关系型数据库和非关系型数据库
      
>关系型： 采用关系模型（二维表）来组织数据结构的数据库 

>非关系型： 不采用关系模型组织数据结构的数据库

* 开源数据库和非开源数据库

> 开源：MySQL(重点)、SQLite、MongoDB

> 非开源：Oracle(重点)、DB2、SQL_Server

* 常见的关系型数据库
  
> MySQL、Oracle、SQL_Server、DB2 SQLite  


### 认识关系型数据库和MySQL

1. 数据库结构 （图库结构）

>数据元素 --> 记录 -->数据表 --> 数据库
>
>![1562566556238](/home/tarena/.config/Typora/typora-user-images/1562566556238.png)

![](img/库结构.png)

2. 数据库概念解析

>数据表 ： 存放数据的表格 

>字段： 每个列，用来表示该列数据的含义

>记录： 每个行，表示一组完整的数据
>
>![1562566571740](/home/tarena/.config/Typora/typora-user-images/1562566571740.png)

![](img/表结构.png)

3. MySQL特点

* 是开源数据库，使用C和C++编写 
* 能够工作在众多不同的平台上
* 提供了用于C、C++、Python、Java、Perl、PHP、Ruby众多语言的API
* 存储结构优良，运行速度快
* 功能全面丰富

4. MySQL安装

>Ubuntu安装MySQL服务
>>安装服务端: sudo apt-get install mysql-server
>>安装客户端: sudo apt-get install mysql-client
>>> 配置文件：/etc/mysql
>>> 命令集： /usr/bin
>>> 数据库存储目录 (存储位置)：/var/lib/mysql

>Windows安装MySQL
>>下载MySQL安装包(windows)  https://dev.mysql.com/downloads/mysql/
  mysql-installer***5.7.***.msi
>>安装教程去安装

5. 启动和连接MySQL服务

>服务端启动
>>查看MySQL状态: sudo /etc/init.d/mysql status
>>
>>启动服务：sudo /etc/init.d/mysql start(启动服务) | stop(停止服务) | restart(重启服务)
>>
>>启动服务 方法二：sudo service mysql start(启动服务) | stop(停止服务) | restart(重启服务)

>客户端连接   ：Navicat for MySQL （重点：数据库第三方可视化工具:简化操作：企业商用）
>>命令格式 
>>>mysql -h主机地址 -u用户名 -p密码 (某个数据库)					 :可直接进入某个具体库
>>>mysql -hlocalhost -uroot -p123456
>>>本地连接可省略 -h 选项: mysql -uroot -p123456

>关闭连接
>> ctrl-D
>> exit


### SQL语句

> 什么是SQL
>
> >结构化查询语言(Structured Query Language)，一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。
> >
> >**SQL文件中注释方法**
> >
> >```sql
> >单行注释: --空格 注释内容
> >多行注释:  /* 多行注销 */
> >```

### SQL指令文件的调用

> 功能作用：SQL指令文件内的代码命令全部执行一遍
>
> ```
>source sql文件（文件地址） ：编写sql语句文件，复制到终端执行sql文件语句，省略终端输入.
> ```
> 
> SQL语句使用特点
>
> * SQL语言基本上独立于数据库本身
>* 各种不同的数据库对SQL语言的支持与标准存在着细微的不同
> * 每条命令必须以 ; 结尾
> * SQL命令关键字不区分字母大小写

### SQL语句优化

​	 一 . 经常select,where,order by 的字段应该建立索引优化语句。

​	 二 . 单条查询语句最后添加 LIMIT 1 ,停止全表扫描。

​	 三 . where 字句中尽量不使用 !=,否则放弃索引全表扫描。

​	 四 . 尽量避免null值判断,否则放弃索引全表扫描。

​	 五 . 尽量避免 or 连接条件，否则放弃索引全表扫描。

​	 六 . 模糊查询尽量避免使用前置 % ,否则全表扫描。

​	 七 . 经量避免使用 in 和 not in,否则全表扫描。

​	 八 . 尽量避免使用 select * ,使用具体字段 * ，不要返回用不到的任何字段。

​	  放弃索引全表扫描：相当于不使用索引直接查询，而是全表中一条一条的记录中查询。

​	  全表扫描：不使用索引等方式查询，在全表中一条一条的记录中查询。

------



# MySQL 数据库操作

### 数据库操作

1.查看已有库
>show databases;

2.创建库(指定字符集)
>方法一：create database 库名 [character set utf8];
>
>方法二：create database 库名 default charset utf8 collate utf8_general_ci; 
>
>​									  （ collate utf8_genneral    :utf8顺序排序，_ci ：不区分大小写）

```sql
e.g. 创建stu数据库，编码为utf8
create database stu character set utf8;
create database stu charset=utf8;
```

3.查看创建库的语句(字符集)

>show create database 库名;

```sql
e.g. 查看stu创建方法
show create database stu;
```

4.查看当前所在库
>select database();

5.切换库
>use 库名;

```sql
e.g. 使用stu数据库
use stu;
```

6.删除库
>drop database 库名;

```sql
e.g. 删除test数据库
drop database test;
```

7.库名的命名规则
>* 数字、字母、下划线,但不能使用纯数字
>* 库名区分字母大小写
>* 不能使用特殊字符和mysql关键字


### 数据表的管理

1. 表结构设计初步
   
    【1】 分析存储内容
    【2】 确定字段构成
    【3】 设计字段类型
  
2. 数据类型支持

    

    #### unique类型:

    | unique类型                         |
    | ---------------------------------- |
    | 设置当前字段的值为唯一的不可重复的 |

>#### 数字类型：
>
>>整数类型（精确值） - INTEGER，INT，SMALLINT，TINYINT，MEDIUMINT，BIGINT
>>定点类型（精确值） - DECIMAL
>>浮点类型（近似值） - FLOAT，DOUBLE
>>比特值类型 - BIT
>>
>>![1562566639507](/home/tarena/.config/Typora/typora-user-images/1562566639507.png)

![](img/整型.png)

>对于精度比较高的东西，比如money，用decimal类型提高精度减少误差。列的声明语法是DECIMAL(M,D)。
>>M是数字的最大位数（精度）。其范围为1～65，M 的默认值是10。
>>D是小数点右侧数字的数目（标度）。其范围是0～30，但不得超过M。
>>比如 DECIMAL(6,2)最多存6位数字，小数点后占2位,取值范围-9999.99到9999.99。

> 比特值类型指0，1值表达2种情况，如真，假

----------------------------------

>#### 字符串类型：
>
>>CHAR和VARCHAR类型
>>BINARY和VARBINARY类型
>>BLOB和TEXT类型
>>ENUM类型和SET类型
>>
>>

![](img/字符串.png)![1562566658123](/home/tarena/.config/Typora/typora-user-images/1562566658123.png)char 和 varchar

>char：定长，效率高，一般用于固定长度的表单提交数据存储，默认1字符
>varchar：不定长，效率偏低

* text 和blob
>text用来存储非二进制文本
>blob用来存储二进制字节串

* enum 和 set
>enum用来存储	给出的一个值
>set用来存储给出的值中一个或多个值

-------------------------------------------


1. 表的基本操作
   
### 创建表(指定字符集)

**语 法：**

```sql
create table 表名(
字段名 数据类型 字段说明,
字段名 数据类型 字段说明,
...
字段名 数据类型 字段说明
);
```

>>* 如果你想设置数字为无符号则加上 unsigned
>>* 如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
>>* DEFAULT 表示设置一个字段的默认值
>>* PRIMARY KEY关键字用于定义列为主键。主键的值不能重复。
>>* AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。

```sql
e.g.  创建班级表
create table class_1 (id int primary key auto_increment,name varchar(32) not null,age int not null,sex enum('w','m'),score float default 0.0);

e.g. 创建兴趣班表
create table interest (id int primary key auto_increment,name varchar(32) not null,hobby set('sing','dance','draw'),course char not null,price decimal(6,2),comment text);
```

> 查看数据表
>
> >show tables；

>查看已有表的字符集
>
>>show create table 表名;

>查看表结构
>
>>desc 表名;

>删除表
>
>>drop table 表名;
>>
>>------
>>
>>------
>>
>>


# 数据基本操作

### 插入(insert)(增)

```SQL
！向所有字段中插入数据
insert into 表名 values(值1),(值2),...;
! 向部分字段中插入数据
insert into 表名(字段1,...) values(值1),...;
```

**注意：**插入的记录值如果不是英文必须 **加 引 号 ( " " )**括起来

```sql
e.g. 
insert into user values("hfk","123456",25,"M");

insert into class_1 values (2,'Baron',10,'m',91),(3,'Jame',9,'m',90);
```

### 查询(select)(查)

```SQL
select * from 表名 [where 条件];
select 字段1,字段名2 from 表名 [where 条件];
```

```sql
e.g. 
查找表内所有记录
select * from 表名;
查找表内具体字段的记录
select 字段1,字段2 from 表名[where 条件];
查找表内字段1或者字段2中字段中3内是3个字符的记录按照升序排序显示
select * from 表名 where (字段名="记录1" or 字段名="记录2") 
and 字段名3 like "__" order by 字段名
查找表内在字段1或者字段2中字段中3内是3个字符的记录按照升序排序显示
select * from 表名 where 字段名 in (字段名，字段名) and 字段名 like "__" order by 字段名

```

### where子句

where子句在sql语句中扮演了重要角色，主要通过一定的运算条件进行数据的筛选

注意:where字句适合用在整表增删改查中添加一定的运算条件进行数据的筛选，字段中适合用分组筛选 ： having

MySQL 主要有以下几种运算符：
>算术运算符
>比较运算符
>逻辑运算符
>位运算符

### 算数运算符



![1562566724729](/home/tarena/.config/Typora/typora-user-images/1562566724729.png)

![](img/算数.png)

```sql
e.g.
select * from class_1 where age % 2 = 0;
```


### 比较运算符

![1562566744347](/home/tarena/.config/Typora/typora-user-images/1562566744347.png)

![](img/比较.png)

```sql
e.g.
select * from class_1 where age > 8;
select * from class_1 where between 8 and 10;
select * from class_1 where age in (8,9);
```

### 逻辑运算符
![1562566787098](/home/tarena/.config/Typora/typora-user-images/1562566787098.png)

![](img/逻辑.png)

```sql
e.g.
select * from class_1 where sex='m' and age>9;
```

### 位运算符
![1562566813536](/home/tarena/.config/Typora/typora-user-images/1562566813536.png)



![1562566837207](/home/tarena/.config/Typora/typora-user-images/1562566837207.png)

```sql
									查询记录做数学运算
e.g. 查询时显示记录数据翻倍
	select 字段名*2 from 表名;
e.g. 更新字段中所有的记录*2
	update 表名 set 字段名=字段名*2 where 字段名="更新对象";
e.g. 查询字段记录+100之后大于800的字段记录
	select 字段名,字段名 from 表名 where 字段名 + 100 > 800;
```




### 更新表记录(update)(改)

```SQL
update 表名 set 字段1=值1,字段2=值2,... where 条件;
```

```sql
e.g.
update class_1 set age=11 where name='Abby';
```


###　删除表记录(delete)(删)

```SQL
delete from 表名 where 条件;

注意:delete语句后如果不加where条件,所有记录全部清空
不删除方法表：表内添加 ISDELETE字段，更改字段类型为0，下次查询不会查到ISDELETE为0的记录。
```
```sql
e.g.
delete from class_1 where name='Abby';
```


### 表字段的操作(alter)

```SQL
语法 ：alter table 表名 执行动作;

* 添加字段(add)
    alter table 表名 add 字段名 数据类型;
    alter table 表名 add 字段名 数据类型 first;
    alter table 表名 add 字段名 数据类型 after 字段名;
* 删除字段(drop)
    alter table 表名 drop 字段名;
* 修改数据类型(modify)
    alter table 表名 modify 字段名 新数据类型;
* 修改字段名(change)
    alter table 表名 change 旧字段名 新字段名 新数据类型;
* 表重命名(rename)
    alter table 表名 rename 新表名;
```

```sql
e.g. 
alter table interest add date Date after course;
```


# 时间类型数据

>时间和日期类型:
>>DATE，DATETIME和TIMESTAMP类型
>>TIME类型
>>年份类型YEAR

![1562566905279](/home/tarena/.config/Typora/typora-user-images/1562566905279.png)

![](img/时间.png)

### 时间格式

> date ："YYYY-MM-DD"
> time ："HH:MM:SS"
> datetime ："YYYY-MM-DD HH:MM:SS"
> timestamp ："YYYY-MM-DD HH:MM:SS"
注意
  1、datetime ：不给值默认返回NULL值
  2、timestamp ：不给值默认返回系统当前时间

### 日期时间函数
  * now()  返回服务器当前时间
  * curdate() 返回当前日期
  * curtime() 返回当前时间
  * date(date) 返回指定时间的日期
  * time(date) 返回指定时间的时间

### 时间操作

* 查找操作
```sql
  select * from timelog where Date = "2018-07-02";
  select * from timelog where Date>="2018-07-01" and Date<="2018-07-31";
```

* 日期时间运算

  - 语法格式

    select * from 表名  where 字段名 运算符 (时间-interval 时间间隔单位);

  - 时间间隔单位：  1 day | 2 hour | 1 minute | 2 year | 3 month

```sql
  select * from timelog where shijian > (now()-interval 1 day);
```

------

------

# 高级查询语句

### 排序

ORDER BY 子句来设定你想按哪个字段哪种方式来进行排序，再返回搜索结果。

使用 ORDER BY 子句将查询数据排序后再返回数据：

```sql
SELECT field1, field2,...fieldN from table_name1 where field1
ORDER BY field1 [ASC [DESC]]
```

默认情况ASC表示升序，DESC表示降序

```sql
select * from class_1 where sex='m' order by age;
```

### 分页 

LIMIT 子句用于限制由 SELECT 语句返回的数据数量 或者 UPDATE(改),DELETE(删)语句的操作数量

带有 LIMIT 子句的 SELECT 语句的基本语法如下：

```sql
SELECT column1, column2, columnN 
FROM table_name
WHERE field
LIMIT [num]
```


### 模糊查询

LIKE用于在where子句中进行模糊查询，SQL LIKE 子句中使用百分号 %字符来表示任意字符。

| 代替符号 | 代替规则                                                     |
| -------- | ------------------------------------------------------------ |
| %        | SQL LIKE 子句中使用百分号 %字符来表示任意字符。(%表示0到多个字符) |
| "_"      | SQL LIKE 子句中使用下划线"_"字符来表示任意一个字符。(字符可以累加使用) |
| "__"     | SQL LIKE 子句中使用两个下划线"__"字符来表示任意两个个字符。  |

使用 LIKE 子句从数据表中读取数据的通用语法：

```sql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1
```

```sql
e.g. 
mysql> select * from class_1 where name like 'A%';
```

### 正则查询 : REGEXP

mysql中对正则表达式的支持有限，只支持部分正则元字符

```sql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 REGEXP condition1
```

```sql
e.g. 
select * from class_1 where name regexp 'B.+';
```

### 联合查询

UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据。

UNION 操作符语法格式：

```sql
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL（所有的，包含重复） | 默认为 DISTINCT（去掉重复）]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```
>expression1, expression2, ... expression_n: 要检索的列。
>tables: 要检索的数据表。
>WHERE conditions: 可选， 检索条件。
>DISTINCT: 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响。
>ALL: 可选，返回所有结果集，包含重复数据。
>要求查询的字段必须相同

```sql
select * from class_1 where sex='m' UNION ALL select * from class_1 where age > 9;
```

### 多表查询

多个表数据可以联合查询，语法格式如下

```sql
select  字段1,字段2... from 表1,表2... [where 条件]
```

```sql
e.g.
select class_1.name,class_1.age,class_1.sex,interest.hobby from class_1,interest where class_1.name = interest.name;
```



### 聚合函数（聚合查询）

| 聚合函数名    | 功能                                   |
| ------------- | -------------------------------------- |
| avg(字段名)   | 求指定字段中的记录的平均值             |
| max(字段名)   | 求指定字段中记录的最大值               |
| min(字段名)   | 求指定字段中的记录的最小值             |
| sum(字段名)   | 求指定字段的记录和                     |
| count(字段名) | 求指定字段的记录的个数                 |
| count(*)      | 记录中不为null，都将统计所有记录的个数 |

**聚合函数使用语法：**	

```sql
select	聚合函数(字段名)1,聚合函数(字段名)2	... ...	from	表名;				
```

注意 ：聚合函数在默认情况下是不能与其他字段一起进行查询。

### 分组查询 + 组合查询

分组：要分组的字段 ：字段内记录，记录相同的数据会被划分到一组。

**语法：**

```sql
select	[分组的字段],聚合函数(字段名),聚合函数(字段名)	... ...

from	表名	[where	条件]	

group	by	分组的字段, ....			     <-------按具体条件进行分组 

[order	by]	... ...						<--------按具体条件进行排序

[limit]	... ...							<-------按具体条件进行限制由SELECT语句返回的数据数量
```

```
e.g.	求表中某个字段的总记录数：（打印结果为：[分组的字段名]+聚合查询结果）
select [分组的字段名],聚合查询(字段名) from 表名 group by 分组的字段名;
e.g.	

```

### 分组筛选 ： having

| having:        having 和 group by ：一起联用   |
| ---------------------------------------------- |
| 功能定义：     group	by	分组后做组内筛选 |

 **having语法：**

```sql
select	[分组的字段],聚合函数(字段名),聚合函数(字段名)	... ...

from	表名	[where	条件]	

group	by	分组的字段, ... ....		    <-------按具体条件进行分组

having 条件 ... ... 					  <---------group by 分组后做组内筛选

[order	by]	... ...						<--------按具体条件进行排序

[limit]	... ...							<-------按具体条件进行限制由SELECT语句返回的数据数量
```

```sql
e.g.
select 字段名,avg(字段名) as 别名 from 表名 group by 字段名 having 字段名 > 200;
select hfk,avg(hfks) as swn from rjr group by hfk having swn > 200;
```

### distinct函数 ：去掉重复

功能作用：去掉重复

**语法：**

```sql
select distinct(字段名) from 表名
```

### 查询记录做数学运算

```sql
									查询记录做数学运算
e.g. 查询时显示记录数据翻倍
	select 字段名*2 from 表名;
e.g. 更新字段中所有的记录*2
	update 表名 set 字段名=字段名*2 where 字段名="更新对象";
e.g. 查询字段记录+100之后大于800的字段记录
	select 字段名,字段名 from 表名 where 字段名 + 100 > 800;
```

### 索引()

一.	什么是索引

​		 什么是索引	：对数据库表的一列或多列的值进行排序的一种结构

二.	优点，缺点

​		 优点 ：	加快数据的检索速度		

​		 缺点：	1.占用物理存储空间

​					    2.对表中数据进行更新时，索引也会动态维护，会降低维护速度

三.	  索引的比对手段:	1.查询系统时间

​											2.执行查询

​			 							   3.查看执行时间

​			 在某字段上创建索引

​											1.查询系统时间

​											2.执行查询

​											3.查看执行时间

**四. 索引的分类****

1.**主键索引**

​		特点：增加主键索引之后，主键字段自动会被增加索引（唯一的，不可重复的,不能为空，效率最高）

**增加主键[索引]语法**	

```sql
已有表添加主键
alter table 表名 add primary key(id)

AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1

创建表时指定主键类型
create table 表名(id int primary key auto_increment) 
```

2.**唯一索引** ：要求字段中对应记录必须是唯一的

​		特点： 1.唯一索引可以有多个 	

​					 2.唯一索引所在的字段的记录必须是唯一的

**唯一索引创建语法：**						**unique类型** ：设置当前字段的值为唯一的不可重复的。    					

```sql
1.创建表的时候指定唯一性
create table 字段名(记录名 类型 unique,... ...);
e.g.
create table 字段名(id int primary key auto_increment, phone varchar(20) unique)

2.对已有表创建唯一索引
create unique index 索引名 on 表名(字段名)
```

3.**普通索引**

**创建语法：**

```sql
创建表同时指定普通索引
create table 表名(
id 数据类型 数据类型 ... ...,
字段名 数据类型 数据类型... ...,
index(字段名),
index(字段名),
)
```

**对已有表创建索引**

```sql
create index 索引 on 表名(字段名)
```

六.**取消(删除)索引**

```sql
drop index 索引名称 on 表名;
```

七.**查询索引**

```
show index from 表名;
```

### 数据备份

1. 备份命令格式
>mysqldump -u用户名 -p 源库名 > ~/***.sql
>> --all-databases  备份所有库
>> 库名             备份单个库
>> -B 库1 库2 库3   备份多个库
>> 库名 表1 表2 表3 备份指定库的多张表

2. 恢复命令格式
>mysql -uroot -p 目标库名 < ***.sql
>从所有库备份中恢复某一个库(--one-database)
>
>>mysql -uroot -p --one-database 目标库名 < all.sql


# Python操作MySQL数据库

### pymysql安装

>sudo pip3 install pymysql


### pymysql使用流程

1. 建立数据库连接(db = pymysql.connect(...))

2. 创建游标对象(c = db.cursor())

3. 游标方法: c.execute("insert ....")     <----游标方法返回值：执行成功返回1  执行失败返回0

4. 提交到数据库 : db.commit()

5. 关闭游标对象 ：c.close()

6. 断开数据库连接 ：db.close()

   ```python
   # 创建mysql连接
   msdb = pymysql.connect(host="localhost",
                          port=3306,
                          user="root",
                          password="123456",
                          charset="utf8",
                          database="redis")
   '示 例 1：
   # 创建游标对象
   c = msdb.cursor()
   sele = "select username,age,gender,password from user where username=%s"
   # 游标方法
   cursor.execute(sele, [username])
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

**常用函数**


>db = pymysql.connect(参数列表)
>>host ：主机地址,本地 localhost
>>port ：端口号,默认3306
>>user ：系统用户名
>>password ：系统用户密码
>>database ：连接的数据库
>>charset ：编码方式,推荐使用 utf8

> **数据库连接对象**(db)的方法
>
> >db.commit() 提交到数据库执行
> >db.rollback() 回滚
> >cur = db.cursor() 返回游标对象,用于执行具体SQL命令
> >db.close() 关闭连接

>**游标对象**(cur)的方法
>
>>cur.execute(sql命令,[列表]) 执行SQL命令
>>cur.close() 关闭游标对象
>>cur.fetchone() 获取查询结果集的第一条数据 (1,100001,"河北省")                  
>>cur.fetchmany(n) 获取n条 ((记录1),(记录2))                 
>>cur.fetchall() 获取所有记录

```

```

------



# 数据库的关系(关系型数据库)

### 外键 ：Foreign Key

​		作用：	约束当前表的某字段的记录必须取自于另外一张表的主键字段的记录值，

​						当前表的某字段的记录的个数不能超过另外一张表的主键字段的个数。	

​		目的：使表中的数据保持一致

​		外键：1.	是另外一张表的主键，可以有多个外键，可以重复使用在不同的字段，也可以是空值。

​					2.	外键内提取的记录值必须是主键内的记录值，外键在主键内提取的记录值可以重复，

​							但外键内的记录值个数不能大于主键内的记录值个数。

​					 3.    约束表与表之间的关系，只有外键一种手段，

​							约束的只是外键中的记录值必须是主键中包含的记录值。

​		主键 ：是不能重复和为空值的，保证数据的完整性，表中只能有一个主键。

| 外键        | 用于建立与另外一张表的关联                                   |
| ----------- | ------------------------------------------------------------ |
| 外键列      | 外键所在的列称之为"外键列"                                   |
| 外键表/子表 | 外键所在的表称之为"外键表"或"子表"                           |
| 主键        | 能够唯一标识一条记录的字段或属性(属性组)(表中只能用一个主键) |
| 主键列      | 主键所在的列称之为"主键列"                                   |
| 主键表/主表 | 被外键列所引用的表称之为"主表"或"主键表"                     |

**语法：** 		

### **创建表的同时指定外键**

```sql
create table 表名(字段名 类型...,字段名 类型..., ... ...
	
constraint 外键名 foreign key(外键列)
                	<---------constraint 添加主键约束
                	<---------外键名 :	给外键起个名字
					<---foreign key(外键列) :需要引用主键表的外键列,需要添加主键约束的外键列
     
references 主键表(主键列)     	
                			<----------被外键引用的主键表(被引用的主键表的主键列)
)；
```

```sql
e.g.
create table Course(
	id in primary key auto_increment,
	cname varchar(20)
)
create table Course(
	id in primary key auto_increment,
	cname varchar(20),
	course int,
	constraint fk_course_teacher Foreign Key(外键列) references Course(id)
)
```



### **对已有表增加外键**	

```sql
alter table 表名 add constraint 外键名 foreign key(外键列) references 主键表(主键列)
				
				<---------add constraint:添加外键约束  
				<---------外键名 :给外键起个名字
				<--------foreign key(外键列) :需要引用主键表中主键列的外键列
    		  	<----------references 主键表(主键列)：被外键引用的主键表(被引用的主键表的主键列)
```

**查看表的主键引用情况**

```sql
show create table 表名;
```

**删 除  外  键**

```sql
alter table 表名 drop foreign key 外键名;
```

```sql
删除外键后，只删除外键，不删除 ：KEY	外键名	(`被设置为外键的字段名`）,
e.g. :
删除后留有：      KEY `fk_major_student` (`major_id`)
```

### 级联操作

功能作用：设置级联操作后，数据表中设置为外键的外键表，依旧可以做更新和删除。

**语 法：**    		----- 对已建表添加级联操作

```sql
alter table 表名 
add constraint 外键名 				<---------add constraint:添加外键约束  
foreign key(外键列) 				<--------foreign key(外键列) :需要引用主键表中主键列的外键列
references 主键表(主键列)	  <--references 主键表(主键列)：被外键引用的主键表(被引用的主键表的主键列)
on delete 级联操作     				<-------级联删除-------
on update 级联操作	   				<-------级联更新(更改)----
```

| on delete | 级联删除       |
| --------- | -------------- |
| on update | 级联更新(更改) |

**级 联 操 作 ---- 取值：**

| restrict     (默认值)   | 子表中有关联数据，那么主表中就不允许做删除或更新 |
| ----------------------- | ------------------------------------------------ |
| cascade     (经常用)    | 数据级联删除,更新(主表删除时子表也跟随删除,更新) |
| set null       (不常用) | 主表删除数据时子表中的相关数据会设置为null       |

```sql
e.g.
--为Score表中的stu_id增加外键，引用student主键的id,并设置级联操作
alter table Score
add constraint fk_student_score
foreign key(stu_id)
references student(id)  < ------此处不能加括号
on delete cascade       <-----设置外键时设置为级联删除操作
on update cascade;		<-----设置外键时设置为级联更新(更改)操作
```

### 表连接查询(表关联查询)

表连接查询功能作用：实现数据在多表中关联的数据查询



### **交 叉 连 接**    

**语 法：**

```sql
select * from 数据表,数据表, ... ...;
```

查询出来的结果(数量)称为 ：笛卡尔积 ：数据表记录相乘的方式展示

**交叉连接显示查看规则**：

```sql
显示内容查看规则: 	第一张表中每条记录都会和第二张表中的每条记录拼接一次。以交叉显示方式呈现。
```

```sql
例如：第二个表中所有记录会交叉显示在第一个表中的第一条记录后面：

			第二个表中所有记录会交叉显示在第一个表中的第二条记录后面：

							... ..... ...... ........省略
```

```
e.g.
查询teacher和course表中的所有的数据
select * from teacher,course;
```



### **内 连 接**  

功能作用	: 在关联的两张表中，把满足条件的数据筛选出来。		**< --------重点**

**语 法:**    				

```sql
select 表名.字段名,表名.字段名, ... ...
from 表名1
inner join 表名2 on 条件 				<------满足两个内连接共同的条件
inner join 表名3 on 条件 				<------满足两个内连接共同的条件
... ...
```

```sql
e.g.
使用内连接查询teacher和course表中的数据(姓名，年龄，课程，名称，课时)
select * from teacher as t 
inner join course as c 
on t.course_id = c.id;

e.g.
查询学员的姓名,年龄，所在班级，专业名称,并筛选出1904班的学员。
select s.name,s.age,c.classname,m.m_name
from student as s
inner join Classinfo as c on s.id = c.id 
inner join major as m on s.major_id = m.id
where c.classneme = "1904"; 
```

### 外 链 接

### **左 外 连 接**

功能作用：一 .	左表中所有的数据都会查询出来(不满足的也会查出来)。

​				   二 .	将右表中满足关联条件的数据查询出来。

​				   三 .	不满足关联条件(关联不上)的数据关联字段将以null值作为填充

​				   左表：	

​			  	 右表：

**语 法：**

```sql
select 字段名,字段名.....

from A表 left join B表 

on 关联条件
```



### **右 外 链 接**

功能作用：一 .	右中所有的数据都会查询出来(不满足的也会查出来)。

​				   二 .	将左表中满足关联条件的数据查询出来。

​				   三 .	不满足关联条件(关联不上)的数据关联字段将以null值作为填充

**语 法：**

```sql
select 字段名,字段名.....

from A表 right join B表 

on 关联条件				   
```

****

### 子查询(嵌套查询)

**定 义：** 	将一个查询结果作为外侧操作中的一个条件出现	

**语 法：**

```sql
select 字段名,字段名 ... ...
from 表名 
where 条件=(select 字段名,字段名 ... ...
		   from 表名 
	       where 条件=(select 字段名,字段名 ... ...
					  from 表名 
                      where 条件=(select ... ...)))
```

```sql
e.g.
-- 查询考过逆风老师所教课程的学员信息
select * from student
where id in(select stu_id from Score
where course_id = (
select course_id from teacher
where name = "逆风"));
```

子查询(嵌套查询)得到的结果中满足条件只有1个：可以使用  = 

子查询(嵌套查询)得到的结果中满足条件有多个：可以使用 in (代替 = ) 

```sql
e.g.
mysql> select * from student
    -> where id =(select stu_id from Score			<-----返回结果有三个 = 号不适用
    -> where score is not null);
ERROR 1242 (21000): Subquery returns more than 1 row  <----字表查询返回超过一行

mysql> select * from student
    -> where id in(select stu_id from Score		<-----改用 in 号即可
    -> where score is not null);
+----+--------+--------+-----+--------------------+----------+----------+
| id | name   | gender | age | school             | class_id | major_id |
+----+--------+--------+-----+--------------------+----------+----------+
|  1 | 小健   | M      |  25 | 哈佛大学           |        1 |        1 |
|  2 | 老健   | M      |  25 | 麻省理工大学       |        2 |        2 |
|  3 | 好健   | M      |  25 | 牛津大学           |        3 |        3 |
+----+--------+--------+-----+--------------------+----------+----------+
```

# E - R 模 型

E-R 模 型 定 义：Entity - Relationship 模型 (实体关系模型)

​						 ：以图形的方式展示数据库中的表与表关系

**应 用 ：**在数据库设计阶段一定会使用到

**概 念 ：**

​			一 . 	**实体 - Entity**

​					   表示数据库中的一个表。

​					    图形表示：矩形框		

​			二 .  	**属性**

​						表示某实体中的某一特性，即表的字段 	

​						图形表示： 椭圆形

​			 三 . 	**关系 - Relationship**

​						表示实体与实体之间的关联关系。(关系只能通过 **添 加 外 键** 添加关系)

​						**一对一关系( 1 : 1 ) :	** 

​										A表中的一条记录只能关联到B表中的一条记录上

​										B表中的一条记录只能关联到A表中的一条记录上。

​										在数据库中的 **实 现 手 段** ：

​												在任意的一张表中增加：

​												一 . 外键，并引用自另外一张表的主键。

​												二 . 外键列加上唯一索引，进行索引约束。

​						**一对多关系( 1 : M ) :**

​			    						A表中的一条记录能关联到B表中的多条记录上。

​										B表中的一条记录只能关联到A表中的一条记录上。

​										在数据库中的 **实 现 手 段** ：

​												在"多"表中增加：

​												一 . 外键，引用"一"表的主键。										

​						**多对多关系( M : M ) :**									

​										A表中的一条记录能关联到B表中的多条记录上。

​										B表中的一条记录能关联到A表中的多条记录上。

​										在数据库中的 **实 现 手 段** ：

​													依靠第三张关联表，来实现多对多：	

​													一 . 创建第三张表

​													二 . 一个主键，两个外键

​															外键分别引用自关联的两个表的引用

### SQL语句优化

​	 一 . 经常select,where,order by 的字段应该建立索引优化语句。

​	 二 . 单条查询语句最后添加 LIMIT 1 ,停止全表扫描。

​	 三 . where 字句中尽量不使用 !=,否则使用全表扫描，放弃索引全表扫描。

​	 四 . 尽量避免null值判断,否则使用全表扫描，放弃索引全表扫描。

​	 五 . 尽量避免 or 连接条件，否则使用全表扫描，放弃索引全表扫描。

​	 六 . 模糊查询尽量避免使用前置 % ,否则使用全表扫描。

​	 七 . 经量避免使用 in 和 not in,否则使用全表扫描。

​	 八 . 尽量避免使用 select * ,使用具体字段 * ，不要返回用不到的任何字段。

​	  放弃索引全表扫描：相当于不使用索引直接查询，而是全表中一条一条的记录中查询。

​	  全表扫描：不使用索引等方式查询，在全表中一条一条的记录中查询。



### 辅助工具

Mavicat for MySQL :MySQL数据库工具(企业专用)

Power Designer :数据库建立模型：(社区版没用) ---只支持windows

Microsoft Visio : 制作 E R 图

# MySQL数据库读锁与写锁

### 读锁(共享锁)

**定 义:**

​		执行MySQL数据库update(更改)命令时，加读锁后，其他人操作数据库，可以查询此数据，此时不可以更改		此数据。

### 写锁(互斥锁--排它锁)

**定 义:**

​		执行MySQL数据库update(更改)命令时，加写锁后，其他人不能查询被更改中的数据，也不能更改此数据。





