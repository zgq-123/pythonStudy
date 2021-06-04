# list1 = [1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 8]
# print(type(list1))
# print(list1)
# print(set(list1))
# set1 = set()
# print(type(set1))
#
# set1.add('hello')
# set1.add('hi')
# print(set1)
# import random
# s = 'zxcvbnmasdfghjklqwertyuiop1234567890ZXCVBNMASDFGHJKLQWERTYUIOP'
# set1 = set()
# while True:
#     code = ''
#     for i in range(4):
#         r = random.choice(s)
#         code += r
#     set1.add(code)
#     if len(set1) == 5:
#         break
# print(list(set1))

# print(set1)
# set1.remove('1')
# print(set1)
# set1.discard('4')
# print(set1)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
a = set1.difference(set2)  # 差集
b = set1.union(set2)  # 并集
c = set1.intersection(set2)  # 交集
d = set1 | set2  # 并集
e = set1 & set2  # 交集
f = set1 - set2  # 差集
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
