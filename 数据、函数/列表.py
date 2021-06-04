# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list1[-1::-2])
#
# m = 'abcdef1234'
# sum = 0
# for i in m:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# list1 = []
# list1.append('a')
# list1.append('b')
# list1.append('c')
# list1.append('d')
# print(list1)
#
# list2 = ['e']
# list2.append('f')
# print(list2)
# list1 += list2
# print(list1)
# print(list1 + [1])
# list1.extend(list2)
# print(list1)
# list1.append(1)
# print(list1)
# list1.pop(len(list1) - 1)
# print(list1)
# list1.remove('f')
# print(list1)
#
# if 'a' in list1:
#     print(True)
# else:
#     print(False)


# for i in list:
#     if i == 2:
#         list.remove(i)
# print(list)
# list.insert(0, 9)
# print(list)
# print(list.index(5))
# list.clear()
# print(list)

# list = [1, 2, 2, 3, 4, 2, 2, 5]
# print(list.count(2))
# del list[3]
#
# list1 = list
# list2 = list1
# list1.append('a')
# print(list1)
# print(list2)

# a = 'hello'
# b = a
# c = a
# del a
# print(b)
# print(c)

# list.sort(reverse=False)
# list.reverse()
# print(list)

# a = 2
# b = 3
# a, b = b, a
# print(a)
# print(b)


s = [5, 2, 1, 7, 6, 8, 3, 4]
for i in range(0, len(s) - 1):
    for j in range(0, len(s) - 1 - i):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
print(s)
