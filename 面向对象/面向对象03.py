# 魔术方法：__名字__()
# class Phone:
#     def __init__(self):
#         print('----------init')
#
#     def call(self):
#         print(self)
#         print('正在打电话')
#
#     def __enter__(self):
#         print('enter')
#
#
# Phone.call()
# huawei1 = Phone()
# huawei1.call()


class Phone:

    def __init__(self, *args, **kwargs):
        print(*args, **kwargs)

    def call(self):
        print(self)
        print('正在打电话')


huawei1 = Phone('zs', 18)
huawei1 = Phone('zs')
# huawei1.call()
