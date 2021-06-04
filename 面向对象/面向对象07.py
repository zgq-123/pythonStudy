# 私有化
# 封装：1.私有化属性 2.定义公有set和get方法
class Student:
    # __age = 18  # 类属性

    def __init__(self, name, age):
        self.__age = age
        self.__name = name
        self.__score = 60  # 私有化

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def __str__(self):
        return '姓名：{},年龄：{}，考试分数：{}'.format(self.__name, self.__age, self.__score)


s = Student('zs', 19)
print(s)

s.setName('lisi')
s.setAge(80)
print(s)
print(s.getAge())
print(s.getName())
print(dir(s))

# 伪装私有，只不过系统改名字了
print(s._Student__age)
print(s._Student__name)
print(s._Student__score)
