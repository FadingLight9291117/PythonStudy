def fuck(a):
    if a*10%1>=0.5:
        a=(a//0.1+1)/10
    else:
        a=a*10//1/10
    return a
a=12.23
# a=fuck(a)
b=a*10//1/10
print(b)