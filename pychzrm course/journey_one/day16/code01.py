"""
  标准库模块
    -- 时间
  练习:fork_server.py
"""
import time

# 1558401657.2616878
# 1558401669.6721954
# 时间戳:从1970年后经过的秒数
print(time.time())
# 时间戳 --> 时间元组
#年    月    日   时   分  秒  星期(周一0  周二1 ... 周日6)  一年的第几天   夏令时
tuple_time = time.localtime(1558401657.2616878)
print(tuple_time)
# 时间元组 --> str
# 年/月/日 小时:分钟:秒
print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))
# str --> 时间元组
print(time.strptime("2019-05-21","%Y-%m-%d"))
# 时间元组  --> 时间戳
print(time.mktime(tuple_time))













