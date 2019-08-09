import pymysql



class Pymysql:
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "123456"
        self.database = "hfklswn"
        self.charset = "utf8"

        self.db() # 建立起数据库连接

    # 建立数据库连接
    def connect(self):
        self.db = pymysql.connect(self.host,
                             self.port,
                             self.user,
                             self.password,
                             self.database,
                             self.charset)
    # 建立游标对象
    def cursor(self):
        # 返回游标对象用于执行SQL语句
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.db.close()