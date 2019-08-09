"""
  pool 进程池
"""

from  multiprocessing import Pool
from time import sleep,ctime  # ctime获取当前时间

# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 放入进程池的函数对象,函数要在进程对象创建前建立
# 创建进程池
pool = Pool()   # 参数为限制进程池执行的进程个数

# 添加事件
for i in range(20):
    msg = "hello %d"%i
    pool.apply_async(worker,args=(msg,))
    # r 代表func事件的一个对象
    # r = pool.apply_async(worker,args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()

# 获取函数事件的返回值
# print(r.get())

