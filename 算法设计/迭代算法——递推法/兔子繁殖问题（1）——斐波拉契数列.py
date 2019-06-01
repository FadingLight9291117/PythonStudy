'''
    算法1：最简单的方法
'''
a = 1
b = 1
print("1月-->{}".format(a))
print("2月-->{}".format(b))
for i in range(3, 13):
    c = a+b
    print("{}月-->{}".format(i, c))
    a = b
    b = c
