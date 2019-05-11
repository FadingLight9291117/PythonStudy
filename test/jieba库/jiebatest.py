#jiebatest.py
#结巴库的使用
import jieba
a=jieba.lcut("我是中华人民共和国,人民！")
for item in a:
    print(item)