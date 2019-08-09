"""
  装饰器
"""

"""
def say_hello():
  print("hello")


def say_goodbye():
  print("goodbye")

say_hello()
say_goodbye()
"""
# 需求:在两个方法所实现的功能基础上,增加一种新功能(打印方法名称).

"""
def say_hello():
  print(say_hello.__name__)
  print("hello")

def say_goodbye():
  print(say_goodbye.__name__)
  print("goodbye")
"""

# 在say_hello与say_goodbye内部调用新功能,不容易改变(增加/删除)
"""
def print_func_name(func):
  print(func.__name__)

def say_hello():
  print_func_name(say_hello)
  print("hello")

def say_goodbye():
  print_func_name(say_goodbye)
  print("goodbye")
"""

"""
def print_func_name(func):# 提供旧功能
  def wrapper():# 包装
    print(func.__name__)# 新功能
    func()# 调用旧功能
  return wrapper

def say_hello():
  print("hello")

def say_goodbye():
  print("goodbye")

# 调用外部函数
say_hello = print_func_name(say_hello)
say_goodbye = print_func_name(say_goodbye)

# 调用内部函数(包装新 + 旧功能)
say_hello()
say_goodbye()
"""
"""
def print_func_name(func):# 提供旧功能
  def wrapper():# 包装
    print(func.__name__)# 新功能
    func()# 旧功能
  return wrapper

@print_func_name # say_hello = print_func_name(say_hello)
def say_hello():
  print("hello")

@print_func_name
def say_goodbye():
  print("goodbye")

say_hello()
say_goodbye()

"""


def print_func_name(func):  # 提供旧功能
  def wrapper(*args, **kwargs):  # 包装
    print(func.__name__)  # 新功能
    return func(*args, **kwargs)  # 旧功能

  return wrapper


@print_func_name  # say_hello = print_func_name(say_hello)
def say_hello():
  print("hello")
  return "ok"


@print_func_name
def say_goodbye(name):
  print(name, "goodbye")


result = say_hello()
print(result)
say_goodbye("张无忌")
