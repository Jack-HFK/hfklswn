"""
示 例： 更改mysql数据库数据，同步到redis数据库
"""
import redis
import pymysql

# 创建mysql连接
msdb = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456",
                       charset="utf8",
                       database="redis")

# 创建redis连接
rdb = redis.Redis(host="localhost", port=6379, db=0)

# 更新MySQL数据库
def update_mysql(age,username):
    # 创建mysql游标对象
    cursor = msdb.cursor()
    upd = "update user set age=%s where username=%s"
    try:
        # code 1 或 0
        code = cursor.execute(upd,[age,username])
        print(code)
        # 提交到数据库
        msdb.commit()
        if code == 1:
            return True
    except Exception as e:
        print("error:",e)
        msdb.rollback()  # 回滚
    # 关闭游标对象
    cursor.close()
    # 关闭数据库连接
    msdb.close()


# 更新Redis数据库
def update_redis(age):
    rdb.hset("user","age",age)
    print("已经同步到Redis")
    # 设置过期时间
    rdb.expire("suer",3)


if __name__ == "__main__":
    username = input("请输入用户名")
    age = input("请输入更改后的年龄")
    if update_mysql(age,username):
        update_redis(age)
    else:
        print("用户名有误")