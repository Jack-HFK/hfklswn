# 练习:手雷爆炸了,可能伤害敌人,玩家
#     还可能伤害未知的事物(鸭子,树...)
# 要求:如果增加了新事物,不影响手雷的代码.
# 体会:开闭原则,依赖倒置

# ------------使用者----------------
class Grenade:
  def explode(self, target):
    """
      爆炸
    """

    # 如果传入的对象,没有按要求继承Damageable,则错误.
    if not isinstance(target,Damageable):
      raise TypeError()

    # 希望调用父类,实际执行子类.
    # 调用目标的受伤方法
    target.damage(100)


class Damageable:
  """
    可以受伤害
  """

  def damage(self, value):
    # 如果子类没有当前方法,则错误.
    raise NotImplementedError()


# ------------定义者----------------
class Player(Damageable):
  """
    玩家
  """

  # 重写:与父类方法相同
  def damage(self, value):
    print("玩家扣%d血,并且碎屏." % value)


class Enemy(Damageable):
  """
    敌人
  """

  def damage(self, value):
    print("敌人扣%d血,并且头顶冒字." % value)

# 测试
g01 = Grenade()
p01 = Player()
e01 = Enemy()
g01.explode(p01)
