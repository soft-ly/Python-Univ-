import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('train.csv')

data.loc[data['Sex'] == 'male', ['Sex']] = 1
data.loc[data['Sex'] == 'female', ['Sex']] = 0

temp_data4 = data.loc[:,['Sex','Age','SibSp','Parch']]
plt.figure(figsize=(10,6))
plt.title('4x4 Heat Map Graph')
correlation_data4 = temp_data4.corr()
sns.heatmap(correlation_data4, annot=False, cmap='YlGnBu', mask)
plt.show()
