'''
Series
由一组数据以及一组与之对应的数据标签（即索引）组成
可以通过pandas.Series来创建Series，每个Series可以看成是DstaFrame的一个列
'''
import string

import pandas as pd

a = [1, 2, 3, 4]
print(type(a))
b = pd.Series(a)
print(type(b))
print(b)
c = pd.Series(a, list("abcd"))
print(c)
d = {"name": "zs", "old": 18}
print(pd.Series(d))
e = pd.Series(d)
print(e["name"])
print(e[1])

print(list(string.ascii_uppercase[0:26]))

# 读取csv文件
m = pd.read_csv("./test.csv", encoding='gbk', sep=',', header=None)
print(m)
