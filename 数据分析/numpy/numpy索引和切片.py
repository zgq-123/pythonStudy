import numpy as np

file_path = './test.txt'
t1 = np.loadtxt(file_path, delimiter=",", dtype="int")
print(t1[2])  # 取第三行数据
print("-" * 70)
print(t1[1:])  # 取多行（2、3行）
print("-" * 70)
print(t1[[0, 2]])  # 取不连续多行（1行和三行）
print("-" * 70)
print(t1[1, 1])  # 取第2行第2列
print("-" * 70)
print(t1[:, 1])  # 取所有行第2列
print("-" * 70)
print(t1[:, [0, 2]])  # 取所有行的第1列和第三列
print("-" * 70)
t2 = np.where(t1 < 5, 100, t1)  # 改变值
print(t2)
print("-" * 70)
t3 = t1.clip(3, 7)  # 改变值
print(t3)
