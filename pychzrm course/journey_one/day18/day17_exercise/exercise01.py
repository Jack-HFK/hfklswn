# 3. 定义学生类(姓名,年龄,性别,成绩)
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
  Student("张三炮", 32, "女", 100),
  Student("吕泽玛利亚", 31, "女", 80),
  Student("宋二哥", 20, "男", 50)
]


def find(list_target):
  result = []
  for item in list_target:
    if item.sex == "女":
      result.append(item)
  return result


def find01(list_target):
  for item in list_target:
    if item.sex == "女":
      yield item

# 生成器表达式
find01 = (item for item in list01 if item.sex == "女")
# 调用方法执行
# 将所有结果存入列表,再返回.
result = find(list01)
for item in result:
  print(item.name)

# 调用方法不执行
# 返回生成器对象
result = find01(list01)
# 循环一次 执行一次 返回一个(替换上一个)
for item in result:
  print(item.name)


# 定义生成器函数:获取列表中年龄大于30的所有学生
def find02(list_target):
  for item in list_target:
    if item.age > 30:
      yield item

find02 = (item for item in list01 if item.age > 30)

result = find02(list01)
# 延迟/惰性操作
# 优点:不会将所有结果计算出来,存储在内存中.
# 缺点:通过索引/切片灵活的访问结果.
# 解决:将延迟操作 转为 立即操作
result = list(result)
print(result[0].name)
for item in result:
  print(item.name)


# 定义生成器函数:获取列表中成绩小于60的所有学生
def find03(list_target):
  for item in list_target:
    if item.score < 60:
      yield item


# 调用生成器函数,创建一个生成器对象
result = find03(list01)
# 使用一次
for item in result:
  print(item.name)

# 再使用一次(没有执行find03函数.)
for item in result:
  print(item.name)
