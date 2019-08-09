"""
中间件示例
"""

# file:middleware/mymw.py

from django.http import HttpResponse
# 中间件类须继承自django.utils.deprecation.MiddlewareMixin类
from django.utils.deprecation import MiddlewareMixin


# 继承父类 MiddlewareMixin类 ,自定义类
class MyMiddleware(MiddlewareMixin):
    count = 0
    # 服务器接收前进行拦截或者验证等处理
    # def process_request(self, request):
    #     self.__class__.count += 1
    #     # print("count = %d"%self.__class__.count)
    #     if self.__class__.count <= 2 :
    #         return None
    #     else:
    #         return HttpResponse("次数用完")

# 创建类，限制一个IP地址多次访问admin后台数据库管理中心
import re
class LimitVisit(MiddlewareMixin):
    visit_times = {}  # 字典键设定为IP地址,值访问次数
    # def process_request(self,request):
    #     ip = request.META["REMOTE_ADDR"]  # 可以得到远程客户端的IP地址
    #     # re.match() 正则匹配字符串开头位置
    #     # 不是adminUPL跳过
    #     if not re.match(r"^admin",request.path_info):  # path_info: URL 字符串
    #         return
    #     # 不是POST请求跳过
    #     if request.method != "POST":
    #         return
    #     time = self.visit_times.get(ip,0) # 设置字典键：有IP 添加IP，没有默认为0
    #     self.visit_times[ip] = time + 1   # 设置字典值：访问次数加1
    #
    #     if time > 2:
    #         return HttpResponse("你访问次数或注册次数过多！")


