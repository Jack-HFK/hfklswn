"""
 Enclosing  外部嵌套作用域 ：函数嵌套。
"""


def fun01():
  a = 1  # 对于fun02 而言,属于外部嵌套作用域

  def fun02():
    b = 2
    # print(a)# 可以直接访问外部嵌套变量
    # a = 111 # 又创建了局部变量a,没有修改外部嵌套变量.
    nonlocal a  # 声明外部嵌套变量
    a = 111
    print(a)

  fun02()
  print(a)


fun01()
