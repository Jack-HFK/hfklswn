"""
基于fork的进程创建演示1
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
  print("Create process failed")
elif pid == 0:
  os._exit(0)
  sleep(3)
  print("New process")
else:
  sleep(5)
  print("Old process")

print("Fork rjr end")