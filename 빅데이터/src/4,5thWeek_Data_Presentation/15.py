import pandas as pd

data = pd.read_csv('new/train.csv')

q1 = data['Age'].quantile(0.25)
q3 = data['Age'].quantile(0.75)
iqr = (q3 - q1)

df_drop_outliers = data[(data['Age'] <= (q3 + 1.5*iqr)) & (data['Age'] >= (q1 - 1.5*iqr))]

print(len(data['Age']))
print(len(df_drop_outliers))
