import numpy as np
a = np.linspace(1, 10, 4)
print(a)
b = np.linspace(1, 10, 4, endpoint=False)
print(b)
c = np.concatenate((a, b))
print(c)
