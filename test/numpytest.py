import numpy as np


def numsum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a**b

    return c

a=numsum()
print(a)
print(type(a))