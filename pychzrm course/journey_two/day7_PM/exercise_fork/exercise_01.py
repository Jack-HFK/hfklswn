"""
fork 创建进程练习

# pid的返回值是子进程的pid号码，子进程的pid返回值是pid函数的返回值默认为0
# 父进程fork执行完毕后，即刻拷贝出子进程，子进程立刻执行
# fork函数： 拷贝出子进程，父子进程同时向一个终端执行
"""
# os模块包含了操作系统的方法
import os,sys
import time

# 实例化对象
pid = os.fork()

def find01():
    pid = os.getpid()
    print("父进程 old process",pid)
def find02():
    pid = os.getpid() # 当前进程pid
    print("子进程 New process",pid)

if pid < 0:
    raise Exception
elif pid == 0:
    time.sleep(1)
    find02()
else:
    time.sleep(2)
    find01()
os._exit(0) # 结束进程下面代码不会执行
print("其他程序")
sys.exit("退出进程,旗下代码不打印")
print("a")
