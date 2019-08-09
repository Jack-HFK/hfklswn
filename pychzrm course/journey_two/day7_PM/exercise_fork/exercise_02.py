import os
import time

pid = os.fork()


if pid < 0:
    raise Exception
elif pid == 0:
    print(1)
else:
    print(2)

pids,status = os.wait()
print(pids)
print(status)