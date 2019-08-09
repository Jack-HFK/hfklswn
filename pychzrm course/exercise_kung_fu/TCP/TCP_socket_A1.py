from  socket import *

st = socket()

st.connect(("172.40.80.251",8888))
while True:
    s = input("请输入")
    n = st.send(("你是谁%s" % s).encode())
    data = st.recv(1024).decode()
    print(data)
    if not data:
        break
st.close()