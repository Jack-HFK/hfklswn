"""
file_open   打开文件
"""

# 打开文件
try:
    fd = open("rjr","w")
    print(fd)
except Exception as e:
    print(e)

#开始你的读写
#关闭文件
fd.close()