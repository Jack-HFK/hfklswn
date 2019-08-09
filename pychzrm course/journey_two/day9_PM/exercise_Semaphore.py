"""
进程信号量通信Semaphore
"""

from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量，最多允许三个任务同时执行
hfk = Semaphore(3)


# 任务函数
def handle():
    # 想执行必须消耗一个信号量
    hfk.acquire()
    print("%d 执行任务" % os.getpid())
    sleep(2)
    print("%d 执行任务完毕" % os.getpid())
    # 增加信号量
    hfk.release()


# 10 人想执行
for i in range(10):
    p = Process(target=handle)
    p.start()

p.join()
