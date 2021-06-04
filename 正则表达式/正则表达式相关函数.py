# -*-coding:utf-8-*-
# 爬虫
import re

# phone = '010-123456789'
# result = re.match('(\d{3}|\d{4})-(\d{9})$', phone)
# print(result.group())
#
# # 分别提取  ()表示分组
# print(result.group(1))  # 第一组
# print(result.group(2))  # 第二组
#
# msg1 = '<html>abc</html>'
# msg2 = '<h1>hello</h1>'
# result = re.match(r'<[0-9a-zA-Z]+>.+</[0-9a-zA-Z]+>', msg1)
# print(result.group())
#
# result = re.match(r'<([0-9a-zA-Z]+)>(.+)<(/\1)>', msg1)  # 使用r就防止了\t的转义    ([0-9a-zA-Z]+)代表第一组   \1代表引用第一组
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
#
# msg = '<html><h1>abc</h1></html>'
# result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)<(/\2)><(/\1)>', msg)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
#
# # 起名的方式:    (?P<名字>正则)  (?P=名字)
# msg = '<html><h1>abc</h1></html>'
# result = re.match(r'<(?P<name1>[0-9a-zA-Z]+)><(?P<name2>[0-9a-zA-Z]+)>(.+)<(/(?P=name2))><(/(?P=name1))>', msg)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))

import requests

msg = requests.get('http://www.12306.cn/')
msg = msg.text
# print(msg)
result = re.findall(r'<(?P<name1>[0-9a-zA-Z]+)>(.+)<(/(?P=name1))>', msg)
print(result)

# 替换
result = re.sub(r'\d+', '100', 'java:80,python:100')
print(result)


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r'\d+', func, 'java:80,python:100')  # 替换
print(result)

result = re.split(r'[,:]', 'java:80,python:100')  # 切割
print(result)
