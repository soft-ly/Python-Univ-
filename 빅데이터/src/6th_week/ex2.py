import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('train.csv')
data = data.drop(['Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis=1)
data.loc[data['Sex'] == 'male','Sex'] = 0
data.loc[data['Sex'] == 'female','Sex'] = 1
data = data.dropna(axis=0)
print(data)

corr = data.corr(method='pearson')
print(corr)

mask = np.zeros_like(corr, dtype = np.bool)
mask[np.triu_indices_from(mask)] = True

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='Blues', mask=mask)
plt.show()