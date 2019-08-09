"""
  包

python 程序结构
包(文件夹)
  模块(文件)
    类
      函数
        语句
"""
# import package01.module01
# package01.module01.fun01()
# from 包.模块 import 成员
from package01.module01 import fun01
fun01()
# from 包.包 import 模块
from package01.package02 import module02
module02.fun02()
# 练习1:根据文档中的目录结构,创建包与模块.
# 练习2:模块与模块的互相调用(包内/包与包).
#      main.py 调用 skill_manager.py 成员
#      skill_manager.py 调用 skill_deployer.py 成员
#      skill_deployer.py 调用 list_helper.py
# 要求:模块中必须包含函数/类(实例方法/类方法)







