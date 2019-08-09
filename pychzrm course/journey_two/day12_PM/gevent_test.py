"""
gevent 协程
"""
import gevent
from time import sleep
# 协程函数
def foo (a,b):
    print("swn",a,b)
    print("love")



f = gevent.spawn(foo("小女子不才","未得公子青睐"))
gevent.sleep(2)