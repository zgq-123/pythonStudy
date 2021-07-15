# 折线图


# import requests
#
# response = requests.get('http://www.baidu.com')
# print(response.content)
# print(response.text)

'''
假设大家在30岁的时候,根据自己的实际情况,统计出来了从11岁到30岁每年交的女(男)朋友的数量如列表a,请绘制出该数据的折线图,以便分析自己每年交女(男)朋友的数量走势
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
要求:
    y轴表示个数
    x轴表示岁数,比如11岁,12岁等
'''

from matplotlib import pyplot as plt

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y1 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
plt.figure(figsize=(20, 8), dpi=80)
# 设置可显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(x, ["{}岁".format(i) for i in x], color='red', rotation=30)
plt.yticks([i / 2 for i in range(0, 13)])
plt.title("从11岁到30岁每年交的女(男)朋友的数量")
plt.xlabel("年龄")
plt.ylabel("个数")
# 绘制网格
plt.grid()
plt.plot(x, y, label="自己", color="red", linestyle=":")
plt.plot(x, y1, label="同桌", color="blue")
# 添加图例
plt.legend()

plt.show()
