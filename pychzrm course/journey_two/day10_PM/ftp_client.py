"""
    ftp 文件服务器客户端
"""
from socket import *
import sys
import time

# 服务器地址
ADDR = ("127.0.0.1", 8888)


# 客户端功能处理类
class FTPClient():
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        # 发送请求
        self.sockfd.send(b"L")
        # 等待回复
        data = self.sockfd.recv(4096).decode()
        if data == "ok":
            # 一次接收完文件列表字符串
            data = self.sockfd.recv(8192)
            print(data.decode())  # 字节串转换字符串
        else:
            print(data)

    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(("G " + filename).encode())
        # 等待回复
        data = self.sockfd.recv(8192).decode()
        if data == "ok":
            fd = open("./" + filename, "wb")
            # 接收文件
            while True:
                data = self.sockfd.recv(8192)
                if data == b"##":
                    break
                else:
                    fd.write(data)
            fd.close()
        else:
            print(data)

    def do_put(self, filename):
        try:
            fd = open(filename,"rb")
        except Exception:
            print("文件不存在")
            return
        # 获取文件名
        filename = filename.split("/")[-1]
        # 发送请求
        self.sockfd.send(("P"+ filename).encode())
        # 等待回复
        data = self.sockfd.recv(8192).decode()
        if data == "ok":
            while True:
                data = fd.read()
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fd.close()
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit("下次再会！")


# 创建客户端网络
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp = FTPClient(sockfd)  # 实例化类对象

    # 循环发送请求
    while True:
        print("\n***********命令选项***********")
        print("  ****       list      ****")
        print("  ****     get file    ****")
        print("  ****     put file    ****")
        print("  ****       quit      ****")
        print("******************************")

        cmd = input("请输入命令：")

        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.strip().split(" ")[-1]
            ftp.do_put(filename)
        elif cmd.strip() == "quit":
            ftp.do_quit()
        else:
            print("请输入正确指令")


if __name__ == "__main__":
    main()
