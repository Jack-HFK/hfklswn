"""
    Thread_class
    自定义线程类
"""

from threading import Thread

# 继承Thread

# 重写__init__ 和 run

class ThreadClass(Thread):
    def __init__(self,attr):
        # 子类有构造函数，覆盖了父类构造函数
        # super函数重新加载父类__init__构造函数属性
        super().__init__()
        self.attr = attr
    # 很多方法配合完成任务
    def f1(self):
        print("方法一")
    def f2(self):
        print("方法二")
    # 重写run方法
    def run(self):
        self.f1()
        self.f2()

t = ThreadClass("****")
t.start()
t.join()
