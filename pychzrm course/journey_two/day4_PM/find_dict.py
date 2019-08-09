"""
    英英词典，查找单词，根据单词打印注释
"""


# # 打开单词文件
# fd = open("/home/tarena/dict.txt","r")

# #   文件对象本身也是一个可迭代对象，在for循环中可以迭代文件的每一行
# for line in fd:
#     if line == "number":
#         print(line)     # 循环一次读取一行


def find_dict(dict01):
    fd = open("/home/tarena/dict.txt", "r")
    # 遍历的单词已经大于目标
    for line in fd:
        tmp = line.split(" ")[0]
        if tmp > dict01:
            print("欧巴内有")
            break
        if dict01 == tmp:
            print(line)
            break
    else:
        raise Exception("妹有呦")

find_dict("student")
