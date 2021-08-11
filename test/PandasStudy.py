import pandas as pd
import numpy as np

# series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(series1)
#
# series2 = pd.Series({'北京': 10, '杭州': 20})
# print(series2)
# print(series2.ndim)  # 维度

list1 = [['zs', 23, '男'], ['ls', 21, '男'], ['wh', 18, '女']]
df1 = pd.DataFrame(list1, columns=['姓名', '年龄', '性别'])
print(df1)
print(df1.shape)
print(df1.values)
print(df1.dtypes)
print(df1.columns.tolist())
