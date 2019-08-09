import pymongo

# 连接对象
conn =pymongo.MongoClient(host="127.0.0.1",port=27017)

# 库对象
db =conn["maoyandb"]   # 连接数据库

# 集合对象
myset = db["filmtab"]

# 插入数据库
myset.insert_one({"name":"聂风"})  # 插入一条数据

