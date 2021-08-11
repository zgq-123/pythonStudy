'''
DataFrame是Pandas的基本结构，类似库中表或者excel中的表格数据格式
DataFrame既有行索引，也有列索引，可以看成是多个Series构成的
'''
import pandas as pd

a = {"name": ["zs", "ls"], "old": [11, 12], "tel": ["10010", "10086"]}
b = pd.DataFrame(a)
print(b)
c = [{"name": "zs", "age": 12}, {"name": "ls", "age": 12}]
d = pd.DataFrame(c)
print(d)
print(d.sort_values(by="name", ascending=False))  # 倒序
print(d[:1])
