"""
 tcp_client套接字编程   ：   客户端流程
    思路：逐步骤完成操作
    重点代码
"""
from socket import *  # 调用 套接字模块

# 创建套接字对象 tcp套接字
sockfd = socket()  # tcp套接字参数默认值即为tcp套接字

#   链接服务端程序
server_addr = ("172.40.74.151", 8888)  # 服务端IP地址,端口号
sockfd.connect(server_addr)


# 消息发送接收
while True:
    data = input("Msg>>")
    # 如果什么不输入，直接回车，退出
    if not data:
        break
    sockfd.send(data.encode())  # 字符串转换字节串发送
    data = sockfd.recv(1024)
    print("啥东东",data)

# 关闭套接字,断开服务端连接
sockfd.close()