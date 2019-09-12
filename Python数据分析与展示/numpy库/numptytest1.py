"简单使用numpy定义一个c数据结构体，并使用、赋值"
import numpy as np

# 定义一个学生数据类型
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(np.dtype(student))
# 赋值
a = np.array([('Diego', 12, 90), ('Eugene', 40, 75)], dtype=student)
print(a)
