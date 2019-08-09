"""
  函数作为参数的案例
    练习:fork_server.py
"""
list01 = [43, 4, 55, 56, 6, 67, 8]


# --------------封装-------------------
# 功能1:查找列表中所有偶数
def find01(list_targt):
  for item in list_targt:
    if item % 2 == 0:
      yield item

# 功能2:查找列表中所有大于5的数
def find02(list_targt):
  for item in list_targt:
    if item > 5:
      yield item

# 功能3:查找列表中所有小于40的数
def find03(list_targt):
  for item in list_targt:
    if item < 40:
      yield item


# --------------继承-------------------
# 提取变化点
def condition01(item):
  return item % 2 == 0

def condition02(item):
  return item > 5

def condition03(item):
  return item < 40

# 定义不变的
def find(list_targt, func):
  for item in list_targt:
    # if item < 40:
    # if condition03(item):
    if func(item):  # ----------多态------------
      yield item

for item in find(list01,condition03):
  print(item)