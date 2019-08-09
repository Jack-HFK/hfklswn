from socket import *
from multiprocessing import Process
import sys
import signal

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

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

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

  # 创建进程处理客户端请求
  p = Process(target=handle,args=(c,))
  p.daemon = True
  p.start()






