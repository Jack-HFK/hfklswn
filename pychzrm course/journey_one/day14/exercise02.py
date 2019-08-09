"""
  练习:

"""

"""
class Employee: 
  def __init__(self, name, base_salary):
    # 代表人的很多数据....
    self.name = name
    self.base_salary = base_salary

  def calculate_salary(self):
    return self.base_salary


class Programmer(Employee):
  def __init__(self, name, base_salary, bonus):
    self.bonus = bonus
    super().__init__(name, base_salary)

  def calculate_salary(self):
    return self.base_salary + self.bonus


class Salesmen(Employee):
  def __init__(self, name, base_salary, sale_value):
    self.sale_value = sale_value
    super().__init__(name, base_salary)

  def calculate_salary(self):
    return self.base_salary + self.sale_value * 0.05


lw = Salesmen("老王", 2000, 5000)
print(lw.calculate_salary())
# 老王  -转岗--> 程序员

# 开除原老王, 招聘新老王
# 缺点:员工的姓名等人的数据,都会重新创建.
# 目标:对象一个部分改变,而不是全部改变.
lw = Programmer("老王",8000,10000)
print(lw.calculate_salary())
"""
class Employee:
  def __init__(self, name,job_instance):
    # 代表人的很多数据....
    self.name = name
    self.job_instance = job_instance

  def get_salary(self):
    return self.job_instance.calculate_salary()

class Job:
  def __init__(self,base_salary):
    self.base_salary = base_salary

  def calculate_salary(self):
    return self.base_salary

class Programmer(Job):
  def __init__(self,base_salary, bonus):
    self.bonus = bonus
    super().__init__(base_salary)

  def calculate_salary(self):
    # return self.base_salary + self.bonus
    # 扩展重写:先调用父类被重写方法,再定义新功能
    return super().calculate_salary()  + self.bonus


class Salesmen(Job):
  def __init__(self, base_salary, sale_value):
    self.sale_value = sale_value
    super().__init__(base_salary)

  def calculate_salary(self):
    return self.base_salary + self.sale_value * 0.05


lw = Employee("老王",Salesmen(2000,5000))
print(lw.get_salary())
# 老王  -转岗--> 程序员

lw.job_instance = Programmer("老王",8000,10000)
print(lw.calculate_salary())









