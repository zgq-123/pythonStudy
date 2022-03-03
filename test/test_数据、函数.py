# 1.String
"""s1 = 'hello'
s2 = s1
s3 = 'hello'
print(s1 == s2 == s3)
print(id(s1), id(s2), id(s3))
print(s1.__eq__(s3))

s1 = 'asAAAddadFFff'
print(s1[1])
print(s1[0:4])
print(len(s1))
print(s1[0:-2:1])
print(s1.replace('A', '1'))

# result = input("开始:")
# print(result.replace('你妹', '**'))
s = '''张三!
 李四!
 王五!'''
print(s.split())
print(s.title())
print(s.capitalize())
print('{}{}'.format('1','ha'))"""

# 2.列表

"""list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[-1::-2])
m = 'dhuiahdhai1345'
sum = 0
for i in m:
    if i.isdigit():
        sum += int(i)
print(sum)

list2 = []
list2.append('a')
list2.append('b')
list2.append('c')
print(list2)
print(list1 + list2)
# list1.extend(list2)
print(list1.append(list2))
print(list1)
list1.pop(5)
print(list1)
print(list1.remove('b'))
print(list1)

if 'a' in list1:
    print(True)
else:
    print(False)

list1.insert(3, 9)
print(list1)
list1.reverse()
print(list1)

for i in range(1,5):
    print(i)"""

# 3.列表推导式
"""x = 2
# for i in range(3):
#     x = x + i

m = [x + i for i in range(3)]
print(m)

print([i for i in range(101) if i % 2 == 0])
print('naf'.title())"""

# 4.元组
"""m = ('a', 'b')
print(type(m))
print(m[0])
print(list(m))"""

# 5.字典
"""a = {}
a['name'] = 'zs'
a['old'] = 18
print(a)
print(a.keys())
print(a.values())
print(a.items())
for k, v in a.items():
    print(k, v)"""

# 6.集合
"""import random

list = [1, 2, 3, 4, 5, 6, 7, 8]
print(type(list))
print(set(list))
set1 = set(list)
set1.add('hello')
set1.add('hi')
print(set1)
s = 'zxcvbnmasdfghjklqwertyuiop1234567890ZXCVBNMASDFGHJKLQWERTYUIOP'
code = ''
for i in range(4):
    r = random.choice(s)
    code += r
print(code)
set1.remove(1)
print(set1)
set1.discard(3)
print(set1)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 - set2)
print(set1 & set2)
print(set1 | set2)"""

# 7.函数
'''def search():
    print('我是函数')


def f(*args):
    print(args, type(args))


search()
f(1, 2, 3)'''

8.
