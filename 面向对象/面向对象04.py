# 类方法

class Phone:
    age = 18

    def __init__(self, age, color):
        self.age = age 
        self.color = color

    def call(self):
        print(self)
        print('正在打电话')

    @classmethod
    def read(cls):
        cls.age = 20
        print('看小说')

    @staticmethod
    def test():
        print('静态方法')
        print(Phone.age)


huawei1 = Phone('zs', 18)
huawei1.read()
huawei1.test()
# huawei1.call()
# huawei1.read()
# Phone.read()
# print(huawei1.age + 1)
