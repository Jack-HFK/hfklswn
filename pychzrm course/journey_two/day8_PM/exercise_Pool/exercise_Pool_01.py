from multiprocessing import Pool
import time



def f1():
    time.sleep(1)
    print(1)
def f3():
    time.sleep(1)
    print(3)
def f2():
    time.sleep(1)
    print(2)
def f4():
    time.sleep(1)
    print(4)
def f5():
    time.sleep(1)
    print(5)
def f6():
    time.sleep(1)
    print(6)
def f7():
    time.sleep(1)
    print(7)
def f8():
    time.sleep(1)
    print(8)
def f9():
    time.sleep(1)
    print(9)
def f10():
    time.sleep(1)
    print(10)


list1 = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

# 放入进程池的函数,要在进程对象创建前建立
# 创建进程池对象
pool = Pool()

for i in list1:
    pool.apply_async(i)

# 结束进程
pool.close()

# 回收进程
pool.join()