"""
  lambda 表达式
  练习:exercise02.py
  匿名方法
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


# def condition01(item):
#   return item % 2 == 0

# def condition02(item):
#   return item > 5
#
# def condition03(item):
#   return item < 40

def find(list_targt, func):
    for item in list_targt:
        if func(item):
            yield item


# 使用 lambda 代替普通方法
list01 = [4, 5, 6, 7, 89]
# for item in find(list01, condition03):
for item in find(list01, lambda item: item % 2 == 0):
    print(item)


# -------语法-------
def fun01():
    return "ok"


# lambda : "ok"

def fun02(a, b):
    return a > b
# lambda a,b: a >b
