"""
  练习:创建模块exercise02.py
      将double_list_helper.py粘贴到day15目录下.
      在exercise02模块中,调用double_list_helper模块方法
      实现以下功能:
        1. 获取00位置向右3个元素
        2. 获取13位置向左2个元素
        3. 获取22位置向上2个元素
      要求:分别使用三种导入方式实现.
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
"""
import double_list_helper as helper

pos = helper.Vector2(0, 0)
dir = helper.Vector2.get_right()
re = helper.get_elements(list01, pos, dir, 3)
print(re)
"""
"""
from double_list_helper import Vector2,get_elements

pos = Vector2(0, 0)
dir = Vector2.get_right()  # 0 1
re = get_elements(list01, pos, dir, 3)
print(re)
"""

# from double_list_helper import *
#
# pos = Vector2(0, 0)
# dir = Vector2.get_right()  # 0 1
# re = get_elements(list01, pos, dir, 3)
# print(re)

# 练习2:
# import double_list_helper as helper
# pos = helper.Vector2(1, 3)
# dir = helper.Vector2.get_left() # 0 1
# re = helper.get_elements(list01, pos, dir, 2)
# print(re)

# from double_list_helper import Vector2, get_elements
#
# pos = Vector2(1, 3)
# dir = Vector2.get_left()  # 0 1
# re = get_elements(list01, pos, dir, 2)
# print(re)

# from double_list_helper import *
# pos = Vector2(1, 3)
# dir = Vector2.get_left()  # 0 1
# re = get_elements(list01, pos, dir, 2)
# print(re)

# 练习3
# import double_list_helper as helper
# pos = helper.Vector2(2, 2)
# dir = helper.Vector2.get_up()  # 0 1
# re = helper.get_elements(list01, pos, dir, 2)
# print(re)

# from double_list_helper import Vector2,get_elements
# pos = Vector2(2, 2)
# dir = Vector2.get_up()  # 0 1
# re = get_elements(list01, pos, dir, 2)
# print(re)

from double_list_helper import *
pos = Vector2(2, 2)
dir = Vector2.get_up() # 0 1
re = get_elements(list01, pos, dir, 2)
print(re)


# import  double_list_helper as helper
# from double_list_helper import Vector2 as v2 ,get_elements as dd
# from double_list_helper import *




