"""
  函数式编程
  -- 函数作为参数
"""

def fun01():
  print("fun01执行执行喽")

# 有小括号,是调函数,a变量得到是函数返回值
# a = fun01()
# 没小括号,没调函数,a变量得到是函数地址
a = fun01
# 通过变量a,调用函数fun01.
a()


def fun03():
  print("fun03执行执行喽")

def fun04():# 定义很多具体函数  [封装]
  print("fun04执行执行喽")

# func 代表(抽象) fun01 fun03  fun04  [继承]
def fun02(func):
  print("fun02的逻辑")
  func()# 调用func执行....  [多态]

fun02(fun01)    #fun02方法执行时调用fun01方法，结果是两个方法都执行
fun02(fun03)    #fun02方法执行时调用fun03方法，结果是两个方法都执行
fun02(fun04)    #fun02方法执行时调用fun04方法，结果是两个方法都执行






