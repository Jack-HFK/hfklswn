# """
# 模仿高并发分别向8000端口和8001端口，都对模型类的字段score对应的值进行+1
# """
# import random
# from threading import Thread
# 
# # 线程事件函数,模仿高并发分别向8000端口和8001端口发请求
# import requests
# 
# 
# def get_request():
#     # 对score字段进行加１操作
#     url1 = "http://127.0.0.1:8000/test2"
#     url2 = "http://127.0.0.1:8001/test2"
#     url = random.choice([url1, url2])
#     # 真实发送请求
#     requests.get(url)
#         
# 
# t_list = []
# 
# for i in range(30):
#     t = Thread(target=get_request)
#     t_list.append(t)
#     t.start()
# 
# for j in t_list:
#     j.join()


'''30个请求,向8000和8001发请求,都对score进行+1操作'''
from threading import Thread
import random
import requests

# 线程事件函数: 向8000或者8001随机发请求
def get_request():
  url1 = 'http://127.0.0.1:8000/test2'
  url2 = 'http://127.0.0.1:8001/test2'
  url = random.choice([url1,url2])
  # 真正发请求
  requests.get(url)

t_list = []

for i in range(30):
  t = Thread(target=get_request)
  t_list.append(t)
  t.start()

for j in t_list:
  j.join()

