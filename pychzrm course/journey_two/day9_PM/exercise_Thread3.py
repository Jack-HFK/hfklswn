
from  threading import Thread
from  time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs


    def run(self):
        self.target(*self.args,**self.kwargs)


def player(sec,song):
    for i in range(3):
        print("player %s: %s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={"song":"女儿情"})
t.start()
t.join()