"""
  封装数据3:使用标准属性封装
  练习:exercise02
"""


class Wife:
  """
    老婆  15:30 上课
  """
  # 练习:修改上午代码,将敌人数据使用属性封装.
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @property # 拦截读取操作
  def age(self):
    return self.__age

  @age.setter# 拦截写入操作
  def age(self, value):
    if 28 <= value <= 32:
      self.__age = value
    else:
      raise Exception("我不要")

  # 拦截 对数据的操作,转为调用读写方法.
  #age = property(get_age, set_age)


w01 = Wife("丽丽", 30)
print(w01.age)
print(w01.__dict__)
