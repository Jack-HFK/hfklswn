import redis


rdb = redis.Redis(host="localhost",port=6379,db=0)

rdb.zadd("ranking",{"song1":1,"song2":1,"song3":1,"song4":1,})
rdb.zadd("ranking",{"song5":1,"song6":1,"song7":1,"song8":1,})
# 指定成员增加分值
rdb.zincrby("ranking",50,"song3")
rdb.zincrby("ranking",60,"song5")
rdb.zincrby("ranking",70,"song8")
# 获取分值前三名 降序
rlist = rdb.zrevrange("ranking",0,2,withscores=True)
print(rlist) # [(b'song8', 71.0), (b'song5', 61.0), (b'song3', 51.0)]

i = 1
for name in rlist:
    # 第1名：song8 播放次数70
    # 第2名：song5 播放次数60
    # 第3名：song3 播放次数50
    l = "第{}名:{} 播放次数{}".format(i,name[0].decode(),int(name[1]))
    print(l)
    i += 1