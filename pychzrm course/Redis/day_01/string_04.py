import redis

# 创建redis对象
r = redis.Redis(host="127.0.0.1",port=6379,db=0)

# True
print(r.set("username","hfk"))
# b'hfk'
print(r.get("username"))

r.mset({"username":"swn","password":"123456"})
# [b'swn', b'123456'] 字节串列表
print(r.mget("username","password"))

# 3
print(r.strlen("username"))

# 数值操作
r.set("age",25)
r.incrby("age",10)
r.decrby("age",10)
r.incr("age",10)
r.decr("age",10)
r.incrbyfloat("age",3.3)
r.incrbyfloat("age",-3.3)
# b'25'
print(r.get("age"))

r.delete("username","password")