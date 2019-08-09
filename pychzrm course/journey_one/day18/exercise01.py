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

# ---------封装---------
# 功能1 - -获取冷却时间为0的所有技能
# 功能2 - -获取攻击力大于10的所有技能
# 功能3 - -获取攻击速度小于5的所有技能
def find01(list_target):
  for item in list_target:
    if item.cd == 0:
      yield item

def find02(list_target):
  for item in list_target:
    if item.atk > 10:
      yield item

def find03(list_target):
  for item in list_target:
    if item.atk_speed < 5:
      yield item
# ---------继承---------
def condition01(item):
  return item.cd == 0

def condition02(item):
  return item.atk > 10

def condition03(item):
  return item.atk_speed < 5

def find(list_target,func_condition):
  for item in list_target:
    if func_condition(item):
      yield item

find(list01,condition01)
find(list01,condition02)
find(list01,condition03)