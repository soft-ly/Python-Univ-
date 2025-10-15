import pandas as pd

data = pd.read_csv('./new/train.csv')
class_group = data.groupby('Pclass')

print(class_group.count())
print(class_group['Survived'].mean())
print(class_group['Age'].max())