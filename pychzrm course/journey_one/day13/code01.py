"""
  继承--方法

  财产:钱不用孩子挣,但是可以花.
  皇位:江山不用孩子打,但是可以坐.
  ...
  代码:子类不用写,但是可以用.

  练习:fork_server.py
"""
# 设计角度: 先有子类,再有父类. 抽象化的过程:子(具体,小概念) -> 父(抽象,大概念)
# 编码角度: 先写父类,再写子类.

class Person:
  def say(self):
    print("会说话")

class Student(Person):
  def study(self):
    print("会学习")

class Teacher(Person):
  def teach(self):
    print("会讲课")

s01 = Student()
# 子类对象,直接使用父类方法.(继承语法的体现)
s01.say()
s01.study()

p01 = Person()
p01.say()
# 父类对象,只能使用自身方法,不能使用子类方法.

# 判断对象是否属于一个类型
print(isinstance(s01, Person))  # true
print(isinstance(s01, Teacher))  # false
print(isinstance(s01, (Person, Teacher)))  # true
print(isinstance(s01, Student))  # true

# 判断一个类型是否属于另一个类型
print(issubclass(Teacher, Person))  # true
print(issubclass(Teacher, Student))  # false
print(issubclass(Person, Student))  # false
print(issubclass(Person, Person))  # true
# 如果判断父子
print(issubclass(Teacher, Person) and Teacher != Person)
print(issubclass(Teacher, Teacher) and Teacher != Teacher)
