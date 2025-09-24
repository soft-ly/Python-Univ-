import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('new/train.csv')
temp = np.array(data['Embarked']).reshape(-1,1)

le = OneHotEncoder()
le.fit(temp)
print(le.transform(temp).toarray())