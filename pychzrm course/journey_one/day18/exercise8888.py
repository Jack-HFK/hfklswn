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

# 查找攻击在50--100的所有技能
for item in filter(lambda e: 100 >= e.atk >= 50, list01):
    print(item.atk)
# 获取技能和cd列表
for i in map(lambda e: [e.name, e.cd], list01):
    print(i)
# 攻击力最小的值
hfk = min(list01, key=lambda e: e.speed)
print(hfk.name)
# 降序排列
result = sorted(list01, key=lambda e: e.cd, reverse=True)
for i in result:
    print(i.name)
# 升序
result2 = sorted(list01,key=lambda e : e.cd, reverse= False)
for i in result2:
    print(i.name)