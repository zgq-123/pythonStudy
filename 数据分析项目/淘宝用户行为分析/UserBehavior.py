import pandas as pd
from sqlalchemy import create_engine
import datetime

# 1.数据读取与展示
# 读取数据库
# conn = create_engine('mysql+pymysql://root:123456@localhost:3306/a')
# sql = 'select * from UserBehavior limit 1000'
# data = pd.read_sql(sql, conn)
# dataframe = data.head(1000)
# print(dataframe.isnull().sum())

# 直接读csv数据
columns = ["userid", 'itemid', 'categoryid', 'type', 'timestamp']
# 数据量过大，这里只选取前1000w行
data = pd.read_csv(r'D:\UserBehavior.csv\UserBehavior.csv', engine='python', encoding='utf-8', names=columns,
                   chunksize=100)
dataframe = data.get_chunk(100)
# 查看数据的基本信息
# dataframe.info()
# 查看缺失值
# print(dataframe.isnull().sum())
# 即返回的是唯一值的个数(统计各维度数据的数量)
# print(dataframe.nunique())

# 2.数据清洗
# 将时间戳转为日期
# 数据集说明中写的是本数据集的日期范围是2017年11月25日至2017年12月3日，所以剔除这日期以外的数据
# 时区转换to_datetime的默认时区不是中国，所以要加八小时
dataframe['time'] = pd.to_datetime(dataframe['timestamp'], unit='s') + datetime.timedelta(
    hours=8)  # unit默认是毫秒ms，而非秒，而一般的10位时间戳的单位是秒，因此需要加上这个参数;datetime.timedelta对象代表两个时间之间的时间差，两个date或datetime对象相减就可以返回一个timedelta对象。
# 保留2017.11.25-2017.12.3期间的数据
startTime = datetime.datetime.strptime("2017-11-25 00:00:00", "%Y-%m-%d %H:%M:%S")
endTime = datetime.datetime.strptime("2017-12-03 23:59:59", "%Y-%m-%d %H:%M:%S")
dataframe = dataframe[(dataframe.time >= startTime) & (dataframe.time <= endTime)]
# 按照日期和小时进行时间拆分
dataframe['date'] = dataframe.time.dt.date
dataframe['hour'] = dataframe.time.dt.hour
# 删除时间戳节约内存
dataframe.drop('timestamp', inplace=True,
               axis=1)  # axis  默认为 0，指删除行，因此删除 columns 时要指定 axis=1;inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的 新 dataframe；
# inplace=True,则会直接在原数据上进行删除操作，删除后无法返回。
print(dataframe.loc[[0]])
