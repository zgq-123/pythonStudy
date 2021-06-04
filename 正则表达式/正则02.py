import re

# msg = 'a5ugfgh^^3647'
# # result = re.search('[a-z][1-9][1-9]', msg)
# # print(result.group())
# # result = re.findall('[a-z][1-9][1-9]', msg)  # findall 匹配整个字符串
# # print(result)
# result = re.match('^[a-z][1-9a-zA-z^]+[6]', msg)
# print(result.group())

msg = 'aa.py ab.txt bb.py cc.py ac.txt'
result = re.findall('\w*.py', msg)
print(result)
