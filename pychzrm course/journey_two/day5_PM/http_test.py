"""
    http 超文本传输协议
"""

from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(3)
c, addr = sockfd.accept()
print("connect from", addr)
data = c.recv(1024)
print(data)

datas = """HTTP/1.1 200 ok
content-type:text/html
<h1>hello world</hi>"""

c.send(datas.encode())

c.close()
sockfd.close()
