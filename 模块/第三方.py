# 第三方：pillow
# import pillow
import requests

response = requests.get('http://www.12306.cn/')
print(response.text)
