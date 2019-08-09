import time

def print_time(func):
    times = time.time()

    def numbers(*args, **kwargs):
        rrrr = func(*args, **kwargs)
        hfk = time.time() - times
        print(hfk, "时间")
        return rrrr

    return print_time

class Student:
    @print_time
    def study(self):
        print("学习。。")
        time.sleep(3)  # 睡眠3秒

    @print_time
    def play(self):
        print("玩。。")
        time.sleep(2)  # 睡眠3秒




stu = Student
stu.play()
stu.study()
