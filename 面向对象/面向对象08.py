# 私有化设置 @property == get方法  @age.setter == set方法
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return '姓名：{},年龄：{}'.format(self.__name, self.__age)


s = Student('zs', 18)
print(s)

s.age = 100
print(s.age)
