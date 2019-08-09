"""
  运算符重载:
    自定义类创建的对象,也可以使用python内置运算符.
"""


class Vector:
  def __init__(self, x):
    self.x = x

  #  当前对象 + 其他数据
  def __add__(self, other):
    return Vector(self.x + other)

  #  其他数据 + 当前对象
  def __radd__(self, other):
    return self.__add__(other)

  # 当前对象 += 其他数据
  def __iadd__(self, other):
    self.x += other
    return self


v01 = Vector(1)
re = v01 + 2  # re   =   v01.__add__(2)
print(re.x)
# 练习:实现其他的算数运算符

re = 2 + v01
print(re.x)
# 练习:实现其他的反向算数运算符

list01 = [1]
list02 = list01 + [2]  # 创建新对象
list01 += [2]  # 原对象基础上累加

print(id(v01))
# 如果不重写+=运算符,则使用+运算符.所以重写+=时,应该选择返回原有对象
v01 += 2
print(id(v01))
print(v01.x)
# 练习:实现其他的复合运算符
