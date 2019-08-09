# 练习1:使用生成器函数,获取列表中所有偶数
#     [34,4,54,5,7,8]

def get_even(list_target):
  for item in list_target:
    if item % 2 == 0:
      # return item  返回一个数据,退出方法.
      yield item  # 返回多个数据,暂时离开方法


list01 = [34, 4, 54, 5, 7, 8]
result = get_even(list01)
# print(result)
# 没有事先存储所有偶数,
# 而是循环一次  计算一次  返回一次
for item in result:
  print(item)
