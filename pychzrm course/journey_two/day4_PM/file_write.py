#   打开文件 ， w 写入的模式打开，有就清除文件内容，没有创建
fd = open("./rjr", "w")

fd.write("东，青龙\n")
fd.write("西，火凤\n")
fd.write("南，白虎\n")
fd.write("北，玄武\n")

#   打开文件 ， wb 以二进制写入的模式打开，有就清除文件内容，没有创建
fd = open("./rjr", "wb")

#   wb二进制打开方式 以二进制写入文件，需要二进制转换为字符串。.encode()转换函数
fd.write("东，诸葛\n".encode())
fd.write("西，欧阳\n".encode())
fd.write("南，令狐\n".encode())
fd.write("北，独孤\n".encode())

# 打开文件 a+ 以读写进入模式，不改变之前内容
fd = open("./rjr", "a+")

fd.writelines(["北冥\n", "轩辕\n"])

# # 结束
fd.close()

# 文件偏移量在开头读取以下所有的数据
fd = open("./rjr", "r")
hfk = fd.read()
print(hfk)




