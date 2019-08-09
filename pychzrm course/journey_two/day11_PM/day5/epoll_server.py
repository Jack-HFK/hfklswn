"""
epoll 服务端程序
尽量掌握
"""

from socket import *
from select import *

#　创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建eｐｏｌｌ对象关注ｓ
ep = epoll()

#　建立查找字典，用于通过ｆｉｌｅｎｏ查找ＩＯ对象
fdmap = {s.fileno():s}

# 关注ｓ
ep.register(s,EPOLLIN|EPOLLERR)

#　循环监控
while True:
  events = ep.poll()
  #　循环遍历发生的事件　ｆｄ-->fileno
  for fd,event in events:
    print("亲，你有ＩＯ需要处理哦")
    #　区分事件进行处理
    if fd == s.fileno():
      c,addr = fdmap[fd].accept()
      print("Connect from",addr)
      #　添加新的关注ＩＯ
      #　将触发方式变为边缘触发
      ep.register(c,EPOLLIN|EPOLLERR|EPOLLET)
      fdmap[c.fileno()] = c #　维护字典
    #　按位与判定是EＰＯＬＬＩＮ就绪
    # elif event & EPOLLIN:
    #   data = fdmap[fd].recv(1024)
    #   if not data:
    #     ep.unregister(fd) #　取消关注
    #     fdmap[fd].close()
    #     del fdmap[fd]  #　从字典中删除
    #     continue
    #   print("Receive:",data.decode())
    #   fdmap[fd].send(b'OK')




