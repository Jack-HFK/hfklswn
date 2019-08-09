"""
  迭代器
     练习: 遍历员工管理器(私有的员工列表)
       exercise03.py
"""

class SkillIterator:
  """
    迭代器
  """

  def __init__(self, target):
    self.target = target
    self.index = 0

  def __next__(self):
    # 需求:将SkillManager中__list_skill的元素返回
    if self.index > len(self.target) - 1:
      raise StopIteration()

    result = self.target[self.index]
    self.index += 1
    return result


class Skill:
  pass
  # def __str__(self):
  #   return "技能"


class SkillManager:
  def __init__(self):
    self.__list_skill = []

  def add_skill(self, skill):
    self.__list_skill.append(skill)

  def __iter__(self):
    return SkillIterator(self.__list_skill)


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

# 目标:for 自定义类的对象
# for item in manager:
#   print(item)

iterator = manager.__iter__()
while True:
  try:
    item = iterator.__next__()
    print(item)
  except StopIteration:
    break

