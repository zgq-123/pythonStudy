# 阻塞式：
# 非阻塞式：
import os
from multiprocessing import Pool
import time

# 非阻塞式
from random import random


def task(task_name):
    print('开始做任务了', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务用时:{},进程id:{}：'.format((end - start), os.getpid()))
    return task_name + '回调函数'


def callback_fun(n):
    print(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '唱歌', '洗衣服', '写作业', '敲代码', '散步', '吃饭']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_fun)
    pool.close()
    pool.join()
    print('over')
