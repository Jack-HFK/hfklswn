"""
 seleck tcp 服务模型
 你的代码需要别人给你条件执行时          rlist     长时间等待
自己主动执行自己的代码，不需要被人下达指令   wlist   直接执行

思路分析：
    【1】 将关注的IO放入对应的监控类别列表
    【2】通过select函数进行监控
    【3】遍历select返回值列表,确定就绪IO事件
    【4】处理发生的IO事件
"""

from select import select
from socket import *
import os

# 创建一个监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 设置关注列表  列表中添加的为IO操作的对象
rlist = [s]
wlist = []
xlist = []

# 循环监控，循环提取准备就绪的IO事件，循环执行IO事件
while True:
    # 监控IO
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历3个返回列表
    for r in rs:
        # 根据遍历到IO的不同使用,if分情况处理不同的操作
        if r is s:
            c, addr = s.accept()
            print("Connect from", addr)
            rlist.append(c)  # 增加新的IO事件
        else:
            data = r.recv(1024)
            if not data:
                # 执行完 r IO事件,从列表中删除，防止列表中下次继续执行它
                rlist.remove(r)
                r.cloce()
                continue
            print("Receive:", data.decode())
            # r.send(b"ok")
            # wlist主动处理IO对象
            wlist.append(r)
    for w in ws:
        w.send(b"ok")
        # 执行完 w IO事件,从列表中删除，防止列表中下次继续执行它
        wlist.remove(w)
    for x in xs:
        pass
