'''
    算法2：每次循环递推三次，c=a+b,a=b+c,b=a+c
        但是并不完美，输出了14项
'''
a = 1
b = 1
print(a)
print(b)
for i in range(4):
    c = a+b
    a = c+b
    b = a+c
    print(c)
    print(a)
    print(b)
