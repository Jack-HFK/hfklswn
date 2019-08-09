import requests
import random

from Spider.day_02.User_Agents import user_agents

url = "http://www.baidu.com/"

# 包装User-Agent
headers = {"User-Agent":random.choice(user_agents)}

# 向网站发起请求,并获取响应对象
res = requests.get(url,headers)
print(res)
# 显示编码
a = res.encoding = "utf-8"
print(a)
# 获取文本内容 string格式
b = html = res.text
print(b)
# 获取文本内容 bytes字节串格式
c = byte = res.content
print(c)
# 获取HTTP响应码
d = rsb = res.status_code
print(d)
# 实际数据的URL地址
e = url = res.url
print(e)