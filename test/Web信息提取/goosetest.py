from goose3 import Goose
url = 'http://www.baidu.com'
g = Goose({'url_meta_language': False, 'target_language': 'es'})
a=article = g.extract(url=url)
b=article.cleaned_text[:150]
print(a)
print(b)
