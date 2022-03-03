'''
注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。

def function(arg,*args,**kwargs):
    print(arg,args,kwargs)

function(6,7,8,9,a=1, b=2, c=3)
'''


def function(arg, *args, **kwargs):
    print(arg, args, kwargs)


function(6, 7, 8, 9, a=1, b=2, c=3)


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
