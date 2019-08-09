"""
  闭包
"""
def fun01():
  a = 1  # 对于fun02 而言,属于外部嵌套作用域

  def fun02():
    print(a)

  return fun02

# 闭包:
# 内部函数可以使用外部嵌套变量,外部函数执行完毕后,
# 没有释放内存,而是等待内部函数执行结束.
func = fun01()# 调用外部函数
func()# 再调用内部函数

#案例:
# 压岁钱
def give_gife_money(money):
  """
    获取压岁钱
  """
  print("得到压岁钱:",money)
  def child_buy(target,price):
    """
      孩子需要买东西
    """
    nonlocal money
    if money >=  price:
      money -= price
      print("孩子需要花%d钱,买%s"%(price,target))
    else:
      print("钱不够")
  # 希望外部可以调用内部函数
  return child_buy

action_buy = give_gife_money(30000)
action_buy("飞机",1000)
action_buy("手机",10000)
action_buy("房子",10000000)




