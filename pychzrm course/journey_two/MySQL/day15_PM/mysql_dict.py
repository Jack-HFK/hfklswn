"""
    mysql数据库添加字典操作练习
"""
# 调用 python mysql
import pymysql
import re

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="stu",
                     charset="utf8")
# 获取游标(用于进项数据操作的对象，承载操作结果)
cur = db.cursor()

while True:
    # 打开文件
    dict = open("/home/tarena/dict.txt", "r")
    for line in dict:
        word = re.findall(r"(\S+)\s+(.*)", line)[0]
        mean = re.findall(r"(\S+)\s+(.*)", line)[1:]

    # 执行SQL语句
    try:

        # 可以执行多个sql语句，同commit一同提交
        sql = "insert into dict(word,mean) values('%s','s%');" % (word, mean)

        # 执行sql语句
        cur.execute(sql)  # 传参方式

        # 将写操作交到数据库
        db.commit()
    except Exception as e:
        # 退回到commit之前的状态
        db.rollback()
        print(e)

# 关闭游标对象
cur.close()
# 关闭数据库
db.close()
