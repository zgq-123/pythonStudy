import random

import numpy as np

t1 = np.array([1, 2, 3])
print(type(t1))
print(t1)

t2 = np.array(range(10))
print(t2)

t3 = np.arange(12)
print(t3)
print(t3.dtype)  # dtype 数组内数据的类型

t4 = np.array(range(1, 4), dtype=float)
print(t4)
print(t4.astype(str))  # stype(str)  转换数据类型

print(np.array(round(random.random(), 2)))
