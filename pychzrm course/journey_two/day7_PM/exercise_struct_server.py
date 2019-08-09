"""
    UDP服务端
"""

from socket import *
import struct

# 创建 UDP 套接字 服务端
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(("127.0.0.1", 8888))

# 数据结构
st = struct.Struct("i32sif")

# 打开文件
f = open("student.txt", "a")

while True:
    data, addr = sockfd.recvfrom(1024)
    data = st.unpack(data)  # 解析数据

    # 整理数据
    info = "%d %-10s %d %.1f\n" % (data[0], data[1].decode(), data[2], data[3])
    f.write(info)
    f.flush()  # 不在缓冲区缓冲，直接写入磁盘。
# 关闭
f.close()
# 断开套接字
sockfd.close()
