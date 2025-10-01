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

male_data = temp_data.loc[temp_data.gender == 'M', ['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]
female_data = temp_data.loc[temp_data.gender == 'F', ['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]
print(male_data)
print(female_data)

plt.figure(figsize=(10,5))
plt.title('Seaborn Strip Plot Graph')

#sns.stripplot(x = 'height', y = 'weight', data=male_data, palette=sns.color_palette())
sns.stripplot(x = 'height', y = 'weight', data=female_data, palette=sns.color_palette())
plt.show()