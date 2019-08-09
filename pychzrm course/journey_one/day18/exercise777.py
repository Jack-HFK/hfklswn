"""
  练习1:
    定义技能类(技能名称,攻击力,冷却时间,攻击速度)

    封装:
        功能1--获取冷却时间为0的所有技能
        功能2--获取攻击力大于10的所有技能
        功能3--获取攻击速度小于5的所有技能

    继承与多态:
      提取变化点
      定义不变的代码(客户端代码)
      测试:最后再实现这3个功能
"""

# class Skill:
#     def __init__(self,name,atk,time,speed):
#         self.name = name
#         self.atk = atk
#         self.time = time
#         self.speed = speed
#


# def skill01(item):
#     return item.time == 0
# def skill02(item):
#     return item.atk > 10
# def skill03(item):
#     return item.speed < 5


# def get_skill(list_skill,change):
#     for item in list_skill:
#         if change(item):
#             yield item
#
#
# lists = [
#     Skill("无双拳",250,1,8),
#     Skill("风神腿",520,0,26),
#     Skill("翻云掌",500,0,25)
# ]
# # 功能1--获取冷却时间为0的所有技能
# for item in get_skill(lists,skill01):
#     print(item.name)
# # 功能2--获取攻击力大于10的所有技能
# for item in get_skill(lists,skill02):
#     print(item.name)
# # 功能3 - -获取攻击速度小于5的所有技能
# for item in get_skill(lists,skill03):
#     print(item.name)



class Skill:
    def __init__(self,name,atk,time,speed):
        self.name = name
        self.atk = atk
        self.time = time
        self.speed = speed



def get_skill(list_skill,change):
    for item in list_skill:
        if change(item):
            yield item


lists = [
    Skill("无双拳",250,1,8),
    Skill("风神腿",520,0,26),
    Skill("翻云掌",500,0,25)
]

# 功能1--获取冷却时间为0的所有技能      形参  列表的元素的地址
for item in get_skill(lists,lambda item:item.time == 0):
    print(item.name)
# 功能2--获取攻击力大于10的所有技能
for item in get_skill(lists,lambda item:item.atk > 10):
    print(item.name)
# 功能3 - -获取攻击速度小于5的所有技能
for item in get_skill(lists,lambda item:item.speed < 5 ):
    print(item.name)
