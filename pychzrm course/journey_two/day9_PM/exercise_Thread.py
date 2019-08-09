"""
    线程Thread
"""
from multiprocessing import Process
import threading
from time import sleep
import os
a = 1
# 主进程函数
def musics():
    a = 100
    for i in range(3):
        sleep(1)
        print(os.getpid(),"爱江山更爱美人")
        print(a)
# 线程函数
def music():
    a = 10000
    for i in range(3):
        sleep(1)
        print(os.getpid(),"九九女儿红")
        print(a)
# 创建线程对象
t = threading.Thread(target=music)

# 启动线程
t.start()

#回收线程
t.join()

print(a)

p = Process(target=musics)
p.start()
p.join()

