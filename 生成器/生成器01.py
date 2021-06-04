# print([i for i in range(1000000)])#列表推导式   []

# 得到生成器   ()
try:
    a = (i for i in range(5))
    print(type(a))  # generator
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(next(a))
    print(next(a))
    print(next(a))
except Exception as err:
    print(err)
    print('没有更多元素了')
