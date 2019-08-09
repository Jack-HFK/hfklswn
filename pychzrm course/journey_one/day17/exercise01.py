"""
  练习:
    通过抛出异常,限制老婆体重在..范围.
    体会:抛出异常 与 接收异常信息
"""


class WeightError(Exception):
  def __init__(self, value, str_msg, code):
    super().__init__(str_msg)
    self.age_value = value
    self.msg = str_msg
    self.code = code


class Wife:
  def __init__(self, weight):
    self.weight = weight

  @property
  def weight(self):
    return self.__weight

  @weight.setter
  def weight(self, value):
    if 40 <= value <= 60:
      self.__weight = value
    else:
      raise WeightError(value, "体重不在范围内", "self.__weight = value")


# w01 = Wife(50)
try:
  w01 = Wife(80)
except WeightError as e:
  print("错误提示:", e.msg)
  print("错误数值:", e.age_value)
  print("错误代码:", e.code)
