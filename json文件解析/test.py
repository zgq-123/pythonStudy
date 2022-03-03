"""
json.dumps()	将python对象编码成Json字符串
json.loads()	将Json字符串解码成python对象
json.dump()	将python中的对象转化成json储存到文件中
json.load()	将文件中的json的格式转化成python对象提取
"""
import json

with open(r"./student.json", encoding='utf-8', mode='r') as f:
    f_read = f.read()
data = json.loads(f_read)
save_data = data['content']
print(save_data)
with open('./copy.json', encoding='utf-8', mode='w') as f:
    json.dump(save_data, f, indent=0, ensure_ascii=False)
f.close()
