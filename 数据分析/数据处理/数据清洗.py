import pandas as pd
from sqlalchemy import create_engine
import numpy as np

conn = create_engine('mysql+pymysql://root:123456@localhost:3306/a')
sql = 'select * from e'
data = pd.read_sql(sql, con=conn)
# print(data)
# print(data.duplicated(subset=['company']))
# # 删除重复值
# print(data.drop_duplicates(subset=['company']))  # drop_duplicates()


# 缺失值的处理
# print(data.isnull())
# print(np.mean(data['salary']))
# print(data.dropna())
# 用平均值来补充薪资为null的值
print(data.salary.fillna(data.salary.mean()))
# 用中位数来补充薪资为null的值
print(data.salary.fillna(data.salary.median()))
# 用众数来补充公司名称为null的值
data.company.fillna(data.company.mode(), inplace=True)
print(data)
# 用前一项的值来填补
data.fillna(method='ffill', inplace=True)
print(data)

# 异常值处理

# 数据离散化
print(pd.cut(data['salary'], [0, 1000, 1500, 1700], labels=['低', '中', '高']))
data.loc[:, '等级'] = pd.cut(data['salary'], [0, 1000, 1500, 1700], labels=['低', '中', '高'])
data['salary'].hist()
