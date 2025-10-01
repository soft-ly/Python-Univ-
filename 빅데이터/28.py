import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iris_flower.csv')
print(data)

SepalLength = data['SepalLength']
SepalWidth = data['SepalWidth']

plt.figure(figsize=(10,6))
plt.boxplot([SepalLength, SepalWidth], tick_labels=['Sepal Length', 'Sepal Width'])

plt.xlabel('Sepal')
plt.ylabel('Value')
plt.title('Iris Sepal Box Plot')
plt.show()

