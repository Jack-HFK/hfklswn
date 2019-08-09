"""
# 练习2:根据生日(年月日),计算活了多天.
# 当前时间戳  -  出生时间戳
# 活了多少秒 --> 活了多少天
"""
import time


def life_days(year, month, day):
  tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
  life_second = time.time() - time.mktime(tuple_time)
  # 秒 -> 分钟- > 小时 -> 天
  return life_second / 60 / 60 // 24


print(life_days(1984, 6, 11))
