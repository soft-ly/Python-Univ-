## 시각화

import matplotlib.pyplot as plt

plt.title('Axis Name Properties')
xdata = [3,5,7,9]
ydata = [1,3,5,7]

plt.plot(xdata,ydata)
plt.xlabel('X Value')
plt.ylabel('Y Value')

plt.show()  