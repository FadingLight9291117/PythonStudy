def prime(m):
    n = int(m)
    if m - n > 0:
        n = n+1
    l = list()
    i = 0
    while True:
        if i == 5:
            break
        for j in range(2, n//2+1):
            if n % j == 0:
                break
        else:
            i += 1
            l.append(n)
        n += 1

    return l


n = eval(input())
l = prime(n)
l = str(l)
l = l.strip('[]')
l = l.replace(" ", '')
print(l)
