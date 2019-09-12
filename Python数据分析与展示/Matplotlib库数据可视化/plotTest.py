import matplotlib.pyplot as plt
import numpy as np
a = np.arange(10)
plt.xlabel('x轴', fontproperties='SimHei', fontsize=14)
plt.ylabel('y轴', fontproperties='SimHei', fontsize=14)
plt.title('标题', fontproperties='SimHei', fontsize=14)
plt.plot(a, a*1.5, a, a*2.5, a, a*3.5, a, a*4.5, 'm-1')
plt.show()
