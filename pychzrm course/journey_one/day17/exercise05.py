"""
  练习1:改写员工管理器
"""

class Employee:
  pass


class EmployeeManager:
  def __init__(self):
    self.__list_emp = []

  def add_employee(self, emp):
    self.__list_emp.append(emp)

  def __iter__(self):
    for item in self.__list_emp:
      yield item

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
