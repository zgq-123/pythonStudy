# import json
#
# with open(r'D:\pythonWorkSpace\pythonStudy\json文件解析\student.json', encoding='utf-8', mode='r') as f:
#     f_read = f.read()
# data = json.loads(f_read)
# print(data)
# save_data = data['code']
# print(save_data)
# print(data['content']['EG_zhibiao6'])
# print(data['content'])


import json

with open(r'D:\pythonWorkSpace\pythonStudy\json文件解析\student.json', encoding='utf-8', mode='r') as f:
    f_read = f.read()
data = json.loads(f_read)
print(data)
print(data['code'])
print(data['content'])
print(data['content']['EG_zhibiao6'])
data['content']['EG_zhibiao6'] = '不正常'
print(data)

with open(r'D:\pythonWorkSpace\pythonStudy\json文件解析\copy.json', encoding='utf-8', mode='w') as fp:
    json.dump(data, fp, indent=0, ensure_ascii=False)
fp.close()
