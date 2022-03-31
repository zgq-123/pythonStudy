import re

'''
s = [110, 'dog', 'cat', 120, 'apple']
s.insert(2, [])
# s.remove('apple')
s.pop(-1)
a, b = s[0], s[-1]
# print(a, b)
print(s)
'''
s = "Apple's unit price is 9 yuan"
num = re.findall(r'\d', s)[0]
print(num)
