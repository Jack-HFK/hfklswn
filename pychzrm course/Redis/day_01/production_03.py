import redis
import time
import random


# 创建连接对象
r = redis.Redis(host='localhost',port=6379,db=0)

# 生产者开始生产URL地址
for page in range(0,67):
    url = "http://app.mi.com/category/2#page=%s" % str(page)
    r.lpush("hfk:url",url)
    print(url)
    time.sleep(random.randint(1,3))  # 等待时间随机1到3秒，执行一次
