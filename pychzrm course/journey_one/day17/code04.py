"""
  迭代器 --> yield
  练习1:exercise05.py
  练习2:exercise06.py
  体会程序执行过程,理解生成迭代器代码的规则.
"""

# class SkillIterator:
# """
#   迭代器
# """
#
# def __init__(self, target):
#   self.target = target
#   self.templates = 0
#
# def __next__(self):
#   if self.templates > len(self.target) - 1:
#     raise StopIteration()
#
#   result = self.target[self.templates]
#   self.templates += 1
#   return result


class Skill:
  pass


class SkillManager:
  """
    可迭代对象
  """

  def __init__(self):
    self.__list_skill = []

  def add_skill(self, skill):
    self.__list_skill.append(skill)

  def __iter__(self):
    # return SkillIterator(self.__list_skill)

    for item in self.__list_skill:
      yield item

    """
      执行过程:
         1. 调用__iter__()方法程序不执行.
         2. 调用__next__()方法开始执行.
         3. 执行到yield语句暂时离开方法.
         4. 再次调用__next__()方法继续执行
         .....
      原理:如果方法体中包含yield语句,则自动生成迭代器代码.
      生成迭代器代码的大致规则:
        1.将yield关键字以前的代码,放到__next__()方法中.
        2.将yield关键字以后的数据,作为__next__()方法返回值.
    """

    # print("准备第一个元素:")
    # yield self.__list_skill[0]
    #
    # print("准备第二个元素:")
    # yield self.__list_skill[1]
    #
    # print("准备第三个元素:")
    # yield self.__list_skill[2]


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

# for item in manager:
#   print(item)

iterator = manager.__iter__()
while True:
  try:
    item = iterator.__next__()
    print(item)
  except StopIteration:
    break
