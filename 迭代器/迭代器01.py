'''
可迭代的对象：1.生成器 2.元组 列表 集合 字典 字符串
如何判断一个对象是否是可迭代？
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

可迭代的 不一定是迭代器
迭代器只能往前，不能后退
'''
from collections.abc import Iterable

list1 = [1, 4, 7, 8, 8]
print(isinstance(list1, Iterable))  # 判断是否可迭代
a = iter(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
