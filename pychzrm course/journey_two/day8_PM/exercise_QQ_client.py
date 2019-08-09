"""
    客户端
"""

# 调用 socket , os , sys 模块
from socket import *
import os, sys

# 命名服务端地址
ADDR = ("127.0.0.1", 8888)


# 发送消息
def send_msg(sockfd, name):
    while True:
        try:
            text = input("开泡:")
        except KeyboardInterrupt:
            text = "quit"
        # 退出
        if text.strip() == "quit":
            msg = "Q " + name
            sockfd.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        sockfd.sendto(msg.encode(), ADDR)


# 接受消息
def resv_msg(sockfd):
    while True:
        try:
            data, addr = sockfd.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 服务器发送EXIT退出
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\n开泡：", end="")


# 启动客户端
def main():
    # 创建UDP套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("name>>>")
        msg = "L " + name
        sockfd.sendto(msg.encode(), ADDR)
        # 等待反馈
        data, addr = sockfd.recvfrom(1024)
        if data.decode() == "OK":
            print("\n欢迎" + name + "进入泡泡")
            break
        else:
            print(data.decode())
    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Eroor!")
    elif pid == 0:
        send_msg(sockfd, name)
    else:
        resv_msg(sockfd)


if __name__ == "__main__":
    main()
