"""
python中的with语句使用于对资源进行访问的场合，
保证不管处理过程中是否发生错误或者异常都会执行规定的“清理”操作，
释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等。
"""
import os
# with语句打开文件 省略了文件关闭close()
with open("/home/tarena/桌面/hfk_python/pychzrm course/journey_two/day4_PM/test","r+") as fd:
    # 读取文件
    # print(fd.read(7)) #读取10个字符（字节）
    # print(fd.readline(10)) #一般只读取文本文件 用来读取文件中一行
    # print(fd.readlines(6)) #读取文件中的每一行作为列表中的一项,返回读取到的内容列表
    # 写入文件
    # fd.seek(14)
    # fd.write("\n公子向北走")
    # fd.writelines(["\n小女子向南瞧"])
    # fd.flush()  # 将缓冲内容写入磁盘
    os.path.getsize(fd)