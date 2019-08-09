"""
3. 使用面向对象,描述下列情景.
   玩家(具有攻击力)攻击敌人,敌人(具有血量)受伤后掉血,还可能死亡(掉装备).
   敌人(具有攻击力)攻击玩家,玩家(具有血量)受伤后掉血并且碎屏,还可能死亡(游戏结束).

   总结:以上情景,属于行为不同.所以定义玩家类与敌人类.用类区分.

   11:05
"""


class Player:
  def __init__(self, hp,atk):
    self.atk = atk
    self.hp = hp

  def attack(self, enemy):
    print("玩家攻击")
    enemy.damage(self.atk)

  def damage(self, value):
    self.hp -= value
    print("玩家受伤啦,还剩%d血量" % self.hp)
    print("屏幕碎啦")
    if self.hp <= 0:
      self.__death()

  def __death(self):
    print("游戏结束")

class Enemy:
  def __init__(self, hp,atk):
    self.hp = hp
    self.atk = atk

  def damage(self, value):
    self.hp -= value
    print("敌人受伤啦,还剩%d血量" % self.hp)
    if self.hp <= 0:
      self.__death()

  def __death(self):
    print("敌人死啦,掉下了?装备")

  def attack(self, player):
    print("敌人攻击")
    player.damage(self.atk)

p01 = Player(500,50)
e01 = Enemy(100,10)
# 玩家打敌人
p01.attack(e01)
p01.attack(e01)
# 敌人打玩家
e01.attack(p01)








