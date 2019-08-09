"""
mysql数据库写操作练习
* 增删改为写操作
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
try:
  # 插入数据
  # name = input("name:")
  # age = int(input('age:'))
  # gender = input('gender:')
  # score = float(input('score:'))

  # sql = "insert into student (name,age,gender,score) \
  #       values ('%s',%d,'%s',%f)"%(name,age,gender,score)

  # sql = "insert into student (name,age,gender,score) \
  #         values (%s,%s,%s,%s)"

#   sql = "insert into interest values \
# (3,'Joy','draw','B',5488.0,'画的鸡蛋还行')"
#   cur.execute(sql,[name,age,gender,score])

  # 修改操作
#   sql = "update student set age=22 \
# where name = 'Lily'"
#   cur.execute(sql)

  # 删除操作
  sql = "delete from student where score<60"
  cur.execute(sql)

  db.commit()  # 可以执行多个sql语句一同提交
except Exception as e:
  db.rollback() # 退回到commit之前的状态
  print(e)

# 关闭数据库
cur.close()
db.close()








