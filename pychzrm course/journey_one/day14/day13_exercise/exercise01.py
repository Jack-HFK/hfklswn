"""
4. (扩展)有若干个图形(圆形/矩形....)
   定义图形管理器
      -- 记录所有图形(多个圆形对象,多个矩形对象),
      -- 提供计算总面积的方法.
      11:00
"""


# --------------调用者--------------------
class GraphicManager:
  """
    图形管理器
  """

  def __init__(self):
    self.__graphics = []

  def add_graphic(self, graphic):
    self.__graphics.append(graphic)

  def get_total_area(self):
    total_area = 0
    for item in self.__graphics:
      # 希望调用的是父类方法(一种动作)
      # 实际执行的是子类方法(不同实现方式)
      # 体现了多态性.
      total_area += item.calculate_area()
    return total_area


class Graphic:
  """
    图形
  """

  def calculate_area(self):
    pass


# -----------------定义者---------------------
class Circle(Graphic):
  """
    圆形
  """

  def __init__(self, r):
    self.radius = r

  def calculate_area(self):
    return 3.14 * self.radius ** 2


class Rectangle(Graphic):
  def __init__(self, l, w):
    self.length = l
    self.width = w

  def calculate_area(self):
    return self.length * self.width


# ----------测试-------------
manager = GraphicManager()
g01 = Circle(10)
manager.add_graphic(g01)
manager.add_graphic(Rectangle(10, 20))
result = manager.get_total_area()
print(result)
