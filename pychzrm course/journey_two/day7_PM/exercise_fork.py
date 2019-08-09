"""
    基于fork的进程创建演示
"""

import os
import time

# pid的返回值是子进程的pid号码，子进程的pid返回值是pid函数的返回值默认为0
# 父进程fork执行完毕后，即刻拷贝出子进程，子进程立刻执行
# fork函数： 拷贝出子进程，父子进程同时向一个终端执行
pid = os.fork()


if pid < 0:
    print("Creatte process failed")

elif pid == 0:  # 子进程执行 elif
    time.sleep(3)
    print("New process")

else:  # 父进程执行else
    time.sleep(5)
    print("old process")
print("Fork rjr end")
