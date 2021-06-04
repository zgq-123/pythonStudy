# __str__
'''
触发时机:使用print(对象)或者str(对象)的时候触发
参数：一个self接收对象
返回值：必须是字符串类型
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)


p = Person('tom', 18)
print(p)
# print(p.name)
