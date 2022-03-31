import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.graph_objs as go

# 显示数据表全
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)
pd.set_option('display.max_columns', 100)
pd.set_option('expand_frame_repr', False)
# 设置可显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.grid()
# 读取数据
data = pd.read_csv('C:/Users/G006696/Desktop/学习文档/数据分析/实战项目/天猫订单数据分析/数据/tmall_order_report.csv')
# print(data.head(10))
# 数据的基本情况
# print(data.info())
# 规范字段名
data.rename(columns={'收货地址 ': '收货地址', '订单付款时间 ': '订单付款时间'}, inplace=True)
data['订单创建时间'] = pd.to_datetime(data['订单创建时间'])
data['订单付款时间'] = pd.to_datetime(data['订单付款时间'])
# 增加分析使用的字段
data['创建时间'] = data['订单创建时间'].dt.strftime('%m月%d日')
data['付款时间'] = data['订单付款时间'].dt.strftime('%m月%d日')


# 创建函数，用来将weekday返回的数字转换为对应的星期几
def to_weekday(a):
    result = np.nan
    if a == 0:
        result = '周一'
    elif a == 1:
        result = '周二'
    elif a == 2:
        result = '周三'
    elif a == 3:
        result = '周四'
    elif a == 4:
        result = '周五'
    elif a == 5:
        result = '周六'
    elif a == 6:
        result = '周日'
    return result


# 增加分析使用的字段
data['创建星期'] = data['订单创建时间'].dt.weekday.apply(to_weekday)
data['创建时刻'] = data['订单创建时间'].dt.hour
data['付款星期'] = data['订单付款时间'].dt.weekday.apply(to_weekday)
data['付款时刻'] = data['订单付款时间'].dt.hour
# 简化地址
data['收货地址'] = data['收货地址'].str.replace('省', '').str.replace('自治区', '')
data['收货地址'] = data['收货地址'].str.replace('壮族', '').str.replace('维吾尔', '').str.replace('回族', '')
# print(data['收货地址'].unique())
# data.to_excel('C:/Users/G006696/Desktop/新增字段后的订单.xlsx')
# 缺失值处理 缺失数量为：3293  缺失比例为14%
# print(sum(data['订单付款时间'].isnull()))
# print(sum(data['订单付款时间'].isnull())/data.shape[0])
# 检查数据 0 得知'订单付款时间'为空的时候，实际付款金额都为0，没有出现错误数据.不需要对其处理
# print(data[data['订单付款时间'].isnull() & data['买家实际支付金额']>0].size)
# 异常值分析 从下表可以看到‘总金额’的最大值远远超过75%分位数，怀疑是异常值。
# print(data.describe(percentiles=[.2, .75, .8, .95]))
# print(data.describe())
# 画个箱线图辅助判断 以看到‘总金额’>175000的数据远离上极限，且25000到175000中间都是空白，判断总金额>175000的为异常值。
# plt.boxplot(data['总金额'])
# plt.show()
# 检查该异常情况的数量：‘总金额’大于175000的数据只有一条，并且没有付款，很有可能是乱点的，将其删除。
# print(data[data['总金额'] > 175000])
data = data.drop(index=data[data['总金额'] > 17500].index)
# ’买家实际支付金额‘异常值处理
# plt.boxplot(data['买家实际支付金额'])
# plt.show()
# 查看实际支付金额大于6000的数据：付款金额不是十分高，而且数量只有2，符合实际，不处理。
# print(data[data['买家实际支付金额'] > 6000])
# 退款金额 异常值处理:
# plt.boxplot(data['退款金额'])
# plt.show()
# 查看退款金额大于2000的数据 :退款金额=总金额，没有出现数据错误，而且数量少，符合生活中的实际情况，不处理。
# print(data[data['退款金额'] > 2000])
# 重复值处理 0：没有重复值
# print(data.duplicated().sum())

# 数据分析:描述性统计
data_desc = data.copy()
# '订单付款时间'为空的代表买家没有付款，对应的'买家实际支付金额'为0的在描述性统计时应当成空值而不是0；
# ‘退款金额’为0代表没有退款，在进行描述性统计时也应当成空值处理。

