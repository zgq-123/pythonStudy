import pandas as pd
from sqlalchemy import create_engine

data1 = pd.read_excel(r'../../test/天气/上海历史天气.xlsx').head(10)
data2 = pd.read_excel(r'../../test/天气/北京历史天气.xlsx').head(10)
print(data1.head(10))
print('-' * 100)
print(data2.head(10))
print('-' * 100)
data3 = pd.concat([data1, data2], axis=0, ignore_index=True)
print(data3)
print('-' * 100)
# 保存至excel
# data3.to_excel(r'../../test/天气/合并天气.xlsx')
# 保存至数据库
# conn = create_engine('mysql+pymysql://root:123456@localhost:3306/a')
# data3.to_sql('合并天气', con=conn)
data3.sort_values('日期', inplace=True, na_position='first')
print(data3)
