# 20:12
class SkillData:
  def __init__(self, name, atk, cd, speed):
    self.name = name
    self.atk = atk
    self.cd = cd
    self.atk_speed = speed


list01 = [
  SkillData("降龙十八掌", 100, 60, 50),
  SkillData("如来神掌", 80, 50, 30),
  SkillData("一阳指", 20, 80, 80)
]

# 练习1: 查找技能列表中攻击力在50 - -100 之间的所有技能.
for item in filter(lambda e:50 <= e.atk <= 100,list01):
  print(item.atk)

# 练习2: 在技能列表中, 获取技能名称与cd的列表.
# list --> 惰性操作 转换为 立即操作
result = list(map(lambda e:(e.name,e.cd),list01))
print(result)

# 练习3: 在列能列表中, 查找攻击速度最小的技能
result = min(list01,key = lambda e:e.atk_speed)
print(result.name)

# 练习4: 根据cd对象技能列表进行降序排列.
result = sorted(list01,key = lambda  e:e.cd,reverse= True)
# sorted 不会改变原来的列表,而是返回新列表.
# 如果需要改变原来的列表,需要通过切片定位元素,再进行修改.
list01[:] = result
for item in list01:
  print(item.cd)

# 练习5: 在技能列表中, 查找名称最长的技能.
result = max(list01,key = lambda e:len(e.name))
print(result.name)