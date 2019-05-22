import copy
a=[2,4,2,[2,3,2],2,2]
b=copy.deepcopy(a)
a[3][0]=1
print(a)
print(b)