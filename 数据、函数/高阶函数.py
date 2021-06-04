# L = range(1, 101)
#
#
# def isprimer(n):
#     flag = 1
#     for i in range(2, n):
#         if n % i == 0:
#             flag = 0
#     if flag == 0:
#         return n
#
#
# print(list(filter(isprimer, L)))

list1 = [1, 2, 3, 4, 5, 6]
r = filter(lambda x: x >= 3, list1)
print(list(r))
