import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('health_data.xlsx')
print(data)

temp_data = data.loc[:,['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]
temp_data.loc[temp_data['gender']==1, ['gender']] = 'M'
temp_data.loc[temp_data['gender']==2, ['gender']] = 'F'
temp_data.loc[temp_data['drinking']==0, ['drinking']] = 'Non-drinking'
temp_data.loc[temp_data['drinking']==1, ['drinking']] = 'Drinking' 
temp_data.loc[temp_data['smoking']==1, ['smoking']] = 'Non-smoking'
temp_data.loc[temp_data['smoking']==2, ['smoking']] = 'Quit-smoking'
temp_data.loc[temp_data['smoking']==3, ['smoking']] = 'Smoking'
print(temp_data)

drinking = temp_data.groupby(['gender', 'drinking'])['drinking'].count()
drinking = drinking.to_frame(name = 'count')
drinking = drinking.reset_index()
print(drinking)

smoking = temp_data.groupby(['gender', 'smoking'])['smoking'].count()
smoking = smoking.to_frame(name = 'count')
smoking = smoking.reset_index()
print(smoking)

temp_data3 = data.loc[:,['gender', 'drinking', 'smoking']]

plt.figure(figsize=(10,6))
plt.title('3x3 Heat Map Graph')

correlation_data3 = temp_data3.corr()
sns.heatmap(correlation_data3, annot=True, cmap='YlGnBu')
plt.show()