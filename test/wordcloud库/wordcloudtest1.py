import wordcloud
txt="lift is short, you need python"
w=wordcloud.WordCloud(\
    background_color="white")
w.generate(txt)
w.to_file("img/pycloud.png")
