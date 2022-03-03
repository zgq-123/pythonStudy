import pandas as pd
from pandas._libs.reshape import explode
from sqlalchemy import create_engine
import datetime
from matplotlib import pyplot as plt

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
                   chunksize=10000000)
dataframe = data.get_chunk(10000000)
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
# print(dataframe.info())

# 数据分析
# 用户行为分析
total_unique_users = dataframe.userid.nunique()  # 独立访问客户数uv
total_unique_itemid = dataframe.itemid.nunique()  # 有操作的商品
total_unique_categoryid = dataframe.categoryid.nunique()  # 有错做的商品类目
user_bought_count = dataframe[dataframe['type'] == 'buy'].userid.nunique()  # 付费用户数
total_nobought_count = total_unique_users - user_bought_count  # 非付费用户数
# print(f"          UV：{total_unique_users}")
# print(f"      商品数：{total_unique_itemid}")
# print(f"      类目数：{total_unique_categoryid}")
# print(f"  付费用户数：{user_bought_count}")
# print(f" 非付费用户数：{total_nobought_count}")
# print(f"付费用户占比：{user_bought_count / total_unique_users * 100:.2f}%")

# 绘制不同行为类型饼状图
type_series = dataframe.type.value_counts()  # value_counts是对某列作处理——“获取该列不同值出现的频数”
plt.figure(figsize=(20, 8), dpi=80)
plt.pie(x=type_series, labels=type_series.index, autopct='%.2f%%')
# plt.show()

# 取消科学计数法，保留两位小数
pd.set_option("float_format", lambda x: "%.2f" % x)
# 9日内各个行为的操作总数，每日平均操作数，每日平均操作用户数记录
type_df = pd.DataFrame([type_series, type_series / 9, type_series / total_unique_users],
                       index=['total', 'avg_day', 'avg_user'])
# 付费用户行为记录
type_df.loc['paying_user'] = dataframe[
    dataframe['userid'].isin(dataframe[dataframe['type'] == 'buy']['userid'])].type.value_counts()
# print(type_df)

# 跳失率和复购率
'''
跳失率=只有点击行为的用户/总用户数
    其实真正的跳失率应该是只浏览一个页面就离开的访问次数 / 该页面的全部访问次数；这边只是为了突出这些有待发展的客户
复购率=购买两次及以上用户数/总购买用户数
    复购率可以分为按客户计算和按交易计算，这里我采用的是按客户计算。一定要确定统计周期，这个数据的统计周起就是9天
'''
groupby_userid = dataframe.groupby(by='userid')  # 488813
print(groupby_userid.head().count())
