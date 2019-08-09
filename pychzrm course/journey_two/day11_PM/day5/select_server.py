"""
select tcp服务模型
重点代码

思路分析：
1.将关注的IO放入对应的监控类别列表
2.通过select函数进行监控
3.遍历select返回值列表，确定就绪IO事件
4.处理发生的IO事件
"""

from socket import *
from select import select

#　创建一个监听套接字作为关注的ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#　设置关注列表
rlist = [s]
wlist = []
xlist = [s]

#　循环监控ＩＯ
while True:
  rs,ws,xs = select(rlist,wlist,xlist)
  # 遍历三个返回列表,处理ＩＯ
  for r in rs:
    # 根据遍历到ＩＯ的不同使用ｉｆ分情况处理
    if r is s:
      c,addr = r.accept()
      print("Connect from",addr)
      rlist.append(c) #　增加新的ＩＯ事件
    # else为客户端套接字就绪情况
    else:
      data = r.recv(1024)
      # 客户端退出
      if not data:
        rlist.remove(r) #　从关注列表移除
        r.close()
        continue # 继续处理其他就绪ＩＯ
      print("Receive:",data.decode())
      # r.send(b'OK')
      #　我们希望主动处理这个ＩＯ对象
      wlist.append(r)

  for w in ws:
    w.send(b'OK')
    wlist.remove(w) #　使用后移除

  for x in xs:
    pass




