"""
    buffer   缓冲区
"""
fd = open("./rjr", "a+")  # 生成fd文件对象
while True:
    str_number = input("请输入内容")
    fd.write(str_number)
    fd.write("杀无赦\n")
    fd.flush()  # 将缓冲内容写入磁盘


fd.close()