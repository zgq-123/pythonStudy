import numpy as np

file_path = './test.txt'
t1 = np.loadtxt(file_path, delimiter=",", dtype="int")
t2 = np.loadtxt(file_path, delimiter=",", dtype="int", unpack=True)  # 相当于转置
print(t1)
print('-' * 40)
print(t2)
print(t2.T)  # 转置
