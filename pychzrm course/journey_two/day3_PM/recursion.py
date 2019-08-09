#　求ｎ的阶乘
def recursion(n):
  #　递归终止条件
  if n < 1:
    return 1
  return n * recursion(n - 1)

print("n!=",recursion(5))

