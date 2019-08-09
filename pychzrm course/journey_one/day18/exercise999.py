# 练习5:
# 功能1: 定义函数, 在列表中获取攻击力最大的技能.
# 功能2: 定义函数, 在列表中计算速度最大的技能.
# ...
# 最终: 将通用代码定义在list_helper.py中
# 将变化点使用lambda表示
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

