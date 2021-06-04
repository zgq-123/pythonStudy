'''
文件上传
保存log

系统函数：
open()
mode='rb' 二进制读
'''
# 读
# stream = open(r'C:\Users\G006696\Desktop\test.txt', mode='r',encoding='utf-8')
# print(stream.name)
# print(stream.read())

# print(stream.readable())  # 判断是否可以读
# print(stream.readlines())
# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break


# 写文件
'''
mode='w'表示写操作,每次都会把原来的内容清空
write(内容) 每次都会把原来的内容清空，然后写当前的内容

mode='a'表示写操作,不会清空之前的内容
'''
stream = open(r'C:\Users\G006696\Desktop\test.txt', mode='a', encoding='utf-8')
s = '''
你好！
    欢迎光临
           张三
'''
# stream.write(s)
# stream.write('aaaaa')
# stream.write('bbbbb')
stream.writelines('dddddddd\n')
# stream.close()  # 释放资源
