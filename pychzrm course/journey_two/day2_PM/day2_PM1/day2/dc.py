from lstack import *

ls = LStack()

while True:
  exp = input()
  tmp = exp.split(' ')
  for i in tmp:
    if i not in ['+','-','p']:
      ls.push(float(i)) #　入栈数字
    elif i == '+':
      x = ls.pop()
      y = ls.pop()
      ls.push(y + x)
    elif i == '-':
      x = ls.pop()
      y = ls.pop()
      ls.push(y - x)
    elif i == 'p':
      print(ls.top())   #　查看栈顶元素
