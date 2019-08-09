
# 《Django 教程》
 - 讲师: 魏明择
 - 时间: 2019

## 目录
<!-- TOC depthFrom:3 depthTo:5 -->

[TOC]

<!-- /TOC -->

### 数据库的操作(CRUD操作)
- CRUD是指在做计算处理时的增加(Create)、读取查询(Read)、更新(Update)和删除(Delete)

#### 管理器对象
**定义：**

​	   每个继承自 models.Model 的模型类，都会有一个 objects 对象被同样继承下来。这个对象叫**管理器对象**

- 数据库的增删改查可以通过模型的管理器实现
    ```python
    class Entry(models.Model):
        ...
    Entry.objects.create(...) # 是管理器对象
    ```
    
    

```python
例如：
from django.http import HttpResponse
from . import models   # 调用models.py，使用其中的模型类(数据表)
# Create your views here.

def add_book_view(request):
    if request.method == "GET":
        btitle = request.GET.get("title","No Name")
        bpub = request.GET.get("pub","")
        # 方法一 使用objects对象创建一条记录
        models.Book.objects.create(title = python_books,  # 字段名 = 英文值 
                                 pub = "中华出版社")  # 字段名 = "中文值"
        return HttpResponse("添加成功")

```



#### 创建数据对象

- Django 使用一种直观的方式把数据库表中的数据表示成Python 对象
- 创建数据中每一条记录就是创建一个数据对象
    1. **Entry.objects.create(属性1=值1, 属性2=值1,...)**
       
        - 成功: 返回创建好的实体对象
        - 失败: 抛出异常
        
    2. **创建 Entry 实体对象,并调用 save() 进行保存**
       
        **方法：**
        
        ```python
        obj = Entry(属性=值,属性=值)
        obj.属性=值
        obj.save()
        无返回值,保存成功后,obj会被重新赋值
        ```
        
        ```python
        # 方法2
        from django.http import HttpResponse
        from . import models  # 调用models.py，使用其中的模型类(数据表)
        
        def add_book_view(request):
            if request.method == "GET":
                btitle = request.GET.get("title","No Name")
                bpub = request.GET.get("pub","")
               
                book = models.Book()  # 创建实例
                book.title = btitle
                book.pub = bpub
                book.price = 99.9
                book.pub_date = "2018-08-08"
                book.save()  # 执行SQL语句
                return HttpResponse("添加成功！")
        ```
        
        
        
    3. 示例1:
        ```python
        try:
            abook = Book.objects.create(title='Python', pub='清华大学出版社')
            print(abook)
        except:
            print('创建对象失败')
        ```
    
    4. 示例2:
        ```python
        try:
            abook = Book(title='Python', pub='清华大学出版社')
            abook.save()
            print(abook)
        except:
            print('创建对象失败')
        ```
    
    5. 示例3:
        ```python
        try:
            abook = Book()
            abook.title='Python'
            abook.pub='清华大学出版社'
            abook.save()
            print(abook)
        except:
            print('创建对象失败')
        ```
    
    - 练习:
        - 使用以上三种方式,分别向Book和Publisher表中各增加三条数据

#### Django shell 的使用
- 在Django提供了一个交互式的操作项目叫 `Django Shell` 它能够在交互模式用项目工程的代码执行相应的操作
- 利用 Django Shell 可以代替编写View的代码来进行直接操作
- 在Django Shell 下只能进行简单的操作，不能运行远程调式
- 启动 Django shell 显示IPython风格的**交互界面**如下:
    ```shell
    $ python3 manage.py shell
    
    manage.py shell
    Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
    Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: 
    In [2]: from bookstore import models
    In [3]: models.Book.objects.create(title="Python")
    Out[3]: <Book: Book object>
    In [4]: book = models.Book.objects.create(title='C++')
    In [4]: print(book)
    Book object
    ```
