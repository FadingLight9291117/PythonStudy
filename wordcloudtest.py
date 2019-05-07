#wordcloudtest.py
import wordcloud
w=wordcloud.WordCloud()
w.generate("Fuck your mother")
w.to_file("py.png")
