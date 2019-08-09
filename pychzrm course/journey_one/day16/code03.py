"""
  异常处理
  练习:exercise04.py
"""


def div_apple(apple_count):
  """
    分苹果
  """
  # ValueError
  person_count = int(input("请输入人数:"))
  # ZeroDivisionError
  result = apple_count / person_count
  print("每人分到%d个苹果" % result)


# 测试
# try:
#   div_apple(10)
# except:
#   print("通用的处理逻辑")

# try:
#   div_apple(10)
# except Exception:
#   print("通用的处理逻辑")


try:
  div_apple(10)

# except ValueError:
#   print("输入的数据应该是整数")
# except ZeroDivisionError:
#   print("分母不能是0")
# except Exception:
#   print("未知错误")
# else:
#   # 没有异常时执行
#   print("分苹果成功喽")

finally:
  print("无论是否发生异常,都执行的代码.")
print("后续逻辑.....")









