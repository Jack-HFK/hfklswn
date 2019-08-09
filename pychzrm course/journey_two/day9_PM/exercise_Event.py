"""
    线程同步互斥方法Event
"""

from threading import Event, Thread
from time import sleep




# 全局变量，用于通信
s = None

# 创建Event对象
e = Event()





def 越前龙马():
    print("你还差的远那")
    global s
    s = "天王盖地虎"
    # 结束wait函数阻塞
    e.set()

t = Thread(target=越前龙马)

# 阻塞其他使用全局变量
t.start()
print("pk vs pk")

e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("开始pk")
else:
    print("送行")

t.join()