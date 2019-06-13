def func(a):
    return a/2

a={2,5,1,2,3,4,2,4,2}
b=map(func,a)
c={eval('%d'%(item)) for item in b}
for item in c:
    print(c)