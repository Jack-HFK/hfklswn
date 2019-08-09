"""
http server
部分功能 的主程序
"""

from socket import *  # 套接字模块
from threading import Thread # 线程模块
from config import *  # 配置模块（自创）
import re  # 正则表达式
import json  # 隐藏输入模块

#　服务器地址
ADDR = (HOST,PORT)

class HTTPServer:
    def __init__(self):
        self.adress = ADDR
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket() # 创建套接字对象
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG) # SO_REUSEADDR　socket关闭后本地断开可以立即重用

    # 绑定地址
    def bind(self):
        self.sockfd.bind(ADDR)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(8) # 设置监听队列大小
        while True:
            connfd,addr = self.sockfd.accept() # 循环等待连接
            client = Thread(target=self.handle,args=(connfd,)) # 创建线程绑定给handle函数，把接受内容传给函数，线程函数处理接受的信息
            client.setDaemon(True) # 设置主线程退出分支线程也退出
            client.start() # 启动线程
    # 处理浏览器请求
    def handle(self,connfd):
        request = connfd.recv(4096).decode() # 接收消息内容
        # 获取请求行
        pattren = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)" # 获取请求类型为捕获组method，请求内容，协议类型为捕获组info
        try:
            # match 获取请求内容开始部分
            env = re.match(pattren,request).groupdict() # groupdict 以捕获组组名为键，请求内容为值，组成捕获组词典
        except:
            connfd.colose()
            return



# 实例化类对象
httpd = HTTPServer()
# 启动程序
httpd.serve_forever

