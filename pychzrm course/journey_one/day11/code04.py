"""
  封装
  __slots__
"""

class Wife:
  __slots__ = ("name","__age")
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self,value):
    self.__age = value

w01 = Wife("丽丽",26)
# 因为类中定义了__slots__,所以不能在类外添加新数据.
# w01.sex = "女"
# w01.nmae = "莉莉"
print(w01.age)


