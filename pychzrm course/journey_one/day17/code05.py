"""
  yield --> 生成器
  练习:exercise07.py
      exercise08.py
      exercise09.py
"""


# class MyRange:
#   def __init__(self, stop_value):
#     self.__stop_value = stop_value
#
#   def __iter__(self):
#     start_value = 0
#     while start_value < self.__stop_value:
#       yield start_value
#       start_value += 1

# 循环一次  计算一次  返回一个
# for i in MyRange(5):
#   print(i)


class MyGenerator:
  """
    备注:本类是生成器的"源码",只需要看,不需要写.
    生成器:可迭代对象 + 迭代器对象
  """

  def __init__(self, stop_value):
    self.__stop_value = stop_value
    self.__start_value = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.__start_value >= self.__stop_value:
      raise StopIteration()
    result = self.__start_value
    self.__start_value += 1
    return result


def my_range(stop_value):
  start_value = 0
  while start_value < stop_value:
    yield start_value
    start_value += 1


# 0 1 2 3 4
result = my_range(5)
# 生成器对象.__iter__() 返回的结果就是生成器对象
# 140573829693376
print(id(result.__iter__()))
# 140573829693376
print(id(result))

# 函数体包含yield语句,返回值类型是生成器.
print(type(result))
for item in result:
  print(item)



# iterator = my_range(5).__iter__()
# while True:
#   try:
#     item = iterator.__next__()
#     print(item)
#   except StopIteration:
#     break
