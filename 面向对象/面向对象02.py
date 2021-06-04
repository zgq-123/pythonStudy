# 类中的方法
class Phone:
    brand = 'hauwei'
    price = 7000
    type = 'mate 20'

    def call(self):
        print(self)
        print(self.note)
        print('正在打电话')


huawei1 = Phone()
huawei1.note = '123456'
print(huawei1.brand)
huawei1.call()

print('*' * 80)

huawei2 = Phone()
huawei2.note = '56789'
print(huawei2.brand)
huawei2.call()
