"""
block_io.py
socket 套接字非阻塞ＩＯ

如果没有客户端连接，每隔３秒填充一个日志
"""

from socket import *
from time import sleep,ctime

#　日志文件
f = open('log.txt','a+')

#　创建套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

#　设置超时检测时间
sockfd.settimeout(3)

while True:
  print("Waiting for connect...")
  try:
    connfd,addr = sockfd.accept()
  except (BlockingIOError,timeout) as e:
    #　如果没有客户端连接，每隔３秒写一个日志
    f.write("%s : %s\n"%(ctime(),e))
    f.flush()
    sleep(3)
  else:
    print("Connect from",addr)
    data = connfd.recv(1024).decode()
    print(data)





