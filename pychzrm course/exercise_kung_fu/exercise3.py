"""
    函数式编程
    匿名方法函数：lamabda
     lambda 参数列表: 方法体

  普通方法
  def 方法名称(参数列表):
      方法体

  相对与普通方法的优缺点:
    优点:省略方法名称
         降低了程序间耦合度
    缺点:由于没有名称,所以不能重复使用.
         方法体只能有一条语句
         方法体必须有返回值

  作用:将方法作为参数,特别优雅.
"""

list01 = [22, 66, 88, 99, 222, 333, 888, 999]


# 查找列表中所有偶数
def find_eveb_number(list_targt):
    for i in list_targt:
        if i % 2 == 0:
            yield i


# 查找变化 提取变化点
def change(i):
    return i % 2 == 0


# 查找列表中所有奇数
def find_odd_number(list_targt):
    for i in list_targt:
        if i % 2 != 0:
            yield i


# 查找变化 提取变化点
def change2(i):
    return i % 2 != 0


# 函数体直接调用变化点
def find_number(list_targt, func):
    for i in list_targt:
        if func(i):
            yield i

# for i in find_number(list01,change):
    # print(i)
for i in find_number(list01,lambda e:e %2 ==0):
    print(i)
# for i in find_number(list01,change2):
#     print(i)
for i in find_number(list01,lambda e:e %2 !=0):
    print(i)
# lamabda 函数 后添加条件
#     3. 语法
# -- 定义：
# 变量 = lambda 形参: 方法体
# 	   -- 调用：
# 			变量(实参)