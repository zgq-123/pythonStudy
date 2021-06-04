'''
a、全局变量：在模块内、在所有函数外面、在class外面，这就是全局变量。

b、局部变量：在函数内、在class的方法内（未加self修饰的），这就是局部变量。

c、 静态变量：在class内的，但不在class的方法内的，这就是静态变量。

d、 实例变量：在class的方法内的，用self修饰的变量，这就是实例变量。
'''

a = 1


def update_a():
    global a  # 全局变量a
    a = 3


update_a()
print(a)

b = ['a', 'b', 'c']


def add_b():
    b.append('d')


add_b()
print(b)
