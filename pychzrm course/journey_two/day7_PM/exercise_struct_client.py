"""
从客户端循环输入信息包含编号（整形）姓名（字符串）年龄（整型），分数（浮点型）
发送的服务端
服务端将接受的内容写入一个文件中，每个学生信息占一行
"""

from socket import *
import struct

# 创建UDP套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ("127.0.0.1", 8888)

# 格式与服务端一致
st = struct.Struct("i32sif")

while True:
    id = int(input("请输入学生编号："))
    name = input("请输入学生姓名：").encode()
    age = int(input("请输入学生年龄："))
    score = float(input("请输入学生分数："))
    # 数据打包
    data = st.pack(id, name, age, score)
    # 发送
    sockfd.sendto(data, server_addr)

sockfd.close()
