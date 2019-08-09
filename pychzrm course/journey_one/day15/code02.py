"""
  模块  调用 module01 中fun01函数.
"""
# 导入方式1:
#  语法:import 模块名称
#  使用:模块名称.成员
#  本质:创建一个变量叫module01,关联模块地址.
# import module01
# module01.fun01()

# 起别名
# import module01 as m
# m.fun01()

# 导入方式2:
# 语法:from 模块名 import 成员
# 使用:直接使用成员
# 本质:将成员添加到当前作用域
# from module01 import fun01
# fun01()

# 导入方式3:
from module01 import *

def fun01():
  print("code02 -- fun01")

# 就近原则:选择调用语句最近的,方法的定义.
fun01()


fun02()






