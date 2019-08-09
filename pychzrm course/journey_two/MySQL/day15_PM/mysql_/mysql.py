"""
pymysql 操作数据库基本流程
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
sql = "insert into student \
(name,age,gender,score) values \
('Lily',14,'w',79.5);"
cur.execute(sql)

db.commit() # 将写操作提交到数据库

# 关闭数据库
cur.close()
db.close()








