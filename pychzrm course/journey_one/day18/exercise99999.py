# 定义函数，对技能列表根据攻击力进行升序排列
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


def get_list(list_target):
    for i in range(len(list_target)):
        for item in range(i + 1, len(list_target)):
            if list_target[i].atk < list_target[item].atk:
                list_target[i], list_target[item] = list_target[item], list_target[i]
    # return list_target


get_list(list01)
for i in list01:
    print(i.name)
# swn = get_list(list01)
# for i in swn:
#     print(i.name)
