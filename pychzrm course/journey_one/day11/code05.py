"""
  封装
    设计思想
  练习:exercise03.py
"""


# 需求:老张开车去东北

class Person:
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def to(self, type, str_pos):
    print(self.name)
    type.run(str_pos)


class Car:
  def run(self, str_pos):
    print("行驶到:", str_pos)


lz = Person("老张")
car = Car()
lz.to(car, "东北")
