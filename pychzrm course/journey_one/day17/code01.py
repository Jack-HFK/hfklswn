"""
  主动抛出异常
  自定义异常类
  练习:fork_server.py
    通过抛出异常,限制老婆体重在..范围.
    体会:抛出异常 与 接收异常信息
  10:35
"""
class AgeError(Exception):
  def __init__(self, value, str_msg, code):
    super().__init__(str_msg)
    self.age_value = value
    self.msg = str_msg
    self.code = code


class Wife:
  def __init__(self, age):
    self.age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, value):
    if 22 <= value <= 30:
      self.__age = value
    else:
      # 将错误信息传递给创建Wife对象的代码
      # 需求:传递的错误信息有很多.
      # raise Exception("我不要")
      raise AgeError(value, "年龄不在范围内", "self.__age = value")


# w01 = Wife(50)
try:
  w01 = Wife(50)
except AgeError as e:
  print("错误提示:", e.msg)
  print("错误数值:", e.age_value)
  print("错误代码:", e.code)
