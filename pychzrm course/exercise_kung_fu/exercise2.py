"""
    生成器函数

"""
#    -- 定义学生类(姓名,年龄,性别,成绩)
#    -- 定义生成器函数:获取列表中所有女同学.
#    -- 定义生成器函数:获取列表中年龄大于30的所有学生
#    -- 定义生成器函数:获取列表中成绩小于60的所有学生

class Student:
    def __init__(self, name, age, sex, score):
      self.name = name
      self.age = age
      self.sex = sex
      self.score = score

list01 = [
    Student("第二梦", 32, "女", 100),
    Student("步惊云", 31, "男", 48),
    Student("聂风", 20, "男", 88)
]
#  返回所以添加到列表的女生
def find_schoolgir(list_target):
    for i in list01:
        result = []
        if i.sex == "女":
            result.append(i)
        return result
#    生成器函数调用（循环）一次计算一次返回一个
def find_schoolgirs(list_target):
    for i in list01:
        result = []
        if i.sex == "女":
            result.append(i)
        yield result
# 生成器表达式
find01 =(i for i in list01  if i.sex == "女")

for i in find01:
    print(i.name)
