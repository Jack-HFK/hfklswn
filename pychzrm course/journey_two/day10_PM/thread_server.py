"""
thread_server 基于线程的网络并发模型
重点代码

思路分析:
1. 基本与进程相同,只是换为线程处理客户端请求
2. 当主线程结束,同时终止所有对客户端的服务
"""

from socket import *
from threading import Thread
import sys

# 创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(c):
  while True:
    # 接受客户端内容，设定接受大小
    data = c.recv(1024)
    # 内容为空，结束
    if not data:
      break
    print(data.decode())  # 字节串转换字符串
    # 发送内容
    c.send(b'OK')
  # 关闭客户端
  c.close()
# 创建套接字
s = socket()  # tcp套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # SO_REUSEADDR 端口号断开后立即重用
# 绑定地址
s.bind(ADDR)
# 设置监听
s.listen(3)

print("Listen the port %d..."%PORT)
# 循环等待客户端连接
while True:
  try:
    # 阻塞等待客户端请求，c:客户端连接套接字
    c,addr = s.accept()
  except KeyboardInterrupt:
    sys.exit("服务器退出")
  except Exception as e:
    print(e)
    continue

  # 创建线程处理客户端请求
  t = Thread(target=handle,args=(c,))
  # setDaemon设置daemon属性daemon为True时主线程退出分支线程也退出
  t.setDaemon(True)
  # 启动线程
  t.start()

