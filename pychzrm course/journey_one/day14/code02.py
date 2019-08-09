"""
  内置可重写函数
"""


class Wife:
  def __init__(self, name, sex, age):
    self.name = name
    self.sex = sex
    self.age = age

  def __str__(self):
    return "奴家%s,芳龄%d,性别:%s" % (self.name, self.age, self.sex)

  def __repr__(self):
    return 'Wife("%s","%s",%d)' % (self.name, self.sex, self.age)


w01 = Wife("铁锤", "女", 23)
# <__main__.Wife object at 0x7f292fef9278>
str01 = str(w01)
#       w01.__str__()
str02 = repr(w01)
#        w01.__repr__()
print(str01)
print(str02)
print(w01)

# eval 作用:根据字符串执行python代码.
re = eval("1+2+3+4")
print(re)  # 10
# 需求:克隆对象
w02 = eval(w01.__repr__())
w03 = w01
w01.name = "捶捶"  # 影响w03 不影响w02
print(w03)
print(w02)

# 练习:定义学生类(姓名,成绩,年龄)
#  重写__str__  __repr__
#  创建1个学生对象,再克隆1个学生对象.
#  在控制台中打印两个对象
#   def __str__(self):
#     return "奴家%s,芳龄%d,性别:%s"%(self.name,self.age,self.sex)
#
#   def __repr__(self):
#     return 'Wife("%s","%s",%d)'%(self.name,self.sex,self.age)
#
