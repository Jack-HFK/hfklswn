"""
    wait函子进程处理退出函数
"""


import os

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process:",os.getpid())
    os._exit(5)
else:
    p,status = os.wait() # 阻碍等待子进程退出
    print("p:",p)
    # 还原退出状态
    print("status:",status)
    while True:
        pass