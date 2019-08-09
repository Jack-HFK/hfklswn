"""
  code03.py
  模块变量
"""
from module01 import *
import module01

fun01()
# fun02()  不能导入__all__规定外的成员
# fun03()  不能导入隐藏成员

# 获取模块文档注释
print(__doc__)
#/home/tarena/1904/python_base/day15/code03.py
print(__file__)

import sys
print(sys.path)
