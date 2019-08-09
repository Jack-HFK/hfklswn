from multiprocessing import Process
import time
A = 5
def process():
    global A
    A = 1000
    time.sleep(3)
    print("传入函数,子进程",A)
p = Process(target=process,args=(),kwargs={})

# 如果设置为True则子进程会随父进程的退出而结束
p.daemon = True

# 启动进程
p.start()

# # 阻塞等待回收进程
# p.join()

print(A)

