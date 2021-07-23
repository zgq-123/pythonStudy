import re

msg = '佟丽娅娜扎热巴戴斯佟丽娅'
pattern = re.compile('佟丽娅')
print(type(pattern))
print(pattern)
result = pattern.findall(msg)
print(result)  # <re.Match object; span=(0, 3), match='佟丽娅'>

# 使用正则re模块方法：match
# msg = '佟丽娅娜扎热巴戴斯佟丽娅'
# result = re.match('佟丽娅', msg)  # 只要从开头进行匹配，如果匹配不成功则就返回None
# print(result)
#
# result = re.search('佟丽娅', msg)  # search 进行正则字符串匹配方法，匹配的是整个字符串
# print(result.span())  # 返回位置
#
# print(result.group())  # 提取匹配到的内容
# print(result.groups())
