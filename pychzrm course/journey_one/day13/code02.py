"""
  继承--数据
  练习:exercise02.py
  14:30
"""
class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  # 如果子类具有构造函数,则没有父类的构造函数.
  def __init__(self, name, score):
    self.score = score
    # 通过super()函数调用父类方法
    super().__init__(name)

s01 = Student("无忌", 100)
print(s01.name)
print(s01.score)


p01 = Person("无忌")
print(p01.name)
# 如果子类没有构造函数,则使用父类的.
