"""
    pool 进程池拷贝文件
"""

from multiprocessing import Pool
import os

swn = "./swn"
# 获取文件的大小
size = os.path.getsize(swn)

def copy_vim1():
    s = open(swn,"rb")
    h = open("./hfklmn","w+")
    n = size//2
    h.write(s.read(n).decode())

def copy_vim2():
    s = open(swn,"rb")
    h = open("./mnlhfk","w+")
    s.seek(size//2,0)
    h.write(s.read().decode())

list01 = [copy_vim1,copy_vim2]

# 创建进程池对象
pool = Pool(996)

# 将事件加入进程池
for i in list01:
    pool.apply_async(i)

# 关闭进程池
pool.close()

# 回收子进程
pool.join()
