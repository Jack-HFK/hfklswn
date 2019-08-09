# 练习: 遍历员工管理器(私有的员工列表)
class EmployeeIterator:
  def __init__(self, target):
    self.__target = target
    self.__index = 0

  def __next__(self):
    if self.__index > len(self.__target)-1:
      raise StopIteration()
    result = self.__target[self.__index]
    self.__index += 1
    return result


class Employee:
  pass


class EmployeeManager:
  def __init__(self):
    self.__list_emp = []

  def add_employee(self, emp):
    self.__list_emp.append(emp)

  def __iter__(self):
    return EmployeeIterator(self.__list_emp)

manager = EmployeeManager()
manager.add_employee(Employee())
manager.add_employee(Employee())

for item in manager:
  print(item)

# 1. 获取迭代器对象(创建迭代器对象,将manager中的数据传递给迭代器)
iterator = manager.__iter__()
while True:
  try:
    # 2. 获取下一个元素(读取元素)
    item = iterator.__next__()
    print(item)
    # 3. 异常处理
  except StopIteration:
    break
