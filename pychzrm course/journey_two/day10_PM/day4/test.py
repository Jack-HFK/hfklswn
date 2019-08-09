# 计算
def count(x,y):
  c = 0
  while c < 7000000:
    c += 1
    x += 1
    y += 1

# io
def io():
  write()
  read()

def write():
  f = open('test','w')
  for i in range(1800000):
    f.write("Hello world\n")
  f.close()

def read():
  f = open('test')
  lines = f.readlines()
  f.close()