~~~python
在 bookstore/models.py 应用中添加两个model类
1. Book - 图书
    1. title - CharField 书名,非空,唯一
    2. pub - CharField 出版社,字符串,非空
    3. price - 图书价格,,
    4. market_price - 图书零售价
2. Author - 作者
    1. name - CharField 姓名,非空,唯一,加索引
    2. age - IntegerField, 年龄,非空，缺省值为1
    3. email - EmailField, 邮箱,允许为空
```
- 然后用Django Shell 添加如下数据
    - 图书信息
        | 书名   | 定价 | 零售价 | 出版社      |
        |---------|-------|--------------|----------------|
        | Python  | 20.00 |        25.00 | 清华大学出版社 |
        | Python3 | 60.00 |        65.00 | 清华大学出版社 |
        | Django  | 70.00 |        75.00 | 清华大学出版社 |
        | JQuery  | 90.00 |        85.00 | 机械工业出版社 |
        | Linux   | 80.00 |        65.00 | 机械工业出版社 |
        | Windows | 50.00 |        35.00 | 机械工业出版社 |
        | HTML5   | 90.00 |       105.00 | 清华大学出版社 |
    - 作者信息:
        | 姓名   | 年龄 | 邮箱 |
        |-------|------|-----|
        | 王老师 | 28 | wangwc@tedu.cn |
        | 吕老师 | 31 | lvze@tedu.cn |
        | 祁老师 | 30 | qitx@tedu.cn |
~~~



# 查询数据
- 数据库的查询需要使用管理器对象进行
- 通过 Entry.objects 管理器方法调用查询接口
    | 方法 | 说明 |
    |-|-|
    | all() | 查询全部记录,返回QuerySet查询对象 |
    | get() | 查询符合条件的单一记录 |
    | filter() | 查询符合条件的多条记录 |
    | exclude() | 查询符合条件之外的全部记录 |
    ... |

#### all()方法

- 方法: all()

- **用法**: Entry.objects.all()

- 作用: 查询Entry实体中所有的数据
    - 等同于
        - select * from tabel
    
- 返回值: QuerySet容器对象,内部存放Entry 实例

- 示例:
    ```python
    from bookstore import models
    books = models.Book.object.all()
    for book in books:
        print("书名", book.title, '出版社:', book.pub)
    ```
    
    ```python
    # 
    In [1]: from bookstore import models
    
    In [2]: books = models.Book.objects.all()
    
    In [3]: for a in books:
       ...:     print(a)
       ...:     
    书名No Name出版社
    书名No Name出版社
    书名No Name出版社
    ```
    
    

#### def __ str __(selef):方法

**在模型类中定义** `def __str__(self): ` 方法可以将自定义的对象转为字符串

```python
class Book(models.Model):
    title = ...
    def __str__(self):
        return "书名: %s, 出版社: %s, 定价: %s" % (self.title, self.pub, self.price)
```

```python
例如：
from django.db import models
# Create your models here.
# file:bookstore/models
class Book(models.Model):
    title = models.CharField('书名', max_length=50,)
    pub = models.CharField('出版社', max_length=50,)
#　类方法输出时转为以下格式的字符串
    def __str__(self):
        return "书名" + self.title + "出版社" + self.pub
