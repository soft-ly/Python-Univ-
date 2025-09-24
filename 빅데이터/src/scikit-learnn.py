import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt

data = pd.read_csv("new/train.csv")
temp = np.array(data['Age'].fillna(0)).reshape(-1,1)

temp_scaler = StandardScaler()
temp_scaler.fit(temp)
before_data = temp_scaler.transform(temp)

plt.hist(data['Age'], bins=30, color='red', alpha = 0.7)
plt.title('before data scaling')
plt.show()
