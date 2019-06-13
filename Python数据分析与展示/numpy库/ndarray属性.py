"ndarray属性测试"
import numpy as np
a = np.arange(10, dtype='int16').reshape(5, 2)
print(list(a))
print("维度为:{} ".format(a.ndim))
print("尺度:{}".format(a.shape))
print("个数:{}".format(a.size))
print("元素类型:{}".format(a.dtype))
print("元素大小:{}".format(a.itemsize))
