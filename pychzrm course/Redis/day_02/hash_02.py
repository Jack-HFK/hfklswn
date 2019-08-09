"""
设置一个字段更改一个字段，设置多个字段，获取相关信息
"""
import redis

r = redis.Redis(host="127.0.0.1",port=6379,db=0)

# 设置
r.hset("user1","name","bujingyun")
# 更新
r.hset("user1","name","niefeng")
# 取数据
print(r.hget("user1","name"))
# 设置多个字段和值
dicts = {"name":"hfk","age":"25","height":"158"}
r.hmset("user2",dicts)
# r.hmset("user2","name" "hfk" "age" "25" "height" "158")
# 取多个字段
r.hmget("user2","name","age","height")
# 获取所有数据，字典
r.hvals("user2")

