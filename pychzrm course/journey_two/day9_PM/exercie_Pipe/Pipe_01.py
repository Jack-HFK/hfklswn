from multiprocessing import Pipe,Pool
import time

# 建立管道通信
pipe1,pipe2 = Pipe()

def f1():
    time.sleep(2)
    a = "f1"
    pipe1.send(a) #向管道发送内容

def f2():
    print("f2")
    b = pipe2.recv() # 从管道接收内容
    print(b)

list1 = [f1,f2]

# 创建进程池
pool = Pool()

for i in list1:
    # 将函数遍历放入进程池，使用进程池一起执行函数
    pool.apply_async(i)

pool.close()

pool.join()