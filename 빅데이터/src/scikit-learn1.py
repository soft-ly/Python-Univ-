import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('new/train.csv')

le = LabelEncoder()
le.fit(data.Embarked)
print(le.transform(data.Embarked))