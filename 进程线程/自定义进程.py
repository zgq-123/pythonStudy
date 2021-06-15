# 进程:自定义
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, age=18, name='小花'):
        super(MyProcess, self).__init__(target=name)
        self.name = name
        self.age = age

    # 重写run方法
    def run(self):
        # print('进程名字:' + self.name)
        n = 1
        while True:
            time.sleep(1)
            print('{}------------>自定义进程,n:{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess(name='小明')
    p1.start()
