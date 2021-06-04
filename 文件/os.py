import os
import shutil

# path = os.path.dirname(r'C:\Users\G006696\Desktop\test.txt')
# print(path)
# result = os.path.join(path, 'testCope.txt')
# print(result)
#
# print(os.path.split(result)[1])
# print(os.path.splitext(result))
# print(os.path.getsize(path))

print(os.getcwd())

result = os.listdir(r'C:\Users\G006696\Desktop\学习文档')  # 该文件夹内所有的文件
print(result)

# os.mkdir(r'C:\Users\G006696\Desktop\python')  # 创建文件夹
# os.rmdir(r'C:\Users\G006696\Desktop\python')  # 删除文件夹
# os.removedirs(r'C:\Users\G006696\Desktop\python')  # 删除文件夹
# os.path.exists()

shutil.rmtree(r'C:\Users\G006696\Desktop\python')  # 文件夹内有内容也可以删
