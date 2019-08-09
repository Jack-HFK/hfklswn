"""
  练习:参照下列代码,定义类MyRange.
  for i in range(5):#0 1 2 3 4
    print(i)

   for i in MyRange(5):#0 1 2 3 4
    print(i)

  15:35
"""


class MyRangeIterator:
  def __init__(self, stop_value):
    self.__start_value = 0
    self.__stop_value = stop_value

  def __next__(self):
    if self.__start_value >= self.__stop_value:
      raise StopIteration()
    result = self.__start_value
    self.__start_value += 1
    return result


class MyRange:
  def __init__(self, stop_value):
    self.__stop_value = stop_value

  def __iter__(self):
    return MyRangeIterator(self.__stop_value)


# 0 1 2
# 循环一次  计算一次  返回一个
for i in MyRange(5):
  print(i)
