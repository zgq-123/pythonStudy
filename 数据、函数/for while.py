import random

# print('hello python')
# cai = random.randint(1, 10)
# print(cai)
# while True:
#     result = input('请输入数字:\n')
#     if int(result) == cai:
#         print('正确')
#         break
#     else:
#         input('错误，重新输入\n')
# for i in range(1, 11):
#     print(i)
# sum1 = 0
# for i in range(1, 11):
#     if i == 1:
#         sum1 += i
#         break
# print(i)
# print(101 // 10)
# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)
# n = 1
# while n <= 5:
#     print('*' * n)
#     n += 1
# n = 1
# while n <= 5:
#     m = 1
#     while m <= n:
#         print('*', end='')
#         m += 1
#     n += 1
#     print()

# for n in range(5):
#     for m in range(n + 1):
#         print('*', end='')
#     print()

# for n in range(5):
#     for m in range(n+1):
#         print('*', end='')
#     print()

for n in range(5, 0, -1):
    print(n * '*')
