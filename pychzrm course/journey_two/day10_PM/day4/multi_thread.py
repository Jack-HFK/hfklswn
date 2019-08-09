from day4.test import *
import time
from threading import Thread

jobs = []
tm = time.time()

for i in range(10):
  t = Thread(target = io)
  jobs.append(t)
  t.start()

for i in jobs:
  i.join()

print("Thread io:",time.time() - tm)


