# 进程创建
'''
process=Process(target=函数，name=进程的名字，args=（给函数传递的参数）)
process 对象

对象调用方法：
process.start()   启动进程并执行任务
process.run()     只是执行了任务但是并没有启动进程
terminate()        终止
'''
from multiprocessing import Process
from time import sleep

# def task1(s):
#     while True:
#         sleep(s)
#         print('这是任务1。。。。。。')
#         print()
#
#
# def task2(s):
#     while True:
#         sleep(s)
#         print('这是任务2。。。。。。')
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task1, name='任务1', args=(1,))
#     p1.start()
#     p2 = Process(target=task2, name='任务2', args=(2,))
#     p2.start()

m = 1


# def task1():
#     global m
#     while True:
#         m += 1
#         sleep(1)
#         print('这是任务1:' + str(m))
#
#
# def task2():
#     global m
#     while True:
#         m += 1
#         sleep(2)
#         print('这是任务2:' + str(m))
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task1, name='任务1')
#     p1.start()
#     p2 = Process(target=task2, name='任务2')
#     p2.start()


class Test():
    m = 2

    def __init__(self):
        m = 5

    def connect(self):
        print(m)


Test().connect()
