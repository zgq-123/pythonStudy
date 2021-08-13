import pandas as pd
from sqlalchemy import create_engine
import numpy as np

data1 = pd.read_csv(r'./James_Harden.csv', encoding='utf8')
# conn = create_engine('mysql+pymysql://root:123456@localhost:3306/a')
# data1.to_sql('James_Harden', con=conn)
data2 = pd.pivot_table(data1, index=['对手', '主客场'], values=['得分', '投篮命中率'], aggfunc=[np.sum, np.mean])
print(data1)
print('-' * 100)
print(data2)
print(data1['得分'].value_counts())
