"""
信号方法处理僵尸进程
"""

import signal
import os

# 子进程退出时，父进程忽略，子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()

if pid < 0:
  pass
elif pid == 0:
  print("Child pid:",os.getpid())
else:
  while True:
    pass