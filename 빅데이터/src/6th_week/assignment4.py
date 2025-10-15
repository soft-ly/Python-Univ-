import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('train.csv')
print(data.columns)
temp_data = data[['Age','Sex','Survived']]

temp_data.loc[temp_data['Sex'] == 'male', 'Sex'] = 0
temp_data.loc[temp_data['Sex'] == 'female', 'Sex'] = 1

temp_data.loc[temp_data['Age'].between(0,10), 'Age'] = 0
temp_data.loc[temp_data['Age'].between(11,20), 'Age'] = 1
temp_data.loc[temp_data['Age'].between(21,30), 'Age'] = 2
temp_data.loc[temp_data['Age'].between(31,40), 'Age'] = 3
temp_data.loc[temp_data['Age'].between(41,50), 'Age'] = 4
temp_data.loc[temp_data['Age'].between(51,60), 'Age'] = 5
temp_data.loc[temp_data['Age'].between(61,70), 'Age'] = 6
temp_data.loc[temp_data['Age'].between(71,80), 'Age'] = 7

temp_data = temp_data.dropna(axis=0)
print(temp_data)
corr = temp_data.corr(method='pearson')
print(corr)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='Blues')
plt.show()