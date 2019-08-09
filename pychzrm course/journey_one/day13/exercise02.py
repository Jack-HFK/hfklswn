# 练习: 定义父类: 汽车(数据: 品牌, 型号, 价格)
# 子类: 电动汽车(数据:电池容量, 充电功率)
# 创建电动汽车对象, 画出内存图.
class Car:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

class ElectricCar(Car):
  def __init__(self, brand, model, price, battery_capacity, charging_power):
    # 调用父类构造函数
    super().__init__(brand, model, price)
    self.battery_capacity = battery_capacity
    self.charging_power = charging_power

c01 = ElectricCar("比亚迪", "唐", 150000, 10000, 200)

# 定义父类:动物(数据:姓名,年龄)
# 定义子类:狗(数据:爱称)

