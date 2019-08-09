"""
pymysql 操作查询数据库
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
sql = "select * from student where swx='w';"

# 执行sql查询语句，cur便会拥有查询结果

# 查询结果 ，是可迭代的，不能三个方法一起查询
cur.execute(sql)
# 获取多个查询结果
# many_row =cur.fetchmany(2)
# print(many_row)
# # 获取全部查询结果
# all_row = cur.fetchall()
# print(all_row)
# # 获取一个查询结果
one_row = cur.fetchone()
print(one_row)

# 将写操作交到数据库
db.commit()

# 关闭游标对象
cur.close()
# 关闭数据库
db.close()