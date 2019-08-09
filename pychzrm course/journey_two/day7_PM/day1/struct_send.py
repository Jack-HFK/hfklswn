from socket import *
import struct

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 格式 与服务端一致
st = struct.Struct("i32sif")

s = socket(AF_INET,SOCK_DGRAM)

while True:
  print("==========================")
  id = int(input("ID:"))
  name = input("Name:").encode()
  age = int(input("Age:"))
  score = float(input("Score:"))
  # 打包数据
  data = st.pack(id,name,age,score)
  s.sendto(data,ADDR)

s.close()

