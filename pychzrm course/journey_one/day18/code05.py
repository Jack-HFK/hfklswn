"""
  内置高阶函数
  练习:exercise04.py
  19:42

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

# 1. map  技能列表  --> 技能名称列表
result = map(lambda e: e.name, list01)
# 返回值:生成器
for item in result:
    print(item)

result = ListHelper.select(list01, lambda e: e.name)
for item in result:
    print(item)

# 2. filter : 获取攻击力大于50的技能
for item in filter(lambda e: e.atk > 50, list01):
    print(item.name)

for item in ListHelper.find(list01, lambda e: e.atk > 50):
    print(item.name)

# 3. sorted :根据攻击力升序排列
# 返回值是列表,sorted没有改变目标列表.
result = sorted(list01, key=lambda e: e.atk)
for item in result:
    print(item.atk)

result = sorted(list01, key=lambda e: e.atk, reverse=True)
for item in result:
    print(item.atk)

ListHelper.order_by(list01, lambda e: e.atk)
for item in list01:
    print(item.atk)

print("----------")
# 4.  获取攻击力最大的技能
result = max(list01, key=lambda e: e.atk)
print(result.name)

result = ListHelper.get_max(list01, lambda e: e.atk)
print(result.name)

# 5. min ...
# 获取最小值
swn = min(list01,key=lambda e: e.atk )
print(swn.name)

