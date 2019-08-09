import redis
from django.http import HttpResponse,HttpResponseRedirect
from user.models import UserProfile

def test_view(request):
    return HttpResponse("test_view")

 # 增加分布式锁
# def test2_view(request):
#     # 创建连接池
#     
#     pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0)
#     # 连接到连接池
#     r = redis.Redis(connection_pool=pool)
#     print(r)
#     print("9")
#     while True:
#         print("10")
#         try:
#             with r.lock("swn", blocking_timeout=3) as lock:
#                 print("12")
#                 # 对score字段进行+1操作
#                 user = UserProfile.objects.get(username="swn")
#                 print("13")
#                 print(user)
#                 user.score += 1
#                 
#                 user.save()
#                 # # 真正发送请求
#                 # return HttpResponse("接受请求")
#             print("66")
#             break
# 
#         except Exception as e:
#             print("获得分布式锁失败")
#     return HttpResponse("哈哈哈")

def test2_view(request):
    pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
    r = redis.Redis(connection_pool=pool)
    # 加分布式锁
    while True:
        try:
            with r.lock('swn',blocking_timeout=3) as lock:
                # 对score字段进行+1操作
                u = UserProfile.objects.get(username='swn')
                u.score += 1
                u.save()
            break
        except Exception as e:
            print('lock failed')

    return HttpResponse('HI HI HI')