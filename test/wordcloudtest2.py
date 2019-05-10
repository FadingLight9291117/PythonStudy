import jieba
import wordcloud
txt="程序设计语言是计算机能够理\
解识别用户操作意图的一种交互体系。"
w=wordcloud.WordCloud(width=1000,font_path="msyh.ttc",\
                      height=700,background_color="white")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("img/pycloud2.png")
    
