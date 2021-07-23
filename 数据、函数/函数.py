def search():
    print('我是函数')
    return 'a'


def add(a, b, c=3):
    return a + b + c


# *args 用来将参数打包成tuple给函数体调用
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# **kwargs 打包关键字参数成dict给函数体调用
def a(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


a(name='zs', old=19)

b = {'lisi': 15, 'zhaoliu': 20}
a(**b)

print(type(('a',)))

print("*".join(['a', 'b', 'c']))
