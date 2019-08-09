"""
    file_read   文件读取  ：注意文件读取时记录读取痕迹
                          下次读取依照痕迹继续读取
"""

# 打开文件
fd = open("./rjr","r")

# while True:
#     data = fd.read(2)
#     # 读取文件结尾得到的空字符串，此时跳出循环
#     if not data:
#         break
#     print(data)

# #读取一行内容
# data = fd.readline()
# print(data)
# #读取第二行内容
# data = fd.readline()
# print(data)

# #   读取所以内容，每行作为列表中一个元素
# data = fd.readline()
# print(data)
# # 读取一行，位置到哪一行的随意一个位置，本行全部读取
# data = fd.readlines(7)
# print(data)


#   文件对象本身也是一个可迭代对象，在for循环中可以迭代文件的每一行
for line in fd:
    print(line)     # 循环一次读取一行
