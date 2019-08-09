# 定义函数，在技能列表中获取攻击力列表
# 定义函数，在技能列表中获取技能名称列表

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

# def get_str(list_target,list_hfk):
#     get_list = []
#     for item in list_target:
#         get_list.append(list_hfk(item))
#     return get_list
#
# rjr = get_str(list01,lambda e :e.name)
# print(rjr)
# rjr = get_str(list01,lambda e :e.atk)
# print(rjr)

result = ListHelper.select(list01,lambda e:{e.name,e.atk})
print(result)
result = ListHelper.select(list01,lambda e:(e.name,e.atk))
print(result)
result = ListHelper.select(list01,lambda e:[e.name,e.atk])
print(result)