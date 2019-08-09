"""
  模块1
"""

# 使用__all__定义可以导出的成员
__all__ = ["fun01"]

def fun01():
  print("fun01")

def fun02():
  print("fun02")

# 隐藏成员(不会被import * 导入)
def _fun03():
  print("fun03")

print(__name__)