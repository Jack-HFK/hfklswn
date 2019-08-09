"""
    发送广播
"""
from  socket import *
import time

# 广播地址


sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
dest = ("172.40.74.255",9999)

data = "老妹儿广场舞走起\n" \
       "老头儿你干嘛？\n"\
       "放下那个老太。。。。"
while True:
    time.sleep(2)
    sockfd.sendto(data.encode(),dest)



sockfd.close()