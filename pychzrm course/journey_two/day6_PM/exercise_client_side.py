"""
客户端
"""
from socket import  *

sockfd = socket()

addr =("172.40.74.177",22222)
sockfd.connect(addr)
while True:

    obj = open("../www/a4e9efd077512c2e35d26f17d59cd6a5.jpg", "rb+")
    sockfd.send((obj.name.split("/")[-1]).encode())
    data = sockfd.recv(1024)
    while data:
        data1 = obj.read(1024)
        if not data1:
            break
        sockfd.send(data1)




sockfd.close()
addr.close()



