"""
1.将一个文件从客户端发到服务端，要求文件类型随意
2. tcp两个程序和函数熟练
"""
"""
 tcp套接字编程   ：   服务端流程
    思路：逐步骤完成操作
    重点代码
"""
import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.bind(("172.40.74.151", 4444))
# 设置监听
sockfd.listen(6666)

while True:
    try:
        # 等待处理客户端连接请求
        connfd, addr = sockfd.accept()
    except:
        raise Exception

    while True:
        # 接受 文件名，没有直接创建
        data_name = connfd.recv(1024)
        datas = data_name.decode()
        datas = open(datas, "wb+")
        # 回复消息
        connfd.send("开始把".encode())
        while data_name:
            # 接收客户端文件信息
            data = connfd.recv(1024)
            if not data:
                break
            data.decode()
            datas.write(data)
        if not data_name:
            break

    connfd.close()  # 断开客户端连接
# 关闭套接字
sockfd.close()  # 断开客户端和客户端地址
