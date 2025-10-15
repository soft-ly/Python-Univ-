## 선 모양, 그림 범위 지정

## 시각화

import matplotlib.pyplot as plt

plt.title('Axis Name Properties')

data1 = [1,3,5,7]
data2 = [9,7,5,3]

plt.plot(data1, color = 'b', label = 'dashed', linestyle = '--')
plt.plot(data2, color = 'r', label = 'dotted', linestyle = ':')
plt.legend()
plt.show()  