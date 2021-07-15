import random
from tkinter import font

from matplotlib import pyplot as plt

# x = range(2, 26, 2)
# y = range(1, 13, 1)
x = range(0, 40)
y = [random.randint(20, 35) for i in range(40)]
# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置可显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
# 设置x的刻度
plt.xticks(x, ["{}时".format(i) for i in x], color='red', rotation=60)
# 设置y的刻度
plt.yticks(y)
# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的变化情况")
# 绘制网格
plt.grid()
# 绘制图片
plt.plot(x, y)
# 展示图片
plt.show()
# 保存图片
# plt.savefig("./sig_size.png")


# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
# print(y)
# plt.plot(x, y)
# plt.show()
