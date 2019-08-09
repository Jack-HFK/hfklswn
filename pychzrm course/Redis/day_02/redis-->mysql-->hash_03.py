import pymysql
import redis

# 1.步骤一 先到到redis缓存中查询个人信息
# 2.步骤二 redis中查询不到，到mysql查询，返回数据到客户端并缓存到redis
# 3.步骤三 在一定时间内，再次查询个人信息，直接到redis缓存中查询。

# 创建mysql连接
msdb = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456",
                       charset="utf8",
                       database="redis")

# 创建redis连接
rdb = redis.Redis(host="localhost", port=6379, db=0)

while True:
    username = input("请输入查询的用户名")

    result = rdb.hgetall("user")
    if result:
        print("获取了redis的数据库",result)
    else:
        # 创建mysql游标对象
        cursor = msdb.cursor()
        sele = "select username,age,gender,password from user where username=%s"
        cursor.execute(sele, [username])
        # userinfo 获取所有数据
        userinfo = cursor.fetchall()
        if not userinfo:
            print("用户不存在")
        else:
            # 获取并打印数据
            print(userinfo)
            # 将数据缓存到 Redis
            user_dict = {
                "username": userinfo[0][0],
                "age": userinfo[0][1],
                "gender": userinfo[0][2],
                "password": userinfo[0][3],
            }
            rdb.hmset("user", user_dict)

            rdb.expire("user", 3)
