# file: middleware/mymw.py

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    "自定义一个MyMiddleware类"
    count = 0 # 此变量用不记录整个网站的访问次数
    def process_request(self,request):
        self.__class__.count += 1
        print("count = %d"%self.__class__.count)
        if self.__class__.count <= 5:
            return None
        else:
            html = "你已经访问此网站5次，你在执行视图之前或你在http请求前被拦截了"
            return HttpResponse(html)