"""
    ftp文件服务器 服务端
    1.技术点分析
        * 并发模型 多线程网络并发模型
        * 网络传输 TCP传输
    2.结构设计
        * 客户端发送请求--> 界面
        list    get filename    put filename
        * 服务端 类封装
    3.功能模块
        * 网络并发结构
        * 查看文件列表
        * 下载文件
        * 上传文件
        * 退出
    4.协议设定
        * 文件列表查看：只提供普通文件（非隐藏文件）
        * 客户端请求类型：L 请求文件列表
                       G filename 下载文件
                       P filename 上传文件
                       Q 退出

    1：接受请求，识别请求，执行请求
    2：查看文件列表：识别请求，读取文件，发送文件
    3：下载文件   ：识别请求，读取文件，发送文件
    4：上传文件   ：识别请求，读取文件，保存文件
"""
from threading import Thread
from socket import *
import os
import time

# 全局变量
HOST = "0.0.0.0"  # 地址
PORT = 8888
ADDR = (HOST, PORT)
FTP = "/home/tarena/ftp/"  # 文件库位置


# 创建文件服务器服务端功能类
class FTPServer(Thread):
    def __init__(self, connfd):
        # 加载父类属性
        super().__init__()
        self.connfd = connfd

    # 接收请求发送文件列表
    def do_list(self):
        # 获取文件名称列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("空空如也".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1) # 防止和后面发送的内容粘包

        # 拼接文件列表
        files_ = ""
        for file in files:
            # 判断文件是否为私有文件 和 判断文件类型：内容是否为空
            if file[0] != "." and os.path.isfile(FTP + file):
                # 列表名称内容换行显示
                files_ += file + "\n"
                # 字符串装换字节串 发送客户端
        self.connfd.send(files_.encode())

    # 下载文件
    def do_get(self, filename):
        try:
            fd = open(FTP + filename, "rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(1)
        # 文件发送
        while True:
            data = fd.read(2048)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件名重复".encode())
            return

        self.connfd.send(b"ok")
        data_name = open(FTP + filename, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            data_name.write(data)
        data_name.close()
    def do_puts(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件名重复".encode())
            return
        self.connfd.send(b"ok")
        f = open(FTP + filename, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()


    # 循环接受客户端请求
    def run(self):
        while True:
            # 接收客户端发送的内容    接收内容大小 字节串转换为字符串
            data = self.connfd.recv(1024).decode()
            if data[0] == "Q":
                return
            elif data == "L":
                self.do_list()
            elif data[0] == "G":  # G filename
                filename = data.split(" ")[-1]
                self.do_get(filename)
            elif data[0] == "P":
                filename = data.split(" ")[-1]
                self.do_put(filename)
            else:
                print(data + "请求不能识别")


# 网络搭建
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # SO_REUSEADDR 端口号断开后立即重连
    sockfd.bind(ADDR)
    sockfd.listen(3)
    print("Listen the port %d" % PORT)
    while True:
        try:
            # 阻塞等待客户端请求，connfd:客户端连接套接字
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("服务器程序退出")
            return
        except Exception as e:
            print(e)
            continue

        # 创建新的线程处理客户端请求
        client = FTPServer(connfd)
        # setDaemon设置daemon属性daemon为True时主线程退出分支线程也退出
        client.setDaemon(True)
        # 运行 run 方法
        client.start()


if __name__ == "__main__":
    main()
