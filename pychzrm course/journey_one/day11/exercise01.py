# 练习:创建敌人类,具有数据(攻击力,血量)
#      保证数据的范围:   10 -攻击力- 50
#      保证数据的范围:   0 -血量- 100

class Enemy:
  def __init__(self,atk,hp):
    # 由于公开了实际存储数据的变量,
    # 所以类定义者失去了对变量的保护力度.
    # self.atk = ?
    # self.hp = ?
    self.set_atk(atk)
    self.set_hp(hp)

  def get_atk(self):
    return self.__atk

  def set_atk(self,value):
    if 10 <= value <= 50:
      self.__atk = value
    else:
      raise Exception("超过攻击力范围")

  def get_hp(self):
    return self.__hp

  def set_hp(self,value):
    if 0 <= value <= 100:
      self.__hp = value
    else:
      raise Exception("超过血量范围")

e01 = Enemy(20,50)
atk = e01.get_atk()
hp = e01.get_hp()
# 总结:1. 私有化实例变量: __变量名
#     2. 提供对实例变量的读\写操作.
#     3. 通过方法,操作数据.
# 执行步骤: