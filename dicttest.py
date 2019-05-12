def DictAdd(a, b):
    if type(a) != dict and type(b) != dict:
        print("error")
        return 0
    c = a
    for item in b:
        if item in c:
            c[item] += b[item]
            if c[item] == 0:
                del c[item]
        else:
            c[item] = b[item]
    return c


def DispDict(a, order="asc"):
    if type(a) != dict:
        print("error")
        return 0
    if order == "asc":
        l = list()
        for i in range(len(a)):
            l.append(min(a))
            l.append(a.pop(min(a), ""))
        return l
    elif order == "desc":
        l = list()
        for i in range(len(a)):
            l.append(max(a))
            l.append(a.pop(max(a), ""))
        return l

def seru(a):
    if a*10 % 1 >= 0.5:
        a = (a//0.1+1)/10
    else:
        a = a*10//1/10
    return a

a = input()
b = input()
a1 = a.split()
b1 = b.split()
a2 = dict()
b2 = dict()
for i in range(1, len(a1), 2):
    a2[a1[i]] = float(a1[i+1])
for i in range(1, len(b1), 2):
    b2[b1[i]] = float(b1[i+1])
c = DictAdd(a2, b2)
l = DispDict(c,order="desc")
print(len(l)//2, end="")
i = 1
for item in l:
    if i % 2 == 0:
        print(" {:.1f}".format(seru(item)), end="")
    else:
        print(" {:d}".format(int(item)), end="")
    i += 1