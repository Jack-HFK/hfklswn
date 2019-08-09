"""
  多继承
  15:15
"""
class A:
  def fun01(self):
    print("A--fun01")

class B(A):
  def fun01(self):
    super().fun01()
    print("B--fun01")

class C(A):
  def fun01(self):
    super().fun01()
    print("C--fun01")

class D(C,B):
  def fun01(self):
    super().fun01()#?
    print("D--fun01")

# 测试
d01 = D()
d01.fun01()
# 同名方法解析顺序
print(D.mro())




