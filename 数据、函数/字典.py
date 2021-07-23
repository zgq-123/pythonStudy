a = {}
a['name'] = 'zs'
a['old'] = 18
a['old'] = 20
print(a)
print(a.get('old1', '无'))
print(list(a.values()))
print(list(a.keys()))
print(a.items())
for i in a.items():
    print(type(a))
    print(i)

for k, v in a.items():
    print(k, v)
