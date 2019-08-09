"""
   封装数据1:使用方法封装(不用)
   练习:fork_server.py
"""


class Wife:
    """
      老婆
    """

    def __init__(self, name, age):
        # 数据成员
        self.name = name
        # 通过方法操作数据,不要直接设置数据.
        self.set_age(age)

    # 2. 提供读取/写入变量的功能
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 28 <= value <= 32:
            # 1. 隐藏变量:内部改变变量名称(下划线+类名+变量名)
            # self.__age = age
            self.__age = value
        else:
            # 人为报错(程序中断)
            raise Exception("我不要")


# 不符合业务逻辑
w01 = Wife("丽丽", 30)
# 创建了新成员变量,没有访问成员变量__age
# w01.__age = 87
# 无法读取私有变量
# print(w01.__age)
# 小人做法
# print(w01._Wife__age)

# 通过方法,操作变量
# w01.set_age(30)
print(w01.get_age())
print(w01.__dict__)
