"""
thread_server 基于线程的网络并发
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
    data = c.recv(1024)
    if not data:
      break
    print(data.decode())
    c.send(b'OK')
  c.close()

s = socket()  # tcp套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

print("Listen the port %d..."%PORT)
# 循环等待客户端连接
while True:
  try:
    c,addr = s.accept()
  except KeyboardInterrupt:
    sys.exit("服务器退出")
  except Exception as e:
    print(e)
    continue

  # 创建线程处理客户端请求
  t = Thread(target=handle,args=(c,))
  t.setDaemon(True)
  t.start()






