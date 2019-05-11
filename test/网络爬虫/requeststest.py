import requests
r=requests.get('http://api.github.com/user',auth=('user','pass'))
print(r.headers['content-type'])