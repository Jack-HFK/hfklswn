"""
chat room
env python3.5
socket udp fork
                            服务端
"""

# 调用socket() 函数 模块
from socket import *
import os, sys

# 命名地址对象
ADDR = ("0.0.0.0", 8888)

# 存储用户 {name:address}
user = {}


# 登录
def do_login(sockfd, name, addr):
    if name in user or "管理员" in name:
        sockfd.sendto("该用户已经存在".encode(), addr)
        return
    sockfd.sendto(b"OK", addr)

    # 通知其他人
    msg = "\n欢迎 %s 来到泡泡" % name
    for i in user:
        sockfd.sendto(msg.encode(), user[i])
    # 插入字典
    user[name] = addr


def do_chat(sockfd, name, text):
    msg = "\n%s : %s" % (name, text)
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(), user[i])


# 退出
def do_quit(sockfd, name):
    msg = "\n%s 退出了聊天室" % name
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(),user[i])
        else:
            sockfd.sendto(b"EXIT",user[i])
    # 删除字典
    del user[name]


# 循环接受客户端请求的函数
def do_request(sockfd):
    while True:
        # 循环接受客户端请求，绑定变量data
        data, addr = sockfd.recvfrom(1024)
        # 拆分请求内容
        tmp = data.decode().split(" ")
        # 根据客户端发送的请求内容，执行不同的内容
        if tmp[0] == "L":
            do_login(sockfd, tmp[1], addr)  # 完成服务端具体的登录工作
        elif tmp[0] == "C":
            text = " ".join(tmp[2:])  # 列表转换成字符串，元素拼接消息内容
            do_chat(sockfd, tmp[1], text)
        elif tmp[0] == "Q":
            # 如果服务器直接断开连接，字典内名字清空，发送消息退出，跳过
            if tmp[1] not in user:
                sockfd.sendto(b"EXIT",addr)
                continue
            do_quit(sockfd, tmp[1])


# 搭建UDP 网络
def main():
    # 创建 UDP套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    sockfd.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            sockfd.sendto(msg.encode(),ADDR)
    else:
        # 请求处理函数
        do_request(sockfd)


if __name__ == "__main__":
    main()
