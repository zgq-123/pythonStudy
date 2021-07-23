import re

import pandas as pd

# 读取文件并合并
city_list = '北京,上海,广州,深圳'.split(',')
path_list = [f'数据/{i}历史天气.xlsx' for i in city_list]
df_list = []
for path in path_list:
    df = pd.read_excel(path)  # <class 'pandas.core.frame.DataFrame'>
    df['地区'] = path[2:4]  # 新增一列地区
    # 现将表构成list，然后在作为concat的输入
    df_list.append(df)  # 合并四个表格的数据
df_p = pd.concat(df_list)  # <class 'pandas.core.frame.DataFrame'> 数据合并与重塑,将数据根据不同的轴作简单的融合
# print(df_p)
# 数据清洗
df_p['空气质量等级'] = df_p['空气质量指数'].map(lambda i: re.compile(r'\s(\w{1,15})').findall(i)[0])
print(type(df_p['空气质量等级']))
print(df_p['空气质量等级'])

df_p.head(n=10)  # 它是指返回行数的整数值。
