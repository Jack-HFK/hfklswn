"""
    mysql数据库写操作练习
    *增删改为写操作
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
    name = input("name:")
    age = int(input("age:"))
    swx = input("swx:")
    score = float(input("score:"))
                                                            # 传参方式
    # sql = "insert into student(name,age,swx,score) values ('%s',%d,'%s',%f);"%(name,age,swx,score)
    sql = "insert into student(name,age,swx,score) values ('%s',%s,'%s',%s);"

    # 执行sql语句
    # cur.execute(sql)      # 传参方式
    cur.execute(sql,[name,age,swx,score])  # 列表定死传参，建议只使用在插入方法

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
