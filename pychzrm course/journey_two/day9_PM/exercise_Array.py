"""
进程共享内存通信 Array
obj = Array(ctype,data)
功能: 开辟共享内存空间
参数: ctype 表示共享内存数据类型
data 整数则表示开辟空间的大小,其他数据类型表示开辟空间存放的初始化数据
     返回值:共享内存对象
Array的  列表或者字符串，有序的可迭代的
Array共享内存读写: 通过遍历obj可以得到每个值,直接可以通过索引序号修改任意值。
* 可以使用obj.value直接打印共享内存中的字节串，只能打印字节串
"""

from multiprocessing import Process,Array

# 创建共享空间
# hfk = Array("i",[1,2,3])

# # 表示开辟三个空间列表
# hfk = Array("i",3)

# 字节串
hfk = Array("c",b"love")

def fun():
    # 共享内存对象可迭代
    for i in hfk:
        print(i)
        # hfk[1] == 888
    hfk[1] = b"g"

p = Process(target=fun)
p.start()
p.join()
fun()
for i in hfk:
    print(i)

# 打印字节串，* 可以使用obj.value直接打印共享内存中的字节串
# hfk.value 只能打印字节串
print(hfk.value)