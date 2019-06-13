# 普通文件操作
a = open('./files/file.txt', 'w', encoding='utf-8')
a.write("sad")
a.close()
with open('./files/file.txt', 'r', encoding='utf-8') as file:
    a = file.read()
    print(a)
