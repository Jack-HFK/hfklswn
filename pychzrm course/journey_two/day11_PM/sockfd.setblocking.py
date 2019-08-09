"""
sockfd.setblocking() 套接字阻塞行为转换
"""
from socket import *
from time import sleep,ctime

# 日志文件
f = open("/home/tarena/ftp","a+")


# 创建套接字对象
socket = socket(AF_INET,SOL_SOCKET)
# 设置端口号重连时间
socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 绑定地址
socket.bind(("127.0.0.1",8888))
# 设置监听
socket.listen(8)
# # 套接字阻塞行为转换为非阻塞
# socket.setblocking(False)
# 超时检测
socket.settimeout(3)

while True:
    print("Waiting for connect...")
    try:
        # 非阻塞等待连接
        connfd,addr = socket.accept()
    except (BlockingIOError,timeout) as e:
        # 如果没有客户端连接，每隔3秒写一个日志
        f.write("%s : %s\n"%(ctime(),e))
        sleep(6)
    else:
        print("连接成功")
        data = connfd.recv(1024).decode()
        print(data)