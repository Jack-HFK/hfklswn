"""
  继承:设计思想
  练习:exercise03.py

  设计原则:
  1. 开闭原则
    扩展(增加新功能)开放(允许)
    修改(改变以前代码)关闭(拒绝)

  2. 依赖倒置
    使用抽象(父类,稳定的),而不是使用子类(多变化)
"""

# 老王开车去东北
# 需求变化:坐飞机
#          火车
#          骑车
#  ....

"""
class Person:
  def __init__(self, name):
    self.name = name

  def to(self, type, str_pos):
    print(self.name)
    if isinstance(type, Car):
      type.run(str_pos)
    elif isinstance(type, Airplane):
      type.flay(str_pos)

class Car:
   def run(self, str_pos):
     print("行驶到:", str_pos) 

class Airplane:
   def flay(self, str_pos):
     print("飞过到:", str_pos)
"""


# ------------使用者------------
class Person:
  def __init__(self, name):
    self.name = name

  def to(self, type, str_pos):
    # 如果传入的不是交通工具
    if not isinstance(type, Vehicle):
      # 人为抛出一个错误(程序中断)
      # 目的:传入的对象,必须是交通工具的子类.
      raise TypeError()
    print(self.name)
    # 关心的不是火车/飞机/汽车等交通工具
    # 关心的是他们有运输的功能
    type.transport(str_pos)


class Vehicle:
  """
    交通工具:代表火车/飞机/汽车..
  """

  def transport(self, str_pos):
    # 人为抛出一个错误(程序中断)
    # 目的:要求子类必须具有当前方法
    raise NotImplementedError()


# ------------定义者------------
class Car(Vehicle):
  def transport(self, str_pos):
    print("行驶到:", str_pos)

class Airplane(Vehicle):
  def transport(self, str_pos):
    print("飞过到:", str_pos)


lw = Person("老王")
c01 = Car()
a01 = Airplane()
lw.to(c01, "东北")
