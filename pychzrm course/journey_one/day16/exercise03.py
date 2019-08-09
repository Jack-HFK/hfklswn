# 练习1:定义函数,在控制台中获取成绩(1--100)
#       如果输入有误,请重新输入.

def get_score():
  while True:
    str_score = input("请输入成绩:")
    try:
      int_score = int(str_score)
    except ValueError:
      continue
    if 1<=int_score<=100:
      return int_score

print(get_score())
# 练习2:将学生管理系统中,可能出错的代码,进行异常处理.
# 要求:程序可以按照既定流程继续向后执行.
