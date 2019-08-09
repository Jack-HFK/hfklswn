# 练习:小明在招商银行取钱.
# 17:15
class Person:
  def __init__(self, name, money):
    self.name = name
    self.money = money

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value


class Bank:
  def __init__(self, name, money):
    self.name = name
    self.money = money

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def draw_money(self, person, value):
    person.money += value
    self.money -= value


xm = Person("小明", 0)
zs = Bank("招商银行", 100000)
print(xm.money)
zs.draw_money(xm, 5000)
print(xm.money)