data_desc['买家实际支付金额'] = np.where(data_desc['订单付款时间'].isnull(), np.nan, data_desc['买家实际支付金额'])
data_desc['退款金额'] = data_desc['退款金额'].replace(0, np.nan)
# print(data_desc.describe())
'''
初步了解一下数据：
订单情况:共记录28009条订单，其中买家实际支付订单24807条（86.0%），买家有退款行为的订单5646条（占实际支付23.4%）
订单总金额：平均每单订单100.2元，金额最小1元，金额最大16065元
实际支付金额：实际支付订单平均每单79元，金额最小0元，金额最大16065元
退款金额：退款订单平均每单退101.4元，金额最小1元，金额最大3800元    
'''
# 总体销售情况
# print(np.sum(data_desc['买家实际支付金额'])) 1902487.15 总销售额
GMV_day = data_desc[data_desc['付款时间'] != 'NaT'].groupby('付款时间').sum()
order_day = data_desc[data_desc['付款时间'] != 'NaT'].groupby('付款时间').count()
# with pd.ExcelWriter('C:/Users/G006696/Desktop/a.xlsx') as writer:
#     GMV_day.to_excel(writer, sheet_name='销售额')
#     order_day.to_excel(writer, sheet_name='销售量')
# 绘制2020年2月销售额走势图
trace1 = go.Scatter(x=GMV_day.index, y=GMV_day['买家实际支付金额'], mode='lines', marker=dict(color='orange'), name='销售额')
trace2 = go.Bar(x=order_day.index, y=order_day['订单编号'], name='订单数', marker=dict(color='steelblue'), yaxis='y2',
                opacity=0.7)
layout = go.Layout(title='2020年2月销售额走势', xaxis=dict(tickangle=45, dtick=1), yaxis=dict(title='销售额（元）', zeroline=False),
                   yaxis_tickformat='auto', yaxis2=dict(title='订单数', overlaying='y', side='right', showgrid=False),
                   annotations=[
                       dict(x=0.1, xref='paper', y=0.95, yref='paper', text='二月份总销售额为190.25万', bgcolor='gainsboro',
                            font={'size': 13}, showarrow=False)],
                   legend=dict(x=0.1, y=0.85))
trace = [trace1, trace2]
fig = go.Figure(trace, layout)
# fig.show()
'''
从上图可以得知以下消息：
二月份总销售额190.5万元
2月16日前销售额很少，仅2月4日和2月9日达到两个小高峰，22000左右
2月10日-2月16日销售额仅有0-1000元
2月17日销量逐渐增长，2月25日达到最高峰（22.8万）
3月1日的销售额突然骤减，仅有298元

问题分析：
2月初销量低可能因为春节假期导致，2020的春节放假为1月24日至2月2日，当时正至疫情开始，复工复产时间推迟至不早于2月9日24时，2月10日-2月16日正好是销售量最低迷的时间，应该是因为消费者正开始复工复产，无暇消费
3月1日销售额突降是因为改日订单只记录了在2月29日创建但在3月1日支付的，并不是3月1日所有的交易数据，可以忽略3月1日

建议：
2020年初疫情突发，导致本应在2月初春节结束恢复的销售，推迟至月中，甚至出现了日销量为0的情况。目前疫情已经常态化，应该准备多个应急方案，保证在突发事件发生时能及时举措，减少突发状况对销售的影响，如果竞争对手没有及时反应我司甚至能拔得头筹获得佳绩。
'''
# 周趋势、日趋势分析
week_order = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
data_week_mean = [data_desc.groupby('付款星期').sum()['买家实际支付金额'].loc[i] for i in week_order]
data_week_count = [data_desc.groupby('付款星期').count()['订单编号'].loc[i] for i in week_order]
# 每个月周n数量是不固定的，如果单纯按周分组求和，数量多的周n会占优势，需要求平均值
data_week_mean = np.divide(data_week_mean, [4, 4, 4, 4, 4, 5, 4])
data_week_count = np.divide(data_week_count, [4, 4, 4, 4, 4, 5, 4])
# 绘制周销售趋势图
trace_week1 = go.Scatter(x=week_order, y=data_week_mean, name='平均销售额', marker=dict(color='orange'))
trace_week2 = go.Bar(x=week_order, y=data_week_count, name='平均订单数', opacity=0.7, yaxis='y2',
                     marker=dict(color='steelblue'))
trace_week = [trace_week1, trace_week2]
layout1 = go.Layout(title='周趋势分析', yaxis=dict(title='销售额（元）'), yaxis2=dict(title='订单数', overlaying='y', side='right'),
                    legend=dict(x=0.9, y=1.4), width=550, height=350)
fig1 = go.Figure(trace_week, layout1)
# fig1.show()
# 绘制日销售趋势图
data_hour_count = data_desc.groupby('付款时刻').count()
data_hour_mean = data_desc.groupby('付款时刻').sum()
trace_hour1 = go.Scatter(x=data_hour_mean.index, y=data_hour_mean['买家实际支付金额'], name='销售额', marker=dict(color='orange'))
trace_hour2 = go.Bar(x=data_hour_count.index, y=data_hour_count['订单编号'], name='订单数', opacity=0.7,
                     marker=dict(color='steelblue'), yaxis='y2')
