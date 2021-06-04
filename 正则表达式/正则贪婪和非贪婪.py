# 贪婪   一般有量词的就是贪婪
# 非贪婪  量词？
import re

msg = 'abc123'
# 贪婪模式
result = re.match(r'abc(\d+)', msg)
print(result.group())  # abc123
# 非贪婪模式
result = re.match(r'abc(\d+?)', msg)
print(result.group())  # abc1
