# 给定一个整数（正负不限），将整数进行反转
# 输入123 返回321
# 输入-456 返回-654

# 思路:正数：反转整数，乘以1
# 思路:负数：反转整数数，乘以-1

x = -123
def reverse(x):
    cmp = lambda a,b:(a>b)-(a<b)  # (-123>0) - (0>-123):false-ture=-1
    s = cmp(x,0)  # 调用函数cmp(传参)
    rev = int(str(s * x)[::-1])  # 调整为正数 反向切片
    return s * rev  # 调整回正负数

print(reverse(x))
