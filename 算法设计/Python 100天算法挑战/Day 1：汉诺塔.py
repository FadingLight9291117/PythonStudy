# 汉诺塔问题
count = 0


def hanoi(n, src="left", dst="right", mid="middle"):
    global count
    if n:
        hanoi(n-1, src, mid, dst)
        print("{}==>{}".format(src, dst))
        count = count+1
        hanoi(n-1, mid, dst, src)


hanoi(4)
print(count)