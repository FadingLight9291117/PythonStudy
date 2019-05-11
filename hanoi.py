# 汉诺塔问题
count = 0


def hanoi(n, src, dst，mid):
    if n == 1:
        print("{}->{}".format(src, dst))
    else:
        return hanoi(n-1,)