```



#### 查询返回指定列values()

- 方法: **values**('列1', '列2')

- **用法**: 

    ​		**Entry.objects.values(...)**

- 作用: 查询部分列的数据并返回(查询部分列的数据返回结果字典表示)
  
    - select 列1,列2 from xxx
    
- 返回值: QuerySet
    - 返回查询结果容器，**容器内存字典**，每个字典代表一条数据,
    - **格式为: {'列1': 值1, '列2': 值2}**
    
- 示例:
    ```python
    from bookstore import models
    books = models.Book.objects.values("title", "pub")
    for book in books:
        print("书名", book["title"], '出版社:', book['pub'])
        print("book=", book)
    ```

#### 查询返回指定列values_list()

- 方法:**values_list**('列1','列2')
- 用法:**Entry.objects.values_list(...)**
- 作用:
  
    - 返回元组形式的查询结果（查询返回结果元组表示)
- 返回值: QuerySet容器对象,内部存放 `元组`
  
    - 会将查询出来的数据封装到元组中,再封装到查询集合QuerySet中
- 示例:
    ```python
    from bookstore import models
    books = models.Book.objects.values_list("title", "pub")
    for book in books:
        print("book=", book)  # ('Python', '清华大学出版社')...
    ```

#### 排序查询order_by()

- **方法:****order_by**

- **用法:**

    ```python
    Entry.objects.order_by('-列','列')
    
    Entry.objects.order_by('列')    <----正序排序
    
    Entry.objects.order_by('-列')　　<-----反序排序
    ```

    ```python
    from bookstore import models
    books = models.Book.objects.order_by("title")
    for book in books:
    	print(book)
    ```

    

- 作用:
  
    - 与all()方法不同，它会用SQL 语句的ORDER BY 子句对查询结果进行根据某个字段选择性的进行排序
    
- 说明:
  
- 默认是按照升序排序,降序排序则需要在列前增加'-'表示
  
- 示例:
    ```python
    from bookstore import models
    books = models.Book.objects.order_by("price")
    for book in books:
        print("书名:", book.title, '价格:', book.price)
    ```
    
    

#### 根据条件查询多条记录filter()

- **方法:** **filter(条件)**
- **语法:** 
  
    ```python
    Entry.objects.filter(属性1=值1, 属性2=值2)
    ```
- **返回值:**
  
    - QuerySet容器对象,内部存放 Entry 实例
- 说明:
  
    - 当多个属性在一起时为与关系，即当`Books.objects.filter(price=20, pub="清华大学出版社")` 返回价格为20 `且` 出版社为"清华大学出版社"的全部图书
- 示例:
    ```python
    # 查询书中出版社为"清华大学出版社"的图书
    from bookstore import models
    books = models.Book.objects.filter(pub="清华大学出版社")
    for book in books:
        print("书名:", book.title)

    2. 查询Author实体中id为1并且isActive为True的
        - authors=Author.objects.filter(id=1,isActive=True)
        
    3.  # 列出所有满足某一个条件的书
        books = models.Book.objects.filter(pub = "中华")
        # 列出所有满足某两个条件的书
        books = models.Book.objects.filter(pub = "条件１",title = "条件２
    ```


#### 字段查找
- 字段查询是指如何指定SQL语句中 WHERE 子句的内容。
- 字段查询需要通过QuerySet的filter(), exclude() and get()的关键字参数指定。
- 非等值条件的构建,需要使用字段查询,**字段查询需要使用查询谓词。**
- 示例:
    ```python
    # 查询作者中年龄大于30
    Author.objects.filter(age__gt = 30)
    # 对应
    SELECT .... WHERE AGE > 35;
    ```
#### 查询谓词
- 每一个查询谓词是一个独立的查询功能

**__exact : 等值匹配**

```python
Author.objects.filter(id__exact=1)
select * from author where id = 1
```

**__contains: 包含指定值**

```
Author.objects.filter(name__contains='w')
select * from author where name like '%w%'
```

**__startswith: 以 XXX 开始**

**__endswith : 以 XXX 开始**

**__gt : 大于指定值**

```
Author.objects.filer(age__gt=50)
select * from author where age > 50
```

**__gte: 大于等于**

**__lt : 小于**

**__lte : 小于等于**

**__in: 查找数据是否在指定范围内** 

- 示例
```
Author.objects.filter(country__in=['中国','日本','韩国'])
# 等同于
select * from author where country in ('中国','日本','韩国')
```

**__range: 查找数据是否在指定的区间范围内**

```
# 查找年龄在某一区间内的所有作者
Author.objects.filter(age__range=(35,50))
# 等同于
SELECT ... WHERE Author BETWEEN 35 and 50;
```

9. 详细内容参见: <https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups>

- 示例
    ```
    Entry.objects.filter(id__gt=4)
    SQL等效：

    SELECT ... WHERE id > 4;
    ```

- 练习:
    1. 查询Author表中age大于等于85的信息
        - `Author.objects.filter(age__gte=85)`
    2. 查询Author表中姓王的人的信息
        - `Author.objects.filter(name__startswith='王')`
    3. 查询Author表中Email中包含"wc"的人的信息
        - `Author.objects.filter(email__contains='in')`

#### 不等的条件筛选exclude()

- **语法:**
  
    ```python
    Entry.objects.exclude(条件)
    ```
    
- **作用:**
  
    - 返回不包含此 **`条件`** 的 作部的数据集
    
- **示例:**
  
    - 查询 `清华大学出版社，价格大于50` 以外的全部图书
    ```python
    books = models.Book.objects.exclude(pub=清华大学出版社, price__lt=50)
    for book in books:
        print(book)
    ```

#### 查询指定的一条数据get

- **语法:**
  
    ```
    Entry.objects.get(条件)
    ```
    
- **作用：**
  
    - 返回满足条件的唯一一条数据
    
- **返回值:**
  
    - Entry 对象
    
- 说明:
    - 该方法只能返回一条数据
    - 查询结果多余一条数据则抛出,Model.MultipleObjectsReturned异常
    - 查询结果如果没有数据则抛出Model.DoesNotExist异常
    
- 示例:
    ```
    from bookstore import models
    book = models.Book.object.get(id=1)
    print(book.title)
    ```

# 修改数据记录
1. **修改单个实体的某些字段值**
   
    1. 查
        - 通过 get() 得到要修改的实体对象
    2. 改
        - 通过 对象.属性 的方式修改数据
    3. 保存
        - 通过 对象.save() 保存数据
    - 如:
        ```python
        from bookstore import models
        abook = models.Book.objects.get(id=10)
        abook.market_price = "10.5"
        abook.save()
        ```
    
    #### 通过 QuerySet 批量修改 对应的全部字段
    
    - 直接调用QuerySet的update(属性=值) 实现批量修改
    - 如:
        ```python
        # 将 id大于3的所有图书价格定为0元
        books = Book.objects.filter(id__gt=3)
        books.update(price=0)
        # 将所有书的零售价定为100元
        books = Book.objects.all()
        books.update(market_price=100)
        ```

# 删除记录delete()
- 删除记录是指删除数据库中的一条或多条记录
- 删除单个Entry对象或删除一个查询结果集(QuerySet)中的全部对象都是调用 delete()方法
1. **删除单个对象**
   
    - 步骤
        1. 查找查询结果对应的一个数据对象
        2. 调用这个数据对象的delete()方法实现删除
        
    - 示例:
        ```python
        try:
            auth = Author.objects.get(id=1)
            auth.delete()
        except:
            print(删除失败)
        ```
        
        ```python
        例如：
        from bookstore import models
        abook = models.Book.objects.get(id=10)
        abook.delect()   # 删除单个
        
        from bookstore import models
        abook = models.Book.objects.filter(id__gt=2)
        abook.delect()  # 删除多个
        ```
        
    
2. **删除查询结果集**
   
    - 步骤
        1. 查找查询结果集中满足条件的全部QuerySet查询集合对象
        2. 调用查询集合对象的delete()方法实现删除
    - 示例:
        ```
        # 删除全部作者中，年龄大于65的全部信息
        auths = Author.objects.filter(age__gt=65)
        auths.delete()
        ```

#### 聚合查询
**定义：**

​			**聚合查询是指对一个数据表中的一个字段的数据进行部分或全部进行统计查询**,查bookstore_book数据表中			的全部书的平均价格，查询所有书的总个数等,都要使用聚合查询

1. 不带分组聚合
    - 不带分组的聚合查询是指**将全部数据进行集中统计查询**
    - 聚合函数:
        - 定义模块: `django.db.models`
        - **用法:** `from django.db.models import *`
        - 聚合函数: 
            - Sum, Avg, Count, Max, Min
    - 语法: 
      
        - **Entry.objects.aggregate(结果变量名=聚合函数('列'))**
    - 返回结果:
        - 由 结果变量名和值组成的字典
        - 格式为:
            - `{"结果变量名": 值}
    - 示例:
        ```python
        # 得到所有书的平均价格
        from bookstore import models
        from django.db.models import Count
        result = models.Book.objects.aggregate(myAvg=Avg('price'))
        print("平均价格是:", result['myAvg'])
        print("result=", result)  # {"myAvg": 58.2}
        
        # 得到数据表里有多少本书
        from django.db.models import Count
        result = models.Book.objects.aggregate(mycnt=Count('title'))
        print("数据记录总个数是:", result['mycnt'])
    print("result=", result)  # {"mycnt": 10}
    
        ```
    
    #### 分组聚合
    
    - 分组聚合是指通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值(也可以是平均值或总和)，即为**查询集**的每一项生成聚合。
    
    - **QuerySet** : 查询结果集合
    
    - **语法:** 
      
        - **QuerySet.annotate(结果变量名=聚合函数('列'))**
        
    - 用法步骤:
        1. 通过先用查询结果Entry.object.value. 查找查询要分组聚合的列
            - **Entry.object.value('列1', '列2')**
            - 如: 
                ```python
                # 获得查询结果集合pub_set
                pub_set = models.Book.objects.values('pub')
    print(books)  # <QuerySet [{'pub': '清华大学出版社'}, {'pub': '清华大学出版社'}, {'pub_hou {'pub': '机械工业出版社'}, {'pub': '清华大学出版社'}]>
                
                ```
        2. 通过返回结果的 QuerySet.annotate 方法**分组聚合**得到分组结果
            - **QuerySet.annotate(名=聚合函数('列'))**
            - 返回 QuerySet 结果集,内部存储结果的字典
            - 如:
                ```python
                # 查询结果集合pub_set调用annotate方法
                pub_count_set = pub_set.annotate(myCount=Count('pub'))
                print(pub_count_set)  # <QuerySet [{'pub': '清华大学出版社', 'myCount': 7}, {'pub': '机械工业出版社', 'myCount': 3}]>
                ```
            
        - .values('查询列名')
        
    - 示例:
        - 得到哪儿个出版社共出版多少本书
        ```py
        def test_annotate(request):
           - from django.db.models import Count
            from . import models
    
            # 得到所有出版社的查询集合QuerySet
            pub_set = models.Book.objects.values('pub')
            # 根据出版社查询分组，出版社和Count的分组聚合查询集合
            pub_count_set = pub_set.annotate(myCount=Count('pub'))  # 返回查询集合
            for item in pub_count_set:
                print("出版社:", item['pub'], "图书有：", item['myCount'])
            return HttpResponse('请查看服务器端控制台获取结果')
        ```

#### F对象
- **一个F对象代表数据库中某个字段的信息**
- F对象通常是对数据库中的字段值在不加载到内存中的情况下直接在数据库服务器端进行操作
- F对象在 数据包 django.db.models 中.使用时需要通过如下语句进行加载
    - **from django.db.models import F**
1. 作用:
    - **用于类属性(字段)之间的比较**。
    - 当**同时对数据库中两个字段的值进行比较获取 QuerySet 数据集时，可以便用F对象**
2. 说明:
   
    - 一个 F()对象代表了一个model的字段的值
3.  使用它就可以直接参考model的field和执行数据库操作而不用再把它们（model field）查询出来放到python内存中。

4. **语法:**
   
    ```python
    from django.db.models import F
    F('列名')
    ```
5. 示例1
    - 更新Book实例中所有的制场价涨10元
    ```python
    models.Book.objects.all().update(market_price=F('market_price')+10)
    
    # 以上做法好于如下代码
    books = models.Book.objects.all()
    for book in books:
        book.update(market_price=book.marget_price+10)
        book.save()
    ```
6. 示例2
    - 对数据库中两个字段的值进行比较，列出哪儿些书的零售价高于定价?
    ```python
    from django.db.models import F
    from bookstore import models
    
    books = models.Book.objects.filter(market_price__gt=F('price'))
    for book in books:
        print(book.title, '定价:', book.price, '现价:', book.market_price)
    ```

#### Q对象 - Q()
**定义：**

​	**当在获取查询结果集 使用复杂的逻辑或  `|` 、 逻辑非 `~` 等操作时可以借助于 Q对象进行操作**

**逻辑或:　| 	逻辑非：　~	逻辑与：　&**

- 如: 想找出定价低于20元 或 清华大学出版社的全部书，可以写成
  
    ```python
    models.Book.objects.filter(Q(price__lt=20)|Q(pub="清华大学出版社"))
    ```
    
- Q对象在 数据包 django.db.models 中。**需要先导入再使用**
  
    ```python
    from django.db.models import Q
    ```
    
    ****

1. **作 用 :** 在条件中用来实现除 and(&) 以外的 or(|) 或 not(~) 操作
2. **运算符:**

    - **& 与操作**
    - **| 或操作**
    - **〜 非操作**

3. 语法
    ```python
    from django.db.models import Q
    Q(条件1)|Q(条件2)  # 条件1成立或条件2成立
    Q(条件1)&Q(条件2)  # 条件1和条件2同时成立
    Q(条件1)&~Q(条件2)  # 条件1成立且条件2不成立
    ...
    ```

4. 示例
    ```python
    from django.db.models import Q
    # 查找清华大学出版社的书或价格低于50的书
    models.Book.objects.filter(Q(market_price__lt=50) | Q(pub_house='清华大学出版社'))
    # 查找不是机械工业出版社的书且价格低于50的书
    models.Book.objects.filter(Q(market_price__lt=50) & ~Q(pub_house='机械工业出版社'))
    # 查找清华大学出版社价格不是低于５０的书
    models.Book.objects.filter(~Q(market_price_lt=50) & Q(pub_house='清华大学出版社'))
    ```

# 原生的数据库操作方法
#### 使用Entry.objects.raw()进行数据库SQL语句查询或操作数据库

- 在django中，可以使用模型管理器的raw方法来执行select语句进行数据查询
1. **语法:** 
   
    ```python
    Entry.objects.raw("sql语句;")
    ```
    
2. **用法**

    - `Entry.objects.raw("sql语句;")`

3. 返回值:

    - QuerySet 集合对象

4. 示例
    ```python
    books = models.Book.objects.raw('select * from bookstore_book')
    
    for book in books:
        print(book)
    ```

##### 使用django中的游标cursor对数据库进行 增删改操作
- 在Django中可以使用 如UPDATE,DELETE等SQL语句对数据库进行操作。
- 在DJaogo中使用上述非查询语句必须使用游标进行操作
- 使用步骤:
   1. **导入cursor所在的包**
      
        - Django中的游标cursor定义在 django.db.connection包中，使用前需要先导入
        
        - **语法：**
          
            ```python
            from django.db import connection
            
            with connection.cursor() as cur:
                
             cur.execute('执行SQL语句')
            ```
    2. 用创建cursor类的构造函数创建cursor对象，再使用cursor对象,为保证在出现异常时能释放cursor资源,通常使用with语句进行创建操作
        - 如:
            ```python
            from django.db import connection
            with connection.cursor() as cur:
             cur.execute('执行SQL语句')
            ```
   
    - 示例
        ```py
        # 用SQL语句将id 为 10的 书的出版社改为 "XXX出版社"
        from django.db import connection
        with connection.cursor() as cur: 
            cur.execute('update bookstore_book set pub_house="XXX出版社" where id=10;')
   
        with connection.cursor() as cur:
            # 删除 id为1的一条记录
            cur.execute('delete from bookstore_book where id=10;')
        ```



