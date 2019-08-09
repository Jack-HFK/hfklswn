"""
  练习:
    定义员工管理器
      -- 记录所有员工
      -- 计算员工总薪资

    1. 普通员工:底薪
    2. 程序员:底薪 + 项目分红
    3. 销售:底薪 + 提成(销售额 * 0.05)
    4. ...
    要求:增加新岗位,员工管理器不变.
  11:25

  练习:说出下列代码的设计思想.
"""


# -------------调用者--------------
class EmployeeManager:
  """
    员工管理器
  """

  def __init__(self):
    self.__employees = []

  def add_employee(self, emp):
    self.__employees.append(emp)

  def get_total_salary(self):
    total_salary = 0
    for item in self.__employees:
      # 调用父类一个方法,在不同子类中有不同实现.[多态]
      total_salary += item.calculate_salary()
    return total_salary


class Employee:
  """
    员工
  """

  def __init__(self, base_salary):
    self.base_salary = base_salary

  def calculate_salary(self):
    """
      计算薪资
    :return:
    """
    return self.base_salary


# ---------------定义者----------------
class Programmer(Employee):
  """
    程序员
  """

  def __init__(self, base_salary, bonus):
    self.bonus = bonus
    super().__init__(base_salary)

  def calculate_salary(self):
    return self.base_salary + self.bonus


class Salesmen(Employee):
  """
    销售员
  """

  def __init__(self, base_salary, sale_value):
    self.sale_value = sale_value
    super().__init__(base_salary)

  def calculate_salary(self):
    return self.base_salary + self.sale_value * 0.05


#------------测试------------
manager = EmployeeManager()
manager.add_employee(Employee(3000))
manager.add_employee(Programmer(8000,300000))
manager.add_employee(Salesmen(1800,2000))

result = manager.get_total_salary()
print(result)




