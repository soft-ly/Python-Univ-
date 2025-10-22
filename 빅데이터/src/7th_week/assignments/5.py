from sklearn.linear_model import LinearRegression as LR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('health_screenings_2020_1000ea.xlsx')
df.head()

x = df[['height']]
y = df['weight']

model = LR()
model.fit(x, y)

print('예상몸무게', model.predict([[185]]))

plt.plot(x, y, 'o')
plt.plot(x, model.predict(x.values.reshape(-1,1)))
plt.show()