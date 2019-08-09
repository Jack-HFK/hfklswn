"""
multiprocessing 示例
"""

import multiprocessing as mp
from time import sleep

a = 100


def fun():
    print("开始一个新的进程")
    sleep(5)
    global a
    a = 10000
    print("子进程结束了")


# 创建进程对象
p = mp.Process(target=fun)
p.start()  # 启动进程
sleep(2)
print("父进程工作")
p.join(1)  # 回收进程
print("a:", a)
