# 编写一个函数，传入一个整数，返回该整数的阶乘
def number(n):
    i = 1
    for i1 in range(1, n+1):
        i *= i1
    return i
print(number(5))

def get_factorial(n):
    if n < 0:
        return 1
    else:
        return n * get_factorial(n-1)