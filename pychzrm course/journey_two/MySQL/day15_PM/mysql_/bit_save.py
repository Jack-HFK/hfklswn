"""
pymysql 存储二进制文件
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

# 存储文件
# with open('boy.jpg','rb') as fd:
#   data = fd.read()
#
# try:
#   sql="insert into Image values (1,'boy.jpg',%s)"
#   cur.execute(sql,[data])
#   db.commit()
# except Exception as e:
#   print(e)
#   db.rollback()

# 获取图片
sql = "select * from Image \
      where filename='boy.jpg'"
cur.execute(sql)

# (1,name,xxxxx)
img = cur.fetchone()
with open(img[1],'wb') as f:
  f.write(img[2])

# 关闭数据库
cur.close()
db.close()








