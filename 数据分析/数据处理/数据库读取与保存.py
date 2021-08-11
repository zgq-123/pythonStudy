import pymysql
from sqlalchemy import create_engine
import pandas as pd

# # 建立连接
# conn = create_engine('mysql+pymysql://root:123456@localhost:3306/d')
# sql = 'select * from d'
# df1 = pd.read_sql(sql, conn)
# print(df1.head(10))

# def query(table):
#     host = 'localhost'
#     user = 'root'
#     passward = '123456'
#     database = 'a'
#     port = 3306
#     conn = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(user, passward, host, port, database))
#     sql = 'select * from {}'.format(table)
#     df1 = pd.read_sql(sql, conn)
#     print(df1.head(10))
#
#
# query('b')

# 将表格内的数据导入数据库
conn = create_engine('mysql+pymysql://root:123456@localhost:3306/a')
df = pd.read_excel(r'./天气/上海历史天气.xlsx')
# df.to_sql('tsetdf', con=conn)

