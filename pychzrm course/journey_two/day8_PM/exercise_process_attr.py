"""
进程对象属性
"""

from multiprocessing import Process
from time import sleep, ctime


def tm():
    for i in range(3):
        sleep(2)
        print(ctime())


p = Process(target=tm, name="Tedo")

# p.daemon = True # 子进程会随父进程退出

p.start()
print("name:", p.name)  # 名称
print("PID:", p.pid)  # PID
print("Is alive:", p.is_alive())  # 生命周期
