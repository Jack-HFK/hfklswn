"""
Redis返回结果都是字节串(bytes)类型
"""
import redis

# 创建连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
print(r.keys("*"))  # [b'spider', b'swn', b'hfk']
print(r.keys("swn"))  # [b'spider', b'swn', b'hfk']

key_list = r.keys("*")
for key in key_list:
    print(key.decode())  # spider  swn   hfk

print(r.type("hfk"))  # b'list'   :字节串列表
print(r.exists("hfk"))  # 返回值：0 或者 1
print(r.delete("hfk"))  # 删除 key : hfk
