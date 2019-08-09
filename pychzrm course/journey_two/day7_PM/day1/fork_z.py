import os

pid = os.fork()

if pid < 0:
  pass
elif pid == 0:
  print("Child pid:",os.getpid())
else:
  while True:
    pass