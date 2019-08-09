# 练习:
# 对下列代码进行异常处理.
dict_commodity_info = {
  101: {"name": "屠龙刀", "price": 10000},
  102: {"name": "倚天剑", "price": 10000},
  103: {"name": "九阴白骨爪", "price": 8000},
  104: {"name": "九阳神功", "price": 9000},
  105: {"name": "降龙十八掌", "price": 8000},
  106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def buying():
  """
    购买
  """
  print_commodity()
  dict_order = create_order()
  list_order.append(dict_order)
  print("添加到购物车。")


def input_number(str_msg):
  while True:
    try:
      number = int(input(str_msg))
      return number
    except:
      print("输入有误")


def create_order():
  """
    创建订单
  :return: 订单 字典类型{"cid": 商品编号, "count": 数量}
  """
  while True:
    # cid = int(input("请输入商品编号："))
    cid = input_number("请输入商品编号：")
    if cid in dict_commodity_info:
      break
    else:
      print("该商品不存在")
  # count = int(input("请输入购买数量："))
  count = input_number("请输入购买数量：")
  return {"cid": cid, "count": count}


def print_commodity():
  for key, value in dict_commodity_info.items():
    print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def select_menu():
  """
     菜单选择
  :return:
  """
  while True:
    item = input("1键购买，2键结算。")
    if item == "1":
      buying()
    elif item == "2":
      settlement()


def settlement():
  """
    结算
  :return:
  """
  print_order()
  total_money = get_total_money()
  pay(total_money)


def pay(total_money):
  """
    购买
  :param total_money:
  :return:
  """
  while True:
    money = float(input("总价%d元，请输入金额：" % total_money))
    if money >= total_money:
      print("购买成功，找回：%d元。" % (money - total_money))
      list_order.clear()
      break
    else:
      print("金额不足.")


def print_order():
  """
    打印订单
  """
  for item in list_order:
    commodity = dict_commodity_info[item["cid"]]
    print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))


def get_total_money():
  """
    获取总价
  :return:
  """
  total_money = 0
  for item in list_order:
    commodity = dict_commodity_info[item["cid"]]
    total_money += commodity["price"] * item["count"]
  return total_money


# 程序入口
select_menu()
