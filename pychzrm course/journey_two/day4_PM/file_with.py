"""
    with 语句
"""

with open("./rjr") as fd:  # 生成fd文件对象
    data = fd.read()  #read() 读写
    print(data)


# with 语句块结束 ， fd 自动销毁