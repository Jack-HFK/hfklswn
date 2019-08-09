"""
思路分析
1. 创建udp套接字
2. 循环接收内容
3. 将接收内容写入文件
"""

from socket import *
import struct

# udp
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 数据结构
st = struct.Struct("i32sif")

# 打开文件
f = open('student.txt','a')

while True:
  data,addr = s.recvfrom(1024)
  data = st.unpack(data) # 解析数据

  # 整理数据
  info = "%d   %-10s   %d   %.1f\n"%\
         (data[0],data[1].decode(),data[2],data[3])
  f.write(info)
  f.flush()

f.close()
s.close()








