"""
    udp 套接字编程
        客户端
"""
from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 服务端地址
ADDR = ("172.40.74.151",8888)

# 收发消息
while True:
    data = input("word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("from server",msg.decode())

# 关闭套接字
sockfd.close()