trace_hour = [trace_hour1, trace_hour2]
layout2 = go.Layout(title='日趋势分析', yaxis=dict(title='销售额（元）'), yaxis2=dict(title='订单数', overlaying='y', side='right'),
                    legend=dict(x=0.9, y=1.4), width=550, height=350)
fig2 = go.Figure(trace_hour, layout2)
# fig2.show()
'''
从上图我们可以得到以下消息:
每周销售最好的是周五,其次是周二,最差的是周一
周末并非预想中最好的时间,甚至比大部分工作日差
凌晨销量最低,从6点开始销量稳定提升,中午开始趋于稳定略有波动,在10时 15时 21时分别有一个高峰,22点后销量开始下滑

建议:
促销活动安排在周五开始,既可以提高原本的高销量,又可以拉到周末的消费
促销信息、产品推广广告的推送时间最好安排在晚上9点,此时消费人数最多,信息的曝光量最大,能带来最大的收益
如果有条件多次推送信息,10点、15点、21点时较好的选择
'''
# 产品价格分析:因为数据集中即没有包含产品名称，也没有包含产品价格，我们姑且将订单总金额当成产品的价格，分析什么价格的产品更受消费者欢迎
sns.histplot(data_desc['总金额'])
# plt.show()
'''
总金额500以上的数据虽然很少但刻度很大，包含进来严重拉伸了图形，不利于分析。
筛选总金额500以内的数据，绘制直方图查看分布。
'''
plt.figure(figsize=(20, 8), dpi=80)
sns.histplot(data_desc[data_desc['总金额'] < 500]['总金额'])
plt.xticks(np.arange(0, 525, 25), fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('订单金额', fontsize=20)
plt.ylabel('订单数', fontsize=20, rotation=0, labelpad=40)
plt.title('订单金额分布情况', fontsize=25)
# plt.show()
'''
可以看到大部分订单金额在200元以下,20-125居多
'''
# 根据上图分布,对订单总金额进行分组
price_max = data_desc['总金额'].max()
bins = [0, 20, 40, 60, 80, 100, 125, 150, 175, 200, 250, 300, 500, price_max]
price_label = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-125', '125-150', '150-175', '175-200', '200-250',
               '250-300', '300-500', '500以上']
price_cut = [pd.cut(data_desc['总金额'], bins=bins, labels=price_label).value_counts()[i] for i in price_label]
plt.figure(figsize=(20, 8), dpi=80)
sns.barplot(x=price_label, y=price_cut, palette='Blues_r')
x = [i for i in range(len(price_label))]
for i, j in zip(x, price_cut):
    plt.text(i, j + 60, j, horizontalalignment='center', fontdict=dict(color='steelblue', fontsize=14))
    plt.text(i, j - 270, '{:.1%}'.format(j / data_desc.shape[0]), horizontalalignment='center',
             fontdict=dict(color='darkturquoise', fontsize=14))
plt.xticks(ticks=x, labels=price_label)
plt.tick_params(pad=10)
plt.xlabel('订单金额', fontsize=12)
plt.ylabel('订单数', rotation=0, labelpad=25, fontsize=12)
plt.title('订单金额分布情况', fontsize=15)
# plt.show()
'''
从上图我们可以获得以下信息：
大部分订单订单金额在200元以下，尤其是20-125元
其中20-40元的订单量最大，占了总订单量的1/4
20元以下和175元以上的订单很少，加起来仅占总订单量的11%
即20-175元的订单占了订单总量的90%
建议:
产品推广以价格20-175元的产品为主，尤其着重推广20-40元的产品，这个价格区间的产品是消费者最喜欢消费的
'''
# 地区分析
# 条形图
data_area = data_desc.groupby('收货地址').sum()['买家实际支付金额'].sort_values(ascending=False).reset_index()
plt.figure(figsize=(20, 8), dpi=80)
sns.barplot(x='收货地址', y='买家实际支付金额', data=data_area, palette='Blues_r')
plt.ylabel('销售额', fontsize=15)
plt.title('各省市销售额情况', fontsize=20)
# plt.show()
# 地图
from pyecharts.charts import Map
from pyecharts import options as opts

data_area_list = [list(i) for i in zip(data_area['收货地址'], np.round(data_area['买家实际支付金额']))]
map = Map()
map.add('销售额', data_area_list, maptype='china', is_map_symbol_show=True)  # is_map_symbol_show 是否显示标记红点
map.set_global_opts(title_opts=opts.TitleOpts(title='各省市销售额', pos_left='center'),
                    visualmap_opts=opts.VisualMapOpts(min_=0, max_=data_desc['总金额'].max() * 10,
                                                      range_color=['#D7E3EF', '#006699']),
                    legend_opts=opts.LegendOpts(is_show=False))
