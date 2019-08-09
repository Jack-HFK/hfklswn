"""
  生成器表达式
"""
list01 = [4, 4, 5, 56, 6, 78]
# 立即执行,将所有结果存入内存
result01 = [item for item in list01 if item > 5]
for item in result01:
    print(item)

result02 = (item for item in list01 if item > 5)
# 延迟执行,循环一次 计算一次  返回一个(覆盖了上一个)
for item in result02:
    print(item)

# 练习:将昨天作业,使用生成器表达式实现.
hfk = [item for item in list01 if item == 4]
for item in hfk:
    print(item)
