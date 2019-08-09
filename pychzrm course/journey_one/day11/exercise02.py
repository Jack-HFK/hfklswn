# 练习:创建敌人类,具有数据(攻击力,血量)
#      保证数据的范围:   10 -攻击力- 50
#      保证数据的范围:   0 -血量- 100

class Enemy:
  def __init__(self,atk,hp):
    self.atk = atk
    self.hp = hp

  @property # 目的:拦截读取操作,本质:创建property对象,注册读取方法.
  def atk(self):
    return self.__atk

  @atk.setter# 目的:拦截写入操作,本质:将写入方法注册到property对象中.
  def atk(self, value):
    if 10 <= value <= 50:
      self.__atk = value
    else:
      raise Exception("超过攻击力范围")

  @property # 相当于定义变量hp,存储property对象地址.
  def hp(self):
    return self.__hp

  @hp.setter
  def hp(self,value):
    if 0 <= value <= 100:
      self.__hp = value
    else:
      raise Exception("超过血量范围")

e01 = Enemy(20,50)
atk = e01.atk
hp = e01.hp
# 总结:1. 私有化实例变量: __变量名
#     2. 提供对实例变量的读\写操作.
#     3. 通过方法,操作数据.
# 执行步骤: