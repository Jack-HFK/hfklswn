"""
extend 函数
       

"""


# 创建一个序列类型的对象
my_list = [1, 2, 3]
# 将现有的序列合并到my_list
extend_my_list = my_list + [4, 5]

print(extend_my_list)  # [1, 2, 3, 4, 5]
# 将一个元组合并到这个序列
extend_my_list = my_list + (6, 7)
# 抛出异常 TypeError: can only concatenate list (not "tuple") to list
print(extend_my_list)

# 使用另一种方式合并
extend_my_list += (6, 7)
print(extend_my_list)  # [1, 2, 3, 4, 5, 6, 7]

# 使用extend()函数进行合并

extend_my_list.extend((7, 8))
print(extend_my_list)  # [1, 2, 3, 4, 5, 6, 7, 7, 8]
