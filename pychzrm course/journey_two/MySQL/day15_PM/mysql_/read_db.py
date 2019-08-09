"""
mysql数据库读操作演示
select语句
"""


import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')

# 获取游标(用于进行数据操作的对象,承载操作结果)
cur = db.cursor()

# 执行sql语句
sql = "select * from student where gender='m'"
cur.execute(sql) #执行查询后cur便会拥有查询结果

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)

# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)

# 获取全部查询结果
all_row = cur.fetchall()
print(all_row)


# 关闭数据库
cur.close()
db.close()








