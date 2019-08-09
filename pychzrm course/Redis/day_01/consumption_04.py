import redis
import time
import random

# 创建连接对象
r = redis.Redis(host='localhost',port=6379,db=0)

while True:
    url = r.brpop("hfk",5)
    if url:
        # print(url)  # (b'hfk', b'value')
        print("正在抓取：",url[1].decode())
    else:
        print("抓取结束")
        r.delete("hfk")
        break
