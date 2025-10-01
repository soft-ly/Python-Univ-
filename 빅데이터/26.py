# scatter
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iris_flower.csv')
print(data)

PetalLength = data['PetalLength']
PetalWidth = data['PetalWidth']

plt.figure(figsize=(10,4))
plt.scatter(PetalLength, PetalWidth)

plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Petal Scatter Graph')
plt.grid()
plt.show()