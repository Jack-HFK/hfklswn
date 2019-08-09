# 练习:参照下列代码现象,自定义生成器函数my_enumerate.
# for item in enumerate([3,34,4,5,6]):
#   print(item)

def my_enumerate(list_target):
  for i in range(len(list_target)):
    yield (i, list_target[i])

for item in my_enumerate([3,34,4,5,6]):
  print(item)

for index,item in enumerate([3,34,4,5,6]):
  print(index,item)










