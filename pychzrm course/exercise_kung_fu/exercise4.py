"""
    闭包

    1. 三要素：
-- 必须有一个内嵌函数。
-- 内嵌函数必须引用外部函数中变量。
-- 外部函数返回值必须是内嵌函数。
    2. 语法
-- 定义：
def 外部函数名(参数):
		外部变量
		def 内部函数名(参数):
			使用外部变量
		return 内部函数名
-- 调用：
	   变量 = 外部函数名(参数)
        变量（参数）
"""


# 查找88大发66大顺
def find01():
    list01 = [66, 666, 88, 888, 8866]

    def find02():
        for i in list01:
            if i == 8866:
                return i

    return find02  # 返回find02方法的地址


a = find01()
print(a())


def find01():
    list01 = [66, 666, 88, 888, 8866]

    def find02():
        for i in list01:
            if i == 8866:
                return i

    return find02()  # 返回结果是：调用find02的函数（方法体）

print(find01())
