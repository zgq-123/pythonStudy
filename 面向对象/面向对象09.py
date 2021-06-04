# 继承  支持多继承
'''
多继承的深度优先和广度优先
1、类为经典类时，多继承情况下，会按照深度优先查找
2、类为新式类时，多继承情况下，会按照广度优先查找
但python3中取消了经典类，默认继承object，即python3之后采用的是广度查找。

'''


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#
# s = Student('lisi', 30)
# print(s.name)


# class A:
#     def test(self):
#         print('--------->A')
#
#
# class B:
#     def test1(self):
#         print('--------->B')
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# c.test()
# c.test1()
# print(C.__mro__)  # 查找执行的顺序

class D:
    def test(self):
        print("D")


class C(D):
    def test(self):
        print("C")


class B(D):
    pass


class A(B, C):
    pass


a = A()
a.test()

print(A.__mro__)

print('aaaaaaaaaaaaaaaab')


