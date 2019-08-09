"""
poll IO 服务端程序

你的代码需要别人给你条件执行时          rlist
自己主动执行自己的代码，不需要被人下达指令   wlist
思路分析

poll_server 步骤
创建套接字
将套接字register
创建查找字典,并维护（要时刻与注意注册的IO保持一致）
循环监控IO发生
处理发生的IO
"""
from select import *
from socket import *

# 创建套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(6)

# 创建POOL 对象关注sockfd
p = poll()

# 建立查找字典，用于fileno通过查找IO对象
fdmap = {sockfd.fileno(): sockfd}

# 关注对象
p.regiter(sockfd, POLLIN | POLLERR)

# 循环监控
while True:
    # 阻塞等待IO事件的发生
    events = p.poll()
    # 循环遍历发送的事件  fd 为文件描述符fileno
    for fd, event in events:
        if fd == sockfd.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from")
            # 添加新的关注IO
            p.regiter(c, POLLIN | POLLERR)
            # 字典添加新的IO 维护字典
            fdmap[c.fileno()] = c
        # 按位与 判断是 POLLIN就绪
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                # 取消关注
                p.unregister(fd)
                # 关闭fd的套接字连接
                fdmap[fd].close()
                # 删除fd在字典中的关注
                del fdmap[fd]
                # 跳出for循环
                continue
            print("Recevive:", data.decode())
            fdmap[fd].send(b"ok")
