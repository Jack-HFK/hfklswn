"""
4. 使用面向对象,描述下列情景.
   张无忌 教 赵敏 打篮球
   赵敏 教 张无忌 画眉
   张无忌 上班赚了10000元
   赵敏  上班赚了5000元.

   总结:以上情景,属于数据不同.所以定义一个人类,让不同的对象区分.
"""


class Person:
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def teach(self, person_other, str_skill):
    # 类内部,可以使用私有变量,也可以使用属性.
    # 类外部,只能使用属性.
    print("%s教%s%s技能" % (self.__name, person_other.name, str_skill))

  def work(self, money):
    print("%s上班赚了%d钱" % (self.name, money))


zwj = Person("张无忌")
zm = Person("赵敏")

zwj.teach(zm, "打篮球")
zm.teach(zwj, "画眉")
zwj.work(10000)
zm.work(5000)
