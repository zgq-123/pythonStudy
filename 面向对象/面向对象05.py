# 魔术方法
'''
__init__: 初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

__new__:实例化的魔术方法
触发时机：在实例化时触发

__call__:对象调用方法
触发时机：将对象完成函数使用的时候，会默认调用此函数内容

__del__:析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发

__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候。是一个实例方法。
也就是： __new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
'''
import sys


class Person:
    def __init__(self, name):
        print('---------->init')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('---------->new')
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print('----------->call', *args, **kwargs)

    def __del__(self):
        print('---------->del')


# person = Person()('hello')

person1 = Person('Jack')
print(person1.name)
print(sys.getrefcount(person1))
del person1
print(sys.getrefcount(person1))
# print(person1.name)
