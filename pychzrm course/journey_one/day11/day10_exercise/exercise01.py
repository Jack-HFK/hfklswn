"""
3.定义学生类,具有(姓名,性别,成绩)数据,
           具有打印个人信息的行为.
  定义函数,在学生列表中,查找姓名是"张无忌"的学生对象.
  定义函数,在学生列表中,查找成绩大于60的所有女同学对象.
  定义函数,计算成绩大于等于60的所有同学数量.
  定义函数,获取最高分的学生对象.
  定义函数,删除所有成绩低于60分的学生对象.
"""


class Student:
  def __init__(self, name="", sex="", score=0):
    self.name = name
    self.sex = sex
    self.score = score

  def print_self(self):
    print(self.name, self.sex, self.score)


# 定义函数, 在学生列表中, 查找姓名是"张无忌"的学生对象.
def find01(list_target):
  for item in list_target:
    if item.name == "张无忌":
      return item


# 定义函数, 在学生列表中, 查找成绩大于60的所有女同学对象.
def find02(list_target):
  result = []
  for item in list_target:
    if item.score > 60 and item.sex == "女":
      result.append(item)
  return result

#定义函数,计算成绩大于等于60的所有同学数量.
def find03(list_target):
  count = 0
  for item in list_target:
    if item.score >= 60:
      count += 1
  return count

# 定义函数,获取最高分的学生对象.
def find04(list_target):
  max_value = list_target[0]
  for i in range(1,len(list_target)):
    if max_value.score <  list_target[i].score:
      max_value = list_target[i]
  return max_value

# 定义函数,删除所有成绩低于60分的学生对象.
def del_list_student(list_target):
  count = 0
  for i in range(len(list_target)-1,-1,-1):
    if list_target[i].score < 60:
      del list_target[i]
      count +=1
  return count

list01 = [
  Student("蔡徐坤", "女", 10),
  Student("吴亦凡", "女", 50),
  Student("张无忌", "男", 90),
  Student("张三丰", "男", 95),
  Student("迪丽热巴", "女", 100),
]
# stu01 = find01(list01)
# stu01.print_self()

# result = find02(list01)
# for item in result:
#   item.print_self()

# count = find03(list01)
# print(count)

# stu02  = find04(list01)
# stu02.print_self()
# print(stu02)

count = del_list_student(list01)
print(count)








