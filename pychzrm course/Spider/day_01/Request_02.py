from urllib import request

url = "http://httpbin.org/get"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

# 1.创建请求对象
req = request.Request(url=url,headers=headers)
# 2.获取响应对象
res = request.urlopen(req)
# 3.提取响应内容
html = res.read().decode("utf-8")

print(html)