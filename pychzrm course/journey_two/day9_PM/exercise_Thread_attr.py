"""
    Thread_attr 线程属性
"""

from threading import Thread
from time import sleep

# 创建线程对象函数
def fun():
    sleep(1)
    print("线程属性")

# 创建线程对象
t = Thread(target=fun,name="Tarena")

# 主线程退出分支线程也退出
t.setDaemon(True)

t.start()

# 设置线程名称
t.setName("Tedu")
# 获取线程名称
print("Name",t.getName())

# 获取线程是否在生命周期
print(t.is_alive())

# 查看daemon属性
print("is Daemon",t.isDaemon())