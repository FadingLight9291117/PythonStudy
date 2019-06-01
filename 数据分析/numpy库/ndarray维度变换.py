import numpy as np
li=[3,3,3,3,1,1,1,1]
a = np.array(li).reshape(2,4)
print(a)
b=a.swapaxes(0,1)
print(b)
del b
print(b)