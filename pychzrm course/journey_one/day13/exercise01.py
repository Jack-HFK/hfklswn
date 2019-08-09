"""
  练习: 定义子类:狗(行为: 看守)
  鸟(行为: 飞)
  父类: 动物(行为:叫)
  创建三个类型的对象.
  体会isinstance(对象, 类型)
  issubclass(子类型, 父类型)
"""
class Animal:
  """
    动物
  """
  def shout(self):
    print("喊叫")

class Bird(Animal):
  """
    鸟
  """
  def fly(self):
    print("飞喽")

class Dog(Animal):
  """
    狗
  """
  def watch(self):
    print("看守")

b01 = Bird()
b01.shout()

d01 = Dog()
d01.shout()

print(isinstance(b01,Bird))
print(issubclass(Bird,Animal))
