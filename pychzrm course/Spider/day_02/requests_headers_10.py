import requests
import random
from Spider.day_02.User_Agents import user_agents

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565352281059&di=3309e32501b4750eed1a2901fe059b92&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2018-01-24%2F5a6844222b387.jpg"
headers = {"User-Agent":random.choice(user_agents)}

res = requests.get(url=url,headers=headers)
html = res.content

with open("宋祖儿.jpg","wb") as f:
    f.write(html)

