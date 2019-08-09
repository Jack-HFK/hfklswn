"""
   管道通信 Pipe
"""

from multiprocessing import Process, Pipe
import os, time

# 创建双向管道对象
hfk, swn = Pipe(duplex=True)
# 创建单向管道
# hfk,swn = Pipe(duplex=False)

# 从管道获取内容
def read():
    while True:
        # 把内存中的管道空间里的内容读取出来
        data = hfk.recv()
        print(data)


# 从管道写入消息
def write():
    while True:
        time.sleep(1)
        # 向内存中的管道空间里写入内容
        swn.send("老王恋爱倒计时：" + time.ctime())  # ctime获取当前时间

# 创建进程对象
h = Process(target=read)
s = Process(target=write)
#运行进程
h.start()
s.start()
#回收子进程
h.join()
s.join()
