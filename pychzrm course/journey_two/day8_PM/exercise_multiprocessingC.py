from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("'I'm %s"%name)
        print("'I'm working....")
# 元祖位置传参
# p = Process(target=worker,args=(2,"baron"))

# 字典键值传参
# p = Process(target= worker,kwargs= {"name":"baron","sec":2})

# 元祖位置传参 + 字典键值传参
p = Process(target= worker,args=(2,),kwargs= {"name":"baron"})

p.start()

p.join()


