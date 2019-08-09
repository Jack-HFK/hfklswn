"""
select 示例
"""
from socket import *
from select import select

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

print("监控ＩＯ")
rs,ws,xs = select([],[s],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)

