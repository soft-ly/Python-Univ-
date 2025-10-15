import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('train.csv')
print(data.columns)
temp_data = data[['Age', 'Sex', 'Survived']]
temp_data.loc[data['Sex'] == 'male','Sex'] = 0
temp_data.loc[data['Sex'] == 'female','Sex'] = 1
temp_data = temp_data.dropna(axis=0)
print(temp_data)

corr = temp_data.corr(method='pearson')
print(corr)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='Blues')
plt.show()
    