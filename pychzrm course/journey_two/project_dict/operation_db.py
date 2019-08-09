"""
dict 　数据库处理
功能：　提供服务端所有数据库操作

"""
import pymysql  # 隐藏输入
import hashlib  # 转换加密

SALT = "#&AID"  # 加密用的盐


class Database:
    def __init__(self, host="localhost",
                 port=3306,
                 user="root",
                 passwd="123456",
                 charset="utf8",
                 database="dict"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_db()  # 连接数据库

    # 建立数据库连接
    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset
                                  )

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.db.close()

    # 注册操作
    def register(self, name, passwd):
        sql = "select * from user where name = '%s'"%name
        self.cur.execute(sql) # 游标cur方法执行Sql语句
        r = self.cur.fetchone()  # 如果有查询结果则name存在
        if r:
            return False

        # 密码加密算法加盐
        hash = hashlib.md5((name + SALT).encode())  # 生成对象
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 提取加密密码
        sql = "insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd]) # 游标cur方法执行Sql语句[给sql传参]
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

        # 登录处理
    def login(self,name,passwd):
        # 算法加盐
        hash = hashlib.md5((name + SALT).encode())  # 生成对象
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 提取加密密码

        # 数据库查找
        sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def query(self,word):
        sql = "select mean from words where word= '%s'"%word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]

    def inser_history(self,name,word):
        sql= "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def history(self,name):
        sql = "select name,word,time from hist where name='%s' order by time desc limit 10"%name
        self.cur.execute(sql)
        return self.cur.fetchall()
