"""
    mysql数据库写操作练习
    *增删改查修改操作
"""
# 调用 python mysql
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="stu",
                     charset="utf8")
# 获取游标(用于进项数据操作的对象，承载操作结果)
cur = db.cursor()

# 执行SQL语句
# 游标方法 \ 参数 填写sql语句
try:
    #可以执行多个sql语句，同commit一同提交
    sql = "update student set age=996 where name = '深咖啡';"

    # 执行sql语句
    cur.execute(sql)      # 传参方式

    # 将写操作交到数据库
    db.commit()
except Exception as e :
    # 退回到commit之前的状态
    db.rollback()
    print(e)



# 关闭游标对象
cur.close()
# 关闭数据库
db.close()
