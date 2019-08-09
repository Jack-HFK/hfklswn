"""
    udp 套接字编程
        服务端
"""

# 创建套接字
from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ("172.40.74.151",8888)
sockfd.bind(server_addr)

# 收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print("收到的消息",data.decode())
    sockfd.sendto(b"love baby",addr)

# 关闭套接字
sockfd.close()



