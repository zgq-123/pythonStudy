'''
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候。是一个实例方法。
也就是： __new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
'''
class Person:
    # 私有化 单例的地址就存在于__instance
    __instance = None  # 单例的地址就存在于__instance

    def __init__(self):
        print('2' + str(self))

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print('1' + str(cls.__instance))
        return cls.__instance


p1 = Person()
p2 = Person()

print(p1)
print(p2)
