import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = datasets.load_diabetes()
df = pd.DataFrame(data['data'], index=data['target'], columns=data['feature_names'])
print(df)

x = df.bmi.values
y = df.index.values

X = x.reshape(-1, 1)
Y = y.reshape(-1, 1)

lr = LinearRegression()
lr.fit(X, Y)

Y2 = lr.coef_[0]*X + lr.intercept_

plt.scatter(X, Y)

plt.plot(X, Y2, color='red')
plt.title('diabetes progression vs BMI')
plt.show()
