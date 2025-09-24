import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt

data = pd.read_csv("new/train.csv")
temp = np.array(data['Age'].fillna(0)).reshape(-1,1)

temp_scaler = RobustScaler()
temp_scaler.fit(temp)
before_data = temp_scaler.transform(temp)

plt.hist(before_data, bins=30, color='red', alpha = 0.7)
plt.title('before data scaling')
plt.show()
