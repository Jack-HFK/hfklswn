# 查找列表中的，偶数，奇数，总和，大于或小于88的数

list01 = [6, 8, 9, 66, 88, 99, 666, 888, 999]


# 偶数
def method01(list_target):
    for i in list_target:
        if i % 2 == 0:
            yield i


# 测试
# value = method01(list01)
# for i in value:
#     print(i)
def method02(list_target):
    for i in list_target:
        if i % 2 != 0:
            yield i


# 测试
# value1 = method02(list01)
# for i in value1:
#     print(i)
def method03(list_target):
    number_sum = 0
    for i in list_target:
        number_sum += i
    return number_sum


# 测试
# value2 = method03(list01)
# print(value2)

def method04(list_target):
    number = list_target[0]
    for i in list_target:
        if number <= i:
            number = i
    return number


# swn = method04(list01)
# print(swn)

def method05(list_target):
    number = list_target[0]
    for i in list_target:
        if number >= i:
            number = i
    return number


# swn = method05(list01)
# print(swn)

def method11(i):
    return i % 2 == 0


def method22(i):
    return i % 2 != 0


def method00(list_target, function):
    for i in list_target:
        if function(i):
            yield i


# swn = method00(list01, method11)
# for i in swn:
#     print(i)
# for i in method00(list01, lambda i: i % 2 == 0):
#     print(i)
#
# rjr = method00(list01, method22)
# for i in rjr:
#     print(i)
# for i in method00(list01, lambda i: i % 2 != 0):
#     print(i)

# 调用模块，调用通用方法
from Common.list_helper import ListHelper

# 调用实例方法：查找列表中所以元素
for item in ListHelper.find(list01, lambda item: item):
    print(item)
# 调用实例方法：获取列表第一个元素
print(ListHelper.first(list01, lambda e: e))
# 调用实例方法：获取列表中满足 >88的数字
print(ListHelper.get_count(list01, lambda e: e > 88))
# 调用实例方法：获列表求和
print(ListHelper.sum(list01, lambda e: e))
# 调用实例方法：获取列表满足条件最大的元素
print(ListHelper.get_max(list01, lambda e: e))

