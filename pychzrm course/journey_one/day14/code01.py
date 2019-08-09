"""
  类与类的关系
"""


# 泛化:父子
class A:
  pass


class B(A):
  pass


# 关联:部分与整体
class C:
  def __init__(self, d):
    self.d = d


class D:
  pass


d01 = D()
c01 = C(d01)


# 依赖:合作
class E:
  def fun01(self, f):
    pass


class F:
  pass
