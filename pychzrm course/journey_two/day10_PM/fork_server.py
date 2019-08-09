"""
    基于fork搭建基础网络并发模型

    1，每当有一个客户端就创建一个新的进程,作为客户端处理进程
    2，客户端如果结束，对应程序应该销毁
"""

from socket import *
import os
import signal

# 创建监听套接字

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(3)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port %d" % PORT)


def handle(c):
    while True:
        data =c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
        c.close()
# 循环等待连接
while True:
    try:
        c, addr = sockfd.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception  as e:
        print(e)
        continue


    # 创建子进程处理这个客户端
    pid = os.fork()
    if pid == 0:
        # 关闭套接字
        sockfd.close()
        handle(c)  # handle处理完客户端请求，子进程也退出程序
        os._exit(0)
    # else:   # 无论出差或者父进程都要循环回去接受请求
    #     pass
    # c对于父进程没有用
    c.close()
