import redis

r = redis.Redis(host="127.0.0.1",port=6379,db=0)

# user1 :　设置user1一年中的第5天和200天登录
r.setbit("user1",4,1)
r.setbit("user1",199,1)
# user2 :　设置user2一年中的第100天和300天登录
r.setbit("user2",99,1)
r.setbit("user2",299,1)
# user3 :　设置user3一年中登录了100天以上
for i in range(1,366,2):
    r.setbit("user3",i,1)
# user4 :　设置user4一年中登录了100天以上
for i in range(1,366,3):
    r.setbit("user4",i,1)

# 获取所有的键
user_list = r.keys("user*")
# 存放活跃用户
active_user = []
# 存放不活跃用户
no_active_user = []
for user in user_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_user.append((user,login_count))
    else:
        no_active_user.append((user,login_count))

for user in active_user:
    for i in user:
        print("活跃用户：%s,活跃次数：%s"%(user[0],user[1]))

for user in no_active_user:
        print("不活跃用户：%s,活跃次数：%s"%(user[0],user[1]))