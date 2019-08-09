"""
pymysql 操作数据库基本流程
"""
# 调用 python mysql
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="Image",
                     charset="utf8")
# 获取游标(用于进项数据操作的对象，承载操作结果)
cur = db.cursor()

# 存储文件
with open("","rb") as fd:
    data = fd.read()


try:    # 执行SQL语句
        # 游标方法 \ 参数 填写sql语句
    sql = "insert into Image(1,'地址',%s ;"
    # 执行sql语句
    cur.execute(sql,[data])
    # 将写操作交到数据库
    db.commit()
except:
    db.rollback()
# 关闭游标对象
cur.close()
# 关闭数据库
db.close()