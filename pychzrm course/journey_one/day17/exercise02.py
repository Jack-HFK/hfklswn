# 练习1: (4,4,5,565,6,7) 通过迭代器,获取元组元素.
tuple01 = (4, 4, 5, 565, 6, 7)
iterator = tuple01.__iter__()
while True:
  try:
    item = iterator.__next__()
    print(item)
  except:
    break

# 面试题:不使用for,获取字典所有记录.
# 练习2: {"张无忌":3,"赵敏":2} 通过迭代器,获取字典记录.
dict01 = {"张无忌":3,"赵敏":2}
iterator = dict01.__iter__()
while True:
  try:
    key = iterator.__next__()
    value = dict01[key]
    print(key,value)
  except:
    break










