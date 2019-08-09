import redis

# 创建连接对象
# r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# 创建连接对象
r = redis.Redis(host='localhost',port=6379,db=0)

# hfk : ["value3","value2","value1"]
r.lpush("hfk","value1","value2","value3")

# hfk : ["value3","value4","value2","value1"]
r.linsert("hfk","before","value2","value4")

# 4
print(r.llen("hfk"))

# [b'value3', b'value4', b'value2', b'value1']
print(r.lrange("hfk",0,-1))

# r.delete("hfk")

while True:
    #如果列表中为空时,返回None
    result = r.brpop("hfk",1)
    if result:
        print(result)
    else:
        break





