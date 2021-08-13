'''
假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?

a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
'''
from matplotlib import pyplot as plt

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]
x_3 = range(1, 32)
x_10 = range(51, 82)
# 设置图片大小
plt.figure(figsize=(22, 9), dpi=80)
# 设置可显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
# 调整刻度
# x刻度
_x = list(x_3) + list(x_10)
_xticks_labels = ["3月{}日".format(i) for i in x_3]
_xticks_labels += ["10月{}日".format(i) for i in range(1, 32)]
plt.xticks(_x, _xticks_labels, rotation=60)
# y刻度
_y = list(y_3) + list(y_10)
_yticks_labels = ["{}度".format(i) for i in _y]
plt.yticks(_y, _yticks_labels)
# 绘制图片
plt.scatter(x_3, y_3, label="3月")
plt.scatter(x_10, y_10, label="10月")
# 添加图例
plt.legend()
# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("3月和10月温度散点图")
# 绘制网格
plt.grid()
# 展示
plt.show()
