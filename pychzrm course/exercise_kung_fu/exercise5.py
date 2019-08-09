# 有一个多层嵌套列表L=[1,2[3,4[5,6[7,8]]]]，打印出来所有数字

L=[1,2,[3,4,[5,6,[7,8]]]]
def bianli(lists):
    ls = []
    ls.append(lists)
    while len(ls) != 0:
        dirl = ls.pop()
        for i in dirl:
            if type(i) is list:
                ls.append(i)
            else:
                print(i)
bianli(L)

# 递归函数
L=[1,2,[3,4,[5,6,[7,8]]]]
def bianlis(lists):
    for i in lists:
        if type(i) is list:
            bianlis(i)
        else:
            print(i)

bianlis(L)
