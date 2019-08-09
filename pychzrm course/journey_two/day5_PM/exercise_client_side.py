"""
客户端
"""
from socket import  *

sockfd = socket()

addr =("172.40.74.177",22222)
sockfd.connect(addr)
while True:

    obj = open("client", "rb+")
    sockfd.send((obj.name.split("/")[-1]).encode())
    data = sockfd.recv(1024)
    while data:
        data1 = obj.read(1024)
        if not data1:
            break
        sockfd.send(data1)




sockfd.close()
addr.close()



