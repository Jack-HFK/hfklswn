"""
  可迭代对象
"""

list01 = [43,4,54,5,566,7,7]
# for itme in list01:
#   print(itme)

# 面试题:可以被for的条件?
#     对象具有__iter__()方法

# for原理:
# 1. 获取迭代器对象
iterator = list01.__iter__()
# 2. 循环获取下一个元素
while True:
  try:
    item = iterator.__next__()
    print(item)
# 3. 异常处理
  except StopIteration:# 迭代完成
    break






