"""
# 练习1:定义函数,根据年月日,返回星期数.
#  星期一  星期二 ... 星期日
"""
import time

def get_week(year,month,day):
  tuple_time = time.strptime("%d-%d-%d"%(year,month,day), "%Y-%m-%d")
  dict_weeks = {
     0:"星期一",
     1:"星期二",
     2:"星期三",
     3:"星期四",
     4:"星期五",
     5:"星期六",
     6:"星期日",
   }
  return dict_weeks[tuple_time[6]]

# ....测试......
print(get_week(2019,5,25))


