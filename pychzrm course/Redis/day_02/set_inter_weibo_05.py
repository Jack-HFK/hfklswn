import redis

rdb = redis.Redis(host="localhost",port=6379,db=0)

# user1关注的人
rdb.sadd("user1:focus","peiqi","qiaomu","haojian")
# user2关注的人
rdb.sadd("user2:focus","peiqi","qiaomu","atongmu")
# user共同关注的人,交集
foucus_set = rdb.sinter("user1:focus","user2:focus")

# 创建空集合，存放结果
sets = set()
for focus in foucus_set:
    sets.add(focus.decode())

print(sets)
