'''
特点：
1.函数A是作为参数出现的（函数B就接收函数A作为参数）
2.要有闭包的特点
'''


def decorate(func):
    a = 100

    def wrapper(*m, **n):
        print(int(*m) * 3)
        print(n)
        func(*m, **n)
        print('--------------->刷漆')
        print('--------------->铺地板', a)

    return wrapper


@decorate  # 引用装饰器，等同于 house = decorator(house)
def house(*m, **n):
    print('我是毛坯房。。。')


house(3, clazz=5)


# def decorate1(func):
#     def wrapper(*args, **kwargs):
#         print('1开始')
#         func(*args, **kwargs)
#         print('装地板')
#         print('1结束')
#
#     return wrapper
#
#
# def decorate2(func):
#     def wrapper(*args, **kwargs):
#         print('2开始')
#         func(*args, **kwargs)
#         print('刷墙')
#         print('2结束')
#
#     return wrapper
#
#
# @decorate2
# @decorate1
# def house(*m, **n):
#     print('我是毛坯房。。。')
#
#
# house()
'''
2开始
1开始
我是毛坯房
装地板
1结束
刷墙
2结束
'''
