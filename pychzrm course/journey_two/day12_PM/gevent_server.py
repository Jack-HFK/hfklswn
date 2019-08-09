"""
    genvet 协程
"""

import  gevent
from  gevent import monkey
# 在导入socket模块前执行
monkey.patch_all()
from socket import *

def handle():
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("未得女子青睐".encode())
    c.close()


# 创建TCP套接字
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(8)
while True:
    # 阻塞等待连接
    c,addr = s.accept()
    print("小爷我不才")
    gevent.spawn(handle,c)

s.close()