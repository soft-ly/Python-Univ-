##histogram

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('iris_flower.csv')
print(data)

versicolor_PetalLength = data.loc[data.Species == 'versicolor',['Species','PetalLength']]
print(versicolor_PetalLength)
virginica_PetalLength = data.loc[data.Species == 'virginica',['Species', 'PetalLength']]
print(virginica_PetalLength)

plt.figure(figsize=(10,6))
plt.hist(versicolor_PetalLength['PetalLength'], bins=5, alpha = 0.5, label='versicolor')
plt.hist(virginica_PetalLength['PetalLength'], bins=5, alpha = 0.5, label='virginica')

plt.xlabel('Petal')
plt.ylabel('Length')
plt.title('Iris Petal Group Histogram')
plt.legend()
plt.grid()
plt.show()