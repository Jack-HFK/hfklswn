"""
    进程消息队列通信
"""

from multiprocessing import Process, Queue
from time import sleep
from random import randint

# 创建消息队列对象
q = Queue(maxsize=5)


def request():
    for i in range(10):
        # 随机生成0到100的整数
        x = randint(0, 100)
        y = randint(0, 100)
        # 向队列存入消息
        print("----------")
        q.put((x, y))



def handle():
    while True:
        sleep(1)
        try:
            x, y = q.get(timeout=5)
        except:
            break
        else:
            print("%d + %d = %d" % (x, y, x + y))

# 创建进程
hfk = Process(target=request)
swn = Process(target=handle)
# 运行进程
hfk.start()
swn.start()
# 收回子进程
hfk.join()
swn.join()
