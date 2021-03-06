'''
假设你获取到了2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 单位:亿
'''
# from matplotlib import pyplot as plt
#
# a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
#      "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]
# b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
#      6.86, 6.58, 6.23]
# # 设置图片大小
# plt.figure(figsize=(20, 8), dpi=80)
# # 设置可显示中文
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
# # 调整刻度
# plt.xticks(range(len(a)), ["{}".format(i) for i in a], rotation=60)
# plt.yticks(range(0, 60, 10))
# # 添加描述信息
# plt.xlabel("电影")
# plt.ylabel("票房(亿元)")
# plt.title("2017电影票房")
# # 绘制图片
# plt.bar(range(len(a)), b, width=0.3)
# # 展示
# plt.show()





# 竖形图 plt.barh
from matplotlib import pyplot as plt

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]
# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置可显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
# 调整刻度
plt.yticks(range(len(a)), ["{}".format(i) for i in a])
plt.xticks(range(0, 60, 10))
# 添加描述信息
plt.ylabel("电影")
plt.xlabel("票房(亿元)")
plt.title("2017电影票房")
# 绘制图片
plt.barh(range(len(a)), b, height=0.3)
# 展示
plt.show()
