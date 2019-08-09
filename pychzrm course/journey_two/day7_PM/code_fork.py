"""
    创建父子进程，复制一个文件，各自复制一半到文件中

    总结：   1.父进程中生成文件描述符，子进程从父进程拷贝
              此时父子进程对该文件描述符的使用相互影响
            2.如果父子进程中各自生成的文件描述符
              那么相互之间没有任何影响
"""
import os
from time import sleep

swn = "./rjr"
size = os.path.getsize(swn)


# 父子进程使用fr会相互影响
# fr = open(rjr,"rb")

def copy_vim():
    fr = open(swn, "rb")
    fw = open("./hfklswn", "wb")
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def copy_vim1():
    fr = open(swn, "rb")
    fw = open("./swnlhfk", "wb")
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    copy_vim1()
else:
    copy_vim()
