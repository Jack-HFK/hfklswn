"""
    getpid
"""

# 获取pid值

import os
from time import *

pid = os.fork()


if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getegid()) # 获取当前子进程PID
    print("Get parent PID:",os.getppid())# 获取父进程PID
else:
    print("Child PID:", pid) # 获得当前子进程PID
    print("Get parent PID:", os.getpid()) # 获得当前父进程PID
