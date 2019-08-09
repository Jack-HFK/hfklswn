# 练习4:
# 功能1: 定义函数, 在列表中计算攻击力的总和.
# 功能2: 定义函数, 在列表中计算速度的总和.
# ...
# 最终: 将通用代码定义在list_helper.py中
# 将变化点使用lambda表示
from common.list_helper import ListHelper


class SkillData:
    def __init__(self, name, atk, cd, speed):
        self.name = name
        self.atk = atk
        self.cd = cd
        self.speed = speed


list01 = [
    SkillData("降龙十八掌", 100, 60, 50),
    SkillData("如来神掌", 80, 50, 30),
    SkillData("一阳指", 20, 0, 80)
]


# def atks(lists,swn):
#     number = 0
#     for item in lists:
#         number += swn(item)
#     return number
#
# aa = atks(list01,lambda e:e.atk)
# print(aa)

#攻击力的和
l = ListHelper.sum(list01,lambda e : e.atk)
print(l)
#速度的和
l1 = ListHelper.sum(list01,lambda e : e.speed)
print(l1)