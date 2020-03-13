import requests
from bs4 import BeautifulSoup

a = requests.get("http://www.baidu.com")
print(a.status_code)
a.encoding = a.apparent_encoding
soup = BeautifulSoup(a.content)
b = soup.prettify()
print(b)