'''
定义生成器的方式二：借助函数完成
只要函数中出现了yield关键字，说明函数就不是函数了，变成为生成器
'''


# def func():
#     n = 0
#     while True:
#         n += 1
#         # print(n)
#         yield n  # return n +暂停
#
#
# g = func()  # 得到生成器
# print(g.__next__())
# print(next(g))
# print(g.__next__())


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        i += 1
    return '没有更多的内容'


g = gen()
print(g.send(None))
n1 = g.send('呵呵')
print('n1:', n1)
n2 = g.send('哈哈')
print('n2', n2)

'''
0
temp: 呵呵
n1: 1
temp: 哈哈
n2 2
'''
