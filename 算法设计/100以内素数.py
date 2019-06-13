# 100以内素数
sum = 2
for i in range(3, 101, 2):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        sum += i
print(sum)
