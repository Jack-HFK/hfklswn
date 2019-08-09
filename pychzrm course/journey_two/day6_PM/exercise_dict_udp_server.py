"""
    udp 套接字编程
        服务端
"""

from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ("172.40.74.151", 8888)
sockfd.bind(server_addr)


# 打开文件
def find_word(dict01):
    fd = open("/home/tarena/dict.txt", "r")
    # 遍历的单词已经大于目标
    for line in fd:
        tmp = line.split(" ")[0]
        if tmp > dict01:
            return ("欧巴内有")
        elif dict01 == tmp:
            return line
    else:
        raise Exception("妹有呦")


# 收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    str_data = data.decode()
    if data == "死吧你":
        break
    datas = find_word(str_data)
    sockfd.sendto(datas.encode(), addr)

# 关闭套接字
sockfd.close()
