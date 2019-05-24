def judge(a):
    if a > 10:
        return True
    else:
        return False


List = {1, 4, 2, 1, 20, 42, 12, 3, 44}
a = filter(judge, List)
for item in a:
    print(item)