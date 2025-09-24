# 이상치 확인

import pandas as pd

data = pd.read_csv('train.csv')

temp_data = data['Age']

z_score = (data['Age'] - data['Age'].mean()) / data['Age'].std()
df_drop_outliers = temp_data[abs(z_score) <= 0.95]

print(len(data['Age']))
print(len(df_drop_outliers))