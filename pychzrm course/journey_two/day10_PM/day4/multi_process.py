from day4.test import *
import time
from multiprocessing import Process

jobs = []
tm = time.time()

for i in range(10):
  p = Process(target = io)
  jobs.append(p)
  p.start()

for i in jobs:
  i.join()

print("Process cpu:",time.time() - tm)


