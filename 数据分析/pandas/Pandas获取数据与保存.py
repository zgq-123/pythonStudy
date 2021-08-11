import os
import pandas as pd

print(os.getcwd())
df = pd.read_excel(r'../../test/天气/上海历史天气.xlsx')
# print(df)
# print(df.columns)
# print(df.dtypes)
# print(df.shape)
# print(df[['日期', '风力风向']][:50])  # 选取这两列的前50行
# print(df[:50])  # 选取所有列的前50行
# print(df.loc[0:2, '日期'])
# loc按标签来找，iloc按索引来找
# print(df.loc[df['最高温'] == '22°'])  # 条件筛选
# print(df.iloc[:, [2, 3]])
