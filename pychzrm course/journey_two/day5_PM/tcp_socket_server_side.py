"""
 tcp套接字编程   ：   服务端流程
    思路：逐步骤完成操作
    重点代码
"""

import socket  # 调用 套接字模块

# 创建套接字对象                 网络地址类型      套接字类型
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(("0.0.0.0", 8888))

# 监听套接字
sockfd.listen(888)


while True:
    print("waiting for connect...")
    try:
        # 等待处理客户端连接
        connfd, addr = sockfd.accept()
        print("connect from", addr)
    except KeyboardInterrupt:
        print("Server exit")
        break

    while True:
        #  接受客户端消息
        data = connfd.recv(1024)
        # 感知到对方断开时，结束连接
        if not data:
            break
        print("Message", data.decode())
        #  向客户端发送消息，返回消息需要为字节数
        n = connfd.send(b"hfnlswn")  # 英文传递字节数用b转换
        print("send %d bytes" % n)

    connfd.close()  # 断开客户端
# # 关闭套接字
sockfd.close()  # 断开客户端和客户端地址
