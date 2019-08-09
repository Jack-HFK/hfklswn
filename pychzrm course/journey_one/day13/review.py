"""
  day12 复习
  封装
    分而治之  封装变化
  信息管理系统
    XXModel:描述需要处理的数据(对象)的模型(类).
    XXView:负责处理界面逻辑.(控制台/网页)
    XXController:负责处理业务逻辑.
    10:50 上课
"""


class XXController:
  def fun01(self):
    print("XXController--fun01")


class XXView:
  def __init__(self):
    # 1.创建对象
    self.manager = XXController()

  def fun02(self):
    # 2. 通过对象地址,调用实例方法
    self.manager.fun01()
    pass

  def fun03(self):
    self.manager.fun01()
    pass

v01 = XXView()
v01.fun02()

