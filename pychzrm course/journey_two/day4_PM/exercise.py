# 熟练使用文件函数（open,read,write）

# 从终端输入一个文件名称（包含路径），
# 如果该文件存在侧将该文件复制到当前目录下，
# 命名为1904（要求文件可以是任意类型），
# 不存在文件则打印文件不存在

def find_file():
    import os
    hfk = open("./rjr", "a+")
    swn = open("/home/tarena/dict.txt", "r")
    while True:
        if os.path.exists("/home/tarena/dict.txt"):
            swn1 = swn.read()
            if not swn1:
                break
            hfk.write(swn1)
        else:
            print("不存在")


# find_file()

# 向一个文件写日志，写入格式：
# 1. 2019-1-1  12:12:12
# 2. 2019-1-1  12:12:12
# 要求每隔一秒写入一次，每条时间占一行，程序死循环，
# crtl-c退出，再次启动要求能和上次时间衔接

import time
#
# rjr = open("./rjr", "a+")
# while True:
#     time01 = time.localtime()
#     time02 = time.strftime("%Y-%m-%d %H-%M-%S", time01)
#     time.sleep(1)
#     rjr.write(time02)
#     rjr.write("\n")
#     rjr.flush()


rjr = open("./rjr", "a+")
n = 0
rjr.seek(0,0)   # 将偏移量移动到开始处，然后计算
for line in rjr:
    n += 1
while True:
    n += 1
    time.sleep(1)
    s = "%d. %s\n" %(n,time.ctime())  #获取当前时间
    rjr.write(s)
    rjr.flush()     #缓存区内容直接存入硬盘



