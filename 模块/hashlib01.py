# 加密算法
import hashlib

msg = '12345654321'
md5 = hashlib.md5(msg.encode('utf-8'))  # e10adc3949ba59abbe56e057f20f883e
print(md5.hexdigest())