map.render('map1.html')
'''
从上面两张图我们可以知道以下信息：
销售额最高的省市是上海，北京、江苏、广东、浙江为第二梯队
销售额高的省市主要集中在东部和南部沿海，以及四川省
销售额最少的省市为西藏、青海、湖北、新疆、宁夏， 主要为西部地区

分析：
湖北此时处于疫情中心，销售额低属于情理之中
从上文得知，目前销量最高的产品价格集中在20-125元，尤其是20-40元。产品价格不高，而且往往对西部偏远省份不包邮，因而在考虑成本的情况下很难提升这些地区的销量，所以建议以提高西南、中部以及东北地区的销量为先，逐渐寻找发展西部地区销量的对策

建议：
保持优势省市的订单量
西南、中部以及东北地区有很大的发展潜力，建议先从这些地区开始开展促销提高销量
'''
# 转化率分析
# 本项目中，用户行为路径为：创建订单->订单付款->订单成交->订单全额成交
# 计算各个阶段订单数
data_create = data.shape[0]
data_pay = data_desc[data_desc['订单付款时间'].notnull()].shape[0]
data_pay_part = data_desc[data_desc['买家实际支付金额'] > 0].shape[0]
data_pay_all = data_desc[data_desc['买家实际支付金额'] == data_desc['总金额']].shape[0]
# 计算转化率
data_funnel = pd.DataFrame()
data_funnel['环节'] = ['下单', '付款', '成交', '全额成交']
data_funnel['订单量'] = [data_create, data_pay, data_pay_part, data_pay_all]
data_funnel['总体转化率%'] = np.round(data_funnel['订单量'] / data_funnel['订单量'][0], 3) * 100
data_funnel['付款订单转化率%'] = np.round(data_funnel['订单量'] / data_funnel['订单量'][1], 3) * 100
data_funnel.loc[0, '付款订单转化率%'] = np.nan
print(data_funnel)
# 绘制总转化率漏斗
from pyecharts.charts import Funnel

funnel1 = Funnel(init_opts=opts.InitOpts(width="600px", height="400px"))
funnel1.add(series_name="转化率", data_pair=list(zip(data_funnel['环节'], data_funnel['总体转化率%'])), gap=2,
            label_opts=opts.LabelOpts(position='inside', formatter='{b}：{c}%'),
            tooltip_opts=opts.TooltipOpts(formatter='{a} <br/>{b} : {c}%'))
funnel1.set_colors(colors=['#B0CDDD', '#5C96BB', '#3470A3', '#163A69'])
funnel1.set_global_opts(title_opts=opts.TitleOpts(title='总体转化率', subtitle='相比总下单数', pos_left='center'),
                        legend_opts=opts.LegendOpts(is_show=False))
funnel1.render('funnel1.html')
# 绘制付款订单转化率漏斗图
funnel2 = Funnel(init_opts=opts.InitOpts(width="600px", height="400px"))
funnel2.add(series_name="转化率", data_pair=list(zip(data_funnel['环节'][1:], data_funnel['付款订单转化率%'][1:])), sort_='none',
            gap=2, label_opts=opts.LabelOpts(position='inside', formatter='{b}：{c}%'),
            tooltip_opts=opts.TooltipOpts(formatter='{a} <br/>{b} : {c}%'))
funnel2.set_colors(colors=['#ffd460', '#ffaa64', '#ff8264'])
funnel2.set_global_opts(title_opts=opts.TitleOpts(title='付款订单转化率', subtitle='相比付款订单数', pos_left='center'),
                        legend_opts=opts.LegendOpts(is_show=False))
funnel2.render('funnel2.html')
'''
从上面的漏斗图我们可以知道：
下单订单的付款率为86%
付款订单里78.7%的订单成交
付款订单里76.6%的订单为全额成交，即有23.4%的订单存在退款行为
分析：
付款订单里23.4%的订单存在退款行为，虽然价格不高，但是商品质量或其他方面存在令人不满意的地方，加大力度整改

建议：
23.4%的退款率说明商品存在的问题比较严重，应尽快找出问题所在（质量不达标、实物与图片不符、尺寸与标注不符、包装不好导致商品破损、快递运输过慢、发货出错、价格高于其他店铺...）
'''

'''
总结：
2月总销售额为190.25万元
为了增加销售，可以从以下几方面开展行动：
找到导致高退款率的原因并解决，这是目前最重要的事情
促销活动可以安排在周五
促销信息、产品推广广告的推送时间最好安排在晚上9点，其次是10点、15点
产品推广以价格20-125元或20-175元的产品为主，尤其着重推广20-40元的产品
保持优势省市的订单量，大力发展西南、中部以及东北地区的销量
'''
