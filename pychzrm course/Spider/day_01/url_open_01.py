# 模块导入

import urllib.request

# 向网站发起请求并获取响应对象
response = urllib.request.urlopen("http://www.baidu.com/")

# 　获取响应对象内容
html = response.read().decode("utf-8")
# 获取HTTP响应码
code = response.getcode()
# 获取返回实际数据的URL地址
url = response.geturl()


print(html)
