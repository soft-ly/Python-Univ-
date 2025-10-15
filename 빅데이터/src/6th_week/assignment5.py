import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('iris_flower.csv')

temp_data = data[['SepalLength','SepalWidth','PetalLength','PetalWidth']]

temp_data = temp_data.dropna(axis=0)
print(temp_data)
corr = temp_data.corr(method='pearson')
print(corr)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='Blues')
plt.show()

