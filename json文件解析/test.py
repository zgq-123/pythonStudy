"""
json.dumps()	��python��������Json�ַ���
json.loads()	��Json�ַ��������python����
json.dump()	��python�еĶ���ת����json���浽�ļ���
json.load()	���ļ��е�json�ĸ�ʽת����python������ȡ
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
