"""
multiprocessing 示例2

multiprocessing 创建的子进程无法使用标准输入：比如input()函数
                父进程能可以使用标准输入
"""

from multiprocessing import Process as p
from time import sleep
import os


def th1():
    sleep(2)
    print("奔跑")
    print(os.getppid(), "////", os.getpid())


def th2():
    sleep(3)
    print("喝酒")
    print(os.getppid(), "////", os.getpid())


def th3():
    sleep(4)
    print("逛窑子")
    print(os.getppid(), "////", os.getpid())


things = [th1, th2, th3]
jobs = []
for th in things:
    paa = p(target=th)
    paa.start()
    jobs.append(paa)  # 将进程对象保存在列表
#  一起回收
for i in jobs:
    i.join()
