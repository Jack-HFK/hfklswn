"""
 进程共享内存通信 value
"""

from multiprocessing import Process,Value
import time
from random import randint

# 创建共享内存
money = Value("i",8000)

# 修改共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        # 修改共享内存中money属性的值
        money.value += randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        # 修改共享内存中money属性的值
        money.value -= randint(100,800)

# 创建进程对象
hfk = Process(target=man)
swn = Process(target=girl)

# 开始进程
hfk.start()
swn.start()

# 回收子进程
hfk.join()
swn.join()

# 获取共享内存
print("私房钱：",money.value)

