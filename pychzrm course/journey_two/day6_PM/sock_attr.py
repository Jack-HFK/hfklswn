"""
    socket 套接字属性
"""

from socket import *

# 创建TCP套接字
sockfd = socket()

# 设置套接字端口立即重用   socket断开直接重新连接
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 绑定连接
sockfd.bind("0.0.0.0", 6666)
# 设置监听
sockfd.listen(3)

c, adrr = sockfd.accept()

# 获取套接字类型
print("套接字类型", sockfd.type)

# 获取地址类型
print("地址类型", sockfd.family)

# 获取文件描述符
print("获取文件描述符", sockfd.fileno())

# 获取选项值
print("获取选项值", sockfd.getsockopt(SOL_SOCKET, SO_REUSEADDR))

# 获取套接字绑定的地址
print("套接字绑定地址", sockfd.getsockname())

# 获取连接套接字客户端地址
print("绑定套接字的客户端地址", sockfd.getpeername())
