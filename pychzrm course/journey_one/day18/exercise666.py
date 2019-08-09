"""
  练习1:
    将通用函数定义在list_helper.py模块中
    在当前模块中,测试find.

  练习2:
    功能1:定义函数,在列表中查找"如来神掌"技能.
    功能2:定义函数,在列表中查找攻击力大于50的单个技能.
    功能3:定义函数,在列表中查找cd大于0的单个技能.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示
"""
from common.list_helper import ListHelper


class SkillData:
    def __init__(self, name, atk, cd, speed):
        self.name = name
        self.atk = atk
        self.cd = cd
        self.atk_speed = speed


list01 = [
    SkillData("降龙十八掌", 100, 60, 50),
    SkillData("如来神掌", 80, 50, 30),
    SkillData("一阳指", 20, 0, 80)
]


# def find_list01(list_hfk):
#     number = 0
#     for item in list_hfk:
#         if item.atk < 50:
#             number += 1
#     return number
#
#
# def find_list02(list_hfk):
#     number = 0
#     for item in list_hfk:
#         if item.cd == 0:
#             number += 1
#     return number
#
#
# def condition01(item):
#     return item.atk < 50
#
#
# def condition02(item):
#     return item.cd == 0
#
#
# def find_list(list_hfk, cindition):
#     number = 0
#     for item in list_hfk:
#         if cindition(item):
#             number += 1
#     return number


rjr = ListHelper.get_count(list01, lambda item: item.atk < 50)
print(rjr)
rjr = ListHelper.get_count(list01, lambda item: item.cd == 0)
print(rjr)

