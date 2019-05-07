def fuck(a):
    if a*10 % 1 >= 0.5:
        a = (a//0.1+1)/10
    else:
        a = a*10//1/10
    return a


def fun(row):
    N = row[1::2]
    a = row[2::2]
    d = dict()
    for i in range(len(N)):
        d[N[i]] = float(a[i])
    return d


row1 = input().split()
row2 = input().split()
d1 = fun(row1)
d2 = fun(row2)
for item in d1:
    d1[item] += d2.pop(item, 0)
d1.update(d2)
b = set()
for item in d1:
    if d1[item] == 0:
        b.add(item)
    else:
        d1[item] = fuck(d1[item])
for item in b:
    del d1[item]
d = sorted(d1, reverse=True)
print(len(d1), end="")
for i in range(len(d1)):
    print(" {0} {1}".format(d[i], d1[d[i]]), end="")
