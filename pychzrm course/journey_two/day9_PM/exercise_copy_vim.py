# """
# fork拷贝文件 vs Process拷贝文件
# """
# # fork 创建子进程拷贝文件
# import os
# from time import sleep
#
# # 文件对象
# rjr = "./swn"
# # 获取文件大小
# size = os.path.getsize(rjr)
#
#
# def copy_vim1():
#     ops = open(rjr, "rb")
#     oph = open("./hfklswn", "w+")
#     number = size // 2
#     oph.write(ops.read(number).decode())
#
#
# def copy_vim2():
#     ops = open(rjr, "rb")
#     oph = open("./swnlhfk", "w+")
#     ops.seek(size // 2, 0)
#     oph.write(ops.read().decode())
#
#
# # 创建新的进程
# pid = os.fork()
#
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     copy_vim1()
# else:
#     copy_vim2()

# process 创建子进程拷贝文件
from multiprocessing import Process
from multiprocessing import Pool
import os

# 创建文件对象
rjr = "./rjr"

# 获取文件大小
size = os.path.getsize(rjr)


def copy_vim1():
    ops = open(rjr, "rb")
    oph = open("hfklrjr", "w+")
    number = size // 2
    oph.write(ops.read(number).decode())
    ops.close()
    oph.close()

def copy_vim2():
    ops = open(rjr, "rb")
    oph = open("rjrlhfk", "w+")
    number = size // 2
    ops.seek(number, 0)
    oph.write(ops.read().decode())
    ops.close()
    oph.close()

list01 = [copy_vim1,copy_vim2]
list02 = []
# 创建进程对象
for i in list01:
    p = Process(target=i)
    # 启动子进程
    p.start()
    list02.append(p) # 将进程对象结果保存在列表


# 父进程一起回收子进程
for i in list02:
    i.join()


