# for i in range(10):
#     print(i)
# print([i for i in range(2, 101, 2)])

# print([i for i in range(1, 21) if i % 2 == 0])
# list = ['a', 'b', 'c', '1', 'd']
#
# print([i for i in list if i.isalpha()])

# list = ['apple', 'banana', 'orange']
# print([i.title() if i.startswith('a') else i.upper() for i in list])
# print({i.title() if i.startswith('a') else i.upper() for i in list})

dict = {'a': 'A', 'b': 'B'}
print({value: key for key, value in dict.items()})
print(dict.items())

print({value: key for key, value in dict.items()})

for k, v in dict.items():
    print(v, k)
