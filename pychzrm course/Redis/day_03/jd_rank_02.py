import redis

rdb = redis.Redis(host="localhost",port=6379,db=0)

# mobile_001

day01_dict = {"huawei":5200,"oppo":4900,"iphone":200}
day02_dict = {"huawei":6200,"oppo":6900,"iphone":300}
day03_dict = {"huawei":7200,"oppo":8900,"iphone":500}

rdb.zadd("mobile-001",day01_dict)
rdb.zadd("mobile-002",day02_dict)
rdb.zadd("mobile-003",day03_dict)

# 并集
rdb.zunionstore("mobile-001:003",
                ("mobile-001","mobile-002","mobile-003"),
                aggregate="max")
# 逆序 [(),(),()]
rlist = rdb.zrevrange("mobile-001:003",0,2,withscores=True)

for r in rlist:
    print("{}-{}".format(r[0].decode(),int(r[1])))

