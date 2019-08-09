"""
    接收广播
"""
from socket import *

# udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 让套接字接受广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 绑定地址
sockfd.bind(("172.40.74.255",9999))

while True:
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

sockfd.close()