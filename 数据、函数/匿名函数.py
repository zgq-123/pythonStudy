'''
匿名函数：简易函数定义
格式：lambda  参数1，参数2..:运算
'''
s = lambda a, b: a + b
# print(s(1, 2))

list1 = [{'a': 10, 'b': 20}, {'a': 11, 'b': 19}, {'a': 12, 'b': 18}]
print(max(list1, key=lambda x: x['a']))
