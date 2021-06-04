with open(r'C:\Users\G006696\Desktop\test.txt', mode='r') as stream:
    container = stream.read()  # 读取内容

    with open(r'C:\Users\G006696\Desktop\testCope.txt', mode='w') as wstream:
        wstream.write(container)

print('复制完成')
