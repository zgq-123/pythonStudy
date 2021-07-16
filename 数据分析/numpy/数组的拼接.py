import numpy as np

a1 = ([[1, 2, 3], [7, 8, 9]])
a2 = ([[4, 5, 6], [10, 11, 12]])
x = np.vstack((a1, a2))  # 竖直拼接
print(x)
print('-' * 70)
y = np.hstack((a1, a2))  # 水平拼接
print(y)
print('-' * 70)
print(np.random.randint(10, 20, (4, 5)))
