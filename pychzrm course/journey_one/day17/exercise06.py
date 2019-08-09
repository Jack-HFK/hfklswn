# 练习2: 改写MyRnage类

class MyRange:
  def __init__(self, stop_value):
    self.__stop_value = stop_value

  def __iter__(self):
    start_value = 0
    while start_value < self.__stop_value:
      yield start_value
      start_value += 1


# 循环一次  计算一次  返回一个
for i in MyRange(5):
  print(i)
