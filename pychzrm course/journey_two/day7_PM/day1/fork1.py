"""
基于fork的进程创建演示2
"""

import os
from time import sleep

print("=========================")
a = 1

pid = os.fork()

if pid < 0:
  print("Create process failed")
elif pid == 0:
  print("New process")
  print("a = ",a)
  a = 10000
else:
  sleep(1)
  print("Old process")
  print("a:",a)

print("All a = ",a)